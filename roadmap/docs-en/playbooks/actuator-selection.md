# Selection Guide: How to Choose an Actuator

The actuator is the part of a humanoid robot BOM where it's easiest to "burn money in the wrong direction": on the same leg, using a smart servo (Servo) can run for a few thousand yuan, while using a harmonic drive + frameless motor (Frameless Motor) might be an order of magnitude more expensive, and the performance difference only matters once you know exactly "what you want." This guide provides a decision framework: first, translate your requirements into four quantifiable numbers, then narrow down to 2–3 candidates using the technology route comparison table and manufacturer tier table, and finally, validate with bench testing. For background principles, see [Chapter 4: Actuators](/wiki/chapters/chapter-04/).

## 1. Four Key Questions: Translating "I want to build a robot" into Selection Parameters

### Question 1: What is the required Peak Torque?

**[What to do]** Perform a worst-case static estimation for the target joint: take the worst posture (knee at the lowest point of a squat, hip pitch during single-leg support with torso leaning forward), roughly calculate using `τ = m·g·d` (d is the moment arm from the center of mass to the joint axis), then multiply by a dynamic margin of 1.5–2. This number is the first filter for screening datasheets.

**[Why]** Peak torque determines the "specification size" of the reducer/motor. For example, the [Harmonic Drive](/entry/ent_component_harmonic_drive_reducer/) CSF-32-100 has a repeated peak torque of 333 N·m and an instantaneous peak of 647 N·m (source: card referencing Tradebearings spec sheet); for reference, the [Unitree](/entry/ent_oem_unitree_robotics/) H1 knee peak torque is 360 N·m (source: Unitree card). The magnitude of your estimate directly determines which rows of the comparison table you should be looking at.

**[How to analyze your situation]** For desktop-level robots (arm span < 0.5 m, self-weight < 5 kg), joint peak torque is typically 5–40 N·m, where servos and small quasi-direct drives are sufficient. For full-size bipeds (height > 1.2 m), hip/knee torque is typically 100–400 N·m, leaving only two paths: "harmonic/RV + frameless motor" and "high-torque quasi-direct drive." For flat-ground walking, multiply the static value by 1.5; for running and jumping, multiply by 2 or more and verify the instantaneous peak torque.

### Question 2: What is the Continuous/Rated Torque and Thermal Consideration?

**[What to do]** Convert a typical task cycle (e.g., continuous walking for 10 minutes) into an RMS torque, and ensure it is below the actuator's continuous/rated torque, not its peak torque.

**[Why]** Actuator failure is almost always due to thermal failure, not instantaneous overload: peak torque can only be sustained for seconds, while continuous output is limited by winding temperature rise. The rated torque L10 for the CSF-32-100 is 137 N·m, only about 40% of its repeated peak torque of 333 N·m (source: harmonic reducer card); the Maxon EC-i 40 has a rated torque of 224 mN·m and a stall torque of 2080 mN·m, a difference of nearly 10 times (source: [Maxon card](/entry/ent_company_maxon_group_2024/)) — this ratio is even more extreme on the motor side, so do not select based on stall torque for continuous operation.

**[How to analyze your situation]** For teaching demonstrations (a few minutes each time), you can select close to the rated value. For prolonged walking or commercial displays, it is recommended to keep the RMS within 70% of the rated value, and confirm the ambient temperature and cooling conditions corresponding to the rated value — if not specified, you must confirm with the supplier yourself.

### Question 3: What is the Weight Budget?

**[What to do]** Assign a weight limit to each joint: leg actuators should ideally not exceed 40–50% of the total robot weight (industry rule of thumb), and concentrate heavier actuators near the hip/torso to reduce leg inertia.

**[Why]** The weight of an actuator becomes part of the load for the next joint: a 1 kg ankle joint increases the torque requirements for both the knee and hip, creating a cycle of "heavier requires more torque." For magnitude reference: the CSF-32-100 harmonic reducer weighs 3.2 kg (source: harmonic reducer card); the equivalent domestic LHS-32-100 weighs 2.5 kg (source: [Leaderdrive card](/entry/ent_company_leaderdrive_2024/)); quasi-direct drives can be significantly lighter — the 6512 actuator from Berkeley Humanoid Lite has a single-unit BOM of approximately $188 (US) / $157 (China) (source: research file berkeley-humanoid-lite.md).

**[How to analyze your situation]** Desktop robots are not sensitive to weight; prioritize low cost and ease of use. For full-size bipeds, calculate the "torque benefit per kilogram" (torque density) for each actuator weight. [Quasi-direct drive actuators (QDD)](/entry/ent_technology_quasi_direct_drive_actuator_2024/) and Unitree's self-developed M107 motor (nominal torque density 189 N·m/kg, source: Unitree card) are products of this line of thinking.

