# Selection Guide: How to Choose a Sensor

A common mistake in sensor selection is "matching the whole machine manufacturer's promotional video": buying a RealSense, a six-axis force/torque sensor, and a tactile array, only to find that the data cannot be processed in time, or that the control frequency is throttled by the USB bandwidth after purchase. This guide takes the opposite approach: first, break down the tasks your robot must accomplish into "what physical quantities must be known," then select sensors that are just sufficient for each type of physical quantity. For background principles, see [Chapter 5: Sensing and Perception Hardware](/wiki/chapters/chapter-05/); for the supplier landscape, see [Chapter 7: Supplier Map](/wiki/chapters/chapter-07/).

## 1. Perception Requirement Decomposition: What Must Your Robot "Know"

Divide sensors into three layers and answer "Do I really need this?" layer by layer:

### Layer 1: Proprioception — Joint Angles and Body Posture

[What to do] List the position feedback scheme for each active joint (motor-side encoder, output-side encoder, or dual encoders), as well as the IMU configuration for the torso/feet (how many units, sampling rate).

[Why] Proprioception is the lifeline of the control loop; without it, the robot doesn't even know "where its own legs are." [Joint Encoder](/entry/ent_component_joint_encoder_2024/) provides high-resolution position feedback for motor control; notably, "where it is mounted" matters: the motor-side encoder cannot see reducer backlash and flexible deformation, so platforms requiring precision force control add an output-side encoder to form dual encoders — the BLMC actuator from the Open Dynamic Robot Initiative uses a "dual encoder (motor-side/output-side)" design (source: research file open-dynamic-robot-initiative.md). Low-budget solutions also exist: Berkeley Humanoid Lite uses a $3 AS5600 magnetic encoder (source: research file berkeley-humanoid-lite.md), and the torso posture uses a single phone-grade BNO085 IMU to achieve zero-shot sim-to-real walking (same file). [IMU](/entry/ent_component_imu_2024/) is responsible for attitude estimation, fusing with encoders and vision to provide high-frequency inertial reference.

[How to analyze your situation] For position-controlled servo solutions (e.g., Dynamixel), the encoder is built-in, so this layer is solved at zero cost. For self-developed QDD joints, at least a motor-side encoder is needed; whether an output-side encoder is required depends on whether you are doing force control (yes → needed). One torso-level IMU is sufficient to start; for dynamic walking research, adding an IMU or ground contact sensor to the feet is recommended — the BRUCE biped robot runs the IMU sampling at 2 kHz for this purpose (source: research file bruce-westwood.md).

### Layer 2: Force Sensing — End-Effector Force, Ankle Force, Fingertip Tactile

[What to do] Decide three things: whether the wrist/ankle needs a [Six-axis F/T Sensor](/entry/ent_component_six_axis_force_torque_sensor_2024/) (which flange to mount, what range); whether the dexterous fingertip needs a [Tactile Sensor Array](/entry/ent_component_tactile_sensor_array_2024/); or whether to first use the actuator current loop to estimate force as a substitute.

[Why] The six-axis force/torque sensor simultaneously measures three-axis forces and three-axis torques, making it a staple for force-controlled assembly, drag teaching, and biped ankle ZMP estimation — THORMANG3 mounts one ATI Mini58 on each ankle (source: research file thormang3.md). However, it is one of the most expensive sensors on the entire robot, and range and precision conflict (buying a larger range wastes resolution). The tactile array measures contact pressure/shear/texture, supporting slip detection for dexterous manipulation; when the budget is tight, an FSR array can be used as an entry point — the Poppy humanoid robot in 2014 was configured with 16 FSR force sensors (source: research file poppy-humanoid.md).

[How to analyze your situation] Only doing walking, not manipulation → current loop force estimation + foot-end switch-type contact sensing is sufficient, saving the cost of a six-axis force/torque sensor. Doing assembly/grinding-type manipulation research → a wrist six-axis force/torque sensor is worth investing in, with the range selected as "maximum contact force × 2." Doing dexterous hand grasping research → tactile array takes priority over wrist six-axis force/torque sensor, because grasping slip mainly occurs at the fingertips.

