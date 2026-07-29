# M04 · Drives, Sensing, and Wiring: Making the Joint Listen and Respond

**Global Position**: After M02 Motor Selection and M03 Reducer Design, before M05 Assembly and M06 Firmware. Inputs are the motor parameters (phase current, phase resistance, KV, bus voltage level) calculated in M02 and the reducer structure from M03. Outputs are three items: **drive board selection conclusion, encoder scheme, single-joint electrical drawings (power/signal/bus)** — M05 wires according to the drawings, M06 burns firmware according to the scheme.

**Prerequisites**: M02 motor calculations are complete (continuous phase current and bus voltage are quantified); M03 reducer structure is finalized (know where the encoder can be mounted and where the wires pass through).

Theoretical background: [Field-Oriented Control (FOC)](/entry/ent_method_foc_motor_control/), [Servo Drive](/entry/ent_component_servo_drive_2024/), [Joint Encoder](/entry/ent_component_joint_encoder_2024/), [CAN Bus](/entry/ent_technology_can_bus_2024/) cards; systematic discussion in [Chapter 4 Actuators](/wiki/chapters/chapter-04/), [Chapter 5 Sensing and Perception Hardware](/wiki/chapters/chapter-05/), and [Chapter 6 Computing, Power, and Thermal Management](/wiki/chapters/chapter-06/).

## Step 1: Drive Selection — FOC is the Baseline

[What to do] Only consider drive solutions that support [FOC](/entry/ent_method_foc_motor_control/). Converge to 1 candidate from the table below:

| Candidate | Positioning | Source/Anchor |
|---|---|---|
| ST B-G431B-ESC1 | Cheapest FOC entry board, $19 | Standard for Berkeley 6512 actuator (`data/roadmap/research/berkeley-humanoid-lite.md`) |
| ODrive / Moteus / VESC | Third-party open-source drives, mature ecosystem | Berkeley structure compatible with these three (same file) |
| ODRI MicroDriver | Research-grade custom drive card, design files fully BSD open-source | `data/roadmap/research/open-dynamic-robot-initiative.md`, beginner-friendliness 2/5 |

After selection, perform two hard checks and write them into the drawing title page:

```
Check 1 (Voltage): Drive board voltage range ⊇ M02's determined bus voltage level (e.g., 24 V level must cover 6S full charge)
Check 2 (Current): Continuous phase current rating ≥ I_M02 × 1.5   (1.5 is an engineering recommended margin, verify based on thermal conditions)
```

Example: M02 calculates joint continuous phase current as 8 A → requires drive board continuous rating ≥ 12 A; bus voltage 24 V level → board rated voltage must cover 24 V. Look up the datasheet and fill both values into the acceptance table; if not found, mark "Requires confirmation from supplier," do not assume "should be enough."

[Why] FOC transforms three-phase currents into the d-q coordinate system rotating with the rotor, decoupling torque and flux linkage. It is a prerequisite for low torque ripple and current-loop force control (FOC entity card). Cheap six-step commutation ESCs cannot achieve this, making M07 force control impossible. Drive board overcurrent burnout is the most common hardware accident during the bench testing phase; the 1.5x margin is for startup/stall current spikes.

[How to analyze your situation] Tight budget, willing to solder: B-G431B-ESC1. Berkeley has verified that a "$129 motor + $19 drive board" can run zero-shot sim-to-real walking. Want out-of-the-box, minimal power-stage work: Moteus/ODrive. Want to develop the drive board yourself: First read the ODRI `open_robot_actuator_hardware` repository before deciding; the entry barrier is high (odri file).

## Step 2: Current Sensing and Current Loop — The Upper Limit of Force Control Lies Here

[What to do] Open the schematic/documentation of the selected drive board. Confirm three items and record them in the drawings:

1. **Current sensing topology**: Low-side three-resistor, low-side single-resistor, or inline (phase line) sensing — conceptual difference: low-side sensing is cheap but can only see current during specific PWM windows; inline sensing provides continuous visibility but is costly;
2. **Current loop bandwidth**: Target ≥ 1 kHz (engineering recommended value, verify against board documentation and actual testing);
3. **Is sampling synchronized with PWM**: If not synchronized, switching noise will be sampled, causing noisy current readings.

[Why] The force control of [Quasi-Direct Drive (QDD)](/entry/ent_technology_quasi_direct_drive_actuator_2024/) essentially uses the current loop as a torque sensor — the faster and more accurate the current loop, the faster and more accurate the force control. Remember one sentence: **Force control performance = Current loop performance + Communication delay**. In the three-loop cascade, the current loop is the innermost; the outer loop bandwidth can only be 1/5–1/10 of it ([Current-Velocity-Position Three Loops](/entry/ent_principle_current_velocity_position_loops/) card). If the inner loop is weak, the entire system fails.

