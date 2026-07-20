# Selection Guide: How to Choose an Actuator

> ⚠️ This roadmap is compiled based on public information and theoretical knowledge, and has not been verified on actual hardware; please verify safety specifications yourself when involving electrical and mechanical operations.

The actuator is the part of a humanoid robot BOM where it's easiest to "burn money in the wrong direction": the same leg can run for a few thousand yuan with smart servos, but might cost an order of magnitude more with a harmonic drive + frameless motor, and the performance difference only matters once you know exactly "what you want." This guide provides a decision framework: first translate your requirements into four quantifiable numbers, then narrow down to 2–3 candidates using the technology comparison table and manufacturer tier table, and finally conclude with bench testing. For theoretical background, see [Chapter 4: Actuators](/wiki/chapters/chapter-04/).

## 1. Four Key Questions: Translating "I want to build a robot" into Selection Parameters

### Question 1: What Peak Torque is needed?

[What to do] Perform a worst-case static estimation for the target joint: take the worst posture (knee at the lowest point of a squat, hip pitch during single-leg support with torso leaning forward), roughly calculate using `τ = m·g·d` (d is the moment arm from the center of mass to the joint axis), then multiply by a dynamic margin of 1.5–2. This number is the first filter for screening datasheets.

[Why] Peak torque determines the "specification size" of the reducer/motor. For example, the [Harmonic Drive reducer](/entry/ent_component_harmonic_drive_reducer/) CSF-32-100 has a repeated peak torque of 333 N·m and an instantaneous peak of 647 N·m (source: card citing Tradebearings spec page); as a reference, the [Unitree](/entry/ent_oem_unitree_robotics/) H1 knee joint peak torque is 360 N·m (source: Unitree card). The order of magnitude your estimate falls into directly determines which rows of the comparison table you should look at.

[How to analyze your situation] Desktop-level (arm span < 0.5 m, self-weight < 5 kg) joint peaks are typically 5–40 N·m, sufficient for servos and small quasi-direct drives; full-size bipedal (height > 1.2 m) hip/knee joints are typically 100–400 N·m, leaving only two paths: "harmonic/RV + frameless motor" and "high-torque quasi-direct drive." For walking on flat ground, use static value × 1.5; for running and jumping, use × 2 or more and verify the instantaneous peak torque.

### Question 2: What Continuous/Rated Torque and Thermal Considerations?

[What to do] Convert a typical duty cycle (e.g., continuous walking for 10 minutes) into an RMS torque, and ensure it is below the actuator's rated/continuous torque, not the peak torque.

[Why] Actuator burnout is almost always due to thermal failure, not instantaneous overload: peak torque can only be sustained for seconds, while continuous output is limited by winding temperature rise. The CSF-32-100 rated torque L10 is 137 N·m, only about 40% of its repeated peak torque of 333 N·m (source: harmonic reducer card); the Maxon EC-i 40 has a rated torque of 224 mN·m and a stall torque of 2080 mN·m, a difference of nearly 10 times (source: [Maxon card](/entry/ent_company_maxon_group_2024/)) — this ratio is even more extreme on the motor side, so don't select based on stall torque for continuous operation.

[How to analyze your situation] For teaching demonstrations (a few minutes each time), you can select close to the rated value; for long-duration walking or commercial exhibitions, it is recommended to keep the RMS within 70% of the rated value, and confirm the ambient temperature and cooling conditions corresponding to the rated value — if not specified, you must confirm with the supplier yourself.

### Question 3: What is the Weight Budget?

[What to do] Assign a weight limit to each joint: leg actuators should not exceed 40–50% of the total robot weight (industry rule of thumb), and concentrate heavy actuators near the hip/torso to reduce lower leg inertia.

[Why] The weight of an actuator becomes a load for the next joint: a 1 kg ankle joint increases the torque requirements for both the knee and hip, creating a cycle of "heavier requires more torque." For reference: the CSF-32-100 harmonic reducer weighs 3.2 kg (source: harmonic reducer card); the same size 32 domestic LHS-32-100 weighs 2.5 kg (source: [Leaderdrive card](/entry/ent_company_leaderdrive_2024/)); quasi-direct drives can be significantly lighter — the Berkeley Humanoid Lite's 6512 actuator has a single-unit BOM of approximately $188 (US) / $157 (China) (source: research file berkeley-humanoid-lite.md).

[How to analyze your situation] Desktop machines are not sensitive to weight; prioritize low cost and ease of use. For full-size bipedal robots, calculate the "torque benefit per kilogram" (torque density) for each actuator weight. [Quasi-direct drive actuators (QDD)](/entry/ent_technology_quasi_direct_drive_actuator_2024/) and Unitree's self-developed M107 motor (nominal torque density 189 N·m/kg, source: Unitree card) are products of this line of thinking.

