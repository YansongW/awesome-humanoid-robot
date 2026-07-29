# Phase 2: Bipedal Platform – From Simulation to the First Walking Robot

Bipedalism is the soul of "humanoid" and also the stage with the highest crash rate in the 0→1 transition. Goal of this phase: Select an open-source bipedal/wheel-legged platform, first run the control stack in simulation, then replicate it with hardware, and finally achieve stable walking on flat ground. All solution data comes from the `data/roadmap/research/` research archives (access date 2026-07-01, with sources annotated for each entry).

## Task List for This Phase (M08–M14)

This page is the phase map; the task pages are the construction manual—complete calculation examples, three-segment details, and checkable acceptance checklists for each step are on the task pages:

| Task | Content | Corresponding Section on This Page |
|---|---|---|
| [M08 · Platform Selection and Procurement](missions/m08-platform-selection.md) | Ten-column comparison of five major open-source platforms, decision tree, license check, BOM ledger | Section 3 |
| [M09 · Full Assembly, Wiring, and Power](missions/m09-mechanical-assembly.md) | Module-by-module assembly, power tree/signal tree, battery and emergency stop, smoke test | Section 4 Steps 1–3, 6; Section 6 |
| [M10 · URDF Modeling and Export](missions/m10-urdf-modeling.md) | Kinematic tree, inertia parameters, joint limits, collision geometry, model package validation | Section 4 Step 5 |
| [M11 · Simulation Environment and Model Conversion](missions/m11-sim-setup.md) | MuJoCo/Isaac installation, URDF→MJCF/USD, actuator and contact modeling | Section 1 |
| [M12 · Simulation Standing and Walking](missions/m12-sim-walking.md) | PD standing, ZMP/LIPM, OpenLoong MPC+WBC hands-on, route decision-making | Section 2 |
| [M13 · Reinforcement Learning Training](missions/m13-rl-training.md) | obs/action/reward design, domain randomization, checkpoint robustness evaluation | Section 2, Level 5 |
| [M14 · Sim-to-Real Deployment and Walking Acceptance](missions/m14-sim-to-real.md) | Deployment pipeline, observation alignment, sysID, phased unlocking, six-level acceptance | Section 4 Steps 4–8; Section 5 |

---

## 1. Simulation First: Run the Control Stack with Zero Hardware

**What to do**: Before buying any motor, install a physics simulator on your computer and get the bipedal model standing and walking in simulation. Two main routes:

- [MuJoCo](/entry/ent_software_mujoco_physics_engine_2022/): Lightweight and free, runs on a laptop. OpenLoong's [OpenLoong-Dyn-Control](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/main/README-zh.md) is an MPC + WBC whole-body control framework deployed on MuJoCo, with built-in walking/jumping/blind obstacle stepping examples—learn the classic control pipeline for a full-size humanoid without writing a single line of hardware code (source: openloong-qinglong.md).
- [Isaac Lab](/entry/ent_software_nvidia_isaac_lab_2024/): GPU-based massively parallel simulation, suitable for reinforcement learning training, requires an NVIDIA GPU. The directory of Berkeley Humanoid Lite is organized according to Isaac Lab, with URDF/MJCF/USD formats all available (source: berkeley-humanoid-lite.md).

**Why**: The biggest reason for failed bipedal replication is not assembly, but "hardware is built, control doesn't work, and it falls over as soon as it's turned on." Simulation isolates "algorithm errors" from "hardware errors," so when you move to the real robot, you only need to troubleshoot the hardware dimension. For simulator selection, see also [Chapter 23 Simulation and Physics Engines](/wiki/chapters/chapter-23/).

**How to analyze your situation**: No NVIDIA GPU, zero budget → MuJoCo + OpenLoong-Dyn-Control, learn the full MPC+WBC meal without spending a cent. Have an RTX GPU, going the RL route → Install Isaac Lab, the training environment seamlessly connects when you later choose Berkeley. Pure Python background → `pip install upkie` to run balancing examples in PyBullet (source: upkie.md), get positive feedback on the same day.

