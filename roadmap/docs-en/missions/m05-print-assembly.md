# M05 · 3D Printing and Mechanical Assembly: Turning Drawings into a Joint That Feels Warm in Your Hand

**Global Position**: After M03 Reducer Design and M04 Electrical Drawings. Input is the reducer/housing drawings, electrical drawings, and a pile of standard parts; output is an **assembled single-joint electromechanical module** — smooth to turn by hand, stable readings, ready to be placed on the test bench for M06 Firmware and M07 Debugging.

**Prerequisites**: M03 reducer drawings and BOM are frozen; M04 electrical drawings (power, signal, and bus — three sheets) are finalized; a leveled FDM printer is ready.

Theoretical Background: [Chapter 3: Key Materials](/wiki/chapters/chapter-03/), [Chapter 10: Manufacturing Process System](/wiki/chapters/chapter-10/), [Chapter 11: Assembly, Integration, and Testing](/wiki/chapters/chapter-11/).

## Step 1: Material Selection — First Decide "Which Material for Which Part"

[What to Do] Select materials based on part function and fill in the material column of the BOM:

| Part | First Choice | Alternative/Notes |
|---|---|---|
| Cycloidal gear/transmission parts | PLA (high-fill printing) | Berkeley cycloidal gears are all made with desktop FDM + PLA, passing a 60-hour endurance test ([arXiv:2504.17249](https://arxiv.org/abs/2504.17249)); advanced option: Nylon/PA-CF |
| Housing/end caps | PETG | Switch to ABS/ASA when close to the motor or requiring higher temperature resistance |
| Brackets/structural parts | PETG | Switch to PA-CF for high stiffness requirements |
| Buffer pads/foot pads/limit pads | TPU | Rely on elasticity; the softer, the slower the printing speed needed |

Nylon/PA-CF has high strength and good wear resistance, making it a preferred gear material, but it is **hygroscopic** — it must be dried before printing after opening, otherwise bubbles and filament breakage will occur; TPU is soft, so first confirm your extruder can handle it.

[Why] There is no "best" material, only the one "best suited for the part's working conditions": gears need to be rigid and wear-resistant — the cycloidal structure distributes load across multiple teeth, so even PLA printed parts can handle it. This is precisely why the cycloidal [quasi-direct-drive actuator](/entry/ent_technology_quasi_direct_drive_actuator_2024/) dares to use plastic gears (berkeley-humanoid-lite archive); housings need to be tough (resistant to cracking from assembly bumps and drops); pads need to be soft. A system map of materials can be found in [Chapter 3: Key Materials](/wiki/chapters/chapter-03/).

[How to Analyze Your Situation] First time: Copy Berkeley's all-PLA approach to get the process running smoothly; if the joint is close to the motor and runs continuously at high temperatures, switch the housing to ASA; only consider PA-CF when pursuing batch consistency — it demands a significantly higher level of machine and drying capability.

## Step 2: Printing Process Parameters

[What to Do] The following parameters are engineering starting points; adjust and record based on your machine and material: 0.4 mm nozzle; layer height 0.12–0.2 mm; outer walls ≥ 4; infill 40–60% (use high infill or even 100% for functional gear parts). The principle for orientation is one sentence: **Layer line direction ⊥ main force direction** — print the cycloidal disc flat so the tooth surfaces are formed in the XY plane. Add supports for overhangs > 60°; three tricks for warping control: bed temperature per material recommendation, brim 5–8 mm, and enclosure printing for ABS/ASA.

[Why] FDM parts are anisotropic: the interlayer bond is the weakest direction, and failure along the layer lines is a classic break pattern; printing the cycloidal disc flat changes the stress at the tooth root from "cross-layer transfer" to "in-plane transfer". Wall count determines strength more than infill percentage — a part with 4 walls + 40% infill is usually more durable than one with 2 walls + 80% infill (process rule, engineering experience). A systematic discussion of manufacturing processes can be found in [Chapter 10: Manufacturing Process System](/wiki/chapters/chapter-10/).

[How to Analyze Your Situation] When using a new material, first print a temperature tower and flow calibration part; for functional gear parts, print one individually for a meshing test, and only proceed to batch printing if it passes. Don't throw away failed prints; weigh them and record the loss — this is exactly what the 15% loss margin set in M01 is for.

## Step 3: Tolerances and Fits

[What to Do] First, accept reality: desktop FDM dimensional accuracy is in the ±0.1–0.3 mm range (varies by machine, material, and orientation; requires your own trial fitting and calibration). Three countermeasures:

1.  **Trial fit block calibration**: Print a set of trial fit blocks with increasing hole diameters (nominal +0.05/+0.10/+0.15/+0.20 mm), measure the actual offset of your machine for each type of fit, and write the conclusion into the drawing notes;
2.  **Bearing housings**: Design for transition to light interference fit; trial fit printed parts before batch production; press in using a vise/press tool at a constant speed — no hammers allowed;
3.  **Shaft-hole**: Use clearance fit with 0.1–0.2 mm allowance (determined by trial fit blocks); use a soldering iron at constant temperature to press **heat-set inserts** vertically; directly printed threaded holes are only suitable for non-load-bearing situations.

Standardize the process: First article trial assembly → Mold modification → Small batch → Full inspection of critical dimensions.

[Why] Fits are the interface between two worlds: "printed parts" and "machined standard parts". Bearings, shafts, and pins have micron-level precision; printed parts are sub-millimeter level. Going straight to batch production without trial fitting = batch scrap. Heat-set inserts embed metal threads into plastic, making them the only reliable solution for repeated disassembly in a vibration environment.

[How to Analyze Your Situation] If you don't have a micrometer, use a caliper plus trial fit feel: it's good if a bearing can be pushed in most of the way by hand and seated lightly with a vise; "needs a hammer" means too much interference, "falls out" means too much clearance.

## Step 4: Standard Parts and Procurement

[What to Do] List hardware items according to the M03 BOM, with all quantities **×1.15** (loss margin, rule set in M01):

| Category | Selection Key Points |
|---|---|
| Bearings | Thin-section deep groove ball series (68xx/69xx type) saves axial space; inner and outer diameters per drawing, normal clearance is sufficient |
| Fasteners | M3/M4 hex socket screws + spring washers, prepare medium-strength threadlocker; length based on thread engagement depth of 1.5–2 times diameter |
| Shafts | Shafts/pins (h6/g6 tolerance grade concept); don't use printed holes directly as bearing seats |
| Lubrication | Cycloidal pinwheel contact surfaces **must** be greased; confirm the specific type yourself, avoid varieties incompatible with plastic |

Reference scale: Berkeley 6512 single-joint BOM $157–188 includes bearings, fasteners, and printed parts (berkeley-humanoid-lite archive) — hardware is cheap, but missing one piece stops the entire line. Supplier channels can be found in [Appendix D: Supplier Directory](/wiki/appendices/appendix-d/).

[Why] The pitfall with standard parts isn't "what to buy", but "buying too few" and "buying the wrong length": a screw 2 mm too long might puncture the motor winding, while one too short won't get enough thread engagement. The 15% margin is calculated per piece, not per cost — lost, stripped, and snapped screws are all small items.

[How to Analyze Your Situation] Place orders by summing "number of joints × single-joint BOM"; don't buy fasteners at the "let's try one joint first" pace — shipping costs more than the screws. Upon receipt, sort by specification into labeled boxes so you don't grab the wrong ones during assembly.

## Step 5: Assembly Process — Slow is Smooth

[What to Do] Assemble in a fixed sequence, and **turn the output shaft by hand** after each step (power off, rotate the output shaft manually):

1.  Reducer sub-assembly: Position cycloidal disc, pins, and bearings; apply grease; tighten in a cross-pattern step by step;
2.  Hand-turn check: No binding points, no abnormal noise throughout the range;
3.  Motor into housing: Verify screw length (don't hit the winding); route phase wires per M04 drawing;
4.  Encoder alignment: Follow the M04 three essentials (coaxiality, gap, stay away from phase wires); double-check before powering on;
5.  Close housing: Tighten screws in a diagonal cross-pattern, in 2–3 steps; bearing preload should be "enough to eliminate axial play but not make hand-turning stiff".

Final actions: Insulation check before powering on; current limit on first power-up; record the **no-load current baseline** (idle current at rated voltage), write it on a label and stick it on the housing — this is the benchmark for M07 temperature rise and efficiency comparison. The systematic approach to assembly and testing can be found in [Chapter 11: Assembly, Integration, and Testing](/wiki/chapters/chapter-11/).

[Why] "Hand-turn after each step" minimizes the cost of fault localization: if it binds only after full assembly, you have to disassemble everything; if it binds right after the previous step, the problem is limited to those few parts. Cross-pattern step-by-step tightening prevents housing warping and bearing misalignment — same principle as changing a tire. No-load current is a comprehensive indicator of assembly quality: poor coaxiality, excessive preload, and insufficient lubrication all show up as increased current.

[How to Analyze Your Situation] If hand-turning reveals a binding point: first loosen the last set of screws installed to see if it disappears, thereby distinguishing between "assembly stress" and "part out-of-tolerance". Endurance expectation management: Berkeley used a 60-hour endurance test to validate PLA cycloidal gears (berkeley-humanoid-lite archive); test your own designed parts at this scale (M07 execution).

## Acceptance Criteria

- [ ] Part-material mapping table documented; printing parameters (layer height/walls/infill/orientation) recorded and archived.
- [ ] Trial fit block calibration completed; all critical fits (bearing housing, shaft-hole) passed trial fitting.
- [ ] No binding or abnormal noise during hand-turning throughout assembly; output shaft can be turned by hand after housing is closed.
- [ ] No-load current ≤ first article baseline × 1.2 (engineering suggestion); baseline value recorded and affixed to housing.
- [ ] Backlash quantified and documented: fix the motor end, measure the output end's angular play (using encoder readings or an angle gauge).
- [ ] Module total weight measured and recorded; compare with the mass budget from the M01 specification table and write back.
- [ ] Hardware list includes +15% loss margin; assembly photos and issue records archived.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Joint overheating, high no-load current | Printing warpage causing coaxiality error / excessive bearing preload | Loosen housing screws and hand-turn segment by segment to locate; disassemble and check mating surface flatness |
| Housing cracks when pressing in bearing | Excessive interference, insufficient wall thickness | Redesign for transition fit and reprint; press in with vise at constant speed, no hammering |
| Motor won't turn, smells burnt | Screw too long, punctured winding | Power off and disassemble; check thread engagement depth, replace with shorter screw |
| Screws loosen after a few days of operation | No threadlocker/spring washer used, vibration loosening | Disassemble and apply threadlocker; mark critical screws with anti-loosening witness lines for visual inspection |
| Early wear of cycloidal disc, debris present | Insufficient lubrication / poor tooth surface print quality | Clean and re-grease; check layer height and flow calibration, reprint if necessary |
| Encoder reading drift or jitter | Bracket deformation causing magnet gap variation | Re-measure gap and coaxiality (M04 three essentials); reinforce bracket and reprint |

## Companion Reading

- Previous task: [M04 · Drive, Sensing, and Wiring](m04-driver-sensing-wiring.md)
- Next task: [M06 · Firmware Flashing and Calibration](m06-firmware-calibration.md)
- Manuals: [Actuator Selection Manual](../playbooks/actuator-selection.md) · [Sensor Selection Manual](../playbooks/sensor-selection.md)
- Theoretical background: [Chapter 3 Key Materials](/wiki/chapters/chapter-03/), [Chapter 10 Manufacturing Process System](/wiki/chapters/chapter-10/), [Chapter 11 Assembly, Integration, and Testing](/wiki/chapters/chapter-11/)
- [Stage 1 Overview](../stage-1-actuator.md) · [Roadmap Overview](../index.md)
