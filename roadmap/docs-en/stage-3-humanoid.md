# Phase 3: Full Humanoid Robot – From Bipedal Platform to "Hear, Walk, Grasp"

> ⚠️ The content of this roadmap is compiled based on public information and theoretical knowledge, and has not been verified on actual hardware; please verify safety specifications yourself when involving electrical and mechanical operations.

After Phase 2's biped can walk stably, Phase 3 adds an "upper body" on top: arms, end effectors, perception, computing power, and an intelligence layer, completing an end-to-end task – **hear a command → walk to the table → pick up a cup**. Each step is expanded in a three-part format: "What to do → Why → How to analyze your situation", tailored by budget/scenario/skills.

## 3.1 Upper Body and Arms: 7-DOF Arm and Kinematics

**Step 1: Determine Configuration and Full Robot Model**
- 【What to do】Select an arm solution: standard 7 degrees of freedom per arm (shoulder 3, elbow 1, wrist 3). First, build a URDF in simulation to confirm no interference, then either purchase or build using actuators from Phase 1/2.
- 【Why】A [7-DOF robotic arm](/entry/ent_component_7dof_arm_2024/) mimics the redundancy of a human arm: 6 DOF can only "reach" a pose, while the 7th allows the elbow to rotate even when the end effector is stationary, enabling obstacle avoidance and singularity avoidance. Torque/weight/price **must be confirmed with the supplier** (see [Chapter 4](/wiki/chapters/chapter-04/) for selection).
- 【How to analyze your situation】For desktop grasping only: start with a single arm or even 6 DOF; dual-arm coordination and obstacle avoidance require 7 DOF. Simulate first, then machine metal parts.

**Step 2: Kinematics and Coordinate Frames**
- 【What to do】Implement [Forward Kinematics (FK)](/entry/ent_method_forward_kinematics/) (homogeneous transformation chain/product of exponentials) and [Inverse Kinematics (IK)](/entry/ent_method_inverse_kinematics/) (Jacobian pseudo-inverse numerical solution or geometric analytical solution); for 7-DOF IK, add secondary objectives in the null space (raise elbow, avoid joint limits). Then integrate the arm into the full robot URDF, unifying the entire TF transform tree.
- 【Why】After vision provides the cup's position, FK converts coordinate frames and IK calculates joint angles; numerical IK can diverge near singularities, with the standard solution being damped least squares. A humanoid has no fixed base, so end-effector accuracy = arm accuracy + torso posture error + foot slip error combined.
- 【How to analyze your situation】Directly use mature IK solvers from the ROS ecosystem; verification sequence: simulation spot check → no load → with load. If walking is unstable, "stand still first, then operate."

## 3.2 End Effector: Starting with a Gripper

**Step 3: Start with a Gripper, Reserve Dexterous Hand Interface**
- 【What to do】The first version uses an electric parallel gripper to grasp cups; design the interface to be replaceable, allowing future upgrades to a [LEAP Hand](/entry/ent_component_leap_hand/) or [Allegro Hand](/entry/ent_component_allegro_hand/).
- 【Why】[Dexterous hand](/entry/ent_component_dexterous_hand_2024/) vs. gripper: the former has high degrees of freedom but complex control and high cost, while the latter is simple and cheap but has limited grasping types. LEAP is a low-cost, open-source 16-DOF anthropomorphic hand (direct-drive Dynamixel + 3D printing, BOM must be confirmed with the project team); Allegro is a commercial 16-DOF four-finger hand from Wonik (torque-controlled joints, ROS compatible, price must be confirmed with the supplier). For tasks like grasping cups, a gripper's success rate is far higher than a poorly tuned dexterous hand.
- 【How to analyze your situation】Use a gripper to get the end-to-end pipeline running; start with LEAP for manipulation learning papers; choose Allegro for commercial reliability.

## 3.3 Perception Stack: RGB-D, LiDAR, and Calibration

**Step 4: Depth Camera**
- 【What to do】Install one [RGB-D camera](/entry/ent_component_rgbd_camera/) on the head/chest for primary vision, and reserve a wrist-mounted camera position for close-up vision. Mainstream options: [Intel RealSense](/entry/ent_component_intel_realsense_depth_camera_2024/) D435i (approx. USD 199, range 0.1–10 m, with IMU – official datasheet) or D455 (approx. USD 299, depth accuracy <2% @ 4 m); for onboard depth estimation, consider the [ZED Stereo Camera](/entry/ent_component_zed_stereo_camera_2024/) (price must be confirmed with the supplier).
- 【Why】Depth acquisition has three routes: structured light, ToF, and stereo vision (see RGB-D card); the D435i's minimum range of 0.1 m is suitable for desktop manipulation, and the wrist camera is a key source of manipulation data.
- 【How to analyze your situation】Start with one D435i on a tight budget; be mindful of USB bandwidth for multiple cameras (see common pitfalls).

