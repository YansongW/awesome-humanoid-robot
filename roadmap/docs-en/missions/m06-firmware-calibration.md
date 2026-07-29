# M06 · Firmware and Calibration: Making the Iron Lump Understand Commands for the First Time

**Global Position**: After M05 assembly is complete, before M07 bench testing. The input is an assembled but "unintelligent" joint module, and the output is a **communicable, calibrated, and three-loop-tuned joint module** — M07 puts it on the bench and uses data to decide whether it is worthy of being installed into the leg. This page expands [Stage 1 Overview](../stage-1-actuator.md) step 6 (Closed-Loop Control Staircase) to a hands-on level.

**Prerequisites**: M05 assembly acceptance passed (no jamming throughout, normal no-load current); driver board, motor, encoder, and wiring harness are all ready; the host computer tool matching the driver board is installed on the PC.

Theoretical background: [FOC (Field-Oriented Control)](/entry/ent_method_foc_motor_control/), [PID Control](/entry/ent_method_pid_control/), [Current-Velocity-Position Three-Loop Cascade](/entry/ent_principle_current_velocity_position_loops/) cards; textbooks see [Chapter 4 Actuators](/wiki/chapters/chapter-04/) and [Chapter 14 Fundamentals of Robot Control](/wiki/chapters/chapter-14/).

## Step 1: Firmware Flashing and Version Freezing

【What to do】The firmware is determined by the driver board selected in M04; match accordingly:

| Driver Board | Firmware Route | Notes |
|---|---|---|
| ST B-G431B-ESC1 | Berkeley Humanoid Lite Open Source FOC Firmware | Board $19; the real robot low-level code is in its repository's `berkeley_humanoid_lite_lowlevel` subdirectory (C language, independent of the training stack — `data/roadmap/research/berkeley-humanoid-lite.md`) |
| ODrive | ODrive Official Firmware + odrivetool | The Berkeley solution is also compatible with ODrive / moteus / VESC (research archive) |
| moteus | moteus Official Firmware + tview | Firmware and host computer versions must match |

Perform the three flashing tasks in order:

1. Install the toolchain (for ST series, use ST-Link + STM32CubeProgrammer or DFU mode; first confirm you can enter bootloader and read back chip information);
2. **Immediately record the firmware version/commit after flashing** — all 22 actuators in the whole robot (Berkeley configuration: 6512×10 units + 5010×12 units, research archive) must be flashed with the same version; mixing versions means communication protocols and default parameters will not match;
3. Back up the factory default parameters (dump a copy to disk) so you can revert with one click if tuning goes wrong.

【Why】Firmware is the "operating system" of the driver board: FOC commutation, three-loop computation, and CAN protocol stack are all inside. Version mixing is the most insidious pitfall in batch debugging — the symptom is "this batch of joints obeys, that batch doesn't," and it takes three days to discover the firmware differs by two commits.

【How to analyze for your case】Follow the Berkeley solution exactly: use the firmware version specified in its documentation; do not chase the latest commit on the main branch. For self-developed firmware: first solidify "can compile, can flash, can read back version number" into a script — you will thank yourself when mass-producing 22 units.

## Step 2: Motor Parameter Entry — One Wrong Number, Everything Fails

【What to do】Enter four core parameters for each unit one by one, filling in the parameter registration form (even motors of the same model have individual differences; register each unit):

| Parameter | Acquisition Method | Consequence of Wrong Entry |
|---|---|---|
| Number of Pole Pairs | Count magnets: pole pairs = number of magnet pieces ÷ 2; or check motor datasheet | Commutation disorder — humming, no rotation, or random jitter |
| Phase Resistance R | Datasheet value; or measure line resistance with milliohm meter/LCR meter ÷ 2 (star connection) | Current loop gain mismatch |
| Phase Inductance L | Datasheet value; or measure line inductance with LCR meter (1 kHz range) ÷ 2 | Current loop auto-tuning failure |
| KV Value | Datasheet value determined during M02 selection | Speed feedforward and maximum speed estimation completely wrong |

Calculation example (star connection conversion): Measured line-to-line resistance between any two phases is 0.20 Ω, then phase resistance = 0.20 ÷ 2 = 0.10 Ω; line inductance is similarly divided by 2.

【Why】These four numbers are the "ID information" of FOC: the number of pole pairs determines the conversion between electrical angle and mechanical angle (electrical angle = mechanical angle × pole pairs), R/L determines the physical magnitude of current loop gain, and KV determines the speed-voltage mapping. The driver board's auto-tuning essentially estimates these numbers — the estimated values must be cross-checked against the datasheet/measured values; a difference of an order of magnitude indicates a wiring or measurement problem.

