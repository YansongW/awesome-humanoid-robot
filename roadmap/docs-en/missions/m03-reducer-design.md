# M03 · Reducer Design and Calculation: Reduction Ratio Is Not a Guess

**Global Position**: The third task of Stage 1, following [M02 · Motor Calculation and Selection](m02-motor-sizing.md) with motor candidates and parameter tables, and preceding [M04 · Driver, Sensing, and Wiring](m04-driver-sensing-wiring.md). The output is the **reduction ratio + reducer topology scheme + structural parameters** (number of teeth / outer diameter / material) for each joint — structural parameters determine the processing files for M05, while the reduction ratio, backlash, and efficiency expected values are backfilled into the M01 indicator table.

**Prerequisites**: M02 completed (motor KV/Kt/mass known, bus voltage determined); M01 indicator table in hand, especially the three columns: **backlash upper limit, whether backdrivability/force control is required, cost upper limit**.

Theoretical background: [Harmonic Reducer](/entry/ent_component_harmonic_drive_reducer/), [Quasi-Direct Drive Actuator QDD](/entry/ent_technology_quasi_direct_drive_actuator_2024/) cards, [Chapter 4 Actuator](/wiki/chapters/chapter-04/), [Chapter 9 Key Subsystem Design](/wiki/chapters/chapter-09/), and [Chapter 3 Key Materials](/wiki/chapters/chapter-03/).

## Step 1: Reduction Ratio Double Inequality — Clamping the Range from Both Torque and Speed

【What to Do】The reduction ratio i is constrained from two directions simultaneously. Write the double inequality and take the intersection:

```
i ≥ τ_joint / (τ_motor × η)    ← Torque must be sufficient (calculate for peak and continuous separately, take the larger)
i ≤ n_motor_max / n_out        ← Speed must be sufficient
```

Transmission efficiency η magnitude (engineering empirical values, need to verify with specific models): Planetary gear ~0.9 per stage, cycloidal pinwheel ~0.7–0.85, harmonic ~0.7–0.9. Complete example using the 8.3 N·m joint from M01/M02 (motor side capability takes continuous 0.5 N·m / peak 1.5 N·m — **example assumed values, need to verify with the data sheet of your selected motor**; η takes the median of cycloidal 0.8; motor loaded speed upper limit takes 70% of no-load 3330 rpm ≈ 2330 rpm, engineering recommended value):

```
i_min(peak) = 8.3 / (1.5 × 0.8) ≈ 6.9
i_min(continuous) = 3.3 / (0.5 × 0.8) ≈ 8.3   ← RMS torque 3.3 N·m, see M02 Step 3
i_max       = 2330 / 30         ≈ 77
Intersection: 8.3 ≤ i ≤ 77 → take i = 9 (close to lower limit, ensure backdrivability and force transparency)
Verification: τ_motor,peak = 8.3/(9×0.8) ≈ 1.15 N·m < 1.5 ✓; n_motor = 30×9 = 270 ≪ 2330 ✓
```

The "preliminary selection of 9:1" in M02 now has a written basis — the two tasks close the loop here.

【Why】The reduction ratio is the exchange rate between torque and speed: if taken too small, the I = τ/Kt from M02 directly exceeds the limit, causing current explosion; if taken too large, the output speed is insufficient and reverse efficiency collapses (cannot be backdriven, see Step 4). The width of the intersection itself is a measure of motor capability — a good motor gives you a wide range, while an insufficient motor squeezes the range into an empty set.

【How to Analyze Your Situation】Intersection is empty: motor torque or speed is insufficient, go back to M02 to change the motor or modify the bus voltage, do not force it. When the intersection is very wide, which end to choose is determined by the M01 indicator table: for force control/backdrivability, take the lower limit (QDD approach, [QDD card](/entry/ent_technology_quasi_direct_drive_actuator_2024/)); for static holding accuracy and no sagging when power is off, take the larger value.

## Step 2: Topology Selection — Matching Five Transmission Types

【What to Do】Compare the three columns of the M01 indicator table — backlash upper limit, backdrivability requirement, cost upper limit — and select the topology from the table below (values not sourced are engineering empirical values; specific models need to be verified with data sheets):

| Topology | Single-Stage Reduction Ratio | Backlash | Efficiency | Backdrivable | Cost Magnitude | Remarks |
|---|---|---|---|---|---|---|
| Planetary Gear | 3–10:1 | Low-Medium | ≈0.9/stage | Good | Low-Medium | 3D printed planetary is mainstream for makers |
| Cycloidal Pinwheel | 10–100:1 | Low | 0.7–0.85 | Medium | Fully 3D printable, very low | Berkeley 6512/5010 uses this scheme (archive) |
| [Harmonic](/entry/ent_component_harmonic_drive_reducer/) | 50–100:1 | Near zero (CSF ≤ 1 arcmin, card) | 0.7–0.9 | Poor | High (requires quotation) | Preferred for precision joints, essentially non-backdrivable |
| Synchronous Belt | 2–6:1 | Near zero | High | Good | Low | Zero backlash, low noise, but takes space and has elasticity |
| Servo Gear Set | Hundreds:1 ([XL330](/entry/ent_component_dynamixel_xl330_m288_t/) is 288.4:1) | Large | Low-Medium | Poor | Low | Plug and play, no force control |

