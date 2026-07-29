# M02 · Motor Calculation and Selection: From Specification Table to Specific Model

**Global Position**: The second task of Stage 1, following [M01 · Mathematical Modeling of Requirements](m01-scenario-to-specs.md) with its specification table, and preceding [M03 · Reducer Design and Calculation](m03-reducer-design.md). Input is the **peak torque / rated speed / mass budget / cost ceiling** four columns for each joint from the specification table; output is **1–2 candidate motor models + a key parameter table** (Kt, KV, number of pole pairs, phase resistance, rated/peak current, mass) for each joint — M03 uses this to calculate the reduction ratio, M04 uses it to select the driver board and wire gauge.

**Prerequisites**: The M01 specification table is finalized; ability to perform unit conversions and solve linear equations (if insufficient, review [Stage 0 Foundation Building](../stage-0-foundations.md)). This task can be done entirely by hand calculation or spreadsheet; no simulation software is required.

Theoretical background: [Brushless DC Motor](/entry/ent_component_bldc_motor/), [Frameless Torque Motor](/entry/ent_component_frameless_torque_motor_2024/), [High-Performance Servo Motor](/entry/ent_comp_servo_motor/) cards, [Chapter 4 Actuators](/wiki/chapters/chapter-04/) and [Chapter 6 Calculation, Power, and Thermal Management](/wiki/chapters/chapter-06/); the selection decision framework is in the [Actuator Selection Handbook](../playbooks/actuator-selection.md).

## Step 1: Translate the Specification Table into Motor Language Using Three Motor Constants

【What to Do】Start the selection with three constants: **Kt** (torque constant, N·m/A — how much torque per ampere of current), **KV** (speed constant, rpm/V — how fast the motor spins unloaded per volt), **number of pole pairs** (affects commutation and low-speed characteristics). Datasheets often only provide KV; Kt is converted using energy conservation (they are reciprocals in SI units):

```
Kt (N·m/A) ≈ 60 / (2π × KV (rpm/V))
```

Then, from the joint peak torque in M01, derive the motor-side phase current: `τ_motor = τ_joint ÷ i ÷ η` (i is the preselected reduction ratio, η is transmission efficiency), `I = τ_motor ÷ Kt`.

Complete example (using the 8.3 N·m joint from M01, preselected i = 9, η = 0.8; candidate motor is the Berkeley 6512 equivalent MAD M6C12 150KV — the model name indicates the KV value, $129, source `data/roadmap/research/berkeley-humanoid-lite.md`):

```
Kt      = 60 / (2π × 150) ≈ 0.064 N·m/A
τ_motor = 8.3 / (9 × 0.8) ≈ 1.15 N·m
I_peak  = 1.15 / 0.064    ≈ 18 A    ← Peak phase current, used by M04 for driver board selection
```

【Why】Kt and KV are two sides of the same electromagnetic design: more winding turns → higher Kt, lower KV. All torque requirements are ultimately converted to current, and **current is the common source of heat generation, driver board current limiting, and wire gauge selection**. Hobbyist motors are accustomed to only specifying KV without Kt; without conversion, they cannot be compared horizontally with industrial motors.

【How to Analyze Your Situation】Manufacturers give Kt in various units (N·m/A, g·cm/A, oz·in/A); always convert to N·m/A for comparison — 1 N·m/A ≈ 10,197 g·cm/A; a unit error by an order of magnitude invalidates all subsequent calculations. Motors whose datasheets do not provide KV/Kt are directly excluded: without these two numbers, they cannot enter any engineering calculation.

## Step 2: KV and Bus Voltage — Is the Speed Sufficient, Can the Current Be Handled

【What to Do】Perform KV checks in two directions to bracket the candidate motor within a range:

1. **KV Lower Limit (Speed Side)**: Motor required speed = M01 output speed × i; no-load speed ≈ KV × V. Check using `KV × V_min × 0.7 ≥ n_motor` (0.7 is an engineering recommended value for the speed drop factor under load).
2. **KV Upper Limit (Current Side)**: Higher KV means lower Kt, requiring more current for the same torque. Derive from the current budget: `Kt_min = τ_motor ÷ I_budget`, then convert `KV_max = 60 / (2π × Kt_min)`. I_budget takes the smaller of the driver board current limit and the thermal calculation (here set to 20 A as an example assumption; M04 will verify with the actual driver board).

Example continuing from Step 1 (bus 6S LiPo: nominal 22.2 V, about 20 V at end of discharge):

```
n_motor = 30 rpm × 9 = 270 rpm
KV lower limit = 270 / (20 × 0.7) ≈ 19 rpm/V
Kt_min  = 1.15 / 20        ≈ 0.058 N·m/A → KV upper limit ≈ 60 / (2π × 0.058) ≈ 165 rpm/V
Candidate 150 KV ∈ [19, 165] ✓; no-load speed 150 × 22.2 = 3330 rpm ≫ 270 rpm
```

Then determine the bus voltage level: LiPo is categorized by series count as 3S (11.1 V) / 6S (22.2 V) / 12S (44.4 V). The Berkeley Humanoid Lite uses 6S 4000 mAh LiPo for the entire robot, with a runtime of about 30 minutes (`data/roadmap/research/berkeley-humanoid-lite.md`) — the 22 V level is the sweet spot for desktop humanoids: at the same power, current is half that of 3S, reducing line loss and heat generation, while not imposing the higher voltage withstand and safety requirements of 12S on the driver board.

【Why】The KV lower limit ensures "it can reach the speed," and the KV upper limit ensures "it won't burn out" — the essence of the upper limit is the Kt lower limit, and current is a hard constraint: hitting the driver board current limit causes torque loss, and exceeding the thermal limit burns the windings. The voltage level simultaneously determines the speed ceiling and the overall current level, making it an implicit independent variable in motor selection.

【How to Analyze Your Situation】If the KV lower limit is not met: increase voltage, switch to a higher KV motor, or reduce the reduction ratio (interacting with M03). If the KV upper limit is not met (common for high-torque joints): switch to a lower KV motor or increase the reduction ratio. Don't be complacent if the margin exceeds 5 times — unused speed is obtained at the cost of current; return to M03 to rebalance.

## Step 3: Power and Heat — Continuous Rating Depends on RMS, Not Peak

【What to Do】Convert the duty cycle from M01 into RMS (root mean square) torque, then calculate the RMS current and copper loss heat generation. Copper loss I²R is the main heat source of the motor; **continuous output capability is determined by RMS current, while peak torque can only be sustained for seconds**. Example continuing (RMS/peak ratio taken as 0.4, an engineering recommended value for a 50% duty cycle; phase resistance R taken as 0.1 Ω is only an example magnitude; check the datasheet or confirm with the supplier):

```
τ_rms     = 0.4 × 8.3               ≈ 3.3 N·m
I_rms     = 3.3 / (9 × 0.8 × 0.064) ≈ 7.2 A
P_cu,rms  = 7.2² × 0.1              ≈ 5.2 W   ← Continuous heat generation
P_cu,peak = 18²  × 0.1              ≈ 32 W    ← Only allowed for seconds
P_mech    = 8.3 N·m × 3.14 rad/s    ≈ 26 W    ← Peak mechanical power at output
```

Reference anchor: Maxon EC-i 40 rated torque 224 mN·m, stall torque 2080 mN·m, a difference of nearly 10 times ([Maxon](/entry/ent_company_maxon_group_2024/) card, cited from [Actuator Selection Handbook](../playbooks/actuator-selection.md)) — no matter how impressive the stall torque figure, selection for continuous operation must be based on the rated value.

