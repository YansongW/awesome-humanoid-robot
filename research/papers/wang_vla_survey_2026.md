---
$id: "ent_paper_wang_vla_survey_2026"
$schema: "../../data/schema/v1/entry_schema.json"
$version: 1

type: "paper"

names:
  en: "Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines"
  zh: "机器人视觉-语言-动作：数据集、基准与数据引擎综述"
  ko: "로보틱스에서의 비전-언어-액션: 데이터셋, 벤치마크 및 데이터 엔진에 대한 서베이"

summary:
  en: "A 2026 survey arguing that VLA progress now depends more on data infrastructure and evaluation co-design than on model architecture, organized around datasets, benchmarks, and data engines."
  zh: "2026 年综述，认为 VLA 的进展现在更多取决于数据基础设施与评测协议的协同设计，而非模型架构本身；围绕数据集、基准与数据引擎三大支柱展开。"
  ko: "2026년 서베이로, VLA의 발전은 모델 아키텍처보다 데이터 인프라와 평가 공동 설계에 더 많이 의존하고 있으며, 데이터셋, 벤치마크, 데이터 엔진 세 축으로 구성됨."

domains:
  - "07_ai_models_algorithms"
  - "08_software_middleware"
  - "09_data_datasets"
  - "10_evaluation_benchmarks"

layers:
  - "intelligence"
  - "validation_markets"

functional_roles:
  - "knowledge"
  - "intelligence"

tags:
  - "vla"
  - "vision_language_action"
  - "survey"
  - "datasets"
  - "benchmarks"
  - "data_engines"
  - "sim_to_real"
  - "embodied_ai"

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-22"
  confidence: "high"
  notes: "Abstract, full PDF, and author list retrieved directly from arXiv. Claims about scope and arguments are based on the published manuscript."

sources:
  - id: "src_paper_wang_vla_survey_2026"
    type: "paper"
    title: "Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines"
    url: "https://arxiv.org/abs/2604.23001"
    date: "2026-04-24"
    accessed_at: "2026-06-22"

related_entities:
  - id: "ent_dataset_open_x_embodiment"
    relationship: "cites"
    description:
      en: "The survey cites Open X-Embodiment as a widely used cross-embodiment pretraining dataset."
      zh: "该综述引用 Open X-Embodiment 作为常用的跨具身预训练数据集。"
      ko: "해당 서베이는 Open X-Embodiment를 널리 사용되는 cross-embodiment 사전 학습 데이터셋으로 인용함."
  - id: "ent_dataset_droid"
    relationship: "cites"
    description:
      en: "The survey cites DROID as a distributed real-world dataset emphasizing visual and environmental variation."
      zh: "该综述引用 DROID 作为强调视觉与环境变化的分布式真实世界数据集。"
      ko: "해당 서베이는 DROID를 시각 및 환경 변화를 강조하는 분산 실제 데이터셋으로 인용함."
  - id: "ent_benchmark_humanoidbench"
    relationship: "cites"
    description:
      en: "The survey discusses HumanoidBench as a simulation benchmark for whole-body locomotion and manipulation."
      zh: "该综述讨论 HumanoidBench 作为全身运动与操作的仿真基准。"
      ko: "해당 서베이는 HumanoidBench를 전신 로코모션 및 조작을 위한 시뮬레이션 벤치마크로 논의함."
  - id: "ent_benchmark_libero"
    relationship: "cites"
    description:
      en: "The survey cites LIBERO as a representative short-horizon table-top VLA benchmark."
      zh: "该综述引用 LIBERO 作为代表性短程桌面 VLA 基准。"
      ko: "해당 서베이는 LIBERO를 대표적인 단기 테이블탑 VLA 벤치마크로 인용함."
  - id: "ent_tech_mimicgen"
    relationship: "cites"
    description:
      en: "The survey discusses MimicGen as a demonstration augmentation method that scales simulator data."
      zh: "该综述讨论 MimicGen 作为扩展仿真器数据的演示增强方法。"
      ko: "해당 서베이는 MimicGen을 시뮬레이터 데이터를 확장하는 데모 증강 방법으로 논의함."
  - id: "ent_tech_robogen"
    relationship: "cites"
    description:
      en: "The survey discusses RoboGen as an LLM-driven automatic task-generation framework for simulation."
      zh: "该综述讨论 RoboGen 作为由大语言模型驱动的仿真自动任务生成框架。"
      ko: "해당 서베이는 RoboGen을 LLM 기반 시뮬레이션 자동 작업 생성 프레임워크로 논의함."
---

# Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines

## 生活实例 + 自然语言阐述逻辑

> **生活实例**：它就像一份报告指出：自动驾驶进步的关键不再是造更炫的车，而是要有更好的地图、更真实的测试场和源源不断的驾驶数据。

> **自然语言逻辑**：这篇 2026 年综述把 VLA 研究重心从模型架构转向数据基础设施，系统梳理了数据集、基准测试和数据引擎三大支柱；它对人形机器人尤为相关，因为人形需要全身、接触丰富的动作数据，而这些真实数据采集成本高、数量少，亟需更好的数据生成与评测体系。

## Overview

This survey (Wang et al., 2026) reframes the VLA research agenda around its data infrastructure. The authors argue that future gains will come less from architectural novelty and more from co-designing high-fidelity data engines with structured evaluation protocols.

## Three Pillars

### 1. Datasets

- **Real-world datasets**: Open X-Embodiment, DROID, BridgeData V2, RH20T, RT-1, RT-2, Ego4D.
- **Synthetic datasets**: SynGrasp-1B, RoboCasa, LIBERO, CALVIN, Meta-World, RLBench, BEHAVIOR-1K, VLABench.
- **Core trade-off**: high-fidelity real data is costly and hard to scale; synthetic data is scalable but limited in physical realism.

### 2. Benchmarks

- Analyzed along two dimensions: **task complexity** (atomic → compositional/long-horizon) and **environment structure** (tabletop → multi-scene).
- Table-top examples: Meta-World, LIBERO, LIBERO-plus/PRO/X, SimplerEnv, CALVIN, GemBench, COLOSSEUM.
- Multi-scene examples: BEHAVIOR-1K, VLABench, Open X-Embodiment.
- Identified gap: existing protocols under-evaluate compositional generalization and long-horizon reasoning.

### 3. Data Engines

- **Video-to-data engines**: H2R, RoboWheel, Video2Policy, X-Humanoid, GenMimic, UniSim.
- **Hardware-assisted engines**: teleoperation and embodied sensing interfaces.
- **Generative engines**: RoboGen, MimicGen, simulation-based procedural generation.
- Shared limitation: physical grounding and sim-to-real transfer remain hard.

## Four Open Challenges

1. **Representation alignment** across heterogeneous embodiments.
2. **Multimodal supervision** that fuses vision, language, force, audio, etc.
3. **Reasoning assessment** for compositional and long-horizon tasks.
4. **Scalable data generation** that preserves physical realism.

## Relevance to Humanoid Robotics

Humanoid robots are the most embodiment-complex target for VLA systems. The paper's data-centric framing is directly applicable because:

- Humanoids require whole-body action spaces (DoF-level control) and diverse contact-rich manipulation.
- Real-world humanoid demonstration data is even more expensive to collect than arm-only data.
- Sim-to-real transfer for humanoids is harder due to contact dynamics, balance, and morphological diversity.
- Benchmarks like HumanoidBench are specifically mentioned as simulation testbeds for whole-body VLA.