### Question 4: Is Force Control and Back-drivability Needed?

[What to do] Clearly answer: does this joint need to "know how much force it is applying and yield when bumped" (force control/compliance), or does it only need to "precisely reach a certain angle" (position control)?

[Why] This is a branching point. High reduction ratio solutions (harmonic/RV/high-ratio servo) have high transmission friction and are not back-drivable; force control requires adding a torque sensor at the output. Low reduction ratio quasi-direct drives can directly estimate torque using the current loop and are naturally back-drivable, making them the mainstream route for proprioceptive force control — the Open Dynamic Robot Initiative's self-developed BLMC actuator is a typical example of "low reduction ratio + dual encoders + high torque transparency" (source: research file open-dynamic-robot-initiative.md). Counterexample: the ROBOTIS OP3's XM430-W350-R servo (reduction ratio 353.5:1, stall torque 4.1 N·m, source: robotis-op3 research file) has high positional accuracy and is plug-and-play, but the file explicitly states it "lacks proprioceptive force control capability and is unsuitable for high-dynamic motion control research."

[How to analyze your situation] Only for fixed-point demonstrations/teaching → position control is sufficient; servos or harmonic solutions are hassle-free. For walking balance, disturbance rejection, or human-robot collaboration → force control is a must; choose quasi-direct drive or "harmonic + joint torque sensor," accepting the trade-off of lower torque density for the former or higher cost for the latter.

## 2. Technology Route Comparison Table

The table below provides a qualitative comparison by route (specific values should be based on individual entity cards and manufacturer datasheets):

| Route | Backlash | Torque Density | Efficiency | Back-drivable | Cost Level | Typical Use |
|---|---|---|---|---|---|---|
| [Harmonic Drive](/entry/ent_component_harmonic_drive_reducer/) | Near zero (CSF ≤1 arcmin; SHF 10–20 arcsec) | High (CSF-32-100 rated 137 N·m / 3.2 kg) | 80%–90% | Essentially no | High (price not public, requires inquiry) | Precision joints: shoulder/elbow/hip/wrist |
| [RV Reducer](/entry/ent_component_rv_reducer/) | Low (arcmin level, confirm with supplier) | Very high, good impact resistance | Medium | No | High (requires inquiry) | Heavy-duty robot waist/hip; use with caution for full-size humanoids (heavy) |
| [Planetary Roller Screw](/entry/ent_component_planetary_roller_screw/) | Depends on lead accuracy | Extremely high linear thrust density (dynamic load 3–5 times that of ball screw for same size) | ~90% (ball screw 90–95%) | Back-drivable with large lead | Very high (Optimus-level solution) | Linear joints (knee/ankle push rods) |
| [Quasi-Direct Drive (QDD)](/entry/ent_technology_quasi_direct_drive_actuator_2024/) | Low (6–10:1 low reduction ratio, backlash depends on gear quality) | Medium (lower torque than harmonic for same weight) | High (short transmission chain) | Good | Low-Medium (BHL single unit BOM $157–188) | Dynamic legs for quadrupeds/bipeds |
| Smart Servo | Higher (multi-stage plastic/metal gear reduction) | Low (XM430 stall 4.1 N·m) | Low-Medium | Poor | Low (requires inquiry by model) | Desktop teaching machines, small joints for head/hands |

Two additional notes:

- Harmonic vs. RV division: Harmonic wins in zero backlash, light weight, and hollow shaft wiring (SHF-32 hollow type 1.665 kg, source: [Harmonic Drive Systems card](/entry/ent_company_harmonic_drive_systems_2024/)); RV wins in rigidity and impact resistance. Both routes have precedents for full-size humanoid hips; simply weigh "weight" against "impact life."
- For the screw route, you must perform the mechanical conversion yourself: thrust `F = 2π·η·τ / l` (l is the lead). Example calculation: with F=8000 N, l=5 mm, η=0.90, the motor-side continuous torque required is approximately 7.07 N·m (source: planetary roller screw card). When the lead angle is greater than the friction angle, it is back-drivable; when smaller, it is self-locking — choose a large lead for force control, and avoid trapezoidal self-locking screws.

## 3. Manufacturer Quick Reference (By Tier)

