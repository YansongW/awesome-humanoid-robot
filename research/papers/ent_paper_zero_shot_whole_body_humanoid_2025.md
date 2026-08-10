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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.11054v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (794 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2504.11054v1

## 개요
본 연구는 기존 비지도 강화학습 방법의 한계를 극복하기 위해, 비지도 RL이 레이블 없는 행동 데이터셋의 궤적을 모방할 수 있도록 하는 새로운 정규화 알고리즘을 제안한다. 기술적 핵심은 순방향-역방향 표현(Forward-Backward Representations)을 훈련하여 레이블 없는 궤적을 상태, 보상, 정책과 동일한 잠재 공간에 임베딩하고, 잠재 조건 판별기(latent-conditional discriminator)를 통해 정책이 데이터셋의 상태를 포괄하도록 유도하는 것이다. 이렇게 훈련된 Meta Motivo 모델은 모션 캡처 데이터셋만 관찰하면 운동 추적, 목표 도달, 보상 최적화를 포함한 다양한 전신 제어 작업을 제로샷으로 해결할 수 있으며, 인간과 유사한 행동을 표현하면서도 작업별 방법의 성능에 도달하거나 이를 능가한다.

## 핵심 내용
### 방법 구조
- **핵심 알고리즘**: 조건부 정책 정규화를 통한 순방향-역방향 표현(Forward-Backward Representations with Conditional-Policy Regularization)
  - 순방향-역방향 표현을 훈련하여 레이블 없는 궤적을 상태, 보상, 정책과 공유되는 잠재 공간에 임베딩
  - 잠재 조건 판별기(latent-conditional discriminator)를 사용하여 정책이 레이블 없는 행동 데이터셋의 상태를 포괄하도록 유도
  - 정규화를 통해 정책을 데이터셋의 행동과 정렬하면서도 제로샷 일반화 능력을 유지

### 실험 설정
- **작업 유형**: 운동 추적, 목표 도달, 보상 최적화
- **데이터 출처**: 관찰 데이터만 사용하는(observation-only) 모션 캡처 데이터셋
- **기준 비교**: 작업별 방법, 최첨단 비지도 RL 방법, 모델 기반 기준선 방법과 비교

### 주요 결과
- Meta Motivo는 프롬프트를 통해 다양한 전신 작업을 해결할 수 있는 최초의 휴머노이드 행동 기반 모델이 됨
- 모델은 인간과 유사한 행동(human-like behaviors)을 표현할 수 있음
- 제로샷 시나리오에서 작업별 방법과 견줄 만한 경쟁력 있는 성능을 달성
- 기존 비지도 RL 및 모델 기반 기준선 방법을 전반적으로 능가

### 결론
본 연구는 비지도 RL과 행동 데이터셋 정규화를 결합하여 제로샷 일반화가 가능한 휴머노이드 로봇 전신 제어 기반 모델을 성공적으로 구축했으며, 물리 애니메이션 및 로봇 제어 분야에 새로운 패러다임을 제시한다.
