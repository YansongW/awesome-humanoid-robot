# M06 · Firmware and Calibration: Making the Iron Lump Understand Commands for the First Time

**Global Position**: After M05 assembly is complete, before M07 bench testing. The input is an assembled but "unintelligent" joint module, and the output is a **communicable, calibrated, and three-loop-tuned joint module** — M07 puts it on the bench and uses data to decide if it's worthy of being installed into a leg. This page expands [Stage 1 Overview](../stage-1-actuator.md) step 6 (Closed-Loop Control Ladder) to a hands-on level.

**Prerequisites**: M05 assembly acceptance passed (no jamming throughout, normal no-load current); driver board, motor, encoder, and wiring harness are all ready; the host computer tool matching the driver board is installed on the PC.

Theoretical background: [FOC (Field-Oriented Control)](/entry/ent_method_foc_motor_control/), [PID Control](/entry/ent_method_pid_control/), [Current-Velocity-Position Three-Loop Cascade](/entry/ent_principle_current_velocity_position_loops/) cards; textbooks see [Chapter 4 Actuators](/wiki/chapters/chapter-04/) and [Chapter 14 Fundamentals of Robot Control](/wiki/chapters/chapter-14/).

## Step 1: Firmware Flashing and Version Freezing

【What to Do】The firmware is determined by the driver board selected in M04; match accordingly:

