# 0→1 Building a Humanoid Robot: Roadmap Overview

!!! note "Safety is not a disclaimer, it's part of the process"
    This roadmap involves real hardware: lithium batteries, 24–48 V bus bars, kg-level swinging metal structural parts, and joint torques sufficient to pinch fingers during stall. Safety is not achieved through statements but is built into the process—see [M09 First Power-On Smoke Test](missions/m09-mechanical-assembly.md) for electrical acceptance, [M14 Phased Unlocking](missions/m14-sim-to-real.md) for walking protection, and [M20 Reliability, Maintenance, and Safety](missions/m20-reliability-safety.md) for long-term safety engineering.

## Three Ways to Use This Repository: Look Up, Learn, Build

This repository serves simultaneously as an "atlas," a "book," and a "construction blueprint." The same concept appears once in each layer, with different responsibilities:

| Usage | Entry Point | When to Use | Example |
|-------|-------------|-------------|---------|
| **Look Up**: Knowledge Graph | [/search/](/search/) and Card Pages | When encountering an unfamiliar term, or needing parameters/sources/upstream-downstream relationships of an entity | Look up what [CAN Bus](/entry/ent_technology_can_bus_2024/) is and where it's used |
| **Learn**: Wiki Monograph | [/wiki/](/wiki/) | When needing systematic understanding of a domain (30 chapters + appendices, written to research paper standards) | Read [Chapter 14: Fundamentals of Robot Control](/wiki/chapters/chapter-14/) to understand WBC |
| **Build**: This Roadmap | The layer you are reading now | When you want to build a humanoid robot from 0 to 1 | Pass each checkpoint in [Stage 0](stage-0-foundations.md) step by step |

Typical cross-layer workflow: Get stuck on a step in the roadmap → Look up parameters and sources for the confusing concept on a card page → Want a thorough understanding, then systematically study the corresponding Wiki chapter. The roadmap does not repeat the Wiki's lengthy derivations; it only tells you "what to do in this step, why, and how to judge if it's done right."

## How to Read Roadmap Pages: Three-Part Structure and Data Discipline

Each practical step in this roadmap follows a three-part structure, which distinguishes it from ordinary tutorials:

1. **【What to Do】** Specific, executable actions with completion criteria;
2. **【Why】** The principle behind this step, linked to corresponding knowledge cards and Wiki chapters for deeper exploration;
3. **【Analyze Your Situation】** Guides you to make trade-offs based on your own budget, scenario, and skill background—the same goal requires different approaches for a pure software background versus a mechanical background.

Data Discipline: Specific parameters appearing in the text (prices, torque, degrees of freedom, power consumption, etc.) are always annotated with a primary source URL (entity card or official repository/paper link) nearby; if a reliable source cannot be found, it is explicitly stated as "needs confirmation from the supplier," and no fabricated numbers are used.

## Four-Stage Map

