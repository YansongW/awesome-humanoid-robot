# M03 · Reducer Design and Calculation: Reduction Ratio Is Not a Guess

**Global Position**: The third task of Stage 1, following [M02 · Motor Calculation and Selection](m02-motor-sizing.md) for motor candidates and parameter tables, and preceding [M04 · Driver, Sensing, and Wiring](m04-driver-sensing-wiring.md). The output is the **reduction ratio + reducer topology scheme + structural parameters** (number of teeth / outer diameter / material) for each joint—structural parameters determine the machining files for M05, while the reduction ratio, backlash, and expected efficiency values are backfilled into the M01 specification table.

**Prerequisites**: M02 completed (motor KV/Kt/mass known, bus voltage determined); M01 specification table in hand, especially the **backlash upper limit, whether back-drivability/force control is required, and cost upper limit** columns.

Theoretical background: [Harmonic Drive Reducer](/entry/ent_component_harmonic_drive_reducer/), [Quasi-Direct Drive Actuator QDD](/entry/ent_technology_quasi_direct_drive_actuator_2024/) cards, [Chapter 4 Actuator](/wiki/chapters/chapter-04/), [Chapter 9 Key Subsystem Design](/wiki/chapters/chapter-09/), and [Chapter 3 Key Materials](/wiki/chapters/chapter-03/).

## Step 1: Reduction Ratio Double Inequality—Clamping the Range from Both Torque and Speed

【What to Do】The reduction ratio i is constrained from two directions simultaneously. Write the double inequality and take the intersection:

```
i ≥ τ_joint / (τ_motor × η)    ← Torque must be sufficient (calculate for peak and continuous separately, take the larger value)
i ≤ n_motor_max / n_out        ← Speed must be sufficient
```

