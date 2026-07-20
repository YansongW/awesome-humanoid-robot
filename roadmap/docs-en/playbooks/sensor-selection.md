# Selection Guide: How to Choose a Sensor

> ⚠️ The content of this roadmap is compiled based on public information and theoretical knowledge, and has not been verified with actual hardware; please verify safety specifications yourself when involving electrical or mechanical operations.

A common mistake in sensor selection is to "match the robot manufacturer's promotional video": buying a RealSense, a six-axis force/torque sensor, and even a tactile array, only to find that the data cannot be processed in time, or that the control frequency is throttled by the USB bandwidth. This guide takes the opposite approach: first, break down the tasks your robot must accomplish into "what physical quantities must be known," then select the sensor that is just sufficient for each type of physical quantity. For the theoretical background, see [Chapter 5: Sensing and Perception Hardware](/wiki/chapters/chapter-05/); for the supplier landscape, see [Chapter 7: Supplier Map](/wiki/chapters/chapter-07/).

## 1. Perception Requirement Decomposition: What Must Your Robot "Know"

Divide sensors into three layers and answer "Do I really need it?" layer by layer:

### Layer 1: Proprioception — Joint Angles and Body Posture

**[What to do]** Define the position feedback scheme for each active joint (motor-side encoder, output-side encoder, or dual encoders), and the IMU configuration for the torso/feet (number of units, sampling rate).

**[Why]** Proprioception is the lifeline of the control loop; without it, the robot doesn't even know "where its own legs are." [Joint Encoder](/entry/ent_component_joint_encoder_2024/) provides high-resolution position feedback for motor control. A key consideration is "which end to mount it on": a motor-side encoder cannot see gearbox backlash or flexural deformation. Platforms requiring precise force control add an output-side encoder to form a dual-encoder setup — the Open Dynamic Robot Initiative's BLMC actuator uses a "dual encoder (motor-side/output-side)" design (source: research file open-dynamic-robot-initiative.md). Low-budget solutions also exist: Berkeley Humanoid Lite uses a $3 AS5600 magnetic encoder (source: research file berkeley-humanoid-lite.md), and its torso posture uses a single phone-grade BNO085 IMU to achieve zero-shot sim-to-real walking (same file). [IMU](/entry/ent_component_imu_2024/) handles attitude estimation, providing high-frequency inertial reference fused with encoder and vision data.

**[How to analyze your situation]** For position-controlled servo solutions (e.g., Dynamixel), the encoder is built-in, so this layer costs nothing. For self-developed QDD joints, at least a motor-side encoder is needed; whether an output-side encoder is required depends on whether you do force control (yes → needed). Start with one torso-level IMU; for dynamic walking research, adding foot IMUs or contact sensing is recommended — BRUCE biped achieves 2 kHz IMU sampling for this purpose (source: research file bruce-westwood.md).

### Layer 2: Force Sensing — End-effector Force, Ankle Force, Fingertip Tactile

**[What to do]** Decide three things: whether to use a [Six-axis F/T Sensor](/entry/ent_component_six_axis_force_torque_sensor_2024/) at the wrist/ankle (which flange, what range); whether to use a [Tactile Sensor Array](/entry/ent_component_tactile_sensor_array_2024/) at the dexterous hand fingertips; or whether to initially estimate force using the actuator's current loop.

**[Why]** A six-axis force/torque sensor measures three force components and three torque components simultaneously. It is essential for force-controlled assembly, drag teaching, and ZMP estimation in bipedal ankles — THORMANG3 uses one ATI Mini58 in each ankle (source: research file thormang3.md). However, it is one of the most expensive sensors on the robot, and its range and precision conflict (a larger range wastes resolution). Tactile arrays measure contact pressure/shear/texture, supporting slip detection for dexterous manipulation; when budget is tight, FSR arrays can be used as an entry point — the Poppy humanoid in 2014 used 16 FSR force sensors (source: research file poppy-humanoid.md).

