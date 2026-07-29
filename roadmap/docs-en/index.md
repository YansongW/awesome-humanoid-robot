# 0→1 Building a Humanoid Robot: Roadmap Overview

!!! note "Safety is not a disclaimer, it's part of the process"
    This roadmap involves real hardware: lithium batteries, 24–48 V bus bars, kg-level swinging metal structural parts, and joint torques sufficient to pinch fingers when stalled. Safety is not achieved through statements but is built into the process—see [M09 First Power-On Smoke Test](missions/m09-mechanical-assembly.md) for electrical acceptance, [M14 Phased Unlocking](missions/m14-sim-to-real.md) for walking protection, and [M20 Reliability, Maintenance, and Safety](missions/m20-reliability-safety.md) for long-term safety engineering.

## Three Ways to Use This Repository: Look Up, Learn, Build

This repository simultaneously serves as an "atlas," a "book," and a "blueprint." The same concept appears once in each layer, with different responsibilities:

| Usage | Entry Point | When to Use | Example |
|-------|-------------|-------------|---------|
| **Look Up**: Knowledge Graph | [/search/](/search/) and Card Pages | When encountering an unfamiliar term, or needing parameters/sources/upstream-downstream relationships of an entity | Look up what [CAN Bus](/entry/ent_technology_can_bus_2024/) is and where it's used |
| **Learn**: Wiki Monograph | [/wiki/](/wiki/) | When needing systematic understanding of a domain (30 chapters + appendices, written to research paper standards) | Read [Chapter 14: Fundamentals of Robot Control](/wiki/chapters/chapter-14/) to understand WBC |
| **Build**: This Roadmap | The layer you are reading now | When wanting to build a humanoid robot from 0 to 1 | Progress step-by-step through the acceptance criteria of [Stage 0](stage-0-foundations.md) |

Typical cross-layer workflow: Get stuck on a step in the roadmap → Look up parameters and sources for the confusing concept on its card page → Want to thoroughly understand it, go to the corresponding Wiki chapter for systematic study. The roadmap does not repeat the lengthy derivations from the Wiki; it only tells you "what to do in this step, why, and how to judge if it's done right."

## How to Read the Roadmap Pages: Three-Part Structure and Data Discipline

Each practical step in this roadmap follows a three-part structure, which distinguishes it from ordinary tutorials:

1. **【What to Do】** Specific, executable actions with completion markers;
2. **【Why】** The principle behind this step, linked to corresponding knowledge cards and Wiki chapters, providing an entry point for deeper exploration;
3. **【How to Analyze Your Situation】** Guides you to make trade-offs based on your own budget, scenario, and skill background—the approach differs for a pure software background versus a mechanical background.

Data Discipline: Specific parameters appearing in the text (price, torque, degrees of freedom, power consumption, etc.) are always annotated with their source nearby (entity card or `data/roadmap/research/` research file); if no reliable source can be found, it is stated as "needs confirmation with the supplier," and no fabricated numbers are used.

## Four-Stage Map

| Stage | Goal | Estimated Time (Part-Time) | Budget Magnitude | Acceptance (Criteria Summary) |
|-------|------|----------------------------|------------------|-------------------------------|
| **Stage 0 Foundations**[→ Page](stage-0-foundations.md) | Get the ticket: Math four-piece set, Python/C++ and ROS 2, circuit concepts, understand URDF | 6–10 weeks (8–10 h/week) | ≈ ¥0: All software open-source; optional 3D printing prototyping experience, cost needs confirmation with supplier | Read a biped URDF; make a biped model stand in MuJoCo for ≥ 10 s |
| **Stage 1 Build a Joint**[→ Page](stage-1-actuator.md) | Build a qualified actuator module on a test bench: fully understand the chain of motor + reduction + sensing + drive + control | 4–8 weeks (estimated) | Hundreds to thousands of RMB per joint: Quasi-Direct Drive (QDD) solution BOM ~$157–188 per unit (Berkeley 6512, source: `data/roadmap/research/berkeley-humanoid-lite.md`); servo/harmonic drive solution price needs confirmation with supplier | Indicator table documented; 30° step overshoot < 10%; 1 Hz sine tracking amplitude attenuation < 10%; communication link continuous 1 h without dropout |
| **Stage 2 Biped Platform**[→ Page](stage-2-biped.md) | First run the control stack in simulation, then replicate an open-source biped/wheeled biped platform to achieve stable walking on flat ground | 3–6 months (estimated) | Budget determined by platform: Upkie ~$3,000, Berkeley Humanoid Lite ~$3,236–4,312, ToddlerBot ~$6,000 (source: corresponding files in `data/roadmap/research/`); approx. ¥20,000–50,000 range, exchange rate and procurement channels need self-calculation | Simulated continuous walking for 10 min without falling; real robot standing ≥ 5 min, continuous walking on flat ground ≥ 10 min, recoverable from light push, emergency stop demonstrable |
| **Stage 3 Full Humanoid**[→ Page](stage-3-humanoid.md) | Add upper body on top of the biped: arms, end-effectors, perception stack, and intelligence layer, complete end-to-end tasks | 6+ months, continuous iteration | Incremental thousands to tens of thousands of RMB (arms/hands/cameras/compute boards, self-calculate based on chosen solution) | Hear verbal command → autonomously walk to table → identify and grasp cup; IK random sampling solution success rate ≥ 95%, end-effector positioning error ≤ 2 cm |

