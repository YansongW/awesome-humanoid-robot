# M13 · Reinforcement Learning Training: Fall Ten Thousand Times in Simulation, Stand Firm Once on the Real Robot

**Global Position**: After the simulation model is tuned (M11) and PD standing is achieved (M12). The input is the simulation environment + your robot model, and the output is an **RL policy for stable walking under domain randomization** (checkpoint), which is handed over to M14 for sim-to-real deployment.

**Prerequisites**: M10 model verification passed; M11 environment ready; a GPU capable of running Isaac Lab (VRAM requirements refer to the [Compute Platform Selection Guide](../playbooks/compute-selection.md), check according to your chosen environment).

Theoretical background: [PPO](/entry/ent_algorithm_ppo/), [Domain Randomization](/entry/ent_method_domain_randomization/), [Sim-to-Real Transfer](/entry/ent_method_sim_to_real/) cards, [Chapter 18 Imitation Learning and Policy Learning](/wiki/chapters/chapter-18/) and [Chapter 23 Simulation and Physics Engines](/wiki/chapters/chapter-23/); reference implementations can be found in the official humanoid examples from [MuJoCo Playground](/entry/ent_paper_202501_mujoco_playground_2025/) and [Isaac Lab](/entry/ent_software_nvidia_isaac_lab_2024/).

## Step 1: First Run the Official Baseline, Then Tackle Your Own Robot

[What to do] Do not train your own model on day one. First, run the official humanoid/quadruped walking environment in [Isaac Lab](/entry/ent_software_nvidia_isaac_lab_2024/) (or MuJoCo Playground): train for a few hundred iterations with default settings, confirm the reward curve rises, and the evaluation shows walking capability. Then, swap in your URDF/MJCF, and **first train a version using the official reward function**.