[How to analyze your situation] Smart servo route: Skip this step (the loop is sealed inside the servo). Self-developed QDD: Use the drive board's host software to perform a current step test, record the rise time, and back-calculate the bandwidth. If the sensing resistor gets hot or readings are noisy, first check the layout and sampling timing, then suspect the algorithm.

## Step 3: Encoder Scheme and Installation

[What to do] Magnetic encoder scheme = chip + radially magnetized magnet ([Neodymium Magnet](/entry/ent_mat_neodymium_magnet/)) + 3D-printed bracket. Order the three items separately:

- Chip: Start with AS5600 (12-bit, $3, used by Berkeley, berkeley-humanoid-lite file); for finer speed estimation, upgrade to a higher resolution model (price needs confirmation with supplier).
- Quantity: 1 on the motor side is mandatory (for FOC commutation); add 1 on the output side for force control to form a dual-encoder setup.

Write the three installation essentials into the assembly process card: ① Magnet and chip are **coaxial**; ② Magnet-chip gap follows the chip datasheet specified value (confirm based on the selected model); ③ Encoder and its wiring are **kept away from high-current phase wires**. Select the interface based on bandwidth and number of wires:

| Interface | Signal Wires | Bandwidth/Latency Qualitative | Suitable For |
|---|---|---|---|
| I²C | 2 | Slow, suitable for low-speed reading | Debugging/Auxiliary |
| SPI | 4 | Fast, low latency | Preferred for motor-side FOC commutation |
| ABI (Incremental) | 3 | Fast, but absolute angle unknown on power-up | Applications with homing capability |
| PWM | 1 | Simple, anti-interference, limited resolution | Low-cost backup |

[Why] The motor-side encoder is the lifeline of FOC: Commutation requires knowing the rotor electrical angle; a one-degree reading error causes a corresponding torque ripple. The value of the output-side encoder is to "see through" the reducer — a dual-encoder setup can directly measure backlash and elastic deformation. The ODRI BLMC actuator achieves proprioceptive force control precisely through motor-side/output-side dual encoders (odri file). Using only a motor-side encoder systematically overestimates accuracy ([Joint Encoder](/entry/ent_component_joint_encoder_2024/) card). Magnetic encoders are sensitive to installation coaxiality and electromagnetic interference; these two factors account for the vast majority of abnormal readings for beginners.

[How to analyze your situation] Smart servo: The built-in feedback is sufficient; don't overcomplicate. Self-developed QDD for position control only: Install the motor-side encoder first, and reserve bracket mounting holes for the output-side encoder on the housing. Target RL walking/force control: Implement dual encoders in one go; starting with the AS5600 level is sufficient — more trade-offs are discussed in the [Sensor Selection Manual](../playbooks/sensor-selection.md).

## Step 4: Wire Gauge, Voltage Drop, and Connectors

[What to do] Select wire gauge using the formula. Criterion: **Full-load voltage drop ≤ 5% of bus voltage** (engineering recommended value):

```
R = ρ·L / A      ρ_copper = 1.7×10⁻⁸ Ω·m, L is the total round-trip length, A is the wire cross-sectional area
ΔV = I·R         Requirement ΔV ≤ 0.05 × V_bus
```

Complete example (bus 24 V level, joint peak current 10 A, one-way wire length 1 m, AWG data for generic copper wire specifications):

```
20 AWG: A ≈ 0.518 mm² → R = 1.7e-8 × 2 / 0.518e-6 ≈ 0.066 Ω
ΔV = 10 × 0.066 = 0.66 V ≈ 2.7% of 24 V  ✓ Pass
Same condition, 12 V bus: 0.66 / 12 = 5.5%  ✗ → Switch to 18 AWG (A ≈ 0.82 mm², ΔV ≈ 0.41 V ≈ 3.4% ✓)
```

Connector selection: Use XT30 (small joints) / XT60 (main trunk) for power, with keying and locking features; use JST type for signals. All solder/crimp points should have strain relief (heat shrink + cable clamp). Bend radius ≥ 5 times the wire diameter (engineering recommended value). Route power and signal wires in **separate bundles**; when crossing is unavoidable, cross perpendicularly.

[Why] Wire resistance not only consumes voltage but also generates heat: The 0.066 Ω in the example dissipates 0.66 W at 10 A, which becomes a heat source inside the joint housing. In a vibrating environment, most "intermittent power loss" incidents are due to loose or poorly crimped connectors, not a faulty board.

