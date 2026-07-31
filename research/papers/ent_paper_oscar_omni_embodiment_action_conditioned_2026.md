---
$id: ent_paper_oscar_omni_embodiment_action_conditioned_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OSCAR: Omni-Embodiment Action-Conditioned World Model for Robotics'
  zh: 'OSCAR: Omni-Embodiment Action-Conditioned World Model for Robotics'
  ko: 'OSCAR: Omni-Embodiment Action-Conditioned World Model for Robotics'
summary:
  en: 'We present OSCAR, a precise action-conditioned video world model that generalizes across different robot embodiments
    and enables robot policy evaluation. Institutions per source list: Peking University、University of Michigan、NVIDIA.'
  zh: OSCAR 是一个精确的动作条件视频世界模型，由研究团队提出，旨在跨不同机器人实体泛化并支持策略评估。其核心贡献包括：构建大规模标准化数据管道以整合机器人及人类数据集，采用 2D 运动学骨架渲染作为统一条件表示，并在单张 GH200
    GPU 上微调 Cosmos-Predict2.5-2B 模型，显著提升了动作跟随、外观质量与运动一致性。
  ko: 'We present OSCAR, a precise action-conditioned video world model that generalizes across different robot embodiments
    and enables robot policy evaluation. Institutions per source list: Peking University、University of Michigan、NVIDIA.'
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
- oscar
- omni
- embodiment
- action
- conditioned
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 731 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2606.04463 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2606.04463v2); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.04463 OSCAR: Omni-Embodiment Action-Conditioned World Model for Robotics'
  url: https://arxiv.org/abs/2606.04463
  accessed_at: '2026-07-31'
  date: '2026-06-03'
- id: src_002
  type: website
  title: Project page
  url: https://wuzy2115.github.io/oscar-project-page/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

OSCAR 针对现有视频世界模型在真实机器人评估中面临的三大挑战——训练数据场景多样性不足、动作跟随不精确以及跨实体泛化能力差——提出了解决方案。研究团队首先开发了一套大规模标准化数据管道，用于整理、过滤和去重广泛的机器人及自我中心人类数据集，生成一个覆盖多样任务、场景、动作和机器人实体的干净联合训练数据集。为统一条件表示，模型采用 2D 运动学骨架渲染，使其能泛化至不同机械臂甚至人类手部。在单张 GH200 GPU 上微调 Cosmos-Predict2.5-2B 模型后，OSCAR 在动作跟随、外观质量和运动一致性上显著优于现有基线方法，这些基线要么模型规模更大，要么需要更多 GPU。最终，OSCAR 被部署用于评估 RoboArena 中的机器人策略，实验表明其虚拟策略评估与真实世界评估之间存在显著相关性。

## 核心内容
### 方法
OSCAR 的核心方法围绕两个关键方面展开：
- **大规模标准化数据管道**：该管道从广泛的机器人数据集和自我中心人类数据集中进行数据整理、过滤和去重，生成一个覆盖多样任务、场景、动作和机器人实体的干净联合训练数据集。这解决了现有训练数据场景多样性不足的问题。
- **统一条件表示**：采用 2D 运动学骨架渲染作为条件表示，该表示能泛化至不同机器人实体（如不同机械臂）甚至人类手部，从而提升跨实体泛化能力。

### 架构与训练
- 模型基于 Cosmos-Predict2.5-2B 进行微调，训练在单张 GH200 GPU 上完成。
- 相比现有基线方法（这些方法要么模型规模更大，要么需要更多 GPU），OSCAR 在动作跟随、外观质量和运动一致性上实现了显著提升。

### 实验设置与关键数字
- 模型被部署用于评估 RoboArena 中的机器人策略。
- 实验结果表明，OSCAR 的虚拟策略评估与真实世界评估之间存在显著相关性，这为未来在虚拟生成世界中纯评估机器人策略奠定了基础。

### 结论
OSCAR 通过解决数据多样性、动作跟随精度和跨实体泛化三大挑战，为机器人策略的虚拟评估提供了有效工具，其与真实世界评估的相关性验证了该方法的实用性。