**Step 5: LiDAR**
- 【What to do】If the task includes indoor navigation, install a 360° LiDAR, such as the [Livox Mid-360](/entry/ent_component_livox_mid_360_lidar_2024/) (approx. CNY 3,999, 265 g, horizontal 360°, 40 m @ 10% reflectivity, built-in IMU – official datasheet), for SLAM localization.
- 【Why】RGB-D has limited range and FOV; a 360° LiDAR allows the robot to continuously localize and avoid obstacles while moving.
- 【How to analyze your situation】For a fixed room with short routes: RGB-D odometry is sufficient; add LiDAR for cross-room navigation.

**Step 6: Joint Calibration**
- 【What to do】Perform camera intrinsic calibration → hand-eye calibration → camera-LiDAR-IMU [joint calibration](/entry/ent_method_calibration_joint_camera_imu/): use a calibration target to minimize reprojection error, and refine point cloud registration with ICP.
- 【Why】Manipulation is essentially a coordinate transformation chain: pixel → camera frame → base frame → end effector; an error in any extrinsic parameter means grasping at air.
- 【How to analyze your situation】Start by calibrating only the head camera to run grasping; write calibration as a one-click script, and recalibrate after any disassembly or reassembly.

## 3.4 Computing Platform: Layered Computing and Real-Time Linux

**Step 7: Real-Time Layer + Intelligence Layer**
- 【What to do】Real-time layer: an industrial PC/MCU runs the joint control loop, with the kernel patched with [RT-PREEMPT](/entry/ent_software_rt_preempt_linux/) (making most of the kernel preemptible, providing deterministic low latency). Intelligence layer: [Jetson AGX Orin](/entry/ent_component_nvidia_jetson_agx_orin_2024/) (up to 275 TOPS @ 64 GB version, 15–60 W, dev kit approx. USD 1,999 – NVIDIA official website/third-party reference); for running humanoid foundation models, evaluate the [Jetson Thor](/entry/ent_component_nvidia_jetson_thor/) (Blackwell architecture, designed for VLA edge inference, price must be confirmed with the supplier).
- 【Why】Control loops require determinism, while AI inference requires throughput; mixing them on a non-real-time system causes mutual interference.
- 【How to analyze your situation】For teleoperation + ACT-level policies, Orin 32 GB is sufficient; for VLA/GR00T N1-level inference, Orin 64 GB or Thor is needed.

## 3.5 Intelligence Layer Ladder: Teleoperation → Data → Imitation Learning → VLA → On-Device → Evaluation

**Step 8: Teleoperation**
- **【What to do】** Build master-slave teleoperation: Refer to [ALOHA](/entry/ent_technology_aloha_teleoperation_system_2023/) (low-cost dual-arm master-slave hardware, complete set approximately $20,000 level—see Step 10 ACT card); for mobile scenarios, draw on [Mobile ALOHA](/entry/ent_technology_mobile_aloha_2024/) whole-body teleoperation ideas; when a full robot is unavailable, use the [UMI gripper interface](/entry/ent_technology_umi_gripper_interface_2024/) (handheld gripper + camera suffices for demonstration collection).
- **【Why】** Teleoperation serves three purposes: verify hardware reachability, collect imitation learning data, and establish task baselines (see [Chapter 17](/wiki/chapters/chapter-17/)).
- **【How to analyze your situation】** With a very tight budget, use UMI first to collect data; with a bipedal robot, teleoperation initially only handles the upper limbs, while the lower limbs use joystick for fixed-point control (the pragmatic division of labor in Mobile ALOHA).

**Step 9: Data Collection**
- **【What to do】** Define the episode format (multi-view images, joint states, actions, language instructions, timestamps), collect data according to a unified protocol, and split into training/validation sets.
- **【Why】** Format determines reusability: [Open X-Embodiment](/entry/ent_dataset_open_x_embodiment/) uses a unified RLDS format to aggregate millions of demonstration frames across embodiments, serving as the standard corpus for VLA pre-training; [DROID](/entry/ent_dataset_droid/) demonstrates distributed multi-lab collection (limitation: only covers fixed arms).
- **【How to analyze your situation】** Collecting tens to hundreds of episodes personally is sufficient to train an ACT-level single-task policy; to fine-tune a VLA, directly align with the OXE format.

