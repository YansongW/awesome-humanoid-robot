---
$id: ent_paper_wang_vla_survey_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines'
  zh: 机器人视觉-语言-动作：数据集、基准与数据引擎综述
  ko: '로보틱스에서의 비전-언어-액션: 데이터셋, 벤치마크 및 데이터 엔진에 대한 서베이'
summary:
  en: A 2026 survey arguing that VLA progress now depends more on data infrastructure and evaluation co-design than on model
    architecture, organized around datasets, benchmarks, and data engines.
  zh: 2026 年综述，认为 VLA 的进展现在更多取决于数据基础设施与评测协议的协同设计，而非模型架构本身；围绕数据集、基准与数据引擎三大支柱展开。
  ko: 2026년 서베이로, VLA의 발전은 모델 아키텍처보다 데이터 인프라와 평가 공동 설계에 더 많이 의존하고 있으며, 데이터셋, 벤치마크, 데이터 엔진 세 축으로 구성됨.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 09_data_datasets
- 10_evaluation_benchmarks
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- vla
- vision_language_action
- survey
- datasets
- benchmarks
- data_engines
- sim_to_real
- embodied_ai
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.23001v1.
sources:
- id: src_paper_wang_vla_survey_2026
  type: paper
  title: 'Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines'
  url: https://arxiv.org/abs/2604.23001
  date: '2026-04-24'
  accessed_at: '2026-06-22'
related_entities:
- id: ent_dataset_open_x_embodiment
  relationship: cites
  description:
    en: The survey cites Open X-Embodiment as a widely used cross-embodiment pretraining dataset.
    zh: 该综述引用 Open X-Embodiment 作为常用的跨具身预训练数据集。
    ko: 해당 서베이는 Open X-Embodiment를 널리 사용되는 cross-embodiment 사전 학습 데이터셋으로 인용함.
- id: ent_dataset_droid
  relationship: cites
  description:
    en: The survey cites DROID as a distributed real-world dataset emphasizing visual and environmental variation.
    zh: 该综述引用 DROID 作为强调视觉与环境变化的分布式真实世界数据集。
    ko: 해당 서베이는 DROID를 시각 및 환경 변화를 강조하는 분산 실제 데이터셋으로 인용함.
- id: ent_benchmark_humanoidbench
  relationship: cites
  description:
    en: The survey discusses HumanoidBench as a simulation benchmark for whole-body locomotion and manipulation.
    zh: 该综述讨论 HumanoidBench 作为全身运动与操作的仿真基准。
    ko: 해당 서베이는 HumanoidBench를 전신 로코모션 및 조작을 위한 시뮬레이션 벤치마크로 논의함.
- id: ent_benchmark_libero
  relationship: cites
  description:
    en: The survey cites LIBERO as a representative short-horizon table-top VLA benchmark.
    zh: 该综述引用 LIBERO 作为代表性短程桌面 VLA 基准。
    ko: 해당 서베이는 LIBERO를 대표적인 단기 테이블탑 VLA 벤치마크로 인용함.
- id: ent_tech_mimicgen
  relationship: cites
  description:
    en: The survey discusses MimicGen as a demonstration augmentation method that scales simulator data.
    zh: 该综述讨论 MimicGen 作为扩展仿真器数据的演示增强方法。
    ko: 해당 서베이는 MimicGen을 시뮬레이터 데이터를 확장하는 데모 증강 방법으로 논의함.
- id: ent_tech_robogen
  relationship: cites
  description:
    en: The survey discusses RoboGen as an LLM-driven automatic task-generation framework for simulation.
    zh: 该综述讨论 RoboGen 作为由大语言模型驱动的仿真自动任务生成框架。
    ko: 해당 서베이는 RoboGen을 LLM 기반 시뮬레이션 자동 작업 생성 프레임워크로 논의함.
theoretical_depth:
- system
---
## 概述
Despite remarkable progress in Vision--Language--Action (VLA) models, a central bottleneck remains underexamined: the data infrastructure that underlies embodied learning. In this survey, we argue that future advances in VLA will depend less on model architecture and more on the co-design of high-fidelity data engines and structured evaluation protocols. To this end, we present a systematic, data-centric analysis of VLA research organized around three pillars: datasets, benchmarks, and data engines. For datasets, we categorize real-world and synthetic corpora along embodiment diversity, modality composition, and action space formulation, revealing a persistent fidelity-cost trade-off that fundamentally constrains large-scale collection. For benchmarks, we analyze task complexity and environment structure jointly, exposing structural gaps in compositional generalization and long-horizon reasoning evaluation that existing protocols fail to address. For data engines, we examine simulation-based, video-reconstruction, and automated task-generation paradigms, identifying their shared limitations in physical grounding and sim-to-real transfer. Synthesizing these analyses, we distill four open challenges: representation alignment, multimodal supervision, reasoning assessment, and scalable data generation. Addressing them, we argue, requires treating data infrastructure as a first-class research problem rather than a background concern.

## 核心内容
Despite remarkable progress in Vision--Language--Action (VLA) models, a central bottleneck remains underexamined: the data infrastructure that underlies embodied learning. In this survey, we argue that future advances in VLA will depend less on model architecture and more on the co-design of high-fidelity data engines and structured evaluation protocols. To this end, we present a systematic, data-centric analysis of VLA research organized around three pillars: datasets, benchmarks, and data engines. For datasets, we categorize real-world and synthetic corpora along embodiment diversity, modality composition, and action space formulation, revealing a persistent fidelity-cost trade-off that fundamentally constrains large-scale collection. For benchmarks, we analyze task complexity and environment structure jointly, exposing structural gaps in compositional generalization and long-horizon reasoning evaluation that existing protocols fail to address. For data engines, we examine simulation-based, video-reconstruction, and automated task-generation paradigms, identifying their shared limitations in physical grounding and sim-to-real transfer. Synthesizing these analyses, we distill four open challenges: representation alignment, multimodal supervision, reasoning assessment, and scalable data generation. Addressing them, we argue, requires treating data infrastructure as a first-class research problem rather than a background concern.

## 参考
- http://arxiv.org/abs/2604.23001v1

