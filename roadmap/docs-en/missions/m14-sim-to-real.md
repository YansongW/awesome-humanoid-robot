# M14 · Sim-to-Real Deployment and Walking Acceptance: From Simulation Champion to the First Step on the Real Robot

**Global Position**: After M13 has trained and screened 2–3 candidate RL checkpoints. The input is a walking strategy that is robust in simulation + a model backfilled with measured parameters, and the output is **real robot flat ground walking passing Stage 2's six-level acceptance**. Stage 3 (starting from M15) will add an upper body to this walking machine—if it can't walk steadily, everything that follows is a castle in the air.

**Prerequisites**: [M13 · Reinforcement Learning Training](m13-rl-training.md) acceptance passed (maximum randomization + disturbance, 100 episode fall rate ≤10% under perturbation); complete robot assembly, zero-point calibration, and emergency stop chain completed (corresponding to [Stage 2 Overview](../stage-2-biped.md) Step 4/6); gantry in place, two-person debugging team with clear division of labor.

Theoretical background: [sim-to-real transfer](/entry/ent_method_sim_to_real/), [domain randomization](/entry/ent_method_domain_randomization/), [system identification](/entry/ent_method_system_identification/) cards, [Chapter 11 Assembly, Integration and Testing](/wiki/chapters/chapter-11/) and [Chapter 25 Robot Evaluation System](/wiki/chapters/chapter-25/).

## Step 1: Deployment Pipeline Setup—Moving the Policy from the Training Machine to the Robot

【What to do】Four tasks executed in order:

1. **Policy Export**: Export as jit (PyTorch `torch.jit`) or ONNX according to the training framework, fix input/output dimensions and freeze weights; immediately after export, rerun the robustness evaluation in simulation using the exported version to confirm no loss in score.
2. **Onboard Inference**: The policy runs on the robot's main controller. Two benchmark routes: Berkeley Humanoid Lite uses C language low-level deployment on Intel N95 (the `berkeley_humanoid_lite_lowlevel` subdirectory is independent of the training stack and can be stress-tested separately, `data/roadmap/research/berkeley-humanoid-lite.md`); ToddlerBot uses pure Python deployment on Jetson Orin NX 16GB (`data/roadmap/research/toddlerbot.md`).
3. **Frequency Layering**: The policy infers joint target positions at 50 Hz, while the low-level PD tracks at high frequency—benchmark files: ToddlerBot 30 motors full state feedback at 50 Hz (toddlerbot.md), Berkeley actuator and IMU CAN communication at 250 Hz (berkeley-humanoid-lite.md).
4. **Process Separation and Watchdog**: Inference, control, and communication run in separate processes; the communication/control processes send heartbeats to each other; if any process times out without response, joint torque is released.

【Why】The training stack and deployment stack are two different things: the training machine has a GPU and ground truth observations, while the robot only has onboard computing power and noisy sensors. The essence of frequency layering is "slow decision, fast execution"—the policy can be slower, but the PD must be high-frequency to suppress disturbances and actuator non-idealities (see the [impedance control](/entry/ent_method_impedance_control/) card for the mechanism); the watchdog ensures that if the software freezes, the robot does not stay rigidly in place applying force.

【How to analyze your situation】For replicated platforms, directly use the official deployment code; this step only requires export and frequency verification. Hard indicators for self-developed stacks: measured inference latency < 50% of the control cycle (for a 50 Hz policy, <10 ms); if it exceeds, reduce network size or switch to a compiled runtime—don't force it.

## Step 2: Observation Alignment—Mapping Simulation Observations to Real Robot Sensors One by One

【What to do】Create an observation mapping table, align, measure, and sign off on each item:

| Simulation Observation | Real Robot Source | Alignment Key Points |
|---|---|---|
| Base orientation (roll/pitch/yaw) | [IMU](/entry/ent_component_imu_2024/) | Installation direction vs. model base frame axis mapping, write into code comments |
| Base angular velocity | IMU gyroscope | Unit rad/s, filter bandwidth consistent with simulation |
| Joint angle | Encoder | Zero point consistent with M06 calibration record, positive direction same as URDF axis |
| Joint velocity | Encoder difference | Add low-pass filter, cutoff frequency consistent with simulation processing |
| Previous action | Policy output cache | Read directly from memory, do not read back from actuator |

Three calibration steps: ① **IMU zero bias**—let the robot stand still for 30 s, record orientation readings; if drift exceeds threshold (e.g., 1°, engineering recommended value, needs verification with your IMU), redo zero bias calibration; ② **Encoder zero point**—use the M06 fixture to re-swing once, compare readings with calibration record; ③ **Coordinate system verification**—manually tilt the robot, compare IMU reading direction with simulation base frame direction.

