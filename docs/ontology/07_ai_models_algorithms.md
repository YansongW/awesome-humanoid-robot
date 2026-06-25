# 07 AI Models & Algorithms

> **Domain Code**: `07_ai_models_algorithms`  
> **Layer**: Intelligence  
> **Status**: Draft — subject to review before v0.1.0  
> **Purpose**: Define the AI-model and algorithm concepts that enable humanoid robots to perceive, reason, plan, and act, and establish how this domain links to the rest of the value chain.

---

## 1. Central Question

> **What algorithms and models enable a humanoid robot to perceive its environment, plan tasks, control its body, and generalize across new tasks and deployments?**

Humanoid robots must fuse high-dimensional perception, language, physics, and action into reliable real-time behavior. The choice of model family — vision-language-action (VLA) foundation model, reinforcement-learning locomotion policy, diffusion/flow manipulation policy, world model, or hierarchical planner — shapes compute requirements, data needs, deployment latency, and the set of tasks the hardware can actually perform. This domain tracks the intelligence layer before it is packaged into software stacks and deployed on physical platforms.

---

## 2. Scope

### 2.1 In Scope

- Vision-language-action (VLA) foundation models for humanoid control.
- Locomotion, whole-body control, and balancing policies.
- Manipulation and loco-manipulation policies.
- World models, predictive models, and sim-to-real transfer methods.
- Task planning, reasoning, and hierarchical skill architectures.
- Learning paradigms: imitation learning, reinforcement learning, self-supervised learning, and fine-tuning.
- Algorithm-level trade-offs: latency, compute cost, sample efficiency, generalization, and safety.

### 2.2 Out of Scope

- Software frameworks, middleware, and simulators as products (covered in `08_software_middleware`).
- Datasets, data pipelines, and licensing (covered in `09_data_datasets`).
- Evaluation protocols, benchmarks, and safety standards (covered in `10_evaluation_benchmarks`).
- General AI research with no demonstrated humanoid-robot relevance.

---

## 3. Key Concepts

### 3.1 Vision-Language-Action (VLA) Foundation Models

VLAs unify visual perception, language understanding, and motor control in a single model. They are attractive for humanoids because they allow operators to instruct robots with natural language and because web-pretrained vision-language backbones transfer broad semantic knowledge to physical tasks.

| Aspect | Description | Examples / Notes |
|--------|-------------|------------------|
| Action representation | Discrete token prediction vs. continuous action generation | RT-2 tokenizes actions; OpenVLA uses discrete tokens; π0 and GR00T N1 use flow-matching or diffusion for continuous motor commands |
| Vision-language backbone | Pretrained VLM provides semantic and spatial understanding | RT-2 uses PaLI-X; OpenVLA uses Llama 2 + DINOv2; GR00T N1 uses NVIDIA Eagle-2 |
| Embodiment handling | Cross-robot data mixing and action-space adaptation | Foundation policies such as GR00T N1 are trained on multiple embodiments and fine-tuned for new robots |
| Latency envelope | Inference cost determines control frequency | GR00T N1-2B reports ~63.9 ms to sample a 16-action chunk on an L40 GPU [GR00T N1 2025] |

**Sources and evidence**:
- RT-2 demonstrated that web-pretrained vision-language models can be fine-tuned for manipulation by treating actions as text tokens, improving generalization over prior end-to-end policies [RT-2 2023].
- OpenVLA released an open-source 7B-parameter VLA trained on the Open X-Embodiment dataset and showed that model size and visual pretraining improve cross-task transfer [OpenVLA 2024].
- π0 introduced a flow-matching action expert coupled to a VLM backbone, producing high-frequency continuous control for dexterous manipulation [π0 2024].
- GR00T N1 is a 2.2B-parameter dual-system VLA for generalist humanoid robots: a VLM-based reasoning module feeds a Diffusion Transformer action module, and the released checkpoint supports multiple embodiments [GR00T N1 2025].

### 3.2 Locomotion and Whole-Body Control

