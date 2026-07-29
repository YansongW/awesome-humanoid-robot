# Building a Simulation Environment from Scratch: Fall Ten Thousand Times in the Digital World First

Humanoid robots are the last hardware that should be "built first, then tuned": a real robot fall costs hundreds of dollars and a week of work, while falling ten thousand times in simulation costs nothing. But if the simulation is set up incorrectly, it's like self-indulging in a world of wrong physics. This page covers six steps: Choose an engine → Prepare a model → Run control simulation → Prepare a sim-to-real toolbox → Set up benchmarks → Install the environment. For theoretical background, see [Chapter 23: Simulation and Physics Engines](/wiki/chapters/chapter-23/); for control background, see [Chapter 14](/wiki/chapters/chapter-14/) and [Chapter 15](/wiki/chapters/chapter-15/).

## Step 1: Choose a Simulation Engine

**【What to do】** First, clarify the main task, then select the primary engine from the table below (most serious teams use two or more engines for cross-validation to reduce the systematic risk of modeling bias from a single engine—see the selection principles in [Chapter 23](/wiki/chapters/chapter-23/) Section 23.3.8):

| Engine | Physics Kernel | Parallel Capability | Rendering Fidelity | Contact Quality | Typical Positioning |
|---|---|---|---|---|---|
| [MuJoCo](/entry/ent_software_mujoco_physics_engine_2022/) | Proprietary convex contact solver | CPU-based, MJX provides GPU path | Medium | High | Control research, RL training |
| [Isaac Sim](/entry/ent_software_nvidia_isaac_sim_2024/) + [Isaac Lab](/entry/ent_software_nvidia_isaac_lab_2024/) | PhysX | GPU massive parallel | High (RTX ray tracing) | Medium-High | Synthetic data, large-scale RL |
| [Gazebo](/entry/ent_software_gazebo/) | ODE/Bullet/DART (optional) | CPU-based | Medium | Medium | ROS full-stack integration testing |
| [Genesis](/entry/ent_software_genesis_generative_physics_eng_2024/) | Proprietary unified solver (rigid/soft/fluid differentiable unified) | GPU massive parallel | Medium-High | Medium-High (including soft bodies) | General/generative simulation |
| [Drake](/entry/ent_software_drake_systems_toolbox_2024/) | Proprietary (hydroelastic contact) | CPU | Medium-Low | High (research-grade) | Optimal control and formal analysis |

(Table compiled from platform capability comparisons in [Chapter 23](/wiki/chapters/chapter-23/) Section 23.3.8.) Also note a commonly confused role: [Pinocchio](/entry/ent_software_pinocchio/) is not a simulator but an efficient open-source C++ library for rigid body dynamics/kinematics and analytical derivatives—it's almost essential for computing dynamics terms in MPC/WBC and complements simulators.

