---
$id: ent_paper_benchmarking_potential_based_r_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Benchmarking Potential Based Rewards for Learning Humanoid Locomotion
  zh: Benchmarking Potential Based Rewards for Learning Humanoid Locomotion
  ko: Benchmarking Potential Based Rewards for Learning Humanoid Locomotion
summary:
  en: Benchmarking Potential Based Rewards for Learning Humanoid Locomotion is a 2023 work on locomotion for humanoid robots.
  zh: 本文是2023年关于人形机器人运动控制的研究，由作者团队完成。核心贡献是系统对比了基于势能的奖励塑形（PBRS）与标准奖励塑形在高维人形机器人强化学习中的效果，发现PBRS在收敛速度上仅有边际提升，但在参数鲁棒性和调参简易性上显著优于传统方法。
  ko: Benchmarking Potential Based Rewards for Learning Humanoid Locomotion is a 2023 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmarking_potential_based_r
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2307.10142v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Benchmarking Potential Based Rewards for Learning Humanoid Locomotion (arXiv)
  url: https://arxiv.org/abs/2307.10142
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
强化学习管线的主要挑战常在于奖励函数的设计与调参。虽然基于势能的奖励塑形（PBRS）理论上能在不影响最优策略的前提下加速学习，但先前研究多局限于网格世界和低维系统。本文首次将PBRS系统应用于高维人形机器人运动控制任务，通过基准测试发现：PBRS对收敛速度的提升有限，但其奖励项对缩放系数的鲁棒性远强于标准奖励塑形，因此更易于调参。

## 核心内容
### 研究背景与问题
- 强化学习管线中，奖励函数的设计与调参是主要瓶颈。
- 设计良好的塑形奖励可显著加速学习，但设计不当的奖励会与期望行为冲突，导致过拟合或不稳定表现。
- 理论上，基于势能的奖励塑形（PBRS）能在不改变最优策略的前提下引导学习过程，但先前研究多限于低维系统（如网格世界），机器人领域仍主要依赖标准奖励塑形。

### 方法与实验设置
- 本文在**高维人形机器人**运动控制任务上，系统对比了标准奖励塑形与PBRS。
- 实验采用强化学习框架，训练人形机器人完成行走任务。
- 评估指标包括：收敛速度、最终策略性能、以及奖励项对缩放系数的鲁棒性。

### 关键发现与数字
- **收敛速度**：PBRS相比标准奖励塑形仅有**边际提升**，未显著加速学习收敛。
- **鲁棒性**：PBRS奖励项对缩放系数的鲁棒性**显著优于**标准奖励塑形，即在不同缩放因子下，PBRS仍能保持稳定学习，而标准方法易出现性能波动。
- **调参简易性**：由于PBRS对缩放不敏感，调参过程更简单，减少了人工试错成本。

### 结论
- 在高维人形机器人任务中，PBRS的主要优势不在于加速收敛，而在于提升奖励函数的鲁棒性与调参效率。
- 建议在实际机器人强化学习应用中，优先考虑PBRS以降低奖励工程难度。

## Overview
The main challenge in developing effective reinforcement learning (RL) pipelines is often the design and tuning the reward functions. Well-designed shaping reward can lead to significantly faster learning. Naively formulated rewards, however, can conflict with the desired behavior and result in overfitting or even erratic performance if not properly tuned. In theory, the broad class of potential based reward shaping (PBRS) can help guide the learning process without affecting the optimal policy. Although several studies have explored the use of potential based reward shaping to accelerate learning convergence, most have been limited to grid-worlds and low-dimensional systems, and RL in robotics has predominantly relied on standard forms of reward shaping. In this paper, we benchmark standard forms of shaping with PBRS for a humanoid robot. We find that in this high-dimensional system, PBRS has only marginal benefits in convergence speed. However, the PBRS reward terms are significantly more robust to scaling than typical reward shaping approaches, and thus easier to tune.