**[How to analyze your situation]** Only walking, no manipulation → current loop force estimation + foot switch contact sensing is sufficient, saving the cost of six-axis F/T. For assembly/grinding manipulation research → a wrist six-axis F/T is worth the investment; select the range as "maximum contact force × 2." For dexterous hand grasping research → prioritize tactile arrays over wrist six-axis F/T, because slip during grasping primarily occurs at the fingertips.

### Layer 3: Exteroception — Seeing the Outside World

**[What to do]** Clarify the type of exteroception task: close-range operation scene understanding (0.3–3 m), indoor navigation and mapping (3–20 m), or outdoor/large spaces. These three correspond to completely different sensors.

**[Why]** [RGB-D cameras](/entry/ent_component_rgbd_camera/) have three depth technologies — structured light, ToF, and stereo — each with applicable distance and lighting constraints: structured light is accurate but sensitive to strong light; stereo is passive but relies on texture. The mainstream head vision solution is [Intel RealSense](/entry/ent_component_intel_realsense_depth_camera_2024/) (D435i/D455 used by platforms like Qinglong and G1, sources: openloong-qinglong research file, Unitree card); the main sensor for navigation and mapping is LiDAR. The [Livox Mid-360](/entry/ent_component_livox_mid_360_lidar_2024/) offers 360° surround view at 265 g, making it a popular choice for quadruped/humanoid SLAM (source: Livox card).

**[How to analyze your situation]** Only desktop grasping → one RGB-D camera is enough; LiDAR is wasteful. For indoor walking navigation → RGB-D (close-range obstacle avoidance) + 360° LiDAR (mapping) is a mature combination. For pure vision research (VLA, visual servoing) → allocate budget to camera frame rate and global shutter, rather than stacking LiDARs.

## II. Component Selection Table: Key Indicators → How They Affect Your Robot → Price Range

### Encoder

| Key Indicator | How It Affects Your Robot | Price Range Reference |
|---|---|---|
| Resolution (Bits) | Determines position control accuracy and speed estimation quality; joints with 17 bits or more can achieve smooth low-speed force control | Magnetic encoder AS5600 (12 bit) approx. $3 (BHL archive); high-resolution optical/absolute types require inquiry |
| Absolute vs Incremental | Absolute encoders know the angle on power-up; humanoid robots have many joints, and incremental encoders require painful homing each time | Absolute encoders are more expensive, choose as needed |
| Mounting Position (Motor Side / Output Side) | Output-side encoders let you "see" gearbox backlash and flexspline deformation, a prerequisite for force control transparency | Dual encoders = double the cost, worthwhile for force control platforms (ODRI archive) |

### IMU

| Key Indicator | How It Affects Your Robot | Price Range Reference |
|---|---|---|
| Gyro Bias Stability | Determines attitude integration drift speed; [IMU Card](/entry/ent_component_imu_2024/) example ADIS16475 is 2°/hr (in operation) | Phone-grade (BNO085, used by BHL) tens of RMB; industrial MEMS (ADIS16475 class) price undisclosed, requires inquiry; FOG-grade separate |
| Angular Random Walk (ARW) | Noise directly enters attitude estimation; ADIS16475 is 0.15°/√hr | Same as above |
| Cross-Axis Alignment Error | Installation alignment effort for multi-sensor fusion; ADIS16475 ±0.1° factory calibrated | Low-end IMUs require self-calibration |
| Sampling Rate / Interface | Balance control loops require high-frequency attitude; SPI has lower latency than I²C; ADIS16475 uses SPI | BRUCE achieves 2 kHz (archive) |

### Six-Axis Force/Torque Sensor

| Key Indicator | How It Affects Your Robot | Price Range Reference |
|---|---|---|
| Range (F/M) | Select based on "maximum contact force × 2"; Shenyuansheng MLL typical 50/50/100 N, 2/2/4 N·m; [OnRobot HEX-E QC](/entry/ent_component_ati_force_torque_sensor_2024/) ±100/±200 N, ±10 N·m (source: two cards) | Domestic analog type (MLL class) requires inquiry; imported ATI Nano25 (±250 N) class significantly more expensive |
| Accuracy / Crosstalk Error | Determines credibility of decoupled six-axis force control; MLL accuracy ≤0.5% FS, crosstalk error ≤2% FS | Higher accuracy models are more expensive |
| Overload Capacity | Bipedal ankles inevitably experience impacts; MLL ≥300% FS, HEX-E approx. 500% FS | Overload margin = lifespan |
| Sampling Rate & Interface | Force control loop requires ≥1 kHz; MLL max 1000 Hz (with acquisition unit), HEX-E uses EtherNet/IP and other industrial buses | Acquisition unit/bus gateway costs extra |

