---
$id: ent_paper_zero_shot_whole_body_humanoid_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Zero-Shot Whole-Body Humanoid Control via Behavioral Foundation Models
  zh: Zero-Shot Whole-Body Humanoid Control via Behavioral Foundation Models
  ko: Zero-Shot Whole-Body Humanoid Control via Behavioral Foundation Models
summary:
  en: Zero-Shot Whole-Body Humanoid Control via Behavioral Foundation Models is a 2025 work on physics-based character animation
    for humanoid robots.
  zh: Zero-Shot Whole-Body Humanoid Control via Behavioral Foundation Models 是2025年关于人形机器人物理动画的工作。该研究提出Meta Motivo，首个基于行为基础模型的人形机器人控制器，通过无监督强化学习与无标签行为数据集实现零样本全身控制。核心贡献在于Forward-Backward
    Representations with Conditional-Policy Regularization算法，使模型能同时处理运动跟踪、目标到达和奖励优化等多种任务。
  ko: Zero-Shot Whole-Body Humanoid Control via Behavioral Foundation Models is a 2025 work on physics-based character animation
    for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- physics_based
- zero_shot_whole_body_humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.11054v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Zero-Shot Whole-Body Humanoid Control via Behavioral Foundation Models (arXiv)
  url: https://arxiv.org/abs/2504.11054
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该工作针对现有无监督强化学习方法的局限性，提出一种新型正则化算法，使无监督RL能够模仿无标签行为数据集中的轨迹。技术核心是训练前向-后向表征将无标签轨迹嵌入到与状态、奖励和策略相同的潜在空间，并通过潜在条件判别器鼓励策略覆盖数据集中的状态。由此训练的Meta Motivo模型仅需观察运动捕捉数据集，即可零样本解决多种全身控制任务，包括运动跟踪、目标到达和奖励优化，在表现类人行为的同时达到甚至超越任务特定方法的性能。

## 核心内容
### 方法架构
- **核心算法**：Forward-Backward Representations with Conditional-Policy Regularization
  - 训练前向-后向表征将无标签轨迹嵌入到与状态、奖励和策略共享的潜在空间
  - 使用潜在条件判别器（latent-conditional discriminator）鼓励策略覆盖无标签行为数据集中的状态
  - 通过正则化使策略与数据集中的行为对齐，同时保留零样本泛化能力

### 实验设置
- **任务类型**：运动跟踪、目标到达、奖励优化
- **数据来源**：仅使用观察数据（observation-only）的运动捕捉数据集
- **基准对比**：与任务特定方法、最先进的无监督RL方法及基于模型的基线方法对比

### 关键结果
- Meta Motivo成为首个能够通过提示解决多种全身任务的人形行为基础模型
- 模型能够表达类人行为（human-like behaviors）
- 在零样本场景下达到与任务特定方法相当的竞争性能
- 全面超越现有无监督RL和基于模型的基线方法

### 结论
该工作通过将无监督RL与行为数据集正则化结合，成功构建了可零样本泛化的人形机器人全身控制基础模型，为物理动画和机器人控制领域提供了新范式。

## Overview
Unsupervised reinforcement learning (RL) aims at pre-training agents that can solve a wide range of downstream tasks in complex environments. Despite recent advancements, existing approaches suffer from several limitations: they may require running an RL process on each downstream task to achieve a satisfactory performance, they may need access to datasets with good coverage or well-curated task-specific samples, or they may pre-train policies with unsupervised losses that are poorly correlated with the downstream tasks of interest. In this paper, we introduce a novel algorithm regularizing unsupervised RL towards imitating trajectories from unlabeled behavior datasets. The key technical novelty of our method, called Forward-Backward Representations with Conditional-Policy Regularization, is to train forward-backward representations to embed the unlabeled trajectories to the same latent space used to represent states, rewards, and policies, and use a latent-conditional discriminator to encourage policies to ``cover'' the states in the unlabeled behavior dataset. As a result, we can learn policies that are well aligned with the behaviors in the dataset, while retaining zero-shot generalization capabilities for reward-based and imitation tasks. We demonstrate the effectiveness of this new approach in a challenging humanoid control problem: leveraging observation-only motion capture datasets, we train Meta Motivo, the first humanoid behavioral foundation model that can be prompted to solve a variety of whole-body tasks, including motion tracking, goal reaching, and reward optimization. The resulting model is capable of expressing human-like behaviors and it achieves competitive performance with task-specific methods while outperforming state-of-the-art unsupervised RL and model-based baselines.

