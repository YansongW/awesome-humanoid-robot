# Phase 1: Build a Joint (Actuator)

Humanoid robots typically have 20–50 degrees of freedom, but each degree of freedom boils down to the same problem: **motor + reduction + sensing + drive + control, all housed in a single shell, outputting controllable torque and angle**. The goal of this phase: build a joint module on a test bench that passes acceptance—master it, and the entire leg and arm are just replication and engineering.

Two publicly validated routes run through this page; it is recommended to reference them throughout:

- **ODRI (Open Dynamic Robot Initiative) BLMC Force-Controlled Actuator**: Off-the-shelf frameless motor + dual encoders + self-developed MicroDriver drive board, low reduction ratio, high torque transparency, full-chain BSD open source (Source: `data/roadmap/research/open-dynamic-robot-initiative.md`, accessed 2026-07-01).
- **Berkeley Humanoid Lite 6512/5010 Cycloidal Quasi-Direct Drive Actuator**: 3D-printed cycloidal pinwheel reducer + drone brushless motor, single unit BOM for 6512 approximately $188 (US) / $157 (China) (Source: `data/roadmap/research/berkeley-humanoid-lite.md`, from arXiv:2504.17249 and EECS-2025-207 technical report).

For theoretical background, first read [Chapter 4: Actuators: The "Muscles" of Humanoid Robots](/wiki/chapters/chapter-04/); for control theory, see [Chapter 14: Fundamentals of Robot Control](/wiki/chapters/chapter-14/).

## Phase Task List (M01–M07)

This page is the phase map; the task pages are the construction manual—complete examples, three-part details, and checkable acceptance checklists for each step are on the task pages:

| Task | Content | Corresponding Step on This Page |
|---|---|---|
| [M01 · Mathematizing the Requirement Scenario](missions/m01-scenario-to-specs.md) | Translate "want to build a robot" into a table of peak torque/speed/mass/backlash/cost specifications | Expansion of Step 1 |
| [M02 · Motor Calculation and Selection](missions/m02-motor-sizing.md) | Kt/KV/pole pairs and three calculations for current, speed, and heat; from specification table to specific model | Steps 1, 3 |
| [M03 · Reducer Design and Calculation](missions/m03-reducer-design.md) | Double inequality for reduction ratio; selection of planetary/cycloidal/harmonic/belt topology | Steps 1–2 |
| [M04 · Driver, Sensing, and Wiring](missions/m04-driver-sensing-wiring.md) | FOC drive board verification, encoder installation, voltage drop and CAN electrical | Steps 3–5 |
| [M05 · 3D Printing and Mechanical Assembly](missions/m05-print-assembly.md) | Materials, printing parameters, tolerance fit, assembly, and manual rotation | Steps 2, 7 |
| [M06 · Firmware and Calibration](missions/m06-firmware-calibration.md) | Firmware flashing, encoder offset calibration, three-loop tuning, CAN networking | Steps 5–6 |
| [M07 · Bench Testing and Acceptance](missions/m07-bench-acceptance.md) | Four tests: step response/frequency sweep/back-drive/temperature rise; write back measured values to specification table | Step 7 |

## Step 1: Define Joint Specifications

[What to do] Before buying anything, write down five numbers: peak torque, rated speed, mass budget, backlash upper limit, and single-joint cost upper limit. Typical ranges for desktop-level single joints (anchor data indicates source; others are engineering recommendations, to be verified per your design):

