# M11 · Simulation Environment and Model Conversion: Fall Ten Thousand Times in the Digital World First

**Global Position**: Immediately following [M10's URDF model package](m10-urdf-modeling.md), this is the first step of Stage 2 simulation. The input is the model package delivered by M10, and the output is a **functional simulation project** — model loading without warnings, reasonable contact behavior, actuator/sensor modeling complete, and all baseline checks passed. [M12](m12-sim-walking.md) uses it to stand and walk, [M13](m13-rl-training.md) uses it to train policies.

**Prerequisites**: M10 acceptance all passed (model package checked in, inertial parameters verified); PD standing feel from [Stage 0](../stage-0-foundations.md) Step 4 still fresh.

Theoretical background: [Chapter 23 Simulation and Physics Engines](/wiki/chapters/chapter-23/), [Chapter 22 Software Middleware](/wiki/chapters/chapter-22/), [Appendix C Software and Simulation Platform List](/wiki/appendices/appendix-c/); engine selection summary table is in the first step of the [Simulation Environment Setup Playbook](../playbooks/sim-setup.md).

## Step 1: Engine Installation and Official Baseline Verification

【What to Do】Two main paths — choose one (or both):

- **[MuJoCo](/entry/ent_software_mujoco_physics_engine_2022/)**: `pip install mujoco`, runs on CPU only;
- **[Isaac Lab](/entry/ent_software_nvidia_isaac_lab_2024/)** (runs on top of [Isaac Sim](/entry/ent_software_nvidia_isaac_sim_2024/)): Requires NVIDIA GPU, conda environment, strict version matching between Isaac Lab and Isaac Sim — the combination changes with releases, refer to the official installation documentation and verify according to your chosen version.

After installation, first run the official examples (MuJoCo's built-in humanoid model / Isaac Lab's H1 humanoid example), then touch your own model:

```bash
# MuJoCo: CPU only; load the official built-in humanoid model for verification (model path varies by version, verify according to your chosen version)
pip install mujoco
python -m mujoco.viewer --mjcf=$(python -c "import mujoco, os; print(os.path.join(os.path.dirname(mujoco.__file__), 'model', 'humanoid', 'humanoid.xml'))")
# Isaac Lab: conda environment + official H1 example (installation steps and task name follow official documentation)
conda create -n isaaclab python=3.10 -y && conda activate isaaclab
git clone https://github.com/isaac-sim/IsaacLab.git
```

【Why】Official examples help you isolate "environment issues" from "model issues" — if the example fails to run, it's an installation error; if the example runs but your model doesn't, it's a model error. Selection logic (see [Simulation Playbook](../playbooks/sim-setup.md) for details): MuJoCo has high contact quality and is the de facto standard for legged locomotion research; Isaac Lab uses GPU for large-scale parallelization, designed for RL training. Open-source anchors: ToddlerBot uses MuJoCo/MJX, Berkeley Humanoid Lite is based on Isaac Lab, OpenLoong's MPC+WBC is deployed in MuJoCo (see [ToddlerBot](https://github.com/hshi74/toddlerbot), [Berkeley Humanoid Lite](https://github.com/HybridRobotics/Berkeley-Humanoid-Lite), [OpenLoong-Dyn-Control](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/main/README-zh.md) repositories respectively).

【How to Analyze Your Situation】No Nvidia GPU: Stick with MuJoCo all the way — sufficient for control research and small-scale CPU RL; Have an RTX card and going the RL route: Install both — use MuJoCo for model tuning, Isaac Lab for policy training (Berkeley uses this combination); Need full ROS stack integration testing: Add [Gazebo](/entry/ent_software_gazebo/), don't worry about its physics accuracy.

## Step 2: URDF → MJCF/USD Conversion and Verification

【What to Do】Convert your [URDF](/entry/ent_technology_urdf_robot_description_format_2024/) to the target format: MuJoCo can directly compile URDF and save as [MJCF](/entry/ent_technology_mjcf_simulation_format_2024/); for Isaac, use the official URDF Importer to convert to USD:

```bash
# MuJoCo Python API compiles URDF and exports MJCF (API details verify according to your chosen version)
python -c "import mujoco; m = mujoco.MjModel.from_xml_path('robot.urdf'); mujoco.mj_saveLastXML('robot_mjcf.xml', m); print('converted OK')"
```

Four classic conversion errors, check one by one:

| Error | Symptom | Fix |
|---|---|---|
| Inertia tensor not positive definite | Compilation error/model jitter | Go back to M10 Step 3, re-export from CAD, check ixx/iyy/izz triangle inequality |
| mesh units mm treated as m | Model 1000x too large/small | Scale by ×0.001 or unify to meters during export |
| mesh path case sensitivity | File not found on Linux | Normalize paths and filenames to lowercase |
| Joint axis convention differences | Motion direction all reversed | Drive each joint in viewer to verify (M10 did initial check, this is in-simulation re-verification) |

After conversion, manually patch the MJCF: `<compiler angle="radian" .../>` to unify angle units, restore joint limits lost during conversion, confirm coordinate system conventions.

【Why】URDF was designed for visualization and the ROS toolchain, only supports tree structures, and has weak actuator models; MJCF was designed for simulation and control — it automatically calculates inertia at compile time, and actuators and sensors are first-class citizens (Chapter 23, Section 23.4). Every conversion loses information; small errors are amplified by the physics engine into "flies apart on first run".

【How to Analyze Your Situation】Replicating an open-source platform: Use the officially maintained MJCF/USD directly (Berkeley has all three formats, archived), this step only requires per-joint verification; Self-developed model: Put the conversion product and patching records into version control — when you modify the model in M13, you'll know what was changed.

## Step 3: Actuator Modeling — Inflated Limits = Sim-to-Real Suicide

【What to Do】In MJCF, configure an actuator for each controllable joint: use `motor` for force control, `position` for position control; three rules:

1. **Torque limit** = Peak torque from the M01 specification table (already written as effort in M10 Step 4, verify it wasn't lost during conversion);
2. **Velocity limit** = Converted value from M01 rated speed;
3. **Actuator dynamics** approximated with a first-order low-pass filter for real response, time constant initially estimated at 5–20 ms (engineering recommended value, [M14](m14-sim-to-real.md) will backfill with measured values from [system identification](/entry/ent_method_system_identification/)).

```xml
<actuator>
  <!-- ctrlrange fills in peak torque from M01 specification table, strictly no inflation -->
  <position joint="l_knee_pitch" kp="40" forcerange="-33 33" ctrllimited="true" ctrlrange="-1.2 1.2"/>
  <!-- First-order low-pass approximates actuator dynamics: dynprm is time constant (seconds), start with 5–20 ms engineering recommendation -->
  <general joint="l_hip_pitch" dyntype="filter" dynprm="0.01" gaintype="fixed" gainprm="1" ctrllimited="true" ctrlrange="-20 20"/>
</actuator>
```

【Why】RL will learn actions within the limits: if limits are inflated, the policy learns actions the real robot cannot execute, leading to direct sim-to-real failure (M10 Step 4 rule). Real actuators are not ideal torque sources — current loop response and communication delay make them approximate first-order inertial elements; without modeling this dynamic, gains usable in simulation will cause oscillation on the real robot.

【How to Analyze Your Situation】Bus servo / QDD quasi-direct drive: `position` + torque limit is closest to real robot operation; Planning pure force control: `motor` + low-pass filter. If unsure about the time constant, start with an order of magnitude of 10 ms, then calibrate in M14. PD gains written in the model (kp/kv) or in the controller code: writing in the model means no retuning when changing controllers; writing in code facilitates online tuning — choose one and be consistent throughout.

## Step 4: Contact and Friction – Everything for Bipedal Locomotion Happens at the Feet

【Actions】Four steps:

1.  **Foot Friction Coefficient**: For rubber/PLA against a floor, initially try a range of 0.6–1.0 (specific values need to be confirmed based on your materials);
2.  **Contact Solver Parameters**: `solref` (time constant, damping ratio) adjusts contact stiffness – too soft causes foot penetration, too hard leads to numerical jitter; `solimp` controls the constraint impedance curve, start with values near the defaults;
3.  **Self-Collision Pair Pruning**: Use `exclude` to keep only necessary contact pairs; the number of contact pairs directly determines simulation speed;
4.  **Floor and Disturbance Interface**: Parameterize the floor geom, reserve an entry point for external force disturbances – M13's [Domain Randomization](/entry/ent_method_domain_randomization/) needs to randomize friction and push the robot.

```xml
<default>
  <!-- solref=(time constant, damping ratio): typically 2–10×timestep, smaller values mean stiffer contact -->
  <geom solref="0.01 1" solimp="0.9 0.95 0.001" friction="0.8 0.005 0.0001"/>
</default>
<contact><exclude body1="l_thigh" body2="l_shank"/></contact>  <!-- Exclude link pairs that cannot collide -->
```

【Why】Contact parameters are a major source of the sim-to-real gap. They must be calibrated against the "foot material – floor material" pair and included in subsequent domain randomization (Chapter 23, Section 23.4.4). First, get the nominal values reasonable, then consider randomization.

【How to Analyze Your Situation】Unsure about friction: Place a sample of your foot material on the target floor and use a spring scale to pull a slider to estimate the magnitude. A printed PLA foot is quite different from a rubber sole; don't copy others' values.

## Step 5: Sensor Simulation and Observation Pipeline

【Actions】Build the observation pipeline according to the real robot's BOM: [IMU](/entry/ent_component_imu_2024/) (orientation/angular velocity + noise model), joint encoders (position/velocity, can add quantization), foot contact forces; and define the frequency hierarchy:

```xml
<sensor>
  <framequat objtype="site" objname="imu_site" noise="0.001"/>
  <gyro site="imu_site" noise="0.005"/>
  <jointpos joint="l_knee_pitch"/>  <jointvel joint="l_knee_pitch"/>
</sensor>
```

```python
# Physics 1 kHz, Control 100 Hz (engineering suggestion, verify against your controller bandwidth and bus rate)
model.opt.timestep = 0.001   # Physics step size
decimation = 10              # Send control every 10 physics steps → 100 Hz
```

**Hard Rule: Observation interfaces must correspond one-to-one with real robot sensors – observations unavailable on the real robot must not be used in the policy** (a common discipline for M13/M14). Control frequency anchors: ToddlerBot full-state feedback at 50 Hz, Berkeley CAN bus at 250 Hz (see respective survey files).

【Why】Observation is the easiest place to cheat in sim-to-real: ground truth values easily readable in simulation (base linear velocity, center of mass position) do not exist on the real robot. Build the pipeline now based on the real robot's sensor list, so M13 training requires zero rework. Adding noise is not about making things difficult; it's about letting the policy adapt to real sensors in advance.

【How to Analyze Your Situation】Real robot sensors not yet decided: First, go back to the [Sensor Selection Guide](../playbooks/sensor-selection.md) to finalize the BOM. Simulation observations follow the real robot, not the other way around.

## Step 6: Baseline Health Check – Ticket to M12

【Actions】Four checks:

1.  **Zero Torque Release**: Disable actuators, free fall / suspension – model doesn't fall apart, joints have damping and don't flail wildly;
2.  **Initial Keyframe**: Standing posture with zero input for 10 s without drift, center of mass projection remains stable within the support polygon;
3.  **Contact Force Magnitude**: When standing, single foot normal force ≈ half the body weight, not too large or too small;
4.  **Simulation Speed**: Record the real-time factor (RTF), target ≥ 1 (RL throughput is a separate consideration).

【Why】Model-level errors (wrong inertia, reversed axes, missing limits) will all be exposed during PD standing. Checking with passive dynamics is the cheapest method. RTF determines the ceiling for subsequent MPC real-time performance and RL training throughput.

【How to Analyze Your Situation】Model falls apart when suspended: Inertia or joint definition is wrong, go back to M10 Step 3. RTF < 0.5: Check the number of contact pairs, collision mesh complexity, and step size; don't try to brute-force it.

## Acceptance Criteria

- [ ] Official engine examples run successfully (MuJoCo humanoid or Isaac Lab H1), screen recording/logs archived.
- [ ] Model loads without warnings; joint drive directions verified against M10 conventions.
- [ ] Actuator limits (torque/speed/position) match the M01 specification table item by item, no inflated values.
- [ ] Zero-torque suspension/free fall test passed: no disintegration, damping is normal; keyframe standing for 10 s without drift, contact force magnitudes are reasonable.
- [ ] Observation list documented: each item specifies its real robot source (which sensor, what rate), items unavailable on the real robot are marked "Forbidden in Policy".
- [ ] Real-time factor recorded; contact pairs and collision bodies have been pruned.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| MJCF compilation error: inertia tensor not positive definite | Manually written inertia matrix violates physical constraints | Go back to M10 Step 3, re-export from CAD; check ixx/iyy/izz triangle inequality |
| Feet sink into floor or slide like on ice | solref too soft / friction coefficient too low | Go back to Step 4, adjust solref time constant and friction |
| Simulation several times slower than real-time | Too many contact pairs / collision mesh too complex | Prune contact pairs with exclude; simplify collision bodies in M10 Step 5 |
| All joint motion directions reversed | Mixing degrees and radians / axis convention differences | Check compiler angle; verify each joint individually in the viewer |
| Limits lost after URDF to USD conversion | Importer option/version behavior differences | Check limits item by item after conversion, manually add missing ones (verify against your chosen version's Importer documentation) |

## Companion Reading

- Previous Task: [M10 · URDF Modeling and Export](m10-urdf-modeling.md)
- Next Task: [M12 · Simulation Standing and Walking](m12-sim-walking.md)
- Theoretical Background: [Chapter 22 Software Middleware](/wiki/chapters/chapter-22/), [Chapter 23 Simulation and Physics Engines](/wiki/chapters/chapter-23/), [Appendix C Software and Simulation Platform List](/wiki/appendices/appendix-c/)
- [Simulation Environment Setup Guide](../playbooks/sim-setup.md) · [Stage 2 Overview](../stage-2-biped.md)