| Tier | Manufacturer | What to Buy | Repository Materials |
|---|---|---|---|
| High-End Import | [Harmonic Drive Systems](/entry/ent_company_harmonic_drive_systems_2024/) | CSF/CSG Component Type, SHF/SHG Hollow Shaft Harmonic Drives, FHA-C Integrated Actuators | ✅ Card includes detailed parameters for CSF-32-50, SHF-32-120 |
| High-End Import | Nabtesco | RV Reducers | ⚠️ No card in this repository; parameters need to be confirmed with the supplier |
| High-End Import | [Maxon](/entry/ent_company_maxon_group_2024/) | EC-i / EC Brushless Motors, Gearboxes, Drives (Common for Dexterous Hands and Small Joints) | ✅ Card includes detailed parameters for EC-i 40, EC 40 |
| High-End Import | Kollmorgen | Frameless Torque Motors (RBE/TBM Series, motor-side option for custom joints) | ⚠️ No card yet; requires price inquiry |
| Domestic Alternative | [Leaderdrive](/entry/ent_company_leaderdrive_2024/) | LHS/LCS Harmonic Drives, LCD Ultra-Thin Series (Wrist/Finger), KGM Integrated Joint Modules | ✅ Card includes detailed parameters for LHS-32-100, LCD-14-100; can serve as a starting point for Harmonic Drive replacement |
| Domestic Complete Machine/Module | [Unitree](/entry/ent_oem_unitree_robotics/) | Self-developed M107 High Torque Density Motor, Joint Modules | ✅ Card includes M107 torque density, H1/G1 joint parameters |
| Maker-Grade | CubeMars | AK Series QDD Joint Modules (MIT Mini Cheetah lineage) | ⚠️ No card yet; parameters need to be confirmed with the supplier |
| Maker-Grade | Custom 3D Printed QDD | Drone Motor + Cycloidal/Planetary 3D Printed Reducer | Research Archive: Berkeley Humanoid Lite (BOM transparent, 60 h durability test) |

One-sentence principle for tier selection: For research reproducibility and stable supply, choose high-end import or domestic alternatives; if budget is tight, you are willing to tinker, and you have many joints, maker-grade QDD or custom development can reduce actuator costs to a fraction of high-end solutions, at the cost of consistency and lifespan validation being your own responsibility.

## 4. Three Scenario-Based Selection Examples

### Scenario A: Desktop Teaching Arm Joint (Reach 0.3–0.5 m, Payload < 1 kg)

Requirement Answer: Peak 5–15 N·m; Continuous low; Weight insensitive; Position control sufficient, force control optional.

- Conservative Solution: Smart servo bus (Dynamixel lineage). Refer to OP3's XM430-W350-R: Stall torque 4.1 N·m, supports current control, bus daisy-chain (Source: robotis-op3 research archive). SDK and documentation are extremely comprehensive, but backlash is large, unsuitable for force control research.
- Advanced Solution: Small harmonic drive. Leaderdrive LCD-14-100: Rated 5.1 N·m, instantaneous peak 33 N·m, weight 0.48–0.68 kg, backlash ≤20 arcsec (Source: Leaderdrive card) – The ultra-thin cup flexspline is designed for tight axial spaces like wrists/forearms.
- How to Analyze Your Situation: Budget priority, short course cycle → Servo motor; Need to publish papers, do compliant control → Small harmonic drive + frameless motor, or practice with custom QDD.

### Scenario B: Biped Hip/Knee Joint (Full-size or 1 m class)

Requirement Answer: Peak 100–400 N·m (calculated per Question 1); Continuous based on walking RMS; Weight sensitive; Force control mandatory.

- Route 1 (Quasi-Direct Drive): MIT Cheetah lineage, Unitree H1 knee peak 360 N·m follows this route (Source: Unitree card). Advantages: back-drivability, impact resistance, high bandwidth; Cost: high standing power consumption (motor continuously outputs torque to support weight).
- Route 2 (Harmonic Drive + Frameless Motor): THORMANG3 approach – Harmonic reduction + high power density servo (its platform uses PH54 series 100 W modules × 11, Source: thormang3 research archive), ample torque but "the main cost of the whole machine is here" (archive quote).
- Route 3 (Linear Drive): [Planetary Roller Screw](/entry/ent_component_planetary_roller_screw/) push-rod knee/ankle (Optimus approach), highest thrust density, can absorb impact, but highest design and manufacturing threshold, price needs to be confirmed with the supplier (SKF data: dynamic load 3–5 times that of ball screw at same size, lifespan 10–15 times, Source: screw card).
- How to Analyze Your Situation: First biped build, strong control background → QDD (BHL archive proves $157 BOM level can also achieve zero-shot sim-to-real); Strong mechanical background, pursuing compactness and long endurance → Harmonic drive + frameless motor; Screw route recommended for the second robot.

### Scenario C: Dexterous Hand Finger

