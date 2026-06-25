# 09 Data & Datasets

> **Domain Code**: `09_data_datasets`  
> **Layer**: Intelligence  
> **Status**: Draft — subject to review before v0.1.0  
> **Purpose**: Define the data assets, collection methods, pipelines, and governance concepts required to train, validate, and continuously improve humanoid robot systems at scale.

---

## 1. Central Question

> **What data is needed to train, evaluate, and continuously improve humanoid robots, and how can it be collected, curated, and governed at production scale?**

Humanoid robots learn their skills from data — teleoperated demonstrations, human motion capture, simulation rollouts, and real-world fleet logs. Unlike large language models, which can train on static internet text, embodied AI requires data that captures physical interaction: contact forces, actuator response, sensor noise, and recovery behaviors. This domain tracks the datasets, formats, infrastructure, and legal/ethical frameworks that turn raw recordings into reusable training fuel.

---

## 2. Scope

### 2.1 In Scope

- Teleoperation and human-demonstration datasets for whole-body humanoid control and manipulation.
- Cross-embodiment robot-learning datasets and standardized formats (e.g., RLDS).
- Human motion-capture (MoCap) datasets and retargeting pipelines.
- Simulation-generated and synthetic datasets, including world-model outputs.
- Multimodal datasets combining vision, language, action, proprioception, and force/tactile sensing.
- Data infrastructure: logging, labeling, storage, replay, fleet telemetry, and data flywheels.
- Data governance: licensing, privacy, consent, anonymization, security, and regulatory compliance.

### 2.2 Out of Scope

- The algorithms that consume data (covered in `07_ai_models_algorithms`).
- Middleware, simulators, and deployment tools as software products (covered in `08_software_middleware`).
- Evaluation protocols and benchmarks as measurement systems (covered in `10_evaluation_benchmarks`).
- General computer-vision or NLP datasets with no demonstrated robot-learning relevance.

---

## 3. Key Concepts

### 3.1 Teleoperation and Real-World Demonstration Data

Teleoperation allows a human operator to control a humanoid robot and record expert trajectories. These demonstrations are the primary source of high-quality, real-world data for imitation learning and behavior cloning.

| Data Source | Modality | Scale / Notable Facts | Humanoid Relevance |
|-------------|----------|----------------------|--------------------|
| **HumanPlus** (Fu et al., 2024) | RGB camera → whole-body shadowing | 33-DoF, 180 cm custom humanoid; tasks learned from ~40 demonstrations with 60–100% success | First full-stack system for humanoids to learn autonomous skills from egocentric human data [HumanPlus 2024]. |
| **OmniH2O-6** (He et al., 2024) | VR + whole-body teleoperation | Six everyday tasks; ~40 minutes of real-world demonstrations; paired RGB-D, motion goals, joint targets at 30 Hz | First released humanoid whole-body control dataset; enables autonomy via imitation or frontier models [OmniH2O 2024]. |
| **Industry teleoperation** | MoCap suits, VR headsets, exoskeletons | Tesla, Figure, and others operate dedicated data-collection teams wearing motion-capture gear for fleet learning | Demonstrates that data collection is becoming an operational role in humanoid mass-production pipelines [Tesla Job Posting 2025]. |

**Sources and evidence**:
- HumanPlus trained a low-level policy in simulation on 40 hours of human motion data, transferred it to the real world for RGB-camera-based shadowing, and used behavior cloning to learn tasks such as folding a sweatshirt, unloading warehouse racks, and typing [HumanPlus 2024].
- OmniH2O demonstrated whole-body teleoperation of a Unitree H1 with dexterous hands and released the OmniH2O-6 dataset with paired visual and motion data for six tasks [OmniH2O 2024].
- Tesla's "Data Collection Operator, Optimus" job posting describes operators wearing motion-capture suits and VR headsets to collect whole-body movement and manipulation data, indicating the industrialization of teleoperation data collection [Tesla Job Posting 2025].

### 3.2 Cross-Embodiment and Large-Scale Robot Datasets

Cross-embodiment datasets aggregate demonstrations from many robot platforms into a common format, enabling generalist policies that transfer across hardware. They are the closest equivalent in robotics to a "pre-training corpus."

