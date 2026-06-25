# 10 Evaluation & Benchmarks

> **Domain Code**: `10_evaluation_benchmarks`  
> **Layer**: Validation & Markets  
> **Status**: Draft — subject to review before v0.1.0  
> **Purpose**: Define the benchmarks, evaluation protocols, safety standards, and production-readiness metrics that determine whether a humanoid robot is ready to leave the lab and enter industrial service.

---

## 1. Central Question

> **How do we know a humanoid robot is good enough to deploy at scale?**

A humanoid robot that performs well in a demo video is not the same as one that can run a factory shift, pass a safety audit, or justify a capital expenditure. This domain tracks the measurement infrastructure — simulation benchmarks, real-world task protocols, safety standards, hardware-in-the-loop validation, and production KPIs — that translate technical capability into deployable, insurable, and economically viable products.

---

## 2. Scope

### 2.1 In Scope

- Simulated benchmarks for whole-body locomotion, manipulation, and navigation.
- Real-world task benchmarks, pilot-study protocols, and factory/warehouse evaluation metrics.
- Safety standards and certification requirements relevant to humanoid robots (ISO, IEEE, national/regional frameworks).
- Performance, reliability, energy, and economic KPIs used to judge production readiness.
- Hardware-in-the-loop (HIL) testing and sim-to-real validation methods.
- Benchmark-data licensing, reproducibility, and reporting conventions.

### 2.2 Out of Scope

- The algorithms being evaluated (covered in `07_ai_models_algorithms`).
- The datasets used for training (covered in `09_data_datasets`).
- The components and manufacturing processes being tested (covered in `02_components_supply_chain`, `03_manufacturing_processes`, `04_assembly_integration_testing`).
- General AI/ML benchmarks with no humanoid-robot relevance.

---

## 3. Key Concepts

### 3.1 Simulation Benchmarks for Whole-Body Control

Simulation benchmarks provide reproducible, low-cost environments for comparing locomotion, manipulation, and navigation policies before risking real hardware.

| Benchmark | Physics engine | Representative robot(s) | Task families | Notable features |
|-----------|---------------|------------------------|---------------|------------------|
| **HumanoidBench** | MuJoCo | Unitree H1 (+ Shadow Hands) | 14 locomotion + 17 manipulation tasks | 61-dimensional action space, normalized success scores, dexterous-hand variants [1] |
| **Isaac Lab** | Isaac Sim / PhysX | Unitree G1/H1, Agility Digit, others | Locomotion, manipulation, navigation | Massively parallel GPU training, visual/perceptive tasks, sim-to-real recipes [2] |
| **DMC Humanoid** | MuJoCo | Procedural humanoid | Stand, walk, run | Low-dimensional classic RL baseline for policy comparison [2] |

**Sources and evidence**:
- HumanoidBench is built around the Unitree H1 model and explicitly designed to evaluate high-dimensional whole-body control, with tasks ranging from walking and running to bookshelf insertion and door opening [1].
- Isaac Lab provides unified environments across classic control, legged locomotion, dexterous manipulation, and navigation, and has been used to benchmark Unitree G1 and Agility Digit locomotion with height-scanner perception [2].
- The DeepMind Control Suite (DMC) humanoid tasks remain a widely used low-dimensional baseline; Isaac Lab re-implements DMC-style tasks alongside higher-fidelity robot models [2].

> **Speculative note**: It is unclear whether leaderboard rankings on these simulation benchmarks are strongly predictive of real-world humanoid performance. The correlation between simulation score and factory-task success is an active research question.

### 3.2 Real-World Task and Pilot Benchmarks

Ultimately, humanoid robots must be evaluated in the target environment. Historical competitions and modern factory pilots show which metrics matter and which failure modes dominate.