【Why】Observation misalignment is the number one cause of sim-to-real failure: if the IMU is installed 180° reversed, the policy sees an "inverted world" and falls immediately upon startup. Repeat the rule established in M13: **observations that cannot be obtained on the real robot should not be in the policy**—quantities like base linear velocity ground truth either require a state estimation solution or should be removed from the observation and the policy retrained; there is no third way.

【How to analyze your situation】For each row in the mapping table, perform a "manual perturbation → print reading → compare with the same scenario in simulation". If only one IMU is installed, do not include foot orientation estimates in the observation—observations without sensor support are landmines.

## Step 3: Actuator System Identification Refinement—Aligning the Randomization Center with the Real Robot

【What to do】

1. **Measure latency**: Send a step position command, record the time difference between the command and the encoder response to obtain total latency (communication + drive + mechanical).
2. **Measure first-order time constant**: Fit the response curve to a first-order model `τ_m·q̇ + q = q_cmd`, extract τ_m.
3. **Kt and friction**: Reuse the current-torque calibration and friction measurement data from the M07 test bench.
4. **Backfill**: Write the measured latency, torque coefficient, and mass deviation back into the simulation, and move the **center** of the M13 [domain randomization](/entry/ent_method_domain_randomization/) range to the measured values; if necessary, narrow the range and retrain a checkpoint.

【Why】The philosophy of domain randomization is "randomize around the true value"—if the center of the range deviates from the real robot, the policy is robust for a robot that doesn't exist; this is the root cause of "acclimatization failure". ToddlerBot's digital twin is the benchmark approach: 3D-printed fixtures complete zero-point calibration in 1 minute, and [system identification](/entry/ent_method_system_identification/) only needs to be done once for the same motor model to transfer to all units—this is the key to its zero-shot sim-to-real (toddlerbot.md).

【How to analyze your situation】For servo motor platforms (ToddlerBot lineage): sysID only needs "1 unit of the same model + full robot zero point"; for self-developed QDD (Berkeley lineage), batch differences are large, so latency and friction must be measured per unit. After backfilling, bring the retrained checkpoint along with the M13 candidates into Step 4 for final real robot comparison.

## Step 4: Phased Unlocking of the Real Robot—Six-Step Ladder, Roll Back on Anomaly

【What to do】Strictly follow the ladder; only upgrade when each step's criteria are met:

| Ladder | Content | Pass Criteria | Rollback Condition |
|---|---|---|---|
| 1 | Full suspension on gantry, pedaling in the air | 5 min without abnormal current/temperature, gait cycle stable | Any anomaly → stop and check observations |
| 2 | Partial load (rope carries 30–50%) | Foot contact switching normal, center of mass does not drift | Orientation angle exceeds threshold |
| 3 | Full load static standing | ≥5 min stationary standing (i.e., Stage 2 standing checkpoint) | Tendency to fall → return to partial load |
| 4 | Marching in place | 1 min marching without leaving position | Deviation exceeds half step width |
| 5 | Straight line walking | Continuous ≥3 min without significant drift | Obvious yaw → return to marching |
| 6 | Turning and speed change | 5 successful left and right turns each | Failure → return to straight line |

Discipline: Two-person system (one monitors telemetry, one guards the [emergency stop system](/entry/ent_component_emergency_stop_system_2024/), the emergency stop hand never leaves); first batch of tests at each ladder must be recorded on video; change only one variable at a time.

【Why】The reality gap reveals itself in layers: suspension exposes observation and latency issues, load exposes friction and contact modeling issues, and walking exposes gait and disturbance rejection issues. Unlocking everything at once mixes all problems together for debugging. Writing down the criteria in advance prevents the "let's try one more step" gamble—rolling back is not failure, it's the process.

【How to analyze your situation】If stuck at a certain ladder: first return to simulation to reproduce the same command—if reproducible in simulation, it's a model problem (return to Step 3 or M13); if not reproducible in simulation, it's an observation/actuator problem (return to Step 2). A 16 kg class (Berkeley) robot can injure someone if it falls, so the gantry and two-person system are not optional; a 3.4 kg class (ToddlerBot) robot must also follow the same procedure—the process is cultivated on small machines.

## Step 5: Protection Strategy and Fault Grading – Turning Falls into Data

【What to Do】

1. **Soft Fault (Recoverable)**: Attitude angle exceeds threshold (e.g., roll/pitch > 30°, engineering recommended value, verify against your platform) → Trigger damped landing/squat, switch joints to damping mode to cushion ground contact.
2. **Hard Fault (Unrecoverable)**: Communication loss, overcurrent, emergency stop triggered → Immediately cut power and release force; emergency stop hardwired, independent of all software chains.
3. **Fall Logging**: Record time, attitude sequence, battery voltage, motor temperature, and video index for each fall – falls are data, not shame.
4. **Structural Protection**: Vulnerable parts (lower legs, ankles, shell) should be replaceable 3D-printed components. Reference magnitude: ToddlerBot can withstand approximately 7 falls, with single repair requiring only 21 minutes of printing + 14 minutes of assembly (toddlerbot.md).