## Overview
The main challenge in developing effective reinforcement learning (RL) pipelines is often the design and tuning of reward functions. Well-designed shaping rewards can lead to significantly faster learning. Naively formulated rewards, however, can conflict with the desired behavior and result in overfitting or even erratic performance if not properly tuned. In theory, the broad class of potential-based reward shaping (PBRS) can help guide the learning process without affecting the optimal policy. Although several studies have explored the use of potential-based reward shaping to accelerate learning convergence, most have been limited to grid-worlds and low-dimensional systems, and RL in robotics has predominantly relied on standard forms of reward shaping. In this paper, we benchmark standard forms of shaping with PBRS for a humanoid robot. We find that in this high-dimensional system, PBRS has only marginal benefits in convergence speed. However, the PBRS reward terms are significantly more robust to scaling than typical reward shaping approaches, and thus easier to tune.

## Content
The main challenge in developing effective reinforcement learning (RL) pipelines is often the design and tuning of reward functions. Well-designed shaping rewards can lead to significantly faster learning. Naively formulated rewards, however, can conflict with the desired behavior and result in overfitting or even erratic performance if not properly tuned. In theory, the broad class of potential-based reward shaping (PBRS) can help guide the learning process without affecting the optimal policy. Although several studies have explored the use of potential-based reward shaping to accelerate learning convergence, most have been limited to grid-worlds and low-dimensional systems, and RL in robotics has predominantly relied on standard forms of reward shaping. In this paper, we benchmark standard forms of shaping with PBRS for a humanoid robot. We find that in this high-dimensional system, PBRS has only marginal benefits in convergence speed. However, the PBRS reward terms are significantly more robust to scaling than typical reward shaping approaches, and thus easier to tune.

## 개요
효과적인 강화 학습(RL) 파이프라인을 개발하는 데 있어 주요 과제는 종종 보상 함수의 설계와 조정입니다. 잘 설계된 형상 보상은 학습 속도를 크게 향상시킬 수 있습니다. 그러나 순진하게 구성된 보상은 원하는 행동과 충돌하여 과적합을 초래하거나, 적절히 조정되지 않으면 불규칙한 성능을 보일 수 있습니다. 이론적으로, 잠재 기반 보상 형성(PBRS)의 광범위한 클래스는 최적 정책에 영향을 주지 않고 학습 과정을 안내하는 데 도움을 줄 수 있습니다. 여러 연구에서 학습 수렴을 가속화하기 위해 잠재 기반 보상 형성을 사용하는 방법을 탐구했지만, 대부분은 그리드 월드와 저차원 시스템에 국한되었으며, 로봇 공학에서의 RL은 주로 표준 형태의 보상 형성에 의존해 왔습니다. 본 논문에서는 인간형 로봇을 대상으로 PBRS와 함께 표준 형태의 형성 방법을 벤치마킹합니다. 이 고차원 시스템에서 PBRS는 수렴 속도에 미미한 이점만을 제공한다는 것을 발견했습니다. 그러나 PBRS 보상 항은 일반적인 보상 형성 접근법보다 스케일링에 훨씬 더 강건하여 조정이 더 쉽습니다.

## 핵심 내용
효과적인 강화 학습(RL) 파이프라인을 개발하는 데 있어 주요 과제는 종종 보상 함수의 설계와 조정입니다. 잘 설계된 형상 보상은 학습 속도를 크게 향상시킬 수 있습니다. 그러나 순진하게 구성된 보상은 원하는 행동과 충돌하여 과적합을 초래하거나, 적절히 조정되지 않으면 불규칙한 성능을 보일 수 있습니다. 이론적으로, 잠재 기반 보상 형성(PBRS)의 광범위한 클래스는 최적 정책에 영향을 주지 않고 학습 과정을 안내하는 데 도움을 줄 수 있습니다. 여러 연구에서 학습 수렴을 가속화하기 위해 잠재 기반 보상 형성을 사용하는 방법을 탐구했지만, 대부분은 그리드 월드와 저차원 시스템에 국한되었으며, 로봇 공학에서의 RL은 주로 표준 형태의 보상 형성에 의존해 왔습니다. 본 논문에서는 인간형 로봇을 대상으로 PBRS와 함께 표준 형태의 형성 방법을 벤치마킹합니다. 이 고차원 시스템에서 PBRS는 수렴 속도에 미미한 이점만을 제공한다는 것을 발견했습니다. 그러나 PBRS 보상 항은 일반적인 보상 형성 접근법보다 스케일링에 훨씬 더 강건하여 조정이 더 쉽습니다.

## 参考
- http://arxiv.org/abs/2307.10142v1
