# M05 · 3D Printing and Mechanical Assembly: Turning Drawings into Joints That Feel Warm in Your Hands

**Global Position**: After M03 Reducer Design and M04 Electrical Drawings. Input is the reducer/housing drawings, electrical drawings, and a pile of standard parts; output is an **assembled single-joint electromechanical module** — smooth to turn, stable readings, ready to be placed on the test bench for M06 Firmware and M07 Debugging.

**Prerequisites**: M03 Reducer drawings and BOM are frozen; M04 Electrical Drawings (power/signal/bus, three sheets) are finalized; one leveled FDM printer.

Theoretical Background: [Chapter 3: Key Materials](/wiki/chapters/chapter-03/), [Chapter 10: Manufacturing Process System](/wiki/chapters/chapter-10/), [Chapter 11: Assembly, Integration, and Testing](/wiki/chapters/chapter-11/).

## Step 1: Material Selection — First Decide "Which Material for Which Part"

[What to Do] Select materials based on part function and fill in the material column of the BOM:

| Part | First Choice | Alternative/Notes |
|---|---|---|
| Cycloidal Gear/Transmission Part | PLA (high-fill printing) | Berkeley cycloidal gears are all desktop FDM + PLA, passing a 60-hour endurance test (`data/roadmap/research/berkeley-humanoid-lite.md`); advanced use Nylon/PA-CF |
| Housing/End Cap | PETG | Switch to ABS/ASA when close to the motor or requiring higher temperature resistance |
| Bracket/Structural Part | PETG | Switch to PA-CF for high stiffness requirements |
| Buffer Pad/Foot Pad/Limit Pad | TPU | Relies on elasticity; the softer it is, the slower the printing speed needed |

Nylon/PA-CF has high strength and good wear resistance, making it a preferred gear material, but it is **hygroscopic** — it must be dried after opening before printing, otherwise bubbles and filament jams will occur; TPU is soft, first confirm that your extruder can handle it.

[Why] There is no "best" material, only the one "best suited for this part's working conditions": Gears need to be rigid and wear-resistant — the cycloidal structure shares the load across multiple teeth, so even PLA printed parts can handle it. This is precisely why cycloidal [quasi-direct drive actuators](/entry/ent_technology_quasi_direct_drive_actuator_2024/) dare to use plastic gears (berkeley-humanoid-lite archive); housings need toughness (resistant to cracking from assembly bumps or drops); pads need to be soft. For a system map of materials, see [Chapter 3: Key Materials](/wiki/chapters/chapter-03/).

[How to Analyze Your Situation] First time: Copy Berkeley's all-PLA approach to get the process running smoothly; if the joint is close to the motor and runs continuously at high temperature, switch the housing to ASA; only consider PA-CF when batch consistency is required — it demands a significantly higher level of machine and drying capability.

## Step 2: Printing Process Parameters

[What to Do] The following parameters are engineering recommended starting points; adjust and record based on your machine and material: 0.4 mm nozzle; layer height 0.12–0.2 mm; outer walls ≥ 4 layers; infill 40–60% (use high infill, even 100%, for functional gear parts). One principle for orientation: **Layer line direction ⊥ Main load direction** — print the cycloidal disc flat so the tooth surfaces are formed in the XY plane. Add supports for overhangs > 60°; three methods for warping control: bed temperature per material recommendation, brim 5–8 mm, enclose the printer for ABS/ASA.

[Why] FDM parts are anisotropic: the interlayer bond is the weakest direction, and stress tearing along the layer lines is a classic failure mode; printing the cycloidal disc flat changes the root stress from "cross-layer transfer" to "in-plane transfer". Wall count determines strength more than infill percentage — a part with 4 walls + 40% infill is generally more durable than one with 2 walls + 80% infill (process rule, engineering experience). For a systematic discussion of manufacturing processes, see [Chapter 10: Manufacturing Process System](/wiki/chapters/chapter-10/).