[Why] The official environment helps you isolate variables: the pipeline (obs/action/reward/reset) is proven correct first, so any remaining issues are "my model/reward" problems. The RL walking of Berkeley Humanoid Lite was achieved by first reproducing the reference pipeline and then migrating to the custom model, ultimately achieving zero-shot sim-to-real ([arXiv:2504.17249](https://arxiv.org/abs/2504.17249)).

[How to analyze your situation] GPU VRAM insufficient for 4096 parallel environments: reduce to 512–1024, the curve will be slower but feasible; no NVIDIA GPU: MuJoCo + CPU can also train (an order of magnitude slower), first get the environment logic correct.

## Step 2: Define Observations, Actions, and Episode Structure

[What to do] Write down three lists:

1. **Observation obs**: Joint positions/velocities, IMU orientation and angular velocity ([IMU](/entry/ent_component_imu_2024/)), previous action; advanced additions include phase clock (sin/cos gait phase). **Do not** stack raw point clouds/images—first learn to walk in state space.
2. **Action action**: Target positions for each joint (PD tracking), clipped according to M10's effort/velocity limits; scaling factors should be written as configuration parameters, not hardcoded.
3. **Episode**: Duration 10–20 s; termination upon falling (torso pitch angle exceeds limit, height too low); random starting position on flat ground.

[Why] The observation determines "what the policy can see": too little and it cannot learn (e.g., missing phase leads to chaotic gait), too much and it cannot train. Using position targets instead of direct torques allows the underlying PD to absorb the actuator non-idealities of the real robot for you—this is a key design for sim-to-real, see [Impedance Control](/entry/ent_method_impedance_control/) and [Quasi-Direct Drive Actuator](/entry/ent_technology_quasi_direct_drive_actuator_2024/) cards.

[How to analyze your situation] Observations that cannot be obtained on the real robot should not be included in the policy (e.g., ground truth base linear velocity)—unless you have a state estimation solution, otherwise missing observations during deployment = policy failure. First, design the obs pipeline in simulation as a "switchable ground truth/estimated value" two-tier system.

## Step 3: Reward Function—From Standing to Walking

[What to do] Add reward terms one by one, train a version after each addition and check the curve, **do not add all at once**. Recommended order and typical weight ideas (specific values should be tuned according to your platform, the following are common starting points, requiring your own experimental verification):

| Order | Reward Term | Purpose | Starting Magnitude |
|---|---|---|---|
| 1 | Survival/Upright | Baseline reward for not falling | +1/step |
| 2 | Linear Velocity Tracking | Track target velocity (first forward/backward, then turning) | exp(-4·err²) |
| 3 | Posture/Height | Penalty for torso pitch, CoM height | -1·err² |
| 4 | Energy & Smoothness | Penalty for torque, torque change rate | -1e-4·Στ² |
| 5 | Gait Shaping | Double support/swing phase transition, foot lift height | Phase-dependent small weight |

[Why] Reward hacking is the number one pitfall in RL: rewarding only speed leads to shaking in place, rewarding only uprightness leads to standing still. "Adding and checking one by one" is the only way to pinpoint which term is steering the policy wrong. A systematic discussion of reward design can be found in [Chapter 18 Imitation Learning and Policy Learning](/wiki/chapters/chapter-18/).

[How to analyze your situation] Curve plateau exceeds 2x expected iteration count: first check if a penalty term's weight is overwhelming the velocity term (the most common failure), halve the dominant term's weight and retrain. Record configuration and curve screenshots for each experiment—reward tuning is experimental science, not mysticism.

## Step 4: Domain Randomization—Vaccinating the Policy Against Reality

[What to do] In [Domain Randomization](/entry/ent_method_domain_randomization/), cover at least four categories, with ranges estimated based on your real robot's uncertainty:

| Randomization Item | Suggested Starting Range | Corresponding Real-World Error |
|---|---|---|
| Link mass/CoM | ±10–15% | Assembly and weighing errors (M10 Step 3) |
| Ground friction coefficient | 0.5–1.2 | Differences in floor/tile/carpet |
| Actuator delay & strength | Delay 0–20 ms; torque ×0.85–1.0 | Drive response and battery voltage fluctuations |
| Random push disturbance | Every 5–8 s, ≤ 50 N·0.2 s | Collisions and slips |

[Why] The reality gap between simulation and reality is not a single error, but the accumulation of all small errors; domain randomization makes the policy robust to "a range of errors" rather than overfitting to "one precise model." Too wide a range prevents learning, too narrow fails on the real robot—start narrow and gradually widen. Theory can be found in [Chapter 23 Simulation and Physics Engines](/wiki/chapters/chapter-23/).

[How to analyze your situation] Don't know the friction coefficient range? Drag the shoe sole on the target ground to measure (use a spring scale to pull a sled for estimation). M14's system identification will later refine the actuator delay and mass terms—first leave the ranges wide.

## Step 5: Training, Evaluation, and Checkpoint Selection

[What to do]

1. Start with [PPO](/entry/ent_algorithm_ppo/) default hyperparameters (lr 3e-4, clip 0.2, entropy 0.01 are common starting points, need verification per environment), maximize parallel environment count based on VRAM;
2. Save checkpoints every 50–100 iterations, log training curves (reward/ep_len/individual penalty components) to TensorBoard or equivalent tool;
3. **Select checkpoint not by highest reward, but by robust evaluation**: Run 100 consecutive episodes under maximum randomization strength + push disturbances, pick the one with "lowest fall rate and meeting speed requirements."

[Why] The reward peak in late training is often an illusion of overfitting to the current randomization seed; robust evaluation corresponds to real robot performance. Berkeley's approach is to validate under strong randomization before moving to the real robot (berkeley-humanoid-lite archive).

[How to analyze your situation] Review evaluation videos one by one: stiff gait but can withstand pushes = ready for the real robot (M14 will continue refinement); beautiful gait but falls with a single push = go back to Step 4 and widen randomization. Keep 2–3 candidate checkpoints for M14, where real robot performance is the final judge.

## Acceptance Criteria

- [ ] Official baseline environment successfully reproduced (screenshots/curves archived).
- [ ] Three lists (obs/action/episode) documented, aligned with observations obtainable on the real robot.
- [ ] Complete record of adding reward terms one by one, final configuration and curves archived.
- [ ] Domain randomization covers mass/friction/delay/push four categories, with estimated basis for ranges.
- [ ] Under robust evaluation (maximum randomization + disturbances), continuous 100 episodes have fall rate ≤ 10%, forward speed meets requirements.
- [ ] 2–3 candidate checkpoints archived for M14 real robot screening.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Reward not increasing | Imbalanced reward weights / Missing key observations / Incorrect action scaling | Reduce rewards one by one to locate the issue; check against the Step 2 checklist; print the actual range of actions |
| Shaking in place without moving forward | Speed term weight too low / Joint torque limits too restrictive | Increase speed tracking weight; verify effort limits (M10 Step 4) |
| Training diverges, curve collapses | lr too high / Reward values explode (a component's magnitude out of control) | Halve lr; print normalization for each component |
| Simulation works well, but falls immediately when randomization is enabled | Randomization range too wide in one step | Halve the range, then widen it by one step every 500 iterations (curriculum-style) |
| Policy is "biased" toward one side's leg | Model left-right asymmetry (URDF mirroring error) | Return to M10 to check mirror joint axes |

## Supporting Reading

- Previous task: [M12 · Simulation Standing and Walking](m12-sim-walking.md)
- Next task: [M14 · Sim-to-Real Deployment and Walking Acceptance](m14-sim-to-real.md)
- Theoretical background: [Chapter 18 Imitation Learning and Policy Learning](/wiki/chapters/chapter-18/), [Chapter 23 Simulation and Physics Engines](/wiki/chapters/chapter-23/)
- [Simulation Environment Setup Guide](../playbooks/sim-setup.md) · [Stage 2 Overview](../stage-2-biped.md)