| Specification | Typical Desktop Range | Basis |
|---|---|---|
| Peak Torque | 0.5–3 N·m class | [Dynamixel XL330-M288-T](/entry/ent_component_dynamixel_xl330_m288_t/) stall torque 0.52 N·m, [Dynamixel XM430-W210-T](/entry/ent_component_dynamixel_xm430_w210_t/) stall torque 3.0 N·m (Source: physical card/ROBOTIS e-Manual) |
| Output Speed | Motor speed ÷ reduction ratio | Arithmetic example: a 50 W [servo motor](/entry/ent_comp_servo_motor/) max 6000 rpm (physical card), with 288:1 reduction (XL330 reduction ratio 288.4:1) yields approximately 20 rpm output; recalculate based on selected motor |
| Mass Budget | Recommended ≤ 3–5% of total robot mass budget/joint | Engineering experience recommendation, not supplier data; specific model mass must be confirmed with the supplier |
| Backlash | Precision class near zero, servo class noticeably perceptible | [Harmonic drive reducer](/entry/ent_component_harmonic_drive_reducer/) core advantage is zero backlash (physical card); plastic gear servos have larger backlash, specific angular value must be confirmed with the supplier |
| Single-Joint Cost | $157–188 for buildable QDD | Berkeley 6512 actuator BOM: motor $129 + drive board $19 + encoder $3 + structural parts (berkeley-humanoid-lite research archive) |

[Why] Specifications conflict with each other: torque is traded for reduction ratio; a high reduction ratio eliminates speed and back-drivability. Torque density is traded for a larger diameter motor, which blows the mass budget. The physical root is in the formula τ = 2πr²l·B_gap·J_s from the [frameless torque motor](/entry/ent_component_frameless_torque_motor_2024/) card—torque scales with the square of the radius, so joint motors are made into "pancakes." Hip and shoulder main joints often require tens to hundreds of N·m (frameless torque motor physical card); reducing the weight of a desktop robot relaxes the joint specifications.

[How to analyze your situation] Answer three questions first: ① How much weight does the joint need to lift, and how fast? Lever arm length × end load, plus a 1.5–2x safety factor, gives the lower limit for peak torque. ② Total budget ÷ number of degrees of freedom = upper limit for single-joint cost—below $160, you are essentially limited to Berkeley-style self-developed QDD or servos. ③ Is force control required? If yes, write "back-drivable, low reduction ratio" into hard specifications; if not, high reduction ratio options are much broader.

## Step 2: Actuator Topology Selection

[What to do] Choose one of four mainstream topologies and first perform single-joint validation:

| Topology | Backlash | Torque Density | Back-drivability | Cost | Suitable For |
|---|---|---|---|---|---|
| Smart Servo ([XL330](/entry/ent_component_dynamixel_xl330_m288_t/) / [XM430](/entry/ent_component_dynamixel_xm430_w210_t/)) | Larger | Low-Medium | Poor (high reduction ratios like 288:1) | Must be confirmed with supplier | Beginners, first getting the whole robot running |
| [Harmonic Drive Reducer](/entry/ent_component_harmonic_drive_reducer/) + Motor | Zero backlash (physical card) | High | Poor-Medium | Must be confirmed with supplier | Upper limb solutions prioritizing precision |
| [Quasi-Direct Drive QDD](/entry/ent_technology_quasi_direct_drive_actuator_2024/) | Small | Medium | Good (force transparency) | $157–188 (Berkeley archive) | Need force control, doing RL motion research |
| [Frameless Torque Motor](/entry/ent_component_frameless_torque_motor_2024/) Direct Drive | Zero (no reducer) | High | Best | Must be confirmed with supplier | Have mechanical processing capability |

[Why] Choosing a topology is essentially choosing a side in the "precision-transparency-cost" triangle. High reduction ratios (servos, harmonic drives) use small motors for large torque, but the output end cannot "feel" the motor current; force can only be estimated. QDD uses a low reduction ratio to preserve bandwidth and force transparency (QDD physical card), at the cost of the motor itself being large—Berkeley directly uses 150 KV drone motors (MAD M6C12, $129, berkeley-humanoid-lite archive). ODRI's BLMC is the research benchmark for this path: off-the-shelf frameless motor + low reduction ratio, using dual encoders for proprioceptive force control (odri research archive).