Locomotion policies must maintain balance under disturbances, traverse uneven terrain, and coordinate dozens of degrees of freedom at high frequency. Whole-body control additionally coordinates the arms, torso, and legs while respecting contact and torque limits.

| Approach | Description | Representative Direction |
|----------|-------------|------------------------|
| Model-based control | MPC, WBC, and ZMP/DCM planners compute dynamically feasible trajectories | Classical bipedal control; often used as a safety baseline or teacher policy |
| Reinforcement learning in simulation | Policies trained with massive parallel RL and transferred zero-shot to real robots | "Learning sim-to-real humanoid locomotion in 15 minutes" uses GPU-based parallel training [Seo et al. 2025] |
| Transformer and neural policies | Causal sequence models predict actions from observation history | Causal transformer policies; can adapt to varied terrain with sufficient sim-to-real training [Seo et al. 2025] |
| Human motion tracking | Policies imitate retargeted human motion capture for natural gaits and recovery | Used in recent whole-body control pipelines based on retargeted human motion data |

**Sources and evidence**:
- Seo et al. (2025) train a humanoid locomotion policy entirely in simulation and deploy it on a real robot, reporting that the whole pipeline — including real-world adaptation — completes in approximately 15 minutes [Seo et al. 2025].
- HumanoidBench provides a standardized simulated testbed based on the Unitree H1, with over 40 tasks spanning locomotion and manipulation, enabling controlled comparison of locomotion algorithms [HumanoidBench 2024].
- Goldberg (2025) argues that the "100,000-year data gap" between robot experience and human physical experience can be closed only through deliberate engineering of sensors, simulators, and structured demonstrations, not by data scaling alone [Goldberg 2025].

### 3.3 Manipulation and Loco-Manipulation Policies

Manipulation policies map perception and task goals into end-effector and finger commands. Loco-manipulation further requires the robot to coordinate stepping, balance, reaching, and contact forces simultaneously.

| Policy family | Mechanism | Humanoid relevance |
|---------------|-----------|--------------------|
| Behavior cloning / ACT | Directly imitate teleoperated demonstrations | Easy to implement; struggles with long-horizon and out-of-distribution tasks |
| Diffusion / flow-matching policies | Generate continuous action trajectories via iterative denoising or flow matching | π0 produces smooth, high-frequency bimanual actions on real robots [π0 2024] |
| End-to-end VLA | Single model maps vision + language to motor actions | Promises generalization but introduces latency and debugging complexity |
| Residual / hierarchical policies | A base policy handles locomotion while a residual or skill policy handles manipulation | Helps factor balance and manipulation in whole-body tasks |

**Sources and evidence**:
- π0 uses a flow-matching action expert to generate continuous actions and reports strong performance on multi-step bimanual manipulation tasks [π0 2024].
- OpenVLA formulates manipulation as autoregressive token prediction and shows competitive zero-shot performance across multiple robot platforms [OpenVLA 2024].
- GR00T N1 explicitly targets bimanual humanoid manipulation tasks such as nut pouring and exhaust-pipe sorting in simulation, with a policy head designed for high-frequency motor output [GR00T N1 2025].

### 3.4 World Models, Simulation, and Sim-to-Real Transfer

World models learn to predict future states, rewards, or observations. For humanoids, they are used to compress experience, plan rollouts, and generate synthetic training data. Sim-to-real transfer bridges the physics and sensor gaps between simulation and deployment.

| Technique | Purpose | Notes |
|-----------|---------|-------|
| Domain randomization | Randomize mass, friction, actuator gains, and sensor noise during training | Increases robustness but can degrade optimality if randomization is too broad |
| System identification | Estimate real robot parameters from data to align simulation | Improves transfer fidelity; requires instrumented experiments |
| World models (Dreamer, TD-MPC, etc.) | Predict dynamics for planning and data-efficient RL | Useful for long-horizon reasoning; accuracy degrades with contact-rich humanoid dynamics |
| Sim-to-real RL pipelines | Train entirely in GPU simulation, deploy zero-shot | Seo et al. (2025) demonstrate this for humanoid locomotion [Seo et al. 2025] |