【Why】Topology determines the **physical upper limits** of backlash, efficiency, and backdrivability; machining accuracy can only approach but not exceed these limits: the zero backlash of harmonic comes from multi-tooth, no-clearance meshing of the flexspline ([Harmonic Reducer Card](/entry/ent_component_harmonic_reducer_2024/)), the large reduction ratio of cycloidal comes from differential tooth meshing, and the high reduction ratio of servo comes from stacking multiple stages of spur gears — backlash also stacks up stage by stage. Determine the topology first, then discuss parameters; the order cannot be reversed.

【How to Analyze Your Situation】RL walking legs (require backdrivability, force transparency, tight budget): cycloidal or planetary with low reduction ratio, i.e., the QDD route; precision arm/wrist (position accuracy priority): harmonic; desktop learning machine for quick prototyping: directly buy a servo, skip Steps 3–5; motor and joint with non-coaxial arrangement: synchronous belt transition.

## Step 3: 3D Printed Cycloidal Pinwheel — Reuse Verified Designs, Don't Draw the Profile Yourself

【What to Do】First understand the principle before acting: the cycloidal disc and pin teeth mesh with a **tooth difference of 1** — for each revolution of the eccentric shaft, the cycloidal disc only moves backward by one tooth, reduction ratio = number of cycloidal disc teeth (textbook example: 12 pin teeth, 11 cycloidal disc teeth → i = 11:1; this is only a principle demonstration, not actual parameters of any product). The rotation of the cycloidal disc is extracted as pure rotation through the output pin mechanism (pin hole-pin shaft). Five key parameters: **number of pin teeth, number of cycloidal disc teeth, eccentricity, pin diameter, tooth width**.