【How to analyze for your case】Datasheets for drone [BLDC motors](/entry/ent_component_bldc_motor/) (e.g., the MAD M6C12 150KV used by Berkeley, $129, research archive) often lack R/L: a hundred-dollar LCR meter is worth buying; if not available, use the driver board's auto-tuned values, but mark "Source: auto-tuned, not re-measured" in the registration form. The Kt calibration in M07 will serve as a backup check.

## Step 3: Encoder Offset Calibration — Aligning Electrical Angle Zero with Mechanical Zero

【What to do】FOC needs to know the precise angle of the rotor's magnetic poles relative to the stator for commutation, but the zero position of the [joint encoder](/entry/ent_component_joint_encoder_2024/) is random upon installation. The principle of automatic calibration: the driver board injects a slowly rotating open-loop current vector; the rotor is "dragged" to follow by electromagnetic torque. When it aligns with the d-axis, the encoder reading is recorded — this is the offset. After calibration, it must be **saved to flash**, then power cycled and verified that the reading persists.

Verification criterion (engineering recommended value; check against your driver board manual): Perform 5 consecutive power-on recalibrations; offset drift < 5° electrical angle. Excessive drift indicates a problem with magnet or encoder installation — tuning cannot fix it; go back to M05 to check assembly.

【Why】A small offset error still allows the motor to rotate, but the output torque is approximately reduced by cos(offset error angle); the extra current all turns into heat. An error of 90° electrical angle means the motor produces no torque at all. If the offset drifts every time power is applied, it is like operating a different motor every day.

【How to analyze for your case】Troubleshooting sequence for calibration failure/erratic offset: Check if the raw encoder reading is clean (rotate the motor by hand and see if the reading monotonically increases) → coaxiality between magnet and chip → whether the calibration current is sufficient (if the rotor cannot be dragged, increase the calibration current, but do not exceed the rated phase current). Magnetic encoders are sensitive to installation coaxiality and electromagnetic interference from phase wires ([Chapter 5 Sensing and Perception Hardware](/wiki/chapters/chapter-05/)); keep encoder wiring away from high-current phase wires.

## Step 4: Three-Loop Tuning Staircase — From Inner to Outer, Tame Step by Step

【What to do】Strictly follow the order: Current Loop → Velocity Loop → Position Loop. Verify each level with a step response before proceeding to the next. Bandwidth should decrease by a factor of 5–10 (principle from the [Three-Loop Cascade](/entry/ent_principle_current_velocity_position_loops/) card): the inner loop must be much faster than the outer loop so that the outer loop can treat the inner loop as an "ideal actuator."

1. **Current Loop**: Estimate gain based on R/L, or directly use the driver board's auto-tuning. Pole placement estimation formula (common engineering starting point; check against your driver board manual):

   ```
   L = 0.05 mH = 0.00005 H, R = 0.10 Ω, target bandwidth fc = 500 Hz
   ωc = 2π × fc = 2π × 500 ≈ 3142 rad/s
   Kp_i = L × ωc = 0.00005 × 3142 ≈ 0.16
   Ki_i = R × ωc = 0.10 × 3142 ≈ 314
   ```

   Step verification: Apply a current step of 30–50% of rated value; observe rise time (ms level) and ringing — if ringing is excessive, reduce bandwidth.

2. **Velocity Loop**: Set bandwidth to 1/5–1/10 of the current loop (in the example above, 500 Hz → 50–100 Hz, engineering recommended value). Verify with a small velocity step of 20% of rated value; a typical symptom of excessive gain is motor squealing (high-frequency hum) — immediately reduce gain.
3. **Position Loop**: Reduce bandwidth by another factor of 5–10 (on the order of 10–20 Hz, engineering recommended value). Verify with a 30° step: overshoot < 10%, steady-state error < 0.5° (consistent with the criteria in [Stage 1 Overview](../stage-1-actuator.md); M07 will re-test under load). If overshoot is large, do not rush to reduce P — adding **velocity feedforward** is often more effective: when the position command changes, simultaneously feedforward a velocity command so that the error is canceled before it accumulates.

【Why】The physical meaning of the three-loop cascade: the current loop manages "how much force" (torque ∝ current), the velocity loop manages "how fast to rotate," and the position loop manages "where to stop." If the outer loop bandwidth exceeds the inner loop, it is like letting a nearsighted person command a microscope — oscillation is inevitable. This is the standard use of [PID control](/entry/ent_method_pid_control/) in a cascade structure; theory is in [Chapter 14 Fundamentals of Robot Control](/wiki/chapters/chapter-14/).

【How to analyze for your case】The driver board has a built-in current loop (Berkeley firmware, ODrive, moteus all have it): your main work is on the velocity loop and position loop. No oscilloscope: the host computer's waveform recording function (tview / odrivetool / custom logging) is sufficient; the sampling rate must be at least 10 times the bandwidth of the loop under test. For the servo route, the three loops are closed internally; this step degenerates to "read the manual and adjust registers."

## Step 5: Communication Networking and Parameter Archiving

【What to Do】