**Step 10: Imitation Learning**
- **【What to do】** Try three methods sequentially: [Behavior Cloning](/entry/ent_method_behavior_cloning/) as baseline → [ACT](/entry/ent_method_action_chunking_transformer/) (predicts approximately 100-step action chunks at once + temporal ensemble smoothing, reports 80%–90% success rate for fine dual-arm tasks—see card) → [Diffusion Policy](/entry/ent_method_diffusion_policy/) (denoising diffusion models action distribution, supports multi-modal actions).
- **【Why】** Frame-by-frame regression accumulates compounding errors; action chunking and diffusion modeling are two mainstream approaches to suppress this (see [Chapter 18](/wiki/chapters/chapter-18/)).
- **【How to analyze your situation】** For a first attempt, go directly with ACT (compatible with ALOHA data); if actions have multiple valid solutions, choose Diffusion Policy.

**Step 11: VLA**
- **【What to do】** Evaluate sequentially: [OpenVLA](/entry/ent_method_openvla/) (open-source VLA trained on OXE) → [π0](/entry/ent_method_pi0/) (versatile policy pre-trained on multi-robot data) → [GR00T N1](/entry/ent_method_gr00t_n1/) (NVIDIA's general-purpose humanoid foundation model), see [Chapter 19](/wiki/chapters/chapter-19/).
- **【Why】** VLA upgrades "understanding instructions" from a hard-coded state machine to a model capability: vision + language directly output actions.
- **【How to analyze your situation】** Without a GPU cluster: use OpenVLA weights + LoRA fine-tuning on self-collected data. Pragmatic approach: VLA only handles instruction parsing and skill scheduling, while low-level grasping is executed by the policy from Step 10.

**Step 12: On-Device Deployment**
- **【What to do】** Deploy the policy to an onboard Jetson: [On-device VLA inference](/entry/ent_tech_on_device_vla_inference/) requires the model to run on built-in compute to meet latency, connectivity, and privacy constraints; methods include quantization, inference engine optimization, and reducing input resolution.
- **【Why】** Mobile robots cannot assume network availability—cloud inference equals loss of control during Wi-Fi jitter.
- **【How to analyze your situation】** Small models like ACT can typically run on Orin; for VLA, first quantize and measure latency; if it doesn't meet requirements, then reduce resolution or action chunk size.

**Step 13: Evaluation**
- **【What to do】** For simulation, use [LIBERO](/entry/ent_benchmark_libero/) (thematic task suite + short-horizon desktop benchmark with procedural scene variations) for regression testing; for the real robot, use a fixed task list and number of trials, re-testing after changes.
- **【Why】** Tuning parameters without a benchmark is alchemy: procedural variations expose overfitting, and re-testing with a fixed protocol is necessary for horizontal comparison of changes.
- **【How to analyze your situation】** For individuals: one LIBERO suite + 20 fixed real-robot tests is sufficient.

## 3.6 System Integration and Engineering

**Step 14: Middleware**
- **【What to do】** Organize all nodes using [ROS 2](/entry/ent_software_ros_2_middleware_2024/) (the de facto standard middleware based on DDS publish/subscribe with real-time support): perception, estimation, planning, control, and policy inference communicate across processes, with frozen interfaces and QoS.
- **【Why】** The multi-process architecture allows the control loop to safely shut down even if perception crashes.
- **【How to analyze your situation】** During the prototype phase, a single launch file can start everything; before joint debugging, critical processes must be split and watchdog timers configured.

**Step 15: Safety Circuit and OTA**
- **【What to do】** (a) Install a hardware [emergency stop system](/entry/ent_component_emergency_stop_system_2024/): a hardwired circuit that cuts power or commands a safe state when pressed, independent of all software; (b) Build a prototype [OTA software update](/entry/ent_technology_ota_software_update_2024/) system: wirelessly push policies/firmware/system software with version management and rollback.
- **【Why】** An emergency stop is the entry ticket for full-size platforms into the lab—software emergency stops are unreliable during a crash; without OTA, every policy change requires a cable connection.
- **【How to analyze your situation】** For platforms that can injure someone if they fall: emergency stop + safety zone + tether during debugging are all essential; for small desktop platforms, a simple independent hardware power switch suffices.

## 3.7 Reference Solutions: OpenLoong and Teaching-Grade Alternatives

- **【What to do】** Select a reference frame by comparing four projects with research archives (`data/roadmap/research/`, snapshot at the time of retrieval):

| Project | Size/DOF | Cost | Open Source & Ecosystem | Suitable For |
|---|---|---|---|---|
| **OpenLoong/Qinglong** | 185 cm / 80 kg+, 43 active DOF (including 5-finger dexterous hand) | BOM **unknown**, reference robot not sold | Main repo Apache-2.0; MPC+WBC runnable in MuJoCo without hardware; EtherCAT, 400 TOPS main controller | Universities/enterprises for full-size secondary development; individuals can use its MuJoCo framework or follow NanoLoong |
| **InMoov** | Life-size **upper body** (no legs, cannot walk), ~28 servos | Third-party estimate USD 800–2,500 | CC BY-NC non-commercial; tendon-driven 5-finger hand; Arduino + MyRobotLab | Low-cost experience with life-size robots; cannot learn walking |
| **Poppy Humanoid** | 84 cm / 3.5 kg, 25 DOF | Kit approx. €9,000 | CC BY-SA / GPLv3; compliant backdrivable for teaching; main repo last updated 2021 | Educators focused on teaching systems and HRI |
| **ROBOTIS OP3** | 51 cm / 3.5 kg, 20 DOF (XM430-W350, stall torque 4.1 N·m) | USD 13,764.35 | Software Apache-2.0, 2025 replica native ROS 2; e-Manual documentation benchmark | Schools/labs with sufficient budget needing a ready-to-use robot |

- **【How to analyze your situation】** For institutions with full-size robots, follow OpenLoong for secondary development; for individuals with < USD 1,000, choose InMoov; for classrooms, choose OP3 (hassle-free) or Poppy (good system but requires self-maintenance). The main path of this roadmap remains self-building, but the software stacks of these projects can all be reused.

## 3.8 Overall Acceptance: End-to-End Task

- **【What to do】** Break the task into a five-stage pipeline and debug it together: instruction parsing → navigation to the table (SLAM + planning) → RGB-D detection of the cup and pose estimation → IK + grasp planning → close gripper and confirm. Test each stage individually, then debug the entire chain together.
- **【Why】** An end-to-end task is a cross-check of all subsystems; segmented observation allows pinpointing the failed stage.
- **【How to analyze your situation】** If walking is unstable: first close the loop with "fixed stance + tabletop grasping" before unlocking the walking stage; for instruction parsing, start with fixed-format text.

## 3.9 Timeline and Budget Summary (Phase 0 → 3 Cumulative)

The procurement prices for Phase 3 are annotated with sources in Sections 3.3–3.5; prices for arms, dexterous hands, and Jetson Thor **must be confirmed with suppliers**. Cumulative perspective (details for Phases 0–2 are on their respective roadmap pages):

| Route | Phase 3 Increment | Phase 0→3 Cumulative | Cumulative Timeline |
|---|---|---|---|
| Teaching Grade (InMoov/OP3/Poppy type) | USD 800–15,000 (sources in Table 3.7) | Same as left, the whole machine is the main cost | Estimated 1–3 months |
| Advanced Grade (self-built, main line of this page) | Perception + computing approx. USD 2,800+, plus arm/end-effector/structure (price inquiry required) | Estimated thousands to tens of thousands of USD, depending on Phase 0–2 BOM | Estimated cumulative 8–24 months |
| Full-Size Grade (OpenLoong type) | BOM unknown (per survey archives), requires institutional-level conditions | Same as left | Measured in team-years |

## Acceptance Criteria

1. Kinematics: Randomly sample 100 target poses within the workspace, IK solution success rate ≥95%, real robot end-effector positioning error ≤2 cm (recommended threshold).
2. Perception: After calibration, RGB point cloud coloring shows no obvious misalignment (reprojection error < 2 pixels); cup 3D positioning error ≤1 cm.
3. Intelligence Layer: Complete ≥50 high-quality teleoperation episodes; real robot grasping success rate under fixed protocol ≥70%.
4. End-to-End: "Hear command → Walk to table → Grasp cup" succeeds ≥7 times out of 10 consecutive trials, each trial ≤2 minutes.
5. Safety: Press emergency stop at any time, power supply is immediately cut off (measured <1 s), reset requires manual confirmation.
6. Engineering: After manually killing the perception process, the control loop does not interrupt, and the robot enters a safe state.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| IK solution failure/joint jump | Target outside workspace; near singular configuration; joint limits not modeled | Check target point in RViz; switch to damped least squares; verify URDF joint limits |
| Whole-body shaking/tipping when reaching | No center-of-mass compensation; excessive speed | Reduce speed and retest; pre-plan center-of-mass trajectory; stabilize before operation |
| ACT/BC real robot performance far worse than training | Data distribution shift; compound error | Supplement failure scenarios; check image and action time alignment |
| VLA cannot run on edge device | Not quantized; insufficient memory/compute | Quantize and measure latency; reduce input resolution; upgrade to Orin 64 GB/Thor |
| Emergency stop pressed but power not cut | Emergency stop routed through software | Emergency stop must be hardwired to cut power circuit; test independently |
| OTA fails to boot | No rollback; power loss during update | A/B partition; check battery level before update; leave serial recovery channel |

## Companion Reading

- [Sensor Selection Guide](playbooks/sensor-selection.md) — Perception stack specifications and price tiers
- [Computing Platform Selection Guide](playbooks/compute-selection.md) — Layered brain and edge inference
- [Actuator Selection Guide](playbooks/actuator-selection.md) — Actuator solutions for arms and dexterous hands
- [Roadmap Overview](index.md)
