# M12 · Simulation Standing and Walking: First Stand Firm, Then Walk

**Global Position**: Immediately follows [M11 Simulation Engineering Ready](m11-sim-setup.md). Input is a simulation model that can be loaded with reasonable contacts; output is **two deliverables**: ① A PD standing demo (10 minutes without falling + recovery from pushes); ② A written walking technical route decision (classic MPC/WBC or RL) — [M13](m13-rl-training.md) will delve deeper into the RL training path.

**Prerequisites**: All M11 acceptance checks passed (all four baseline health checks passed); the PD standing feel from [Stage 0](../stage-0-foundations.md) is still fresh — this task's Step 1 is its scaled-up version.

Theoretical Background: [Chapter 14 Fundamentals of Robot Control](/wiki/chapters/chapter-14/), [Chapter 15 Motion Generation and Locomotion](/wiki/chapters/chapter-15/), [Chapter 23 Simulation and Physics Engines](/wiki/chapters/chapter-23/); the complete balance theory ladder is in [Stage 2 Overview](../stage-2-biped.md) Section 2.

## Step 1: PD Standing — The Ticket to Walking

[What to Do] Three things in order:

1. **Design a Zero-Moment Standing Posture**: Target joint angles (ankle/knee/hip compensation) so the center of mass projection falls near the center of the support polygon — start with M11's keyframe, fine-tune until no drift;
2. **Position PD Control**: Follow M11's frequency layering (physics at 1 kHz, control on the order of 100 Hz):

```python
# Position PD main loop: target angle tracking + torque limiting (limiting consistent with M11 Step 3)
tau = kp * (q_des - q) - kd * dq
tau = np.clip(tau, -tau_max, tau_max)
```

3. **Stepwise Acceptance Criteria**: 10 s → 60 s → 10 min without falling; then apply a small impulse disturbance to the torso, recovery is required to pass. Gain tuning: P first, then D — increase P until just before oscillation, then use D to suppress oscillation; for high-frequency oscillation, reduce P first; if still oscillating, check the simulation timestep.

[Why] Standing is a subset of walking: once the standing loop (ankle/hip strategy) is tuned, walking is just periodically shifting the balance point out of the support polygon and recapturing it (per the [Stage 2](../stage-2-biped.md) reproduction flow Step 7). PD standing validates **model correctness** — zero position, axes, mass properties (the first stage of the three-stage rocket in the [Simulation Playbook](../playbooks/sim-setup.md)). If this step fails, everything after is wasted effort.

[How to Analyze Your Situation] If it can't stand, don't rush to tune parameters. Troubleshoot in the order "model error → gain error → timestep error": Has the zero-moment suspension test passed (M11 Step 6)? Has the center of mass projection been calculated? Does halving the gains change the behavior?

## Step 2: Balance Theory Ladder — ZMP, LIPM, and Hierarchical Architecture

[What to Do] Work through the three levels in order (see [Stage 2](../stage-2-biped.md) Section 2 for details):

1. **[ZMP (Zero Moment Point)](/entry/ent_paper_zero_moment_point_2024/)**: The equivalent point of ground reaction force must lie within the support polygon to avoid tipping. In simulation, plot/print the ZMP trajectory and observe when it leaves the support polygon and when the robot falls;
2. **LIPM (Linear Inverted Pendulum Model)**: Simplify the whole body to a "center of mass + massless legs". Under the constant center of mass height assumption, there is an analytical solution, and for flat ground ZMP estimation:

```
# Flat ground LIPM approximation: x_zmp = x_com - (z_com / g) * x_ddot_com
x_zmp = x_com - (z_com / 9.81) * x_ddot_com
```

3. **[Gait Planning](/entry/ent_method_gait_planning/) and Hierarchical Architecture**: Given a target velocity, determine the swing foot placement and the timing of double support/swing phase transitions (classic entry point is LIPM + capture point analysis: predict where you would fall without stepping, and step there); and establish a hierarchical understanding: **Footstep planning → Center of mass trajectory → WBC allocation → Joint torques**.