**【Why】** Each engine has its own foundation: MuJoCo formulates contact dynamics as a convex optimization problem, offering smooth contacts and good physical consistency, and has long been the de facto standard for legged control and deep RL papers (Chapter 23, Section 23.3.1); Isaac Sim's core advantage is photorealistic rendering and support for the GR00T synthetic data pipeline (source: [Isaac Sim](/entry/ent_software_nvidia_isaac_sim_2024/) card), with Isaac Lab providing modular abstractions for RL environments, rewards, and domain randomization, including built-in humanoid task examples like H1/G1; Gazebo has mediocre physics but an irreplaceable ROS ecosystem; Drake excels in rigorous integration of dynamics and mathematical programming; Genesis unifies soft/deformable bodies into a differentiable GPU framework, though its ecosystem is still growing. Real-world open-source project choices can serve as anchors: ToddlerBot uses MuJoCo/MJX for PPO; Berkeley Humanoid Lite is based on Isaac Lab; OpenLoong's MPC+WBC framework is deployed in MuJoCo; Upkie uses PyBullet for zero-cost entry (see the respective repositories: [ToddlerBot](https://github.com/hshi74/toddlerbot), [Berkeley Humanoid Lite](https://github.com/HybridRobotics/Berkeley-Humanoid-Lite), [OpenLoong-Dyn-Control](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/main/README-zh.md), [Upkie](https://github.com/upkie/upkie)).

**【How to analyze your situation】** Decide based on your goal:

- **RL walking/full-body control research** → MuJoCo (Isaac Lab for GPU massive parallel), works even without an NVIDIA GPU.
- **Visual policies, VLA, synthetic data** → Isaac Sim/Lab, provided you have an NVIDIA GPU supporting RTX.
- **ROS/ROS2 full-stack integration and navigation** → Gazebo, don't worry about physics accuracy.
- **MPC/WBC algorithm derivation and validation** → Drake + Pinocchio.
- **Exploring soft foot soles/flexible skin interaction** → Keep an eye on Genesis, but don't rely on it as your only engine.

## Step 2: Prepare the Robot Model

**【What to do】** Four actions:

1. **Format conversion**: Obtain [URDF (Robot Description Format)](/entry/ent_technology_urdf_robot_description_format_2024/) from CAD or existing repositories—the standard XML format in the ROS ecosystem, describing links, joints, inertia, and geometry; then convert to [MJCF (MuJoCo Simulation Format)](/entry/ent_technology_mjcf_simulation_format_2024/) (MuJoCo's `compile` can directly load URDF). For Isaac, an additional conversion to USD is needed. Berkeley Humanoid Lite maintains URDF/MJCF/USD formats simultaneously (source: [Berkeley Humanoid Lite GitHub](https://github.com/HybridRobotics/Berkeley-Humanoid-Lite)), and the habit of "having all three formats" is worth copying.
2. **Collision geometry simplification**: Never use high-polygon visual meshes directly as collision geometry—collision detection will slow down by one to two orders of magnitude. Use convex decomposition or primitive approximations like spheres, capsules, or boxes instead (source: Chapter 23, Section 23.4.3).
3. **Inertial parameter verification**: Trust mass properties in the order of "CAD theoretical values → measured weight values → system identification corrected values." Keep the overall center of mass error within millimeters; otherwise, the balance controller will be constantly "surprised" on the real robot (source: Chapter 23, Section 23.4.4).
4. **Contact parameter calibration**: Calibrate contact stiffness, damping, and friction coefficients for the foot-ground pair based on "foot material-ground material" combinations, and include them in subsequent domain randomization (source: Chapter 23, Section 23.4.4).

**【Why】** URDF was designed for visualization and the ROS toolchain, supporting only tree structures with weak actuator models; MJCF was designed for simulation and control—it automatically computes inertia at compile time, natively supports closed-chain equality constraints, and treats actuators and sensors as first-class citizens (source: Chapter 23, Sections 23.4.1/23.4.2). Each conversion step involves information loss: loss of inertia tensors, differences in joint orientation and limit conventions, and rendering materials versus physics materials being two separate systems (source: Chapter 23, Section 23.4.3). A model's "realism" depends not on the engine but on these modeling details.

**【How to analyze your situation】** For replicating open-source robots: directly use the officially maintained description files (e.g., Upkie's [upkie_description](https://github.com/upkie/upkie_description) URDF repository), focusing your effort on verifying zero positions and actuator parameters. For self-developed robots: first export a simplified URDF to get standing working, then iteratively refine; don't wait for a perfect CAD before entering simulation. Joint zero position calibration is the first step in aligning simulation with the real robot; ToddlerBot designed a 3D-printed zero calibration jig for this, completing calibration in 1 minute (source: [ToddlerBot paper](https://arxiv.org/html/2502.00893v2)).

## Step 3: Run Through the Control Simulation Pipeline

**【What to Do】** Advance in three stages, each with a clear "pass" criterion:

1.  **PID Standing**: Use joint position loop PID to keep the robot standing upright. Pass criterion: Static standing for over 60 seconds, able to recover from a gentle push.
2.  **MPC Walking**: Integrate model-based gait control. You can use Pinocchio for dynamics calculations with a QP solver for MPC; or directly reproduce OpenLoong-Dyn-Control—based on MPC + WBC, including walking, jumping, and blind obstacle stepping examples, deployable in MuJoCo (Source: [OpenLoong-Dyn-Control](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/main/README-zh.md)). Pass criterion: Continuous walking on flat ground for 100 steps without falling, with adjustable step speed.
3.  **RL Training**: Use [PPO (Proximal Policy Optimization)](/entry/ent_algorithm_ppo/) to train walking/full-body policies—it limits policy update step sizes to prevent destructive updates and improve sample efficiency, making it the default starting point for legged RL (Source: PPO Card). The Upkie project includes examples of three balance control paradigms (PID, MPC, Reinforcement Learning with Stable-Baselines3) and a Gymnasium interface (Source: [Upkie GitHub](https://github.com/upkie/upkie)), serving as a ready-made textbook for comparing these paradigms. Training methods are detailed in [Chapter 18](/wiki/chapters/chapter-18/).

**【Why】** The three-stage sequence is critical: PID standing verifies **model correctness** (zero positions, joint axes, mass properties); MPC verifies **dynamics modeling** (actuator models, contact parameters); RL is used to trade computation for policy performance only after confirming "simulation reliability." Both ToddlerBot and BHL achieved zero-shot sim-to-real for RL walking policies (Source: respective survey files), precisely because model calibration was done first.

**【How to Analyze Your Situation】** Time allocation suggestion: If you are a beginner stuck on PID standing, don't panic—model errors found at this stage are the cheapest to fix. Those with a control theory background can quickly pass PID and focus on comparing MPC vs. RL—the final choice for hardware deployment depends on actuator capabilities (servo motors have weak force control, making RL output position targets more practical; QDD motors support force control, making both feasible).

## Step 4: Prepare the Sim-to-Real Toolbox

**【What to Do】** Three tools, prepared in the order of "narrowing the gap, desensitizing, and engineering fallback":

1.  **[System Identification](/entry/ent_method_system_identification/)**: Build models using measured data to "pull" simulation towards reality. For single joints, use sweep/step excitation to fit gain, delay, and friction curves; for the whole robot, optimize inertial parameters using excitation trajectories collected under constraints (Section 23.7.3). ToddlerBot's experience: A single sysID for one motor model can be transferred to all 30 motors (Source: [ToddlerBot Paper](https://arxiv.org/html/2502.00893v2)).
2.  **[Domain Randomization](/entry/ent_method_domain_randomization/)**: Randomize simulation parameters during training to make the policy insensitive to residual errors. Typical randomization items for humanoids: link mass and CoM (on the order of ±10%), joint friction and damping, ground friction, actuator gain and delay, sensor noise, external push disturbances (Section 23.7.2). The range is informed by sysID priors—too wide leads to conservative policies, too narrow leads to transfer failure. Can be combined with observation history for implicit online parameter identification, or use a "narrow-to-wide" curriculum for convergence.
3.  **[Hardware-in-the-Loop (HIL)](/entry/ent_method_hardware_in_the_loop/)**: The in-the-loop ladder before hardware deployment: SiL (Software-in-the-Loop for logic verification) → HIL (control software runs on the real vehicle platform, closed-loop with a real-time simulator via real EtherCAT/CAN bus, verifying real-time performance and communication timing) → Single-joint/single-leg test bench → Full robot first test under gantry protection (Section 23.7.4).

**【Why】** Reality gaps fall into three categories: Parameterizable gaps (mass, friction, delay—narrowed by sysID, covered by domain randomization), Structural gaps (backlash, hysteresis, soft body deformation—addressed by modeling or structural avoidance), and Perception distribution gaps (rendered vs. real image differences—addressed by visual domain randomization or mixing real data) (Section 23.7.1). HIL has special requirements for simulation: it must advance synchronously with wall-clock time (Real-Time Factor RTF = 1); timeouts manifest as bus frame drops on the controller side. Therefore, HIL uses deterministic scheduling and simplified models, not the high-throughput variants used for RL training (Section 23.7.4).

**【How to Analyze Your Situation】** For individual developers with limited budgets: sysID is a must (cost is only time), domain randomization is a must (cost is only computation), HIL can be simplified to a "SiL + single actuator test bench" two-stage process. For institutional teams building full-size robots: the complete in-the-loop ladder is a safety baseline and cannot be cut—the first test of an 80 kg robot must use gantry protection.

## Step 5: Quantify Your Policy with Benchmarks

**【What to Do】** After training your policy, benchmark it on public standards before hardware deployment:

- **[HumanoidBench](/entry/ent_benchmark_humanoidbench/)**: A full-body humanoid benchmark based on the Unitree H1 morphology, with over 40 tasks covering pure locomotion (walking, running, balancing), pure manipulation (reaching, carrying, inserting), and coupled locomotion-manipulation. Unified model and environment parameters enable meaningful cross-algorithm comparisons (Section 23.8.1 and Benchmark Card).
- **[ManiSkill](/entry/ent_benchmark_maniskill/)**: A unified benchmark for generalizable manipulation skills. The third generation, ManiSkill3, GPU-accelerates both physics and rendering parallelism, enabling high-throughput sampling even for manipulation tasks with visual observations. It comes with demonstration data and baselines (Sections 23.3.7/23.8.2). Evaluation methodology is detailed in [Chapter 25: Robot Evaluation System](/wiki/chapters/chapter-25/).

**【Why】** The value of benchmarks is to turn "I trained well" from anecdotal evidence into a quantifiable, comparable protocol. However, their limitations must be clear—HumanoidBench only covers simulation and is tied to the H1 morphology; extrapolation to your robot and real hardware requires additional validation (Section 23.8.1). In engineering, you should also build an "accident-driven scenario library": convert every real-world failure into a reproducible simulation test case for regression testing (Section 23.8.3).

**【How to Analyze Your Situation】** For locomotion research: first run HumanoidBench locomotion tasks to see relative ranking. For manipulation: ManiSkill's demonstration data can save you weeks of data collection. For productization: public benchmarks are just the entry ticket; the private scenario library is the main body.

## Step 6: Hardware Configuration and Installation

**【What to Do】** Prepare hardware and install based on the engine:

- **MuJoCo Route**: Pure CPU is sufficient; start with `pip install mujoco`. ToddlerBot proves the entire "simulation + RL training + deployment" pipeline can be pure Python, installed with a single `pip` command (Python >= 3.10) (Source: [ToddlerBot GitHub](https://github.com/hshi74/toddlerbot)). GPU is only necessary for large-scale parallel training with MJX.
- **Isaac Sim/Lab Route**: Requires an NVIDIA GPU supporting RTX ray tracing with matching driver/CUDA versions. Specific GPU models and minimum VRAM vary with version; check the current version requirements with the supplier (official documentation).
- **Genesis Route**: GPU accelerated; confirm its current version's CUDA requirements before installation.
- **Upkie Zero-Cost Start**: Use `pixi`/`uv` with a single command to run simulation examples, ideal for learning control before buying hardware (Source: [Upkie PyPI](https://pypi.org/project/upkie/)).

**【Why】** 90% of installation issues stem from three sources: NVIDIA driver and CUDA toolkit version mismatch, missing display environment on headless servers (requires EGL/Vulkan offscreen rendering configuration), and dynamic library conflicts from mixed Python environments. First, get the engine's official examples running, then load your own model—isolate "environment issues" from "model issues."

**【How to Analyze Your Situation】** If you only have a laptop (no Nvidia GPU): MuJoCo + CPU training is entirely feasible; small MLP policies are acceptable within days. If you have an RTX gaming card: both Isaac Lab and Genesis can run; VRAM determines the number of parallel environments. Only with a server/multiple GPUs should you consider Isaac Gym-style thousands of parallel environments and end-to-end GPU pipelines (observation and action tensors stay on GPU memory, Section 23.3.3).

## Acceptance Criteria

- The simulator's official example runs on your machine, and you can clearly explain why you chose this engine (referencing the selection table from Step 1).
- The robot model in simulation: each joint's axis and limits are verified one by one, collision bodies are simplified geometries, and the source of inertial parameters is documented (CAD/weighing/sysID level).
- At least the first two stages of the three-stage pipeline (PID standing, MPC walking (or reproducing an open-source MPC example), PPO walking training) are completed, with screen recordings and logs archived for each stage.
- The sim-to-real toolbox has implementation records: sysID data and fitted parameters, domain randomization range list (with justification), SiL/HIL test reports.
- A reproducible baseline score is achieved on at least one public benchmark (HumanoidBench or ManiSkill), with commands and random seeds documented.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Robot "falls apart" or twitches after URDF to MJCF conversion | Missing/incorrect inertial parameters, differences in joint axis conventions | Check `<origin>` and axis for each joint; verify inertial completeness for each link; use `simulate` interactive mode for single-joint excitation test |
| Extremely low simulation frame rate | High-polygon visual meshes used as collision bodies | Replace with convex hull/primitive collision bodies; explicitly disable collision pairs for links that cannot contact |
| Isaac Sim black screen/crash on startup | Driver and CUDA version mismatch, insufficient VRAM | Check official version compatibility matrix; confirm driver with `nvidia-smi`; reduce parallel environment count or disable ray tracing for testing |
| Rendering error on headless server | Missing EGL/Vulkan off-screen rendering configuration | Configure headless rendering environment variables per engine documentation; first run pure physics without rendering for verification |
| RL training curve does not improve | Reward design issues or mismatch between physics step size and control frequency | First reproduce with official baseline environment; check frequency decoupling settings between physics stepping and policy stepping |
| Sim-to-real robot falls immediately | Domain randomization range does not cover real parameters, no sysID performed | Perform actuator sweep identification; check zero position calibration; replay and reproduce real robot failure poses in simulation |
| Controller reports bus frame loss in HIL | Simulation not running at real-time rate (RTF ≠ 1) | Switch to simplified physics model; use real-time kernel + dedicated core for simulation; monitor actual time per frame |

## Companion Reading

- [Stage 0 · Foundation Building](../stage-0-foundations.md) — Getting started with simulation
- [Stage 2 · Biped Platform](../stage-2-biped.md) — From simulation walking to sim-to-real
- [Roadmap Overview](../index.md)