[How to analyze your situation] Match based on skills and budget: Beginners who want to get a joint moving quickly—XM430-class servo, one command and it rotates. Can FDM print, flash firmware, target RL locomotion—copy Berkeley 6512, structural parts can be printed in PLA with a desktop FDM printer (berkeley-humanoid-lite archive). Have motion control/power electronics background—study ODRI's `open_robot_actuator_hardware` repository (BSD license). Need industrial-grade precision with a generous budget—harmonic drive route, price and lead time must be confirmed with the supplier.

## Step 3: Motor Body and Driver

【What to Do】Choose one of two motors: [Brushless DC Motor (BLDC)](/entry/ent_component_bldc_motor/) or AC Permanent Magnet Synchronous [Servo Motor](/entry/ent_comp_servo_motor/) (PMSM type); the driver is either a purchased [servo drive](/entry/ent_component_servo_drive_2024/) or an open-source driver board supporting [FOC (Field-Oriented Control)](/entry/ent_method_foc_motor_control/) (Berkeley uses ST B-G431B-ESC1, $19, also compatible with Moteus / ODrive / VESC — berkeley-humanoid-lite archive).

【Why】BLDC back-EMF is trapezoidal, paired with six-step commutation (switching the conducting phase every 60° electrical angle), offering simple control and low cost; PMSM back-EMF is sinusoidal, paired with FOC for lower torque ripple and higher efficiency (BLDC entity card). [FOC](/entry/ent_method_field_oriented_control/) transforms three-phase currents into a d-q coordinate system that rotates with the rotor, decoupling torque and flux, giving AC motors speed regulation performance similar to DC motors (FOC entity card). Joint drivers are typically "FOC + current/speed/position three loops," with high demands on size, heat dissipation, EMI, and current loop bandwidth (servo drive entity card).

【How to Analyze Your Situation】Tight budget, hands-on ability: Hobby-grade BLDC + open-source FOC board is the cheapest entry ticket. Berkeley has verified that a "$129 motor + $19 driver board" combination can run zero-shot sim-to-real RL walking. Don't want to touch power electronics at all: Buy integrated servos or smart actuators, focus your effort on control algorithms. Planning to develop your own driver board: Read the ODRI MicroDriver design files first before deciding — the barrier is high; the odri archive rates friendliness for beginners at only 2/5.

## Step 4: Position Sensing — Joint Encoder

【What to Do】Install at least one output-side [joint encoder](/entry/ent_component_joint_encoder_2024/); for force control, use dual encoders: one on the motor side (for FOC commutation and speed loop), one on the output side (for actual joint angle). A low-cost magnetic encoder is sufficient to start — Berkeley uses the AS5600, unit price $3 (berkeley-humanoid-lite archive).

【Why】Encoder resolution directly determines the controllable bandwidth of the speed loop and position accuracy — the industrial servo reference point is Yaskawa Sigma-7's built-in 24-bit serial encoder (servo motor entity card). The value of dual encoders lies in "seeing through" the gearbox: the output-side encoder can measure gearbox deformation and backlash. ODRI achieves proprioceptive force control precisely through motor-side/output-side dual encoders (odri research archive). High reduction ratio solutions using only a motor-side encoder systematically overestimate accuracy.

【How to Analyze Your Situation】Actuator route: Built-in feedback is sufficient, don't overcomplicate. QDD force control route: The motor-side encoder is the lifeline for FOC; it must be installed stably and accurately. For the output-side encoder, add it if the budget allows (magnetic encoder solution = few-dollar chip + radial magnet + printed bracket). Magnetic encoders are sensitive to installation coaxiality and phase line electromagnetic interference; route wiring away from high-current phase lines.

## Step 5: Communication Bus — CAN vs EtherCAT

【What to Do】For desktop-level, default to [CAN bus](/entry/ent_technology_can_bus_2024/): Berkeley Humanoid Lite uses one CAN 2.0 bus per limb (1 Mbps, connected to the main controller via USB-CAN adapter), actuators and IMU communicate at 250 Hz, single bus supports up to 64 devices (berkeley-humanoid-lite archive). Evaluate [EtherCAT](/entry/ent_technology_ethercat_2024/) for advanced needs.