Transmission efficiency η magnitude (engineering empirical values, subject to verification per specific model): Planetary gear ~0.9 per stage, cycloidal pinwheel ~0.7–0.85, harmonic ~0.7–0.9. Full calculation example using the 8.3 N·m joint from M01/M02 (motor-side capability: continuous 0.5 N·m / peak 1.5 N·m—**example assumed values, subject to verification per your selected motor's datasheet**; η taken as the median for cycloidal, 0.8; motor loaded speed upper limit taken as 70% of no-load 3330 rpm ≈ 2330 rpm, engineering recommended value):

```
i_min(peak) = 8.3 / (1.5 × 0.8) ≈ 6.9
i_min(continuous) = 3.3 / (0.5 × 0.8) ≈ 8.3   ← RMS torque 3.3 N·m, see M02 Step 3
i_max       = 2330 / 30         ≈ 77
Intersection: 8.3 ≤ i ≤ 77 → take i = 9 (close to lower limit, preserving back-drivability and force transparency)
Verification: τ_motor,peak = 8.3/(9×0.8) ≈ 1.15 N·m < 1.5 ✓; n_motor = 30×9 = 270 ≪ 2330 ✓
```

In M02, the "preliminary selection of 9:1" now has a documented basis—the two tasks close the loop here.

【Why】The reduction ratio is the exchange rate between torque and speed: if taken too small, M02's I = τ/Kt directly exceeds the limit, causing current explosion; if taken too large, output speed is insufficient and reverse efficiency collapses (non-back-drivable, see Step 4). The width of the intersection itself is a measure of motor capability—a good motor gives you a wide range, while an inadequate motor squeezes the intersection into an empty set.

【How to Analyze Your Situation】Intersection is empty: motor torque or speed is insufficient; return to M02 to change the motor or adjust the bus voltage; do not force it. When the intersection is very wide, the choice of which end to select is determined by the M01 specification table: for force control/back-drivability, choose the lower limit (QDD approach, [QDD card](/entry/ent_technology_quasi_direct_drive_actuator_2024/)); for static holding precision and no collapse upon power loss, choose the higher value.

## Step 2: Topology Selection—Match Five Transmission Types to Your Needs

【What to Do】Compare the backlash upper limit, back-drivability requirement, and cost upper limit columns from the M01 specification table, and select the topology from the table below (values without specified sources are engineering empirical values; specific models must be verified per datasheet):

| Topology | Single-Stage Reduction Ratio | Backlash | Efficiency | Back-Drivable | Cost Level | Notes |
|---|---|---|---|---|---|---|
| Planetary Gear | 3–10:1 | Low-Medium | ≈0.9/stage | Good | Low-Medium | 3D printed planetary is mainstream for makers |
| Cycloidal Pinwheel | 10–100:1 | Low | 0.7–0.85 | Medium | Fully 3D printable, very low | Berkeley 6512/5010 uses this scheme (archive) |
| [Harmonic](/entry/ent_component_harmonic_drive_reducer/) | 50–100:1 | Near zero (CSF ≤ 1 arcmin, card) | 0.7–0.9 | Poor | High (requires quotation) | Preferred for precision joints, essentially non-back-drivable |
| Synchronous Belt | 2–6:1 | Near zero | High | Good | Low | Zero backlash, low noise, but occupies space and has elasticity |
| Servo Gear Set | Hundreds:1 ([XL330](/entry/ent_component_dynamixel_xl330_m288_t/) is 288.4:1) | Large | Low-Medium | Poor | Low | Plug-and-play, unsuitable for force control |

【Why】Topology determines the **physical upper limits** of backlash, efficiency, and back-drivability; machining precision can only approach but not exceed these limits: the zero backlash of harmonic drives comes from the multi-tooth, backlash-free meshing of the flexspline ([Harmonic Drive Reducer card](/entry/ent_component_harmonic_reducer_2024/)), the large reduction ratio of cycloidal drives comes from differential tooth meshing, and the high reduction ratio of servo gears is built up by stacking multiple stages of spur gears—backlash also accumulates stage by stage. Determine the topology first, then discuss parameters; the order cannot be reversed.

【How to Analyze Your Situation】RL walking legs (require back-drivability, force transparency, tight budget): cycloidal or planetary with low reduction ratio, i.e., the QDD route; precision arms/wrists (position accuracy priority): harmonic; desktop learning machine for rapid prototyping: directly buy a servo, skip Steps 3–5; motor and joint with non-coaxial arrangement: synchronous belt transition.

## Step 3: 3D Printed Cycloidal Pinwheel—Reuse Verified Designs, Don't Draw the Profile Yourself

【What to Do】First understand the principle: the cycloidal disc and the pin teeth mesh with a **tooth count difference of 1**—for each revolution of the eccentric shaft, the cycloidal disc only moves backward by one tooth, and the reduction ratio = number of teeth on the cycloidal disc (textbook example: 12 pin teeth, 11 cycloidal disc teeth → i = 11:1; this is only a principle demonstration, not the actual parameters of any product). The rotation of the cycloidal disc is extracted as pure rotation through the output pin mechanism (pin hole-pin shaft). Five key parameters: **number of pin teeth, number of cycloidal disc teeth, eccentricity, pin diameter, tooth width**.

Then make the most important engineering decision of this step: **directly reuse the parametric cycloidal design open-sourced by Berkeley Humanoid Lite, do not draw the profile yourself**—all its structural parts can be manufactured with a common desktop FDM printer (PLA), CAD and print files are released via GitHub Releases, and the multi-tooth load-sharing characteristic of the cycloidal gear has been verified by 60-hour endurance testing (`data/roadmap/research/berkeley-humanoid-lite.md`). Machining details such as print tolerances, profile modification, and layout direction are uniformly left for M05.

【Why】The cycloidal profile is generated by parametric equations, with modification amounts on the order of 0.0x mm—a slight error in self-drawing can lead to either explosive backlash or assembly jamming (the most common rework cause in M05). Reusing a verified design is equivalent to freeloading on the tolerance band and 60-hour endurance data that the other party has iterated over, which is a rare free lunch in self-developed mechanical parts.

【How to Analyze Your Situation】Replicating Berkeley 6512/5010: directly use the official print files; this step only requires reading comprehension. Modifying dimensions (e.g., for higher torque): modify the tooth width/outer diameter on its parametric model, do not draw the profile from scratch. Buying a ready-made metal reducer (planetary/harmonic): skip this step and focus effort on verifying the matching of the input shaft diameter with the M02 motor shaft.

## Step 4: Backlash, Stiffness, and Efficiency—The "Invisible Indicators" of the Reducer

【What to Do】Three indicators that are not written into the BOM but determine control quality; set expected values for each:

1. **Backlash**: Three sources—tooth clearance, bearing clearance, and fit clearance (shaft and hole). Backlash directly eats into position accuracy and creates a dead zone in force control. The remedy is **dual encoders**: one at the motor end and one at the output end; the output-end encoder can "see through" the reducer, measuring deformation and backlash—ODRI achieves intrinsic force control precisely through dual encoders + low reduction ratio (`data/roadmap/research/open-dynamic-robot-initiative.md`, also see the [Joint Encoder](/entry/ent_component_joint_encoder_2024/) card).
2. **Efficiency**: P_loss = P_out × (1−η)/η—when η = 0.8, for every 100 W output, 25 W becomes heat in the reducer. Efficiency also eats into battery life: the Berkeley whole robot's approximately 30-minute battery life (archive) with a 6S 4000 mAh battery includes this loss.
3. **Back-drivability** = high reverse transmission efficiency: schemes with low reduction ratios and short transmission chains (planetary, cycloidal, synchronous belt) can have reverse efficiency high enough that the output end can "feel" the motor current—the current loop acts as a torque sensor, which is the very reason for [QDD](/entry/ent_technology_quasi_direct_drive_actuator_2024/)'s existence. Harmonic drives and servo gears with high reduction ratios have low reverse efficiency, cannot be moved when power is off, and force can only be estimated.

【Why】Position-controlled robots can tolerate backlash (closed loop on the outside), but force-controlled robots cannot—backlash and low reverse efficiency shatter the "current ↔ torque" correspondence. The three expected values from this step (backlash angle, η, back-drive starting torque) are backfilled into the M01 specification table, and M07 bench acceptance testing will measure against these.

【How to Analyze Your Situation】Requiring RL force control: low reduction ratio + dual encoders (ODRI mode); tight budget: low reduction ratio + single encoder, estimate torque via current (Berkeley mode, AS5600 encoder $3—archive). High reduction ratio schemes with only a motor-end encoder will systematically overestimate their own accuracy; write this deviation into the notes during selection.

## Step 5: Strength and Life Verification – Calculate by Peak Torque, Not Rated Torque

[What to Do] Qualitative verification in four steps (can be done without FEA tools):

1. **Which tooth to verify**: The tooth under the greatest load on the meshing contact line, with force deduced backward from the output end. Example: Output 8.3 N·m, cycloidal gear pitch radius taken as 25 mm (example geometry, modify according to your design):
```
F_tooth = τ_out / r_pitch = 8.3 / 0.025 ≈ 332 N
```
Under the multi-tooth load-sharing characteristic of cycloidal drives (explicitly noted in the Berkeley archive), estimate simultaneous load-bearing by 3–4 teeth, giving approximately 80–110 N per tooth.
2. **Consider two failure modes**: Tooth root bending (tooth breakage) and tooth surface contact (pitting/crushing). Qualitative judgment: With a 330 N-level load acting on printed PLA teeth, Berkeley's 60-hour endurance test provides a "feasible" empirical anchor (archive); if your peak torque exceeds this, increase tooth width or change material.
3. **Material constraints** (material selection details reserved for M05; this page only defines constraints): PLA has the best rigidity but is brittle, PETG is tough but has significant creep, nylon is wear-resistant and impact-resistant but difficult to print – for the first prototype, start with "proven PLA + 2x safety margin on peak torque" (engineering recommendation).
4. **Bearings and failure criteria**: Deep groove ball bearings handle radial forces; **install in pairs** to withstand overturning moments (engineering experience). Three failure criteria – tooth surface pitting, tooth breakage, and wear causing backlash to exceed the M01 upper limit.

[Why] Verifying only by rated torque without checking peak torque is equivalent to pre-ordering tooth breakage: the instantaneous impact during walking/landing is the peak torque condition. The interlayer strength of printed parts is the weak link; try to align the load within the layers along the tooth width direction – this determines the layout direction in M05; this page only states the constraints.

[How to Analyze Your Situation] Torque magnitude comparable to Berkeley 6512: directly inherit its tooth width/material/parameter combination, with durability anchored by the 60-hour test. If exceeding that magnitude: first establish a destructive sampling test plan (print 3–5 gear samples and load to failure, executed in M05/M07) before discussing assembly. For metal reducer route: this step degenerates into checking the peak/instantaneous torque classification limits in the data manual (see discipline for reading tables in [Actuator Selection Manual](../playbooks/actuator-selection.md)).

## Acceptance Criteria

- [ ] Each joint reduction ratio has a dual inequality formula archived, closed-loop with the current/speed calculations from M02 (τ_motor, n_motor verification both passed).
- [ ] Topology selection has written justification, checked item by item against the backlash/back-drivability/cost columns of the M01 specification table.
- [ ] Cycloidal solution provides specific tooth count parameter combinations, or explicitly references the Berkeley open-source parametric design.
- [ ] Backlash, efficiency, and back-drivability expected values are written into the M01 specification table (mark "needs self-confirmation" if no data).
- [ ] Strength verification completed: maximum tooth force formula + material selection + peak torque condition explanation.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Output speed cannot meet the specification | Reduction ratio too large, only half of the dual inequality done | Return to Step 1 and add i ≤ n_motor_max/n_out calculation |
| Joint cannot be moved after power-off, force control inaccurate | High reduction ratio causes reverse efficiency collapse | Determined by topology, parameter tuning cannot fix; if force control needed, return to Step 2 and switch to a lower ratio solution |
| Cycloidal gear cannot fit into the pin ring or rotates with jamming | Profile parameters / printing tolerance error | Stop and reuse Berkeley parametric file; tolerance troubleshooting reserved for M05 |
| Backlash significantly increases after tens of hours of operation | Tooth surface wear/pitting, insufficient material or lubrication | Disassemble and inspect tooth surfaces; determine scrapping per Step 5 criteria; evaluate material change |
| Tooth breakage after impact condition | Verified only by rated torque, not peak torque | Return to Step 5 and recalculate with peak torque; increase tooth width or change topology |
| Current-torque calibration relationship is scattered | Large backlash + non-linear transmission friction | Use dual encoders to measure actual output end angle; current calibration reserved for M04 |

## Companion Reading

- Previous task: [M02 · Motor Calculation and Selection](m02-motor-sizing.md)
- Next task: [M04 · Driver, Sensing, and Wiring](m04-driver-sensing-wiring.md)
- Theoretical background: [Chapter 4 Actuators](/wiki/chapters/chapter-04/), [Chapter 9 Key Subsystem Design](/wiki/chapters/chapter-09/), [Chapter 3 Key Materials](/wiki/chapters/chapter-03/)
- [Actuator Selection Manual](../playbooks/actuator-selection.md) · [Stage 1 Overview](../stage-1-actuator.md)
