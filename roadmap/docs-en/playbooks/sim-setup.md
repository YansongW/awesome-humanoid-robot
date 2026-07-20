# Building a Simulation Environment from Scratch: Fall Ten Thousand Times in the Digital World First

> ⚠️ The content of this roadmap is compiled based on public information and theoretical knowledge, and has not been verified on actual hardware; please verify safety specifications yourself when involving electrical and mechanical operations.

Humanoid robots are the hardware that should least be "built first and tuned later": a real fall costs hundreds of dollars and a week of work, while falling ten thousand times in simulation costs nothing. But if the simulation is set up incorrectly, it's like indulging in a world with wrong physics. This page covers six steps: Choose Engine → Prepare Model → Run Control Simulation → Prepare Sim-to-Real Toolbox → Run Benchmarks → Set Up Environment. For theoretical background, see [Chapter 23: Simulation and Physics Engines](/wiki/chapters/chapter-23/); for control background, see [Chapter 14](/wiki/chapters/chapter-14/) and [Chapter 15](/wiki/chapters/chapter-15/).

## Step 1: Choose a Simulation Engine

**【What to do】** First, clarify the main task, then refer to the table below to select the primary engine (most serious teams use two or more engines for cross-validation to reduce the systemic risk of modeling bias from a single engine—see the selection principles in [Chapter 23](/wiki/chapters/chapter-23/), Section 23.3.8):

| Engine | Physics Kernel | Parallel Capability | Rendering Fidelity | Contact Quality | Typical Positioning |
|---|---|---|---|---|---|
| [MuJoCo](/entry/ent_software_mujoco_physics_engine_2022/) | Proprietary convex contact solver | CPU-based, MJX provides GPU path | Medium | High | Control research, RL training |
| [Isaac Sim](/entry/ent_software_nvidia_isaac_sim_2024/) + [Isaac Lab](/entry/ent_software_nvidia_isaac_lab_2024/) | PhysX | GPU massive parallel | High (RTX ray tracing) | Medium-High | Synthetic data, large-scale RL |
| [Gazebo](/entry/ent_software_gazebo/) | ODE/Bullet/DART (selectable) | CPU-based | Medium | Medium | ROS full-stack integration testing |
| [Genesis](/entry/ent_software_genesis_generative_physics_eng_2024/) | Proprietary unified solver (rigid/soft/fluid differentiable unified) | GPU massive parallel | Medium-High | Medium-High (including soft bodies) | General/generative simulation |
| [Drake](/entry/ent_software_drake_systems_toolbox_2024/) | Proprietary (hydroelastic contact) | CPU | Medium-Low | High (research-grade) | Optimal control and formal analysis |

(Table compiled from the platform capability comparison in [Chapter 23](/wiki/chapters/chapter-23/), Section 23.3.8.) There is also a role that is easily confused: [Pinocchio](/entry/ent_software_pinocchio/) is not a simulator, but an efficient open-source C++ library for rigid body dynamics/kinematics and analytical derivative computation—it is almost essential for computing dynamics terms when doing MPC/WBC, complementing the simulator.

**【Why】** Each engine has its own foundation: MuJoCo formulates contact dynamics as a convex optimization problem, resulting in smooth contacts and good physical consistency, making it the de facto standard for legged control and deep RL papers for a long time (Chapter 23, Section 23.3.1); Isaac Sim's core advantage is photorealistic rendering, supporting the GR00T synthetic data pipeline (source: [Isaac Sim](/entry/ent_software_nvidia_isaac_sim_2024/) card), and Isaac Lab provides modular abstractions for RL environments, rewards, and domain randomization on top of it, with built-in humanoid task examples like H1/G1; Gazebo has mediocre physics but an irreplaceable ROS ecosystem; Drake excels in the rigorous combination of dynamics and mathematical programming; Genesis unifies soft/deformable bodies into a differentiable GPU framework, but its ecosystem is still accumulating. Actual choices from open-source projects can serve as anchors: ToddlerBot uses MuJoCo/MJX for PPO; Berkeley Humanoid Lite is based on Isaac Lab; OpenLoong's MPC+WBC framework is deployed on MuJoCo; Upkie uses PyBullet for zero-cost entry (source: data/roadmap/research/ various files).

**【How to analyze your situation】** Decide based on your goals:

- **RL locomotion/full-body control research** → MuJoCo (Isaac Lab if you need GPU massive parallel), works even without an Nvidia GPU.
- **Visual policies, VLA, synthetic data** → Isaac Sim/Lab, prerequisite: an NVIDIA GPU with RTX support.
- **ROS/ROS2 full-stack integration and navigation** → Gazebo, don't worry about physics accuracy.
- **MPC/WBC algorithm derivation and verification** → Drake + Pinocchio.
- **Experimenting with soft soles/flexible skin interaction** → Keep an eye on Genesis, but don't rely on it as your only engine.

