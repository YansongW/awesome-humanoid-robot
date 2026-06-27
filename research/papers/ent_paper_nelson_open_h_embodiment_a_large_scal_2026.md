---
$id: ent_paper_nelson_open_h_embodiment_a_large_scal_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Open-H-Embodiment: A Large-Scale Dataset for Enabling Foundation Models in
    Medical Robotics'
  zh: Open-H-Embodiment：面向医疗机器人基础模型的大规模数据集
  ko: 'Open-H-Embodiment: 의료 로봇의 기초 모델을 위한 대규모 데이터셋'
summary:
  en: Introduces Open-H-Embodiment, a 780-hour multimodal dataset of synchronized
    medical robotic video, language, and kinematics spanning more than 50 institutions
    and 20 robotic platforms, and presents GR00T-H and Cosmos-H-Surgical-Simulator
    as foundation models for surgical vision-language-action learning and world simulation.
  zh: 介绍了Open-H-Embodiment，一个涵盖50多家机构、20种机器人平台、780小时同步医疗机器人视频、语言与运动学数据的多模态数据集，并提出了用于外科视觉-语言-动作学习与世界仿真的基础模型GR00T-H和Cosmos-H-Surgical-Simulator。
  ko: 50개 이상의 기관과 20개의 로봇 플랫폼에서 수집된 780시간의 동기화된 의료 로봇 영상, 언어 및 운동학 데이터인 Open-H-Embodiment를
    소개하고, 외과 VLA 학습 및 세계 시뮬레이션을 위한 기초 모델인 GR00T-H와 Cosmos-H-Surgical-Simulator를 제시한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the provided metadata and abstract; quantitative claims
    (780 hours, 50+ institutions, 20 platforms, 25% SutureBot success, 64% ex vivo
    success) are taken from the supplied metadata and should be spot-checked against
    the arXiv PDF before full verification.
sources:
- id: src_001
  type: paper
  title: 'Open-H-Embodiment: A Large-Scale Dataset for Enabling Foundation Models
    in Medical Robotics'
  url: https://arxiv.org/abs/2604.21017
  date: '2026'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
related_entities:
- id: ent_dataset_open_x_embodiment
  relationship: cites
  description:
    en: The paper cites Open-X-Embodiment as related large-scale robotic learning
      infrastructure.
    zh: 本文引用Open-X-Embodiment作为相关的大规模机器人学习基础设施。
    ko: 본 논문은 관련 대규모 로봇 학습 인프라로 Open-X-Embodiment를 인용한다.
---

## Overview

Open-H-Embodiment addresses the data bottleneck in autonomous medical robotics by collecting and releasing the largest open dataset of medical robotic video with synchronized kinematics to date. The dataset comprises 780 hours, 119 sub-datasets, data from more than 50 institutions, and 20 robotic platforms, including the CMR Versius, Intuitive Surgical da Vinci Si/Xi, da Vinci Research Kit (dVRK), Rob Surgical BiTrack, Virtual Incision MIRA, Moon Surgical Maestro, and various custom systems. It spans surgical manipulation, robotic ultrasound, and endoscopy procedures.

The authors use this dataset to post-train two foundation models. GR00T-H is the first open vision-language-action (VLA) foundation model for medical robotics; it is reported to be the only evaluated model that achieves full end-to-end task completion on the SutureBot benchmark (25% of trials) and reaches 64% average success across a 29-step ex vivo suturing sequence. Cosmos-H-Surgical-Simulator is the first action-conditioned world model trained to enable multi-embodiment surgical simulation from a single checkpoint, supporting in silico policy evaluation and synthetic data generation across nine robotic platforms.

The work is positioned as generalizable infrastructure: by demonstrating that healthcare-specific post-training on large, diverse, cross-embodiment data improves generalization, out-of-distribution robustness, and fine-tuning data efficiency, the authors argue that analogous open data collection can serve as critical infrastructure for robot learning beyond the medical domain.

## Key Contributions

- Open-H-Embodiment: the first large-scale, cross-embodiment, multimodal dataset for surgical and healthcare robotics, with 780 hours, 119 datasets, 50+ institutions, and 20 robot platforms.
- GR00T-H: the first open foundational vision-language-action model for medical robotics, achieving full end-to-end task completion on the SutureBot benchmark (25%) and 64% average success on a 29-step ex vivo suturing sequence.
- Cosmos-H-Surgical-Simulator: the first multi-embodiment, kinematic action-conditioned world model for surgical simulation, enabling in silico policy evaluation and synthetic data generation from a single checkpoint.
- Empirical evidence that healthcare-specific post-training on large, diverse data improves cross-embodiment generalization, out-of-distribution robustness, and fine-tuning data efficiency for surgical policies.

## Relevance to Humanoid Robotics

Although the paper focuses on surgical and medical robots rather than bipedal humanoids, its methodology is directly transferable to generalist humanoid robot learning. The core contribution is a recipe for building large-scale, cross-embodiment, multimodal datasets with synchronized video, language, and kinematics, which is exactly the kind of data infrastructure required to train generalist humanoid vision-language-action models. GR00T-H's architecture and post-training pipeline demonstrate how domain-specific data can adapt a general VLA backbone to heterogeneous embodiments, a problem central to humanoid deployment across diverse environments. Likewise, the action-conditioned world model Cosmos-H-Surgical-Simulator illustrates how synthetic data generation and in-silico policy evaluation can scale when a single checkpoint covers many robot morphologies, an approach that could reduce real-world data requirements for humanoid training.
