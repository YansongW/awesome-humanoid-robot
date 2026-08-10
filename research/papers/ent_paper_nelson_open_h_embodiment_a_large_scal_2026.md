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
  zh: Open-H-Embodiment 是当前最大的开放医疗机器人多模态数据集，包含 780 小时同步视频、语言与运动学数据，覆盖 50 多家机构与 20 多种机器人平台。基于该数据集，研究团队训练了首个开放医疗机器人视觉-语言-动作基础模型
    GR00T-H 以及多体态手术世界模型 Cosmos-H-Surgical-Simulator，在缝合基准测试中实现 25% 的端到端任务完成率（其他模型为 0%），并在 29 步离体缝合序列中达到 64% 的平均成功率。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.21017v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1187 chars, DeepSeek).'
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
Open-H-Embodiment 数据集由多个研究机构联合构建，旨在解决医疗机器人领域数据规模小、体态单一且不开放的根本问题。该数据集包含来自 CMR Versius、Intuitive Surgical da Vinci、da Vinci Research Kit (dVRK)、Rob Surgical BiTrack、Virtual Incision MIRA、Moon Surgical Maestro 等 20 多种机器人平台的同步视频、语言指令与运动学数据，涵盖手术操作、机器人超声与内窥镜检查等场景。基于该数据集训练的 GR00T-H 模型是首个开放医疗机器人视觉-语言-动作基础模型，在结构化缝合基准测试中实现了 25% 的端到端任务完成率，而所有其他对比模型均为 0%；在 29 步离体缝合序列中平均成功率达 64%。同时训练的 Cosmos-H-Surgical-Simulator 是首个支持多体态手术模拟的动作条件世界模型，可从单一检查点覆盖九种机器人平台，用于策略评估与合成数据生成。

## 核心内容
### 数据集构建
- **规模与组成**：Open-H-Embodiment 包含 780 小时的多模态数据，同步记录医疗机器人操作视频、语言指令与运动学信息。
- **覆盖范围**：数据来自 50 多家机构，涵盖 20 多种机器人平台，包括 CMR Versius、Intuitive Surgical da Vinci、da Vinci Research Kit (dVRK)、Rob Surgical BiTrack、Virtual Incision MIRA、Moon Surgical Maestro 以及多种定制系统。
- **任务类型**：包括手术操作、机器人超声检查与内窥镜检查等医疗场景。

### 基础模型
- **GR00T-H**：首个开放医疗机器人视觉-语言-动作基础模型，采用端到端学习架构。
  - 在结构化缝合基准测试中，GR00T-H 在 25% 的试验中实现完整任务完成，而所有其他对比模型（包括通用机器人基础模型）均为 0%。
  - 在 29 步离体缝合序列中，平均成功率达 64%。
- **Cosmos-H-Surgical-Simulator**：首个动作条件世界模型，支持多体态手术模拟。
  - 从单一检查点覆盖九种机器人平台，可进行计算机内策略评估与合成数据生成。
  - 为医疗机器人领域提供虚拟仿真环境，降低真实数据采集成本。

### 实验设置与结论
- 实验采用结构化缝合基准与离体缝合序列作为评估任务，对比模型包括通用机器人基础模型与专用医疗机器人模型。
- 结果表明，开放大规模医疗机器人数据收集可作为研究社区的关键基础设施，推动机器人学习与世界建模等领域的进步。

## Overview
Autonomous medical robots hold promise to improve patient outcomes, reduce provider workload, democratize access to care, and enable superhuman precision. However, autonomous medical robotics has been limited by a fundamental data problem: existing medical robotic datasets are small, single-embodiment, and rarely shared openly, restricting the development of foundation models that the field needs to advance. We introduce Open-H-Embodiment, the largest open dataset of medical robotic video with synchronized kinematics to date, spanning more than 50 institutions and multiple robotic platforms including the CMR Versius, Intuitive Surgical's da Vinci, da Vinci Research Kit (dVRK), Rob Surgical BiTrack, Virtual Incision's MIRA, Moon Surgical Maestro, and a variety of custom systems, spanning surgical manipulation, robotic ultrasound, and endoscopy procedures. We demonstrate the research enabled by this dataset through two foundation models. GR00T-H is the first open foundation vision-language-action model for medical robotics, which is the only evaluated model to achieve full end-to-end task completion on a structured suturing benchmark (25% of trials vs. 0% for all others) and achieves 64% average success across a 29-step ex vivo suturing sequence. We also train Cosmos-H-Surgical-Simulator, the first action-conditioned world model to enable multi-embodiment surgical simulation from a single checkpoint, spanning nine robotic platforms and supporting in silico policy evaluation and synthetic data generation for the medical domain. These results suggest that open, large-scale medical robot data collection can serve as critical infrastructure for the research community, enabling advances in robot learning, world modeling, and beyond.

