---
$id: ent_paper_video_prediction_policy_generalist_robot_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations'
  zh: 'Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations'
  ko: 'Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations'
summary:
  en: Visual representations play a crucial role in developing generalist robotic policies. Previous vision encoders, typically
    pre-trained with single-image reconstruction or two-image contrastive learning, tend to capture static information, often
    neglecting the dynamic aspects vital for embodied tasks.
  zh: Video Prediction Policy (VPP) 是一种通用机器人策略，由研究团队提出，利用视频扩散模型 (VDM) 的内部预测视觉表征来指导机器人动作学习。其核心贡献在于通过隐式逆动力学模型，将未来动态预测信息融入当前状态表征，在
    Calvin ABC-D 基准上相对提升 18.6%，并在真实世界灵巧操作任务中成功率提高 31.6%。
  ko: Visual representations play a crucial role in developing generalist robotic policies. Previous vision encoders, typically
    pre-trained with single-image reconstruction or two-image contrastive learning, tend to capture static information, often
    neglecting the dynamic aspects vital for embodied tasks.
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
- video
- prediction
- policy
- generalist
- robot
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 768 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2412.14803v2); zh content by DeepSeek from the abstract. Institutions unknown
    (not in source list).'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2412.14803 Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations'
  url: https://arxiv.org/abs/2412.14803
  accessed_at: '2026-07-31'
  date: '2024-12-19'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

VPP 的核心思想是：视频扩散模型 (VDM) 不仅能预测未来帧，其内部生成的视觉表征天然融合了当前静态信息与未来动态信息，这对机器人动作学习至关重要。传统视觉编码器（如单图像重建或双图像对比学习）往往忽略动态信息，而 VPP 则利用 VDM 的预测能力，学习一个隐式逆动力学模型，该模型以 VDM 内部的未来预测表征为条件。为了提升预测精度，研究团队在机器人数据集和互联网人类操作数据上对预训练的视频基础模型进行了微调。实验表明，VPP 在 Calvin ABC-D 泛化基准上超越了先前最先进方法，并在复杂真实世界灵巧操作任务中取得了显著性能提升。

## 核心内容
### 方法架构
VPP 的核心架构包含两个关键组件：
- **视频扩散模型 (VDM)**：作为视觉表征的生成器。VPP 利用预训练的视频基础模型（如 Stable Video Diffusion），并在机器人数据集和互联网人类操作数据上进行微调，以提升未来帧预测的准确性。
- **隐式逆动力学模型**：该模型以 VDM 内部产生的未来预测表征为条件，学习从当前状态和预测的未来状态中推断出动作。这避免了直接使用像素级预测，而是利用 VDM 的潜在空间表征。

### 实验设置
- **基准测试**：在 Calvin ABC-D 泛化基准上进行评估，该基准要求机器人完成一系列未见过的任务组合。
- **真实世界任务**：涉及复杂的灵巧操作任务，如抓取和放置不同形状的物体。
- **对比方法**：与先前最先进的视觉表征学习方法（如 R3M、MVP 等）进行比较。

### 关键数字与结果
- **Calvin ABC-D 基准**：VPP 实现了 18.6% 的相对性能提升，相比之前的最先进方法。
- **真实世界灵巧操作**：成功率提高了 31.6%，表明 VPP 在动态和复杂场景中具有更强的泛化能力。
- **消融实验**：验证了微调 VDM 和利用未来预测表征的重要性，移除这些组件会导致性能显著下降。

### 结论
VPP 通过将视频扩散模型的预测能力融入机器人策略学习，有效解决了传统视觉表征忽略动态信息的问题。该方法在多个基准和真实世界任务中展现了优越性，为通用机器人策略的发展提供了新思路。项目页面提供了更多细节和演示视频。

## Overview
Visual representations play a crucial role in developing generalist robotic policies. Previous vision encoders, typically pre-trained with single-image reconstruction or two-image contrastive learning, tend to capture static information, often neglecting the dynamic aspects vital for embodied tasks. Recently, video diffusion models (VDMs) demonstrate the ability to predict future frames and showcase a strong understanding of physical world. We hypothesize that VDMs inherently produce visual representations that encompass both current static information and predicted future dynamics, thereby providing valuable guidance for robot action learning. Based on this hypothesis, we propose the Video Prediction Policy (VPP), which learns implicit inverse dynamics model conditioned on predicted future representations inside VDMs. To predict more precise future, we fine-tune pre-trained video foundation model on robot datasets along with internet human manipulation data. In experiments, VPP achieves a 18.6\% relative improvement on the Calvin ABC-D generalization benchmark compared to the previous state-of-the-art, and demonstrates a 31.6\% increase in success rates for complex real-world dexterous manipulation tasks. Project page at https://video-prediction-policy.github.io