### Layer 3: Exteroception — Seeing the Outside World

[What to do] Clarify the type of exteroception task: close-range manipulation scene understanding (0.3–3 m), indoor navigation and mapping (3–20 m), or outdoor/large spaces. These three correspond to completely different sensors.

[Why] [RGB-D Camera](/entry/ent_component_rgbd_camera/) has three depth routes — structured light, ToF, and binocular stereo — each with applicable distance and lighting constraints: structured light has high precision but is afraid of strong light; binocular is passive but relies on texture. The mainstream for head vision is [Intel RealSense](/entry/ent_component_intel_realsense_depth_camera_2024/) (D435i/D455 adopted by platforms like Qinglong and G1, source: openloong-qinglong research file, Unitree card); the main force for navigation and mapping is LiDAR, with [Livox Mid-360](/entry/ent_component_livox_mid_360_lidar_2024/) offering 360° surround view at 265 g, a popular choice for quadruped/humanoid SLAM (source: Livox card).

[How to analyze your situation] Only doing desktop grasping → one RGB-D camera is enough; LiDAR is a waste. Doing indoor walking navigation → RGB-D (close-range obstacle avoidance) + 360° LiDAR (mapping) is a mature combination. Pure vision research (VLA, visual servoing) → spend the budget on camera frame rate and global shutter, rather than stacking LiDARs.

## II. Component Selection Table: Key Indicators → How They Affect Your Robot → Price Range

### Encoder

| Key Indicator | How It Affects Your Robot | Price Range Reference |
|---|---|---|
| Resolution (Bits) | Determines position control accuracy and speed estimation quality; joints above 17 bits can achieve smooth low-speed force control | Magnetic encoder AS5600 (12 bit) approx. $3 (BHL archive); high-resolution optical/absolute types require inquiry |
| Absolute vs Incremental | Absolute type knows angle on power-up; with many humanoid robot joints, incremental type requires painful homing each time | Absolute type is expensive, choose as needed |
| Mounting End (Motor Side / Output Side) | Output-side encoder lets you "see" reducer backlash and flexspline deformation, a prerequisite for force control transparency | Dual encoder = double cost, worth it for force control platforms (ODRI archive) |

### IMU

| Key Indicator | How It Affects Your Robot | Price Range Reference |
|---|---|---|
| Gyro Bias Stability | Determines attitude integration drift speed; [IMU Card](/entry/ent_component_imu_2024/) example ADIS16475 is 2°/hr (in operation) | Phone-grade (BNO085, used by BHL) tens of yuan; industrial MEMS (ADIS16475 class) price undisclosed, requires inquiry; FOG-grade separate |
| Angular Random Walk (ARW) | Noise directly enters attitude estimation; ADIS16475 is 0.15°/√hr | Same as above |
| Inter-axis Alignment Error | Installation alignment workload for multi-sensor fusion; ADIS16475 ±0.1° factory calibrated | Low-end IMU requires self-calibration |
| Sampling Rate / Interface | Balance control loop requires high-frequency attitude; SPI has lower latency than I²C; ADIS16475 uses SPI | BRUCE achieves 2 kHz (archive) |

### 6-Axis Force/Torque Sensor

| Key Indicator | How It Affects Your Robot | Price Range Reference |
|---|---|---|
| Range (F/M) | Select based on "maximum contact force × 2"; Shenyuansheng MLL typical 50/50/100 N, 2/2/4 N·m; [OnRobot HEX-E QC](/entry/ent_component_ati_force_torque_sensor_2024/) ±100/±200 N, ±10 N·m (source: two cards) | Domestic analog type (MLL class) requires inquiry; imported ATI Nano25 (±250 N) class significantly more expensive |
| Accuracy / Crosstalk Error | Determines credibility of decoupled 6-axis force control; MLL accuracy ≤0.5% FS, crosstalk error ≤2% FS | Higher accuracy models are more expensive |
| Overload Capacity | Biped ankles inevitably experience impacts; MLL ≥300% FS, HEX-E approx. 500% FS | Overload margin = lifespan |
| Sampling Rate & Interface | Force control loop requires ≥1 kHz; MLL max 1000 Hz (with data acquisition unit), HEX-E uses EtherNet/IP and other industrial buses | Data acquisition unit / bus gateway cost extra |

