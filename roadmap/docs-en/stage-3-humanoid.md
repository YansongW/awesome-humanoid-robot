# Phase 3: Complete Humanoid Robot – From Bipedal Platform to "Hear, Walk Over, Pick Up"

After Phase 2's biped can walk stably, Phase 3 adds the "upper body" on top: arms, end-effectors, perception, computing power, and an intelligence layer to complete end-to-end tasks – **Hear a command → Walk to the table → Pick up a cup**. Each step is expanded in a "What → Why → How to analyze your situation" three-part format, tailored by budget/scenario/skill.

## Phase Task List (M15–M20)

This page is the phase map; the task pages are the construction manual – complete calculation examples, three-part details, and checkable acceptance checklists for each step are in the task pages:

| Task | Content | Corresponding Section on This Page |
|---|---|---|
| [M15 · Upper Body & End Effector](missions/m15-upper-body.md) | Arm configuration & DOF, joint parameter recalculation, gripper/dexterous hand, FK/IK | 3.1, 3.2 |
| [M16 · Perception Stack Setup](missions/m16-perception-stack.md) | RGB-D/LiDAR configuration, time synchronization, calibration chain, detection & localization | 3.3, 3.4 |
| [M17 · Teleoperation & Data Collection](missions/m17-teleop-data.md) | Four-tier teleop solutions, collection pipeline, scenario design, data quality check | 3.5 Steps 8–9 |
| [M18 · Imitation Learning Training & Deployment](missions/m18-imitation-learning.md) | BC/ACT/Diffusion ladder, evaluation protocol, edge deployment | 3.5 Steps 10–12 |
| [M19 · End-to-End Task Integration](missions/m19-e2e-task.md) | State machine, navigation segment, manipulation segment, full-chain integration & acceptance drill | 3.8 |
| [M20 · Reliability, Maintenance & Safety Engineering](missions/m20-reliability-safety.md) | FMEA, protection mechanism testing, battery procedures, maintenance & documentation | 3.6 + Throughout |

## 3.1 Upper Body & Arms: 7-DOF Arms & Kinematics

**Step 1: Determine Configuration & Full-Body Model**
- 【What】Select the arm solution: standard 7 DOF per arm (shoulder 3, elbow 1, wrist 3). First build a URDF in simulation to confirm no interference, then purchase or fabricate using Phase 1/2 actuators.
- 【Why】A [seven-degree-of-freedom robotic arm](/entry/ent_component_7dof_arm_2024/) mimics human arm redundancy: 6 DOF can only "reach" a pose; the 7th allows the elbow to move while the end-effector remains stationary, enabling obstacle avoidance and singularity avoidance. Torque/weight/price **must be confirmed with the supplier** (selection see [Chapter 4](/wiki/chapters/chapter-04/)).
- 【How to analyze your situation】For desktop grasping only: start with a single arm or even 6 DOF; bimanual coordination and obstacle avoidance require 7 DOF. Simulate first, then machine metal parts.

**Step 2: Kinematics & Coordinate Systems**
- 【What】Implement [Forward Kinematics (FK)](/entry/ent_method_forward_kinematics/) (homogeneous transformation chain/product of exponentials) and [Inverse Kinematics (IK)](/entry/ent_method_inverse_kinematics/) (Jacobian pseudo-inverse numerical solution or geometric analytical solution); for 7-DOF IK, add secondary objectives in the null space (raise elbow, avoid joint limits). Then integrate the arm into the full-body URDF, unifying the whole-body TF transform tree.
- 【Why】After vision provides the cup position, FK converts coordinate systems and IK solves for joint angles; near singularities, numerical IK can diverge; the standard solution is damped least squares. A humanoid has no fixed base; end-effector accuracy = arm accuracy + torso posture error + foot slip accumulation.
- 【How to analyze your situation】Directly use mature IK solvers from the ROS ecosystem; verification sequence: simulation spot-check → no-load → loaded. If walking is unstable, adopt a "stand still, then operate" strategy.

## 3.2 End Effector: Start with a Gripper

