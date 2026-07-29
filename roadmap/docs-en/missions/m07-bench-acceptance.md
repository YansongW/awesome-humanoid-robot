# M07 · Bench Testing and Acceptance: Data Speaks, Only Passed Units Are Installed

**Global Position**: After M06 firmware and calibration, before the full robot stage (M08 selection / M09 assembly). Input is a joint module that "can rotate", output is a **measured data package** (curves + conclusions) — and the M01 specification table is upgraded from "estimated version" to "measured version". Only after all six tests pass can this joint be installed. This page expands [Stage 1 Overview](../stage-1-actuator.md) step 7 to a hands-on level.

**Prerequisites**: M06 acceptance passed (three loops tuned, 250 Hz communication stable); profile bench, weight bar and weights, temperature measurement tools (infrared thermometer or thermocouple) ready.

Theoretical background: Test methods see [Chapter 11 Assembly, Integration and Testing](/wiki/chapters/chapter-11/), evaluation methodology see [Chapter 25 Robot Evaluation System](/wiki/chapters/chapter-25/), control criteria see [Chapter 14 Fundamentals of Robot Control](/wiki/chapters/chapter-14/).

## Step 1: Bench Setup — First Ensure the Bench Itself Does Not Lie

【What to do】

1. **Rigid Fixation**: Use aluminum profile + clamps to lock the joint module, with the output shaft extending horizontally. First perform a "hand shake/tap test": no movement, tap vibration decays quickly, and the bench natural frequency is clearly separated from the joint motion frequency — bench resonance will contaminate all data (see Common Pitfall #1).
2. **Weight Bar Load**: Bar length measured from output shaft center to weight hanging point, load mass calculated inversely from peak torque:

   ```
   m = τ_peak ÷ (g × L)
   Example: τ_peak = 8 N·m, bar length L = 0.5 m
   m = 8 ÷ (9.81 × 0.5) ≈ 1.63 kg
   ```

   Prepare weights in three levels: 0 kg (no load) / 0.8 kg (half load) / 1.63 kg (full load).
3. **Recording Chain**: The drive board host computer synchronously records angle/current/temperature, sampling rate ≥ control frequency (250 Hz, benchmarked against Berkeley communication rate, `data/roadmap/research/berkeley-humanoid-lite.md`); each curve, along with test conditions (load level, firmware version, gain parameters), is saved in raw format.

【Why】The bench is not a supporting actor; it is part of the measurement instrument: a 1 mm loose clamp adds a false ringing to the step response curve; saving only screenshots without raw data makes reproduction analysis impossible three months later. The prerequisite for accurate measurement is "everything except the measured object is harder and more stable than it".

【How to analyze your situation】No aluminum profile: thick steel plate + bench vise also works, same criteria — no movement when shaken, crisp tap sound. No weights: dumbbell plates, water bottles are fine, but mass must be measured with a scale, not taken from nominal values. Don't forget the weight bar's own weight: bar inertia about the axis ≈ ⅓·m_bar·L², must be included in the load (see Common Pitfall #2).

## Step 2: Step Response — The Mirror of Stiffness and Damping

【What to do】Apply a 30° position step (maximum load torque when the weight bar rotates to horizontal), record the angle curve. Criteria (engineering recommended values, adjust according to your M01 specification table; consistent with [Stage 1 Overview](../stage-1-actuator.md)):

- Rise time < 0.2 s;
- Overshoot < 10% (i.e., peak does not exceed 33°);
- Steady-state error < 0.5°.

Test three times each for no load → half load → full load, archive all curves. Slower rise and larger overshoot under load are normal; if any item exceeds the limit under full load, first go back to M06 step 4 and retune with actual inertia under load; if tuning fails, then question the specification itself.

【Why】The step response reveals three things at once: whether gain is sufficient (rise time), whether damping is sufficient (overshoot and ringing), and whether static error and gravity/friction compensation are adequate (steady-state error). These three directly determine whether the joint "follows commands" during the full robot stage.

【How to analyze your situation】Full load overshoot of 15% cannot be reduced: first add gravity feedforward/friction compensation, then reduce position loop P and increase D; if still not working, recalculate load inertia — if inertia quadruples, original gains will inevitably oscillate. For joints like hip and knee that "bear full robot impact during stance phase", it is recommended to tighten the full load criteria (e.g., overshoot < 5%, engineering recommended value), which will benefit the full robot stage.

## Step 3: Frequency Response and Bandwidth — Can It Really Be Used as a Leg

【What to do】

1. First send a 1 Hz, ±20° sinusoidal position command. Criteria (engineering recommended values, same as [Stage 1 Overview](../stage-1-actuator.md)): amplitude attenuation < 10% (output peak-to-peak ≥ 36°), phase lag < 15°.
2. Then sweep frequency: measure output/command amplitude ratio step by step at 0.5 → 1 → 2 → 5 → 10 → 20 Hz, find the frequency where amplitude drops to 70.7% (−3 dB) — this is the **measured position loop bandwidth**.

Why bandwidth determines whether it can be a leg: during walking, each step switches between stance/swing phase, a step frequency of 1–2 Hz means the joint experiences multiple load transients and command reversals per second, whose frequency components are much higher than the step frequency itself. When position loop bandwidth is only a few Hz, the joint is "still chasing the previous command" at the moment of stance phase switching, resulting in soft legs and wobbling. Recommended bandwidth for main leg joints ≥ 10 Hz order of magnitude (engineering recommended value, check against your gait frequency).

【Why】Step response looks at time domain, sweep looks at frequency domain — they are two photos of the same system; sweep quantifies "response capability" into a comparable hard metric, upgrading the corresponding column in the M01 specification table to measured values.

【How to analyze your situation】Three steps for insufficient bandwidth: increase position loop gain (constrained by overshoot) → acceleration/velocity feedforward → check mechanical backlash and encoder resolution (nonlinearities inherently limit bandwidth, tuning cannot solve). High reduction ratio servo solutions are naturally limited in this aspect — determined by topology, record honestly and note "not for dynamic walking" in the specification table.

## Step 4: Backdrivability and Force Transparency (Mandatory for QDD/Direct Drive)

【What to do】[Quasi-Direct Drive (QDD)](/entry/ent_technology_quasi_direct_drive_actuator_2024/) and direct drive solutions add three tests; high reduction ratio solutions (servo/harmonic) directly record "Fail — determined by topology", no need to test.

1. **Power-off Backdrivability**: With power off, manually rotate the output shaft; should be smooth without jamming or obvious cogging.
2. **Zero Stiffness Drag**: Power on, set zero stiffness (position gain = 0, small damping); should be able to "zero-gravity" drag the output shaft — this is a degenerate form of [Impedance Control](/entry/ent_method_impedance_control/) and a prerequisite for subsequent force control.
3. **Current-Torque Calibration (Measure Kt)**: Hang a known weight and hold stationary, record steady-state phase current, inversely calculate the measured torque constant:

   ```
   Kt_output = τ ÷ I = (m × g × L) ÷ I
   Example: m = 1.63 kg, L = 0.5 m → τ = 1.63 × 9.81 × 0.5 ≈ 8.0 N·m
   Measured steady-state phase current I = 5.2 A
   Kt_output = 8.0 ÷ 5.2 ≈ 1.54 N·m/A
   ```

   Compare with theoretical value (motor Kt × reduction ratio × efficiency, M02 datasheet value); if deviation > 10%, investigate cause (engineering recommended value): current sampling calibration error, friction consuming torque, or inflated datasheet Kt.
4. **Dual Encoder Solution**: Synchronously record motor-side and output-side [Joint Encoder](/entry/ent_component_joint_encoder_2024/) readings; their difference = reducer deformation + backlash — ODRI uses this difference for proprioceptive force control (`data/roadmap/research/open-dynamic-robot-initiative.md`). No-load difference approximates backlash, load-induced difference increment approximates reducer stiffness deformation; both are recorded in the data package.

【Why】Force transparency is the raison d'être of QDD: the equation "current ≈ torque" holds, so subsequent impedance/force control does not require additional torque sensors. If Kt deviation is large but the datasheet value is used, the entire robot force control feedforward will be wrong.

【How to analyze your situation】Cannot rotate with power off: check reducer assembly too tight (go back to M05) or topology inherently non-backdrivable. Zero stiffness drag "jerky": mostly cogging torque + uncompensated friction; add a small amount of current feedforward compensation, record the compensation amount in the data package (directly reused in the full robot stage).

## Step 5: Temperature Rise and Durability – Time is the Revealer

【What to Do】

1.  **Temperature Rise**: Run continuously for 30 minutes under rated load (half-load weight tracking a 1 Hz sine wave, or equivalent based on your M01 duty cycle), and record the case temperature curve. Criterion: Case temperature < 60 °C (engineering recommended value; the insulation class limit must be confirmed with the motor supplier). Record the ambient test temperature as well; for retesting in summer, adjust based on the temperature rise difference.
2.  **Durability Sampling**: Berkeley used 60 hours of continuous operation to verify the reliability of 3D-printed cycloidal gears (`data/roadmap/research/berkeley-humanoid-lite.md`) – test your self-developed reducer at this magnitude: run the first unit for 60 h, and sample 10% of production units for 10–20 h (engineering recommended process). After running, disassemble and inspect tooth surface wear, re-measure backlash and no-load current, and compare with the first unit baseline.
3.  **Efficiency Rough Measurement**: Under constant speed and heavy load conditions, input electrical power vs. output mechanical power:

    ```
    η = (τ × ω) ÷ (V × I)
    Example: Output τ = 4 N·m, ω = 3 rad/s → Mechanical power 12 W
    Input 24 V × 1.0 A = 24 W
    η = 12 ÷ 24 ≈ 50%
    ```

    This is the total efficiency of the reducer + motor + driver, a reference value for magnitude, which needs to be verified against your system.

【Why】Passing the step response only shows "instantaneous capability"; temperature rise and durability show "sustained capability" – walking is a continuous condition lasting minutes to hours. Insufficient thermal margin means overheating and derating after a few steps. Efficiency directly determines the M09 battery selection and range estimation. Background on thermal design can be found in [Chapter 6: Computation, Power, and Thermal Management](/wiki/chapters/chapter-06/).

【How to Analyze Your Situation】No temperature sensor: Use an infrared thermometer to measure the case, and record the built-in temperature reading from the driver board simultaneously. If it cannot sustain 30 minutes: gradually reduce the continuous current limit to find the "current that can sustain 30 minutes", and back-calculate the actual usable continuous torque – this value is the rated value that should be written in the M01 specification table.

## Step 6: Data Write-Back and Release Decision

【What to Do】

1.  Fill the measured values back into the [M01 Specification Table](m01-scenario-to-specs.md) item by item: peak torque (measured Kt × current limit), bandwidth, backlash, continuous torque, efficiency – upgrade from "estimated version" to "measured version".
2.  Handle out-of-tolerance items one by one, choosing one of three paths: Insufficient performance → **Change motor** (back to M02); Response or torque mismatch → **Change reduction ratio** (back to M03); Specification itself set too high → **Change specification** (back to M01, must provide a written reason: "Why lowering the specification does not affect the mission statement").
3.  After all items meet the criteria, output a written conclusion "This joint module is ready for assembly", accompanied by a data package index (curve directory + parameter version + test bench photos + wiring diagram).

【Why】Write-back turns experience into assets: the measured distribution (Kt, backlash, temperature rise) of 22 joints is the first-hand data for parameterizing the actuator model in the full robot simulation (M10/M11) – using measured values in simulation reduces sim-to-real issues by half.

【How to Analyze Your Situation】Testing all 22 units individually is too laborious: fully test the first 3 units on all six items; for the rest, test the three key items (step response + temperature rise + Kt). Compare the data distribution with the first unit, and perform full testing on outliers (engineering recommended process, adjust based on your batch size). Standardize the data package naming convention once: `JointID_TestItem_Date_FirmwareVersion`.

## Acceptance Criteria

- [ ] Curves for all six tests (step/sine/sweep/back-drive & Kt/temperature rise/durability) are archived in original format, with complete test conditions.
- [ ] 30° step response with three load levels: rise time < 0.2 s, overshoot < 10%, steady-state error < 0.5° (or value defined in specification table).
- [ ] 1 Hz ±20° sine wave: amplitude attenuation < 10%, phase lag < 15°; measured value for −3 dB bandwidth is available.
- [ ] QDD/direct drive solution: smooth zero-stiffness back-driving, measured Kt deviation from theoretical value ≤ 10% or cause of deviation identified; dual encoder difference (backlash + deformation) quantified.
- [ ] Case temperature < 60 °C (or within supplier limit) after 30 min of rated load; reducer durability sampling completed with disassembly inspection records.
- [ ] M01 specification table upgraded to "measured version", all write-back differences have a disposition conclusion (change motor/change reduction ratio/change specification, including written reason).
- [ ] "Ready for assembly" conclusion documented in writing; test bench photos and wiring diagram archived.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Fixed-frequency oscillation on step response curve | Bench resonance misidentified as joint oscillation | Reinforce fixture/add mass to bench and retest; tap the bench to hear natural frequency |
| Bandwidth much lower than M06 no-load tuning value | Inertia of weight bar and weight ignored | Include ⅓·m_bar·L² + m_weight·L² in load inertia, re-tune |
| Two temperature rise results inconsistent | Ambient temperature/airflow not fixed | Fix ambient temperature and placement, record room temperature; adjust based on temperature rise difference |
| Passes no-load test, fails when installed on robot | Only tested no-load and declared pass | Three load levels are a hard requirement; failing full load = failing |
| Data cannot be reproduced for analysis | Only saved screenshots, not raw data | Save raw format (csv/log) along with firmware version and parameters |
| Measured Kt much lower than datasheet | Friction not compensated / misread power supply current as phase current | Confirm reading phase current; measure in forward and reverse directions and average to cancel friction |
| Backlash increases after durability test | Printed gear wear / bearing clearance increase | Disassemble and inspect tooth surface; compare with Berkeley 60 h magnitude to evaluate material/process change |

## Companion Reading

- Previous Task: [M06 · Firmware and Calibration](m06-firmware-calibration.md)
- Next Task: [M08 · Platform Selection and Procurement](m08-platform-selection.md)
- Theoretical Background: [Chapter 11: Assembly, Integration, and Testing](/wiki/chapters/chapter-11/), [Chapter 25: Robot Evaluation System](/wiki/chapters/chapter-25/), [Chapter 14: Robot Control Fundamentals](/wiki/chapters/chapter-14/), [Chapter 6: Computation, Power, and Thermal Management](/wiki/chapters/chapter-06/)
- [Stage 1 Overview](../stage-1-actuator.md) · [Stage 2 Overview](../stage-2-biped.md) · [Actuator Selection Playbook](../playbooks/actuator-selection.md)