**Sources and evidence**:
- Seo et al. (2025) report a practical sim-to-real recipe for humanoid locomotion in which a policy is trained with massively parallel reinforcement learning and transferred to hardware without real-world training [Seo et al. 2025].
- HumanoidBench is explicitly designed to benchmark whole-body locomotion and manipulation algorithms in simulation before costly hardware deployment [HumanoidBench 2024].
- Goldberg (2025) contends that closing the data gap for robot manipulation requires engineering simulators and data-collection systems that capture physical contact and human intent, rather than relying on raw scale [Goldberg 2025].

### 3.5 Task Planning, Reasoning, and Hierarchical Architectures

Long-horizon autonomy requires decomposing instructions into subtasks, selecting skills, and handling failures. Hierarchical architectures typically separate a slow, deliberative reasoning module from a fast, reactive control module.

| Layer | Function | Example approaches |
|-------|----------|--------------------|
| High-level planner | Parse language goals, generate subgoal sequences, and monitor progress | LLM/VLM planners; chain-of-thought reasoning in RT-2 [RT-2 2023] |
| Skill library | Reusable low-level behaviors (grasp, place, walk-to) | Retrieval, structured skill priors, or learned option policies |
| Low-level policy | Execute high-frequency motor commands | VLA action expert, RL policy, or MPC controller |

**Sources and evidence**:
- RT-2 showed that chain-of-thought reasoning emerging from vision-language pretraining can support multi-step manipulation planning, although reliability remains task-dependent [RT-2 2023].
- GR00T N1 adopts a dual-system design: a VLM-based reasoning module (System 2) and a Diffusion Transformer action module (System 1), explicitly separating high-level interpretation from high-frequency control [GR00T N1 2025].
- The 2026 Stanford AI Index reports that industry produced over 90% of notable frontier AI models in 2025, highlighting the concentration of foundation-model development in a small set of well-resourced organizations [AI Index 2026].

> **Speculative note**: It is plausible that future humanoid systems will ship with a small set of foundation policies plus customer-specific fine-tuning rather than fully general zero-shot models. The reasoning is that actuator dynamics, sensor calibrations, and safety envelopes vary enough across platforms that embodiment-agnostic policies remain limited without targeted adaptation.

---

## 4. Relationship Patterns to Other Domains

| From | To | Relationship | Rationale |
|------|-----|--------------|-----------|
| `07_ai_models_algorithms` | `02_components_supply_chain` | `requires` | VLAs and foundation policies require edge GPUs, high-bandwidth sensors, torque-dense actuators, and low-latency buses |
| `07_ai_models_algorithms` | `06_design_engineering` | `constrains` / `enables` | Control frequency, joint range, and morphology choices determine feasible policies; learned policies can compensate for some hardware limitations |
| `07_ai_models_algorithms` | `08_software_middleware` | `requires` | Algorithms depend on real-time OS, middleware (ROS 2, DDS), simulators, and deployment pipelines for execution |
| `07_ai_models_algorithms` | `09_data_datasets` | `consumes` | Models consume teleoperation demonstrations, motion capture, simulation logs, and multimodal datasets |
| `07_ai_models_algorithms` | `10_evaluation_benchmarks` | `requires` | Development and procurement of AI models require reproducible benchmarks (e.g., HumanoidBench, real-world task suites) |
| `07_ai_models_algorithms` | `11_applications_markets` | `enables` | Perception, planning, and control algorithms determine which industrial tasks are economically and technically viable |
| `07_ai_models_algorithms` | `12_policy_regulation_ethics` | `is_regulated_by` | Safety certification, liability, and autonomy frameworks constrain acceptable algorithm behavior |

---

## 5. Controlled Vocabulary

### 5.1 Category Tags

