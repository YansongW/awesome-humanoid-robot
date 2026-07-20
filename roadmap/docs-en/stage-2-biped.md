# Phase 2: Bipedal Platform – From Simulation to the First Walking Robot

> ⚠️ The content of this roadmap is compiled based on public information and theoretical knowledge, and has not been verified on actual hardware; please verify safety specifications yourself when performing electrical and mechanical operations.

Bipedal locomotion is the soul of "humanoid" and also the stage with the highest crash rate from 0→1. The goal of this phase: choose an open-source bipedal/wheeled-legged platform, first run the control stack in simulation, then spend money to replicate it, and finally achieve stable walking on flat ground. All solution data comes from the research files in `data/roadmap/research/` (accessed 2026-07-01, with sources annotated item by item).

---

## 1. Simulation First: Run the Control Stack with Zero Hardware

**What to do**: Before buying any motor, first install a physics simulator on your computer and get the standing and walking of a bipedal model working. Two main routes:

- [MuJoCo](/entry/ent_software_mujoco_physics_engine_2022/): Lightweight and free, runs on a laptop. OpenLoong's [OpenLoong-Dyn-Control](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/main/README-zh.md) is an MPC + WBC whole-body control framework deployed on MuJoCo, with built-in walking/jumping/blind obstacle stepping examples—learn the classic control pipeline for a full-size humanoid without writing a single line of hardware code (source: openloong-qinglong.md).
- [Isaac Lab](/entry/ent_software_nvidia_isaac_lab_2024/): GPU-based massively parallel simulation, suitable for reinforcement learning training, requires an NVIDIA GPU. The directory of Berkeley Humanoid Lite is organized according to Isaac Lab, with URDF/MJCF/USD formats all available (source: berkeley-humanoid-lite.md).

**Why**: The biggest reason for failed bipedal replication is not assembly, but "the hardware is built, the control doesn't work, and it falls over as soon as it's turned on." Simulation isolates "algorithm errors" from "hardware errors," so when you move to the real robot, you only need to debug the hardware dimension. For simulator selection, see also [Chapter 23: Simulation and Physics Engines](/wiki/chapters/chapter-23/).

**How to analyze your situation**: No NVIDIA GPU, zero budget → MuJoCo + OpenLoong-Dyn-Control, learn the full MPC+WBC meal without spending a cent. Have an RTX GPU, going the RL route → Install Isaac Lab, and the training environment will seamlessly connect when you later choose Berkeley. Pure Python background → `pip install upkie` to run balancing examples in PyBullet (source: upkie.md), get positive feedback on the same day.

---

## 2. Balance Theory Ladder: Chew in Order, Don't Skip Levels

Bipedal balance is a ladder, with a card at each level. Validate one level in simulation before moving up.

**Level 1: ZMP (Zero Moment Point)**
- What to do: Understand [Zero Moment Point](/entry/ent_paper_zero_moment_point_2024/)—the necessary and sufficient condition for a robot not to tip over is that the equivalent point of ground reaction force falls within the support polygon. Observe in simulation when the ZMP runs outside the support region and when the robot falls.
- Why: ZMP is the most classic criterion for bipedal stability; subsequent gait planning revolves around "controlling the ZMP." For background, see [Chapter 14: Fundamentals of Robot Control](/wiki/chapters/chapter-14/) and [Chapter 15: Motion Generation and Locomotion](/wiki/chapters/chapter-15/).
- How to analyze your situation: The wheeled-legged (Upkie) route also requires learning this—just replace the support polygon with the line connecting the two wheel ground contact points.

**Level 2: Gait Planning**
- What to do: Learn [Gait Planning](/entry/ent_method_gait_planning/): Given a target velocity, how to generate the swing foot landing point, the switching timing between support and swing phases, and the center of mass trajectory. The classic entry point is LIPM (Linear Inverted Pendulum Model) + Capture Point analysis.
- Why: Gait planning is the decision layer (where to step), while MPC/WBC is the execution layer (how to generate joint torques); layering allows you to pinpoint whether "walking crooked" is due to a wrong landing point or insufficient force control.
- How to analyze your situation: For the RL route, just understand the concepts—the policy learns the landing point itself; for the MPC route, you must master it thoroughly.