## 参考
- https://arxiv.org/abs/2412.14803
- https://github.com/ImChong/Robotics_Notebooks

## 개요

VPP의 핵심 아이디어는 다음과 같습니다: 비디오 확산 모델(VDM)은 미래 프레임을 예측할 수 있을 뿐만 아니라, 내부에서 생성하는 시각적 표현이 현재의 정적 정보와 미래의 동적 정보를 자연스럽게 융합한다는 점입니다. 이는 로봇의 행동 학습에 매우 중요합니다. 전통적인 시각 인코더(예: 단일 이미지 재구성 또는 이중 이미지 대비 학습)는 종종 동적 정보를 무시하는 반면, VPP는 VDM의 예측 능력을 활용하여 암시적 역운동학 모델을 학습하며, 이 모델은 VDM 내부의 미래 예측 표현을 조건으로 사용합니다. 예측 정확도를 높이기 위해 연구팀은 로봇 데이터셋과 인터넷 인간 조작 데이터에서 사전 학습된 비디오 기반 모델을 미세 조정했습니다. 실험 결과, VPP는 Calvin ABC-D 일반화 벤치마크에서 이전 최첨단 방법을 능가했으며, 복잡한 실제 세계 정밀 조작 작업에서도 상당한 성능 향상을 달성했습니다.

## 핵심 내용
### 방법 아키텍처
VPP의 핵심 아키텍처는 두 가지 주요 구성 요소를 포함합니다:
- **비디오 확산 모델 (VDM)**: 시각적 표현의 생성기 역할을 합니다. VPP는 사전 학습된 비디오 기반 모델(예: Stable Video Diffusion)을 활용하며, 로봇 데이터셋과 인터넷 인간 조작 데이터에서 미세 조정하여 미래 프레임 예측의 정확도를 향상시킵니다.
- **암시적 역운동학 모델**: 이 모델은 VDM 내부에서 생성된 미래 예측 표현을 조건으로 사용하여, 현재 상태와 예측된 미래 상태에서 행동을 추론하는 방법을 학습합니다. 이는 픽셀 수준 예측을 직접 사용하는 대신 VDM의 잠재 공간 표현을 활용합니다.

### 실험 설정
- **벤치마크 테스트**: Calvin ABC-D 일반화 벤치마크에서 평가되었으며, 이 벤치마크는 로봇이 일련의 보지 못한 작업 조합을 완료해야 합니다.
- **실제 세계 작업**: 다양한 모양의 물체를 잡고 배치하는 것과 같은 복잡한 정밀 조작 작업을 포함합니다.
- **비교 방법**: 이전 최첨단 시각 표현 학습 방법(예: R3M, MVP 등)과 비교합니다.

### 주요 수치 및 결과
- **Calvin ABC-D 벤치마크**: VPP는 이전 최첨단 방법 대비 18.6%의 상대적 성능 향상을 달성했습니다.
- **실제 세계 정밀 조작**: 성공률이 31.6% 향상되어, VPP가 동적이고 복잡한 시나리오에서 더 강력한 일반화 능력을 보여줍니다.
- **절제 실험**: VDM 미세 조정과 미래 예측 표현 활용의 중요성을 검증했으며, 이러한 구성 요소를 제거하면 성능이 크게 저하됩니다.

### 결론
VPP는 비디오 확산 모델의 예측 능력을 로봇 정책 학습에 통합함으로써, 전통적인 시각 표현이 동적 정보를 무시하는 문제를 효과적으로 해결합니다. 이 방법은 여러 벤치마크와 실제 세계 작업에서 우수성을 입증했으며, 범용 로봇 정책 개발에 새로운 방향을 제시합니다. 프로젝트 페이지에서 더 많은 세부 정보와 데모 비디오를 제공합니다.