### Question 4: Is Force Control and Back-drivability Required?

**[What to do]** Clearly answer: Does this joint need to "know how much force it is applying and yield when bumped" (force control/compliance), or does it only need to "accurately reach a certain angle" (position control)?

**[Why]** This is a branching point. High reduction ratio solutions (harmonic/RV/high-ratio servos) have high transmission friction and are not back-drivable; force control requires adding a torque sensor at the output. Low reduction ratio quasi-direct drives can directly estimate torque using the current loop and are naturally back-drivable, making them the mainstream route for proprioceptive force control — the Open Dynamic Robot Initiative's self-developed BLMC actuator is a typical example of "low reduction ratio + dual encoders + high torque transparency" (source: research file open-dynamic-robot-initiative.md). Counterexample: the ROBOTIS OP3's XM430-W350-R servo (reduction ratio 353.5:1, stall torque 4.1 N·m, source: robotis-op3 research file) has high positional accuracy and is plug-and-play, but the file explicitly evaluates it as "lacking proprioceptive force control capability, unsuitable for high-dynamic motion control research."

**[How to analyze your situation]** For fixed-point demonstrations/teaching only → position control is sufficient; servos or harmonic solutions are worry-free. For walking balance, disturbance rejection, or human-robot collaboration → force control is a must; choose quasi-direct drive or "harmonic + joint torque sensor," accepting the lower torque density of the former or the higher cost of the latter.

## 2. Technology Route Comparison Table

The table below provides a qualitative comparison by route (refer to individual entity cards and manufacturer datasheets for specific values):

| Route | Backlash | Torque Density | Efficiency | Back-drivability | Cost Level | Typical Use Cases |
|---|---|---|---|---|---|---|
| [Harmonic Drive](/entry/ent_component_harmonic_drive_reducer/) | Near zero (CSF ≤1 arcmin; SHF 10–20 arcsec) | High (CSF-32-100 rated 137 N·m / 3.2 kg) | 80%–90% | Essentially none | High (price not public, request quote) | Precision joints: shoulder/elbow/hip/wrist |
| [RV Reducer](/entry/ent_component_rv_reducer/) | Low (arcmin level, confirm with supplier) | Very high, good shock resistance | Medium | None | High (request quote) | Heavy-load robot waist/hip; use cautiously in full-size humanoids (heavy) |
| [Planetary Roller Screw](/entry/ent_component_planetary_roller_screw/) | Depends on lead accuracy | Very high linear thrust density (3–5 times dynamic load of ball screw for same size) | ~90% (ball screw 90–95%) | Back-drivable with large lead | Very high (Optimus-level solution) | Linear joints (knee/ankle pushrods) |
| [Quasi-Direct Drive (QDD)](/entry/ent_technology_quasi_direct_drive_actuator_2024/) | Low (6–10:1 low reduction ratio, backlash depends on gear quality) | Medium (lower torque than harmonic for same weight) | High (short transmission chain) | Good | Medium-Low (BHL single unit BOM $157–188) | Dynamic legs for quadrupeds/bipeds |
| Smart Servo | Higher (multi-stage plastic/metal gear reduction) | Low (XM430 stall 4.1 N·m) | Low-Medium | Poor | Low (request quote by model) | Desktop teaching robots, small joints for head/hands |

Two additional notes:

- **Harmonic vs. RV division of labor:** Harmonic wins with zero backlash, light weight, and hollow wiring (SHF-32 hollow type 1.665 kg, source: [Harmonic Drive Systems card](/entry/ent_company_harmonic_drive_systems_2024/)); RV wins with rigidity and shock resistance. Both routes have precedents for full-size humanoid hips; simply weigh "weight" against "shock resistance lifespan."
- **Mechanical conversion for screw routes must be calculated manually:** Thrust `F = 2π·η·τ / l` (l is the lead). Example calculation: For F=8000 N, l=5 mm, η=0.90, the motor-side continuous torque required is approximately 7.07 N·m (source: planetary roller screw card). When the lead angle is greater than the friction angle, it is back-drivable; when smaller, it is self-locking — choose a large lead for force control, do not select a trapezoidal self-locking screw.

## III. Manufacturer Quick Reference (by Tier)

