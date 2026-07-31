---
$id: ent_paper_hrdexdb_paired_human_robot_dataset_cross_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HRDexDB: A Paired Human-Robot Dataset for Cross-Embodiment Dexterous Grasping'
  zh: 'HRDexDB: A Paired Human-Robot Dataset for Cross-Embodiment Dexterous Grasping'
  ko: 'HRDexDB: A Paired Human-Robot Dataset for Cross-Embodiment Dexterous Grasping'
summary:
  en: 'We present HRDexDB, a paired cross-embodiment dexterous grasping dataset of high-fidelity dexterous grasping sequences
    featuring both human and diverse robotic hands. Institutions per source list: Seoul National University、RLWRLD.'
  zh: HRDexDB 是一个跨形态灵巧抓取数据集，由研究团队构建，包含人类与多种机器人手部的高保真抓取序列。其核心贡献在于提供了 2.1K 次抓取试验，涵盖 100 种物体，并配有同步视觉、运动学及触觉力信号，作为跨形态灵巧操作的基准。
  ko: 'We present HRDexDB, a paired cross-embodiment dexterous grasping dataset of high-fidelity dexterous grasping sequences
    featuring both human and diverse robotic hands. Institutions per source list: Seoul National University、RLWRLD.'
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
- hrdexdb
- paired
- human
- robot
- dataset
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 410 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2604.14944 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2604.14944v2); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2604.14944 HRDexDB: A Paired Human-Robot Dataset for Cross-Embodiment Dexterous Grasping'
  url: https://arxiv.org/abs/2604.14944
  accessed_at: '2026-07-31'
  date: '2026-04-16'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

HRDexDB 数据集专注于跨形态灵巧抓取，提供了人类手部与多种机器人手部在相同物体上的高精度抓取轨迹。它利用先进视觉方法和多相机系统，获取了 2.1K 次试验的时空 3D 真实运动数据，覆盖 100 种不同物体。每个试验都包含同步的视觉和运动学模态，对于支持触觉的机器人手部还提供了接触力信号。该数据集通过对齐人类灵巧性与机器人执行过程，为跨形态灵巧操作研究建立了基础基准。

## 核心内容
### 方法
HRDexDB 采用多相机系统结合 state-of-the-art 视觉方法，捕捉人类和机器人手部在抓取过程中的高精度时空 3D 运动。数据集通过精心设计的实验协议，确保人类与机器人手部在相同目标物体上执行可比的抓取动作，从而实现跨形态对齐。

### 架构
数据集包含 2.1K 次抓取试验，每次试验都提供同步的视觉和运动学模态。对于配备触觉传感器的机器人手部，还额外提供了接触力信号。数据覆盖 100 种多样物体，确保泛化性。

### 实验设置
- **数据规模**：2.1K 次抓取试验。
- **物体多样性**：100 种不同物体。
- **模态**：同步视觉、运动学数据，以及触觉机器人手部的接触力信号。
- **系统**：专用多相机系统用于高保真捕捉。

### 关键数字
- 2.1K 次抓取试验。
- 100 种物体。
- 提供高精度时空 3D 真实运动数据。

### 结论
HRDexDB 作为跨形态灵巧操作的基准数据集，通过提供人类与机器人手部在相同物体上的对齐抓取数据，支持跨形态灵巧操作研究。其丰富的模态和高精度数据为未来研究奠定了基础。

## Overview
We present HRDexDB, a paired cross-embodiment dexterous grasping dataset of high-fidelity dexterous grasping sequences featuring both human and diverse robotic hands. Unlike existing datasets, HRDexDB provides a comprehensive collection of grasping trajectories across human hands and multiple robot hand embodiments, spanning 100 diverse objects. Leveraging state-of-the-art vision methods and a dedicated multi-camera system, HRDexDB offers high-precision spatiotemporal 3D ground-truth motion for both the agent and the manipulated object. The dataset comprises 2.1K grasping trials, each enriched with synchronized visual and kinematic modalities, with contact-force signals available for tactile-enabled robotic hands. By providing closely aligned captures of human dexterity and robotic execution on the same target objects under comparable grasping motions, HRDexDB serves as a foundational benchmark for cross-embodiment dexterous manipulation.

## 参考
- https://arxiv.org/abs/2604.14944
- https://github.com/ImChong/Robotics_Notebooks

## 개요

HRDexDB 데이터셋은 교차 형태의 손재주 있는 잡기를 중점적으로 다루며, 동일한 물체에 대한 인간 손과 다양한 로봇 손의 고정밀 잡기 궤적을 제공합니다. 첨단 시각 방법과 다중 카메라 시스템을 활용하여 100가지 다양한 물체를 대상으로 2.1K회 실험의 시공간 3D 실제 운동 데이터를 획득했습니다. 각 실험은 동기화된 시각 및 운동학적 모드를 포함하며, 촉각을 지원하는 로봇 손의 경우 접촉력 신호도 제공합니다. 이 데이터셋은 인간의 손재주와 로봇 실행 과정을 정렬함으로써 교차 형태 손재주 조작 연구를 위한 기본 기준을 설정합니다.

## 핵심 내용
### 방법
HRDexDB는 다중 카메라 시스템과 최첨단 시각 방법을 결합하여 인간 및 로봇 손의 잡기 과정에서 고정밀 시공간 3D 운동을 포착합니다. 데이터셋은 정교하게 설계된 실험 프로토콜을 통해 인간과 로봇 손이 동일한 목표 물체에 대해 비교 가능한 잡기 동작을 수행하도록 보장하여 교차 형태 정렬을 실현합니다.

### 구조
데이터셋은 2.1K회의 잡기 실험을 포함하며, 각 실험은 동기화된 시각 및 운동학적 모드를 제공합니다. 촉각 센서가 장착된 로봇 손의 경우 추가로 접촉력 신호도 제공됩니다. 데이터는 100가지 다양한 물체를 포괄하여 일반화 가능성을 보장합니다.

### 실험 설정
- **데이터 규모**: 2.1K회 잡기 실험.
- **물체 다양성**: 100가지 다양한 물체.
- **모드**: 동기화된 시각, 운동학 데이터, 및 촉각 로봇 손의 접촉력 신호.
- **시스템**: 고충실도 포착을 위한 전용 다중 카메라 시스템.

### 주요 수치
- 2.1K회 잡기 실험.
- 100가지 물체.
- 고정밀 시공간 3D 실제 운동 데이터 제공.

### 결론
HRDexDB는 교차 형태 손재주 조작을 위한 기준 데이터셋으로, 동일한 물체에 대한 인간과 로봇 손의 정렬된 잡기 데이터를 제공하여 교차 형태 손재주 조작 연구를 지원합니다. 풍부한 모드와 고정밀 데이터는 미래 연구를 위한 기반을 마련합니다.