| Benchmark / pilot | Setting | Key metrics | Key lessons |
|-------------------|---------|-------------|-------------|
| **DARPA Robotics Challenge (DRC)** | Disaster-response tasks with Atlas humanoid | Task score, completion time, fall recovery, operator interventions | Hardware reliability and fall recovery are critical; many robots required human rescue [3] |
| **Factory pilots (automotive, logistics)** | Assembly, sheet-metal loading, box handling | Uptime, cycle time, placement success, mean time between failures (MTBF), human interventions | Defined success criteria and phased gates are prerequisites for scaling [4] |
| **Warehouse pilot protocols** | Picking, loading, sorting | Pieces per hour (PPH), error rate, battery-swap time, WMS integration latency | Realistic environment replication and integration with warehouse software matter [5] |

**Sources and evidence**:
- A post-DRC analysis by participating teams reports that Atlas robots were functional roughly 50% of the available development time, with failures caused by hardware degradation, operator errors, and software bugs; the authors identify robust hardware and fall recovery as prerequisites for real disaster response [3].
- Modern manufacturing pilots (e.g., automotive sheet-metal loading) track cycle time, placement tolerance, uptime, and intervention rate; structured validation phases of three to six months are common before live production entry [4].
- Warehouse pilot guidance emphasizes replicating real machinery, spacing, lighting, and terrain; key metrics include process speed, error rate, uptime/downtime, energy cost, and battery-swap time [5].

### 3.3 Safety Standards and Certification Benchmarks

Humanoid robots do not yet have a single dedicated international safety standard. Current deployments borrow from personal-care, industrial, and collaborative robot standards, creating a compliance patchwork.

| Standard | Scope | Relevance to humanoids | Known gap |
|----------|-------|------------------------|-----------|
| **ISO 13482:2014** | Personal care robots (mobile servant, physical assistant, person carrier) | Closest existing framework for service humanoids; covers human-robot physical contact | Does not address bipedal dynamic balance, fall safety, or autonomous walking speed |
| **ISO 10218-1:2025** | Industrial robot safety | Applies to manipulator arms and robot systems in factories | Designed for fixed or mobile industrial arms, not free-walking humanoids |
| **ISO/TS 15066:2016** | Collaborative industrial robots | Force/power limits and separation monitoring for human contact | Limited to industrial robot systems; excludes non-industrial service robots |
| **IEEE P2839 / ISO 25785-1** | Emerging humanoid-specific safety | Intended to cover fall mitigation, impact force, emergency-stop behavior, dynamic balance | Draft / under development; no published consensus standard as of mid-2026 |

**Sources and evidence**:
- ISO 13482:2014 explicitly covers personal care robots operating near humans, including human-robot physical contact, but excludes industrial robots, medical devices, toys, military robots, and robots travelling faster than 20 km/h [6].
- ISO 10218-1:2025 specifies inherently safe design and risk-reduction measures for industrial robots, including Class I/II force-testing methodology; it is a type-C standard under ISO 12100 and is aimed at robot manufacturers and integrators [7].
- ISO/TS 15066:2016 provides collaborative-robot safety guidance, including power and force limiting and speed/separation monitoring, but its scope is industrial robot systems [7].

> **Speculative note**: No published international standard fully covers free-walking humanoids in mixed-use spaces. The observed industry practice of combining ISO 10218 for arms, ISO 13482 for mobile bases, and ISO/TS 15066 for contact limits is an analytical inference based on the scope limitations of those standards; it should be treated as forward-looking until documented in integrator safety-case disclosures.

> **Speculative note**: IEEE P2839 and ISO 25785-1 are widely discussed as humanoid-specific initiatives, but publication timelines and final scope remain uncertain. Treat claims about their content as forward-looking until final drafts are published.

### 3.4 Metrics and KPIs for Production Readiness

Research metrics (success rate, reward) must be supplemented with production metrics (uptime, cost, safety) when judging mass-production readiness.

