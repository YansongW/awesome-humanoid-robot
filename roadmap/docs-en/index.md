# 0→1 Building a Humanoid Robot: Roadmap Overview

> ⚠️ This roadmap is compiled based on publicly available information and theoretical knowledge, and has not been verified on actual hardware. When dealing with electrical or mechanical operations, please verify safety standards yourself.

!!! warning "Read This First, Then Talk About Building a Robot"
    This is a roadmap involving **real hardware**: lithium batteries, 24–48 V bus bars, metal structural components swinging at the kg level, and joint torques sufficient to pinch fingers when stalled. No page of this roadmap is a substitute for a safety manual. Before powering on, please verify electrical and mechanical safety standards yourself; for any operation you are unsure about, have someone with hardware experience present to review it. All prices, lead times, and supplier information are subject to the actual situation at the time of your order.

## Three Ways to Use This Repository: Look Up, Learn, Build

This repository serves simultaneously as an "atlas", a "book", and a "blueprint". The same concept appears once in each of the three layers, with different responsibilities:

| Usage | Entry Point | When to Use | Example |
|------|-------------|-------------|---------|
| **Look Up**: Knowledge Graph | [/search/](/search/) and Card Pages | When encountering an unfamiliar term, or needing parameters/sources/upstream-downstream relationships of an entity | Look up what [CAN Bus](/entry/ent_technology_can_bus_2024/) is and where it is used |
| **Learn**: Wiki Monograph | [/wiki/](/wiki/) | When needing systematic understanding of a field (30 chapters + appendices, written to research paper standards) | Read [Chapter 14: Fundamentals of Robot Control](/wiki/chapters/chapter-14/) to understand WBC |
| **Build**: This Roadmap | The layer you are reading now | When you want to build a humanoid robot from 0 to 1 | Pass the acceptance criteria of [Stage 0](stage-0-foundations.md) item by item |

Typical interaction between the three layers: You reach a certain step in the roadmap → Look up parameters and sources for a confusing concept on the card page → Go to the corresponding Wiki chapter for systematic study if you want to fully understand it. The roadmap does not repeat the lengthy derivations from the Wiki; it only tells you "what to do in this step, why, and how to judge if it's done right".

## How to Read the Roadmap Pages: Three-Part Structure and Data Discipline

Each practical step in this roadmap follows a three-part structure, which distinguishes it from ordinary tutorials:

1. **【What to Do】** Specific, executable actions with clear completion criteria;
2. **【Why】** The principle behind this step, linked to corresponding knowledge cards and Wiki chapters, providing an entry point for deeper exploration;
3. **【How to Analyze Your Situation】** Guides you to make trade-offs based on your own budget, scenario, and skill background—the same goal requires a different approach for a pure software background versus a mechanical background.

Data Discipline: Specific parameters appearing in the text (prices, torque, degrees of freedom, power consumption, etc.) are always annotated with their source nearby (entity card or `data/roadmap/research/` investigation file); if a reliable source cannot be found, it is explicitly stated as "needs to be confirmed with the supplier", and no fabricated numbers are used.

## Four-Stage Map

| Stage | Goal | Estimated Time (Hobbyist Commitment) | Budget Magnitude | Acceptance (Criteria Summary) |
|-------|------|--------------------------------------|------------------|-------------------------------|
| **Stage 0: Foundations**[→ Page](stage-0-foundations.md) | Get the ticket: Math four-piece set, Python/C++ and ROS 2, circuit concepts, understand URDF | 6–10 weeks (8–10 h/week) | ≈ ¥0: All software open source; optional 3D printing prototyping experience, cost to be confirmed with supplier | Understand a bipedal URDF; make a bipedal model stand in MuJoCo for ≥ 10 s |
| **Stage 1: Build an Actuator**[→ Page](stage-1-actuator.md) | Build a qualified actuator module on a test bench: fully understand the chain of motor + reduction + sensing + drive + control | 4–8 weeks (estimated) | Hundreds to thousands of RMB per joint: Quasi-Direct Drive (QDD) solution BOM approx. $157–188 per unit (Berkeley 6512, source: `data/roadmap/research/berkeley-humanoid-lite.md`); servo/harmonic solution prices to be confirmed with supplier | Indicator table documented; 30° step overshoot < 10%; 1 Hz sine tracking amplitude attenuation < 10%; communication link no dropouts for 1 continuous hour |
| **Stage 2: Bipedal Platform**[→ Page](stage-2-biped.md) | First, run the control stack in simulation, then replicate an open-source bipedal/wheeled-leg platform to achieve stable walking on flat ground | 3–6 months (estimated) | Budget determined by platform: Upkie approx. $3,000, Berkeley Humanoid Lite approx. $3,236–4,312, ToddlerBot approx. $6,000 (source: corresponding files in `data/roadmap/research/`); approx. ¥20,000–50,000 range, exchange rate and procurement channel fluctuations to be calculated by yourself | Continuous walking in simulation for 10 min without falling; real robot standing ≥ 5 min, continuous walking on flat ground ≥ 10 min, recoverable from a light push, emergency stop demonstrable |
| **Stage 3: Full Humanoid**[→ Page](stage-3-humanoid.md) | Add the upper body to the biped: arms, end-effectors, perception stack, and intelligence layer, completing end-to-end tasks | 6+ months, continuous iteration | Incremental cost of thousands to tens of thousands of RMB (arms/hands/cameras/compute boards, calculate based on chosen solution) | Hear a verbal command → autonomously walk to a table → identify and pick up a cup; IK random sampling solution success rate ≥ 95%, end-effector positioning error ≤ 2 cm |