| Dataset | Scope | Scale | Key Finding |
|---------|-------|-------|-------------|
| **Open X-Embodiment (OXE)** | 22 robot embodiments, 21 institutions | >1 million trajectories, 527 skills, 160,266 tasks | RT-2-X trained on OXE showed ~3× improvement on emergent skills compared with RT-2 trained only on Google robot data [Open X-Embodiment 2023]. |
| **DROID** | Franka Panda arms in 52 labs | 76,000 trajectories, 564 scenes | Designed for cross-embodiment pretraining with standardized protocols and diverse "in-the-wild" scenes [DROID 2024]. |
| **Bridge Data V2** | WidowX kitchen manipulation | ~60,000 demonstrations | Widely used open subset of OXE for low-cost manipulation research [Open X-Embodiment 2023]. |

**Sources and evidence**:
- The Open X-Embodiment Collaboration released the largest open robot-learning dataset to date and showed that a single high-capacity policy (RT-X) trained on mixed-robot data outperforms platform-specific policies, establishing cross-embodiment pretraining as a viable path [Open X-Embodiment 2023].
- DROID provides a large-scale, reproducible collection workflow and is used to study generalization across scenes and tasks [DROID 2024].
- These datasets are typically stored in RLDS (Robot Learning Dataset Specification) format, built on TensorFlow Datasets, with episodes containing observations, actions, rewards, and metadata [RLDS / OXE documentation].

> **Speculative note**: Whether cross-embodiment data is sufficient for high-degree-of-freedom humanoid control — as opposed to mostly single-arm manipulation — remains an open research question. Humanoid-specific datasets may still be required for whole-body dynamics and balance.

### 3.3 Human Motion Capture and Retargeting Data

Human motion is a rich prior for humanoid robots because of their similar kinematic structure. MoCap datasets provide reference motions that can be retargeted to robot joint space and used to train low-level skills or motion priors.

| Dataset / System | Content | Use Case |
|------------------|---------|----------|
| **AMASS** | Large-scale human motion capture in SMPL format | Pretraining motion priors and retargeting to humanoid kinematics [Clone 2025; CLOT 2026]. |
| **ExBody / ExBody2** | Expressive whole-body humanoid control from human motion | Training humanoid robots to perform diverse, dynamic human motions [ExBody2 2024]. |
| **CLOT human motion dataset** | ~20 hours of OptiTrack-captured full-body motion at 120 Hz | Tailored for humanoid teleoperation; includes walking, running, martial arts, dance, and balancing [CLOT 2026]. |

**Sources and evidence**:
- CLOT captures over 20 hours of full-body human motion with explicit consideration of foot-contact consistency and humanoid actuation limits, then retargets it online to a 31-DoF Adam Pro humanoid for closed-loop teleoperation [CLOT 2026].
- Clone augments AMASS through motion editing and collects additional MoCap data specifically for humanoid controllers, noting that animation-oriented datasets underrepresent the kinematic configurations and dynamic transitions needed for real-world control [Clone 2025].
- ExBody2 advances expressive whole-body humanoid control using human motion data and reinforcement learning [ExBody2 2024].

### 3.4 Simulation, Synthetic Data, and World Models

Simulation can generate data at scales that are impractical to collect physically. Synthetic data is especially valuable for rare scenarios, contact-rich manipulation, and safety-critical edge cases.

| Platform / Dataset | Output | Claim / Result |
|--------------------|--------|----------------|
| **NVIDIA Isaac GR00T Blueprint** | Synthetic humanoid motion trajectories | Generated 780,000 synthetic trajectories (~6,500 human-demonstration hours) in 11 hours; combining synthetic + real data improved GR00T N1 performance by 40% versus real data alone [NVIDIA GR00T N1 2025]. |
| **HumanoidBench** | Simulated benchmark tasks | 27 whole-body locomotion and manipulation tasks in MuJoCo; state-of-the-art RL algorithms struggle, highlighting the need for better data and hierarchical methods [HumanoidBench 2024]. |
| **DexGraspNet** | Synthetic dexterous grasps | 1.32 million ShadowHand grasps on 5,355 objects across 133 categories, generated in NVIDIA Isaac Sim [DexGraspNet 2024]. |