【Why】Motor burnout is almost always a thermal failure: winding insulation has a temperature limit, and heat accumulates with I²R × time. The constraint for peak is the demagnetization current and the driver board current limit (seconds), while the constraint for continuous is heat dissipation (minutes); both must be calculated separately and with separate margins. System-level thermal design is covered in [Chapter 6 Calculation, Power, and Thermal Management](/wiki/chapters/chapter-06/).

【How to Analyze Your Situation】If the RMS/peak ratio is uncertain, estimate it as 0.4; the M07 bench temperature rise test will verify the actual value. The "rated current" in the datasheet usually corresponds to room temperature + free air + a metal mounting surface; derating is required for enclosure with 3D-printed parts and summer ambient conditions — for rated values without specified cooling conditions, confirm with the supplier yourself.

## Step 4: Topology and Form Factor – Why Joint Motors Are Made into "Pancakes"

[What to Do] First understand the physics behind the form factor, then choose among the three types. The electromagnetic root of torque is given by the [Frameless Torque Motor](/entry/ent_component_frameless_torque_motor_2024/) card: τ = 2πr²l·B_gap·J_s – **Torque grows with the square of the air gap radius**, so joint motors are made into large-diameter, short-axial-length outer-rotor "pancakes". The number of pole pairs is the second lever: more pole pairs → higher electrical frequency at the same mechanical speed, lower KV, higher Kt, which perfectly suits the "low speed, high torque" appetite of joints; the cost is increased commutation frequency and iron losses, placing higher demands on the driver board (foreshadowing M04).

| Form Factor | Representative Model/Solution | Torque Density | Integration Level | Cost | Suitable For |
|---|---|---|---|---|---|
| Hobbyist Outer Rotor [BLDC](/entry/ent_component_bldc_motor/) | MAD M6C12 150KV, $129 (Berkeley Archive) | High | Low (gearing/driver/encoder all self-sourced) | Low | Self-developed QDD, tight budget |
| [Frameless Torque Motor](/entry/ent_component_frameless_torque_motor_2024/) | ODRI uses off-the-shelf frameless motors (odri archive) | Highest | Medium (embedded into joint structure) | Need to confirm with supplier directly | Has machining capabilities |
| Integrated [Servo](/entry/ent_comp_servo_motor/)/Smart Actuator | [XM430-W210-T](/entry/ent_component_dynamixel_xm430_w210_t/) Stall torque 3.0 N·m | Low-Medium | Highest (plug-and-play) | Need to inquire price by model | Zero experience, get running first |

[Why] The outer rotor pushes the air gap radius to the structural limit, a direct realization of τ ∝ r²l; frameless motors go a step further, eliminating the housing and output shaft to "knead" the motor into the joint – the ODRI BLMC actuator follows this path (off-the-shelf frameless motor + self-developed driver board, `data/roadmap/research/open-dynamic-robot-initiative.md`). Integrated solutions trade torque density for peace of mind, sealing gearing, driver, and feedback all in one housing.

[How to Analyze Your Situation] Match by budget: Single joint < ¥400 → Servo (XM430 class); Around ¥1,000 → Hobbyist BLDC + 3D-printed reducer (Berkeley 6512 already used a $129 motor + printed cycloidal drive for RL walking, archive); Pursuing performance with machining capabilities → Frameless motor, but note the ODRI route has a beginner-friendliness rating of only 2/5 (odri archive), proceed with caution.

## Step 5: Candidate Convergence and Pre-Order Checklist

[What to Do] Converge each joint to 1–2 candidates, fill out the **Motor Parameter Verification Checklist** item by item before ordering. Use the Berkeley 6512 joint (MAD M6C12 150KV) as an example to demonstrate the filling method:

| Parameter | Value in This Example | Source / Status |
|---|---|---|
| Model / Price | MAD M6C12 150KV, $129 | berkeley-humanoid-lite research archive |
| KV | 150 rpm/V | Model specification |
| Kt | ≈ 0.064 N·m/A | Conversion formula from Step 1 |
| Peak Phase Current Requirement | ≈ 18 A | Calculation from Step 1 (this example joint) |
| No-load Speed @22.2 V | 3330 rpm | Calculation from Step 2 |
| Number of Pole Pairs | — | Not found in datasheet, need to confirm with supplier directly |
| Phase Resistance | — | Same as above (0.1 Ω in Step 3 is just an example magnitude) |
| Continuous Current | — | Same as above |
| Mass | — | Same as above (backfill into M01 mass budget column) |
| Shaft Diameter / Mounting Holes | — | Same as above (verify against M03 reducer input interface) |

Alternative route: If you don't want to source individual components yourself, refer to ODRI's approach of purchasing off-the-shelf frameless motors + self-developed driver board (fully BSD open-source for mechanics and electronics, odri archive); to get running fastest, use an integrated servo, where this task degenerates into "look up the table by torque requirement".

[Why] The pitfalls before ordering are concentrated in the last five rows of the checklist: wrong pole pair count, FOC commutation fails directly; missing phase resistance, the thermal calculation in Step 3 becomes a castle in the air; wrong shaft diameter/hole positions, the motor won't fit the reducer upon arrival. Any unfilled items must be marked "Need to confirm with supplier directly", and guessing numbers from product photos is forbidden.

[How to Analyze Your Situation] Replicating Berkeley 6512/5010: Verify the checklist item by item against the official BOM and 3D-print files; the design has already been validated by a full robot with 22 actuators (archive). Self-developed hybrid: Fill out the checklist for all three candidates before comparing. Compare not by unit price, but by "how much Kt × current capability per gram within the mass budget".

## Acceptance Criteria

- [ ] Each joint has ≥ 1 candidate motor model, with the selection rationale documented (corresponding to the four columns of indicators in M01).
- [ ] Five calculations archived per joint: Kt conversion, peak phase current, KV upper/lower limit check, RMS current, copper loss heating.
- [ ] Bus voltage level determined, KV range check passed, with written explanation for any margin.
- [ ] Motor parameter verification checklist filled item by item or marked "Need to confirm with supplier directly".
- [ ] Peak/RMS phase currents fully recorded, clearly handed over to M04 for driver board current limit verification.
- [ ] Motor mass backfilled into M01 indicator table, overall robot mass budget not exceeded.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Motor runs fine unloaded, overheats under load | High KV with low reduction ratio: Kt too small, torque全靠 current brute force | Go back to Step 1, recalculate I = τ/Kt; switch to lower KV motor or increase reduction ratio (link with M03) |
| Motor bought for "max torque" gets hot in minutes | Confused stall torque with continuous torque | Check datasheet rated (continuous) torque, reselect based on RMS requirement (Maxon example in Step 3) |
| Two candidates have "Kt" values differing by tens of times, can't judge | Unit confusion (N·m/A vs g·cm/A, difference of ~10,197 times) | Convert all to SI units before comparing; if only KV is given, use Step 1 formula for conversion |
| FOC auto-tuning fails, motor hums but doesn't spin | Wrong pole pair count / phase resistance not measured | Complete the two items in the checklist; leave parameter identification for M04 |
| Peak current requirement exceeds driver board current limit | Selection only considered motor, not driver | Compare I_peak from Step 1 against candidate driver board current limit; if exceeded, change motor or lower specifications |
| Motor doesn't fit reducer upon arrival | Shaft diameter / mounting holes not verified | Verify last two rows of checklist before ordering; cross-check against M03 input interface drawing |

## Companion Reading

- Previous Task: [M01 · Mathematical Modeling of Requirements and Scenarios](m01-scenario-to-specs.md)
- Next Task: [M03 · Reducer Design and Calculation](m03-reducer-design.md)
- Theoretical Background: [Chapter 4 Actuators](/wiki/chapters/chapter-04/), [Chapter 6 Calculation, Power, and Thermal Management](/wiki/chapters/chapter-06/)
- [Actuator Selection Playbook](../playbooks/actuator-selection.md) · [Stage 1 Overview](../stage-1-actuator.md)