### Tactile Array

| Key Indicator | How It Affects Your Robot | Price Range Reference |
|---|---|---|
| Spatial Resolution (Taxel Density) | Determines ability to discern contact shape and texture, supporting slip prediction | Discrete FSR points are cheapest (Poppy uses 16 points); array type requires inquiry |
| Measurement Dimension | Normal pressure only vs. triaxial force (including shear) – shear is a precursor to slip | Triaxial arrays are much more expensive, only needed for grasping research |
| Curved Surface Attachment & Wiring | Curved fingertip mounting and routing is a major engineering challenge, often more labor-intensive than the sensor itself | Evaluate flexible PCB solutions |

### RGB-D Camera (RealSense vs ZED)

| Key Indicator | How It Affects Your Robot | Price Range Reference |
|---|---|---|
| Ideal Range & Accuracy | Manipulation scenarios focus on 0.3–1 m accuracy: [RealSense](/entry/ent_component_intel_realsense_depth_camera_2024/) D435i is 0.1–10 m, <2% @2 m; D455 is 0.6–6 m, <2% @4 m (source: RealSense card, official datasheet) | D435i approx. USD 199, D455 approx. USD 299 (public market reference, card specification) |
| Shutter Type | Head is moving; global shutter (D455) avoids rolling shutter distortion | Global shutter models are generally slightly more expensive |
| Built-in IMU | Visual-inertial fusion (VIO) saves an external IMU: D435i has built-in BMI055 | Only available in 'i' suffix models |
| Compute Dependency | [ZED Stereo Camera](/entry/ent_component_zed_stereo_camera_2024/) onboard depth + spatial AI, but depth computation relies on host GPU ecosystem (source: ZED card); price requires direct supplier confirmation | RealSense ecosystem (librealsense+ROS) has zero compute barrier; ZED requires NVIDIA host |

### LiDAR

| Key Indicator | How It Affects Your Robot | Price Range Reference |
|---|---|---|
| FOV | [Livox Mid-360](/entry/ent_component_livox_mid_360_lidar_2024/) horizontal 360°, vertical -7°~52°, one unit covers torso surround view (source: Livox card) | Mid-360 approx. CNY 3,999 (official store, card specification) |
| Detection Range & Accuracy | 40 m @10% reflectivity, ≤2 cm @10 m – more than sufficient for indoor navigation and mapping | Same as left |
| Point Rate & Frame Rate | 200,000 points/sec, 10 Hz, determines dynamic scene update rate | Same as left |
| Weight / Power Consumption | 265 g, 6.5 W, acceptable for head/torso; built-in ICM40609 IMU enables LIO | Same as left |

## III. Calibration & Time Synchronization: Buying the Right Sensor is Only Half the Job

[What to Do] Develop a calibration plan: camera intrinsics (checkerboard), camera-LiDAR extrinsics, camera-IMU extrinsics and time offset, joint zero positions, and agree on a unified time source (PTP or hardware trigger).

[Why] All algorithms for multi-sensor fusion assume "extrinsics known, clocks synchronized." The [Joint Camera-IMU Calibration](/entry/ent_method_calibration_joint_camera_imu/) card provides the standard workflow: multi-pose calibration target acquisition → camera corner detection + LiDAR plane/corner extraction → PnP initial value + ICP/nonlinear optimization → minimize reprojection error for verification; when no calibration target is available, scene edge alignment or mutual information methods can be used for online refinement. If the time offset is not calibrated, fusion results during motion become "ghosted" – VIO divergence and point cloud color misalignment originate from this. See [Chapter 11: Assembly, Integration, and Testing](/wiki/chapters/chapter-11/) for systematic integration and testing methods.