**Sources and evidence**:
- NVIDIA's GR00T N1 announcement states that synthetic data generation, built on Omniverse and Cosmos world models, can multiply limited human demonstrations into large training corpora and measurably improve foundation-model performance [NVIDIA GR00T N1 2025].
- HumanoidBench provides a high-dimensional simulated environment with a Unitree H1-like model and dexterous hands, designed to accelerate algorithmic research without fragile hardware [HumanoidBench 2024].
- DexGraspNet demonstrates that simulation can produce grasp datasets orders of magnitude larger than prior real-world collections, with demonstrated sim-to-real transfer [DexGraspNet 2024].

> **Speculative note**: The long-term ratio of synthetic-to-real data in production humanoid training is uncertain. Current evidence suggests that synthetic data is a powerful multiplier but not yet a full replacement for real-world physical interaction data.

### 3.5 Data Governance, Licensing, and Privacy

As humanoid robots deploy in homes, factories, and public spaces, the data they collect raises governance questions: who owns the data, what consent is required, how long it is retained, and how it is secured.

| Concern | Relevant Framework / Practice | Humanoid Relevance |
|---------|------------------------------|--------------------|
| **Personal data collection** | GDPR (EU), CCPA/CPRA (California), BIPA (Illinois) | Cameras, microphones, LiDAR, and 3D home maps can capture faces, voices, and spatial layouts; privacy impact assessments are typically required [Robot Data Privacy Guide 2026; Kite Compliance 2025]. |
| **Data minimization & anonymization** | On-device processing, face blurring, pseudonymization | Reduces regulatory risk and storage cost; aligns with GDPR data-minimization and storage-limitation principles [Robot Data Privacy Guide 2026]. |
| **Security & telemetry** | Encrypted channels, secure boot, vendor DPAs | Researchers have observed humanoid robots transmitting telemetry without visible consent mechanisms, creating GDPR and cybersecurity concerns [Help Net Security 2025]. |
| **Dataset licensing** | Per-subset licenses in OXE, Creative Commons, commercial restrictions | Mixed licensing in aggregated datasets complicates commercial use and redistribution [Open X-Embodiment 2023]. |

**Sources and evidence**:
- A robot data-privacy compliance guide notes that camera-equipped robots in warehouses or public spaces collect personal data subject to GDPR, CCPA, and BIPA, with GDPR penalties up to 4% of global annual revenue [Robot Data Privacy Guide 2026].
- Kite Compliance identifies privacy, bias, and transparency as one of four pillars of humanoid robot compliance, alongside physical safety, functional safety, and cybersecurity [Kite Compliance 2025].
- A 2025 security analysis of a consumer humanoid robot found unencrypted DDS traffic, disabled TLS certificate checks, and automatic telemetry transmissions including camera, microphone, and spatial data, highlighting concrete cybersecurity gaps [Help Net Security 2025].

---

## 4. Relationship Patterns to Other Domains

| From | To | Relationship | Rationale |
|------|-----|--------------|-----------|
| `09_data_datasets` | `07_ai_models_algorithms` | `is_prerequisite_for` | Datasets are the training substrate for VLA models, world models, locomotion/manipulation policies, and imitation-learning algorithms. |
| `09_data_datasets` | `08_software_middleware` | `requires` | Data pipelines depend on simulators (Isaac Sim, MuJoCo), middleware (ROS 2, DDS), logging frameworks, and fleet-management tools. |
| `09_data_datasets` | `02_components_supply_chain` | `requires` | Data collection requires sensors, edge compute, storage, and network bandwidth; component fidelity limits signal quality and frequency. |
| `09_data_datasets` | `10_evaluation_benchmarks` | `is_prerequisite_for` / `verified_by` | Benchmarks need representative datasets to train and test policies; evaluation results feed back into dataset curation. |
| `09_data_datasets` | `04_assembly_integration_testing` | `produces` | System integration and field testing generate telemetry, failure logs, and demonstration data that close the data loop. |
| `09_data_datasets` | `11_applications_markets` | `serves` / `drives_demand_for` | Application-specific tasks define what data must be collected; deployment scale creates demand for fleet-data infrastructure. |
| `09_data_datasets` | `12_policy_regulation_ethics` | `is_regulated_by` | Data collection, retention, and sharing are governed by privacy law, safety standards, and emerging AI/data-governance regulation. |