**Step 3: Start with a Gripper, Reserve Dexterous Hand Interface**
- 【What】The first version uses an electric parallel gripper for cup grasping; the interface is designed to be replaceable, allowing future upgrades to the [LEAP dexterous hand](/entry/ent_component_leap_hand/) or [Allegro dexterous hand](/entry/ent_component_allegro_hand/).
- 【Why】[Dexterous hand](/entry/ent_component_dexterous_hand_2024/) vs. gripper: the former has high DOF but complex control and high cost; the latter is simple, cheap, but has limited grasping types. LEAP is a low-cost open-source 16-DOF anthropomorphic hand (direct-drive Dynamixel + 3D printing, BOM needs confirmation from the project team); Allegro is Wonik's commercial 16-DOF four-finger hand (torque-controlled joints, ROS compatible, price needs confirmation from the supplier). For cup-grasping tasks, a gripper's success rate is much higher than a poorly tuned dexterous hand.
- 【How to analyze your situation】Use a gripper to get the end-to-end pipeline working; start with LEAP for imitation learning research papers; choose Allegro for commercial reliability.

## 3.3 Perception Stack: RGB-D, LiDAR & Calibration

**Step 4: Depth Camera**
- 【What】Install one [RGB-D camera](/entry/ent_component_rgbd_camera/) on the head/chest for primary vision, and reserve a near-field camera position on the wrist. Mainstream options: [Intel RealSense](/entry/ent_component_intel_realsense_depth_camera_2024/) D435i (approx. USD 199, range 0.1–10 m, with IMU – official datasheet) or D455 (approx. USD 299, depth accuracy <2% @ 4 m); for onboard depth estimation, consider the [ZED stereo camera](/entry/ent_component_zed_stereo_camera_2024/) (price needs confirmation from the supplier).
- 【Why】Depth acquisition has three routes: structured light, ToF, and stereo vision (see RGB-D card); the D435i's minimum range of 0.1 m is suitable for desktop operations; the wrist camera is a key source of manipulation data.
- 【How to analyze your situation】On a tight budget, start with one D435i; for multiple cameras, pay attention to USB bandwidth (see common pitfalls).

**Step 5: LiDAR**
- 【What】If the task includes indoor navigation, install a 360° LiDAR, such as the [Livox Mid-360](/entry/ent_component_livox_mid_360_lidar_2024/) (approx. CNY 3,999, 265 g, horizontal 360°, 40 m @ 10% reflectivity, built-in IMU – official datasheet), for SLAM localization.
- 【Why】RGB-D has limited range and FOV; a 360° LiDAR allows the robot to continuously localize and avoid obstacles while moving.
- 【How to analyze your situation】Fixed room, short path: RGB-D odometry is sufficient; cross-room navigation requires LiDAR.

**Step 6: Joint Calibration**
- 【What】Perform sequentially: camera intrinsic calibration → hand-eye calibration → camera-LiDAR-IMU [joint calibration](/entry/ent_method_calibration_joint_camera_imu/): use a calibration target to minimize reprojection error, and ICP to refine point cloud registration.
- 【Why】Manipulation is essentially a coordinate transformation chain: pixel → camera frame → base frame → end-effector frame; if any extrinsic parameter in the chain is wrong, the robot will grasp at air.
- 【How to analyze your situation】Calibrating only the head camera is sufficient to start grasping; write calibration as a one-click script; recalibration is mandatory after any disassembly/assembly.

## 3.4 Computing Platform: Layered Computing Power & Real-Time Linux

**Step 7: Real-Time Layer + Intelligence Layer**
- 【What】Real-time layer: industrial PC/MCU runs joint control loops, with the kernel patched by [RT-PREEMPT](/entry/ent_software_rt_preempt_linux/) (making most of the kernel preemptible, providing deterministic low latency). Intelligence layer: [Jetson AGX Orin](/entry/ent_component_nvidia_jetson_agx_orin_2024/) (up to 275 TOPS @ 64 GB version, 15–60 W, dev kit approx. USD 1,999 – NVIDIA official/third-party reference); for running humanoid foundation models, evaluate [Jetson Thor](/entry/ent_component_nvidia_jetson_thor/) (Blackwell architecture, designed for VLA edge inference, price needs confirmation from the supplier).
- 【Why】Control loops require determinism; AI inference requires throughput; mixing them on a non-real-time system causes mutual degradation.
- 【How to analyze your situation】For teleoperation + ACT-level policies, Orin 32 GB is sufficient; for VLA/GR00T N1-level inference, Orin 64 GB or Thor is needed.