### Tactile Array

| Key Indicator | How It Affects Your Robot | Price Range Reference |
|---|---|---|
| Spatial Resolution (Taxel Density) | Determines ability to discern contact shape and texture, supporting slip prediction | Discrete FSR points are cheapest (Poppy uses 16 points); array type requires inquiry |
| Measurement Dimension | Normal pressure only vs triaxial force (including shear) – shear is a precursor to slip | Triaxial arrays are much more expensive, only needed for grasping research |
| Curved Surface Attachment & Wiring | Curved fingertip mounting and wiring are major engineering challenges, often more labor-intensive than the sensor itself | Evaluate flexible PCB solutions |

### RGB-D Camera (RealSense vs ZED)

| Key Indicator | How It Affects Your Robot | Price Range Reference |
|---|---|---|
| Ideal Range & Accuracy | Manipulation scenarios focus on 0.3–1 m accuracy: [RealSense](/entry/ent_component_intel_realsense_depth_camera_2024/) D435i is 0.1–10 m, <2% @2 m; D455 is 0.6–6 m, <2% @4 m (source: RealSense card, official datasheet) | D435i approx. USD 199, D455 approx. USD 299 (public market reference, card specification) |
| Shutter Type | Head is moving; global shutter (D455) avoids rolling shutter distortion | Generally, global shutter models are slightly more expensive |
| Built-in IMU | Visual-Inertial Odometry (VIO) saves an external IMU: D435i has built-in BMI055 | Only 'i' suffix models have it |
| Compute Dependency | [ZED Stereo Camera](/entry/ent_component_zed_stereo_camera_2024/) onboard depth + spatial AI, but depth computation relies on host GPU ecosystem (source: ZED card); price needs confirmation with supplier | RealSense ecosystem (librealsense+ROS) has zero compute barrier; ZED requires NVIDIA host |

### LiDAR

| Key Indicator | How It Affects Your Robot | Price Range Reference |
|---|---|---|
| FOV | [Livox Mid-360](/entry/ent_component_livox_mid_360_lidar_2024/) horizontal 360°, vertical -7°~52°, one unit covers torso surround view (source: Livox card) | Mid-360 approx. CNY 3,999 (official store, card specification) |
| Detection Range & Accuracy | 40 m @10% reflectivity, ≤2 cm @10 m – more than sufficient for indoor navigation and mapping | Same as left |
| Point Rate & Frame Rate | 200,000 points/sec, 10 Hz, determines dynamic scene update rate | Same as left |
| Weight / Power Consumption | 265 g, 6.5 W, acceptable for head/torso; built-in ICM40609 IMU enables LIO | Same as left |

## III. Calibration and Time Synchronization: Buying the Right Sensor is Only Half the Job

[What to Do] Develop a calibration plan: camera intrinsics (checkerboard), camera-LiDAR extrinsics, camera-IMU extrinsics and time offset, joint zero positions, and agree on a unified time source (PTP or hardware trigger).

[Why] All algorithms for multi-sensor fusion assume "extrinsics known, clocks synchronized." The [Joint-Camera-IMU Calibration](/entry/ent_method_calibration_joint_camera_imu/) card provides the standard procedure: collect calibration target in multiple poses → camera detects corners + LiDAR extracts planes/corners → PnP initial value + ICP/nonlinear optimization → minimize reprojection error for verification; when no calibration target is available, scene edge alignment or mutual information methods can be used for online refinement. If time offset is not calibrated properly, the fusion result during motion becomes a "ghost image"; VIO divergence and point cloud coloring misalignment both stem from this. See [Chapter 11: Assembly, Integration, and Testing](/wiki/chapters/chapter-11/) for systematic integration and testing methods.