Two clarifications:

- **Time is an estimate**, based on 8–10 hours per week of part-time effort; full-time work could compress it to about 1/3. It is heavily influenced by your background, see next section.
- **Budget excludes** general-purpose equipment you already own (computer, multimeter, soldering iron). Commercial off-the-shelf platforms exist in a different price world: ROBOTIS OP3 costs $13,764.35 (source: `data/roadmap/research/robotis-op3-darwin-op.md`, 2026 page snapshot), which is one reason this roadmap recommends open-source platforms over commercial ones in Stage 2.

## Mission Page Index (M01–M20)

The four-stage overview is the map; the 20 mission pages are the construction manual: each page has 4–6 three-part steps (what/why/how to analyze your situation), complete numerical examples, checkable acceptance criteria and troubleshooting tables; each concept links to nearby knowledge cards and Wiki chapters, and each device's data is annotated with its research file source. It is recommended to proceed sequentially in the order of the arrows:

- **Stage 1 · Build a Joint**: [M01 Quantify Scenario Requirements](missions/m01-scenario-to-specs.md) → [M02 Motor Calculation and Selection](missions/m02-motor-sizing.md) → [M03 Reducer Design and Calculation](missions/m03-reducer-design.md) → [M04 Driver, Sensing, and Wiring](missions/m04-driver-sensing-wiring.md) → [M05 3D Printing and Mechanical Assembly](missions/m05-print-assembly.md) → [M06 Firmware and Calibration](missions/m06-firmware-calibration.md) → [M07 Bench Testing and Acceptance](missions/m07-bench-acceptance.md)
- **Stage 2 · Biped Platform**: [M08 Platform Selection and Procurement](missions/m08-platform-selection.md) → [M09 Full Assembly, Wiring, and Power Supply](missions/m09-mechanical-assembly.md) → [M10 URDF Modeling and Export](missions/m10-urdf-modeling.md) → [M11 Simulation Environment and Model Conversion](missions/m11-sim-setup.md) → [M12 Simulated Standing and Walking](missions/m12-sim-walking.md) → [M13 Reinforcement Learning Training](missions/m13-rl-training.md) → [M14 Sim-to-Real Deployment and Walking Acceptance](missions/m14-sim-to-real.md)
- **Stage 3 · Full Humanoid**: [M15 Upper Body and End Effectors](missions/m15-upper-body.md) → [M16 Perception Stack Setup](missions/m16-perception-stack.md) → [M17 Teleoperation and Data Collection](missions/m17-teleop-data.md) → [M18 Imitation Learning Training and Deployment](missions/m18-imitation-learning.md) → [M19 End-to-End Task Integration](missions/m19-e2e-task.md) → [M20 Reliability, Maintenance, and Safety Engineering](missions/m20-reliability-safety.md)

## Boundaries of This Roadmap

Clearly stating "what not to do" protects your time more than promising "what to do":