## 3.5 Intelligence Layer Ladder: Teleoperation → Data → Imitation Learning → VLA → On-Device → Evaluation

**Step 8: Teleoperation**
- 【What】Set up master-slave teleoperation: Reference [ALOHA](/entry/ent_technology_aloha_teleoperation_system_2023/) (low-cost dual-arm master-slave hardware, complete set approximately $20,000 level—see Step 10 ACT card); for mobile scenarios, draw on [Mobile ALOHA](/entry/ent_technology_mobile_aloha_2024/) whole-body teleoperation ideas; without a full robot, use the [UMI gripper interface](/entry/ent_technology_umi_gripper_interface_2024/) (handheld gripper + camera suffices for collecting demonstrations).
- 【Why】Teleoperation serves three purposes: verify hardware reachability, collect imitation learning data, and establish task baselines (see [Chapter 17](/wiki/chapters/chapter-17/)).
- 【How to analyze your situation】With a very tight budget, use UMI first to collect data; with a bipedal robot, teleoperation initially only manages the upper limbs, while the lower limbs use joystick for fixed-point control (the pragmatic division of labor in Mobile ALOHA).

**Step 9: Data Collection**
- 【What】Define the episode format (multi-view images, joint states, actions, language instructions, timestamps), collect data according to a unified protocol, and split into training/validation sets.
- 【Why】Format determines reusability: [Open X-Embodiment](/entry/ent_dataset_open_x_embodiment/) uses a unified RLDS format to aggregate millions of demonstration frames across embodiments, serving as the standard corpus for VLA pre-training; [DROID](/entry/ent_dataset_droid/) demonstrates distributed multi-lab collection (limitation: only covers fixed arms).
- 【How to analyze your situation】Collecting tens to hundreds of episodes individually is sufficient to train an ACT-level single-task policy; to fine-tune a VLA, directly align with the OXE format.

**Step 10: Imitation Learning**
- 【What】Try three methods sequentially: [Behavior Cloning](/entry/ent_method_behavior_cloning/) as baseline → [ACT](/entry/ent_method_action_chunking_transformer/) (predicts ~100-step action chunks at once + temporal ensemble smoothing, reports 80%–90% success rate for fine dual-arm tasks—see card) → [Diffusion Policy](/entry/ent_method_diffusion_policy/) (denoising diffusion models action distribution, supports multi-modal actions).
- 【Why】Frame-by-frame regression accumulates compounding errors; action chunking and diffusion modeling are two mainstream suppression approaches (see [Chapter 18](/wiki/chapters/chapter-18/)).
- 【How to analyze your situation】For a first attempt, go directly with ACT (compatible with ALOHA data); if actions have multiple valid solutions, choose Diffusion Policy.

