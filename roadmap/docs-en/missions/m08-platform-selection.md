# M08 · Platform Selection and Procurement: Choosing the Right Platform, Half the Battle Won

**Global Position**: This is the first hands-on task of [Stage 2 Biped Platform](../stage-2-biped.md), building on the joint-level experience from Stage 1 (M01–M07). The inputs are the task specification and metrics table from M01 + your budget ceiling, and the output is **a selected open-source platform + a verified BOM procurement list**—downstream M09 full assembly will directly follow the procurement results of this task. The cost of choosing the wrong platform is thousands of dollars and months of time.

**Prerequisites**: The metrics table from [M01 · Quantifying Requirements Scenarios](m01-scenario-to-specs.md) is completed; you have read the solution comparison and decision tree in [Stage 2 Overview](../stage-2-biped.md) (this task is its detailed, step-by-step version); the budget has a clear upper limit.

**Theoretical Background**: [Chapter 26 Full System Case Studies](/wiki/chapters/chapter-26/), [Chapter 4 Actuators](/wiki/chapters/chapter-04/), and [Chapter 7 Supplier Map](/wiki/chapters/chapter-07/). All platform data on this page is sourced from the `data/roadmap/research/` research files (access date 2026-07-01); items marked "unknown" in the files are retained as is.

## Step 1: Comprehensive Comparison of Candidate Platforms

[What to Do] Go through the five candidate platforms across ten columns of indicators, checking each row (each number is cited from the corresponding research file; items not found are marked "unknown"):

| Platform | Cost (BOM) | Height/Weight | DoF | Actuators | Main Controller | Simulation Stack | Replication Difficulty | License | Documentation Completeness |
|---|---|---|---|---|---|---|---|---|---|
| [ToddlerBot](/entry/ent_robot_system_toddlerbot/) | ~$6,000 (90% spent on motors and computer) | 0.56 m / 3.4 kg | 30 (arm 7×2, leg 6×2, neck 2, waist 2) | ROBOTIS Dynamixel bus servos ×30 (5 models) | Jetson Orin NX 16GB | MuJoCo/MJX + PPO | Low: pure Python/pip install, 3 days assembly for those without hardware experience (verified by paper) | Code MIT; design files non-commercial CC | Documentation site + assembly manual/video/jigs complete |
| [Berkeley Humanoid Lite](/entry/ent_robot_system_berkeley_humanoid_lite/) | US $4,312 / China $3,236 | 0.8 m / 16 kg | 22 (leg 6×2, arm 5×2) | Custom 6512/5010 quasi-direct drive ×22 (3D printed cycloidal reducer) | Intel N95 mini PC (~$129) | Isaac Lab (URDF/MJCF/USD complete) | Medium: need to build 22 actuators, solder CAN, flash FOC firmware | Code MIT; CAD CC BY-SA 4.0 | GitBook + technical report with complete BOM |
| [Upkie](/entry/ent_robot_system_upkie/) (wheeled-legged) | ~$3,000 + 60 hours printing | Unknown (varies by configuration) | 6 (per leg: hip, knee, wheel) | mjbots qdd100 ×4 + moteus drive wheels | Raspberry Pi 4 + pi3hat | PyBullet (built-in PID/MPC/RL balance examples) | Low: wheeled-legged avoids pure walking tuning hell | Apache-2.0 (wheel mesh CC BY 4.0) | Step-by-step build guide + active community |
| [BRUCE](/entry/ent_robot_system_bruce/) | ~$6.5K (third-party paper estimate, official inquiry-based pricing) | 70 cm / 4.8 kg | 16 (leg 5×2, arm 3×2) | Koala BEAR quasi-direct drive (250 g, peak 10.5 N·m, knee liquid cooling) | 6 TOPS compute board | Variable period MPC (model used as benchmark by third-party papers) | High: full robot frame not publicly available, only commercial procurement | Component-level open source (PyBEAR etc.), full robot license unverified | Professional-oriented, few beginner tutorials |
| [OpenLoong](/entry/ent_robot_system_openloong/) | Unknown (reference design not sold directly) | 185 cm / 80 kg+ | 43 (including five-fingered dexterous hand) | Primarily rotary actuators (specific models unknown) | 400 TOPS controller | Full-stack open-source MPC+WBC on MuJoCo (can learn with zero hardware) | Not suitable for individual replication (institutional-level conditions) | Code Apache-2.0; hardware license marked NOASSERTION | Chinese engineering documentation, delivery-oriented not teaching |