【Why】CAN is cheap, noise-resistant, has a mature ecosystem; 1 Mbps is sufficient for a dozen joints running at 250–500 Hz. Its weaknesses are bandwidth and determinism. EtherCAT's killer feature is "processing on the fly" — slaves read/write immediately as the frame passes through, without receiving and forwarding the entire frame, offering far better determinism than CAN (EtherCAT entity card). The cost is expensive slave chips and the need for a real-time system on the master. The actuator route uses TTL half-duplex serial (XL330/XM430 both use TTL communication, entity card), which is the simplest but has limited speed and topology.

【How to Analyze Your Situation】Joints ≤ 12, control frequency ≤ 500 Hz: CAN, don't hesitate; a USB-CAN adapter costs only tens of dollars to get started. For multi-joint, high-bandwidth force control (≥ 1 kHz): Evaluate EtherCAT, but first confirm you can handle a real-time Linux master (refer to the ODRI Master Board concept, odri research archive). More discussion in [Chapter 6: Computing, Power, and Thermal Management](/wiki/chapters/chapter-06/).

## Step 6: Closed-Loop Control Ladder

【What to Do】Climb the ladder step by step, verifying each level before moving to the next:

1. **[PID Control](/entry/ent_method_pid_control/)** : Position loop PID, makes the shaft rotate to a specified angle; the proportional-integral-derivative three terms adjust tracking error, forming the foundation for everything that follows.
2. **[Current-Velocity-Position Three-Loop Cascade](/entry/ent_principle_current_velocity_position_loops/)** : Innermost current loop (torque loop), middle velocity loop, outermost position loop; each layer's bandwidth is approximately 5–10 times that of the next inner layer to ensure stability (three-loop entity card).
3. **[Impedance Control](/entry/ent_method_impedance_control/)** : No longer separates position/force; makes the joint exhibit a desired "mass-damper-spring" characteristic: F = M_d(ẍ_d−ẍ) + D_d(ẋ_d−ẋ) + K_d(x_d−x) (formula source: impedance control entity card).

【Why】A single-loop PID can control position but cannot control "feel" — the motor will still push hard against a collision. The three-loop cascade makes torque (current) an independently assignable command, a prerequisite for impedance control; impedance control allows the joint to respond compliantly according to desired dynamics when disturbed, which is precisely the purpose of QDD/ODRI-type actuators. Theoretical details in [Chapter 14: Fundamentals of Robot Control](/wiki/chapters/chapter-14/) and [Chapter 8: Humanoid Robot Design Principles](/wiki/chapters/chapter-08/).

【How to Analyze Your Situation】Actuator route: The three loops are sealed inside the actuator; you only have a position command interface, focus your effort on trajectory planning. Self-developed QDD: FOC boards (B-G431B / ODrive etc.) generally come with built-in current and velocity loops; you write the outer position loop + feedforward. Impedance control requires high current loop bandwidth and low communication latency; start with a "virtual spring" experiment (set K_d, manually turn the output shaft to feel the restoring force) before moving to complex control.

## Step 7: Bench Testing and Acceptance

【What to Do】Fix the joint to a test bench (profile rail + fixture, hang a known mass on the output shaft as a load), perform four tests sequentially. Criteria are engineering recommendations; adjust according to your own specification sheet:

1. **Step Response**: 30° step, record the angle curve. Criteria: rise time < 0.2 s, overshoot < 10%, steady-state error < 0.5°.
2. **Sine Tracking**: 1 Hz, ±20° sine command. Criteria: amplitude attenuation < 10%, phase lag < 15°; sweeping frequency to −3 dB quantifies bandwidth.
3. **Backdrivability Feel** (QDD/Direct Drive only): Easily movable by hand when powered off; with power on and zero stiffness set, should be draggable with "zero gravity" feel. High reduction ratio actuators fail this test directly — it's determined by topology, not tunable.
4. **Temperature Rise**: Continuous operation at rated load for 30 minutes; motor case temperature recommended < 60 °C (insulation class limit must be confirmed with the motor supplier). Durability reference: Berkeley used a 60-hour endurance test to verify the reliability of 3D-printed cycloidal gears (berkeley-humanoid-lite archive); for self-developed gearboxes, sample test at this magnitude.