Requirement Answer: Very small peak (mN·m level); Extremely space-constrained; Fast response required; Cost × number of fingers.
- Mainstream Solution: [Hollow Cup Motor](/entry/ent_component_hollow_cup_motor_2024/) (Ironless) + Micro reducer/leadscrew/tendon. Dingsi series outer diameter Ø10–Ø42 mm, weight 5–60 g, example rated torque 1.5 mN·m, stall torque range 1–50 mN·m, mechanical time constant <5 ms (Source: Hollow Cup Motor card) – Ironless means no cogging torque, low inertia, enabling fast finger flexion/extension.
- Alternative Solution: Maxon ECX SPEED and other high-speed brushless motors (Source: Maxon card), or linear motors/tendon drive external to forearm.
- How to Analyze Your Situation: First calculate fingertip force target to back-calculate tendon tension and motor stall torque; Hollow cup motor unit price is not public, requires price inquiry, and for procurement scales of "6–20 units per hand", both bargaining power and consistency need to be discussed.

## 5. Validation Methods: How to Read Datasheets, How to Test on a Bench

### Five Disciplines for Reading Datasheets

1.  Distinguish Four Torque Ratings: Rated (continuous), Starting/Stopping Allowable, Repeated Peak, Instantaneous Peak. Compare each against your RMS/Peak requirements (See Leaderdrive LHS-32-100 card for differences: Starting/Stopping Allowable 221 N·m is approx. 2.4 times the Rated 91 N·m).
2.  Rated torque often comes with a speed condition (e.g., "at 2000 rpm input"). Standardize to the same speed when comparing across manufacturers.
3.  Check Backlash Units Carefully: arcmin vs arcsec (1 arcmin = 60 arcsec). Harmonic Drive SHF specifies 10–20 arcsec, Leaderdrive specifies ≤20 arcsec – same order of magnitude.
4.  Torsional Stiffness uses segmented values (Harmonic K1/K2/K3). Use K1 from the low-torque segment for force control bandwidth estimation, don't fool yourself with K3.
5.  Efficiency, lifespan (L10) are tied to lubrication. If changing grease or operating in low-temperature environments, values need to be confirmed with the supplier.

### Bench Test Checklist (Mandatory After Receiving)

- Backlash Measurement: Lock input, apply ±5% rated torque, measure return difference with dial indicator/encoder, compare with datasheet.
- Back-drive Torque: Manually push and rotate the QDD joint when powered off to measure starting torque; excessive values indicate high friction or inertia, compromising force control transparency.
- Temperature Rise Curve: Run at rated RMS torque continuously for 30 min, record housing temperature, back-calculate duty cycle limits.
- Current-Torque Calibration: Hang weight lever arm, load point by point, fit the actual slope of `τ = K_t·I`. The accuracy of current-based force control depends entirely on this table.
- Torque Ripple: Rotate slowly at constant speed, record current ripple, evaluate low-speed force control limits.

## Acceptance Criteria

- Each target joint has a written "Four-Question Requirement" answer: Peak/Continuous torque (with calculation process), weight limit, force control requirement boolean.
- Candidates are narrowed down to ≤3 "Motor + Reducer" combinations, each supported by a real datasheet, with rated torque > RMS requirement and instantaneous peak > worst-case scenario estimate.
- Key parameters (torque, backlash, weight) are all traceable to cards, datasheets, or research archives; any unverifiable parameters are marked "needs confirmation with supplier".
- At least one prototype has undergone bench testing (backlash + temperature rise + current-torque calibration), with a written explanation for any deviation between measured values and datasheet.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Joint loses torque/overheats after a few minutes of continuous operation | Selected based on peak torque, RMS exceeds rated | Check task RMS torque vs rated value; add cooling or reduce duty cycle |
| Motor hums and heats up during static standing | QDD standing power consumption underestimated | Measure standing phase current; consider parallel elastic elements or change route |
| Position tracking has dead zone/jitter | Large reducer backlash (common with servos) | Measure backlash with dial indicator; switch to low-backlash solution or compensate in control |
| Force control estimated torque doesn't match external force sensor | K_t value is theoretical, not calibrated | Perform current-torque calibration with weight lever; update K_t and friction compensation |
| Harmonic joint precision degrades after impact | Instantaneous torque exceeded limit, damaging flexspline | Compare impact scenario vs instantaneous peak limit; re-measure backlash |
| Screw joint cannot be back-driven, force control fails | Lead angle < friction angle, self-locking | Calculate lead angle/friction angle; switch to larger lead screw |

## Companion Reading

- [Phase 1 · Build an Actuator](../stage-1-actuator.md) – Full process of assembly, driving, and debugging after selection
- [Roadmap Overview](../index.md)