| Metric category | Examples | Research use | Production / deployment use |
|-----------------|----------|--------------|----------------------------|
| **Task performance** | Success rate, pieces per hour (PPH), placement tolerance, cycle time | Algorithm ranking, sim-to-real comparison | ROI calculation, line-rate planning |
| **Efficiency** | Energy per task, battery runtime, cost per task | Policy optimization | Operating expenditure, charging infrastructure sizing |
| **Reliability** | MTBF, MTTR, uptime, fault rate, intervention rate | Stress testing, regression testing | Fleet planning, maintenance contracts |
| **Safety** | Collision force, fall frequency, emergency-stop latency, contact-force limits | Safety-case evidence | Certification, insurance, liability |

**Sources and evidence**:
- DRC post-analysis identified hardware reliability as a limiting factor, with Atlas robots experiencing mean times between failures of hours to days; the authors argue that behaviors must tolerate component failures [3].
- Factory pilot reports track uptime, cycle time, placement success, and intervention rate as exit criteria before scaling [4].
- Warehouse pilot guidance explicitly recommends energy utilization, downtime, and battery-swap time as part of a holistic productivity assessment [5].

### 3.5 Hardware-in-the-Loop and Sim-to-Real Validation

HIL and sim-to-real methods attempt to close the gap between simulation scores and real-world behavior.

| Method | What it tests | Role in validation | Limitation |
|--------|--------------|-------------------|------------|
| **Hardware-in-the-loop (HIL)** | Real controller + simulated plant | Regression testing of safety-critical control loops before field deployment | Cannot reproduce all contact dynamics, sensor noise, or environmental variation |
| **Domain randomization / adaptation** | Policy robustness to sim variations | Improves transfer from simulation to real hardware | May overfit to the training distribution; success is task-dependent |
| **Real-world pilot** | Full system in target environment | Ground-truth performance and failure-mode discovery | Expensive, slow, non-reproducible, requires safety supervision |

**Sources and evidence**:
- A survey of robot-policy evaluation for sim-to-real transfer argues that benchmarks should systematically increase task complexity and scenario perturbation, and should quantify the alignment between real-world performance and simulation counterparts [8].
- Hardware-in-the-loop testing, telemetry normalization, and staged rollout gates are standard practices in safety-critical robotics deployment; while the terminology is common in production engineering, specific public case studies for humanoid fleets remain limited.

---

## 4. Relationship Patterns to Other Domains

| From | To | Relationship | Rationale |
|------|-----|--------------|-----------|
| `10_evaluation_benchmarks` | `07_ai_models_algorithms` | `is_prerequisite_for` | Benchmarks define the tasks and metrics against which policies are ranked and selected |
| `10_evaluation_benchmarks` | `09_data_datasets` | `requires` | Benchmarks need standardized training and test datasets to be reproducible |
| `10_evaluation_benchmarks` | `02_components_supply_chain` | `requires` | HIL and real-world benchmarks require specific actuators, sensors, and compute hardware |
| `10_evaluation_benchmarks` | `04_assembly_integration_testing` | `is_prerequisite_for` | Evaluation protocols determine which integrated systems pass factory exit gates |
| `10_evaluation_benchmarks` | `06_design_engineering` | `constrains` | Safety benchmarks constrain morphology, mass, contact surfaces, and joint torque limits |
| `10_evaluation_benchmarks` | `11_applications_markets` | `serves` | Benchmarks and pilot metrics validate whether a robot can meet application economics |
| `10_evaluation_benchmarks` | `12_policy_regulation_ethics` | `is_regulated_by` | Safety certifications and standards set mandatory evaluation criteria for deployment |

---

## 5. Controlled Vocabulary

### 5.1 Benchmark / Evaluation Categories

- `simulation_benchmark`
- `real_world_task_benchmark`
- `hardware_in_the_loop`
- `safety_standard`
- `certification`
- `pilot_study`
- `performance_metric`
- `reliability_metric`
- `energy_metric`
- `sim_to_real_validation`

### 5.2 Relevant Entity Types

From the project information model:

- `benchmark`
- `standard`
- `certification`
- `dataset`
- `paper`
- `report`
- `robot_system`
- `application_scenario`
- `market_segment`

---

## 6. Key Sources

### 6.1 Primary / Authoritative Sources

1. **Sferrazza, C., Huang, D.-M., Lin, X., Lee, Y., & Abbeel, P.** (2024). *HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation*. arXiv:2403.10506.  
   URL: https://arxiv.org/abs/2403.10506  
   Annotation: Introduces a high-dimensional MuJoCo benchmark based on Unitree H1 with 31 locomotion and manipulation tasks and dexterous-hand variants.

2. **Mittal, M., et al.** (2025). *Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning*. arXiv:2511.04831.  
   URL: https://arxiv.org/abs/2511.04831  
   Annotation: NVIDIA's open-source robot-learning framework built on Isaac Sim, providing locomotion, manipulation, and navigation environments for humanoids including Unitree G1/H1 and Agility Digit.

3. **Atkeson, C. G., et al.** (2015). *What Happened at the DARPA Robotics Challenge, and Why?* Journal of Field Robotics.  
   URL: https://www.cs.cmu.edu/~cga/drc/jfr-what.pdf  
   Annotation: Post-hoc analysis by competing teams of the DRC, identifying hardware reliability, operator errors, and lack of fall recovery as dominant failure modes.

### 6.2 Industry and Market Analysis

4. **Fortune / cited in industry deployment tracking** (2026). Reports on Figure AI's BMW Spartanburg pilot, including ~1,250 operating hours and commercial expansion criteria.  
   URL: https://fortune.com/ (secondary citations in deployment trackers such as https://humanoid.guide/)  
   Annotation: Illustrates current factory-pilot gating practices (uptime, task success, cycle time) before commercial scale-out.

5. **Manufacturing Today** (2024). *Humanoid Robots in Warehouses: A Pilot Study Approach*.  
   URL: https://manufacturing-today.com/news/humanoid-robots-in-warehouses-a-pilot-study-approach/  
   Annotation: Practitioner guidance on warehouse pilot design, emphasizing realistic environment replication and metrics such as PPH, error rate, uptime, and energy cost.

### 6.3 Standards and Safety Sources

6. **ISO 13482:2014.** *Robots and robotic devices — Safety requirements for personal care robots*.  
   URL: https://www.iso.org/standard/53820.html  
   Annotation: The closest published international safety standard for service humanoids; covers mobile servant, physical assistant, and person carrier robots.

7. **ISO 10218-1:2025 and ISO/TS 15066:2016.** *Industrial robot and collaborative robot safety requirements*.  
   URLs: https://www.iso.org/obp/ui/en/#!iso:std:73933:en (ISO 10218-1:2025) and https://www.iso.org/standard/62996.html (ISO/TS 15066:2016)  
   Annotation: Revised industrial-robot safety standard and collaborative-robot technical specification, defining force-testing methodology, power/force limiting, and speed/separation monitoring.

### 6.4 Domain-Specific Sources

8. **Yang, X., Eppner, C., Tremblay, J., Fox, D., Birchfield, S., & Ramos, F.** (2025). *Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective*. arXiv:2508.11117.  
   URL: https://arxiv.org/abs/2508.11117  
   Annotation: Discusses desiderata for sim-to-real benchmarks, including systematic perturbation and quantified alignment between simulated and real-world performance.

---

## 7. Open Questions

1. Which simulation benchmarks, if any, are the strongest predictors of real-world humanoid factory performance, and how should we validate that predictive power?
2. How should the ontology represent benchmark versions and leaderboards as they evolve rapidly (e.g., HumanoidBench task additions, Isaac Lab environment updates)?
3. What is the minimum set of real-world pilot metrics that buyers should require before accepting a humanoid robot for industrial deployment?
4. How can the project track emerging humanoid-specific safety standards (IEEE P2839, ISO 25785-1) and map them to certification requirements across regions?
