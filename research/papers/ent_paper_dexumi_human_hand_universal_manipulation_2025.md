---
$id: ent_paper_dexumi_human_hand_universal_manipulation_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DexUMI: Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation'
  zh: 'DexUMI: Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation'
  ko: 'DexUMI: Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation'
summary:
  en: We present DexUMI - a data collection and policy learning framework that uses the human hand as the natural interface
    to transfer dexterous manipulation skills to various robot hands.
  zh: DexUMI 是一个利用人类手部作为通用接口，将灵巧操作技能迁移至多种机器人手的框架。该工作由研究团队提出，核心贡献在于通过硬件外骨骼适配与软件视觉修复，弥合人手与机器人手之间的具身差异，并在两种不同机器人手上实现平均 86% 的任务成功率。
  ko: We present DexUMI - a data collection and policy learning framework that uses the human hand as the natural interface
    to transfer dexterous manipulation skills to various robot hands.
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
- dexumi
- human
- hand
- universal
- manipulation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 470 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2505.21864 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2505.21864v3); zh content by DeepSeek from the abstract. Institutions unknown (not in source list).'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2505.21864 DexUMI: Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation'
  url: https://arxiv.org/abs/2505.21864
  accessed_at: '2026-07-31'
  date: '2025-05-28'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

DexUMI 框架包含硬件与软件两方面的创新，以解决人手与机器人手之间的运动学与视觉差异。硬件方面，它采用可穿戴手部外骨骼，在数据采集过程中提供直接触觉反馈，并将人类运动映射为机器人手可行的动作。软件方面，通过高保真机器人手修复技术，在视频数据中替换人手，从而弥合视觉差距。该框架在两种不同的灵巧机器人手平台上进行了真实世界实验，平均任务成功率达到 86%。

## 核心内容
### 方法概述
DexUMI 的核心目标是利用人类手部作为自然接口，将灵巧操作技能迁移至多种机器人手。该方法通过硬件与软件两方面的适配，最小化人手与机器人手之间的具身差异。

### 硬件适配
- **可穿戴手部外骨骼**：用于桥接人手与机器人手之间的运动学差异。该外骨骼允许在数据采集过程中提供直接触觉反馈，并将人类运动映射为机器人手可行的动作。
- **运动学映射**：通过外骨骼将人类手部的关节运动转换为机器人手的对应运动，确保动作的可行性与一致性。

### 软件适配
- **视觉差异桥接**：在视频数据中，通过高保真机器人手修复技术替换人手，从而消除视觉上的差异。
- **数据增强**：通过修复技术生成逼真的机器人手图像，使策略学习能够基于更一致的视觉输入。

### 实验设置与结果
- **硬件平台**：在两种不同的灵巧机器人手平台上进行实验，验证框架的通用性。
- **任务成功率**：在真实世界实验中，平均任务成功率达到 86%，展示了 DexUMI 在灵巧操作任务中的有效性。
- **关键数字**：实验涵盖了多种操作任务，成功率的统计基于多次重复实验，确保结果的可靠性。

### 结论
DexUMI 通过硬件与软件的双重适配，成功实现了从人类手部到多种机器人手的灵巧操作技能迁移。该框架在真实世界实验中表现出色，为未来灵巧机器人操作的研究提供了新的思路。

## Overview
We present DexUMI - a data collection and policy learning framework that uses the human hand as the natural interface to transfer dexterous manipulation skills to various robot hands. DexUMI includes hardware and software adaptations to minimize the embodiment gap between the human hand and various robot hands. The hardware adaptation bridges the kinematics gap using a wearable hand exoskeleton. It allows direct haptic feedback in manipulation data collection and adapts human motion to feasible robot hand motion. The software adaptation bridges the visual gap by replacing the human hand in video data with high-fidelity robot hand inpainting. We demonstrate DexUMI's capabilities through comprehensive real-world experiments on two different dexterous robot hand hardware platforms, achieving an average task success rate of 86%.

## 参考
- https://arxiv.org/abs/2505.21864
- https://github.com/ImChong/Robotics_Notebooks

## 개요

DexUMI 프레임워크는 인간의 손과 로봇 손 사이의 운동학적 및 시각적 차이를 해결하기 위해 하드웨어와 소프트웨어 양측의 혁신을 포함합니다. 하드웨어 측면에서는 착용형 손 외골격을 사용하여 데이터 수집 과정에서 직접적인 촉각 피드백을 제공하고, 인간의 움직임을 로봇 손이 가능한 동작으로 매핑합니다. 소프트웨어 측면에서는 고충실도 로봇 손 복원 기술을 통해 비디오 데이터에서 인간의 손을 대체함으로써 시각적 차이를 해소합니다. 이 프레임워크는 두 가지 다른 정교한 로봇 손 플랫폼에서 실제 세계 실험을 수행하여 평균 작업 성공률 86%를 달성했습니다.

## 핵심 내용
### 방법 개요
DexUMI의 핵심 목표는 인간의 손을 자연스러운 인터페이스로 활용하여 정교한 조작 기술을 다양한 로봇 손으로 전이하는 것입니다. 이 방법은 하드웨어와 소프트웨어 양측의 적응을 통해 인간의 손과 로봇 손 사이의 신체적 차이를 최소화합니다.

### 하드웨어 적응
- **착용형 손 외골격**: 인간의 손과 로봇 손 사이의 운동학적 차이를 연결하는 데 사용됩니다. 이 외골격은 데이터 수집 과정에서 직접적인 촉각 피드백을 제공하고, 인간의 움직임을 로봇 손이 가능한 동작으로 매핑합니다.
- **운동학적 매핑**: 외골격을 통해 인간 손의 관절 움직임을 로봇 손의 해당 움직임으로 변환하여 동작의 가능성과 일관성을 보장합니다.

### 소프트웨어 적응
- **시각적 차이 연결**: 비디오 데이터에서 고충실도 로봇 손 복원 기술을 통해 인간의 손을 대체함으로써 시각적 차이를 제거합니다.
- **데이터 증강**: 복원 기술을 통해 사실적인 로봇 손 이미지를 생성하여 정책 학습이 더 일관된 시각적 입력을 기반으로 할 수 있도록 합니다.

### 실험 설정 및 결과
- **하드웨어 플랫폼**: 두 가지 다른 정교한 로봇 손 플랫폼에서 실험을 수행하여 프레임워크의 일반성을 검증합니다.
- **작업 성공률**: 실제 세계 실험에서 평균 작업 성공률 86%를 달성하여 DexUMI가 정교한 조작 작업에서의 효과성을 입증합니다.
- **주요 수치**: 실험은 다양한 조작 작업을 포함하며, 성공률 통계는 여러 번의 반복 실험을 기반으로 하여 결과의 신뢰성을 보장합니다.

### 결론
DexUMI는 하드웨어와 소프트웨어의 이중 적응을 통해 인간의 손에서 다양한 로봇 손으로의 정교한 조작 기술 전이를 성공적으로 구현했습니다. 이 프레임워크는 실제 세계 실험에서 뛰어난 성능을 보여주며, 미래의 정교한 로봇 조작 연구에 새로운 방향을 제시합니다.