(Data sources: toddlerbot.md, berkeley-humanoid-lite.md, upkie.md, bruce-westwood.md, openloong-qinglong.md.)

[Why] Among the ten columns, the four that truly determine success or failure are: **Cost** (can you afford it), **Replication Difficulty** (can you build it), **Actuator Solution** (whether you need to touch a soldering iron and FOC; physical background see [Quasi-Direct Drive Actuator](/entry/ent_technology_quasi_direct_drive_actuator_2024/) card), and **Simulation Stack** (determines how smoothly M11–M13 go—[MuJoCo](/entry/ent_software_mujoco_physics_engine_2022/) is lightweight and free, [Isaac Lab](/entry/ent_software_nvidia_isaac_lab_2024/) requires an NVIDIA GPU). BRUCE and OpenLoong are included in the table as reference points: one shows you "what high dynamics costs," the other shows you "why a full-size robot can't be replicated at home."

[How to Analyze Your Situation] Copy the above table into your own comparison table, adding two columns: **My Final Price** (including tax and shipping) and **My Capability Match**. For capability match, self-assess based on the actuator solution: if you have no experience with soldering and firmware flashing, mark the "Custom QDD" row red; if you don't have an NVIDIA GPU, mark the Isaac Lab column red.

## Step 2: Decision Tree—Budget → Hands-on Ability → Goal

[What to Do] Three-level decision, converging layer by layer:

```
Level 1 (Budget):
  < $3.5k  → Upkie (~$3,000, upkie.md), minimal crash cost, learn balance control first
  $3.5–7k  → Go to Level 2
  Institutional budget → Only then consider BRUCE (inquiry-based pricing) or finished robot ROBOTIS OP3 ($13,764.35, robotis-op3-darwin-op.md)
Level 2 (Hands-on Ability):
  Zero experience/pure software background → ToddlerBot: servo bus, no FOC tuning needed, mainly screwdriving and plugging cables
  Has 3D printing + soldering + embedded experience → Berkeley: China price $3,236 for 22 DoF, cost is building 22 actuators yourself
Level 3 (Goal):
  Quick positive feedback, learn balance control/RL deployment → Upkie
  Walking + loco-manipulation data collection → ToddlerBot
  RL motion control research → Berkeley (Isaac Lab pipeline ready)
  High dynamics (running/jumping) research → BRUCE (institutional procurement, software license needs confirmation with supplier)
  Full-size control stack learning → OpenLoong-Dyn-Control (MuJoCo, zero hardware, no cost for full robot)
```

Then use the **Five-Item Self-Checklist** to find your match:

| Self-Check Item | Your Answer | Points To |
|---|---|---|
| Budget ceiling | < $3.5k | Upkie |
| Budget ceiling | $3.5–7k | ToddlerBot or Berkeley (decided by next four rows) |
| Weekly available hours | < 5 h | ToddlerBot (most hand-holding documentation); Berkeley printing ~1 week + assembly ~3 days (berkeley-humanoid-lite.md) |
| 3D printer | No | Use online printing service; note Upkie requires 60+ hours printing (upkie.md) |
| GPU | No NVIDIA GPU | MuJoCo route (ToddlerBot / OpenLoong examples); Isaac Lab route requires RTX-class GPU |
| Soldering experience | None | Servo bus platform (ToddlerBot); Berkeley requires soldering CAN, flashing firmware |

[Why] The core KPI for the first biped robot is "getting it to walk," not achieving everything at once. The order of the decision tree is deliberate: budget is a hard constraint to cut first, hands-on ability is the main cause of failure second, and goals are only used to sort among remaining options—those who choose in reverse (looking at goals first) mostly get stuck on "can afford but can't build."

[How to Analyze Your Situation] The row where all five items are checked is your platform; if two or more items are not met, drop down one level, don't force it. Especially, don't use "learning to solder on the side" as a reason to choose Berkeley—the learning cost will stack on top of assembly risk. The lessons from both robots (ToddlerBot paper's reproducibility experiment, Berkeley's self-rated beginner-friendliness 3.5/5) point to the same conclusion: choose conservatively for the first one.