[Why] ZMP is the most classic criterion for bipedal stability and the primary tool for diagnosing all falls. The hierarchical architecture allows you to pinpoint whether "walking crooked" is due to wrong foot placement (decision layer) or insufficient force control (execution layer). Without building this understanding before jumping into RL, you won't know if a fall is due to a model error or a control error. Systematic derivation is in [Chapter 14](/wiki/chapters/chapter-14/) and [Chapter 15](/wiki/chapters/chapter-15/).

[How to Analyze Your Situation] For the RL route: conceptual understanding is sufficient (the policy learns foot placement itself), but the ZMP observation exercise is mandatory; for the MPC route: the LIPM derivation must be thoroughly understood, as it is the prediction model for MPC in Step 3.

## Step 3: Classic Route Hands-On — Run OpenLoong MPC+WBC

[What to Do] Run OpenLoong-Dyn-Control: An MPC+WBC whole-body control framework deployed on [MuJoCo](/entry/ent_software_mujoco_physics_engine_2022/), with built-in **walking/jumping/blind obstacle stepping** examples. It has been implemented on a physical prototype for walking and blind obstacle stepping, Apache-2.0 ([OpenLoong-Dyn-Control](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/main/README-zh.md)):

```bash
git clone https://github.com/loongOpen/OpenLoong-Dyn-Control.git
# Dependency installation and compilation strictly follow the repository README (versions change with repository updates; verify against your chosen version)
```

After running it, **modify it hands-on** and record: MPC weights, step frequency, step length. For each modification, record the change in walking quality (stability/speed tracking/oscillation). Also clarify the division of labor: [MPC (Model Predictive Control)](/entry/ent_method_model_predictive_control/) rolls out predictions over a time horizon, solves a constrained optimization, and handles "how to step and how much force to use in the next few steps"; [WBC (Whole-Body Control)](/entry/ent_method_whole_body_control/) distributes task objectives to joint torques according to priority, handling "how much force each joint outputs in this instant"; [Pinocchio](/entry/ent_software_pinocchio/) is an efficient rigid body dynamics library, almost essential for MPC/WBC to compute dynamics terms.