**Step 11: VLA**
- 【What】Evaluate sequentially: [OpenVLA](/entry/ent_method_openvla/) (open-source VLA trained on OXE) → [π0](/entry/ent_method_pi0/) (generalist policy pre-trained on multi-robot data) → [GR00T N1](/entry/ent_method_gr00t_n1/) (NVIDIA's general-purpose humanoid foundation model), see [Chapter 19](/wiki/chapters/chapter-19/).
- 【Why】VLA upgrades "understanding instructions" from a hard-coded state machine to a model capability: vision + language directly output actions.
- 【How to analyze your situation】Without a GPU cluster: use OpenVLA weights + LoRA fine-tuning on self-collected data. Pragmatic approach: VLA only handles instruction parsing and skill scheduling, while low-level grasping is executed by the policy from Step 10.

**Step 12: On-Device Deployment**
- 【What】Deploy the policy to an onboard Jetson: [On-device VLA inference](/entry/ent_tech_on_device_vla_inference/) requires the model to run on built-in compute to meet latency, connectivity, and privacy constraints; methods include quantization, inference engine optimization, and reducing input resolution.
- 【Why】Mobile robots cannot assume network availability—cloud inference equals loss of control during Wi-Fi jitter.
- 【How to analyze your situation】Small models like ACT can usually run on Orin; for VLA, first quantize and measure latency, then reduce resolution or action chunks if targets are not met.

**Step 13: Evaluation**
- 【What】For simulation, use [LIBERO](/entry/ent_benchmark_libero/) (thematic task suite + short-horizon desktop benchmark with procedural scene variations) for regression testing; for the real robot, use a fixed task list and number of trials, re-testing after changes.
- 【Why】Tuning without a benchmark is alchemy: procedural variations expose overfitting, and fixed-protocol re-testing is necessary for horizontal comparison of changes.
- 【How to analyze your situation】Individual: one LIBERO suite + 20 fixed real-robot tests are sufficient.

## 3.6 System Integration and Engineering

**Step 14: Middleware**
- 【What】Organize all nodes using [ROS 2](/entry/ent_software_ros_2_middleware_2024/) (DDS-based publish/subscribe, de facto standard middleware with real-time support): perception, estimation, planning, control, and policy inference communicate across processes, with frozen interfaces and QoS.
- 【Why】The multi-process architecture allows the control loop to safely shut down even if perception crashes.
- 【How to analyze your situation】During the prototype phase, a single launch file can bring everything up; before joint debugging, critical processes must be split and watchdog timers configured.

**Step 15: Safety Circuit and OTA**
- 【What】(a) Install a hardware [emergency stop system](/entry/ent_component_emergency_stop_system_2024/): a hardwired circuit that cuts power or commands a safe state upon pressing, independent of all software; (b) Build a prototype [OTA software update](/entry/ent_technology_ota_software_update_2024/) system: wirelessly push policies/firmware/system software with version management and rollback.
- 【Why】An emergency stop is the entry ticket for full-sized platforms into the lab—software emergency stops are unreliable during crashes; without OTA, every policy change requires a cable connection.
- 【How to analyze your situation】For platforms that can injure someone upon falling: emergency stop + safety zone + tether during debugging are indispensable; for small desktop platforms, a simple independent hardware power switch suffices.

## 3.7 Reference Solutions: OpenLoong and Teaching-Grade Alternatives

- 【What】Select a reference frame by comparing four projects with research archives (`data/roadmap/research/`, snapshot at retrieval time):

| Project | Size/DOF | Cost | Open Source & Ecosystem | Suitable For |
|---|---|---|---|---|
| **OpenLoong/Qinglong** | 185 cm / 80 kg+, 43 active DOF (including 5-finger dexterous hand) | BOM **unknown**, reference robot not sold | Main repo Apache-2.0; MPC+WBC runnable in MuJoCo without hardware; EtherCAT, 400 TOPS main controller | Universities/enterprises for full-size secondary development; individuals use its MuJoCo framework or follow NanoLoong |
| **InMoov** | Life-size **upper body** (no legs, cannot walk), ~28 servos | Third-party estimate USD 800–2,500 | CC BY-NC non-commercial; tendon-driven 5-finger hand; Arduino + MyRobotLab | Low-cost experience of life-size robotics; cannot learn walking |
| **Poppy Humanoid** | 84 cm / 3.5 kg, 25 DOF | Kit approx. €9,000 | CC BY-SA / GPLv3; compliant backdrivable for teaching; main repo last updated 2021 | Educators focused on teaching systems and HRI |
| **ROBOTIS OP3** | 51 cm / 3.5 kg, 20 DOF (XM430-W350, stall torque 4.1 N·m) | USD 13,764.35 | Software Apache-2.0, 2025 replica native ROS 2; e-Manual documentation benchmark | Schools/labs with sufficient budget needing an out-of-the-box robot |

- 【How to analyze your situation】Institutions with full-size follow OpenLoong for secondary development; individuals with < USD 1,000 choose InMoov; classrooms choose OP3 (hassle-free) or Poppy (good system but requires self-maintenance). The main line of this roadmap remains self-building, but the software stacks of these projects can all be reused.

## 3.8 Overall Acceptance: End-to-End Task

- 【What】Break the task into a five-stage pipeline and integrate: instruction parsing → navigation to table (SLAM + planning) → RGB-D cup detection and pose estimation → IK + grasp planning → close gripper and confirm. Test each stage individually, then integrate the full chain.
- 【Why】An end-to-end task is a cross-check of all subsystems; segmented observation allows pinpointing the failed stage.
- 【How to analyze your situation】If walking is unstable: first close the loop with "fixed stance + tabletop grasping" before unlocking the walking stage; for instruction parsing, start with fixed-format text.

## 3.9 Timeline and Budget Summary (Phase 0 → 3 Cumulative)

The procurement prices for Phase 3 have been annotated with sources in Sections 3.3–3.5; prices for the arm, dexterous hand, and Jetson Thor **must be confirmed with suppliers**. Cumulative perspective (details for Phases 0–2 can be found on their respective roadmap pages):

| Route | Phase 3 Increment | Phase 0→3 Cumulative | Cumulative Timeline |
|---|---|---|---|
| Educational (InMoov/OP3/Poppy class) | USD 800–15,000 (see Table in 3.7 for sources) | Same as left, the whole machine is the main cost | Estimated 1–3 months |
| Advanced (Self-built, main thread of this page) | Perception + compute approx. USD 2,800 and up, plus arm/end-effector/structure (requires price inquiry) | Estimated thousands to tens of thousands of USD, depending on Phase 0–2 BOM | Estimated cumulative 8–24 months |
| Full-size (OpenLoong class) | BOM unknown (per research archive scope), requires institutional-level conditions | Same as left | Measured in team-years |

## Acceptance Criteria

1.  Kinematics: Randomly sample 100 target poses within the workspace, IK solution success rate ≥95%, real robot end-effector positioning error ≤2 cm (recommended threshold).
2.  Perception: After calibration, RGB point cloud coloring shows no obvious misalignment (reprojection error < 2 pixels); cup 3D positioning error ≤1 cm.
3.  Intelligence Layer: Complete ≥50 high-quality teleoperation episodes; real robot grasping success rate under fixed protocol ≥70%.
4.  End-to-End: "Hear command → Walk to table → Grasp cup" succeeds ≥7 times out of 10 consecutive trials, each trial ≤2 minutes.
5.  Safety: Press emergency stop at any time, power supply is immediately cut off (measured <1 s), reset requires manual confirmation.
6.  Engineering: After manually killing the perception process, the control loop does not interrupt, and the robot enters a safe state.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| IK solution failure/joint jump | Target outside workspace; near singular configuration; joint limits not modeled | Check target point in RViz; switch to damped least squares; verify URDF joint limits |
| Whole robot shakes or tips over when reaching | No center of mass compensation; excessive speed | Reduce speed and retest; pre-plan center of mass trajectory; stabilize before operation |
| ACT/BC real robot performance far worse than training | Data distribution shift; compound error | Supplement collection of failure scenarios; check image and action time alignment |
| VLA cannot run on edge device | Not quantized; insufficient VRAM/compute | Quantize and measure latency; reduce input resolution; upgrade to Orin 64 GB/Thor |
| Emergency stop pressed but power not cut | Emergency stop routed through software | Emergency stop must be hardwired to cut the power circuit; test independently |
| OTA fails to boot | No rollback; power loss during update | A/B partitioning; check battery level before update; retain serial recovery channel |

## Companion Reading

- [Sensor Selection Guide](playbooks/sensor-selection.md) — Perception stack specifications and price tiers
- [Compute Platform Selection Guide](playbooks/compute-selection.md) — Layered brain and edge inference
- [Actuator Selection Guide](playbooks/actuator-selection.md) — Actuator solutions for arms and dexterous hands
- [Roadmap Overview](index.md)