[How to Analyze Your Situation] Starting with a single RGB-D only requires camera intrinsics; adding LiDAR necessitates camera-LiDAR extrinsics (the card method can be directly applied); performing VIO/multi-IMU fusion then requires time calibration. Use reprojection error as the acceptance criterion, don't rely on visual "looks roughly aligned."

## IV. Two Recommended Configurations

### Beginner Minimal Kit (Goal: Walk, See, Survive Falls)

- Joint Feedback: Smart servo built-in encoder, or self-developed joint using AS5600-class magnetic encoder ($3/unit, BHL archive specification).
- Attitude: One phone-grade IMU (BNO085 class), first get attitude estimation working.
- External Perception: One RealSense D435i (approx. USD 199, card specification) – depth + RGB + IMU all-in-one, most mature ecosystem.
- Force Sensing: Skip initially, use current loop for force estimation; foot end can use switch/FSR for ground contact detection.
- Analysis Logic: This setup spends every dollar on "essentials for control loop closure," sufficient for walking and grasping demos; upgrade item by item when bottlenecks become clear (large attitude drift, inability to detect grasp slip).

### Research-Grade Kit (Goal: Force Control / Manipulation / Navigation Paper-Quality Data)

- Joint Feedback: Dual encoder (motor side + output side), output side uses high-resolution absolute type.
- Attitude: Industrial MEMS IMU (ADIS16475 class: ARW 0.15°/√hr, bias 2°/hr, ±0.1° alignment, card specification) + distributed placement on torso/feet, sampling towards 1–2 kHz.
- Force Sensing: Wrist 6-axis force (domestic MLL class or ATI/OnRobot class) + biped ankle 6-axis force (THORMANG3 configuration precedent), dexterous hand adds tactile array.
- External Perception: RealSense D455 (global shutter, approx. USD 299) or ZED (when GPU host is available) + Livox Mid-360 (approx. CNY 3,999) for 360° mapping.
- Calibration: Full set of intrinsic/extrinsic/time synchronization calibration, reprojection error included in acceptance.
- Analysis Logic: The core of research-grade is "data credibility" – expensive sensors are not the goal; calibratability, traceability, and clock synchronization are.

## Acceptance Criteria

- Have a list of "physical quantity → sensor → mounting location → interface → sampling rate," able to answer "what happens without it" for each item.
- Key indicators (range/accuracy/bandwidth) of each sensor correspond one-to-one with task requirements and are traceable to cards or datasheets; items without public prices are marked "requires confirmation with supplier."
- Calibration plan implemented: camera intrinsics completed; if LiDAR is installed, camera-LiDAR extrinsics completed and reprojection error recorded.
- Timestamps of all sensors unified to the same clock source; fusion nodes show no visually apparent temporal misalignment.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Slow drift in pose estimation, increasingly skewed | Insufficient IMU bias stability or lack of temperature compensation calibration | Check bias stability indicators; estimate bias while stationary, upgrade to industrial-grade IMU if necessary |
| VIO/fusion divergence during walking | Camera-IMU time offset not calibrated | Perform time synchronization calibration; verify timestamp source consistency |
| Point cloud coloring misalignment, ghosting | Camera-LiDAR extrinsic parameters outdated (after collision) | Re-perform multi-pose calibration, check if reprojection error converges |
| Six-axis force reading zero drift | Temperature drift or tare not performed; installation stress interference | Tare after power-on warm-up; check flange preload |
| Six-axis force range always saturated | Range selected based on "typical force" rather than "impact × 2" | Verify ankle impact peak values; switch to larger range or add overload protection strategy |
| Large depth map voids in sunlight | Structured light/active IR susceptible to strong light (inherent to the approach) | Check depth technology approach; switch to passive binocular or LiDAR for outdoor use |
| High noise in tactile array data | Lead wire bending interference, power supply ripple | Secure lead wire routing; check power supply with oscilloscope, add filtering |

## Companion Reading

- [Stage 3 · Full Humanoid](../stage-3-humanoid.md) — Perception Stack Integration and Calibration Practice
- [Stage 2 · Biped Platform](../stage-2-biped.md) — Role of Proprioceptive Sensors in Balance Control
- [Roadmap Overview](../index.md)