[How to Analyze Your Situation] Starting with a single RGB-D only requires camera intrinsics; adding LiDAR necessitates camera-LiDAR extrinsics (the card method can be directly applied); VIO/multi-IMU fusion requires additional time calibration. Use reprojection error as the acceptance metric, don't rely on visual "looks roughly aligned."

## IV. Two Recommended Configurations

### Beginner Minimum Kit (Goal: Walk, See, Not Break Easily)

- Joint Feedback: Smart servo built-in encoder, or self-developed joint using AS5600-class magnetic encoder ($3/unit, BHL archive specification).
- Attitude: One phone-grade IMU (BNO085 class), first get attitude estimation working.
- External Perception: One RealSense D435i (approx. USD 199, card specification) – depth + RGB + IMU all-in-one, most mature ecosystem.
- Force Sensing: Not initially; use current loop for force estimation; foot end can use switch/FSR for ground contact detection.
- Analysis Logic: This setup spends every dollar on "essentials for control loop closure," sufficient for walking and grasping demos; upgrade item by item when bottlenecks become clear (large attitude drift, inability to detect grasp slip).

### Research-Grade Kit (Goal: Force Control / Manipulation / Navigation Paper-Quality Data)

- Joint Feedback: Dual encoders (motor side + output side), output side using high-resolution absolute type.
- Attitude: Industrial MEMS IMU (ADIS16475 class: ARW 0.15°/√hr, bias 2°/hr, ±0.1° alignment, card specification) + distributed placement on torso/feet, sampling towards 1–2 kHz.
- Force Sensing: Wrist six-axis force (domestic MLL class or ATI/OnRobot class) + bipedal ankle six-axis force (THORMANG3 configuration precedent), dexterous hand with tactile array.
- External Perception: RealSense D455 (global shutter, approx. USD 299) or ZED (when GPU host is available) + Livox Mid-360 (approx. CNY 3,999) for 360° mapping.
- Calibration: Full set of intrinsic/extrinsic/time synchronization calibration, reprojection error included in acceptance.
- Analysis Logic: The core of research-grade is "data credibility" – expensive sensors are not the goal; calibratability, traceability, and clock synchronization are.

## Acceptance Criteria

- Have a checklist of "physical quantity → sensor → mounting position → interface → sampling rate," where each item can answer "what happens without it."
- Key indicators (range/accuracy/bandwidth) of each sensor correspond one-to-one with task requirements and are traceable to cards or datasheets; items without public prices are marked "requires direct supplier confirmation."
- Calibration plan implemented: camera intrinsics completed; if LiDAR is installed, camera-LiDAR extrinsics completed and reprojection error recorded.
- All sensor timestamps unified to the same clock source; fusion nodes show no visible temporal misalignment.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Slow drift in attitude estimation, increasingly skewed walking | Insufficient IMU bias stability or lack of temperature compensation calibration | Check bias stability indicator; estimate bias while stationary, upgrade to industrial-grade IMU if necessary |
| VIO/fusion divergence during walking | Camera-IMU time offset not calibrated | Perform time synchronization calibration; check if timestamp sources are unified |
| Point cloud coloring misalignment, ghosting | Camera-LiDAR extrinsic parameters outdated (after collision) | Re-perform multi-pose calibration, check if reprojection error converges |
| Six-axis force reading zero drift | Temperature drift or failure to tare; installation stress interference | Tare after power-on warm-up; check flange preload |
| Six-axis force range always saturated | Range selected based on "typical force" rather than "impact × 2" | Verify ankle impact peak; replace with larger range or add overload protection strategy |
| Large depth map voids in sunlight | Structured light/active IR susceptible to strong light (inherent to the approach) | Check depth technology approach; switch to passive stereo or LiDAR for outdoor use |
| High noise in tactile array data | Wire bending interference, power supply ripple | Secure wire routing; check power supply with oscilloscope, add filtering |

## Related Reading

- [Stage 3 · Full Humanoid](../stage-3-humanoid.md) — Perception Stack Integration and Calibration Practice
- [Stage 2 · Biped Platform](../stage-2-biped.md) — Role of Proprioceptive Sensors in Balance Control
- [Roadmap Overview](../index.md)
