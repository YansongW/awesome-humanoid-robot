# M08 · Platform Selection and Procurement: Choosing the Right Platform, Half the Battle Won

**Global Position**: This is the first hands-on task of [Stage 2 Biped Platform](../stage-2-biped.md), building on the joint-level experience from Stage 1 (M01–M07). The inputs are the task specification and metrics table from M01 + your budget ceiling, and the output is **a selected open-source platform + a verified BOM procurement list**—downstream M09 full assembly will directly follow the procurement results of this task. The cost of choosing the wrong platform is thousands of dollars and months of time.

**Prerequisites**: The metrics table from [M01 · Quantifying Requirements Scenarios](m01-scenario-to-specs.md) is filled; you have read the solution comparison and decision tree in [Stage 2 Overview](../stage-2-biped.md) (this task is its detailed, step-by-step expansion); the budget has a clear upper limit.

**Theoretical Background**: [Chapter 26 Full System Case Studies](/wiki/chapters/chapter-26/), [Chapter 4 Actuators](/wiki/chapters/chapter-04/), and [Chapter 7 Supplier Map](/wiki/chapters/chapter-07/). All platform data on this page is sourced from [public research archives](https://github.com/YansongW/awesome-humanoid-robot/tree/main/data/roadmap/research/) (accessed 2026-07-01). Items marked "unknown" in the archives are retained as is.

## Step 1: Comprehensive Comparison of Candidate Platforms

[What to do] Go through the five candidate platforms across ten columns of indicators, checking row by row (each number is cited from the corresponding research archive; items not found are marked "unknown"):

| Platform | Cost (BOM) | Height/Weight | DoF | Actuators | Main Controller | Simulation Stack | Replication Difficulty | License | Documentation Completeness |
|---|---|---|---|---|---|---|---|---|---|
| [ToddlerBot](/entry/ent_robot_system_toddlerbot/) | ~$6,000 (90% spent on motors and computer) | 0.56 m / 3.4 kg | 30 (Arm 7×2, Leg 6×2, Neck 2, Waist 2) | ROBOTIS Dynamixel bus servos ×30 (5 models) | Jetson Orin NX 16GB | MuJoCo/MJX + PPO | Low: Pure Python/pip install, 3 days for someone with no hardware experience (verified by paper) | Code MIT; Design files Non-commercial CC | Documentation site + assembly manual/video/jigs complete |
| [Berkeley Humanoid Lite](/entry/ent_robot_system_berkeley_humanoid_lite/) | US $4,312 / China $3,236 | 0.8 m / 16 kg | 22 (Leg 6×2, Arm 5×2) | Custom 6512/5010 quasi-direct drive ×22 (3D printed cycloidal reducer) | Intel N95 Mini PC (~$129) | Isaac Lab (URDF/MJCF/USD complete) | Medium: Requires building 22 actuators, soldering CAN, flashing FOC firmware | Code MIT; CAD CC BY-SA 4.0 | GitBook + technical report with complete BOM |
| [Upkie](/entry/ent_robot_system_upkie/) (Wheeled Leg) | ~$3,000 + 60 hours printing | Unknown (varies by configuration) | 6 (Per leg: hip, knee, wheel) | mjbots qdd100 ×4 + moteus drive wheels | Raspberry Pi 4 + pi3hat | PyBullet (built-in PID/MPC/RL balance examples) | Low: Wheeled leg avoids pure walking tuning hell | Apache-2.0 (Wheel mesh CC BY 4.0) | Step-by-step build guide + active community |
| [BRUCE](/entry/ent_robot_system_bruce/) | ~$6.5K (third-party paper estimate, official price upon inquiry) | 70 cm / 4.8 kg | 16 (Leg 5×2, Arm 3×2) | Koala BEAR quasi-direct drive (250 g, peak 10.5 N·m, liquid-cooled knee) | 6 TOPS compute board | Variable period MPC (model used as benchmark by third-party papers) | High: Full robot frame not public, only commercial procurement | Component-level open source (PyBEAR, etc.), full robot license unverified | For professional users, few beginner tutorials |
| [OpenLoong Qinglong](/entry/ent_robot_system_openloong/) | Unknown (reference design not sold directly) | 185 cm / 80 kg+ | 43 (including 5-finger dexterous hand) | Primarily rotary actuators (specific model unknown) | 400 TOPS controller | Full-stack open source MPC+WBC on MuJoCo (can learn with zero hardware) | Not suitable for individual replication (institutional-level conditions) | Code Apache-2.0; Hardware license marked NOASSERTION | Chinese engineering documentation, delivery-oriented not teaching-oriented |

(Data sources: toddlerbot.md, berkeley-humanoid-lite.md, upkie.md, bruce-westwood.md, openloong-qinglong.md.)

[Why] Among the ten columns, the four that truly determine success or failure are: **Cost** (can you afford it), **Replication Difficulty** (can you build it), **Actuator Solution** (whether you need to touch a soldering iron and FOC; see the [Quasi-Direct Drive Actuator](/entry/ent_technology_quasi_direct_drive_actuator_2024/) card for physics background), and **Simulation Stack** (determines whether M11–M13 will go smoothly—[MuJoCo](/entry/ent_software_mujoco_physics_engine_2022/) is lightweight and free, [Isaac Lab](/entry/ent_software_nvidia_isaac_lab_2024/) requires an NVIDIA GPU). BRUCE and Qinglong are placed in the table as reference points: one tells you "what high dynamics costs," the other tells you "why a full-size robot cannot be replicated at home."

[How to analyze your situation] Copy the table above into your own comparison table, adding two columns: **My landed cost** (including tax and shipping) and **My capability match**. For capability match, self-assess based on the actuator solution: if you have no experience with soldering and firmware flashing, mark the "Custom QDD" row red directly; if you don't have an NVIDIA GPU, mark the Isaac Lab column red directly.

## Step 2: Decision Tree — Budget → Hands-on Ability → Goal

[What to do] Three-level decision, converging layer by layer:

```
Level 1 (Budget):
  < $3.5k  → Upkie (~$3,000, upkie.md), minimal crash cost, learn balance control first
  $3.5–7k  → Go to Level 2
  Institutional budget → Only then consider BRUCE (price upon inquiry) or finished robot ROBOTIS OP3 ($13,764.35, robotis-op3-darwin-op.md)
Level 2 (Hands-on Ability):
  Zero experience / pure software background → ToddlerBot: servo bus, no FOC tuning needed, mainly screwing and plugging cables
  Has 3D printing + soldering + embedded experience → Berkeley: China price $3,236 for 22 DoF, cost is building 22 actuators yourself
Level 3 (Goal):
  Fast positive feedback, learn balance control/RL deployment → Upkie
  Walking + loco-manipulation data collection → ToddlerBot
  RL motion control research → Berkeley (Isaac Lab pipeline ready)
  High dynamics (running/jumping) research → BRUCE (institutional procurement, software license needs confirmation with supplier)
  Full-size control stack learning → OpenLoong-Dyn-Control (MuJoCo, zero hardware, no cost for the whole robot)
```

Then use the **five-item self-check list** to find your match:

| Self-check Item | Your Answer | Points To |
|---|---|---|
| Budget ceiling | < $3.5k | Upkie |
| Budget ceiling | $3.5–7k | ToddlerBot or Berkeley (decided by rows below) |
| Weekly available hours | < 5 h | ToddlerBot (most hand-holding documentation); Berkeley printing ~1 week + assembly ~3 days (berkeley-humanoid-lite.md) |
| 3D printer | — | Use online printing service; note Upkie requires 60+ hours printing (upkie.md) |
| GPU | No NVIDIA GPU | MuJoCo route (ToddlerBot / OpenLoong examples); Isaac Lab route requires RTX-class GPU |
| Soldering experience | — | Servo bus platform (ToddlerBot); Berkeley requires soldering CAN, flashing firmware |

[Why] The core KPI for the first biped is "getting it to walk," not achieving everything at once. The order of the decision tree is deliberate: budget is a hard constraint, so it's cut first; hands-on ability is the main cause of failure, so it's next; the goal is only used to sort among the remaining options—those who choose in reverse order (looking at the goal first) mostly get stuck at "can afford but can't build."

[How to analyze your situation] The row where all five items are checked is your platform; if two or more items are not met, drop down one level, don't force it. Especially, don't use "learning to solder on the side" as a reason to choose Berkeley—the learning cost will compound with the assembly risk. The lessons from both machines (ToddlerBot paper's reproducibility experiment, Berkeley's self-rated beginner-friendliness of 3.5/5) all point to the same conclusion: choose conservatively for the first one.

## Step 3: License and Compliance Check

【What to Do】Distinguish between two types of licenses, check each platform (all quoting original archive text):

- **Code license vs. design file license** are two different things. [ToddlerBot](/entry/ent_robot_system_toddlerbot/): Code and documentation MIT, design files (Onshape, STL) are **non-commercial** CC license (toddlerbot.md) — fine for personal replication, selling complete machines/kits crosses the line.
- [Berkeley Humanoid Lite](/entry/ent_robot_system_berkeley_humanoid_lite/): Code MIT, CAD and other assets CC BY-SA 4.0 (berkeley-humanoid-lite.md) — modifiable and commercial, but requires attribution + derivative works shared under the same terms.
- [Upkie](/entry/ent_robot_system_upkie/): Apache-2.0 (upkie.md); [ODRI Bolt](/entry/ent_robot_system_odri_bolt/): BSD-3-Clause (open-dynamic-robot-initiative.md) — the most permissive tier.
- [InMoov](/entry/ent_robot_system_inmoov/): Printed parts CC BY-NC 3.0 (non-commercial) (inmoov.md); [Poppy Humanoid](/entry/ent_robot_system_poppy_humanoid/): Hardware CC BY-SA 4.0, software GPLv3 (poppy-humanoid.md).
- [OpenLoong](/entry/ent_robot_system_openloong/): Code Apache-2.0, but the hardware repository license is marked as NOASSERTION by GitHub (terms unclear) (openloong-qinglong.md) — ask the community before using its hardware drawings.

【Why】"Open source" does not equal "commercially usable": NC (non-commercial) clauses block all revenue-generating scenarios; SA (share-alike) requires your modifications to remain open; GPLv3 can infect accompanying software. If you have commercial intent (even just taking orders to assemble for others), you must read the license thoroughly; see [Chapter 12: Certification, Compliance, and Quality Standards](/wiki/chapters/chapter-12/) for the certification and compliance framework on the path to productization.

【How to Analyze Your Situation】Pure learning/personal use: all five platforms are green; courses/paid demonstrations: avoid NC clauses (ToddlerBot design files, InMoov); planning productization: prioritize BSD/Apache types (Upkie, ODRI). Document the check conclusion in a one-page file — date, license name, your intended use, and conclusion, four lines are enough.

## Step 4: BOM Verification and Ordering

【What to Do】Verify item by item from the official BOM, create a four-column ledger: **Specification / Quantity / Landed Cost (incl. tax & shipping) / Lead Time**. Four rules:

1. **Spend money where it counts**: Motors and computers account for the bulk of the cost — ToddlerBot's BOM spends about 90% on motors and computers (toddlerbot.md); Berkeley's single unit 6512 actuator BOM costs $157 (China)–$188 (US), just 10 units of 6512 cost $1,570–1,880 (berkeley-humanoid-lite.md). Cut the budget in the right places, don't skimp on fasteners.
2. **Out-of-stock replacement verification process**: List key parameters and compare item by item — for motors check KV value/size/rated torque, for servos check torque/voltage/communication protocol, for batteries check cell count/capacity/discharge rate; if any parameter doesn't match, mark it as "**must confirm with supplier yourself**", don't order on assumptions.
3. **Order electromechanical and structural parts separately**: Motors/main controllers/batteries with long lead times should be locked in first; printed parts/bearings/fasteners can be supplemented while reviewing assembly documentation.
4. **Total cost +15% scrap margin** (M01 rule, engineering recommendation): Failed prints, crushed terminals, broken servos all come from this.

【Why】The BOM is an ideal list from a paper; when you order, there will always be stockouts and price increases. The four-column ledger exposes "overspending" before ordering, not halfway through assembly. Lead time is the first hidden cost — THORMANG3 dealer lead time is 12 weeks (thormang3.md), and popular motors for personal platforms can be out of stock for a month.

【How to Analyze Your Situation】For domestic replication of Berkeley, purchase directly according to the China BOM cost ($3,236) from the technical report (berkeley-humanoid-lite.md); for cross-border items (Dynamixel, qdd100), include customs duties and shipping in the landed cost. For any item with a lead time > 2 weeks in the ledger, lock the order on the same day; don't wait to "think it over."

## Step 5: Tools, Consumables, and Workspace Preparation

【What to Do】

- **Tool List**: 3D printer or online printing service (functional part material/infill consistent with official specs — Berkeley cycloidal gears work with standard desktop FDM + PLA, officially tested for 60 hours, berkeley-humanoid-lite.md; Upkie requires 60+ hours of printing, upkie.md), temperature-controlled soldering iron, multimeter, crimping tool, wire stripper, hot glue gun, torque screwdriver; hoisting plan (M09 first power-on and standing/walking acceptance will both use it).
- **Consumables**: Wire (silicone wire, select gauge by current), terminals and connectors, bearing and fastener kit (directly reuse M05's specification experience), heat shrink tubing, zip ties, threadlocker. Small items: better to have too many than too few.
- **Workspace and LiPo Storage**: Dedicated workbench; store LiPo in explosion-proof bags/fireproof containers, charge only when attended; see [Lithium Battery Technical Card](/entry/ent_tech_li_battery_humanoid/) for specifications — a 6S 4000 mAh battery short circuit has enough energy to ignite desktop clutter (Stage 2 safety red line).

【Why】The number one reason for assembly interruptions is not technical issues, but "missing one roll of wire, missing one pack of terminals" and waiting three days for delivery; LiPo storage is a safety prerequisite, not an afterthought.

【How to Analyze Your Situation】No printer: First send the print files to an online printing service for a prototype set (specify material and infill consistent with official specs), which is cheaper than buying a printer; only buy tools needed for this task; for the hoist, first build a simple version with a gantry frame + straps.

## Acceptance Criteria

- [ ] Platform selection has a written rationale: check off each of the five decision steps, able to explain "why this one, why not the other two."
- [ ] BOM ledger: 100% of items are in stock, or out-of-stock replacements have parameter comparison records (mismatched items marked "must confirm with supplier yourself").
- [ ] Total cost ≤ budget limit, and includes +15% scrap margin; motor and computer cost share has been calculated separately.
- [ ] License check conclusion documented: code license and design file license recorded separately, with a clear conclusion for commercial intent.
- [ ] Tool/consumable list has been inventoried, LiPo storage container is in place.
- [ ] Key long-lead-time items have been ordered, delivery plan aligned with M09 start date.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Stuck halfway due to missing parts | Underestimated lead time, long-lead items not ordered first | Sort ledger by lead time, lock items > 2 weeks on the same day |
| Replacement motor can't drive or burns the board | Only compared price, not parameters | Go back to Step 4 for item-by-item key parameter comparison; mark uncertainties as "must confirm with supplier yourself" |
| Repeatedly reordering terminals/wire/bearings | Only ordered BOM major items, missed small ones | Buy all consumables from Step 5 list at once; better to have too many than too few |
| Preparing for commercial use, community warns of infringement | Only saw "open source," didn't read the license | Go back to Step 3: NC clause platforms are not for commercial use; document the conclusion |
| Chosen platform can't be assembled | Aimed too high, misjudged hands-on ability | Go back to Step 2 for five self-checks; downgrade if two are not met |
| Total cost exceeds budget by 30%+ | Missed customs/shipping/scrap costs | Landed cost = incl. tax & shipping; add 15% margin before checking against budget |

## Companion Reading

- Previous task: [M07 · Bench Testing and Acceptance](m07-bench-acceptance.md)
- Next task: [M09 · Full Assembly, Wiring, and Power](m09-mechanical-assembly.md)
- [Stage 2 Overview](../stage-2-biped.md) · [Compute Platform Selection Playbook](../playbooks/compute-selection.md)
- Theoretical background: [Chapter 7: Supplier Map](/wiki/chapters/chapter-07/) and [Appendix D: Supplier Directory](/wiki/appendices/appendix-d/), [Chapter 26: Full System Case Studies](/wiki/chapters/chapter-26/), [Chapter 12: Certification, Compliance, and Quality Standards](/wiki/chapters/chapter-12/)
