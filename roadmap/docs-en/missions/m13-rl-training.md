# M13 · Reinforcement Learning Training: Fall Ten Thousand Times in Simulation, Stand Firm Once on the Real Robot

**Global Position**: After the simulation model is tuned (M11) and PD standing is achieved (M12). The input is the simulation environment + your robot model, and the output is an **RL policy for stable walking under domain randomization** (checkpoint), which is passed to M14 for sim-to-real deployment.

**Prerequisites**: M10 model verification passed; M11 environment ready; a GPU capable of running Isaac Lab (VRAM requirements refer to the [Compute Platform Selection Manual](../playbooks/compute-selection.md), check against your chosen environment).

Theoretical background: [PPO](/entry/ent_algorithm_ppo/), [Domain Randomization](/entry/ent_method_domain_randomization/), [Sim-to-Real Transfer](/entry/ent_method_sim_to_real/) cards, [Chapter 18 Imitation Learning and Policy Learning](/wiki/chapters/chapter-18/) and [Chapter 23 Simulation and Physics Engines](/wiki/chapters/chapter-23/); reference implementations can be found in [MuJoCo Playground](/entry/ent_paper_202501_mujoco_playground_2025/) and the official humanoid examples of [Isaac Lab](/entry/ent_software_nvidia_isaac_lab_2024/).

## Step 1: First Run the Official Baseline, Then Talk About Your Own Robot

【What to Do】Don't train your own model on day one. First, run the official humanoid/quadruped walking environment in [Isaac Lab](/entry/ent_software_nvidia_isaac_lab_2024/) (or MuJoCo Playground): train for a few hundred iterations with default settings, confirm the reward curve rises, and the evaluation can walk. Then swap in your URDF/MJCF, **first train a version using the official reward function**.

【Why】The official environment helps you isolate variables: the pipeline (obs/action/reward/reset) is proven correct first, so any remaining problems are "my model/reward" issues. The RL walking of Berkeley Humanoid Lite first reproduced the reference pipeline before migrating to the custom model, ultimately achieving zero-shot sim-to-real (`data/roadmap/research/berkeley-humanoid-lite.md`).

【How to Analyze Your Situation】Insufficient GPU VRAM for 4096 parallel environments: reduce to 512–1024; the curve will be slower but manageable; no NVIDIA GPU: MuJoCo + CPU can also train (an order of magnitude slower), first get the environment logic correct.

## Step 2: Define Observation, Action, and Episode Structure

【What to Do】Write down three lists:

1. **Observation obs**: joint positions/velocities, IMU orientation and angular velocity ([IMU](/entry/ent_component_imu_2024/)), previous action; advanced: add phase clock (sin/cos gait phase). **Do not** stack raw point clouds/images—first learn to walk in state space.
2. **Action action**: target positions for each joint (PD tracking), clipped according to M10's effort/velocity limits; scaling coefficients written as configuration, not hardcoded.
3. **Episode**: duration 10–20 s; termination upon falling (torso pitch exceeding limits, height too low); flat ground with random starting positions.

【Why】Observations determine "what the policy can see": missing something prevents learning (e.g., lacking phase causes gait confusion), too much makes training difficult. Using position targets instead of direct torques allows the underlying PD to absorb the real actuator's non-idealities—this is a key design for sim-to-real, see [Impedance Control](/entry/ent_method_impedance_control/) and [Quasi-Direct Drive Actuator](/entry/ent_technology_quasi_direct_drive_actuator_2024/) cards.

【How to Analyze Your Situation】Do not include observations that are unavailable on the real robot in the policy (e.g., base linear velocity ground truth)—unless you have a state estimation solution, missing observations at deployment = policy failure. First, design the obs pipeline in simulation as "switchable between ground truth/estimated values."

## Step 3: Reward Function—From Standing to Walking

【What to Do】Add reward terms one by one, train a version after each addition and check the curve, **do not add all at once**. Recommended order and typical weight ideas (specific values adjusted per platform, the following are common starting points, requiring self-experimentation and calibration):

| Order | Reward Term | Purpose | Starting Magnitude |
|---|---|---|---|
| 1 | Survival/Upright | Baseline for not falling | +1/step |
| 2 | Linear Velocity Tracking | Track target velocity (first forward/backward, then turning) | exp(-4·err²) |
| 3 | Orientation/Height | Penalty for torso pitch, CoM height | -1·err² |
| 4 | Energy & Smoothness | Penalty for torque, torque change rate | -1e-4·Στ² |
| 5 | Gait Shaping | Double support/swing phase switching, foot lift height | Phase-dependent small weight |

【Why】Reward hacking is the biggest pitfall in RL: rewarding only speed leads to leg shaking in place, rewarding only uprightness leads to standing still. "Add one by one, check one by one" allows you to pinpoint which term is steering the policy wrong. A systematic discussion of reward design is in [Chapter 18 Imitation Learning and Policy Learning](/wiki/chapters/chapter-18/).

