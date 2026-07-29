# M16 · Building the Perception Stack: Let the Robot See Where the Cup Is

**Global Position**: After the arm and end-effector are ready (M15), before teleoperation data collection (M17). The input is the assembled sensor hardware, and the output is a **calibrated vision/localization stack** — give it a scene, and it outputs the 3D pose of the target object and the robot's own position. This output is a common consumer for M17 data collection, M18 imitation learning, and M19 task planning.

**Prerequisites**: The URDF from M10 plus the arm from M15 make the full-body TF tree available; sensors have been purchased or are on the procurement list (selection basis in [Sensor Selection Handbook](../playbooks/sensor-selection.md)); the onboard computing platform is ready ([Compute Platform Selection Handbook](../playbooks/compute-selection.md)).

Theoretical background: [Chapter 5: Sensing and Perception Hardware](/wiki/chapters/chapter-05/) covers sensor principles, [Chapter 22: Software Middleware](/wiki/chapters/chapter-22/) covers the communication skeleton; this task is to weave them into a "pixels → 3D pose" pipeline.

## Step 1: Define the Sensor Configuration Plan

【What to do】Define three tiers of configurations based on the task and write them into the procurement and installation checklist:

1.  **Primary Vision (Required)**: One [RGB-D camera](/entry/ent_component_rgbd_camera/) on the head/chest. Mainstream options: [Intel RealSense](/entry/ent_component_intel_realsense_depth_camera_2024/) D435i (~USD 199, range 0.1–10 m, built-in IMU — official datasheet spec) or D455 (~USD 299, depth accuracy <2% @ 4 m, global shutter — card spec); for onboard depth and spatial AI, consider the [ZED Stereo Camera](/entry/ent_component_zed_stereo_camera_2024/) (depth computation relies on host GPU ecosystem, price needs to be confirmed with the supplier).
2.  **Wrist Close-up Camera (Strongly Recommended)**: One small RGB camera on each wrist. The wrist perspective is a key source of operational data — the last 10 cm of grasping, where the head camera is often blocked by the robot's own arm.
3.  **360° LiDAR (Only for Navigation)**: For indoor cross-room navigation, add the [Livox Mid-360](/entry/ent_component_livox_mid_360_lidar_2024/) (~CNY 3,999, 265 g, 40 m @ 10% reflectivity, built-in IMU — official datasheet/card spec), used for SLAM localization.

Simultaneously, perform a **USB bandwidth budget**: A single D435i with depth + RGB fully enabled has a data flow on the order of hundreds of MB/s (engineering recommendation, measure based on your resolution/frame rate); multiple cameras on the same USB controller will compete for bandwidth and drop frames — allocate "one camera per USB 3 controller", or reduce resolution/frame rate.

