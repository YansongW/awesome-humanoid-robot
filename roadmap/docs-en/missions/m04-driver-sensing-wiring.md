# M04 · Drives, Sensing, and Wiring: Making the Joint Understand and Respond

**Global Position**: After M02 Motor Selection and M03 Reducer Design, before M05 Assembly and M06 Firmware. Inputs are the motor parameters calculated in M02 (phase current, phase resistance, KV, bus voltage level) and the reducer structure from M03. Outputs are three items: **drive board selection conclusion, encoder scheme, single-joint electrical drawings (power/signal/bus)** — M05 wires according to the drawings, M06 burns firmware according to the scheme.

**Prerequisites**: Motor calculations from M02 are complete (continuous phase current and bus voltage are quantified); the reducer structure from M03 is finalized (knowing where the encoder can be mounted and where the wires pass through).

Theoretical background: [Field-Oriented Control (FOC)](/entry/ent_method_foc_motor_control/), [Servo Drive](/entry/ent_component_servo_drive_2024/), [Joint Encoder](/entry/ent_component_joint_encoder_2024/), [CAN Bus](/entry/ent_technology_can_bus_2024/) cards; systematic discussion in [Chapter 4 Actuators](/wiki/chapters/chapter-04/), [Chapter 5 Sensing and Perception Hardware](/wiki/chapters/chapter-05/), and [Chapter 6 Computing, Power, and Thermal Management](/wiki/chapters/chapter-06/).

## Step 1: Drive Selection — FOC is the Baseline

[What to do] Only consider drive solutions that support [FOC](/entry/ent_method_foc_motor_control/), converging to one from the candidates in the table below:

| Candidate | Positioning | Source/Anchor |
|---|---|---|
| ST B-G431B-ESC1 | Cheapest FOC entry board, $19 | Standard for Berkeley 6512 actuator ([Berkeley Humanoid Lite GitHub](https://github.com/HybridRobotics/Berkeley-Humanoid-Lite)) |
| ODrive / Moteus / VESC | Third-party open-source drives, mature ecosystem | Berkeley structure compatible with these three (same repository) |
| ODRI MicroDriver | Research-grade custom drive card, BSD fully open-source design files | [ODRI Actuator Hardware Repository](https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware), beginner-friendliness 2/5 |

After selection, perform two hard checks and record them on the drawing title page:

```
Check 1 (Voltage): Drive board voltage range ⊇ M02's determined bus voltage level (e.g., 24 V level must cover 6S full charge)
Check 2 (Current): Continuous phase current rating ≥ I_M02 × 1.5   (1.5 is an engineering recommended margin, verify based on thermal conditions)
```

Example: M02 calculates joint continuous phase current 8 A → requires drive board continuous rating ≥ 12 A; bus voltage 24 V level → board rated voltage must cover 24 V. Look up the datasheet and fill both values into the acceptance table; if not found, mark "Must confirm with supplier," do not assume "should be enough."

[Why] FOC transforms three-phase currents into the d-q coordinate system rotating with the rotor, decoupling torque and flux linkage. It is a prerequisite for low torque ripple and current-loop force control (FOC entity card); cheap six-step commutation ESCs cannot achieve this, making all M07 force control impossible. Drive board overcurrent burnout is the most common hardware accident during the bench testing phase; the 1.5x margin is reserved for startup/stall current spikes.

[How to analyze your situation] Tight budget, willing to solder: B-G431B-ESC1. Berkeley has verified that a "$129 motor + $19 drive board" can run zero-shot sim-to-real locomotion. Want out-of-the-box, minimal power-stage work: Moteus/ODrive. Want to develop the drive board yourself: Read the ODRI `open_robot_actuator_hardware` repository first before deciding; the entry barrier is high (odri documentation).

## Step 2: Current Sensing and Current Loop — The Upper Limit of Force Control Lies Here

[What to do] Open the schematic/documentation of the selected drive board, confirm three items, and record them in the drawings:

1. **Current Sensing Topology**: Low-side three-resistor, low-side single-resistor, or inline (phase wire) sampling — conceptual difference: low-side sampling is cheap but can only see current during specific PWM windows; inline sampling provides continuous visibility but is costly;
2. **Current Loop Bandwidth**: Target ≥ 1 kHz (engineering recommended value, verify against board documentation and actual measurement);
3. **Whether sampling is synchronized with PWM**: If not synchronized, switching noise will be captured, causing noisy current readings.

[Why] The force control of [Quasi-Direct Drive (QDD)](/entry/ent_technology_quasi_direct_drive_actuator_2024/) is essentially "using the current loop as a torque sensor" — the faster and more accurate the current loop, the faster and more accurate the force control. Remember one sentence: **Force control performance = Current loop performance + Communication latency**. In the three-loop cascade, the current loop is the innermost; the outer loop bandwidth can only be 1/5–1/10 of it ([Current-Velocity-Position Three Loops](/entry/ent_principle_current_velocity_position_loops/) card). If the inner loop is weak, the whole system fails.

[How to analyze your situation] Smart servo route: Skip this step (the loop is sealed inside the servo). Self-developed QDD: Use the drive board's host software to perform a current step test, record the rise time, and back-calculate the bandwidth; if the sense resistor gets hot or readings are noisy, first check the layout and sampling timing, then suspect the algorithm.

## Step 3: Encoder Scheme and Mounting

[What to do] Magnetic encoder scheme = chip + radially magnetized magnet ([Neodymium Magnet](/entry/ent_mat_neodymium_magnet/)) + 3D-printed bracket. Order the three items separately:

- Chip: Start with AS5600 (12-bit, $3, used by Berkeley, berkeley-humanoid-lite repository); for finer velocity estimation, upgrade to a higher-resolution model (price must be confirmed with supplier).
- Quantity: One on the motor side is mandatory (for FOC commutation); for force control, add one on the output side to form a dual-encoder setup.

Record the three installation essentials in the assembly process card: ① Magnet and chip are **coaxial**; ② Magnet-chip gap follows the value specified in the chip datasheet (must be confirmed based on the selected model); ③ Encoder and its wiring are **kept away from high-current phase wires**. Select the interface based on bandwidth and wire count:

| Interface | Signal Wire Count | Bandwidth/Latency Qualitative | Suitable For |
|---|---|---|---|
| I²C | 2 | Slow, suitable for low-speed reading | Debugging/Auxiliary |
| SPI | 4 | Fast, low latency | Preferred for motor-side FOC commutation |
| ABI (Incremental) | 3 | Fast, but absolute angle unknown on power-up | Applications with homing capability |
| PWM | 1 | Simple, anti-interference, limited resolution | Low-cost backup |

[Why] The motor-side encoder is the lifeline of FOC: commutation requires knowing the rotor's electrical angle; a one-degree reading error causes a corresponding torque ripple. The value of the output-side encoder is to "see through" the reducer — dual encoders can directly measure backlash and elastic deformation. The ODRI BLMC actuator achieves proprioceptive force control precisely through motor-side/output-side dual encoders (odri documentation); installing only the motor-side encoder systematically overestimates accuracy ([Joint Encoder](/entry/ent_component_joint_encoder_2024/) card). Magnetic encoders are sensitive to coaxial alignment and electromagnetic interference; these two factors account for the vast majority of abnormal readings for beginners.

[How to analyze your situation] Smart servo: The built-in feedback is sufficient; don't overcomplicate. Self-developed QDD for position control only: Install the motor-side encoder first, and reserve bracket mounting holes on the housing for the output-side encoder. Target RL locomotion/force control: Go straight to dual encoders; starting with the AS5600 level is sufficient — for more trade-offs, see the [Sensor Selection Manual](../playbooks/sensor-selection.md).

## Step 4: Wire Gauge, Voltage Drop, and Connectors

[What to do] Select wire gauge using the formula, criterion: **Full-load voltage drop ≤ 5% of bus voltage** (engineering recommended value):

```
R = ρ·L / A      ρ_copper = 1.7×10⁻⁸ Ω·m, L is total round-trip length, A is wire cross-sectional area
ΔV = I·R         Requirement ΔV ≤ 0.05 × V_bus
```

Complete example (bus voltage 24 V level, joint peak current 10 A, one-way wire length 1 m, AWG data for generic copper wire):

```
20 AWG: A ≈ 0.518 mm² → R = 1.7e-8 × 2 / 0.518e-6 ≈ 0.066 Ω
ΔV = 10 × 0.066 = 0.66 V ≈ 2.7% of 24 V  ✓ Pass
Same condition, 12 V bus: 0.66 / 12 = 5.5%  ✗ → Switch to 18 AWG (A ≈ 0.82 mm², ΔV ≈ 0.41 V ≈ 3.4% ✓)
```

Connector selection: Use XT30 (small joints) / XT60 (trunk lines) for power, with keying and locking features; use JST type for signals. All solder/crimp points should have strain relief (heat shrink + cable clamp); bend radius ≥ 5x wire diameter (engineering recommended value); route power and signal wires in **separate bundles**; when crossing is unavoidable, cross perpendicularly.

[Why] Wire resistance not only consumes voltage but also generates heat: the 0.066 Ω in the example dissipates 0.66 W at 10 A, which becomes a heat source when enclosed in the joint housing. In a vibrating environment, most "intermittent power loss" incidents are due to loose or poorly crimped connectors, not a faulty board.

[How to analyze your situation] For internal joint wiring < 0.3 m, you can slightly reduce wire gauge to save weight; trunk lines from the torso to the legs must be calculated item by item. First, build a sample wire run and measure the voltage drop at 10 A before bulk ordering — actual measurement is more reliable than tables.

## Step 5: CAN Bus Electrical

【What to Do】Wire in a daisy-chain (hand-in-hand) topology, **star topology is prohibited**; solder one 120 Ω termination resistor at each end of the bus; stub lengths ≤ 0.3 m (engineering recommendation). Power off after completion, measure resistance between CANH-CANL with a multimeter; it should be ≈ 60 Ω (two 120 Ω resistors in parallel). Baud rate is tied to cable length: 1 Mbps corresponds to meter-scale cable length; for longer cables, reduce the baud rate (engineering recommendation, verify against the transceiver datasheet).

For the anchor solution, you can directly copy: Berkeley Humanoid Lite has one CAN 2.0 bus per limb (1 Mbps, connected to the main controller via a USB-CAN adapter), actuators and IMU communicate at 250 Hz, with a maximum of 64 devices per bus (berkeley-humanoid-lite archive).

【Why】[CAN](/entry/ent_technology_can_bus_2024/) relies on differential signals for noise immunity, but high-frequency signals reflect at cable ends—termination resistors absorb these reflections; without them, waveform ringing and random frame loss occur. The daisy-chain topology ensures continuous impedance along each segment; star branches are impedance discontinuities, and communication becomes unreliable as node count increases. If bandwidth is insufficient, evaluate [EtherCAT](/entry/ent_technology_ethercat_2024/), at the cost of expensive slave chips and the need for a real-time Linux master (refer to the ODRI Master Board approach, odri archive).

【How to Analyze Your Situation】Number of joints ≤ 12, control frequency ≤ 500 Hz: CAN 2.0 is sufficient; a USB-CAN adapter costs tens of dollars to get started. Multiple driver boards ship with the same default node ID; **power them on one by one to change IDs, label them, then network them**; otherwise, all devices will conflict on the bus as soon as it is activated.

## Acceptance Criteria

- [ ] Single-joint electrical drawings documented: three drawings for power, signal, and bus, specifying wire gauge, connector model, and termination resistor location.
- [ ] Two hard checks (voltage, current) for the driver board with formulas and numerical values, sourced from the datasheet or marked as "needs confirmation from supplier."
- [ ] Encoder readings stable when stationary: fluctuation on the order of ±1 LSB (AS5600 is 12-bit, 1 LSB ≈ 0.088°, see [Sensor Selection Manual](../playbooks/sensor-selection.md)).
- [ ] Wire gauge selection includes complete formulas and calculation examples; measured voltage drop at full load ≤ 5% of the bus voltage.
- [ ] CAN network measured with power off: CANH-CANL ≈ 60 Ω; continuous communication at 250 Hz for 1 hour without disconnection.
- [ ] Each driver board node ID is unique and labeled, recorded in the drawings.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Encoder readings jitter, velocity loop oscillation | Magnetic encoder routed parallel to phase wires / Magnet eccentric or gap misaligned | Twist encoder wires, keep away from phase wires; recheck coaxiality and gap |
| CAN communication randomly interrupted | Termination resistor missing/duplicated, star topology | Measure 60 Ω with power off: infinite = missing, far below 60 = too many; change to daisy-chain |
| Connector/harness heating | Loose connection, undersized wire gauge, poor crimping | Use infrared thermography at full load to locate hot spots; re-crimp or increase wire gauge |
| I²C encoder data erratic | Incorrect pull-up resistors, trace too long | Shorten traces, adjust pull-ups per datasheet; if still problematic, switch to SPI |
| Communication intermittent, no pattern found | Ground loop (multiple ground points) | Single-point grounding for signal ground; use isolated CAN transceivers if necessary |
| Occasional power loss after vibration | Poor terminal crimping, no strain relief | Perform pull-force tests on each wire; add heat shrink tubing and cable clamps |

## Companion Reading

- Previous task: [M03 · Reducer Design and Calculation](m03-reducer-design.md)
- Next task: [M05 · 3D Printing and Mechanical Assembly](m05-print-assembly.md)
- Manuals: [Actuator Selection Manual](../playbooks/actuator-selection.md) · [Sensor Selection Manual](../playbooks/sensor-selection.md)
- Theoretical background: [Chapter 4 Actuators](/wiki/chapters/chapter-04/), [Chapter 5 Sensing and Perception Hardware](/wiki/chapters/chapter-05/), [Chapter 6 Computing, Power, and Thermal Management](/wiki/chapters/chapter-06/)
- [Stage 1 Overview](../stage-1-actuator.md) · [Roadmap Overview](../index.md)