【Why】Learning to walk inevitably involves falling; the difference is whether you get a diagnostic data set or a pile of fragments afterward. Soft/hard grading allows the robot to "fall properly" – damped landing spreads the impact over the entire process, saving structural parts compared to a rigid fall; the log loop makes every rollback in Step 4 traceable, rather than relying on memory.

【How to Analyze Your Situation】Set soft fault thresholds conservatively during the first week of testing; it's better to trigger damped landing a few more times. Keep spare parts as "three most breakable parts × 2" on hand; immediately retire batteries that are over-discharged, swollen, or have been dropped, following the specifications in the [Humanoid Robot Lithium-Ion Battery System](/entry/ent_tech_li_battery_humanoid/) card.

## Step 6: Stage 2 Acceptance Execution – Pass Six Checks One by One, Archive Data

【What to Do】Execute each item according to the [Stage 2 Overview](../stage-2-biped.md) acceptance criteria (see checklist below). Manage expectations for battery life based on archive data: ToddlerBot RL walking measured 19 minutes to thermal throttling (toddlerbot.md), Berkeley 6S 4000 mAh LiPo approximately 30 minutes (berkeley-humanoid-lite.md), BRUCE approximately 20 minutes (bruce-westwood.md) – reaching the same magnitude is normal; don't hold yourself to the fantasy of a "room-temperature, fully charged, new battery."

【Why】The six checks are the ticket to Stage 3: the Standing Check ensures a stable base after adding arms in M15, and the Disturbance Rejection Check ensures the whole machine remains stable when reaching out. Full documentation (video + telemetry curves) serves as baseline data for diagnosing "walking performance degradation" in Stage 3.

【How to Analyze Your Situation】If stuck on a particular check: return to the [Stage 2 Overview](../stage-2-biped.md) common pitfalls table for troubleshooting, **do not change strategies on the spot during acceptance** – acceptance is measurement, not debugging; after changes, retrain and restart from Ladder 3.

## Acceptance Criteria

- [ ] Policy exported as jit/ONNX and re-tested in simulation without loss; onboard inference latency < 50% of control cycle.
- [ ] Observation mapping table documented and verified item by item; IMU static drift over 30 s and encoder zero-point verification passed.
- [ ] Actuator latency/time constant/Kt measured and backfilled; domain randomization center aligned with measured values.
- [ ] Six-step ladder fully recorded on video; each step has a pass record; rollbacks have logs.
- [ ] **Standing Check**: Static standing under full load without harness for ≥5 min; motor temperature below official limit (for unrated models, confirm with supplier).
- [ ] **Walking Check**: Continuous walking on flat, hard ground for ≥10 min; no falls; cumulative yaw < 90°.
- [ ] **Disturbance Rejection Check**: Recovers balance after a light one-handed push (approx. 5–10 N, within 0.5 s); does not fall or enter protective shutdown.
- [ ] **Protection Check**: Manually trigger fall scenarios under harness protection; emergency stop and damped landing activate; no structural fractures.
- [ ] **Safety Check**: Time from pressing emergency stop to power cutoff measured <1 s; battery charging and storage fully comply with lithium battery safety standards.
- [ ] Fall logs and battery life data (voltage/temperature/duration) archived; battery life matches the magnitude in the archive.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Falls immediately upon startup | Observation coordinate system error (IMU mounting direction vs base frame) | Return to Step 2 for coordinate system triple-check; print and compare item by item |
| Joint high-frequency jitter, buzzing sound | Actuator delay not modeled / gain too high | Return to Step 3 to measure and backfill delay; reduce PD gain and re-test |
| Simulation champion fails on real robot | Domain randomization center deviates from measured parameters | Backfill sysID data, narrow range, and retrain (Step 3) |
| Slowly tilts to one side while standing | IMU zero-bias drift / attitude filter divergence | Let it sit for 30 s and check attitude readings; redo zero-bias calibration |
| Eager to remove harness, falls under load | Skipping ladder steps, criteria treated as a formality | Return to the corresponding ladder in Step 4; go through criteria one by one and keep records |
| Torque weakens, gait deteriorates after a few minutes | Battery voltage drop / actuator thermal throttling | Check voltage and temperature telemetry; compare with ToddlerBot's 19 min thermal throttling archive |

## Companion Reading

- Previous Task: [M13 · Reinforcement Learning Training](m13-rl-training.md)
- Next Task: [M15 · Upper Body and End Effector](m15-upper-body.md)
- Theoretical Background: [Chapter 11 Assembly, Integration, and Testing](/wiki/chapters/chapter-11/), [Chapter 25 Robot Evaluation System](/wiki/chapters/chapter-25/)
- [Stage 2 Overview](../stage-2-biped.md) · [Roadmap Overview](../index.md)
