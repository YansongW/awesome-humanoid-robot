# M20 · Reliability, Maintenance, and Safety Engineering: Making Machines Last Longer and People Feel Safe to Approach

**Global Position**: The wrap-up and long-term task spanning M09–M19. The input is a complete machine that "can run end-to-end tasks," and the output is three living documents—**Safety Archive, Maintenance Procedures, and Failure Contingency Plan**. This task has no "completed" state: every accident and every change must be written back into these three documents until the machine is retired.

**Prerequisites**: [M19 · End-to-End Task Integration](m19-e2e-task.md) acceptance passed (only if the system can run can we talk about running long); [M14](m14-sim-to-real.md) communication watchdog grading and [M10](m10-urdf-modeling.md) soft limit rules implemented; Stage 2 safety red lines (emergency stop hardwiring, gantry, lithium battery specifications) are always in effect.

Theoretical background: [Chapter 11 Assembly Integration and Testing](/wiki/chapters/chapter-11/) (testing and maintenance system), [Chapter 12 Certification Compliance and Quality Standards](/wiki/chapters/chapter-12/) (standards and certification paths), [Chapter 25 Robot Evaluation System](/wiki/chapters/chapter-25/) (regression evaluation); regulatory standards list see [Appendix E Standards and Regulations](/wiki/appendices/appendix-e/).

## Step 1: FMEA—Write Down "How It Might Break" Before It Breaks

[What to Do] Create a failure mode table, covering at least: falling, joint overheating, CAN/communication interruption, battery failure, structural fracture, perception failure (detection errors/localization drift). Score each item on three dimensions (1–10, engineering convention):

- **S Severity**: How severe the consequences are (injuring a person = 10, breaking a printed part = 3);
- **O Occurrence Probability**: How often it occurs;
- **D Detectability**: How hard it is to detect in advance (with sensor monitoring = low score, no warning = high score);

```
RPN = S × O × D
```

Sort by RPN, and write **mitigation measures for the Top 5 items one by one** (design changes / monitoring alerts / operating procedures).

[Why] The value of FMEA is prioritization: hobby projects have limited resources; RPN tells you "which failures are both severe and hard to detect," so you spend your protection budget there. "Joint overheating" usually has high O and low D (when no temperature monitoring is installed)—a cheap thermistor monitor can knock it off the top list. See [Chapter 11](/wiki/chapters/chapter-11/) and [Chapter 12](/wiki/chapters/chapter-12/) for methodology.

[How to Analyze in Your Case] If you're unsure about scoring, use three levels (1/4/8) for rough scoring; the point of FMEA is relative ranking, not absolute precision. The table must include "things that actually happened": record every crash, board burn, and communication interruption during the M14–M19 debugging period—your historical record is the most accurate source of O values.

## Step 2: Protection Mechanism Checklist and Actual Testing—Protection Doesn't Exist in Code, It Exists in Test Records

[What to Do] Establish and **verify through actual testing** each item (default is non-existent; only counts if tested):

| Protection Mechanism | Rule | Actual Testing Method |
|---|---|---|
| Soft Limits | 5–10° smaller than mechanical hard limits ([M10](m10-urdf-modeling.md) rule), written into the driver, not just in the host computer | Send out-of-range commands while powered on; they should be rejected; manually move to hard limits with power off to confirm margin |
| Current Limiting + I²t Thermal Protection | Peak current time-limited; continuous current derated by I²t integral | Bench stall test, record trigger time |
| Temperature Derating | Linear derating when motor/drive temperature exceeds threshold; disable if higher | Block airflow and run under load, observe derating curve activation |
| Communication Watchdog | Timeout grading: first damping/force reduction, then disable ([M14](m14-sim-to-real.md) grading) | **Cable pull test**: pull CAN/network cable during operation and observe response |
| Emergency Stop | [Emergency Stop System](/entry/ent_component_emergency_stop_system_2024/) hardwired to cut power, independent of all software | Press and time (Stage 3 criterion <1 s); reset requires manual confirmation |
| Independent Safety Layer | Safety logic on [Safety MCU](/entry/ent_component_safety_mcu/): can still cut power when main controller crashes | Force power-off/simulate crash of main controller, verify safety MCU takes over |

[Why] Software protection shares a common failure premise: the main controller is still alive. Stage 2 safety red lines require the emergency stop to be independent of the software chain, forced by the failure mode "main controller crash"; the [Safety MCU](/entry/ent_component_safety_mcu/) card extends this principle to all safety monitoring (functional safety standard background see the card and [Chapter 12](/wiki/chapters/chapter-12/)). Each protection is "actually tested" rather than "assumed" because protection circuit failures are silent—without testing, you always think it's working.