【How to Analyze Your Situation】Curve plateau exceeding 2x expected iterations: first check if a penalty term's weight is overwhelming the speed term (most common cause of death), halve the dominant term's weight and retrain. Record configuration and curve screenshots for each experiment—reward tuning is experimental science, not mysticism.

## Step 4: Domain Randomization—Vaccinate the Policy Against Reality

【What to Do】In [Domain Randomization](/entry/ent_method_domain_randomization/), cover at least four categories, with ranges estimated based on your real robot's uncertainty:

| Randomization Item | Suggested Starting Range | Corresponding Real-World Error |
|---|---|---|
| Link Mass/CoM | ±10–15% | Assembly and weighing errors (M10 Step 3) |
| Ground Friction Coefficient | 0.5–1.2 | Differences between floor/tile/carpet |
| Actuator Delay & Strength | Delay 0–20 ms; Torque ×0.85–1.0 | Drive response and battery voltage fluctuations |
| Random Push Disturbance | Every 5–8 s, ≤ 50 N·0.2 s | Collisions and slips |

【Why】The gap between simulation and reality (reality gap) is not a single error but the accumulation of all small errors; domain randomization makes the policy robust to a "range of errors," not overfitted to a "single precise model." Too wide a range prevents learning, too narrow fails on the real robot—start narrow and gradually widen. Theory is in [Chapter 23 Simulation and Physics Engines](/wiki/chapters/chapter-23/).

【How to Analyze Your Situation】Don't know the friction coefficient range? Drag the shoe sole on the target floor to measure (estimate using a spring scale pulling a slider). M14's system identification will later refine actuator delay and mass—first leave the ranges wide.

## Step 5: Training, Evaluation, and Checkpoint Selection

【What to Do】

1. Start with [PPO](/entry/ent_algorithm_ppo/) default hyperparameters (lr 3e-4, clip 0.2, entropy 0.01 are common starting points, need calibration per environment), maximize parallel environments based on VRAM;
2. Save checkpoints every 50–100 iterations, log training curves (reward/ep_len/individual penalty components) to TensorBoard or equivalent tools;
3. **Select checkpoints not by highest reward, but by robust evaluation**: test 100 episodes under maximum randomization strength + push disturbances, pick the one with "lowest fall rate and meets speed target."

【Why】The reward peak in late training is often an illusion of overfitting to the current randomization seed; robust evaluation corresponds to real-world performance. Berkeley's approach is to validate under strong randomization before moving to the real robot (berkeley-humanoid-lite archive).

【How to Analyze Your Situation】Review evaluation videos one by one: stiff gait but can withstand pushes = ready for the real robot (M14 will continue refinement); beautiful gait but falls with a single push = return to Step 4 to widen randomization. Keep 2–3 candidate checkpoints for M14; real robot performance is the final judge.

## Acceptance Criteria

- [ ] Official baseline environment successfully reproduced (screenshots/curves archived).
- [ ] Three lists (obs/action/episode) documented and aligned with real robot available observations.
- [ ] Complete record of adding reward terms one by one, final configuration and curves archived.
- [ ] Domain randomization covers mass/friction/delay/push four categories, ranges have estimation basis.
- [ ] Robust evaluation (max randomization + disturbances) shows fall rate ≤ 10% over 100 consecutive episodes, forward speed meets target.
- [ ] 2–3 candidate checkpoints archived for M14 real robot screening.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Reward not increasing | Imbalanced reward weights / Missing key observations / Incorrect action scaling | Reduce rewards one by one to locate the issue; check against the checklist in Step 2; print the actual range of actions |
| Shaking in place without moving forward | Speed term weight too low / Joint torque limits too restrictive | Increase speed tracking weight; verify effort limits (M10 Step 4) |
| Training diverges, curve collapses | Learning rate too high / Reward values exploding (a component's magnitude out of control) | Halve the learning rate; print normalization per component |
| Simulation works well, but falls immediately upon randomization | Randomization range too wide in one step | Halve the range, then widen it by one step every 500 iterations (curriculum-style) |
| Policy is "biased" toward one side's leg | Model asymmetry left-right (URDF mirroring error) | Return to M10 to check mirrored joint axes |

## Supporting Reading

- Previous task: [M12 · Simulation Standing and Walking](m12-sim-walking.md)
- Next task: [M14 · Sim-to-Real Deployment and Walking Acceptance](m14-sim-to-real.md)
- Theoretical background: [Chapter 18 Imitation Learning and Policy Learning](/wiki/chapters/chapter-18/), [Chapter 23 Simulation and Physics Engines](/wiki/chapters/chapter-23/)
- [Simulation Environment Setup Guide](../playbooks/sim-setup.md) · [Stage 2 Overview](../stage-2-biped.md)
