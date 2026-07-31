---
$id: ent_paper_humannet_scaling_human_centric_video_one_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumanNet: Scaling Human-centric Video Learning to One Million Hours'
  zh: 'HumanNet: Scaling Human-centric Video Learning to One Million Hours'
  ko: 'HumanNet: Scaling Human-centric Video Learning to One Million Hours'
summary:
  en: 'Progress in embodied intelligence increasingly depends on scalable data infrastructure. While vision and language have
    scaled with internet corpora, learning physical interaction remains constrained by the lack of large, diverse, and richly
    annotated human activity data. Institutions per source list: 北京大学（DAGroup-PKU）.'
  zh: HumanNet 是一个包含一百万小时人类活动视频的大型数据集，由研究团队构建，旨在通过人类中心视频推动具身智能学习。其核心贡献在于提供了跨视角、细粒度交互标注的视频语料，并验证了第一人称人类视频可作为机器人数据的可扩展替代方案。
  ko: 'Progress in embodied intelligence increasingly depends on scalable data infrastructure. While vision and language have
    scaled with internet corpora, learning physical interaction remains constrained by the lack of large, diverse, and richly
    annotated human activity data. Institutions per source list: 北京大学（DAGroup-PKU）.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- humannet
- scaling
- human
- centric
- video
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 386 (merged duplicate list rows: [412]) (.staging/ingest_yuanxq). Tier
    A->full. Title guard: substring (score 1.0). Abstract and metadata from arXiv API (2605.06747v1); zh content by DeepSeek
    from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2605.06747 HumanNet: Scaling Human-centric Video Learning to One Million Hours'
  url: https://arxiv.org/abs/2605.06747
  accessed_at: '2026-07-31'
  date: '2026-05-07'
- id: src_002
  type: website
  title: Project page
  url: https://dagroup-pku.github.io/HumanNet/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: Project page
  url: https://github.com/DAGroup-PKU/HumanNet/
  accessed_at: '2026-07-31'
- id: src_004
  type: website
  title: Project page
  url: https://github.com/DAGroup-PKU/HumanNet
  accessed_at: '2026-07-31'
- id: src_005
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

HumanNet 数据集规模达一百万小时，涵盖第一人称和第三人称视角，记录了人类在真实环境中与物体的精细交互、工具使用及长期行为。该数据集不仅包含原始视频，还提供了交互式标注，如描述、运动描述及手部与身体信号，支持运动感知和交互感知学习。其数据策展范式将人类中心过滤、时间结构、视角多样性和标注丰富性作为核心设计原则，将非结构化互联网视频转化为可扩展的学习资源。通过控制实验，研究团队发现使用 HumanNet 中 1000 小时第一人称视频对 Qwen VLM 模型进行持续训练，其效果优于使用 100 小时真实机器人数据（来自 Magic Cobot）的训练，表明人类视频可作为机器人数据的低成本替代。

## 核心内容
### 数据集规模与视角
- HumanNet 包含 **100 万小时** 的人类活动视频，覆盖 **第一人称** 和 **第三人称** 视角。
- 数据来源为互联网视频，经过系统化策展，确保场景多样性（如家庭、办公室、户外等）。

### 标注与结构
- 提供 **交互式标注**，包括：
  - 视频描述（captions）
  - 运动描述（motion descriptions）
  - 手部与身体信号（hand and body-related signals）
- 数据按 **时间结构** 组织，支持长期行为（long-horizon behaviors）分析。

### 设计原则
- 数据策展遵循四大原则：
  - **人类中心过滤**：筛选与人类活动相关的视频。
  - **时间结构化**：保留动作序列的时序信息。
  - **视角多样性**：同时包含第一人称和第三人称视角。
  - **标注丰富化**：添加多模态标注信号。

### 实验验证
- 使用 **Qwen VLM** 模型进行视觉-语言-动作（vision-language-action）消融实验。
- 固定验证集下，**1000 小时 HumanNet 第一人称视频** 的持续训练，性能超过 **100 小时 Magic Cobot 真实机器人数据** 的训练。
- 结果表明，第一人称人类视频可作为机器人数据的 **可扩展且低成本替代**。

### 结论
- HumanNet 旨在探索利用人类中心视频扩展具身基础模型，而非仅依赖机器人专用数据。该数据集为表示学习、活动理解、运动生成及人机迁移提供了可扩展的基础。