1. **CAN ID Allocation**: Power on each unit individually, change the default ID to the unique ID from the allocation table, and affix a label (joint name + ID). Only network after all changes are complete. Document the allocation table in a format such as "Left Hip Pitch = 0x01".
2. **Unified Baud Rate**: Use the same rate across the entire network. Reference value: Berkeley uses CAN 2.0 @ 1 Mbps, with one bus per limb, connected to the main controller via a USB-CAN adapter, with a maximum of 64 devices per bus (research archive).
3. **Transmission/Reception Test**: The host computer performs transmission/reception with all network joints at 250 Hz (matching Berkeley's actuator and IMU communication at 250 Hz, research archive). The test passes if there are no dropouts and no surge in error frames for 1 continuous hour (criteria same as [Stage 1 Overview](../stage-1-actuator.md)).
4. **Parameter Archiving**: Save the final parameters (motor parameters + offsets + three-loop gains + ID) for each joint to a file, with dual backups in a git repository and a spreadsheet.

Rough bus load calculation (engineering recommendation, recalculate based on your frame length): Extended frame full load is approximately 130 µs/frame. With 6 joints per bus (Berkeley uses approximately 5–6 joints per limb bus) and bidirectional transmission/reception at 250 Hz = 6 × 250 × 2 × 130 µs ≈ 39% occupancy, which is healthy. If 12 joints are all on one bus, occupancy approaches 80%, requiring bus separation.

【Why】The [CAN bus](/entry/ent_technology_can_bus_2024/) shares a single pair of wires among multiple nodes. When IDs conflict, two devices transmit the same frame simultaneously, causing error frames to snowball into a bus storm and paralyze the entire network—and the symptom is "random dropout," which is extremely difficult to locate. Parameter archiving is a lifeline for the M07 and whole-machine stages: with 22 joints, no one will remember the offset of joint #7 three months later.

【How to Analyze Your Situation】The first step in networking is always to measure the CANH-CANL resistance with power off: with 120 Ω terminators at both ends, it should be approximately 60 Ω—infinite means no terminator is connected, far below 60 Ω means too many are connected (same as the troubleshooting table in [Stage 1 Overview](../stage-1-actuator.md)). For communication protocol and middleware selection, see [Chapter 22 Software Middleware](/wiki/chapters/chapter-22/).

## Acceptance Criteria

- [ ] All joints have the same firmware version, with the version number/commit recorded, and factory default parameters backed up.
- [ ] Motor parameters (pole pairs/R/L/KV) are registered for each unit, with the source noted (datasheet/measured/self-tuning).
- [ ] Power-on auto-calibration passes, with offset drift < 5° electrical angle (or the value specified in the driver board manual) for 5 consecutive repeated calibrations, and the calibration result written to flash.
- [ ] Three-loop tuning is complete: no-load 30° step overshoot < 10%, steady-state error < 0.5°, with curves archived.
- [ ] CAN networking is complete: ID allocation table documented, 250 Hz transmission/reception for 1 continuous hour with no dropouts.
- [ ] All parameters are saved to disk with dual backups (git + spreadsheet), allowing one-click restoration to any joint.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Needs recalibration every time it powers on | Calibration result not written to flash | Execute save command after calibration, power cycle to verify |
| Bus storm and network-wide dropout after networking | ID conflict between two joints | Power on each unit individually to change ID, affix labels, then network |
| High-frequency motor whine, feels tingly | Velocity loop gain too high | Halve the velocity loop Kp; confirm its bandwidth ≤ 1/5 of current loop bandwidth |
| Offset drifts with each calibration | Loose magnets / eccentric encoder installation | Check magnet adhesion and coaxiality, return to M05 for assembly repair |
| Motor reverses, lacks torque, or hums without turning | Incorrect phase sequence / incorrect pole pair count | Perform open-loop low-current rotation test to confirm phase sequence; recount magnets |
| Current loop self-tuning fails | R/L values are absurd / phase wires are poorly connected | Re-measure with LCR meter; check three-phase wiring and solder joints |
| Low-speed crawling, jerky motion | Current loop bandwidth too low / insufficient encoder resolution | Increase current loop bandwidth; verify encoder bit count and installation coaxiality |

## Companion Reading

- Previous Task: [M05 · 3D Printing and Mechanical Assembly](m05-print-assembly.md)
- Next Task: [M07 · Bench Testing and Acceptance](m07-bench-acceptance.md)
- Theoretical Background: [Chapter 4 Actuators](/wiki/chapters/chapter-04/), [Chapter 5 Sensing and Perception Hardware](/wiki/chapters/chapter-05/), [Chapter 14 Fundamentals of Robot Control](/wiki/chapters/chapter-14/), [Chapter 22 Software Middleware](/wiki/chapters/chapter-22/)
- [Stage 1 Overview](../stage-1-actuator.md) · [Actuator Selection Playbook](../playbooks/actuator-selection.md)