---

## 5. Controlled Vocabulary

### 5.1 Data Categories

- `teleoperation_data`
- `human_demonstration_data`
- `motion_capture_data`
- `cross_embodiment_data`
- `simulation_data`
- `synthetic_data`
- `multimodal_dataset`
- `vision_language_action_dataset`
- `fleet_telemetry`
- `failure_log`
- `world_model_data`

### 5.2 Relevant Entity Types

From the project information model:

- `dataset`
- `benchmark`
- `software_platform`
- `paper`
- `report`
- `technology`
- `policy`

---

## 7. Key Sources

### 7.1 Primary / Authoritative Sources

1. **Fu, Z. et al.** *HumanPlus: Humanoid Shadowing and Imitation from Humans* (2024). arXiv:2406.10454. Introduces a full-stack pipeline for humanoids to learn motion and autonomous skills from human data via shadowing and behavior cloning.  
   URL: https://arxiv.org/abs/2406.10454

2. **He, T. et al.** *OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning* (2024). arXiv:2406.08858. Presents a whole-body teleoperation system and releases the OmniH2O-6 humanoid dataset.  
   URL: https://arxiv.org/abs/2406.08858

3. **Open X-Embodiment Collaboration.** *Open X-Embodiment: Robotic Learning Datasets and RT-X Models* (2023). arXiv:2310.08864. Assembles >1M trajectories from 22 robot embodiments across 21 institutions and demonstrates cross-embodiment transfer with RT-X.  
   URL: https://arxiv.org/abs/2310.08864

4. **Sferrazza, C. et al.** *HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation* (2024). arXiv:2403.10506. Provides a 27-task MuJoCo benchmark for humanoid learning and control.  
   URL: https://arxiv.org/abs/2403.10506

### 7.2 Industry and Market Analysis

5. **NVIDIA.** *Accelerate Generalist Humanoid Robot Development with NVIDIA Isaac GR00T N1* (2025). Describes GR00T N1, synthetic-data generation blueprints, and the claim that synthetic + real data improved model performance by 40%.  
   URL: https://developer.nvidia.com/blog/accelerate-generalist-humanoid-robot-development-with-nvidia-isaac-gr00t-n1/

6. **Khazatsky, A. et al.** *DROID: A Large-Scale In-the-Wild Robot Manipulation Dataset* (2024). arXiv:2403.12945. Documents a 76K-trajectory, 564-scene, 52-lab manipulation dataset for cross-embodiment research.  
   URL: https://arxiv.org/abs/2403.12945

### 7.3 Domain-Specific Sources

7. **Robotomated.** *Robot Data Privacy: GDPR, CCPA, and Camera-Equipped Robot Compliance* (2026). Practical guide to privacy frameworks, data-minimization practices, and compliance penalties for camera-equipped robots.  
   URL: https://robotomated.com/learn/guides/robot-data-privacy-compliance

8. **Tesla.** *Data Collection Operator, Optimus* job posting (2025). Operational evidence of motion-capture and VR-based whole-body data collection for humanoid development.  
   URL: https://www.tesla.com/careers/search/job/data-collection-operator-optimus-222857

---

## 8. Open Questions

1. What is the optimal mix of real teleoperation, synthetic simulation, and cross-embodiment data for training generalist humanoid policies, and how does it vary by task (locomotion vs. manipulation vs. long-horizon planning)?
2. How should the ontology represent dataset quality dimensions — such as action-space consistency, embodiment gap, contact-richness, and annotation density — so that downstream model builders can reason about fitness-for-use?
3. What data-governance frameworks and technical standards are needed for industrial humanoid fleets that continuously record video, audio, and worker-interaction data in factories or warehouses?
4. How can the community build open humanoid datasets that are large enough to rival proprietary industrial collections without exposing individuals, facilities, or intellectual property to privacy or security risks?