[How to Analyze in Your Case] Desktop small platforms can simplify (independent hardware power switch replaces full emergency stop circuit, per Stage 3 Step 15); platforms that can injure people when falling must have all six items. Test records go into the safety archive: date, method, result, retest cycle.

## Step 3: Electrical and Battery Safety Procedures—No Luck with LiPo

[What to Do] Write the lithium battery procedure on one page and post it in the charging area (based on [Humanoid Robot Lithium-Ion Battery System](/entry/ent_tech_li_battery_humanoid/) and [Battery Management System](/entry/ent_component_battery_management_system/) cards):

1. **Charging Attendance**: Someone must be present throughout LiPo charging; use explosion-proof bags/fireproof containers, away from flammable materials;
2. **Retirement Rule**: Over-discharged, swollen, dropped, or water-damaged batteries **must be retired immediately**—no observation, no luck;
3. **Storage Charge**: Store at storage charge (approx. 3.8–3.85 V/cell, industry common practice; verify with your battery specification sheet) for long-term non-use; check monthly;
4. **Transport Regulations**: Follow lithium battery dangerous goods rules for cross-region transport (airlines have watt-hour limits; check the carrier's latest regulations before travel);
5. **Insulation Check**: Regularly measure insulation and polarity of the power distribution system—must be done after drops or disassembly; review BMS alarm records monthly.

[Why] Lithium battery thermal runaway is the only risk in hobby robot projects that could "burn down a house"; its precursors (swelling, increased internal resistance, drop damage) are observable, and the essence of the procedure is "see it, then execute it." Stage 2 safety red lines list "battery charging and storage must comply with lithium battery safety specifications" as a power-on prerequisite; this step refines it into daily actions. Compliance background see [Chapter 12](/wiki/chapters/chapter-12/) and [Appendix E](/wiki/appendices/appendix-e/).

[How to Analyze in Your Case] Multiple batteries in rotation: create an archive for each (purchase date, cycle count, internal resistance trend); retire those with significantly rising internal resistance first. For 24–48 V bus platforms: write "disconnect battery first, then touch the distribution" into the operating manual—low-voltage DC can also arc; don't plug/unplug live with bare hands.

## Step 4: Maintenance Procedures—Checking Periodically Is Ten Times Cheaper Than Repairing After Failure

[What to Do] Print and post a three-level maintenance checklist:

| Period | Item |
|---|---|
| Daily (before each power-on) | Fastener spot check, wire harness wear and routing, printed part cracks (focus: joint connections), listen for abnormal noise during idle rotation |
| Weekly | Key joint backlash trend (compare to initial marks), no-load current vs M07 bench baseline (investigate if drift >20%, engineering recommended value) |
| Monthly | Battery internal resistance, bearing condition (play/noise), full structural part inspection, emergency stop and watchdog retest |

Spare parts strategy: keep ≥2 sets of common printed parts—inventory parts equal downtime. Anchor: ToddlerBot can withstand about 7 falls, with single repair taking only 21 minutes of printing + 14 minutes of assembly (source: [ToddlerBot Project Homepage](https://toddlerbot.github.io/))—**with spare parts**, repair is at this level; with zero inventory, "one fall means one week of downtime." Maintenance record table: date/item/finding/action/next attention.

[Why] Almost all mechanical failures have precursors: gradually increasing backlash, gradually increasing current, gradually growing cracks—the three-level periodic inspection turns these gradual changes into readable numbers. The maintenance record table is the only data source for trend analysis: a single reading is meaningless; "backlash increasing for three consecutive weeks" points to a specific worn part. System testing and maintenance methods see [Chapter 11](/wiki/chapters/chapter-11/).

[How to Analyze in Your Case] For platforms with many printed parts: take ToddlerBot's "quick repair" as a design goal—make vulnerable parts modular and quick-release; replace, don't repair, when broken. For metal part platforms: shift monthly focus to bolt preload and bearing lubrication. Hang the checklist next to the machine and check off items—a checklist that isn't executed is as good as none.

## Step 5: Logging and Traceability – Making Every Anomaly Reviewable

【What to Do】

1. **Operation Logs**: Temperature, current, fall events, protection triggers (limit switch/watchdog/emergency stop) are automatically written to disk, with unified timestamps across all nodes;
2. **Version Archive**: A single table records the version correspondence among model weights, firmware, parameter configurations, and URDF; any change to any of these writes a new row;
3. **Change Management Discipline**: Change only one variable at a time; after any change, run regression tests – re-execute the 20 fixed protocols from [M18](m18-imitation-learning.md) and the 10 full-chain protocols from [M19](m19-e2e-task.md); the change is considered complete only when the numbers align with the baseline.

【Why】Questions like "Why did the success rate drop from 75% to 60%" can only be answered with a version correspondence table plus regression protocols; anomalies without logged data are equivalent to never having occurred – protection trigger records are also the source for calibrating the O value in Step 1 FMEA. Changing only one variable at a time is the sole discipline that distinguishes "improvement" from "regression" (same as M18 Step 6).

【How to Analyze Your Situation】Don't over-engineer the logging solution: [ROS 2](/entry/ent_software_ros_2_middleware_2024/) bag + a version table (Markdown or spreadsheet) is sufficient for personal projects. The key is to start recording from today – a traceability system can only record the future, not make up for the past.

## Step 6: Documentation and Handover – It's Not Done Until Someone Else Can Take Over

【What to Do】Produce and continuously update three documents + one update mechanism:

1. **Safety Archive**: FMEA table, risk assessment, emergency stop/watchdog test records, incident records (time/phenomenon/cause/remediation);
2. **Operation Manual**: Startup checklist (battery level/fasteners/environment/gantry/emergency stop at hand), shutdown checklist (unload power/disconnect battery/battery disposal/storage posture), emergency response (what to do for fire/loss of control/pinch injury respectively);
3. **Newcomer Onboarding Path**: Which pages to read in order ([Roadmap Overview](../index.md) → Stage 2 Safety Red Lines → this page), which tests to follow (emergency stop actual test, watchdog cable pull, no-load power-on) before being allowed to operate independently;
4. **OTA Prototype**: [OTA Software Update](/entry/ent_technology_ota_software_update_2024/) with version management and rollback – A/B partition or equivalent mechanism, check battery level before update, retain a serial recovery channel (consistent with Stage 3 Step 15 and common pitfalls).

【Why】The only acceptance criterion for safety documentation is "a third party can understand it, dare to operate it, and trace back after an accident"; procedures stored only in memory reset to zero at handover (or when you forget everything three months later). OTA solves the daily risk of "changing a strategy requires wiring, and wrong wiring bricks the device"; rollback is its bottom line – OTA without rollback is a remote bricking tool (Stage 3 common pitfall).

【How to Analyze Your Situation】Even for personal projects, write it down: your future self is that "newcomer". Place the documents in the repository alongside the code for version control, update them synchronously with every change; print a separate copy of the safety archive and keep it in the lab, accessible even during power or network outages.

## Acceptance Criteria

- [ ] FMEA table documented: ≥6 failure modes, RPN ranking, Top 5 each with mitigation measures implemented.
- [ ] Six protection mechanisms each have actual test records (including cable pull tests and emergency stop timing), with test dates and retest cycles on file.
- [ ] Lithium battery procedure documented on a single page and posted on the wall; battery archive (cycle count/internal resistance trend) established; retirement rules have execution records.
- [ ] Three-level maintenance checklist has ≥4 weeks of execution records; ≥2 sets of spare consumable printed parts in inventory.
- [ ] Operation logs automatically written to disk; version correspondence table (model/firmware/parameters/URDF) established and has recorded at least one real change.
- [ ] Three documents – safety archive, operation manual, and newcomer path – are written and available for third-party review; OTA rollback mechanism has been tested once.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Limit switch only implemented in upper computer software | Fails when firmware crashes/communication is lost | Move soft limits down to drive firmware; test by manually exceeding limits after power-off |
| Watchdog never triggers | Threshold too wide, effectively non-existent | Test response time by pulling the cable; set threshold to 2–3 times the control cycle (engineering recommendation) |
| One fall stops work for a week | Zero spare parts inventory | Keep ≥2 sets of common consumable printed parts based on ToddlerBot anchor points; archive print parameters with the parts |
| Anomaly cannot be reviewed | Logs not written to disk / timestamps not unified | Synchronize clocks across all nodes; add special markers for protection triggers; review logs weekly |
| Procedures stuck in memory | Not written / written but no one reads | Print documents and post on wall; force newcomers to follow the onboarding path with actual tests |
| OTA fails to boot | No rollback / power loss during update | A/B partition; check battery level before update; practice serial recovery channel once |

## Companion Reading

- Previous Task: [M19 · End-to-End Task Integration](m19-e2e-task.md)
- Theoretical Background: [Chapter 11 Assembly Integration and Testing](/wiki/chapters/chapter-11/), [Chapter 12 Certification Compliance and Quality Standards](/wiki/chapters/chapter-12/), [Chapter 25 Robot Evaluation System](/wiki/chapters/chapter-25/), [Appendix E Standards and Regulations](/wiki/appendices/appendix-e/)
- [Stage 2 Safety Red Lines](../stage-2-biped.md) · [Stage 3 Overview](../stage-3-humanoid.md) · [Roadmap Overview](../index.md)