| Driver Board | Firmware Route | Notes |
|---|---|---|
| ST B-G431B-ESC1 | Berkeley Humanoid Lite Open Source FOC Firmware | Board $19; the real robot's low-level code is in its repository's `berkeley_humanoid_lite_lowlevel` subdirectory (C language, independent of the training stack — [Berkeley Humanoid Lite GitHub](https://github.com/HybridRobotics/Berkeley-Humanoid-Lite)) |
| ODrive | ODrive Official Firmware + odrivetool | The Berkeley solution is also compatible with ODrive / moteus / VESC (research archive) |
| moteus | moteus Official Firmware + tview | Firmware and host computer versions must match |

Three things for flashing, do them in order:

1. Install the toolchain (ST series uses ST-Link + STM32CubeProgrammer or DFU mode; first confirm you can enter bootloader and read back chip information);
2. **Immediately record the firmware version number/commit** after flashing — all 22 actuators in the whole machine (Berkeley configuration: 6512×10 units + 5010×12 units, research archive) must be flashed with the same version; mixing versions = mismatched communication protocols and default parameters;
3. Back up the factory default parameters (dump one copy to disk) so you can revert with one click if tuning goes wrong.

【Why】Firmware is the "operating system" of the driver board: FOC commutation, three-loop calculation, and the CAN protocol stack are all inside it. Version mixing is the most insidious pitfall in batch debugging — the symptom is "this batch of joints obeys, that batch doesn't," and it takes three days to find out the firmware differs by two commits.

【How to Analyze Your Situation】Copy the Berkeley solution: use the firmware version specified in its documentation, don't chase the latest commit on the main branch. For self-developed firmware: first solidify "can compile, can flash, can read back version number" into a script; when mass-producing 22 units, you'll thank yourself.

## Step 2: Motor Parameter Entry — Fill One Number Wrong, Everything Fails

【What to Do】Enter four core parameters one by one for each unit, fill them into a parameter registration form (even motors of the same model have individual differences; register each one):

| Parameter | Acquisition Method | Consequence of Wrong Entry |
|---|---|---|
| Pole Pairs | Count magnets: pole pairs = number of magnet pieces ÷ 2; or check motor manual | Commutation chaos — humming, no rotation, or random jitter |
| Phase Resistance R | Manual value; or measure line resistance with milliohm meter/LCR meter ÷ 2 (star connection) | Current loop gain mismatch |
| Phase Inductance L | Manual value; or measure line inductance with LCR meter (1 kHz range) ÷ 2 | Current loop auto-tuning failure |
| KV Value | Manual value determined during M02 selection | All velocity feedforward and maximum speed estimates are wrong |

Calculation Example (Star Connection Conversion): Measured line-to-line resistance of any two phases is 0.20 Ω, then phase resistance = 0.20 ÷ 2 = 0.10 Ω; line inductance is similarly divided by 2.

【Why】These four numbers are the "ID information" for FOC: pole pairs determine the conversion between electrical angle and mechanical angle (electrical angle = mechanical angle × pole pairs), R/L determine the physical magnitude of the current loop gain, and KV determines the velocity-voltage mapping. The driver board's auto-tuning essentially estimates these numbers — the estimates must be checked against the manual/measured values; a difference of an order of magnitude indicates a wiring or measurement problem.

【How to Analyze Your Situation】Drone [Brushless DC Motor](/entry/ent_component_bldc_motor/) (e.g., the MAD M6C12 150KV used by Berkeley, $129, research archive) manuals often lack R/L: a hundred-dollar LCR meter is worth buying; if you don't have one, use the driver board's auto-tuned values, but mark "Source: auto-tuned, not re-measured" in the registration form. The Kt calibration in M07 will double-check for you.

## Step 3: Encoder Offset Calibration — Aligning Electrical Angle Zero with Mechanical Zero

【What to Do】FOC needs to know the precise angle of the rotor's magnetic poles relative to the stator for commutation, but the zero position of the [Joint Encoder](/entry/ent_component_joint_encoder_2024/) is random upon installation. The principle of auto-calibration: the driver board injects a slowly rotating open-loop current vector, the rotor is "dragged" to follow by electromagnetic torque, and when it aligns with the d-axis, the encoder reading is recorded — this is the offset. After calibration, you **must write to flash to save it**, then power cycle and verify the reading persists.

Verification Criterion (engineering recommended value, check against your driver board manual): Power cycle and recalibrate 5 consecutive times, offset drift < 5° electrical angle. Excessive drift indicates a problem with the magnet or encoder installation; parameter tuning can't fix it, go back to M05 to check assembly.

【Why】If the offset is slightly wrong, the motor will still turn, but the output torque is approximately discounted by cos(offset error angle), and the excess current all turns into heat; if it's wrong by 90° electrical angle, the motor produces no torque at all. If the offset drifts every time you power on, it's like driving a different motor every day.

【How to Analyze Your Situation】Troubleshooting order for calibration failure/erratic offset: Is the raw encoder reading clean (turn the motor by hand and see the reading increase monotonically) → Coaxiality between the magnet and the chip → Is the calibration current sufficient (if it can't drag the rotor, increase the calibration current, but be careful not to exceed the rated phase current). Magnetic encoders are sensitive to installation coaxiality and phase line electromagnetic interference ([Chapter 5 Sensing and Perception Hardware](/wiki/chapters/chapter-05/)); keep the encoder wiring harness away from high-current phase lines.

## Step 4: Three-Loop Tuning Ladder — From Inside Out, Tame Step by Step

【What to Do】Strictly follow the order **Current Loop → Velocity Loop → Position Loop** for tuning, and verify each level with a step response before moving to the next. Bandwidth should decrease by a factor of 5–10 ([Three-Loop Cascade](/entry/ent_principle_current_velocity_position_loops/) card principle): the inner loop must be much faster than the outer loop so the outer loop can treat the inner loop as an "ideal actuator."

1. **Current Loop**: Estimate gains based on R/L, or directly use the driver board's auto-tuning. Pole placement estimation formula (common engineering starting point, check against your driver board manual):

   ```
   L = 0.05 mH = 0.00005 H, R = 0.10 Ω, target bandwidth fc = 500 Hz
   ωc = 2π × fc = 2π × 500 ≈ 3142 rad/s
   Kp_i = L × ωc = 0.00005 × 3142 ≈ 0.16
   Ki_i = R × ωc = 0.10 × 3142 ≈ 314
   ```

   Step response verification: Apply a current step of 30–50% of the rated value, observe the rise time (ms level) and ringing — if there's a lot of ringing, reduce the bandwidth.

2. **Velocity Loop**: Set bandwidth to 1/5–1/10 of the current loop (in the example above, 500 Hz → 50–100 Hz, engineering recommended value). Verify with a small velocity step of 20% of the rated value; the typical symptom of excessive gain is motor screeching (high-frequency buzzing), immediately reduce the gain.
3. **Position Loop**: Reduce bandwidth by another factor of 5–10 (on the order of 10–20 Hz, engineering recommended value). Verify with a 30° step: overshoot < 10%, steady-state error < 0.5° (consistent with the criteria in [Stage 1 Overview](../stage-1-actuator.md); M07 will re-test under load). If overshoot is large, don't rush to lower P — adding **velocity feedforward** is often a more fundamental fix: when the position command changes, feedforward a velocity command simultaneously, so the error is canceled before it accumulates.

【Why】The physical meaning of the three-loop cascade: the current loop manages "how much force" (torque ∝ current), the velocity loop manages "how fast to spin," and the position loop manages "where to stop." If the outer loop's bandwidth exceeds the inner loop's, it's like letting a nearsighted person command a microscope — it will inevitably oscillate. This is the standard use of [PID Control](/entry/ent_method_pid_control/) in a cascade structure; theory is in [Chapter 14 Fundamentals of Robot Control](/wiki/chapters/chapter-14/).

【How to Analyze Your Situation】The driver board has a built-in current loop (Berkeley firmware, ODrive, moteus all have it): your main work is on the velocity loop and position loop. No oscilloscope: the host computer's waveform recording function (tview / odrivetool / custom logging) is sufficient; the sampling rate must be at least 10 times higher than the bandwidth of the loop being tested. For the servo route, the three loops are closed internally; this step degenerates to "read the manual and adjust registers."

## Step 5: Communication Networking and Parameter Archiving

【What to Do】

1. **CAN ID Allocation**: Power on each unit individually, change the default ID to a unique ID from the allocation table, and affix a label (joint name + ID). Only network after all changes are complete. Document the allocation table in a format such as "Left Hip Pitch = 0x01".
2. **Unified Baud Rate**: Use the same rate across the entire network. Reference value: Berkeley uses CAN 2.0 @ 1 Mbps, with one bus per limb, connected to the main controller via a USB-CAN adapter, with a maximum of 64 devices per bus (research archive).
3. **Transmission/Reception Test**: The host computer performs transmission/reception with all joints on the network at 250 Hz (matching Berkeley's actuator and IMU communication at 250 Hz, research archive). The test passes if there are no dropouts and no surge in error frames for 1 continuous hour (criteria same as [Stage 1 Overview](../stage-1-actuator.md)).
4. **Parameter Archiving**: Save the final parameters (motor parameters + offsets + three-loop gains + ID) for each joint to a file, with dual backups in a git repository and a spreadsheet.

Rough bus load calculation (engineering suggestion, recalculate based on your frame length): Extended frame full load is approximately 130 µs/frame. With 6 joints on one bus (Berkeley uses approximately 5–6 joints per limb bus) and bidirectional transmission/reception at 250 Hz = 6 × 250 × 2 × 130 µs ≈ 39% bus utilization, which is healthy. If 12 joints are all on one bus, utilization approaches 80%, requiring bus separation.

【Why】[CAN Bus](/entry/ent_technology_can_bus_2024/) Multiple nodes share a pair of wires. When IDs conflict, two devices transmit the same frame simultaneously, causing error frames to snowball into a bus storm and paralyze the entire network—and the symptom is "random dropout," which is extremely difficult to locate. Parameter archiving is a lifesaver for the M07 and whole-machine phases: with 22 joints, no one will remember the offset for joint #7 three months later.

【How to Analyze Your Situation】The first step in networking is always to measure the CANH-CANL resistance with power off: with two 120 Ω terminators, it should be approximately 60 Ω—infinite means no terminators are connected, far below 60 Ω means too many are connected (same as the troubleshooting table in [Stage 1 Overview](../stage-1-actuator.md)). For communication protocol and middleware selection, see [Chapter 22: Software Middleware](/wiki/chapters/chapter-22/).

## Acceptance Criteria

- [ ] All joints have the same firmware version, with the version number/commit recorded, and factory default parameters backed up.
- [ ] Motor parameters (pole pairs/R/L/KV) are registered for each motor individually, with the source noted (manual/measured/self-tuning).
- [ ] Power-on auto-calibration passes, with offset drift < 5° electrical angle (or the value specified in the driver board manual) for 5 consecutive repeated calibrations, and the calibration result has been written to flash.
- [ ] Three-loop tuning is complete: no-load 30° step response overshoot < 10%, steady-state error < 0.5°, with curves archived.
- [ ] CAN networking is complete: ID allocation table is documented, with 250 Hz transmission/reception for 1 continuous hour without dropout.
- [ ] All parameters are saved to disk with dual backups (git + spreadsheet), allowing one-click restoration to any joint.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Requires recalibration every time it powers on | Calibration result not written to flash | Execute save command after calibration, power cycle to verify |
| Bus storm and network-wide dropout after networking | ID conflict between two joints | Power on each unit individually to change ID, affix label, then network |
| High-frequency motor whine, feels tingly to the touch | Velocity loop gain too high | Halve the velocity loop Kp for testing; confirm its bandwidth ≤ 1/5 of the current loop |
| Offset drifts with every calibration | Loose magnets / Eccentric encoder mounting | Check magnet adhesion and coaxiality, return to M05 to fix assembly |
| Motor reverses, is weak, or hums without turning | Incorrect phase sequence / Incorrect pole pair count | Perform open-loop low-current rotation test to confirm phase sequence; recount magnets |
| Current loop self-tuning fails | R/L values entered are absurd / Phase wires are poorly connected | Re-measure with LCR meter; check three-phase wiring and solder joints |
| Low-speed crawling, jerky motion | Current loop bandwidth too low / Encoder resolution insufficient | Increase current loop bandwidth; verify encoder bit count and mounting coaxiality |

## Companion Reading

- Previous Task: [M05 · 3D Printing and Mechanical Assembly](m05-print-assembly.md)
- Next Task: [M07 · Bench Testing and Acceptance](m07-bench-acceptance.md)
- Theoretical Background: [Chapter 4: Actuators](/wiki/chapters/chapter-04/), [Chapter 5: Sensing and Perception Hardware](/wiki/chapters/chapter-05/), [Chapter 14: Fundamentals of Robot Control](/wiki/chapters/chapter-14/), [Chapter 22: Software Middleware](/wiki/chapters/chapter-22/)
- [Stage 1 Overview](../stage-1-actuator.md) · [Actuator Selection Playbook](../playbooks/actuator-selection.md)