【Why】Step response tests rigidity and damping, sine tracking tests bandwidth, backdrivability tests transparency, temperature rise tests thermal design margin — these four items together provide all key information for "can it be installed in the leg." Finding a problem at the bench stage means removing just one motor; finding it after integration into the whole machine means disassembling an entire leg. Testing methods in [Chapter 11: Assembly, Integration, and Testing](/wiki/chapters/chapter-11/).

【How to Analyze Your Situation】No oscilloscope? Use the driver's USB host software (ODrive Tool, Dynamixel Wizard, etc.) to record curves; it's sufficient. Calculate the load mass inversely from "peak torque ÷ lever arm length." If time is tight, thoroughly complete the step response and temperature rise tests; leave the sine sweep for the whole machine integration stage.

## Acceptance Criteria

- [ ] Specification sheet documented: Peak torque/speed/mass/backlash/cost — five items with numbers and sources (or marked "needs confirmation from supplier").
- [ ] Topology selection has written justification: Explain which edge of the "precision-transparency-cost" triangle was chosen and why other routes were not selected.
- [ ] Communication link established: Main controller sends/receives stably at target frequency (CAN recommended ≥ 250 Hz, per Berkeley scheme) for 1 continuous hour without disconnection.
- [ ] Step response: 30° step, overshoot < 10%, steady-state error < 0.5° (or value defined in specification sheet).
- [ ] Sine tracking: 1 Hz ±20°, amplitude attenuation < 10% (or self-defined value), curve recorded and archived.
- [ ] QDD/Direct Drive solution: Smooth manual backdrivability; for dual encoder solutions, the deviation between motor-side and output-side readings has been quantified.
- [ ] Temperature rise: 30 minutes at rated load, case temperature < 60 °C or within the limit given by the supplier.
- [ ] Gearbox assembly: No jamming, no abnormal noise throughout operation; no-load current matches the baseline measured on the first unit.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| CAN bus frame loss, random interruptions in multi-node communication | Missing or duplicate termination resistors | Power off and measure resistance between CANH-CANL: should be ~60 Ω with 120 Ω at each end; infinite = missing, far below 60 Ω = too many |
| Encoder reading jitter, speed loop oscillation | Ground loop / improper shield grounding / magnetic encoder interference from phase lines | Single-point ground for signal ground; use twisted-pair shielded encoder wires, keep away from phase lines |
| FOC auto-tuning fails, motor hums but doesn't rotate | Wrong pole pair count / incorrect phase sequence / encoder electrical angle offset not calibrated | Verify pole pair count; perform open-loop low-current rotation test to confirm phase sequence; redo encoder offset calibration |
| Stiffness, overheating, high no-load current after reducer assembly | Excessive bearing/gear preload, axis misalignment, warped 3D-printed parts | Tighten in a cross pattern and manually rotate step by step; check coaxiality; compare no-load current before and after assembly |
| Large overshoot and ringing in step response | Excessive position loop gain, missing velocity feedforward, unexpected load inertia | Reduce P, increase D, or add feedforward; measure actual load inertia and retune |
| Motor gets hot to the touch after a few minutes of stall | Continuous current exceeds rating, no thermal protection | Check phase current (not supply current) against motor rating; add current limiting and I²t thermal protection |
| Bus chaos when multiple actuators power on simultaneously | Duplicate factory-default node IDs | Power on each unit individually, change ID, label it, then network them together |

## Related Reading

- [Actuator Selection Guide](playbooks/actuator-selection.md) — More comprehensive route comparison, manufacturer quick reference, and verification methods
- [Compute Platform Selection Guide](playbooks/compute-selection.md) — Board selection for the real-time control layer
- [Roadmap Overview](index.md)