| Stage | Goal | Estimated Time (Hobbyist Commitment) | Budget Magnitude | Acceptance (Criteria Summary) |
|-------|------|--------------------------------------|------------------|-------------------------------|
| **Stage 0: Foundations**[→ Page](stage-0-foundations.md) | Get the ticket: Math four-piece set, Python/C++ and ROS 2, circuit concepts, understand URDF | 6–10 weeks (8–10 h/week) | ≈ ¥0: All software open-source; optional 3D printing prototyping experience, cost needs confirmation from supplier | Read a biped URDF; make a biped model stand ≥ 10 s in MuJoCo |
| **Stage 1: Build a Joint**[→ Page](stage-1-actuator.md) | Build a qualified actuator module on a test bench: fully understand the motor + reduction + sensing + drive + control chain | 4–8 weeks (estimated) | Hundreds to thousands of RMB per joint: Quasi-Direct Drive (QDD) solution single unit BOM approx. $157–188 (Berkeley 6512, source: [EECS-2025-207 Technical Report BOM](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/Archive/EECS-2025-207.pdf)); servo/harmonic drive solution price needs confirmation from supplier | Document the specification sheet; 30° step overshoot < 10%; 1 Hz sine tracking amplitude attenuation < 10%; communication link no dropouts for 1 continuous hour |
| **Stage 2: Biped Platform**[→ Page](stage-2-biped.md) | First, run the control stack in simulation, then replicate an open-source biped/wheeled-biped platform to achieve stable walking on flat ground | 3–6 months (estimated) | Platform determines budget: Upkie approx. $3,000, Berkeley Humanoid Lite approx. $3,236–4,312, ToddlerBot approx. $6,000 (source: official pages for each platform: [Upkie](https://hackaday.io/project/185729-upkie-wheeled-biped-robots), [Berkeley Humanoid Lite](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/Archive/EECS-2025-207.pdf), [ToddlerBot](https://arxiv.org/html/2502.00893v2)); approx. ¥20,000–50,000 range, exchange rates and procurement channels vary, needs own calculation | Continuous walking in simulation for 10 min without falling; real robot stands ≥ 5 min, continuous walking on flat ground ≥ 10 min, recovers from light push, emergency stop demonstrable |
| **Stage 3: Full Humanoid**[→ Page](stage-3-humanoid.md) | Add the upper body onto the biped: arms, end-effectors, perception stack, and intelligence layer, complete end-to-end tasks | 6+ months, continuous iteration | Incremental thousands to tens of thousands of RMB (arms/hands/cameras/compute board, calculate based on chosen solution) | Hear a verbal command → autonomously walk to a table → identify and grasp a cup; IK random sampling solution success rate ≥ 95%, end-effector positioning error ≤ 2 cm |

Two clarifications:

- **Time is an estimate**, based on a hobbyist commitment of 8–10 hours per week; full-time work could compress it to about 1/3. It is heavily influenced by your background, see the next section.
- **Budget excludes** general-purpose equipment you already own (computer, multimeter, soldering iron). Commercial off-the-shelf platforms are in a different price world: the ROBOTIS OP3 sells for $13,764.35 (source: [ROBOTIS US Store Page](https://www.robotis.us/robotis-op3-us/), 2026 page snapshot), which is one reason this roadmap recommends open-source platforms in Stage 2 rather than finished robots.

## Mission Page Index (M01–M20)

The four-stage overview is the map; the 20 mission pages are the construction manual: each page has 4–6 three-part steps (What to Do/Why/Analyze Your Situation), complete numerical examples, checkable acceptance criteria and troubleshooting tables; each concept is linked to nearby knowledge cards and Wiki chapters, and each piece of equipment data is annotated with its research archive source. It is recommended to pass through them one by one in the order of the arrows:

- **Stage 1 · Build a Joint**: [M01: Mathematize the Scenario](missions/m01-scenario-to-specs.md) → [M02: Motor Calculation and Selection](missions/m02-motor-sizing.md) → [M03: Reducer Design and Calculation](missions/m03-reducer-design.md) → [M04: Driver, Sensing, and Wiring](missions/m04-driver-sensing-wiring.md) → [M05: 3D Printing and Mechanical Assembly](missions/m05-print-assembly.md) → [M06: Firmware and Calibration](missions/m06-firmware-calibration.md) → [M07: Bench Testing and Acceptance](missions/m07-bench-acceptance.md)
- **Stage 2 · Biped Platform**: [M08: Platform Selection and Procurement](missions/m08-platform-selection.md) → [M09: Full Assembly, Wiring, and Power](missions/m09-mechanical-assembly.md) → [M10: URDF Modeling and Export](missions/m10-urdf-modeling.md) → [M11: Simulation Environment and Model Conversion](missions/m11-sim-setup.md) → [M12: Simulation Standing and Walking](missions/m12-sim-walking.md) → [M13: Reinforcement Learning Training](missions/m13-rl-training.md) → [M14: Sim-to-Real Deployment and Walking Acceptance](missions/m14-sim-to-real.md)
- **Stage 3 · Full Humanoid**: [M15: Upper Body and End Effectors](missions/m15-upper-body.md) → [M16: Perception Stack Setup](missions/m16-perception-stack.md) → [M17: Teleoperation and Data Collection](missions/m17-teleop-data.md) → [M18: Imitation Learning Training and Deployment](missions/m18-imitation-learning.md) → [M19: End-to-End Task Integration](missions/m19-e2e-task.md) → [M20: Reliability, Maintenance, and Safety Engineering](missions/m20-reliability-safety.md)

## Boundaries of This Roadmap

Clearly stating "what not to do" protects your time more than promising "what to do":

- **It is not a paper reading list.** Cutting-edge algorithms (VLA, world models, etc.) are systematically discussed in Wiki Chapters 18–20; the roadmap only points to them "when needed for building the robot." First, make the machine stand up, then talk about intelligence.
- **It is not a path to build everything from scratch.** Stage 2 explicitly recommends building your first robot on mature open-source platforms. Designing the structure and actuation for 20+ degrees of freedom from scratch is a team-level, multi-robot iteration workload, not a reasonable goal for an individual's first robot. The [public research archive](https://github.com/YansongW/awesome-humanoid-robot/tree/main/data/roadmap/research/) provides cost and barrier analysis for candidate platforms like Berkeley Humanoid Lite, ToddlerBot, Poppy, and ROBOTIS OP3; read it directly when selecting.
- **It is not a purchasing guide or safety manual.** All platform comparisons only state verifiable facts and trade-offs; verify the latest prices, licenses (some open-source design files have non-commercial licenses, e.g., ToddlerBot, source: [ToddlerBot GitHub](https://github.com/hshi74/toddlerbot)), and compliance requirements yourself before ordering.
- **It does not guarantee linear progress.** In practice, you might burn a driver in Stage 1 and return to Stage 0 Step 3 to relearn electronics, or fail to tune the simulation in Stage 2 and go back to Step 1 to brush up on mechanics. The value of the roadmap is to let you know where you are and where to go next, not to forbid backtracking.

## Choose Your Entry Point Based on Your Background

### Pure Software Background (CS / AI / Algorithm Engineer)

Your weakness is not code, but **physical intuition and electrical knowledge**. Suggestions:

1. Among the four math foundations, only supplement [Classical Mechanics](/entry/ent_foundation_classical_mechanics/); use the Stage 0 criteria to self-check the rest, and skip if passed;
2. Invest the saved time in Stage 0 Step 3 (Circuits and CAN) and Step 4 (Simulation Standing) – the former is your insurance against burning hardware in Stage 1, the latter is your training ground for mechanical intuition;
3. Do not skip 3D printing basics; structural parts in Stage 2 heavily rely on printing (Berkeley Humanoid Lite even prints its cycloidal reducers, source: [Berkeley Humanoid Lite Paper](https://arxiv.org/abs/2504.17249)).

### Hardware Background (Mechanical / Electrical / Automation Engineer)

Your weakness is in **software engineering and modern control/learning algorithms**. Suggestions:

1. In Stage 0 Step 1, focus on supplementing [Probability Theory](/entry/ent_foundation_probability_theory/) and [Convex Optimization](/entry/ent_foundation_convex_optimization/); for Step 3's circuit section, a 30-minute overview of concepts is sufficient;
2. Python/ROS 2/git must meet the criteria; do not settle for "just understanding" – all work from Stage 1 onward is in code;
3. Your intuition about tolerances, assembly, and safety is a valuable asset, which will pay off in Stage 1 (Benchmark Joint) and Stage 2 (Full Robot Replication).

### Zero-Background Student

Follow Stage 0 sequentially, but **set a deadline for each step**: check the "how much is enough" criteria for each section, move on once met, and do not backtrack for extra practice. Suggestions:

1. First, read Wiki [Chapter 1 Introduction](/wiki/chapters/chapter-01/) to build an overall picture of the system you are building;
2. Multiply your total time budget by 1.5; the cost figures in the budget table remain unchanged for you (Stage 0 is essentially free anyway);
3. The biggest risk is "infinite foundation building" – Stage 0's acceptance criteria are designed to prevent this. Check items one by one, move to Stage 1 immediately upon completion, and Stage 1 will tell you what you are missing.

## Stage Badges on Card Pages

On card pages (`/entry/...`) in this repository, you may see badges like `Stage 0 · Foundation Building`. The conventions are:

- **Badge = Learning Timing Hint**: The stage in the roadmap where understanding this entity is "first non-negotiable." For example, [URDF Robot Description Format](/entry/ent_technology_urdf_robot_description_format_2024/) is marked Stage 0 because understanding it is a prerequisite for getting started with simulation.
- **A card can have multiple badges**: Entities used repeatedly across multiple stages (e.g., [ROS 2 Middleware](/entry/ent_software_ros_2_middleware_2024/)) will show each stage where it becomes critical.
- **Badges are not difficulty or importance ratings**: A Stage 0 entity is not necessarily "simple," and a Stage 3 entity is not necessarily "advanced"; they only indicate where in the robot-building process the entity appears.

## Next Steps

Open [Stage 0 Foundations](stage-0-foundations.md) and start against the acceptance criteria. Then proceed sequentially to [Stage 1 Build a Joint](stage-1-actuator.md), [Stage 2 Biped Platform](stage-2-biped.md), and [Stage 3 Full Humanoid Robot](stage-3-humanoid.md).
