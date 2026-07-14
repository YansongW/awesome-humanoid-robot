---
$id: ent_paper_nelson_open_h_embodiment_a_large_scal_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Open-H-Embodiment: A Large-Scale Dataset for Enabling Foundation Models in Medical Robotics'
  zh: Open-H-Embodiment：面向医疗机器人基础模型的大规模数据集
  ko: 'Open-H-Embodiment: 의료 로봇의 기초 모델을 위한 대규모 데이터셋'
summary:
  en: Introduces Open-H-Embodiment, a 780-hour multimodal dataset of synchronized medical robotic video, language, and kinematics
    spanning more than 50 institutions and 20 robotic platforms, and presents GR00T-H and Cosmos-H-Surgical-Simulator as foundation
    models for surgical vision-language-action learning and world simulation.
  zh: 介绍了Open-H-Embodiment，一个涵盖50多家机构、20种机器人平台、780小时同步医疗机器人视频、语言与运动学数据的多模态数据集，并提出了用于外科视觉-语言-动作学习与世界仿真的基础模型GR00T-H和Cosmos-H-Surgical-Simulator。
  ko: 50개 이상의 기관과 20개의 로봇 플랫폼에서 수집된 780시간의 동기화된 의료 로봇 영상, 언어 및 운동학 데이터인 Open-H-Embodiment를 소개하고, 외과 VLA 학습 및 세계 시뮬레이션을 위한
    기초 모델인 GR00T-H와 Cosmos-H-Surgical-Simulator를 제시한다.
domains:
- 09_data_datasets
- 07_ai_models_algorithms
- 10_evaluation_benchmarks
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- medical_robotics
- surgical_robotics
- vla
- vision_language_action
- foundation_model
- cross_embodiment
- dataset
- world_model
- simulation
- kinematics
- surgical_simulation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.21017v3.
sources:
- id: src_001
  type: paper
  title: 'Open-H-Embodiment: A Large-Scale Dataset for Enabling Foundation Models in Medical Robotics'
  url: https://arxiv.org/abs/2604.21017
  date: '2026'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
related_entities:
- id: ent_dataset_open_x_embodiment
  relationship: cites
  description:
    en: The paper cites Open-X-Embodiment as related large-scale robotic learning infrastructure.
    zh: 本文引用Open-X-Embodiment作为相关的大规模机器人学习基础设施。
    ko: 본 논문은 관련 대규모 로봇 학습 인프라로 Open-X-Embodiment를 인용한다.
---
## 概述
Autonomous medical robots hold promise to improve patient outcomes, reduce provider workload, democratize access to care, and enable superhuman precision. However, autonomous medical robotics has been limited by a fundamental data problem: existing medical robotic datasets are small, single-embodiment, and rarely shared openly, restricting the development of foundation models that the field needs to advance. We introduce Open-H-Embodiment, the largest open dataset of medical robotic video with synchronized kinematics to date, spanning more than 50 institutions and multiple robotic platforms including the CMR Versius, Intuitive Surgical's da Vinci, da Vinci Research Kit (dVRK), Rob Surgical BiTrack, Virtual Incision's MIRA, Moon Surgical Maestro, and a variety of custom systems, spanning surgical manipulation, robotic ultrasound, and endoscopy procedures. We demonstrate the research enabled by this dataset through two foundation models. GR00T-H is the first open foundation vision-language-action model for medical robotics, which is the only evaluated model to achieve full end-to-end task completion on a structured suturing benchmark (25% of trials vs. 0% for all others) and achieves 64% average success across a 29-step ex vivo suturing sequence. We also train Cosmos-H-Surgical-Simulator, the first action-conditioned world model to enable multi-embodiment surgical simulation from a single checkpoint, spanning nine robotic platforms and supporting in silico policy evaluation and synthetic data generation for the medical domain. These results suggest that open, large-scale medical robot data collection can serve as critical infrastructure for the research community, enabling advances in robot learning, world modeling, and beyond.

## 核心内容
Autonomous medical robots hold promise to improve patient outcomes, reduce provider workload, democratize access to care, and enable superhuman precision. However, autonomous medical robotics has been limited by a fundamental data problem: existing medical robotic datasets are small, single-embodiment, and rarely shared openly, restricting the development of foundation models that the field needs to advance. We introduce Open-H-Embodiment, the largest open dataset of medical robotic video with synchronized kinematics to date, spanning more than 50 institutions and multiple robotic platforms including the CMR Versius, Intuitive Surgical's da Vinci, da Vinci Research Kit (dVRK), Rob Surgical BiTrack, Virtual Incision's MIRA, Moon Surgical Maestro, and a variety of custom systems, spanning surgical manipulation, robotic ultrasound, and endoscopy procedures. We demonstrate the research enabled by this dataset through two foundation models. GR00T-H is the first open foundation vision-language-action model for medical robotics, which is the only evaluated model to achieve full end-to-end task completion on a structured suturing benchmark (25% of trials vs. 0% for all others) and achieves 64% average success across a 29-step ex vivo suturing sequence. We also train Cosmos-H-Surgical-Simulator, the first action-conditioned world model to enable multi-embodiment surgical simulation from a single checkpoint, spanning nine robotic platforms and supporting in silico policy evaluation and synthetic data generation for the medical domain. These results suggest that open, large-scale medical robot data collection can serve as critical infrastructure for the research community, enabling advances in robot learning, world modeling, and beyond.

## 参考
- http://arxiv.org/abs/2604.21017v3