【Why】There are three routes for depth acquisition: structured light/active stereo (good indoor close-range accuracy, sensitive to strong light), ToF, passive stereo (works in sunlight but relies on texture). Trade-offs are in the [RGB-D card](/entry/ent_component_rgbd_camera/). Anchor: [ToddlerBot](/entry/ent_robot_system_toddlerbot/) uses dual fisheye cameras + chest IMU ([ToddlerBot Project Page](https://toddlerbot.github.io/)); D435i is used as head vision on platforms like Qinglong, G1, etc. (Sensor Selection Handbook).

【How to analyze your situation】Only doing "fixed stance + tabletop grasping": one D435i + wrist cameras are sufficient; LiDAR is a pure waste. Need to walk to the table and then grasp: add Mid-360. Budget limit: start with a single D435i, add wrist cameras later, but mechanically reserve the mounting positions and cable routing.

## Step 2: Drivers, Time Synchronization, and TF Tree Integration

【What to do】

1.  Install [ROS 2](/entry/ent_software_ros_2_middleware_2024/) drivers (RealSense uses the official ROS 2 wrapper, Livox uses the official driver), check topic by topic: `ros2 topic hz` to confirm frame rate meets requirements, `ros2 topic echo` to see if timestamps are monotonically increasing.
2.  **Time Synchronization**: Sensors on the same main controller use the system clock for timestamps; when deploying with a main controller and Jetson dual-machine, use chrony/NTP for time synchronization (millisecond level, engineering recommendation); for VIO/multi-sensor fusion, use PTP or hardware triggering.
3.  **TF Tree Integration**: Attach each sensor's frame into the full-body TF tree from M15 (add fixed joint in URDF, or publish static transform in launch file), use `tf2_tools view_frames` to check the entire tree is connected without islands.

【Why】All algorithms for multi-sensor fusion assume "extrinsics known, clocks synchronized". A 30 ms timestamp difference causes ghosting in motion fusion results — VIO diverges, point cloud coloring is misaligned (Section 3 of [Sensor Selection Handbook](../playbooks/sensor-selection.md)). If dual-machine time synchronization is not done well, images and joint states won't match, and the data collected in M17 will be directly unusable.

【How to analyze your situation】Single-machine deployment + single camera: this step can be done in half a day. Dual-machine (main controller + Jetson): complete time synchronization before proceeding further; don't move forward with a 50 ms clock offset — every subsequent step will be contaminated by it.

## Step 3: Calibration Chain — Intrinsics, Hand-Eye, Multi-Sensor Joint

【What to do】Perform three levels of calibration in order, all scripted into a one-click script and archived:

1.  **Camera Intrinsics**: Collect 20+ images of a checkerboard/dot grid board from multiple poses, calibration tool outputs fx/fy/cx/cy and distortion coefficients, **reprojection error < 0.5 px level** (engineering recommendation, based on calibration tool report spec) before finishing.
2.  **Hand-Eye Calibration**: Eye-to-hand (head camera relative to base) or eye-in-hand (wrist camera relative to end-effector), essentially solving AX=XB: move the calibration board through 10–15 different poses relative to the camera (ensure sufficient rotation), solve for the transformation from camera to robot frame.
3.  **Camera-LiDAR-IMU Joint Calibration** (only if LiDAR is installed): Process in [Joint Calibration](/entry/ent_method_calibration_joint_camera_imu/) card: collect multiple poses of calibration target → detect corners in camera + extract planes from LiDAR → initial value + ICP/nonlinear optimization → reprojection error verification.

Iron Rule: **Must recalibrate after any disassembly, collision, or transport**. Acceptance for this step: RGB point cloud coloring has no obvious misalignment, reprojection error < 2 px (Stage 3 criterion).

【Why】Manipulation is essentially a coordinate transformation chain: pixels → camera frame → base frame → end-effector. If any link's extrinsics are wrong, you grasp at air (Stage 3 original text). If calibration is not scripted, you'll spend a day recalling how to adjust parameters after every disassembly.

【How to analyze your situation】Only doing tabletop grasping: complete steps 1+2 is sufficient; leave LiDAR joint calibration for when navigation is unlocked. Archive calibration results with date and version number — the dataset card for M17 must include the calibration version; mismatched data and calibration means wasted collection.

## Step 4: Perception Algorithm Pipeline — From Point Cloud to Object Pose

【What to do】Build a four-level pipeline:

1.  **Point Cloud Preprocessing**: Voxel downsampling → Pass-through filtering (keep only the tabletop workspace) → Plane segmentation (remove the tabletop). Parameters are tuned based on actual measurements of table height and camera mounting angle.
2.  **Two Paths for Object Detection**:
    - Geometric method: cup ≈ cylinder, RANSAC cylinder fitting, zero training cost, ready to use immediately;
    - Learning method: detection/segmentation model outputs masks, no need to rewrite geometric assumptions when changing object categories.
3.  **6D Pose**: Geometric method directly gives pose from fitting parameters; learning method can connect to a 6D pose estimation model (first version can use "mask center point + principal axis direction" approximation).
4.  **Output Definition** (frozen as an interface): `{object category, 3D pose, confidence}`, publish frequency **10–30 Hz** (engineering recommendation, measure based on compute power).

【Why】Always use the geometric method for the first version: it gives you an end-to-end baseline with zero training data and can also provide automatic annotations for the learning method. Once the output interface is frozen, M17/M18/M19 only recognize this definition; later algorithm changes won't affect downstream.

【How to analyze your situation】Only one type of cup in the scene: the geometric method is sufficient; focus effort on calibration and localization. Need to generalize to multiple objects: start with the learning method, but first use geometric method results as coarse annotations; don't start manually labeling hundreds of images.

## Step 5: Localization – Where the Robot Is

[What to Do] Three gears to choose based on the task:

| Gear | Solution | Applicable Scenario |
|---|---|---|
| Leg Odometry | Joint encoder kinematics + torso [IMU](/entry/ent_component_imu_2024/) fusion | Stationary operation, short-distance shuffling |
| VIO | Camera + IMU visual-inertial odometry (D435i built-in IMU can save an external one) | Indoor fixed room, sufficient texture |
| LiDAR SLAM | Mid-360 + built-in IMU for LIO | Cross-room navigation, long distance |

**Drift Quantification**: Have the robot walk a closed-loop path back to the origin (or a marker), measure the deviation of the final pose from the origin, and divide by the path length to get the relative drift rate – this number must be included in the acceptance criteria.

[Why] For fixed-room desktop grasping, RGB-D odometry-level accuracy is sufficient (Stage 3 scope); cross-room reliance solely on proprioception will cause drift to the point of grasping air. For open-source references, see [ORB-SLAM3](/entry/ent_paper_orb_slam3_an_accurate_open_sou_2026/) and [VINS-Fusion](/entry/ent_paper_vins_fusion_an_optimization_ba_2026/) paper cards.

[How to Analyze Your Situation] In the first phase (stationary grasping), only retain leg odometry + visual servoing closed loop; localization errors are absorbed by the "visible servo". Only add VIO/LIO after unlocking walking; do not stack all three gears at once.

## Step 6: Compute Allocation and Engineering

[What to Do]

1. **Perception runs on Layer 2**: All vision/SLAM nodes are deployed on the intelligent layer (e.g., [Jetson AGX Orin](/entry/ent_component_nvidia_jetson_agx_orin_2024/), up to 275 TOPS @ 64 GB version, 15–60 W, dev kit approx. USD 1,999 – card scope), isolated from the control loop processes; machine-level isolation is better.
2. **Failure Drill**: Manually kill all perception processes; the control loop must not be interrupted, and the robot must enter a safe state (Stage 3 acceptance criterion).
3. **Frequency/Latency Budget Table** (engineering recommendations, verify with actual measurements):

| Node | Target Frequency | Single-Frame Latency Budget |
|---|---|---|
| Camera Driver | 30 Hz | — |
| Point Cloud Preprocessing | 15–30 Hz | < 30 ms |
| Detection + Pose | 10–30 Hz | < 100 ms |
| Localization | 10–100 Hz (depends on gear) | < 50 ms |

4. **Resource Monitoring**: CPU/GPU/memory/temperature must be continuously monitored. ToddlerBot's actual onboard inference experienced thermal throttling after 19 minutes (research archive) – heat is a hidden budget for perception.

[Why] The control loop requires determinism, perception requires throughput; running them together causes mutual degradation (see the layered logic in the [Compute Platform Selection Manual](../playbooks/compute-selection.md)). A separate process architecture ensures that even if perception crashes, the control can still safely shut down (Stage 3, Step 14).

[How to Analyze Your Situation] With only one motherboard: at least achieve process isolation + lower perception process priority + watchdog; if possible, use a dual-computer setup (main controller + Jetson) – ToddlerBot uses Orin NX 16GB to run a 300M parameter diffusion policy with ~100 ms latency, 10 Hz onboard stereo depth estimation (research archive), proving this scale is sufficient for perception + small policies.

## Acceptance Criteria

- [ ] Sensor configuration document created: each sensor has mounting position, interface, bandwidth budget; no USB controller allocation conflicts.
- [ ] All topic frame rates/timestamps verified; dual-computer deployment has clock synchronization records.
- [ ] Camera intrinsic reprojection error < 0.5 px and archived; hand-eye calibration completed; one-click calibration script stored in repository, and re-calibration process after disassembly rehearsed.
- [ ] RGB point cloud coloring shows no obvious misalignment (reprojection < 2 px, Stage 3 criterion).
- [ ] Cup 3D localization error ≤ 1 cm @ desktop distance (Stage 3 criterion), repeated 10 times with distribution recorded.
- [ ] Localization return-to-origin deviation quantified (path length vs. deviation), documented in acceptance report.
- [ ] After killing perception processes, control loop is not interrupted, robot enters safe state (actual test video archived).

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Depth stream frame drops with multiple cameras | Insufficient USB bandwidth, multiple cameras contending for the same controller | `lsusb -t` to check controller topology; reduce resolution/frame rate; assign to separate controllers |
| Point cloud coloring misaligned, ghosting | Camera-LiDAR extrinsic parameters outdated (after collision) / timestamp offset not calibrated | Re-run joint calibration and check reprojection error; verify timestamp source consistency |
| Hand-eye calibration always misaligned | Insufficient rotation in collected poses / timestamp misalignment | Increase pose diversity (especially rotation); check time synchronization first, then re-calibrate |
| Large depth holes on transparent/reflective objects | Inherent limitation of structured light / active IR methods | Change viewing angle; apply matte powder; switch to passive stereo or learning-based depth |
| Depth failure in sunlight | Active IR overwhelmed by sunlight | Use indoors or with shading; for outdoor tasks, switch to LiDAR/passive methods |
| RViz reports TF break | Inconsistent frame names / static transform not published | Use `tf2_tools view_frames` to find orphan frames; cross-check against M15 naming convention |
| Perception frequency drops after a few minutes | Thermal throttling (ToddlerBot precedent at 19 minutes) | Monitor temperature curve; lower power mode; improve cooling airflow |

## Companion Reading

- Previous Task: [M15 · Upper Body and End Effector](m15-upper-body.md)
- Next Task: [M17 · Teleoperation and Data Collection](m17-teleop-data.md)
- Theoretical Background: [Chapter 5 Sensing and Perception Hardware](/wiki/chapters/chapter-05/), [Chapter 22 Software Middleware](/wiki/chapters/chapter-22/), [Chapter 11 Assembly, Integration, and Testing](/wiki/chapters/chapter-11/)
- [Sensor Selection Manual](../playbooks/sensor-selection.md) · [Compute Platform Selection Manual](../playbooks/compute-selection.md) · [Stage 3 Overview](../stage-3-humanoid.md)