[How to Analyze Your Situation] For new materials, first print a temperature tower and flow calibration part; for functional gear parts, print one individually for a meshing test before batch production. Don't throw away failed prints; weigh them and record the loss — this is exactly what the 15% loss margin established in M01 is for.

## Step 3: Tolerances and Fits

[What to Do] First, accept reality: Desktop FDM dimensional accuracy is in the ±0.1–0.3 mm range (varies by machine, material, and orientation; requires your own trial calibration). Three countermeasures:

1.  **Trial Fit Block Calibration**: Print a set of trial fit blocks with increasing hole diameters (nominal +0.05/+0.10/+0.15/+0.20 mm), measure the actual offset of your machine for each type of fit, and record the conclusions in the drawing notes;
2.  **Bearing Housing**: Design for transition to light interference fit; trial fit printed parts before batch production; press in using a vise/press tool at a constant speed; hammers are prohibited;
3.  **Shaft-Hole**: Use clearance fit with 0.1–0.2 mm allowance (determined by trial fit blocks); use a **heat-set insert** with a constant-temperature soldering iron pressed vertically; directly printed threaded holes are only suitable for non-load-bearing applications.

Process solidification: First article trial assembly → Mold modification → Small batch → Full inspection of critical dimensions.

[Why] Fits are the interface between two worlds: "printed parts" and "machined standard parts". Bearings, shafts, and pins have micron-level precision; printed parts have sub-millimeter precision. Not trial fitting before batch production = batch scrap. Heat-set inserts embed metal threads into plastic, providing the only reliable solution for repeated disassembly in a vibration environment.

[How to Analyze Your Situation] If you don't have a micrometer, use a caliper + trial fit feel: It's good if a bearing can be pushed in mostly by hand and seated with light pressure from a vise; "needs to be hammered in" means the interference is too large; "falls out" means the clearance is too large.

## Step 4: Standard Parts and Procurement

[What to Do] List hardware items according to the M03 BOM, all quantities **×1.15** (loss margin, rule established in M01):

| Category | Selection Key Points |
|---|---|
| Bearings | Thin-section deep groove ball series (68xx/69xx type) to save axial space; inner/outer diameter per drawing; normal clearance is sufficient |
| Fasteners | M3/M4 hex socket screws + spring washers; have medium-strength threadlocker on hand; length based on engagement depth of 1.5–2 times the diameter |
| Shafts | Shaft/pin shafts (concept of h6/g6 tolerance zone); do not use printed holes directly as bearing seats |
| Lubrication | The contact surface of the cycloidal pinwheel *must* be coated with grease; specific type needs independent confirmation; avoid types incompatible with plastic |

Reference scale: Berkeley 6512 single-joint BOM $157–188 includes bearings/fasteners/printed parts (berkeley-humanoid-lite archive) — hardware is cheap, but missing one can halt the entire line. Supplier channels can be found in [Appendix D: Supplier Directory](/wiki/appendices/appendix-d/).

[Why] The pitfalls of standard parts are not "what to buy", but "buying too few" and "buying the wrong length": a screw 2 mm too long might pierce the motor windings; one too short won't get enough thread engagement. The 15% margin is calculated per piece, not per cost — lost, stripped, or broken parts are all small items.

[How to Analyze Your Situation] Place orders aggregated by "number of joints × single-joint BOM"; don't buy fasteners in the rhythm of "let's try one joint first" — shipping costs more than the screws. After receiving, sort by specification into labeled boxes so you don't grab the wrong one during assembly.

## Step 5: Assembly Process — Slow is Fast

[What to Do] Assemble in a fixed sequence, and **manually turn the output shaft** (power off, rotate by hand) after each step:

1.  Reducer sub-assembly: Position cycloidal disc, pins, bearings; apply grease; tighten in a cross-pattern step-by-step;
2.  Turn check: No binding points, no abnormal noise throughout;
3.  Motor into housing: Verify screw length (don't hit windings); route phase wires per M04 drawing;
4.  Encoder centering: Follow the three essentials from M04 (coaxiality, gap, distance from phase wires); double-check before powering on;
5.  Close housing: Tighten screws in a diagonal cross-pattern, in 2–3 steps; bearing preload should be "enough to eliminate axial play but not make turning stiff".

Final actions: Insulation check before powering on; current limit on first power-up; record the **no-load current baseline** (current at rated voltage with no load), write it on a label and stick it on the housing — this is the benchmark for M07 temperature rise and efficiency comparison. For systematic methods of assembly and testing, see [Chapter 11: Assembly, Integration, and Testing](/wiki/chapters/chapter-11/).

[Why] "Turning after each step" minimizes the cost of fault localization: If it binds only after full assembly, you have to disassemble everything; if it binds right after the previous step, the problem is limited to those few parts. Cross-pattern step-by-step tightening prevents housing warping and bearing misalignment — same principle as changing a tire. No-load current is a comprehensive indicator of assembly quality: poor coaxiality, excessive preload, insufficient lubrication — all manifest as increased current.

[How to Analyze Your Situation] If there's a binding point during turning: first loosen the last set of screws installed to see if it disappears, thereby distinguishing between "assembly stress" and "part out-of-tolerance". Endurance expectation management: Berkeley used a 60-hour endurance test to validate PLA cycloidal gears (berkeley-humanoid-lite archive); test your own designed parts at this scale (executed in M07).

## Acceptance Criteria

- [ ] Part-material comparison table documented; printing parameters (layer height/wall count/infill/orientation) recorded and archived.
- [ ] Trial fit block calibration completed; all critical fits (bearing housing, shaft hole) passed trial fitting.
- [ ] No binding or abnormal noise during the entire assembly turning process; output shaft can be turned by hand after closing the housing.
- [ ] No-load current ≤ first article baseline × 1.2 (engineering recommended value); baseline value recorded and attached to the housing.
- [ ] Backlash quantified and documented: Fix the motor end, measure the output end's wobble angle (using encoder reading or angle gauge).
- [ ] Module total weight measured and recorded; compared against the mass budget from the M01 specification table and feedback written.
- [ ] Hardware list includes +15% loss margin; assembly photos and problem records archived.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Joint overheating, high no-load current | Printing warpage causing coaxiality error / excessive bearing preload | Loosen housing screws, turn in sections to locate; disassemble and check mating surface flatness |
| Housing cracks when pressing bearing | Excessive interference, insufficient wall thickness | Re-print with transition fit; press in using a vise at constant speed, no hammering |
| Motor doesn't turn, has burnt smell | Screw too long, pierced windings | Power off, disassemble and inspect; verify engagement depth, replace with shorter screw |
| Screws loosen after a few days of operation | No threadlocker/spring washer used, vibration loosening | Disassemble, inspect, apply threadlocker; draw anti-loosening marking lines on critical screws for visual inspection |
| Early cycloidal disc wear, debris present | Insufficient lubrication / poor tooth surface print quality | Clean, re-grease; check layer height and flow calibration, re-print if necessary |
| Encoder reading drifts or jumps | Bracket deformation causing magnet gap change | Re-measure gap and coaxiality (M03 three essentials); reinforce bracket and re-print |

## Companion Reading

- Previous task: [M04 · Drivers, Sensors, and Wiring](m04-driver-sensing-wiring.md)
- Next task: [M06 · Firmware Flashing and Calibration](m06-firmware-calibration.md)
- Manuals: [Actuator Selection Manual](../playbooks/actuator-selection.md) · [Sensor Selection Manual](../playbooks/sensor-selection.md)
- Theoretical background: [Chapter 3 Key Materials](/wiki/chapters/chapter-03/), [Chapter 10 Manufacturing Process System](/wiki/chapters/chapter-10/), [Chapter 11 Assembly, Integration, and Testing](/wiki/chapters/chapter-11/)
- [Stage 1 Overview](../stage-1-actuator.md) · [Roadmap Overview](../index.md)