**Level 3: MPC (Model Predictive Control)**
- What to do: Understand [Model Predictive Control](/entry/ent_method_model_predictive_control/): At each step, use simplified dynamics to predict forward over a time horizon, solve an optimization problem, execute only the first step, and roll forward. In OpenLoong's MuJoCo example, modify the weights and observe the change in walking quality.
- Why: MPC explicitly handles constraints (no foot slip, limited torque) and is the mainstream real-robot solution for high-dynamic bipeds—BRUCE uses variable-period MPC to achieve walking/running/jumping (source: bruce-westwood.md).
- How to analyze your situation: Solid math foundation → MPC has the highest ceiling; average math → skip hand-coding MPC and go directly with the RL route.

**Level 4: WBC (Whole-Body Control)**
- What to do: Understand [Whole-Body Control](/entry/ent_method_whole_body_control/): Treat the joint torques of the whole body as a quadratic programming (QP) problem with task priorities—first ensure no falling and no foot slip, then allocate the remaining capacity to secondary tasks like arm movement.
- Why: For a humanoid with dozens of degrees of freedom, single-joint PID cannot manage the coupled dynamics; the output of MPC is precisely distributed to each joint by WBC (OpenLoong uses the MPC+WBC architecture).
- How to analyze your situation: The RL route can postpone deep dives into derivations, but during sim-to-real debugging, the difference between expected and actual torque is an important diagnostic signal.

**Level 5: RL Route**
- What to do: Combine [PPO](/entry/ent_algorithm_ppo/) + [Domain Randomization](/entry/ent_method_domain_randomization/) + [Sim-to-Real](/entry/ent_method_sim_to_real/): Train a walking policy using PPO in simulation, randomizing parameters like friction, mass, and motor delay during training, then deploy zero-shot on the real robot. ToddlerBot (MuJoCo/MJX + PPO) and Berkeley Humanoid Lite (Isaac Lab) are both complete open-source implementations of this route (source: respective research files).
- Why: RL bypasses the heavy labor of manual modeling and tuning, and has been verified by these two robots as "reproducible by an individual." The sim2real gap is essentially "the physics you didn't model," and domain randomization makes the policy insensitive to it.
- How to analyze your situation: Have a GPU, ML background → your home turf, prioritize ToddlerBot or Berkeley; no GPU → rent cloud computing for training, or fall back to the MPC route (OpenLoong examples run on CPU).

## 3. Solution Selection Comparison and Decision Tree

All parameters are from research files; items marked "unknown" in the files are retained as-is.