Two notes:

- **Time is an estimate**, based on a hobbyist commitment of 8–10 hours per week; full-time work could compress it to about 1/3. It is heavily influenced by your background, see next section.
- **Budget excludes** general-purpose equipment you already own (computer, multimeter, soldering iron). Commercial off-the-shelf platforms are in a different price world: the ROBOTIS OP3 sells for $13,764.35 (source: `data/roadmap/research/robotis-op3-darwin-op.md`, 2026 page snapshot), which is one reason this roadmap recommends open-source platforms over finished robots in Stage 2.

## Boundaries of This Roadmap

Clarifying "what is not done" protects your time better than promising "what is done":

- **It is not a paper reading list.** Cutting-edge algorithms (VLA, world models, etc.) are systematically discussed in Wiki Chapters 18–20; the roadmap only points to them "when needed for building the robot". First, make the robot stand, then talk about intelligence.
- **It is not a route to self-develop everything from scratch.** Stage 2 explicitly recommends building your first robot on a mature open-source platform: designing the structure and drive for 20+ degrees of freedom from scratch is a team-level, multi-iteration workload, not a reasonable goal for an individual's first robot. The investigation files in `data/roadmap/research/` provide cost and threshold analyses for candidate platforms like Berkeley Humanoid Lite, ToddlerBot, Poppy, and ROBOTIS OP3, which you can read directly when selecting.
- **It is not a purchasing guide or safety manual.** All platform comparisons only state verifiable facts and trade-offs from sources; verify the latest prices, licenses (some open-source design files have non-commercial licenses, e.g., ToddlerBot, source: `data/roadmap/research/toddlerbot.md`), and compliance requirements yourself before ordering.
- **It does not guarantee linear progress.** In reality, you might burn a driver in Stage 1 and go back to Stage 0, Step 3 to re-learn electronics, or get stuck tuning a simulation in Stage 2 and go back to Step 1 to brush up on mechanics. The value of the roadmap is to let you know where you are and where to go next, not to forbid going back.

## Choose Your Entry Point Based on Your Background

### Pure Software Background (CS / AI / Algorithm Engineer)

Your weakness is not in code, but in **physical intuition and electrical common sense**. Suggestions:

1. Among the four math modules, only supplement [Classical Mechanics](/entry/ent_foundation_classical_mechanics/); use the Stage 0 criteria to self-check the rest, and skip if you pass;
2. Invest the saved time into Stage 0 Step 3 (Circuits & CAN) and Step 4 (Simulation Stand)—the former is your insurance against burning hardware in Stage 1, the latter is your training ground for mechanical intuition;
3. Do not skip 3D printing basics; Stage 2 structural parts heavily rely on printing (Berkeley Humanoid Lite even prints its cycloidal reducers, source: `data/roadmap/research/berkeley-humanoid-lite.md`).

### Hardware Background (Mechanical / Electrical / Automation Engineer)

Your weakness lies in **software engineering and modern control/learning algorithms**. Suggestions:

1. In Stage 0 Step 1, focus on supplementing [Probability Theory](/entry/ent_foundation_probability_theory/) and [Convex Optimization](/entry/ent_foundation_convex_optimization/); for Step 3 circuits, spend 30 minutes to skim the concepts;
2. Python/ROS 2/git must meet the criteria—do not settle for "just understanding"—all work from Stage 1 onward is in code;
3. Your intuition for tolerances, assembly, and safety is a valuable asset, which will pay off in Stage 1 (bench joint) and Stage 2 (full robot replication).

### Zero-Background Student

Follow Stage 0 in order diligently, but **set a hard deadline for each step**: check against the "how much is enough" criteria in each section, move on once you pass, and do not go back to drill. Suggestions:

1. First read Wiki [Chapter 1 Introduction](/wiki/chapters/chapter-01/) to build an overall picture of what system you are building;
2. Multiply your total time budget by 1.5; the cost in the budget table remains unchanged for you (Stage 0 is essentially free anyway);
3. The biggest risk is "endless foundation building"—the Stage 0 acceptance criteria are designed to prevent this. Check off items one by one, immediately enter Stage 1 upon completion, and Stage 1 will tell you what you lack.

## Stage Badges on Card Pages

On the card pages (`/entry/...`) of this repository, you may see badges like `Stage 0 · Foundations`. The conventions are as follows:

- **Badge = Learning Timing Hint**: The stage in the roadmap where this entity "must be understood first." For example, [URDF Robot Description Format](/entry/ent_technology_urdf_robot_description_format_2024/) is marked Stage 0 because understanding it is a prerequisite for simulation entry.
- **A Card Can Have Multiple Badges**: Entities used repeatedly across multiple stages (e.g., [ROS 2 Middleware](/entry/ent_software_ros_2_middleware_2024/)) will mark each stage where it becomes critical.
- **Badges Are Not Difficulty or Importance Ratings**: A Stage 0 entity is not necessarily "simple," and a Stage 3 entity is not necessarily "advanced"; they only indicate where the entity appears in the robot-building process.

## Next Steps

Open [Stage 0 Foundations](stage-0-foundations.md) and start against the acceptance criteria. Then proceed sequentially to [Stage 1 Build a Joint](stage-1-actuator.md), [Stage 2 Biped Platform](stage-2-biped.md), and [Stage 3 Full Humanoid Robot](stage-3-humanoid.md).