[How to analyze your situation] For internal joint wiring < 0.3 m, you can slightly reduce wire gauge to save weight; the main trunk from the torso to the legs must be calculated item by item. First, build a sample wire section, perform a 10 A actual voltage drop test, then batch order — actual testing is more reliable than tables.

## Step 5: CAN Bus Electrical

【What to Do】Route wiring in a daisy-chain (hand-in-hand) topology, **star topology is prohibited**; solder one 120 Ω termination resistor at each end of the bus; branch stubs ≤ 0.3 m (engineering recommendation). Power off after completion, measure resistance between CANH-CANL with a multimeter; it should be ≈ 60 Ω (two 120 Ω resistors in parallel). Baud rate is linked to cable length: 1 Mbps corresponds to meter-scale cable length; for longer cables, reduce the baud rate (engineering recommendation, verify against the transceiver datasheet).

For the anchor solution, you can directly copy: Berkeley Humanoid Lite has one CAN 2.0 bus per limb (1 Mbps, connected to the main controller via a USB-CAN adapter), actuators and IMU communicate at 250 Hz, with a maximum of 64 devices per bus (berkeley-humanoid-lite archive).

【Why】[CAN](/entry/ent_technology_can_bus_2024/) relies on differential signals for noise immunity, but high-frequency signals reflect at the cable ends—termination resistors absorb these reflections; without them, waveforms ring and frames are randomly lost. The daisy-chain topology ensures continuous impedance along each segment; star branches are impedance discontinuities, and communication becomes unreliable once multiple nodes are added. If bandwidth is insufficient, evaluate [EtherCAT](/entry/ent_technology_ethercat_2024/), at the cost of expensive slave chips and a real-time Linux master (refer to the ODRI Master Board approach, odri archive).

【How to Analyze Your Situation】Number of joints ≤ 12, control frequency ≤ 500 Hz: CAN 2.0 is sufficient, and a USB-CAN adapter costs tens of dollars to get started. Multiple drive boards ship with the same default node ID; **power them on one by one to change the ID, label them, then form the network**, otherwise all devices will conflict on the bus as soon as it is activated.

## Acceptance Criteria

- [ ] Single-joint electrical drawings documented: three drawings for power, signal, and bus, with wire gauge, connector model, and termination resistor location marked.
- [ ] Two hard checks (voltage, current) for the drive board with formulas and values, sourced from the datasheet or marked as "needs confirmation from supplier".
- [ ] Encoder readings stable at rest: fluctuation on the order of ±1 LSB (AS5600 is 12-bit, 1 LSB ≈ 0.088°, see [Sensor Selection Manual](../playbooks/sensor-selection.md)).
- [ ] Wire gauge selection includes complete formulas and calculation examples; measured voltage drop at full load ≤ 5% of the bus voltage.
- [ ] CAN network measured with power off: CANH-CANL ≈ 60 Ω; continuous communication at 250 Hz for 1 hour with no dropouts.
- [ ] Each drive board node ID is unique and labeled, recorded in the drawings.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Encoder readings jitter, velocity loop oscillation | Magnetic encoder routed parallel to phase wires / Magnet eccentric or gap misaligned | Twist encoder wires, keep them away from phase wires; recheck coaxiality and gap |
| CAN communication randomly interrupted | Termination resistor missing/duplicated, star topology | Measure 60 Ω with power off: infinite = missing, far below 60 = too many; switch to daisy-chain |
| Connector/wire harness heating | Loose connection, undersized wire gauge, poor crimping | Locate hot spots with infrared thermometer at full load; re-crimp or increase wire gauge |
| I²C encoder data erratic | Incorrect pull-up resistors, trace too long | Shorten traces, adjust pull-ups per datasheet; if still problematic, switch to SPI |
| Communication intermittent, no pattern found | Ground loop (multiple ground points) | Single-point ground for signal ground; use isolated transceivers for CAN if necessary |
| Occasional power loss after vibration | Poor terminal crimping, no strain relief | Perform pull tests on each wire; add heat shrink tubing and cable clamps |

## Companion Reading

- Previous task: [M03 · Reducer Design and Calculation](m03-reducer-design.md)
- Next task: [M05 · 3D Printing and Mechanical Assembly](m05-print-assembly.md)
- Manuals: [Actuator Selection Manual](../playbooks/actuator-selection.md) · [Sensor Selection Manual](../playbooks/sensor-selection.md)
- Theoretical background: [Chapter 4 Actuators](/wiki/chapters/chapter-04/), [Chapter 5 Sensing and Perception Hardware](/wiki/chapters/chapter-05/), [Chapter 6 Computing, Power, and Thermal Management](/wiki/chapters/chapter-06/)
- [Stage 1 Overview](../stage-1-actuator.md) · [Roadmap Overview](../index.md)