| Platform | Cost (BOM) | Height/Weight | DoF | Actuator | Main Controller | Replication Difficulty | Source |
|---|---|---|---|---|---|---|---|
| ToddlerBot | ~$6,000 (90% spent on motors and computer) | 0.56 m / 3.4 kg | 30 (arm 7×2, leg 6×2, neck 2, waist 2) | ROBOTIS Dynamixel bus servo | Jetson Orin NX 16GB | Low – Pure Python/pip install, digital twin zero-shot sim2real; inexperienced users can assemble in 3 days (paper verified) | [Paper](https://arxiv.org/html/2502.00893v2), toddlerbot.md |
| Berkeley Humanoid Lite | US $4,312 / China $3,236 | 0.8 m / 16 kg | 22 (leg 6×2, arm 5×2) | Self-developed 6512/5010 quasi-direct drive, 3D printed cycloidal reducer | Intel N95 | Medium – Isaac Lab training + C low-level deployment; requires building 22 actuators and soldering CAN | [Technical Report](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/Archive/EECS-2025-207.pdf), berkeley-humanoid-lite.md |
| Upkie (Wheeled Biped) | ~$3,000 + 60 hours printing | Unknown (varies by configuration) | 6 (per leg: hip, knee, wheel) | mjbots qdd100 ×4 + moteus | Raspberry Pi 4 + pi3hat | Low – Built-in PID/MPC/RL balance examples; wheeled biped avoids pure walking tuning hell | [Project Page](https://hackaday.io/project/185729-upkie-wheeled-biped-robots), upkie.md |
| BRUCE | ~$6.5K (third-party paper estimate, official pricing upon inquiry) | 70 cm / 4.8 kg | 16 (leg 5×2, arm 3×2) | Koala BEAR quasi-direct drive (250 g, peak 10.5 N·m, liquid-cooled knee) | 6 TOPS compute board | High – Variable-cycle MPC can run and jump, but the full robot framework is not public; only commercial procurement | [Comparison Table](https://arxiv.org/html/2502.00893v2), bruce-westwood.md |
| OpenLoong Qinglong | Unknown (public version not sold separately) | 185 cm / 80 kg+ | 43 (including five-fingered dexterous hand) | Primarily rotary actuators (specific model unknown) | 400 TOPS controller | Not suitable for personal replication (institutional-level conditions) – but MPC+WBC full-stack open source, MuJoCo allows zero-hardware learning | [Framework README](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/main/README-zh.md), openloong-qinglong.md |

**Decision Tree**:

1. **Budget < $3.5k?** Yes → Upkie (~$3,000): Highest success rate for learning balance control on real hardware, minimal crash damage, good practice before pure biped. No → Question 2.
2. **Want a walking humanoid; what's your hands-on ability?** Zero experience/pure software background → ToddlerBot: Bus servos eliminate FOC tuning, comprehensive documentation/assembly videos/jigs, but BOM is most expensive. Have 3D printing + soldering + embedded experience → Berkeley: ~$3,236 in China gets a 22 DoF humanoid capable of RL walking, but requires building 22 actuators yourself.
3. **Need high dynamics or full size?** High dynamics research (institutional) → BRUCE, but open-source level of the full robot is questionable; confirm software licensing with supplier before purchase. Full size → Individuals should not attempt to replicate Qinglong; only use OpenLoong-Dyn-Control as free educational material. Domestic teams can watch for the lightweight model NanoLoong open-sourced in 2025-08.

**How to analyze your situation**: List five items: "budget, weekly available hours, have 3D printer, have GPU, have used a soldering iron." Check them against the table above. The row with all checks is your choice – the core KPI for the first biped is "walking," not getting it perfect in one go.

---

## 4. Replication Process Breakdown

Using well-documented platforms (ToddlerBot / Berkeley) as templates, there are eight steps. Each step: "Action → Principle → Self-Analysis."

**Step 1 BOM Verification**: Order from the official BOM and record the landed cost and lead time (Berkeley's technical report provides US and China BOMs; for domestic procurement, use the China version). Motors and computer account for the bulk of the cost (90% for ToddlerBot); cut budget in the right places. For BOM items without specified specifications, confirm parameters with the supplier.

**Step 2 3D Printing Structural Parts**: Print according to official files (ToddlerBot via MakerWorld, Berkeley via GitHub Releases); cycloidal gears can use standard desktop FDM + PLA (official 60-hour durability test) – structural precision determines backlash, large backlash causes force control jitter; do not change materials yourself. Without a printer, use online printing services; specify the same infill rate/material as the official for functional parts.

**Step 3 Mechanical Assembly**: Assemble in modules (single leg → single arm → torso → final assembly). After each module, manually check smoothness and interference to avoid multiple reworks after final assembly. With little hands-on experience, choose a bus servo platform (mainly screwing and plugging wires); if tackling self-developed actuators, first test a single 6512 unloaded, then replicate 22 units.

**Step 4 Zero Calibration and System Identification (sysID)**: Use printed jigs to position each joint at mechanical zero and write offsets; perform sysID once for the same motor model, backfill parameters into the simulation model. This is the foundation of sim-to-real – ToddlerBot's digital twin approach (1-minute jig calibration + single sysID per motor model) is key to its zero-shot transfer. A typical symptom of skipping sysID is "stable in simulation, shaking on real hardware."

**Step 5 Simulation Alignment**: Backfill actual mass, center of mass, zero points, and motor parameters into URDF/MJCF. Re-run walking policies to ensure stability in simulation (re-tune MPC weights / retrain RL if necessary) – machining errors mean the real robot is not the one in the drawing; alignment acknowledges and makes this explicit. RL is less sensitive to ±10% mass errors; MPC requires more careful alignment.

**Step 6 First Power-On (Smoke Test)**: Suspension rig (feet off ground) → verify emergency stop chain → enable each joint for small amplitude sinusoidal swings → check temperature, current, communication. Electrical errors are exposed here; any loss of control under suspension does not crash the robot; the emergency stop must be verified now. Two-person operation: one monitors the interface, one guards the emergency stop.

**Step 7 Standing**: Gradually reduce suspension load → static standing on both feet → add small center-of-mass swings and light push recovery. Standing is a subset of walking – once the standing control loop (ankle/hip strategy) is tuned, walking is just periodically shifting the balance point out of the support polygon and recapturing it. If this step fails for the RL route, return to Step 4/5 to check calibration alignment; do not hard-tune reward functions on the real robot.

**Step 8 Walking**: Mark time → straight line → turns → timed continuous walking. Record battery voltage, motor temperature, and fall count. Manage endurance expectations according to file data: ToddlerBot RL walking measured 19 minutes (until thermal throttling), Berkeley's 6S 4000 mAh LiPo ~30 minutes, BRUCE ~20 minutes – reaching the same order of magnitude is normal.

---

## 5. Acceptance Criteria

All must be passed to proceed to the next stage:

1. **Simulation Check**: The selected platform's official example (or self-trained policy) walks continuously for 10 minutes of simulation time in MuJoCo/Isaac Lab without falling, and can recover after random external force perturbations.
2. **Standing Check**: Real robot stands statically under full load without suspension for ≥ 5 minutes, with all joint motor temperatures below the official limit (for unspecified models, confirm with the supplier).
3. **Walking Check**: Continuous walking on a flat, hard surface for ≥ 10 minutes, no falls, no significant drift (cumulative yaw < 90°).
4. **Disturbance Check**: During walking/standing, withstand a light one-hand push (~5–10 N, within 0.5 s) and recover balance without falling or entering protective shutdown.
5. **Protection Check**: Under suspension protection, artificially trigger a fall scenario; the emergency stop and fall protection must activate – joint force unloading or entering damping mode before ground contact, with no structural fractures (reference: ToddlerBot can withstand ~7 falls, repair requires only 21 minutes printing + 14 minutes assembly).
6. **Safety Check**: The response time from pressing the emergency stop to power cutoff must be demonstrable; battery charging and storage must comply with lithium battery safety regulations.

---

## 6. Safety Red Lines

If any of the following is not met, do NOT power on the physical robot:

- **Emergency Stop (E-Stop)**: A hardware-level [emergency stop system](/entry/ent_component_emergency_stop_system_2024/) independent of the software chain is mandatory—pressing it must physically cut motor power without going through the main controller. BRUCE comes with a dedicated wireless E-stop (source: bruce-westwood.md); self-replicated platforms must at least have a wired E-stop within the operator's reach.
- **Gantry/Safety Harness**: The first power-on, standing, and walking tests must be conducted under a gantry or overhead safety rope—a 3.4 kg ToddlerBot can still break from a fall, and a 16 kg Berkeley tipping over can injure people and damage the robot. During debugging, keep fingers away from gear meshing zones and joint ranges of motion; confirm no one is touching the robot before enabling motors.
- **Lithium Battery Safety**: LiPo batteries are the biggest fire hazard for desktop humanoids. Charging must be attended and done in a fireproof bag/container; batteries that are over-discharged, swollen, or dropped must be retired immediately. See the [Lithium Battery Technical Card](/entry/ent_tech_li_battery_humanoid/) for specifications. A short circuit in a large-capacity battery like a 6S 4000 mAh can generate enough energy to ignite desktop clutter—double-check polarity before wiring.

---

## 7. Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Stable in simulation but shaky or falling on the real robot (sim-to-real gap) | Zero-point calibration error; sysID not performed; mass/friction modeling deviation | Re-do fixture calibration and system identification; verify URDF/MJCF mass against actual measured values; for RL approaches, increase [domain randomization](/entry/ent_method_domain_randomization/) range and retrain |
| Gait softens and performance degrades after a few minutes of walking | Actuator thermal throttling (ToddlerBot measured thermal throttling after 19 minutes) | Read motor temperature telemetry; shorten continuous operation or add cooling; check if operating near peak torque for extended periods |
| Slowly tilting to one side while standing still | [IMU](/entry/ent_component_imu_2024/) zero-bias drift; attitude filter divergence | Let it rest for 30 s and check if attitude readings drift; redo zero-bias calibration; check filter covariance parameters |
| High-frequency joint jitter and buzzing | Gain too high; large backlash; bus packet loss causing feedback delay | Lower gain and retest; manually move the joint to feel backlash; check packet loss rate (baseline: ToddlerBot 50 Hz, Berkeley 250 Hz CAN) |
| Nose-dives immediately upon receiving a walking command | Footstep planning lags behind CoM; support/swing phase transition timing error | First reproduce the same command in simulation; check if footstep and ZMP trajectories are synchronized against [gait planning](/entry/ent_method_gait_planning/) |
| Repeated breakage of the same structural part after a fall; battery life far below claimed specs | Using old version printed parts; battery aging; sustained high current in a joint | Check the latest printed parts and changelog in the repository; measure battery internal resistance; examine current distribution across joints to find the abnormal one—usually due to over-tight assembly or calibration error |

## Related Reading

- [Simulation Environment Setup Guide](playbooks/sim-setup.md) — Complete implementation workflow for the simulation-first principle
- [Compute Platform Selection Guide](playbooks/compute-selection.md) — Main controller and real-time solutions
- [Sensor Selection Guide](playbooks/sensor-selection.md) — IMU, encoder, and force sensing
- [Roadmap Overview](index.md)