[Why] This is a ready-made textbook for learning the classic control pipeline of a full-size humanoid without hardware — the Qinglong robot is 185 cm/80 kg+, which an individual cannot replicate, but the control framework can be freely studied (per the archive's scope). Modifying parameters yourself and seeing the change in walking quality builds intuition faster than reading ten papers.

[How to Analyze Your Situation] If compilation fails: strictly verify dependency versions against the repository README; do not upgrade on your own. If you can't follow the math: first treat it as a "tunable black box", record the "parameter → phenomenon" correspondence, and catch up on the derivations later.

## Step 4: RL Route Preview — Only Prove the Pipeline Works, Don't Start Training

[What to Do] Only one thing: get the official environment you'll use in M13 running on your machine — [Isaac Lab](/entry/ent_software_nvidia_isaac_lab_2024/) humanoid example or [MuJoCo Playground](/entry/ent_paper_202501_mujoco_playground_2025/). Confirm that the obs/action/reward data flow can run, and record FPS and GPU memory/CPU usage:

```bash
# Isaac Lab official humanoid environment smoke test (task name and script path: verify against your chosen version's official documentation)
./isaaclab.sh -p <official RL example script> --task=<humanoid task name> --num_envs=16 --headless --max_iterations=2
# Record: FPS, nvidia-smi GPU memory usage, obs/action dimensions
```

**Do not start training**: Running the official baseline, swapping in your own model, and tuning rewards are tasks for [M13](m13-rl-training.md) Steps 1–3. This step is only a pipeline rehearsal to prove "it can run on this machine".

[Why] The environment/dependency/version issues in the RL stack are extremely time-consuming. Exposing them now means M13 can start training directly; FPS and hardware usage data determine how to set the number of parallel environments in M13 ([PPO](/entry/ent_algorithm_ppo/) is throughput-hungry).

[How to Analyze Your Situation] No Nvidia GPU: Use MuJoCo Playground/MJX or a CPU-based small-scale environment to first verify the data flow; with a GPU: Run the Isaac Lab official humanoid task for two iterations or load an official pre-trained checkpoint for evaluation, and save screenshots of the data flow logs.

## Step 5: Route Decision – Write It Down, Don't Drift

【What to Do】Select a main route by comparing the table below and record it in the build log (you can try both, but clearly state the primary and secondary routes and your reasoning):

| Dimension | Classic MPC/WBC | RL ([PPO](/entry/ent_algorithm_ppo/) + Domain Randomization) |
|---|---|---|
| Development Effort | High derivation and implementation effort, but OpenLoong provides a ready-to-learn framework | Training pipeline is ready; reward engineering is the new workload |
| Mathematical Threshold | High (dynamics + optimization) | Medium (concepts are sufficient to start; tuning rewards is experimental science) |
| Hardware Requirements | CPU is sufficient (MuJoCo) | Nvidia GPU is smoother for training (Isaac Lab); CPU works but is an order of magnitude slower |
| Interpretability | High – every torque has a clear source | Low – the policy is a black box |
| Real Robot Examples | BRUCE achieves walking/running/jumping with variable-period MPC (bruce-westwood.md) | ToddlerBot, Berkeley achieve zero-shot [sim-to-real](/entry/ent_method_sim_to_real/) walking (various files) |

【Why】Both paths lead to success, but your time only allows for one main route; writing down the decision ensures you don't drift when troubleshooting in M13/[M14](m14-sim-to-real.md). The same logic from the [Stage 2](../stage-2-biped.md) decision tree applies: the core KPI for the first robot is "get it walking," not achieving perfection in one go.

【How to Analyze Your Situation】Strong math + want to deeply understand control → MPC/WBC main route, OpenLoong is your textbook; ML background + have a GPU → RL main route straight to M13; want to try both → RL as main route, read OpenLoong code as a secondary route to understand control structure (or vice versa), but the log must clearly state which is the main route.

## Acceptance Criteria

- [ ] PD standing: 10 minutes of simulation time without falling; recovers after a gentle push to the torso (save screen recording).
- [ ] ZMP observation documented: whether the ZMP stays within the support polygon during standing and after a push, with figures and conclusions.
- [ ] At least one OpenLoong example or official RL environment runs successfully (screen recording + record of parameter changes/data flow).
- [ ] Route decision documented in writing: main/secondary route, reasoning, expected risks, recorded in the build log.
- [ ] If the main route is RL: confirm the official environment required for M13 runs, with FPS and hardware usage recorded.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| PD standing: high-frequency jitter, buzzing | P gain too high / simulation step size too large | Halve P and retest; reduce step size for comparison; check if damping was mistakenly written as stiffness |
| Standing: slowly tilting to one side | CoM projection deviates from support polygon center / model asymmetry left-right | Print CoM projection; go back to M10 to check mirrored joint axes |
| Standing: feet sliding, unable to stay upright | Friction coefficient too low or contact too soft | Go back to M11 Step 4 to adjust friction and solref |
| Falls with one push, cannot recover | D gain insufficient / ankle torque limit too restrictive | Increase D and retest; check ankle actuator limits (M11 Step 3) |
| Jumping straight to RL, unable to tell whose fault the fall is | Skipped the balance theory ladder | Go back to Step 2 for ZMP observation; discuss RL only after PD standing acceptance |
| OpenLoong example fails to run | Dependency version mismatch | Strictly follow the repository README to check versions; do not upgrade dependencies on your own |

## Companion Reading

- Previous task: [M11 · Simulation Environment and Model Conversion](m11-sim-setup.md)
- Next task: [M13 · Reinforcement Learning Training](m13-rl-training.md)
- Theoretical background: [Chapter 14 Fundamentals of Robot Control](/wiki/chapters/chapter-14/), [Chapter 15 Motion Generation and Locomotion](/wiki/chapters/chapter-15/), [Chapter 23 Simulation and Physics Engines](/wiki/chapters/chapter-23/), [Appendix C Software and Simulation Platform List](/wiki/appendices/appendix-c/)
- [Simulation Environment Setup Guide](../playbooks/sim-setup.md) · [Stage 2 Overview](../stage-2-biped.md)