- **Not a paper reading list.** Cutting-edge algorithms (VLA, world models, etc.) are systematically covered in Wiki Chapters 18–20; the roadmap only points to them "when building the robot requires it." First make the machine stand, then talk about intelligence.
- **Not a path to build everything from scratch.** Stage 2 explicitly recommends standing on mature open-source platforms for your first robot. Designing a structure with 20+ degrees of freedom and its actuation from scratch is a team-level, multi-robot-iteration workload, not a reasonable goal for an individual's first robot. The research archive `data/roadmap/research/` contains cost and barrier analyses for candidate platforms such as Berkeley Humanoid Lite, ToddlerBot, Poppy, and ROBOTIS OP3—read it directly when selecting.
- **Not a purchasing guide or safety manual.** All platform comparisons state only verifiable facts and trade-offs; verify the latest prices, licenses (some open-source design files use non-commercial licenses, e.g., ToddlerBot, source: `data/roadmap/research/toddlerbot.md`), and compliance requirements yourself before ordering.
- **Does not guarantee linear progress.** In practice, you may burn a driver in Stage 1 and return to Stage 0 Step 3 to relearn electronics, or fail to tune a simulation in Stage 2 and go back to Step 1 to catch up on mechanics. The value of the roadmap is to let you know where you are and where to go next, not to forbid backtracking.

## Choose Your Entry Point Based on Your Background

### Pure Software Background (CS / AI / Algorithm Engineer)

Your weakness is not code, but **physical intuition and electrical knowledge**. Suggestions:

1. Among the four math pillars, only supplement [Classical Mechanics](/entry/ent_foundation_classical_mechanics/); use Stage 0's criteria to self-check the rest—skip if you pass;
2. Invest the saved time into Stage 0 Step 3 (circuits and CAN) and Step 4 (simulation standing)—the former is your insurance against burning boards on real hardware in Stage 1, the latter is your training ground for mechanical intuition;
3. Do not skip 3D printing basics; Stage 2's structural parts heavily rely on printing (Berkeley Humanoid Lite even prints its cycloidal reducers, source: `data/roadmap/research/berkeley-humanoid-lite.md`).

### Hardware Background (Mechanical / Electrical / Automation Engineer)

Your weakness lies in **software engineering and modern control/learning algorithms**. Suggestions:

1. In Stage 0 Step 1, focus on supplementing [Probability Theory](/entry/ent_foundation_probability_theory/) and [Convex Optimization](/entry/ent_foundation_convex_optimization/); for Step 3's circuit section, spend 30 minutes to grasp the concepts;
2. Python/ROS 2/git must meet the criteria—don't settle for "just understanding"; from Stage 1 onward, all work happens in code;
3. Your intuition about tolerances, assembly, and safety is a valuable asset, and it will pay off in Stage 1 (benchmark joint) and Stage 2 (full robot replication).

### Zero-Background Student

Follow Stage 0 in order, but **set a hard deadline for each step**: use the "how much to learn to be sufficient" criteria in each section, move on once you meet them, and do not go back to drill. Suggestions:

1. First read Wiki [Chapter 1 Introduction](/wiki/chapters/chapter-01/) to build a global picture and understand what system you are building;
2. Multiply your total time budget by 1.5; the amounts in the budget table remain unchanged for you (Stage 0 is essentially free anyway);
3. The biggest risk is "endlessly building foundations"—Stage 0's acceptance criteria are designed to prevent this. Check them one by one, and immediately proceed to Stage 1 once done; Stage 1 will tell you what you lack.

## Stage Badges on Card Pages

On card pages (`/entry/...`) in this repository, you may see badges like `Stage 0 · Foundations`. Their meaning is as follows:

- **Badge = Learning timing hint**: The stage at which this entity "must first be understood" in the roadmap. For example, [URDF Robot Description Format](/entry/ent_technology_urdf_robot_description_format_2024/) is marked Stage 0 because understanding it is a prerequisite for simulation.
- **A card may have multiple badges**: Entities used repeatedly across multiple stages (e.g., [ROS 2 Middleware](/entry/ent_software_ros_2_middleware_2024/)) will show each stage where they become critical.
- **Badges are not difficulty or importance ratings**: A Stage 0 entity is not necessarily "simple," and a Stage 3 entity is not necessarily "advanced"; they only indicate where the entity appears in the robot-building process.

## Next Steps

Open [Stage 0 Foundations](stage-0-foundations.md) and start against the acceptance criteria. Then proceed sequentially to [Stage 1 Build a Joint](stage-1-actuator.md), [Stage 2 Biped Platform](stage-2-biped.md), and [Stage 3 Full Humanoid Robot](stage-3-humanoid.md).