Then make the most important engineering decision of this step: **directly reuse the parametric cycloidal design open-sourced by Berkeley Humanoid Lite, do not draw the profile yourself** — all its structural parts can be manufactured with a common desktop FDM printer (PLA), CAD and print files are released via GitHub Releases, and the multi-tooth load-sharing characteristic of the cycloidal gear has been verified by 60-hour durability testing ([Berkeley Humanoid Lite GitHub](https://github.com/HybridRobotics/Berkeley-Humanoid-Lite)). Processing details such as printing tolerances, profile modification, and layout orientation are all left to M05.

【Why】The cycloidal profile is generated by parametric equations, with modification amounts on the order of 0.0x mm — a small error in self-drawing can lead to either backlash explosion or assembly jamming (the most common rework reason in M05). Reusing a verified design is equivalent to benefiting from the other party's iterated tolerance band and 60-hour durability data, which is a rare free lunch in self-developed mechanical parts.

【How to Analyze Your Situation】Replicating Berkeley 6512/5010: directly use the official print files, this step only requires reading comprehension. Modifying dimensions (e.g., higher torque): modify tooth width/outer diameter on its parametric model, do not draw the profile from scratch. Buying off-the-shelf metal reducers (planetary/harmonic): skip this step, focus effort on verifying the matching between the input shaft diameter and the M02 motor shaft.

## Step 4: Backlash, Stiffness, and Efficiency – The "Invisible Indicators" of a Reducer

【What to Do】Three indicators not written into the BOM but that determine control quality, with expected values set item by item:

1. **Backlash**: Three sources – tooth side clearance, bearing clearance, and fit clearance (shaft and hole). Backlash directly eats into position accuracy and creates a dead zone in force control. The remedy is **dual encoders**: one on the motor side and one on the output side. The output-side encoder can "see through" the reducer, measuring deformation and backlash – ODRI relies on dual encoders + a low reduction ratio to achieve proprioceptive force control ([ODRI Actuator Hardware Repository](https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware), also see the [Joint Encoder](/entry/ent_component_joint_encoder_2024/) card).
2. **Efficiency**: P_loss = P_out × (1−η)/η – when η = 0.8, for every 100 W output, 25 W turns into heat inside the reducer. Efficiency also eats into battery life: Berkeley's whole robot with a 6S 4000 mAh battery has about 30 minutes of endurance (archive), which includes this loss.
3. **Backdrivability** = High reverse transmission efficiency: Solutions with low reduction ratios and short transmission chains (planetary, cycloidal, synchronous belt) can have high reverse efficiency, allowing the output side to "feel" the motor current – the current loop acts as a torque sensor. This is the reason for [QDD](/entry/ent_technology_quasi_direct_drive_actuator_2024/). Harmonic drives and high-ratio servo actuators have low reverse efficiency, cannot be moved when powered off, and force can only be estimated.

【Why】Position-controlled robots can tolerate backlash (closed loop on the outside), but force-controlled robots cannot – backlash and low reverse efficiency break the "current ↔ torque" correspondence. The three expected values from this step (backlash angle, η, backdriving start torque) are filled back into the M01 indicator table, and the M07 bench acceptance test will measure against these.

【How to Analyze Your Situation】For RL force control: low reduction ratio + dual encoders (ODRI mode); if the budget is tight, use a low reduction ratio + single encoder, estimating torque via current (Berkeley mode, AS5600 encoder $3 – archive). High reduction ratio solutions with only a motor-side encoder will systematically overestimate their own accuracy; write this deviation into the notes during selection.

## Step 5: Strength and Life Verification – Calculate by Peak Torque, Not Rated Torque

【What to Do】Qualitative verification in four steps (doable even without FEA tools):

1. **Which tooth to check**: The tooth under the highest load on the meshing contact line, with force derived backward from the output. Example calculation: Output 8.3 N·m, cycloidal gear pitch circle radius taken as 25 mm (example geometry, modify according to your design):
```
F_tooth = τ_out / r_pitch = 8.3 / 0.025 ≈ 332 N
```
Given the multi-tooth load-sharing characteristic of cycloidal drives (explicitly noted in the Berkeley archive), estimate 3–4 teeth bearing the load simultaneously, so per tooth ≈ 80–110 N.
2. **Check two failure modes**: Tooth root bending (tooth breakage) and tooth surface contact (pitting/crushing). Qualitative judgment: A 330 N level load on printed PLA teeth, with Berkeley's 60-hour endurance test providing a "feasible" empirical anchor (archive); if your peak torque exceeds this, increase tooth width or change material.
3. **Material constraints** (material selection details left for M05, this page only sets constraints): PLA has the best rigidity but is brittle, PETG is tough but has significant creep, Nylon is wear-resistant and impact-resistant but difficult to print – for the first prototype, start with "proven PLA + 2x safety margin on peak torque" (engineering recommendation).
4. **Bearings and failure criteria**: Deep groove ball bearings handle radial forces, **installed in pairs** to withstand overturning moments (engineering experience). Three scrap criteria – tooth surface pitting, tooth breakage, wear causing backlash to exceed the M01 upper limit.

【Why】Only verifying by rated torque and not peak torque is equivalent to pre-ordering tooth breakage: the instantaneous impact of a walking landing is a peak torque condition. The interlayer strength of printed parts is the weak point; try to orient the load within the layer along the tooth width direction – this determines the layout direction for M05, this page only writes the constraints.

【How to Analyze Your Situation】Torque level comparable to Berkeley 6512: directly inherit its tooth width/material/parameter combination, with durability anchored by the 60-hour test. Exceeding that level: first set a destructive sampling test plan (print 3–5 gear samples and load to failure, executed in M05/M07) before discussing assembly. For the metal reducer route: this step degenerates into checking the peak/instantaneous torque rating limits in the data sheet (see the reading discipline in the [Actuator Selection Manual](../playbooks/actuator-selection.md)).

## Acceptance Criteria

- [ ] Each joint's reduction ratio has a dual inequality calculation archived, closed-loop with the current/speed calculations from M02 (τ_motor, n_motor verification both passed).
- [ ] Topology selection has a written rationale, checked item by item against the backlash/backdrivability/cost columns of the M01 indicator table.
- [ ] The cycloidal solution provides a specific combination of tooth number parameters, or explicitly references the Berkeley open-source parametric design.
- [ ] Expected values for backlash, efficiency, and backdrivability are written into the M01 indicator table (mark "needs self-confirmation" if no data).
- [ ] Strength verification completed: maximum tooth force calculation + material selection + peak condition explanation.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Output speed never reaches the target | Reduction ratio too large, dual inequality only half done | Go back to Step 1 and add the i ≤ n_motor_max/n_out calculation |
| Joint cannot be moved when powered off, force control inaccurate | High reduction ratio reverse efficiency collapse | Determined by topology, cannot be fixed by tuning; for force control, go back to Step 2 and switch to a low-ratio solution |
| Cycloidal gear cannot fit into the pin ring or rotates stuck | Profile parameters / printing tolerance error | Stop and reuse Berkeley's parametric file; leave tolerance troubleshooting for M05 |
| Backlash significantly increases after tens of hours of running | Tooth surface wear/pitting, insufficient material or lubrication | Disassemble and inspect tooth surface; determine scrap per Step 5 criteria; evaluate material change |
| Tooth breakage after impact condition | Only verified by rated torque, not peak | Go back to Step 5 and recalculate with peak torque; increase tooth width or change topology |
| Current-torque calibration relationship is scattered | Large backlash + nonlinear transmission friction | Use dual encoders to measure the true output side angle; leave current calibration for M04 |

## Companion Reading

- Previous task: [M02 · Motor Calculation and Selection](m02-motor-sizing.md)
- Next task: [M04 · Driver, Sensing, and Wiring](m04-driver-sensing-wiring.md)
- Theoretical background: [Chapter 4 Actuator](/wiki/chapters/chapter-04/), [Chapter 9 Key Subsystem Design](/wiki/chapters/chapter-09/), [Chapter 3 Key Materials](/wiki/chapters/chapter-03/)
- [Actuator Selection Manual](../playbooks/actuator-selection.md) · [Stage 1 Overview](../stage-1-actuator.md)