- `vla_model` — vision-language-action models that output motor commands.
- `foundation_model` — large pretrained models adapted to embodied control.
- `locomotion_policy` — policies for walking, running, balancing, and terrain traversal.
- `manipulation_policy` — policies for grasping, placing, tool use, and dexterous manipulation.
- `loco_manipulation` — combined locomotion and manipulation tasks.
- `world_model` — learned predictive models of environment dynamics.
- `sim_to_real` — methods that transfer policies from simulation to real hardware.
- `imitation_learning` — policies trained from demonstrations.
- `reinforcement_learning` — policies trained through environment reward signals.
- `task_planner` — high-level reasoning and subgoal decomposition.
- `whole_body_control` — coordination of all joints under physical constraints.
- `flow_matching` / `diffusion_policy` — generative continuous-action policies.

### 5.2 Relevant Entity Types

From the project information model:

- `technology`
- `paper`
- `dataset`
- `benchmark`
- `software_platform`

---

## 6. Key Sources

### 6.1 Primary / Authoritative Sources

1. **Bjorck, J., et al. (NVIDIA)**. *GR00T N1: An Open Foundation Model for Generalist Humanoid Robots* (2025). Describes a 2.2B-parameter dual-system VLA, training mixture, and embodiment-agnostic policy head for humanoid manipulation.  
   URL: https://arxiv.org/abs/2503.14734

2. **Black, K., et al. (Physical Intelligence)**. *π0: A Vision-Language-Action Flow Model for General Robot Control* (2024). Introduces a flow-matching action expert for continuous robot control and reports real-world manipulation results.  
   URL: https://arxiv.org/abs/2410.24164

3. **Kim, M., et al.** *OpenVLA: An Open-Source Vision-Language-Action Model* (2024). Presents a 7B-parameter open VLA trained on Open X-Embodiment data and evaluates cross-task generalization.  
   URL: https://arxiv.org/abs/2406.09246

4. **Zitkovich, S., et al. (Google DeepMind)**. *RT-2: Vision-Language-Action Models* (2023). Demonstrates fine-tuning web-pretrained VLMs for manipulation via tokenized actions and chain-of-thought reasoning.  
   URL: https://arxiv.org/abs/2307.15818

### 6.2 Domain-Specific Sources

5. **Sferrazza, C., et al. (UC Berkeley)**. *HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation* (2024). Provides a simulation benchmark based on Unitree H1 with over 40 locomotion and manipulation tasks.  
   URL: https://arxiv.org/abs/2403.10506

6. **Seo, Y., et al. (UC Berkeley / NVIDIA)**. *Learning Sim-to-Real Humanoid Locomotion in 15 Minutes* (2025). Reports a massively parallel RL pipeline that trains humanoid locomotion in simulation and transfers to real hardware.  
   URL: https://arxiv.org/abs/2512.01996

7. **Goldberg, K.** *Good old-fashioned engineering can close the 100,000-year "data gap" in robotics* (2025). *Science Robotics*, 10(105), eaea7390. Argues that deliberate sensor, simulator, and demonstration engineering is needed to close the robot-data gap.  
   URL: https://doi.org/10.1126/scirobotics.aea7390

### 6.3 Industry / Market Context

8. **Stanford HAI**. *2026 AI Index Report* (2026). Tracks global AI R&D trends, noting that industry produced over 90% of notable frontier models in 2025.  
   URL: https://hai.stanford.edu/ai-index/2026-ai-index-report

---

## 7. Open Questions

1. How well do VLA foundation models generalize across heterogeneous humanoid embodiments with different kinematics, sensor suites, and actuators without per-platform retraining?
2. What is the minimum real-world demonstration data required to deploy a reliable manipulation policy on a new humanoid platform, and can simulation-generated data close most of the gap?
3. Which combination of model architecture (autoregressive VLA vs. diffusion/flow action expert), inference hardware, and control rate meets industrial requirements for latency, cost, and safety?
4. How should the ontology represent hierarchical policies that span high-level task planning, whole-body control, and low-level motor commands while preserving verifiability?