## 개요
비지도 강화 학습(Unsupervised reinforcement learning, RL)은 복잡한 환경에서 다양한 하위 작업을 해결할 수 있는 에이전트를 사전 학습하는 것을 목표로 합니다. 최근 발전에도 불구하고, 기존 접근 방식은 몇 가지 한계를 가지고 있습니다: 각 하위 작업에 대해 RL 프로세스를 실행하여 만족스러운 성능을 달성해야 하거나, 좋은 범위 또는 잘 정리된 작업별 샘플이 포함된 데이터셋에 접근해야 하거나, 관심 있는 하위 작업과 상관관계가 낮은 비지도 손실 함수로 정책을 사전 학습해야 할 수 있습니다. 본 논문에서는 레이블이 없는 행동 데이터셋의 궤적을 모방하도록 비지도 RL을 정규화하는 새로운 알고리즘을 소개합니다. 조건부 정책 정규화를 사용한 순방향-역방향 표현(Forward-Backward Representations with Conditional-Policy Regularization)이라는 우리 방법의 핵심 기술적 혁신은, 순방향-역방향 표현을 학습하여 레이블 없는 궤적을 상태, 보상 및 정책을 표현하는 데 사용되는 동일한 잠재 공간에 임베딩하고, 잠재 조건부 판별기를 사용하여 정책이 레이블 없는 행동 데이터셋의 상태를 "포괄"하도록 장려하는 것입니다. 그 결과, 데이터셋의 행동과 잘 정렬된 정책을 학습하면서도 보상 기반 및 모방 작업에 대한 제로샷 일반화 능력을 유지할 수 있습니다. 우리는 이 새로운 접근 방식의 효과를 까다로운 휴머노이드 제어 문제에서 입증합니다: 관찰 전용 모션 캡처 데이터셋을 활용하여, 동작 추적, 목표 도달 및 보상 최적화를 포함한 다양한 전신 작업을 해결하도록 프롬프트할 수 있는 최초의 휴머노이드 행동 기반 모델인 Meta Motivo를 학습합니다. 결과 모델은 인간과 유사한 행동을 표현할 수 있으며, 작업별 방법과 경쟁력 있는 성능을 달성하면서 최첨단 비지도 RL 및 모델 기반 기준선을 능가합니다.

## 핵심 내용
비지도 강화 학습(Unsupervised reinforcement learning, RL)은 복잡한 환경에서 다양한 하위 작업을 해결할 수 있는 에이전트를 사전 학습하는 것을 목표로 합니다. 최근 발전에도 불구하고, 기존 접근 방식은 몇 가지 한계를 가지고 있습니다: 각 하위 작업에 대해 RL 프로세스를 실행하여 만족스러운 성능을 달성해야 하거나, 좋은 범위 또는 잘 정리된 작업별 샘플이 포함된 데이터셋에 접근해야 하거나, 관심 있는 하위 작업과 상관관계가 낮은 비지도 손실 함수로 정책을 사전 학습해야 할 수 있습니다. 본 논문에서는 레이블이 없는 행동 데이터셋의 궤적을 모방하도록 비지도 RL을 정규화하는 새로운 알고리즘을 소개합니다. 조건부 정책 정규화를 사용한 순방향-역방향 표현(Forward-Backward Representations with Conditional-Policy Regularization)이라는 우리 방법의 핵심 기술적 혁신은, 순방향-역방향 표현을 학습하여 레이블 없는 궤적을 상태, 보상 및 정책을 표현하는 데 사용되는 동일한 잠재 공간에 임베딩하고, 잠재 조건부 판별기를 사용하여 정책이 레이블 없는 행동 데이터셋의 상태를 "포괄"하도록 장려하는 것입니다. 그 결과, 데이터셋의 행동과 잘 정렬된 정책을 학습하면서도 보상 기반 및 모방 작업에 대한 제로샷 일반화 능력을 유지할 수 있습니다. 우리는 이 새로운 접근 방식의 효과를 까다로운 휴머노이드 제어 문제에서 입증합니다: 관찰 전용 모션 캡처 데이터셋을 활용하여, 동작 추적, 목표 도달 및 보상 최적화를 포함한 다양한 전신 작업을 해결하도록 프롬프트할 수 있는 최초의 휴머노이드 행동 기반 모델인 Meta Motivo를 학습합니다. 결과 모델은 인간과 유사한 행동을 표현할 수 있으며, 작업별 방법과 경쟁력 있는 성능을 달성하면서 최첨단 비지도 RL 및 모델 기반 기준선을 능가합니다.

## 参考
- http://arxiv.org/abs/2504.11054v1