## 参考
- http://arxiv.org/abs/2604.21017v3

## 개요
Open-H-Embodiment 데이터셋은 여러 연구 기관이 공동으로 구축한 것으로, 의료 로봇 분야의 데이터 규모가 작고, 체형이 단일하며, 개방되지 않은 근본적인 문제를 해결하는 것을 목표로 합니다. 이 데이터셋은 CMR Versius, Intuitive Surgical da Vinci, da Vinci Research Kit (dVRK), Rob Surgical BiTrack, Virtual Incision MIRA, Moon Surgical Maestro 등 20개 이상의 로봇 플랫폼에서 수집된 동기화된 비디오, 언어 지시 및 운동학 데이터를 포함하며, 수술 조작, 로봇 초음파 및 내시경 검사 등의 시나리오를涵盖합니다. 이 데이터셋을 기반으로 훈련된 GR00T-H 모델은 최초의 개방형 의료 로봇 비전-언어-행동 기반 모델로, 구조화된 봉합 벤치마크에서 25%의 종단 간 작업 완료율을 달성했으며, 다른 모든 비교 모델은 0%였습니다. 29단계 체외 봉합 시퀀스에서 평균 성공률은 64%에 달했습니다. 동시에 훈련된 Cosmos-H-Surgical-Simulator는 다중 체형 수술 시뮬레이션을 지원하는 최초의 행동 조건부 세계 모델로, 단일 체크포인트에서 9가지 로봇 플랫폼을覆盖하며, 정책 평가 및 합성 데이터 생성에 사용됩니다.

## 핵심 내용
### 데이터셋 구축
- **규모 및 구성**: Open-H-Embodiment는 780시간의 다중 모달 데이터를 포함하며, 의료 로봇 조작 비디오, 언어 지시 및 운동학 정보를 동기화하여 기록합니다.
- **覆盖 범위**: 데이터는 50개 이상의 기관에서 수집되었으며, CMR Versius, Intuitive Surgical da Vinci, da Vinci Research Kit (dVRK), Rob Surgical BiTrack, Virtual Incision MIRA, Moon Surgical Maestro 및 다양한 맞춤형 시스템을 포함한 20개 이상의 로봇 플랫폼을涵盖합니다.
- **작업 유형**: 수술 조작, 로봇 초음파 검사 및 내시경 검사 등의 의료 시나리오를 포함합니다.

### 기반 모델
- **GR00T-H**: 최초의 개방형 의료 로봇 비전-언어-행동 기반 모델로, 종단 간 학습 아키텍처를 채택합니다.
  - 구조화된 봉합 벤치마크에서 GR00T-H는 25%의 시험에서 완전한 작업 완료를 달성했으며, 다른 모든 비교 모델(일반 로봇 기반 모델 포함)은 0%였습니다.
  - 29단계 체외 봉합 시퀀스에서 평균 성공률은 64%에 달했습니다.
- **Cosmos-H-Surgical-Simulator**: 다중 체형 수술 시뮬레이션을 지원하는 최초의 행동 조건부 세계 모델입니다.
  - 단일 체크포인트에서 9가지 로봇 플랫폼을覆盖하며, 컴퓨터 내 정책 평가 및 합성 데이터 생성을 가능하게 합니다.
  - 의료 로봇 분야에 가상 시뮬레이션 환경을 제공하여 실제 데이터 수집 비용을 절감합니다.

### 실험 설정 및 결론
- 실험은 구조화된 봉합 벤치마크와 체외 봉합 시퀀스를 평가 작업으로 사용했으며, 비교 모델에는 일반 로봇 기반 모델과 전용 의료 로봇 모델이 포함됩니다.
- 결과는 개방형 대규모 의료 로봇 데이터 수집이 연구 커뮤니티의 핵심 인프라로 작용하여 로봇 학습 및 세계 모델링 분야의 발전을 촉진할 수 있음을 보여줍니다.