## Overview
We present OSCAR, a precise action-conditioned video world model that generalizes across different robot embodiments and enables robot policy evaluation. Existing video world models face three main challenges for real-world robot evaluation: limited scenario diversity in current robot training datasets, imprecise action following, and poor generalization across embodiments for broad adoption. We tackle these challenges from two perspectives. At its core is a large-scale standardized data pipeline that curates, filters, and deduplicates broad robotics and egocentric human datasets, yielding a clean joint-training dataset that spans diverse tasks, scenarios, actions, and robot embodiments. To condition the video model, we adopt 2D kinematic skeleton rendering as a unified conditioning representation that generalizes across different robot arms or even human hands. We finetune the Cosmos-Predict2.5-2B model on a single GH200 GPU. Our model achieves significant improvement on action following, appearance quality, and motion consistency, compared to existing baselines, which either have a much larger model size or require more GPUs. We further deploy OSCAR to evaluate robot policies from RoboArena. Extensive experiments demonstrate the significant correlation between our virtual policy evaluation in OSCAR and real-world evaluation, paving the way for the future where robot policies can be purely evaluated in virtual generated worlds.

## 参考
- https://arxiv.org/abs/2606.04463
- https://wuzy2115.github.io/oscar-project-page/
- https://github.com/ImChong/Robotics_Notebooks

## 개요

OSCAR는 기존 비디오 월드 모델이 실제 로봇 평가에서 직면하는 세 가지 주요 과제——훈련 데이터의 장면 다양성 부족, 부정확한 동작 추종, 교차 엔티티 일반화 능력 저하——에 대한 해결책을 제시합니다. 연구팀은 먼저 대규모 표준화 데이터 파이프라인을 개발하여 광범위한 로봇 및 자기 중심 인간 데이터셋을 정리, 필터링 및 중복 제거하여 다양한 작업, 장면, 동작 및 로봇 엔티티를 포괄하는 깨끗한 통합 훈련 데이터셋을 생성했습니다. 조건부 표현을 통일하기 위해 모델은 2D 운동학적 스켈레톤 렌더링을 사용하여 다양한 로봇 팔, 심지어 인간 손에도 일반화할 수 있도록 했습니다. 단일 GH200 GPU에서 Cosmos-Predict2.5-2B 모델을 미세 조정한 후, OSCAR는 동작 추종, 외관 품질 및 운동 일관성에서 기존 베이스라인 방법보다 현저히 우수한 성능을 보였으며, 이러한 베이스라인 방법은 더 큰 모델이거나 더 많은 GPU를 필요로 했습니다. 최종적으로 OSCAR는 RoboArena에서 로봇 정책을 평가하는 데 배포되었으며, 실험 결과 가상 정책 평가와 실제 세계 평가 간에 유의미한 상관관계가 있음을 보여주었습니다.

## 핵심 내용
### 방법
OSCAR의 핵심 방법은 두 가지 주요 측면에 중점을 둡니다:
- **대규모 표준화 데이터 파이프라인**: 이 파이프라인은 광범위한 로봇 데이터셋과 자기 중심 인간 데이터셋에서 데이터를 정리, 필터링 및 중복 제거하여 다양한 작업, 장면, 동작 및 로봇 엔티티를 포괄하는 깨끗한 통합 훈련 데이터셋을 생성합니다. 이는 기존 훈련 데이터의 장면 다양성 부족 문제를 해결합니다.
- **통일된 조건부 표현**: 2D 운동학적 스켈레톤 렌더링을 조건부 표현으로 사용하여, 이 표현은 다양한 로봇 엔티티(예: 다른 로봇 팔) 및 심지어 인간 손에도 일반화할 수 있어 교차 엔티티 일반화 능력을 향상시킵니다.

### 아키텍처 및 훈련
- 모델은 Cosmos-Predict2.5-2B를 기반으로 미세 조정되었으며, 단일 GH200 GPU에서 훈련이 완료되었습니다.
- 기존 베이스라인 방법(더 큰 모델이거나 더 많은 GPU가 필요한 방법)과 비교하여 OSCAR는 동작 추종, 외관 품질 및 운동 일관성에서 현저한 개선을 달성했습니다.

### 실험 설정 및 주요 수치
- 모델은 RoboArena에서 로봇 정책을 평가하는 데 배포되었습니다.
- 실험 결과 OSCAR의 가상 정책 평가와 실제 세계 평가 간에 유의미한 상관관계가 있음을 보여주었으며, 이는 미래에 가상 생성 세계에서 로봇 정책을 순수하게 평가할 수 있는 기반을 마련했습니다.

### 결론
OSCAR는 데이터 다양성, 동작 추종 정확도 및 교차 엔티티 일반화라는 세 가지 과제를 해결함으로써 로봇 정책의 가상 평가를 위한 효과적인 도구를 제공하며, 실제 세계 평가와의 상관관계는 이 방법의 실용성을 입증합니다.