## Step 2: Prepare the Robot Model

**【What to do】** Four actions:

1. **Format conversion**: Obtain [URDF (Robot Description Format)](/entry/ent_technology_urdf_robot_description_format_2024/) from CAD or existing repositories—the standard XML format in the ROS ecosystem, describing links, joints, inertia, and geometry; then convert to [MJCF (MuJoCo Simulation Format)](/entry/ent_technology_mjcf_simulation_format_2024/) (MuJoCo's `compile` can directly load URDF). For Isaac, an additional conversion to USD is needed. Berkeley Humanoid Lite maintains URDF/MJCF/USD three formats simultaneously (source: data/roadmap/research/berkeley-humanoid-lite.md), and the habit of "keeping all three formats" is worth copying.
2. **Collision geometry simplification**: Never use high-polygon visual meshes directly as collision geometry—collision detection will be one to two orders of magnitude slower; use convex decomposition or primitive approximations like spheres/capsules/boxes instead (source: Chapter 23, Section 23.4.3).
3. **Inertial parameter verification**: Adopt a hierarchical approach for mass properties: "CAD theoretical values → measured weight values → system identification corrected values", keeping the whole-body center of mass error at the millimeter level; otherwise, the balance controller will be constantly "surprised" on the real robot (source: Chapter 23, Section 23.4.4).
4. **Contact parameter calibration**: Calibrate contact stiffness, damping, and friction coefficients between the foot sole and ground in pairs based on "foot sole material - ground material", and include them in subsequent domain randomization (source: Chapter 23, Section 23.4.4).

**【Why】** URDF was designed for visualization and the ROS toolchain, supporting only tree structures with weak actuator models; MJCF was designed for simulation and control—it automatically calculates inertia at compile time, natively supports closed-chain equality constraints, and treats actuators and sensors as first-class citizens (source: Chapter 23, Sections 23.4.1/23.4.2). Each conversion step incurs information loss: loss of inertia tensors, differences in joint orientation and limit conventions, and the fact that rendering materials and physics materials are two separate systems (source: Chapter 23, Section 23.4.3). The model's "realism" depends not on the engine but on these modeling details.

**【How to analyze your situation】** For replicating open-source robot models: directly use the officially maintained description files (e.g., Upkie's `upkie_description` URDF repository, source: data/roadmap/research/upkie.md), focusing your effort on verifying zero positions and actuator parameters. For self-developed models: first export a simplified URDF to get standing working, then iterate and refine; don't wait for a perfect CAD before entering simulation. Joint zero position calibration is the first step in aligning simulation with the real robot; ToddlerBot designed a 3D-printed zero-point calibration fixture for this, completing calibration in 1 minute (source: data/roadmap/research/toddlerbot.md).

## Step 3: Run Through the Control Simulation Pipeline

**【What to Do】** Propel in three stages, each with a clear "pass" criterion:

1.  **PID Standing**: Use joint position loop PID to keep the robot standing upright. Pass criterion: Stands statically for over 60 seconds and recovers from a gentle push.
2.  **MPC Walking**: Integrate model-based gait control. You can use Pinocchio for dynamics calculations with a QP solver for MPC, or directly reproduce OpenLoong-Dyn-Control—based on MPC + WBC, including walking, jumping, and blind obstacle stepping examples, deployable on MuJoCo (Source: `data/roadmap/research/openloong-qinglong.md`). Pass criterion: Walks continuously on flat ground for 100 steps without falling, with adjustable step speed.
3.  **RL Training**: Use [PPO (Proximal Policy Optimization)](/entry/ent_algorithm_ppo/) to train walking/full-body policies—it limits policy update step sizes to prevent destructive updates and improve sample efficiency, making it the default starting point for legged RL (Source: PPO card). The Upkie project comes with examples of three balancing control paradigms (PID, MPC, Reinforcement Learning via Stable-Baselines3) and a Gymnasium interface (Source: `data/roadmap/research/upkie.md`), serving as a ready-made textbook for comparing the three paradigms. See [Chapter 18](/wiki/chapters/chapter-18/) for training methods.

**【Why】** The three-stage sequence cannot be altered: PID standing validates **model correctness** (zero position, axes, mass properties); MPC validates **dynamics modeling** (actuator model, contact parameters); RL uses computational power for policy performance only after confirming "simulation fidelity." Both ToddlerBot and BHL achieved zero-shot sim-to-real for RL walking policies (Source: respective research files), precisely because model calibration was done first.

**【How to Analyze Your Situation】** Time allocation suggestion: Beginners stuck on PID standing should not panic—model errors exposed at this stage are the cheapest to fix. Those with a control theory background can quickly pass PID and focus on comparing MPC vs. RL—the final choice for hardware deployment depends on actuator capabilities (servo motors have weak force control, making RL position targets more realistic; QDD motors support force control, making both feasible).

## Step 4: Prepare the Sim-to-Real Toolbox

**【What to Do】** Three tools, prepared in the order of "shrink the gap, desensitize, engineering safety net":

1.  **[System Identification](/entry/ent_method_system_identification/)**: Build models from measured data to "pull" simulation towards reality. For single joints, use sweep/step excitation to fit gain, delay, and friction curves. For the whole robot, collect excitation trajectories under constraints to optimize inertial parameters (Chapter 23, Section 23.7.3). ToddlerBot's experience: SysID performed once on one motor model can be transferred to all 30 motors (Source: `data/roadmap/research/toddlerbot.md`).
2.  **[Domain Randomization](/entry/ent_method_domain_randomization/)**: Randomize simulation parameters during training to make policies insensitive to residual errors. Typical randomization items for humanoids: link mass and center of mass (±10% order), joint friction and damping, ground friction, actuator gain and delay, sensor noise, external push disturbances (Chapter 23, Section 23.7.2). The range is informed by sysID priors—too wide leads to conservative policies, too narrow leads to transfer failure. Can be combined with observation history for implicit online parameter identification, or use a "narrow-to-wide" curriculum for convergence.
3.  **[Hardware-in-the-Loop (HIL)](/entry/ent_method_hardware_in_the_loop/)**: The in-the-loop ladder before hardware deployment: SiL (Software-in-the-Loop for logic validation) → HIL (control software runs on the real vehicle platform, closed-loop with a real-time simulator via real EtherCAT/CAN bus, validating real-time performance and communication timing) → Single-joint/single-leg test bench → Full robot first test under gantry protection (Chapter 23, Section 23.7.4).

**【Why】** Reality gaps fall into three categories: Parameterizable gaps (mass, friction, delay—shrunk by sysID, covered by domain randomization), Structural gaps (backlash, hysteresis, soft body deformation—addressed by modeling supplements or structural avoidance), Perception distribution gaps (rendered vs. real image differences—addressed by visual domain randomization or mixed real data) (Chapter 23, Section 23.7.1). HIL has special requirements for simulation: it must run synchronously with wall-clock time (Real-Time Factor RTF = 1); timeouts manifest as bus frame drops on the controller side. Hence, HIL uses deterministic scheduling and simplified models, not the high-throughput variants used for RL training (Chapter 23, Section 23.7.4).

**【How to Analyze Your Situation】** For budget-constrained individual developers: SysID is a must (costs only time), domain randomization is a must (costs only compute), HIL can be simplified to a "SiL + single actuator test bench" two-stage process. For institutional teams working on full-size robots: The complete in-the-loop ladder is a safety baseline and cannot be cut—first tests of an 80 kg robot must use gantry protection.

## Step 5: Quantify Your Policy with Benchmarks

**【What to Do】** After training your policy, benchmark it on public standards before hardware deployment:

-   **[HumanoidBench](/entry/ent_benchmark_humanoidbench/)**: A full-body humanoid benchmark based on the Unitree H1 morphology, with over 40 tasks covering pure locomotion (walking, running, balancing), pure manipulation (reaching, carrying, inserting), and coupled locomotion-manipulation. Unified model and environment parameters enable meaningful cross-algorithm comparisons (Chapter 23, Section 23.8.1 and benchmark card).
-   **[ManiSkill](/entry/ent_benchmark_maniskill/)**: A unified benchmark for generalizable manipulation skills. The third generation, ManiSkill3, GPU-accelerates both physics and rendering parallelism, enabling high-throughput sampling for manipulation tasks with visual observations. It comes with demonstration data and baselines (Chapter 23, Sections 23.3.7/23.8.2). See [Chapter 25: Robot Evaluation System](/wiki/chapters/chapter-25/) for evaluation methodology.

**【Why】** The value of benchmarks is to turn "I trained it well" from anecdotal evidence into a quantifiable, comparable protocol. Their limitations must also be clear: HumanoidBench only covers simulation and is tied to the H1 morphology; extrapolation to your robot model and real hardware requires additional validation (Chapter 23, Section 23.8.1). Engineering-wise, you should also build an "accident-driven scenario library": convert every real-world failure into a reproducible simulation test case for regression testing (Chapter 23, Section 23.8.3).

**【How to Analyze Your Situation】** For locomotion research: First run HumanoidBench locomotion tasks to see relative ranking. For manipulation: ManiSkill's demonstration data can save you weeks of data collection. For productization: Public benchmarks are just the entry ticket; your private scenario library is the main body.

## Step 6: Hardware Configuration and Installation

**【What to Do】** Prepare hardware and install based on the engine:

-   **MuJoCo Route**: Pure CPU is sufficient; start with `pip install mujoco`. ToddlerBot proves the entire "simulation + RL training + deployment" pipeline can be pure Python, installed with a single `pip` command (Python >= 3.10) (Source: `data/roadmap/research/toddlerbot.md`). GPU is only necessary for MJX large-scale parallel training.
-   **Isaac Sim/Lab Route**: Requires an NVIDIA GPU supporting RTX ray tracing with matching driver/CUDA versions. Specific GPU models and minimum VRAM vary with version; check current requirements with the supplier (official documentation).
-   **Genesis Route**: GPU accelerated; check its current CUDA requirements before installation.
-   **Upkie Zero-Cost Start**: Run simulation examples with a single `pixi`/`uv` command, ideal for learning control before buying hardware (Source: `data/roadmap/research/upkie.md`).

**【Why】** 90% of installation issues stem from three areas: NVIDIA driver and CUDA toolkit version mismatch, missing display environment on headless servers (requires EGL/Vulkan off-screen rendering configuration), and Python environment conflicts causing dynamic library clashes. First, get the engine's official example running, then load your own model—this isolates "environment issues" from "model issues."

**【How to Analyze Your Situation】** Laptop only (no NVIDIA GPU): MuJoCo + CPU training is entirely feasible; small MLP policies are acceptable within days. One RTX gaming GPU: Isaac Lab and Genesis can both run; VRAM determines the number of parallel environments. Server/multi-GPU: Only then consider Isaac Gym-style thousands of parallel environments and end-to-end GPU pipelines (observation and action tensors stay on GPU, Chapter 23, Section 23.3.3).

## Acceptance Criteria

-   The simulator's official example runs on your machine, and you can clearly explain why you chose this engine (referencing the selection table from Step 1).
-   The robot model in simulation: Joint axes/limits are verified one by one, collision bodies are simplified geometries, and the source of inertial parameters is documented (CAD/weighing/sysID level).
-   At least the first two of the three-stage process (PID standing, MPC walking or open-source MPC example reproduction, PPO walking training) are completed, with screen recordings and logs archived for each stage.
-   The sim-to-real three-tool set has implementation records: SysID data and fitted parameters, domain randomization range list (with justification), SiL/HIL test reports.
-   A reproducible baseline score is obtained on at least one public benchmark (HumanoidBench or ManiSkill), with commands and random seeds documented.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Robot "falls apart" or twitches after URDF to MJCF conversion | Missing/incorrect inertial parameters, differences in joint axis conventions | Check `<origin>` and axis for each joint; verify inertial completeness for each link; use `simulate` interactive mode for single-joint excitation test |
| Extremely low simulation frame rate | High-polygon visual meshes used as collision bodies | Replace with convex hull/primitive collision bodies; explicitly disable collision pairs for links that cannot contact |
| Isaac Sim starts with black screen/crashes | Mismatched driver and CUDA versions, insufficient VRAM | Check official version compatibility matrix; confirm driver with `nvidia-smi`; reduce parallel environment count or disable ray tracing to test |
| Rendering error on headless server | Missing EGL/Vulkan off-screen rendering configuration | Configure headless rendering environment variables per engine documentation; first run pure physics without rendering to verify |
| RL training curve does not improve | Reward design issues or mismatch in physics step size/control frequency | First reproduce with official baseline environment; check frequency decoupling settings between physics stepping and policy stepping |
| Sim-to-real fails immediately on hardware | Domain randomization range does not cover real parameters, no system identification performed | Perform actuator sweep identification; check zero-position calibration; replay real-world failure postures in simulation |
| Controller reports bus frame loss during HIL | Simulation not running at real-time rate (RTF ≠ 1) | Switch to simplified physics model; use real-time kernel + dedicated core for simulation; monitor per-frame actual time consumption |

## Supplementary Reading

- [Stage 0 · Foundations](../stage-0-foundations.md) — Entry path for first simulation experience
- [Stage 2 · Biped Platform](../stage-2-biped.md) — From simulation walking to sim-to-real
- [Roadmap Overview](../index.md)