## Step 3: Licensing and Compliance Verification

【What to Do】Distinguish between the two types of licenses, and verify platform by platform (all quoting the original archive text):

- **Code license vs. design file license** are two different things. [ToddlerBot](/entry/ent_robot_system_toddlerbot/): Code and documentation are MIT, design files (Onshape, STL) are **non-commercial** CC license (toddlerbot.md) — replicating for personal use is fine, selling complete machines/kits crosses the line.
- [Berkeley Humanoid Lite](/entry/ent_robot_system_berkeley_humanoid_lite/): Code is MIT, CAD and other assets are CC BY-SA 4.0 (berkeley-humanoid-lite.md) — can be modified and used commercially, but must provide attribution + share derivative works under the same terms.
- [Upkie](/entry/ent_robot_system_upkie/): Apache-2.0 (upkie.md); [ODRI Bolt](/entry/ent_robot_system_odri_bolt/): BSD-3-Clause (open-dynamic-robot-initiative.md) — the most permissive tier.
- [InMoov](/entry/ent_robot_system_inmoov/): Printed parts are CC BY-NC 3.0 (non-commercial) (inmoov.md); [Poppy Humanoid](/entry/ent_robot_system_poppy_humanoid/): Hardware is CC BY-SA 4.0, software is GPLv3 (poppy-humanoid.md).
- [OpenLoong Qinglong](/entry/ent_robot_system_openloong/): Code is Apache-2.0, but the hardware repository license is marked as NOASSERTION by GitHub (terms unclear) (openloong-qinglong.md) — ask the community first before using its hardware drawings.

【Why】"Open source" does not equal "commercially usable": The NC (non-commercial) clause blocks all revenue-generating scenarios; SA (share-alike) requires your modifications to remain open; GPLv3 can infect accompanying software. If you have commercial intent (even just taking orders to assemble for others), you must read the license thoroughly. For certification and compliance frameworks on the path to productization, see [Chapter 12: Certification Compliance and Quality Standards](/wiki/chapters/chapter-12/).

【How to Analyze Your Situation】Pure learning/personal use: All five platforms are green light; doing courses/paid demonstrations: Avoid NC clauses (ToddlerBot design files, InMoov); planning productization: Prioritize BSD/Apache types (Upkie, ODRI). Write the verification conclusion as a one-page document for archiving — just four lines: date, license name, your intended use, and conclusion.

## Step 4: BOM Verification and Ordering

【What to Do】Verify item by item from the official BOM, and create a four-column ledger: **Specification / Quantity / Landed Cost (incl. tax & shipping) / Lead Time**. Four rules:

1. **Spend money where it matters**: Motors and computers account for the bulk of the cost — ToddlerBot's BOM spends about 90% on motors and computers (toddlerbot.md); a single Berkeley unit with 6512 actuators costs $157 (China)–$188 (US) in BOM, and just 10 units of 6512 cost $1,570–$1,880 (berkeley-humanoid-lite.md). Cut the budget in the right places, don't skimp on fasteners.
2. **Out-of-stock replacement verification process**: List key parameters and compare item by item — for motors, check KV value/size/rated torque; for servos, check torque/voltage/communication protocol; for batteries, check cell count/capacity/discharge rate. If any parameter doesn't match, mark it as "**Must confirm with supplier**" — never order on assumption.
3. **Order electromechanical and structural parts separately**: Motors/main controllers/batteries with long lead times should be locked in first; printed parts/bearings/fasteners can be supplemented while reviewing assembly documentation.
4. **Total cost +15% buffer for waste** (M01 rule, engineering recommendation): Failed prints, crushed terminals, broken servos all come from this buffer.

【Why】The BOM is an ideal list from a paper; when you order, there will inevitably be stockouts and price increases. The four-column ledger exposes "overspending" before you order, not halfway through assembly. Lead time is the first hidden cost — THORMANG3 distributor quotes a 12-week delivery time (thormang3.md), and popular motors for personal platforms can be out of stock for a month.