---

## 2. Balance Theory Ladder: Climb in Order, Don't Skip Levels

Bipedal balance is a ladder, each level is a card. Validate one level in simulation before moving up.

**Level 1: ZMP (Zero Moment Point)**
- What to do: Understand [Zero Moment Point](/entry/ent_paper_zero_moment_point_2024/)—the necessary and sufficient condition for a robot not to fall is that the equivalent point of ground reaction force falls within the support polygon. Observe in simulation when the ZMP runs outside the support region and when the robot falls.
- Why: ZMP is the most classic criterion for bipedal stability; subsequent gait planning revolves around "controlling the ZMP." See background in [Chapter 14 Fundamentals of Robot Control](/wiki/chapters/chapter-14/) and [Chapter 15 Motion Generation and Locomotion](/wiki/chapters/chapter-15/).
- How to analyze your situation: The wheel-legged (Upkie) route also needs to learn this—just replace the support polygon with the line connecting the two wheel contact points.

**Level 2: Gait Planning**
- What to do: Learn [Gait Planning](/entry/ent_method_gait_planning/): Given a target velocity, how to generate the swing foot landing point, the timing of support/swing phase transitions, and the center of mass trajectory. The classic entry point is LIPM (Linear Inverted Pendulum Model) + capture point analysis.
- Why: Gait planning is the decision layer (where to step), MPC/WBC is the execution layer (how to generate joint torques); layering allows you to pinpoint whether "walking crooked" is due to wrong foot placement or insufficient force control.
- How to analyze your situation: For the RL route, understanding the concept is sufficient—the policy learns foot placement itself; the MPC route must be thoroughly understood.

**Level 3: MPC (Model Predictive Control)**
- What to do: Understand [Model Predictive Control](/entry/ent_method_model_predictive_control/): At each step, use simplified dynamics to predict forward over a time horizon, solve an optimization problem, execute only the first step, and roll forward. In OpenLoong's MuJoCo example, modify weights to observe changes in walking quality.
- Why: MPC explicitly handles constraints (no foot slip, limited torque) and is the mainstream real-world solution for high-dynamic bipeds—BRUCE uses variable-period MPC for walking/running/jumping (source: bruce-westwood.md).
- How to analyze your situation: Solid math foundation → MPC has the highest ceiling; average math → skip hand-coding MPC and directly use the RL route.

**Level 4: Whole-Body Control (WBC)**
- What to do: Understand [Whole-Body Control](/entry/ent_method_whole_body_control/): Treat the whole-body joint torques as a task-prioritized quadratic programming (QP) problem—first ensure no falling and no foot slip, then allocate remaining capacity to secondary tasks like arms.
- Why: For a humanoid with dozens of degrees of freedom, single-joint PID cannot manage coupled dynamics; the output of MPC is precisely distributed to each joint by WBC (OpenLoong uses the MPC+WBC architecture).
- How to analyze your situation: The RL route can postpone deep derivation, but during sim-to-real troubleshooting, the difference between expected and actual torque is an important diagnostic signal.

**Level 5: RL Route**
- What to do: [PPO](/entry/ent_algorithm_ppo/) + [Domain Randomization](/entry/ent_method_domain_randomization/) + [Sim-to-Real](/entry/ent_method_sim_to_real/) combination: Train walking policies with PPO in simulation, randomizing parameters like friction, mass, motor delay during training, then deploy zero-shot on the real robot. ToddlerBot (MuJoCo/MJX + PPO) and Berkeley Humanoid Lite (Isaac Lab) are both complete open-source implementations of this route (source: respective research archives).
- Why: RL bypasses the heavy labor of manual modeling and tuning, and has been verified by these two robots as "reproducible by individuals." The sim2real gap is essentially "the physics you didn't model," and domain randomization makes the policy insensitive to it.
- How to analyze your situation: Have a GPU, ML background → home turf, prioritize ToddlerBot or Berkeley; no GPU → rent cloud computing for training, or fall back to the MPC route (OpenLoong examples run on CPU).