| Tier | Manufacturer | What to Buy | Repository Materials |
|---|---|---|---|
| High-End Import | [Harmonic Drive Systems](/entry/ent_company_harmonic_drive_systems_2024/) | CSF/CSG component type, SHF/SHG hollow shaft harmonic reducers, FHA-C integrated actuators | ✅ Card includes detailed parameters for CSF-32-50, SHF-32-120 |
| High-End Import | Nabtesco | RV reducers | ⚠️ No card in this repository; parameters need to be confirmed with the supplier |
| High-End Import | [Maxon](/entry/ent_company_maxon_group_2024/) | EC-i / EC brushless motors, gearboxes, drives (commonly used in dexterous hands and small joints) | ✅ Card includes detailed parameters for EC-i 40, EC 40 |
| High-End Import | Kollmorgen | Frameless torque motors (RBE/TBM series, motor-side option for custom joints) | ⚠️ No card yet; requires price inquiry |
| Domestic Alternative | [Leaderdrive](/entry/ent_company_leaderdrive_2024/) | LHS/LCS harmonic reducers, LCD ultra-thin series (wrist/finger), KGM integrated joint modules | ✅ Card includes detailed parameters for LHS-32-100, LCD-14-100; can serve as a starting point for Harmonic Drive replacement |
| Domestic Complete Machine/Module | [Unitree](/entry/ent_oem_unitree_robotics/) | Self-developed M107 high torque density motors, joint modules | ✅ Card includes M107 torque density, H1/G1 joint parameters |
| Maker-Level | CubeMars | AK series QDD joint modules (MIT Mini Cheetah lineage) | ⚠️ No card yet; parameters need to be confirmed with the supplier |
| Maker-Level | Custom 3D Printed QDD | Drone motor + cycloidal/planetary printed reducer | Research archive: Berkeley Humanoid Lite (BOM transparent, 60 h durability test) |

One-sentence principle for tier selection: For research reproducibility and stable supply, choose high-end import or domestic alternatives; if budget is tight, you are willing to tinker, and the number of joints is high, maker-level QDD or custom development can reduce actuator costs to a fraction of high-end solutions, at the cost of consistency and lifespan validation being your own responsibility.

## IV. Three Scenario-Based Selection Examples

### Scenario A: Desktop Teaching Arm Joint (Reach 0.3–0.5 m, Payload < 1 kg)

Requirement Answer: Peak 5–15 N·m; continuous low; weight insensitive; position control sufficient, force control optional.

- Conservative Solution: Smart servo bus (Dynamixel lineage). Refer to OP3's XM430-W350-R: Stall torque 4.1 N·m, supports current control, bus daisy-chain (Source: robotis-op3 research archive). SDK and documentation are extremely comprehensive, but backlash is large, unsuitable for force control research.
- Advanced Solution: Small harmonic. Leaderdrive LCD-14-100: Rated 5.1 N·m, instantaneous peak 33 N·m, weight 0.48–0.68 kg, backlash ≤20 arcsec (Source: Leaderdrive card) – the ultra-thin cup flexspline is designed for tight axial spaces like wrists/forearms.
- How to Analyze Your Situation: Budget priority, short course cycle → servo motor; aiming for publication, compliance control → small harmonic + frameless motor, or practice with custom QDD.

### Scenario B: Biped Hip/Knee Joint (Full-size or ~1 m class)

Requirement Answer: Peak 100–400 N·m (calculated per Question 1); continuous based on walking RMS; weight sensitive; force control mandatory.

- Route 1 (Quasi-Direct Drive): MIT Cheetah lineage, Unitree H1 knee peak 360 N·m follows this route (Source: Unitree card). Advantages: backdrivability, impact resistance, high bandwidth; Cost: high standing power consumption (motor continuously outputs torque to support body weight).
- Route 2 (Harmonic + Frameless Motor): THORMANG3 approach – harmonic reduction + high power density servo (its platform uses PH54 series 100 W modules × 11, Source: thormang3 research archive), ample torque but "the main cost of the whole machine lies here" (archive quote).
- Route 3 (Linear Drive): [Planetary Roller Screw](/entry/ent_component_planetary_roller_screw/) push-rod knee/ankle (Optimus approach), highest thrust density, can absorb impact, but highest design and manufacturing threshold; price needs confirmation with supplier (SKF data: dynamic load capacity 3–5 times that of ball screws for the same size, lifespan 10–15 times, Source: screw card).
- How to Analyze Your Situation: First biped build, strong control background → QDD (BHL archive proves $157 BOM level can also achieve zero-shot sim-to-real); strong mechanical background, pursuing compactness and long endurance → harmonic + frameless motor; screw route recommended for the second robot.

### Scenario C: Dexterous Hand Finger

