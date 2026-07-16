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

## Overview
Autonomous medical robots hold promise to improve patient outcomes, reduce provider workload, democratize access to care, and enable superhuman precision. However, autonomous medical robotics has been limited by a fundamental data problem: existing medical robotic datasets are small, single-embodiment, and rarely shared openly, restricting the development of foundation models that the field needs to advance. We introduce Open-H-Embodiment, the largest open dataset of medical robotic video with synchronized kinematics to date, spanning more than 50 institutions and multiple robotic platforms including the CMR Versius, Intuitive Surgical's da Vinci, da Vinci Research Kit (dVRK), Rob Surgical BiTrack, Virtual Incision's MIRA, Moon Surgical Maestro, and a variety of custom systems, spanning surgical manipulation, robotic ultrasound, and endoscopy procedures. We demonstrate the research enabled by this dataset through two foundation models. GR00T-H is the first open foundation vision-language-action model for medical robotics, which is the only evaluated model to achieve full end-to-end task completion on a structured suturing benchmark (25% of trials vs. 0% for all others) and achieves 64% average success across a 29-step ex vivo suturing sequence. We also train Cosmos-H-Surgical-Simulator, the first action-conditioned world model to enable multi-embodiment surgical simulation from a single checkpoint, spanning nine robotic platforms and supporting in silico policy evaluation and synthetic data generation for the medical domain. These results suggest that open, large-scale medical robot data collection can serve as critical infrastructure for the research community, enabling advances in robot learning, world modeling, and beyond.

## Content
Autonomous medical robots hold promise to improve patient outcomes, reduce provider workload, democratize access to care, and enable superhuman precision. However, autonomous medical robotics has been limited by a fundamental data problem: existing medical robotic datasets are small, single-embodiment, and rarely shared openly, restricting the development of foundation models that the field needs to advance. We introduce Open-H-Embodiment, the largest open dataset of medical robotic video with synchronized kinematics to date, spanning more than 50 institutions and multiple robotic platforms including the CMR Versius, Intuitive Surgical's da Vinci, da Vinci Research Kit (dVRK), Rob Surgical BiTrack, Virtual Incision's MIRA, Moon Surgical Maestro, and a variety of custom systems, spanning surgical manipulation, robotic ultrasound, and endoscopy procedures. We demonstrate the research enabled by this dataset through two foundation models. GR00T-H is the first open foundation vision-language-action model for medical robotics, which is the only evaluated model to achieve full end-to-end task completion on a structured suturing benchmark (25% of trials vs. 0% for all others) and achieves 64% average success across a 29-step ex vivo suturing sequence. We also train Cosmos-H-Surgical-Simulator, the first action-conditioned world model to enable multi-embodiment surgical simulation from a single checkpoint, spanning nine robotic platforms and supporting in silico policy evaluation and synthetic data generation for the medical domain. These results suggest that open, large-scale medical robot data collection can serve as critical infrastructure for the research community, enabling advances in robot learning, world modeling, and beyond.

## 개요
자율 의료 로봇은 환자 결과 개선, 의료진 업무 부담 감소, 의료 접근성 민주화, 초인적 정밀도 구현에 기여할 가능성을 지니고 있습니다. 그러나 자율 의료 로봇 공학은 근본적인 데이터 문제로 인해 제한을 받아 왔습니다. 기존 의료 로봇 데이터셋은 규모가 작고, 단일 체현(single-embodiment)에 국한되며, 공개적으로 공유되는 경우가 드물어 해당 분야 발전에 필요한 기초 모델 개발을 제약하고 있습니다. 본 연구에서는 Open-H-Embodiment를 소개합니다. 이는 현재까지 가장 큰 규모의 공개 의료 로봇 영상 데이터셋으로, 동기화된 운동학 데이터를 포함하며, 50개 이상의 기관과 CMR Versius, Intuitive Surgical의 da Vinci, da Vinci Research Kit(dVRK), Rob Surgical BiTrack, Virtual Incision의 MIRA, Moon Surgical Maestro 등 다양한 로봇 플랫폼 및 맞춤형 시스템을 아우릅니다. 수술 조작, 로봇 초음파, 내시경 시술을 포괄합니다. 본 데이터셋을 통해 가능해진 연구를 두 가지 기초 모델로 입증합니다. GR00T-H는 의료 로봇 공학을 위한 최초의 공개 기초 비전-언어-행동 모델로, 구조화된 봉합 벤치마크에서 완전한 종단 간 작업 완료를 달성한 유일한 평가 모델입니다(시도 중 25% 성공, 다른 모델은 0%). 또한 29단계의 생체 외 봉합 시퀀스에서 평균 64%의 성공률을 기록했습니다. 또한 Cosmos-H-Surgical-Simulator를 학습시켰습니다. 이는 단일 체크포인트로 다중 체현 수술 시뮬레이션을 가능하게 하는 최초의 행동 조건부 세계 모델로, 9개의 로봇 플랫폼을 아우르며 의료 분야의 인실리코 정책 평가 및 합성 데이터 생성을 지원합니다. 이러한 결과는 공개적이고 대규모인 의료 로봇 데이터 수집이 연구 커뮤니티의 핵심 인프라 역할을 하여 로봇 학습, 세계 모델링 및 그 이상의 발전을 가능하게 함을 시사합니다.

## 핵심 내용
자율 의료 로봇은 환자 결과 개선, 의료진 업무 부담 감소, 의료 접근성 민주화, 초인적 정밀도 구현에 기여할 가능성을 지니고 있습니다. 그러나 자율 의료 로봇 공학은 근본적인 데이터 문제로 인해 제한을 받아 왔습니다. 기존 의료 로봇 데이터셋은 규모가 작고, 단일 체현에 국한되며, 공개적으로 공유되는 경우가 드물어 해당 분야 발전에 필요한 기초 모델 개발을 제약하고 있습니다. 본 연구에서는 Open-H-Embodiment를 소개합니다. 이는 현재까지 가장 큰 규모의 공개 의료 로봇 영상 데이터셋으로, 동기화된 운동학 데이터를 포함하며, 50개 이상의 기관과 CMR Versius, Intuitive Surgical의 da Vinci, da Vinci Research Kit(dVRK), Rob Surgical BiTrack, Virtual Incision의 MIRA, Moon Surgical Maestro 등 다양한 로봇 플랫폼 및 맞춤형 시스템을 아우릅니다. 수술 조작, 로봇 초음파, 내시경 시술을 포괄합니다. 본 데이터셋을 통해 가능해진 연구를 두 가지 기초 모델로 입증합니다. GR00T-H는 의료 로봇 공학을 위한 최초의 공개 기초 비전-언어-행동 모델로, 구조화된 봉합 벤치마크에서 완전한 종단 간 작업 완료를 달성한 유일한 평가 모델입니다(시도 중 25% 성공, 다른 모델은 0%). 또한 29단계의 생체 외 봉합 시퀀스에서 평균 64%의 성공률을 기록했습니다. 또한 Cosmos-H-Surgical-Simulator를 학습시켰습니다. 이는 단일 체크포인트로 다중 체현 수술 시뮬레이션을 가능하게 하는 최초의 행동 조건부 세계 모델로, 9개의 로봇 플랫폼을 아우르며 의료 분야의 인실리코 정책 평가 및 합성 데이터 생성을 지원합니다. 이러한 결과는 공개적이고 대규모인 의료 로봇 데이터 수집이 연구 커뮤니티의 핵심 인프라 역할을 하여 로봇 학습, 세계 모델링 및 그 이상의 발전을 가능하게 함을 시사합니다.