## 3. Solution Selection Comparison and Decision Tree

All parameters are sourced from research files; items marked "unknown" in the files are retained as is.

| Platform | Cost (BOM) | Height/Weight | DoF | Actuator | Main Controller | Replication Difficulty | Source |
|---|---|---|---|---|---|---|---|
| ToddlerBot | Approx. $6,000 (90% spent on motors and computer) | 0.56 m / 3.4 kg | 30 (arm 7×2, leg 6×2, neck 2, waist 2) | ROBOTIS Dynamixel bus servo | Jetson Orin NX 16GB | Low – Pure Python/pip install, digital twin zero-shot sim2real; inexperienced users can assemble in 3 days (paper verified) | [Paper](https://arxiv.org/html/2502.00893v2), toddlerbot.md |
| Berkeley Humanoid Lite | USA $4,312 / China $3,236 | 0.8 m / 16 kg | 22 (leg 6×2, arm 5×2) | Custom 6512/5010 quasi-direct drive, 3D printed cycloidal reducer | Intel N95 | Medium – Isaac Lab training + C low-level deployment; requires building 22 actuators and soldering CAN | [Technical Report](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/Archive/EECS-2025-207.pdf), berkeley-humanoid-lite.md |
| Upkie (Wheeled Biped) | Approx. $3,000 + 60 hours printing | Unknown (varies by configuration) | 6 (per leg: hip, knee, wheel) | mjbots qdd100 ×4 + moteus | Raspberry Pi 4 + pi3hat | Low – Built-in PID/MPC/RL balancing examples; wheeled biped avoids pure walking tuning pitfalls | [Project Page](https://hackaday.io/project/185729-upkie-wheeled-biped-robots), upkie.md |
| BRUCE | Approx. $6.5K (third-party paper estimate, official inquiry required) | 70 cm / 4.8 kg | 16 (leg 5×2, arm 3×2) | Koala BEAR quasi-direct drive (250 g, peak 10.5 N·m, liquid-cooled knee) | 6 TOPS compute board | High – Variable-period MPC can run and jump, but the full robot framework is not public, only available via commercial procurement | [Comparison Table](https://arxiv.org/html/2502.00893v2), bruce-westwood.md |
| OpenLoong Qinglong | Unknown (public version not sold separately) | 185 cm / 80 kg+ | 43 (including five-fingered dexterous hand) | Primarily rotary actuators (specific model unknown) | 400 TOPS controller | Unsuitable for personal replication (institutional-level requirements) – but MPC+WBC full-stack open source, MuJoCo allows zero-hardware learning | [Framework README](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/main/README-zh.md), openloong-qinglong.md |

**Decision Tree**:

1. **Budget < $3.5k?** Yes → Upkie (approx. $3,000): Highest success rate for learning balance control on real hardware, minimal crash cost, serves as training before pure biped. No → Question 2.
2. **Want a walking humanoid, what is your hands-on ability?** Zero experience / pure software background → ToddlerBot: Bus servo eliminates FOC tuning, comprehensive documentation/assembly videos/jigs, cost is highest BOM. Has 3D printing + soldering + embedded experience → Berkeley: Approx. $3,236 in China for a 22 DoF humanoid capable of RL walking, cost is building 22 actuators yourself.
3. **Need high dynamics or full size?** High dynamics research (institutional) → BRUCE, but open-source status of the full robot is questionable; confirm software licensing with supplier before purchase. Full size → Individuals should not attempt to replicate Qinglong; only use OpenLoong-Dyn-Control as free educational material; domestic teams can watch for the lightweight model NanoLoong open-sourced in 2025-08.

**How to analyze your situation**: List five items: "budget, weekly available hours, have 3D printer, have GPU, have used a soldering iron". Check them against the table above. The row with all checks is your choice – the core KPI for the first biped is "walking", not achieving everything at once.

---

## 4. Replication Process Breakdown

Using platforms with comprehensive documentation (ToddlerBot / Berkeley) as templates, eight steps total, each with "Action → Principle → Self-Analysis".

**Step 1 BOM Verification**: Order from the official BOM and record the received price and lead time (Berkeley technical report provides US and China BOMs; purchase according to the Chinese BOM for domestic procurement). Motors and computers account for the majority of cost (90% for ToddlerBot); cut budget in the right places. For BOM items without specified specifications, confirm parameters with the supplier.

**Step 2 3D Printing Structural Parts**: Print according to official files (ToddlerBot via MakerWorld, Berkeley via GitHub Releases); cycloidal gears can use standard desktop FDM + PLA (official 60-hour durability test) – structural precision determines backlash, large backlash causes force control jitter; do not change materials arbitrarily. Without a printer, use online printing services; for functional parts, specify the same infill rate/material as the official version.

**Step 3 Mechanical Assembly**: Assemble in modules (single leg → single arm → torso → final assembly). After each module, manually check smoothness and interference to avoid multiple reworks after final assembly. For less hands-on experience, choose a bus servo platform (mainly screwing and plugging wires); for those daring to build custom actuators, first assemble and test a single 6512 unloaded, then replicate 22 units.

**Step 4 Zero Calibration and System Identification (sysID)**: Use printed jigs to position each joint at mechanical zero and write offsets; perform sysID on motors of the same model and backfill parameters into the simulation model. This is the foundation of sim-to-real – ToddlerBot's digital twin approach (1-minute calibration with jig + single sysID per motor model) is key to its zero-shot transfer. The typical symptom of skipping sysID is "stable in simulation, shaky on real hardware".

**Step 5 Simulation Alignment**: Backfill measured mass, center of mass, zero points, and motor parameters into URDF/MJCF. Rerun walking policies to confirm stability in simulation (re-tune MPC weights / retrain RL if necessary) – manufacturing tolerances mean the real robot is not the one in the drawing; alignment acknowledges and makes this explicit. RL approaches are less sensitive to ±10% mass errors; MPC approaches require more care.

**Step 6 First Power-On (Smoke Test)**: Suspension rig (feet off ground) → verify emergency stop chain → enable each joint for small amplitude sinusoidal oscillation → check temperature, current, communication. Electrical errors are exposed here; any loss of control under suspension does not cause a crash; the emergency stop must be verified as functional at this stage. Two-person operation: one monitors the interface, one guards the emergency stop.

**Step 7 Standing**: Gradually reduce suspension rig load → static standing on both feet → add small center-of-mass oscillations and light push recovery. Standing is a subset of walking – once the standing control loop (ankle/hip strategy) is tuned, walking is simply periodically shifting the balance point out of the support polygon and recapturing it. If this step fails for the RL approach, return to Step 4/5 to check calibration alignment; do not hard-tune reward functions on the real robot.

**Step 8 Walking**: Mark time → straight line → turning → timed continuous walking. Record battery voltage, motor temperature, and number of falls. Manage runtime expectations according to file data: ToddlerBot RL walking measured 19 minutes (until thermal throttling), Berkeley's 6S 4000 mAh LiPo approx. 30 minutes, BRUCE approx. 20 minutes – achieving similar durations is normal.

---

## 5. Acceptance Criteria

All must be passed to proceed to the next stage:

1. **Simulation Check**: The selected platform's official example (or self-trained policy) walks continuously for 10 minutes of simulation time in MuJoCo/Isaac Lab without falling, and can recover after random external force perturbations.
2. **Standing Check**: The real robot stands statically under full load without the suspension rig for ≥ 5 minutes, with all joint motor temperatures below the official limit (for models without specified limits, confirm with the supplier).
3. **Walking Check**: Continuous walking on a flat, hard surface for ≥ 10 minutes without falling and without significant drift (cumulative yaw < 90°).
4. **Disturbance Rejection Check**: Recovers balance after a light one-handed push (approx. 5–10 N, within 0.5 s) during walking/standing, without falling or entering protective shutdown.
5. **Protection Check**: Under suspension rig protection, artificially trigger a fall scenario; the emergency stop and fall protection must activate – joints should unload or enter damping mode before ground contact, with no structural fractures (reference: ToddlerBot can withstand approx. 7 falls, repair requires only 21 minutes printing + 14 minutes assembly).
6. **Safety Check**: The response time from pressing the emergency stop to power cutoff must be demonstrable; battery charging and storage must comply with lithium battery safety regulations.

---

## 6. Safety Red Lines

If any of the following is not met, do NOT power on the physical robot:

- **Emergency Stop (E-Stop)**: A hardware-level [emergency stop system](/entry/ent_component_emergency_stop_system_2024/) independent of the software chain must be present—pressing it physically cuts motor power without going through the main controller. BRUCE comes with an independent wireless E-stop (source: bruce-westwood.md); self-replicated platforms must at least have a wired E-stop within reach of the operator.
- **Gantry/Safety Harness**: The first power-on, standing, and walking tests must be conducted under a gantry or overhead safety rope—a 3.4 kg ToddlerBot can still require repairs after a fall, and a 16 kg Berkeley tipping over can injure people and damage the robot. During debugging, keep fingers away from gear meshing zones and joint ranges of motion; confirm no one is touching the robot before enabling motors.
- **Lithium Battery Safety**: LiPo batteries are the biggest fire hazard for desktop humanoids. Charging must be attended and performed in a fireproof bag/container; batteries that are over-discharged, swollen, or dropped must be retired immediately. See the [Lithium Battery Technical Card](/entry/ent_tech_li_battery_humanoid/) for specifications. A short circuit in high-capacity batteries like 6S 4000 mAh can generate enough energy to ignite desktop clutter; double-check polarity before wiring.

---

## 7. Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Stable in simulation but shaky or falls on the real robot (sim-to-real gap) | Zero-point calibration error; sysID not performed; mass/friction modeling deviation | Re-do fixture calibration and system identification; verify URDF/MJCF mass against actual measured values; for RL approaches, increase [domain randomization](/entry/ent_method_domain_randomization/) range and retrain |
| Gait softens and performance degrades after a few minutes of walking | Actuator thermal throttling (ToddlerBot measured thermal throttling after 19 minutes) | Read motor temperature telemetry; shorten continuous operation or add cooling; check if operating near peak torque for extended periods |
| Slowly tilts to one side while standing still | [IMU](/entry/ent_component_imu_2024/) zero-bias drift; attitude filter divergence | Let it rest for 30 s and check if attitude readings drift; redo zero-bias calibration; check filter covariance parameters |
| High-frequency joint jitter and buzzing | Gain too high; large backlash; bus packet loss causing feedback delay | Lower gain and retest; manually shake the joint to feel backlash; check packet loss rate (baseline: ToddlerBot 50 Hz, Berkeley 250 Hz CAN) |
| Nose-dives immediately upon receiving a walking command | Footstep planning lags behind CoM; support/swing phase switching timing error | First reproduce the same command in simulation; check if footstep and ZMP trajectories are synchronized against [gait planning](/entry/ent_method_gait_planning/) |
| Same structural part repeatedly breaks after a fall; battery life far below documented specs | Using old printed parts; battery aging; sustained high current in one joint | Verify the latest printed parts and changelog in the repository; measure battery internal resistance; check current distribution across joints to find the abnormal joint—usually due to overly tight assembly or calibration error |

## Companion Reading

- [Simulation Environment Setup Guide](playbooks/sim-setup.md) — Complete implementation workflow for the simulation-first principle
- [Compute Platform Selection Guide](playbooks/compute-selection.md) — Main controller and real-time solutions
- [Sensor Selection Guide](playbooks/sensor-selection.md) — IMU, encoder, and force sensing
- [Roadmap Overview](index.md)