Requirement Answer: Very small peak (mN·m level); extremely space-constrained; fast response required; cost × number of fingers.
- Mainstream Solution: [Hollow Cup Motor](/entry/ent_component_hollow_cup_motor_2024/) (coreless) + micro reducer/leadscrew/tendon. Dingsheng series outer diameter Ø10–Ø42 mm, weight 5–60 g, example rated torque 1.5 mN·m, stall torque range 1–50 mN·m, mechanical time constant <5 ms (Source: Hollow Cup Motor card) – coreless means no cogging torque, low inertia, enabling fast finger flexion/extension.
- Alternative Solution: Maxon ECX SPEED and other high-speed brushless motors (Source: Maxon card), or linear motors/tendon drives placed in the forearm.
- How to Analyze Your Situation: First calculate fingertip force target, then back-calculate tendon tension and motor stall torque; hollow cup motor unit price is not public, requires price inquiry, and procurement at a scale of "6–20 units per hand" requires negotiation on pricing and consistency.

## V. Validation Methods: How to Read Datasheets, How to Test on a Bench

### Five Disciplines for Reading Datasheets

1.  Distinguish four torque levels: Rated (continuous), Allowable for start/stop, Repeated peak, Instantaneous peak. Compare each against your RMS/peak requirements (See Leaderdrive LHS-32-100 card for differences: Allowable start/stop torque 221 N·m is approx. 2.4 times rated 91 N·m).
2.  Rated torque often comes with a speed condition (e.g., "at 2000 rpm input"). Standardize to the same speed when comparing across manufacturers.
3.  Check backlash units carefully: arcmin vs arcsec (1 arcmin = 60 arcsec). Harmonic Drive SHF specifies 10–20 arcsec, Leaderdrive specifies ≤20 arcsec – same order of magnitude.
4.  Torsional stiffness uses segmented values (K1/K2/K3 for harmonics). Use K1 for the low-torque segment when estimating force control bandwidth; don't deceive yourself with K3.
5.  Efficiency, lifespan (L10) are tied to lubrication. If changing grease or operating in low-temperature environments, values need confirmation with the supplier.

### Bench Test Checklist (Mandatory Upon Arrival)

- Backlash Measurement: Lock input shaft, apply ±5% rated torque, measure return difference with a dial indicator/encoder, compare with datasheet.
- Backdrive Torque: Manually push/pull the QDD joint when powered off to feel the starting torque; excessive values indicate high friction or inertia, compromising force control transparency.
- Temperature Rise Curve: Run continuously at rated RMS torque for 30 min, record housing temperature, infer the upper limit of the duty cycle.
- Current-Torque Calibration: Load incrementally using a weight arm, fit the actual slope of `τ = K_t·I`. The accuracy of current-based force control depends entirely on this table.
- Torque Ripple: Rotate slowly at constant speed, record current ripple, evaluate the lower limit of low-speed force control.

## Acceptance Criteria

- For each target joint, there is a written answer to the "Four Requirement Questions": Peak/Continuous torque (with calculation process), Weight limit, Force control requirement (boolean).
- Candidates are narrowed down to ≤3 "motor + reducer" combinations, each supported by a real datasheet, with rated torque > RMS requirement and instantaneous peak > worst-case scenario estimate.
- Key parameters (torque, backlash, weight) are all traceable to cards, datasheets, or research archives; any unverifiable parameters are marked "requires confirmation with supplier".
- At least one prototype joint has undergone bench testing (backlash + temperature rise + current-torque calibration), with a written explanation for any deviation between measured values and datasheet specifications.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Joint loses torque/overheats after a few minutes of continuous operation | Selected based on peak torque, RMS exceeds rated | Check task RMS torque vs rated value; add cooling or reduce duty cycle |
| Motor hums and heats up during static standing | QDD standing power consumption underestimated | Measure standing phase current; consider parallel elastic elements or change route |
| Position tracking has dead zone/jitter | Large reducer backlash (common with servos) | Measure backlash with dial indicator; switch to low-backlash solution or compensate in control |
| Force control estimated torque doesn't match external force sensor | K_t used is theoretical, not calibrated | Perform current-torque calibration with weight arm; update K_t and friction compensation |
| Harmonic joint precision degrades after impact | Instantaneous torque exceeded limit, damaging flexspline | Verify impact scenario vs instantaneous peak limit; re-measure backlash |
| Screw joint cannot be backdriven, force control fails | Lead angle < friction angle, self-locking | Calculate lead angle/friction angle; switch to a larger lead screw |

## Companion Reading

- [Stage 1 · Build a Joint](../stage-1-actuator.md) – Full process of assembly, driving, and debugging after selection
- [Roadmap Overview](../index.md)