【How to Analyze Your Situation】For domestic replication of Berkeley, purchase directly according to the China BOM cost ($3,236) from the technical report (berkeley-humanoid-lite.md); for cross-border items (Dynamixel, qdd100), include customs duties and shipping in the landed cost. For any item in the ledger with a lead time > 2 weeks, lock in the order on the same day — don't wait to "think it over."

## Step 5: Tools, Consumables, and Workspace Preparation

【What to Do】

- **Tool List**: 3D printer or online printing service (functional part material/infill consistent with official specs — Berkeley cycloidal gears can use standard desktop FDM + PLA, officially tested for 60 hours of durability, berkeley-humanoid-lite.md; Upkie requires 60+ hours of printing, upkie.md), temperature-controlled soldering iron, multimeter, crimping tool, wire stripper, hot glue gun, torque screwdriver; hoisting fixture plan (M09 first power-on and standing/walking acceptance both require it).
- **Consumables**: Wires (silicone wire, select gauge by current), terminals and connectors, bearing and fastener kit (directly reuse M05 specification experience), heat shrink tubing, zip ties, thread-locking adhesive. Better to have too many small parts than too few.
- **Workspace and LiPo Storage**: Dedicated workbench; store LiPo in explosion-proof bags/fireproof containers, charge only when attended. See specifications in [Lithium Battery Tech Card](/entry/ent_tech_li_battery_humanoid/) — a 6S 4000 mAh battery short circuit has enough energy to ignite desktop clutter (Stage 2 safety red line).

【Why】The number one reason for assembly interruptions is not technical issues, but "missing one roll of wire, missing one pack of terminals" — waiting three days for delivery; LiPo storage is a safety prerequisite, not an afterthought.

【How to Analyze Your Situation】No printer: First send the print files to an online printing service for a prototype set (specify material and infill consistent with official specs) — cheaper than buying a printer; only buy tools needed for this task; for the hoisting fixture, start with a gantry frame + straps for a simple version.

## Acceptance Criteria

- [ ] Platform selection has a written rationale: Check each of the five decision steps, able to explain "why this one, why not the other two."
- [ ] BOM ledger has 100% of items in stock, or out-of-stock replacements have parameter comparison records (items that don't match marked "Must confirm with supplier").
- [ ] Total cost ≤ budget limit, and includes +15% waste buffer; motor and computer cost share has been calculated separately.
- [ ] License verification conclusion is documented: Code license and design file license recorded separately, with a clear conclusion for commercial intent.
- [ ] Tool/consumable list has been checked, LiPo storage container is in place.
- [ ] Key long-lead-time items have been ordered, delivery plan aligns with M09 start date.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Stuck mid-assembly due to missing parts | Underestimated lead time, long-lead items not ordered first | Sort ledger by lead time, lock in items > 2 weeks on the same day |
| Replacement motor can't drive or burns the board | Only compared price, not parameters | Go back to Step 4 for item-by-item key parameter comparison; mark uncertain items "Must confirm with supplier" |
| Repeatedly reordering terminals/wires/bearings | Only ordered BOM major items, missed small parts | Buy all consumables at once per Step 5 list; better to have too many than too few |
| Preparing for commercial use, community warns of infringement | Only saw "open source," didn't read the license | Go back to Step 3: NC-licensed platforms are not for commercial use; document the conclusion |
| Chosen platform can't be assembled | Aimed too high, misjudged hands-on ability | Go back to Step 2 for five self-checks; downgrade if two are not met |
| Total cost exceeds budget by 30%+ | Missed customs/shipping/waste costs | Landed cost = incl. tax & shipping; add 15% buffer before comparing to budget |

## Companion Reading

- Previous Task: [M07 · Bench Testing and Acceptance](m07-bench-acceptance.md)
- Next Task: [M09 · Full Assembly, Wiring, and Power](m09-mechanical-assembly.md)
- [Stage 2 Overview](../stage-2-biped.md) · [Compute Platform Selection Playbook](../playbooks/compute-selection.md)
- Theoretical Background: [Chapter 7: Supplier Map](/wiki/chapters/chapter-07/) and [Appendix D: Supplier Directory](/wiki/appendices/appendix-d/), [Chapter 26: Full System Case Studies](/wiki/chapters/chapter-26/), [Chapter 12: Certification Compliance and Quality Standards](/wiki/chapters/chapter-12/)
