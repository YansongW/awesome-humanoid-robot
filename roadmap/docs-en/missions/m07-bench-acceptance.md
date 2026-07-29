# M07 · Bench Testing and Acceptance: Data Speaks, Only Passed Units Are Installed

**Global Position**: After M06 firmware and calibration, before the whole-machine phase (M08 Selection / M09 Assembly). The input is a joint module that "can rotate", and the output is a **measured data package** (curves + conclusions)—upgrading the M01 specification table from an "estimated version" to a "measured version". Only after all six tests are passed can this joint be installed. This page expands [Stage 1 Overview](../stage-1-actuator.md) Step 7 to a hands-on level.

**Prerequisites**: M06 acceptance passed (three loops tuned, 250 Hz communication stable); profile bench, weight bar and weights, temperature measurement tools (infrared thermometer or thermocouple) ready.

Theoretical background: Test methods in [Chapter 11 Assembly, Integration, and Testing](/wiki/chapters/chapter-11/), evaluation methodology in [Chapter 25 Robot Evaluation System](/wiki/chapters/chapter-25/), control criteria in [Chapter 14 Robot Control Basics](/wiki/chapters/chapter-14/).

## Step 1: Bench Setup—First Ensure the Bench Itself Does Not Lie

【What to Do】

1. **Rigid Fixation**: Lock the joint module with aluminum profiles + clamps, with the output shaft extending horizontally. First perform a "hand shake/tap test": no movement, rapid vibration decay upon tapping, and the bench's natural frequency clearly separated from the joint's motion frequency—bench resonance will contaminate all data (see Common Pitfall #1).
2. **Weight Bar Load**: Bar length measured from the output shaft center to the weight hanging point. Load mass calculated inversely from peak torque:

   ```
   m = τ_peak ÷ (g × L)
   Example: τ_peak = 8 N·m, bar length L = 0.5 m
   m = 8 ÷ (9.81 × 0.5) ≈ 1.63 kg
   ```

   Prepare weights in three levels: 0 kg (no load) / 0.8 kg (half load) / 1.63 kg (full load).
3. **Recording Chain**: The driver board host computer synchronously records angle/current/temperature at a sampling rate ≥ control frequency (250 Hz, matching Berkeley communication rate, [Berkeley Humanoid Lite paper](https://arxiv.org/html/2504.17249v1)); save each curve along with test conditions (load level, firmware version, gain parameters) in raw format.

【Why】The bench is not a supporting actor; it is part of the measurement instrument: a 1 mm loose clamp adds a false ring to the step response; saving only screenshots without raw data makes reproduction impossible three months later. Accurate measurement requires that "everything except the test object is stiffer and more stable than it."

【How to Analyze Your Situation】No aluminum profiles: thick steel plate + bench vise works, with the same criteria—no movement by hand, crisp sound when tapped. No weights: dumbbell plates or water bottles are fine, but mass must be measured with a scale, not taken from nominal values. Don't forget the weight bar's own mass: bar inertia about the axis ≈ ⅓·m_bar·L², which must be included in the load (see Common Pitfall #2).

## Step 2: Step Response—The Mirror of Stiffness and Damping

【What to Do】Apply a 30° position step (maximum load torque when the weight bar rotates to horizontal), record the angle curve. Criteria (engineering recommended values, adjust per your M01 specification table; consistent with [Stage 1 Overview](../stage-1-actuator.md)):

- Rise time < 0.2 s;
- Overshoot < 10% (i.e., peak not exceeding 33°);
- Steady-state error < 0.5°.

Test three times each for no load → half load → full load, archive all curves. Slower rise and larger overshoot under load are normal; if any item exceeds limits under full load, first return to M06 Step 4 to retune with actual load inertia, and only question the specification itself if tuning fails.

【Why】The step response reveals three things at once: whether gain is sufficient (rise time), whether damping is sufficient (overshoot and ringing), and whether static error and gravity/friction compensation are adequate (steady-state error). These three directly determine whether the joint "follows commands" in the whole-machine phase.

【How to Analyze Your Situation】Full load overshoot of 15% cannot be reduced: first add gravity feedforward/friction compensation, then reduce position loop P and increase D; if still not working, recalculate load inertia—if inertia quadruples, original gains will inevitably oscillate. For hip and knee joints that "bear whole-machine impact during the stance phase," it is recommended to tighten the full load criteria (e.g., overshoot < 5%, engineering recommended value), which will benefit the whole-machine phase.

## Step 3: Frequency Response and Bandwidth—Can It Really Be Used as a Leg

【What to Do】

1. First send a 1 Hz, ±20° sinusoidal position command. Criteria (engineering recommended values, same as [Stage 1 Overview](../stage-1-actuator.md)): amplitude attenuation < 10% (output peak-to-peak ≥ 36°), phase lag < 15°.
2. Then sweep frequency: measure output/command amplitude ratio stepwise from 0.5 → 1 → 2 → 5 → 10 → 20 Hz, find the frequency where amplitude drops to 70.7% (−3 dB)—this is the **measured position loop bandwidth**.

Why bandwidth determines leg capability: during walking, the stance/swing phase switches once per step; a step frequency of 1–2 Hz means the joint experiences multiple load transients and command reversals per second, with frequency components far higher than the step frequency itself. When position loop bandwidth is only a few Hz, the joint is "still chasing the previous command" during stance phase transitions, resulting in soft legs and wobbling. Recommended bandwidth for major leg joints ≥ 10 Hz (engineering recommended value, adjust per your gait frequency).

【Why】Step response looks at the time domain, frequency sweep at the frequency domain—two photos of the same system; the sweep quantifies "response capability" into a comparable hard metric, upgrading the corresponding column in the M01 specification table to measured values.

【How to Analyze Your Situation】Three approaches for insufficient bandwidth: increase position loop gain (constrained by overshoot) → acceleration/velocity feedforward → check mechanical backlash and encoder resolution (nonlinearities fundamentally limit bandwidth; tuning cannot solve). High reduction ratio servo solutions are inherently limited by topology—record honestly and note in the specification table "not for dynamic walking."

## Step 4: Backdrivability and Force Transparency (Mandatory for QDD/Direct Drive)

【What to Do】[Quasi-Direct Drive (QDD)](/entry/ent_technology_quasi_direct_drive_actuator_2024/) and direct drive solutions add three tests; for high reduction ratio solutions (servo/harmonic), directly record "Fail—determined by topology," no need to force test.

1. **Power-off Backdrivability**: Manually rotate the output shaft with power off; should be smooth without jamming or noticeable cogging torque.
2. **Zero Stiffness Drag**: Power on, set zero stiffness (position gain = 0, low damping); should be able to drag the output shaft with "zero gravity" feel—this is a degenerate form of [impedance control](/entry/ent_method_impedance_control/) and a prerequisite for subsequent force control.
3. **Current-Torque Calibration (Measure Kt)**: Hang a known weight and hold stationary, record steady-state phase current, back-calculate the measured torque constant:

   ```
   Kt_output = τ ÷ I = (m × g × L) ÷ I
   Example: m = 1.63 kg, L = 0.5 m → τ = 1.63 × 9.81 × 0.5 ≈ 8.0 N·m
   Measured steady-state phase current I = 5.2 A
   Kt_output = 8.0 ÷ 5.2 ≈ 1.54 N·m/A
   ```

   Compare with theoretical value (motor Kt × reduction ratio × efficiency, from M02 manual); if deviation > 10%, investigate cause (engineering recommended value): incorrect current sampling calibration, friction consuming torque, or inflated manual Kt.
4. **Dual Encoder Solution**: Synchronously record readings from the motor-side and output-side [joint encoder](/entry/ent_component_joint_encoder_2024/); their difference = reducer deformation + backlash—ODRI uses this difference for proprioceptive force control ([ODRI actuator hardware repository](https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware)). The difference under no load approximates backlash; the incremental difference under load approximates reducer stiffness deformation; record both in the data package.

【Why】Force transparency is the raison d'être of QDD: the equation "current ≈ torque" holds, allowing subsequent impedance/force control without additional torque sensors. If Kt deviation is large but manual values are used, the whole-machine force control feedforward will be entirely wrong.

【How to Analyze Your Situation】Cannot rotate by hand when powered off: check for overly tight reducer assembly (return to M05) or topology that is inherently non-backdrivable. "Jerky" motion during zero stiffness drag: mostly cogging torque + uncompensated friction; add a small amount of current feedforward compensation, record the compensation amount in the data package (directly reusable in the whole-machine phase).

## Step 5: Temperature Rise and Durability – Time is the Revealer

【What to Do】

1. **Temperature Rise**: Run continuously for 30 min under rated load (half-load weight tracking a 1 Hz sine wave, or equivalent based on your M01 duty cycle), and record the case temperature curve. Criterion: Case temperature < 60 °C (engineering recommended value; the insulation class limit must be confirmed with the motor supplier). Record the ambient test temperature as well; for summer retests, adjust based on the temperature rise difference.
2. **Durability Sampling**: Berkeley verified the reliability of 3D-printed cycloidal gears with 60 hours of continuous operation ([arXiv:2504.17249](https://arxiv.org/abs/2504.17249)) – for your custom reducer, sample test at this scale: run the first unit for 60 h, and sample 10% of production units for 10–20 h (engineering recommended process). After running, inspect gear tooth wear, and retest backlash and no-load current, comparing against the first unit baseline.
3. **Efficiency Rough Measurement**: Under constant high-load conditions, input electrical power vs. output mechanical power:

   ```
   η = (τ × ω) ÷ (V × I)
   Example: Output τ = 4 N·m, ω = 3 rad/s → Mechanical power 12 W
   Input 24 V × 1.0 A = 24 W
   η = 12 ÷ 24 ≈ 50%
   ```

   This is the total efficiency of the reducer + motor + drive, a reference order-of-magnitude value, to be verified against your system.

【Why】Passing step response tests only shows "instantaneous capability"; temperature rise and durability show "whether it can sustain that capability" – walking is a continuous minute-to-hour-level operation; insufficient thermal margin means overheating and derating after a few steps. Efficiency directly determines M09 battery selection and range estimation. For thermal design background, see [Chapter 6: Computation, Power, and Thermal Management](/wiki/chapters/chapter-06/).

【How to Analyze Your Situation】No temperature sensor: Use an infrared thermometer for case temperature + the drive board's built-in temperature reading for dual recording. If it can't sustain 30 min: Gradually reduce the continuous current limit to find the "current that can sustain 30 min," then back-calculate the actual usable continuous torque – this value is what should be written as the rated value in the M01 specification table.

## Step 6: Data Write-Back and Release Decision

【What to Do】

1. Fill the measured values item by item back into the [M01 Specification Table](m01-scenario-to-specs.md): Peak torque (measured Kt × current limit), bandwidth, backlash, continuous torque, efficiency – upgrade from "estimated version" to "measured version."
2. Handle out-of-tolerance items one by one, choosing one of three paths: Insufficient performance → **Replace the motor** (back to M02); Mismatched response or torque → **Change the reduction ratio** (back to M03); The specification itself is set too high → **Change the specification** (back to M01, must include a written reason: "Why reducing the specification does not affect the mission requirements").
3. After all items meet criteria, output a written conclusion: "This joint module is ready for assembly," along with a data package index (curve directory + parameter version + test bench photos + wiring diagram).

【Why】Write-back turns experience into assets: The measured distribution (Kt, backlash, temperature rise) across 22 joints is first-hand data for parameterizing the actuator model in full-machine simulation (M10/M11) – using measured values in simulation cuts sim-to-real pitfalls by half.

【How to Analyze Your Situation】Testing all 22 units individually is too labor-intensive: Fully test the first 3 units on all six items; for the rest, test only the three key items (step response, temperature rise, Kt). Compare the data distribution with the first unit, and perform full retests on outliers (engineering recommended process, adjust based on your batch size). Name the data package consistently from the start: `JointID_TestItem_Date_FirmwareVersion`.

## Acceptance Criteria

- [ ] Curves for all six tests (step response/sine wave/sweep/back-drive & Kt/temperature rise/durability) are archived in original format, with complete test conditions.
- [ ] 30° step response under three load levels: Rise time < 0.2 s, overshoot < 10%, steady-state error < 0.5° (or value defined in the specification table).
- [ ] 1 Hz ±20° sine wave: Amplitude attenuation < 10%, phase lag < 15°; −3 dB bandwidth has a measured value.
- [ ] QDD/direct drive solution: Smooth zero-stiffness back-driving, measured Kt deviation from theoretical value ≤ 10% or the cause of deviation is identified; dual-encoder difference (backlash + deformation) is quantified.
- [ ] Case temperature < 60 °C (or within supplier's limit) after 30 min at rated load; reducer durability sampling is completed with inspection records.
- [ ] M01 specification table is upgraded to "measured version," with a disposition conclusion for all write-back discrepancies (replace motor/change reduction ratio/change specification, including written reasons).
- [ ] The "ready for assembly" conclusion is documented in writing; test bench photos and wiring diagrams are archived.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Fixed-frequency oscillation in step response curve | Bench resonance mistaken for joint oscillation | Reinforce fixture/add mass to bench and retest; tap the bench to identify natural frequency |
| Bandwidth much lower than M06 no-load tuning value | Inertia of weight bar and weights neglected | Include ⅓·m_bar·L² + m_weight·L² in load calculation and retune |
| Two temperature rise results don't match | Ambient temperature/airflow not fixed | Fix ambient temperature and placement, record room temperature; adjust based on temperature rise difference |
| Passes no-load tests but fails when installed | Only no-load tests performed before declaring pass | Three load levels are a hard requirement; failing under full load = fail |
| Data cannot be reproduced for analysis | Only screenshots saved, no raw data | Save raw format (csv/log) along with firmware version and parameters |
| Measured Kt much lower than datasheet | Friction not compensated / power supply current mistaken for phase current | Confirm phase current reading; measure in both directions and average to cancel friction |
| Backlash increases after durability test | Gear wear / bearing clearance increase | Inspect gear teeth; evaluate material/process change against Berkeley's 60 h scale |

## Companion Reading

- Previous Task: [M06 · Firmware and Calibration](m06-firmware-calibration.md)
- Next Task: [M08 · Platform Selection and Procurement](m08-platform-selection.md)
- Theoretical Background: [Chapter 11: Assembly, Integration, and Testing](/wiki/chapters/chapter-11/), [Chapter 25: Robot Evaluation System](/wiki/chapters/chapter-25/), [Chapter 14: Fundamentals of Robot Control](/wiki/chapters/chapter-14/), [Chapter 6: Computation, Power, and Thermal Management](/wiki/chapters/chapter-06/)
- [Stage 1 Overview](../stage-1-actuator.md) · [Stage 2 Overview](../stage-2-biped.md) · [Actuator Selection Handbook](../playbooks/actuator-selection.md)