## Overview
Progress in embodied intelligence increasingly depends on scalable data infrastructure. While vision and language have scaled with internet corpora, learning physical interaction remains constrained by the lack of large, diverse, and richly annotated human activity data. We present HumanNet, a one-million-hour human-centric video corpus that captures how humans interact with the physical world at scale. HumanNet spans both first-person and third-person perspectives and covers fine-grained activities, human-object interactions, tool use, and long-horizon behaviors across diverse real-world environments. Beyond raw video, the dataset provides interaction-centric annotations, including captions, motion descriptions, and hand and body-related signals, enabling motion-aware and interaction-aware learning. Beyond scale, HumanNet introduces a systematic data curation paradigm for embodied learning, where human-centric filtering, temporal structuring, viewpoint diversity, and annotation enrichment are treated as first-class design principles. This design transforms unstructured internet video into a scalable substrate for representation learning, activity understanding, motion generation, and human-to-robot transfer. We conduct a first-step validation on the value of this design through controlled vision-language-action ablation: under a fixed set of validation data, continued training from the Qwen VLM model with 1000 hours of egocentric video drawn from HumanNet surpasses the continued training with 100 hours of real-robot data from Magic Cobot, indicating that egocentric human video could be a scalable and cost-effective substitute for robot data. By building this project, we aim to explore the opportunity to scale embodied foundation models using human-centric videos, rather than relying solely on robot-specific data.

## 参考
- https://arxiv.org/abs/2605.06747
- https://dagroup-pku.github.io/HumanNet/
- https://github.com/DAGroup-PKU/HumanNet/
- https://github.com/DAGroup-PKU/HumanNet
- https://github.com/ImChong/Robotics_Notebooks

## 개요

HumanNet 데이터셋은 백만 시간 규모로, 일인칭 및 삼인칭 시점을 포함하며 실제 환경에서 인간이 물체와 정밀하게 상호작용하고 도구를 사용하며 장기적인 행동을 수행하는 모습을 기록합니다. 이 데이터셋은 원본 비디오뿐만 아니라 설명, 동작 설명, 손과 신체 신호와 같은 상호작용적 주석을 제공하여 운동 인식 및 상호작용 인식 학습을 지원합니다. 데이터 큐레이션 패러다임은 인간 중심 필터링, 시간 구조, 시점 다양성 및 주석 풍부성을 핵심 설계 원칙으로 삼아 비구조화된 인터넷 비디오를 확장 가능한 학습 자원으로 변환합니다. 제어 실험을 통해 연구팀은 HumanNet의 1000시간 일인칭 비디오로 Qwen VLM 모델을 지속적으로 훈련한 결과, 100시간의 실제 로봇 데이터(Magic Cobot 출처)를 사용한 훈련보다 더 나은 성능을 보였으며, 이는 인간 비디오가 로봇 데이터의 저비용 대안이 될 수 있음을 시사합니다.

## 핵심 내용
### 데이터셋 규모와 시점
- HumanNet은 **100만 시간**의 인간 활동 비디오를 포함하며, **일인칭** 및 **삼인칭** 시점을 모두 다룹니다.
- 데이터는 인터넷 비디오에서 수집되었으며, 체계적인 큐레이션을 통해 장면 다양성(예: 가정, 사무실, 야외 등)을 보장합니다.

### 주석과 구조
- **상호작용적 주석**을 제공하며, 여기에는 다음이 포함됩니다:
  - 비디오 설명(captions)
  - 동작 설명(motion descriptions)
  - 손과 신체 관련 신호(hand and body-related signals)
- 데이터는 **시간 구조**에 따라 구성되어 장기적 행동(long-horizon behaviors) 분석을 지원합니다.

### 설계 원칙
- 데이터 큐레이션은 네 가지 원칙을 따릅니다:
  - **인간 중심 필터링**: 인간 활동과 관련된 비디오를 선별합니다.
  - **시간 구조화**: 동작 시퀀스의 시간적 정보를 유지합니다.
  - **시점 다양성**: 일인칭 및 삼인칭 시점을 모두 포함합니다.
  - **주석 풍부화**: 다중 모달 주석 신호를 추가합니다.

### 실험 검증
- **Qwen VLM** 모델을 사용하여 시각-언어-동작(vision-language-action) 소거 실험을 수행했습니다.
- 고정된 검증 세트에서 **1000시간 HumanNet 일인칭 비디오**로 지속 훈련한 결과, **100시간 Magic Cobot 실제 로봇 데이터**로 훈련한 것보다 성능이 뛰어났습니다.
- 이는 일인칭 인간 비디오가 로봇 데이터의 **확장 가능하고 저비용인 대안**이 될 수 있음을 보여줍니다.

### 결론
- HumanNet은 로봇 전용 데이터에만 의존하지 않고 인간 중심 비디오를 활용하여 구현 기반 모델을 확장하는 것을 목표로 합니다. 이 데이터셋은 표현 학습, 활동 이해, 동작 생성 및 인간-로봇 전이를 위한 확장 가능한 기반을 제공합니다.
