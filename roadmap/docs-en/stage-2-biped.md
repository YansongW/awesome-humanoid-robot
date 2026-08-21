# Phase 2: Biped Platform – From Simulation to the First Walking Robot

Biped is the soul of "humanoid" and also the stage with the highest crash rate from 0→1. The goal of this phase: select an open-source biped/wheeled-biped platform, first run the control stack in simulation, then replicate it with hardware, and finally achieve stable walking on flat ground. All solution data comes from the [public research archive](https://github.com/YansongW/awesome-humanoid-robot/tree/main/data/roadmap/research/) (accessed 2026-07-01, with sources annotated item by item).

## Phase Task List (M08–M14)

This page is the phase map; the task pages are the construction manual—complete calculation examples, three-segment details, and checkable acceptance checklists for each step are on the task pages:

| Task | Content | Corresponding Section on This Page |
|---|---|---|
| [M08 · Platform Selection and Procurement](missions/m08-platform-selection.md) | Ten-column comparison of five major open-source platforms, decision tree, license check, BOM ledger | Section 3 |
| [M09 · Full Assembly, Wiring, and Power](missions/m09-mechanical-assembly.md) | Module-by-module assembly, power tree/signal tree, battery and emergency stop, smoke test | Section 4 Steps 1–3, 6; Section 6 |
| [M10 · URDF Modeling and Export](missions/m10-urdf-modeling.md) | Kinematic tree, inertia parameters, joint limits, collision geometry, model package verification | Section 4 Step 5 |
| [M11 · Simulation Environment and Model Conversion](missions/m11-sim-setup.md) | MuJoCo/Isaac installation, URDF→MJCF/USD, actuator and contact modeling | Section 1 |
| [M12 · Simulated Standing and Walking](missions/m12-sim-walking.md) | PD standing, ZMP/LIPM, OpenLoong MPC+WBC hands-on, route decision | Section 2 |
| [M13 · Reinforcement Learning Training](missions/m13-rl-training.md) | obs/action/reward design, domain randomization, checkpoint robustness evaluation | Section 2, Level 5 |
| [M14 · Sim-to-Real Deployment and Walking Acceptance](missions/m14-sim-to-real.md) | Deployment pipeline, observation alignment, sysID, phased unlocking, six-level acceptance | Section 4 Steps 4–8; Section 5 |

---

## 1. Simulation First: Run the Control Stack with Zero Hardware

**What to do**: Before buying any motor, install a physics simulator on your computer and get the biped model to stand and walk. Two main routes:

- [MuJoCo](/entry/ent_software_mujoco_physics_engine_2022/): Lightweight and free, runs on a laptop. OpenLoong's [OpenLoong-Dyn-Control](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/main/README-zh.md) is an MPC + WBC whole-body control framework deployed on MuJoCo, with built-in walking/jumping/blind obstacle stepping examples—learn the full-size humanoid classic control pipeline without writing a single line of hardware code (source: openloong-qinglong.md).
- [Isaac Lab](/entry/ent_software_nvidia_isaac_lab_2024/): GPU-based massively parallel simulation, suitable for reinforcement learning training, requires an NVIDIA GPU. The Berkeley Humanoid Lite directory is organized according to Isaac Lab, with all three formats (URDF/MJCF/USD) available (source: berkeley-humanoid-lite.md).

**Why**: The biggest reason for biped replication failure is not assembly, but "the hardware is built, the control doesn't work, and it falls over as soon as it's turned on." Simulation isolates "algorithm errors" from "hardware errors," so when you move to the real robot, you only need to troubleshoot the hardware dimension. For simulator selection, see also [Chapter 23 Simulation and Physics Engines](/wiki/chapters/chapter-23/).

**How to analyze your situation**: No NVIDIA GPU, zero budget → MuJoCo + OpenLoong-Dyn-Control, learn the full MPC+WBC meal without spending a penny. Have an RTX GPU, going the RL route → Install Isaac Lab; when choosing Berkeley later, the training environment will seamlessly integrate. Pure Python background → `pip install upkie` to run balancing examples in PyBullet (source: upkie.md), get positive feedback the same day.

---

## 2. Balance Theory Ladder: Follow the Order, Don't Skip Levels

Biped balance is a ladder, with a card for each level. Validate one level in simulation before moving up.

**Level 1: ZMP (Zero Moment Point)**
- What to do: Understand the [Zero Moment Point](/entry/ent_method_zero_moment_point/)—the necessary and sufficient condition for a robot not to fall is that the equivalent point of ground reaction force lies within the support polygon. Observe in simulation when the ZMP leaves the support region and when the robot falls.
- Why: ZMP is the most classic criterion for biped stability; subsequent gait planning revolves around "controlling the ZMP." See background in [Chapter 14 Fundamentals of Robot Control](/wiki/chapters/chapter-14/) and [Chapter 15 Motion Generation and Locomotion](/wiki/chapters/chapter-15/).
- How to analyze your situation: The wheeled-biped (Upkie) route also requires learning this—just replace the support polygon with the line connecting the two wheel ground contact points.

**Level 2: Gait Planning**
- What to do: Learn [Gait Planning](/entry/ent_method_gait_planning/): given a target velocity, how to generate swing foot placement, support/swing phase switching timing, and center of mass trajectory. The classic entry point is LIPM (Linear Inverted Pendulum Model) + capture point analysis.
- Why: Gait planning is the decision layer (where to place the foot), while MPC/WBC is the execution layer (how to generate joint torques); layering allows you to diagnose whether "walking crooked" is due to wrong foot placement or insufficient force control.
- How to analyze your situation: For the RL route, understanding the concept is sufficient—the policy learns foot placement on its own; for the MPC route, you must master it thoroughly.

**Level 3: MPC (Model Predictive Control)**
- What to do: Understand [Model Predictive Control](/entry/ent_method_model_predictive_control/): at each step, use a simplified dynamics model to predict forward over a time horizon, solve an optimization problem, execute only the first step, and roll forward. In OpenLoong's MuJoCo example, modify the weights and observe changes in walking quality.
- Why: MPC explicitly handles constraints (no foot slip, limited torque) and is the mainstream real-robot solution for high-dynamic bipeds—BRUCE uses variable-period MPC for walking/running/jumping (source: bruce-westwood.md).
- How to analyze your situation: Strong math background → MPC has the highest ceiling; average math → skip hand-coding MPC and go directly to the RL route.

**Level 4: WBC (Whole-Body Control)**
- What to do: Understand [Whole-Body Control](/entry/ent_method_whole_body_control/): treat the joint torques of the entire body as a quadratic programming (QP) problem with task priorities—first ensure no falling and no foot slip, then allocate the remaining capacity to secondary tasks like arm movement.
- Why: For a humanoid with dozens of degrees of freedom, single-joint PID cannot manage coupled dynamics; the output of MPC is distributed to each joint by WBC (OpenLoong uses the MPC+WBC architecture).
- How to analyze your situation: The RL route can postpone deep derivation, but during sim-to-real troubleshooting, the difference between expected and actual torque is an important diagnostic signal.

**Level 5: RL Route**
- What to do: [PPO](/entry/ent_algorithm_ppo/) + [Domain Randomization](/entry/ent_method_domain_randomization/) + [Sim-to-Real](/entry/ent_method_sim_to_real/) combination: train a walking policy using PPO in simulation, randomize parameters like friction, mass, and motor delay during training, then deploy zero-shot on the real robot. ToddlerBot (MuJoCo/MJX + PPO) and Berkeley Humanoid Lite (Isaac Lab) are both complete open-source implementations of this route (source: respective research files).
- Why: RL bypasses the heavy labor of manual modeling and tuning, and has been validated by these two robots as "reproducible by an individual." The sim2real gap is essentially "the physics you didn't model," and domain randomization makes the policy insensitive to it.
- How to analyze your situation: Have a GPU, ML background → home turf, prioritize ToddlerBot or Berkeley; no GPU → rent cloud computing for training, or fall back to the MPC route (OpenLoong examples run on CPU).

## 3. Solution Selection Comparison and Decision Tree

All parameters are sourced from research files; items marked "Unknown" in the files are retained as is.

| Platform | Cost (BOM) | Height/Weight | DoF | Actuator | Main Controller | Replication Difficulty | Source |
|---|---|---|---|---|---|---|---|
| ToddlerBot | Approx. $6,000 (90% spent on motors and computer) | 0.56 m / 3.4 kg | 30 (Arm 7×2, Leg 6×2, Neck 2, Waist 2) | ROBOTIS Dynamixel Bus Servo | Jetson Orin NX 16GB | Low – Pure Python/pip installation, digital twin zero-shot sim2real; inexperienced users can assemble in 3 days (paper verified) | [Paper](https://arxiv.org/html/2502.00893v2), toddlerbot.md |
| Berkeley Humanoid Lite | USA $4,312 / China $3,236 | 0.8 m / 16 kg | 22 (Leg 6×2, Arm 5×2) | Custom 6512/5010 Quasi-Direct Drive, 3D Printed Cycloidal Reducer | Intel N95 | Medium – Isaac Lab training + C low-level deployment; requires building 22 actuators and soldering CAN | [Technical Report](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/Archive/EECS-2025-207.pdf), berkeley-humanoid-lite.md |
| Upkie (Wheeled Biped) | Approx. $3,000 + 60 hours printing | Unknown (varies by configuration) | 6 (Per leg: hip, knee, wheel) | mjbots qdd100 ×4 + moteus | Raspberry Pi 4 + pi3hat | Low – Built-in PID/MPC/RL balancing examples; wheeled biped avoids pure walking tuning pitfalls | [Project Page](https://hackaday.io/project/185729-upkie-wheeled-biped-robots), upkie.md |
| BRUCE | Approx. $6.5K (third-party paper estimate, official inquiry-based pricing) | 70 cm / 4.8 kg | 16 (Leg 5×2, Arm 3×2) | Koala BEAR Quasi-Direct Drive (250 g, peak 10.5 N·m, liquid-cooled knee) | 6 TOPS Compute Board | High – Variable-cycle MPC can run and jump, but the overall framework is not public, only available via commercial procurement | [Comparison Table](https://arxiv.org/html/2502.00893v2), bruce-westwood.md |
| OpenLoong Qinglong | Unknown (public version not sold individually) | 185 cm / 80 kg+ | 43 (Including five-finger dexterous hand) | Primarily rotary actuators (specific model unknown) | 400 TOPS Controller | Not suitable for personal replication (institutional-level requirements) – but MPC+WBC full-stack open source, MuJoCo allows zero-hardware learning | [Framework README](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/main/README-zh.md), openloong-qinglong.md |

**Decision Tree**:

1. **Budget < $3.5k?** Yes → Upkie (approx. $3,000): Highest success rate for learning balance control on real hardware, minimal crash damage, serves as training before pure biped. No → Question 2.
2. **Want a walking humanoid, what is your hands-on ability?** Zero experience/pure software background → ToddlerBot: Bus servo eliminates FOC tuning, comprehensive documentation/assembly videos/jigs, cost is highest BOM. Has 3D printing + soldering + embedded experience → Berkeley: Approx. $3,236 in China for a 22 DoF humanoid capable of RL walking, cost is building 22 actuators yourself.
3. **Need high dynamics or full size?** High dynamics research (institutional) → BRUCE, but open-source level of the whole robot is questionable; confirm software licensing with supplier before purchase. Full size → Individuals should not attempt to replicate Qinglong; only use OpenLoong-Dyn-Control as free educational material; domestic teams can watch for the lightweight model NanoLoong open-sourced in 2025-08.

**How to analyze your situation**: List five items: "Budget, weekly available hours, have 3D printer, have GPU, have used a soldering iron". Check them against the table above. The row with all checks is your choice – the core KPI for the first biped is "walk", not perfection from the start.

---

## 4. Replication Process Breakdown

Using well-documented platforms (ToddlerBot / Berkeley) as templates, eight steps total, each with "Action → Principle → Self-Analysis".

**Step 1 BOM Verification**: Order from the official BOM and record the landed cost and lead time (Berkeley technical report provides US and China BOMs; purchase according to the Chinese BOM for domestic procurement). Motors and computers account for the majority of cost (90% for ToddlerBot); cut budget in the right places. For substitute items not specified in the BOM, confirm parameters with the supplier.

**Step 2 3D Printing Structural Parts**: Print according to official files (ToddlerBot via MakerWorld, Berkeley via GitHub Releases); cycloidal gears can use standard desktop FDM + PLA (official 60-hour durability test) – structural precision determines backlash, large backlash causes force control jitter; do not change materials arbitrarily. If no printer, use online printing services; specify the same infill rate/material as the official for functional parts.

**Step 3 Mechanical Assembly**: Assemble in modules (single leg → single arm → torso → final assembly). After each module, manually check smoothness and interference to avoid multiple reworks after final assembly. For less hands-on experience, choose a bus servo platform (mainly screwing and plugging wires); for those daring to build custom actuators, first assemble and test a single 6512 unloaded, then replicate 22 units.

**Step 4 Zero Calibration and System Identification (sysID)**: Use printed jigs to position each joint at mechanical zero and write offsets; perform sysID on motors of the same model and backfill parameters into the simulation model. This is the foundation of sim-to-real – ToddlerBot's digital twin approach (1-minute calibration with jig + single sysID for same motor model) is key to its zero-shot transfer. Skipping sysID typically results in "simulation stable, real robot shaking".

**Step 5 Simulation Alignment**: Backfill all measured mass, center of mass, zero points, and motor parameters into URDF/MJCF. Re-run walking strategies to ensure stability in simulation (re-tune MPC weights / retrain RL if necessary) – manufacturing tolerances mean the real robot is not the one in the drawing; alignment acknowledges and makes this explicit. RL is less sensitive to ±10% mass errors; MPC requires more careful tuning.

**Step 6 First Power-On (Smoke Test)**: Suspension rig (feet off ground) → verify emergency stop chain → enable each joint for small amplitude sinusoidal oscillation → check temperature, current, communication. Electrical errors are exposed here; any loss of control under suspension does not crash the robot; emergency stop must be verified now. Two-person operation: one monitors the interface, one guards the emergency stop.

**Step 7 Standing**: Gradually reduce suspension load → static standing on both feet → add small center-of-mass oscillations and light push recovery. Standing is a subset of walking – once the standing control loop (ankle/hip strategy) is tuned, walking is just periodically shifting the balance point out of the support polygon and recapturing it. If this step fails for the RL route, return to Step 4/5 to check calibration alignment; do not hard-tune reward functions on the real robot.

**Step 8 Walking**: March in place → straight line → turn → timed continuous walking. Record battery voltage, motor temperature, and fall count. Manage endurance expectations according to file data: ToddlerBot RL walking measured 19 minutes (until thermal throttling), Berkeley's 6S 4000 mAh LiPo approx. 30 minutes, BRUCE approx. 20 minutes – achieving similar duration is normal.

---

## 5. Acceptance Criteria

All must be passed to proceed to the next stage:

1. **Simulation Check**: The selected platform's official example (or self-trained policy) walks continuously for 10 minutes of simulation time in MuJoCo/Isaac Lab without falling, and can recover after random external force perturbations.
2. **Standing Check**: Real robot stands statically under full load without suspension for ≥ 5 minutes, with all joint motor temperatures below the official limit (for unspecified models, confirm with the supplier).
3. **Walking Check**: Continuous walking on a flat, hard surface for ≥ 10 minutes without falling or significant drift (cumulative yaw < 90°).
4. **Disturbance Rejection Check**: During walking/standing, withstand a light one-hand push (approx. 5–10 N, within 0.5 s) and recover balance without falling or entering protective shutdown.
5. **Protection Check**: Under suspension, artificially trigger a fall scenario; emergency stop and fall protection should activate – joints should unload or enter damping mode before ground contact, with no structural fractures (reference: ToddlerBot can withstand approx. 7 falls, repair requires only 21 minutes printing + 14 minutes assembly).
6. **Safety Check**: Emergency stop response time from button press to power cutoff must be demonstrable; battery charging and storage must comply with lithium battery safety regulations.

---

## 6. Safety Red Lines

If any of the following is not met, do not power on the physical robot:

- **Emergency Stop (E-Stop)**: A hardware-level [emergency stop system](/entry/ent_component_emergency_stop_system_2024/) independent of the software chain must be present—pressing it physically cuts motor power without going through the main controller. BRUCE comes with a dedicated wireless E-stop (source: bruce-westwood.md); self-replicated platforms must at least have a wired E-stop within the operator's reach.
- **Gantry/Safety Harness**: The first power-on, standing, and walking tests must be conducted under a gantry or overhead safety rope—a 3.4 kg ToddlerBot can still require repairs after a fall, and a 16 kg Berkeley tipping over can injure people and damage the robot. During debugging, keep fingers away from gear meshing areas and joint ranges of motion, and confirm no one is touching the robot before enabling motors.
- **Lithium Battery Safety**: LiPo batteries are the biggest fire hazard for desktop humanoids. Charging must be attended and done in a fireproof bag/container; batteries that are over-discharged, swollen, or dropped must be retired immediately. See the [Lithium Battery Technical Card](/entry/ent_tech_li_battery_humanoid/) for specifications. Short-circuiting a large-capacity battery like a 6S 4000 mAh can generate enough energy to ignite desktop clutter—double-check polarity before wiring.

---

## 7. Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Stable in simulation but shaky or falls on the real robot (sim-to-real gap) | Zero-point calibration error; sysID not performed; mass/friction modeling deviation | Re-do fixture calibration and system identification; verify URDF/MJCF mass against actual measured values; for RL approaches, increase [domain randomization](/entry/ent_method_domain_randomization/) range and retrain |
| Gait softens and performance degrades after a few minutes of walking | Actuator thermal throttling (ToddlerBot measured thermal throttling after 19 minutes) | Read motor temperature telemetry; shorten continuous operation or add cooling; check if operating near peak torque for extended periods |
| Slowly tilts to one side while standing still | [IMU](/entry/ent_component_imu_2024/) zero-bias drift; attitude filter divergence | Let it rest for 30 s and check if attitude readings drift; redo zero-bias calibration; check filter covariance parameters |
| High-frequency joint jitter and humming | Gain too high; large backlash; bus packet loss causing feedback delay | Lower gain and retest; manually move the joint to feel backlash; count packet loss rate (baseline: ToddlerBot 50 Hz, Berkeley 250 Hz CAN) |
| Nose-dives forward as soon as a walking command is given | Footstep planning lags behind the center of mass; support/swing phase switching timing error | First reproduce the same command in simulation; check if footstep and ZMP trajectories are synchronized against [gait planning](/entry/ent_method_gait_planning/) |
| Same structural part repeatedly breaks after a fall; battery life is far below the datasheet | Using old printed parts; battery aging; a specific joint drawing high current continuously | Verify the latest printed parts and changelog in the repository; measure battery internal resistance; check current distribution across joints to find the abnormal one—usually due to overly tight assembly or calibration error |

## Companion Reading

- [Simulation Environment Setup Guide](playbooks/sim-setup.md) — Complete implementation flow for the simulation-first principle
- [Compute Platform Selection Guide](playbooks/compute-selection.md) — Main controller and real-time solutions
- [Sensor Selection Guide](playbooks/sensor-selection.md) — IMU, encoder, and force sensing
- [Roadmap Overview](index.md)
