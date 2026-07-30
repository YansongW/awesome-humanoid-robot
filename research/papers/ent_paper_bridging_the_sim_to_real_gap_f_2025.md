---
$id: ent_paper_bridging_the_sim_to_real_gap_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation
  zh: Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation
  ko: Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation
summary:
  en: Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation is a 2025 work on sim-to-real for humanoid robots.
  zh: 本文提出一种面向人形机器人运动操控的两阶段训练方法，通过Unsupervised Actuator Net (UAN) 弥合仿真与现实的差距，并采用预训练-微调策略引导探索。该方法使机器人能够学习举重、投掷和拖拽等动态行为，且从仿真到现实迁移时保持高保真度。
  ko: Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation is a 2025 work on sim-to-real for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- bridging_the_sim_to_real_gap_f
- humanoid
- sim_to_real
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.10894v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation (arXiv)
  url: https://arxiv.org/abs/2502.10894
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
传统基于跟踪奖励的训练方法仅引导机器人沿参考轨迹运动，难以实现真正的动态目标导向行为。本文提出两阶段训练流程：首先引入Unsupervised Actuator Net (UAN)，利用真实数据在不依赖扭矩传感的情况下解决复杂驱动机制的仿真到现实迁移问题；其次采用预训练-微调策略，以参考轨迹作为初始提示引导探索。该方法有效缓解了任务奖励易被利用（奖励破解）和探索方向不足的问题，使机器人能够学习举重、投掷和拖拽等运动操控技能，并在仿真到现实迁移中保持高保真度。

## 核心内容
### 核心挑战
- 传统跟踪奖励仅引导机器人沿参考轨迹运动，无法驱动真正动态、目标导向的行为
- 任务奖励（如“尽可能远地投掷球”、“尽可能快地举起重物”）虽能激发敏捷性和力量，但存在两大问题：
  - 奖励破解：任务奖励容易被利用，导致非预期行为
  - 探索方向不足：缺乏有效引导，探索过程可能陷入低效

### 方法架构
#### 第一阶段：Unsupervised Actuator Net (UAN)
- 利用真实世界数据，在不依赖扭矩传感的情况下弥合复杂驱动机制的仿真到现实差距
- 通过确保学习行为鲁棒且可迁移，有效缓解奖励破解问题

#### 第二阶段：预训练-微调策略
- 使用参考轨迹作为初始提示，引导探索过程
- 在预训练阶段建立基础行为，再通过微调优化任务奖励

### 实验设置与结果
- 机器人运动员在仿真环境中学习举重、投掷和拖拽等运动操控技能
- 从仿真到现实迁移时，行为保持高保真度，验证了UAN和预训练-微调策略的有效性
- 该方法使机器人能够展现出与真实运动员相当的敏捷性和力量表现

## Overview
Achieving athletic loco-manipulation on robots requires moving beyond traditional tracking rewards - which simply guide the robot along a reference trajectory - to task rewards that drive truly dynamic, goal-oriented behaviors. Commands such as "throw the ball as far as you can" or "lift the weight as quickly as possible" compel the robot to exhibit the agility and power inherent in athletic performance. However, training solely with task rewards introduces two major challenges: these rewards are prone to exploitation (reward hacking), and the exploration process can lack sufficient direction. To address these issues, we propose a two-stage training pipeline. First, we introduce the Unsupervised Actuator Net (UAN), which leverages real-world data to bridge the sim-to-real gap for complex actuation mechanisms without requiring access to torque sensing. UAN mitigates reward hacking by ensuring that the learned behaviors remain robust and transferable. Second, we use a pre-training and fine-tuning strategy that leverages reference trajectories as initial hints to guide exploration. With these innovations, our robot athlete learns to lift, throw, and drag with remarkable fidelity from simulation to reality.

## 개요
로봇에서 운동적 위치-조작(loco-manipulation)을 구현하려면 단순히 기준 궤적을 따라 로봇을 안내하는 전통적인 추적 보상(tracking rewards)을 넘어, 진정으로 역동적이고 목표 지향적인 행동을 유도하는 작업 보상(task rewards)으로 전환해야 합니다. "공을 최대한 멀리 던져라" 또는 "무게를 가능한 한 빨리 들어 올려라"와 같은 명령은 로봇이 운동 성능에 내재된 민첩성과 힘을 발휘하도록 강제합니다. 그러나 작업 보상만으로 훈련하면 두 가지 주요 문제가 발생합니다: 이러한 보상은 악용(보상 해킹)되기 쉬우며, 탐색 과정이 충분한 방향성을 갖지 못할 수 있습니다. 이러한 문제를 해결하기 위해 우리는 2단계 훈련 파이프라인을 제안합니다. 첫째, Unsupervised Actuator Net(UAN)을 도입하여 토크 감지에 접근할 필요 없이 실제 데이터를 활용해 복잡한 구동 메커니즘에 대한 시뮬레이션-현실 격차(sim-to-real gap)를 해소합니다. UAN은 학습된 행동이 견고하고 전이 가능하도록 보장하여 보상 해킹을 완화합니다. 둘째, 기준 궤적을 초기 힌트로 활용하여 탐색을 안내하는 사전 훈련 및 미세 조정 전략을 사용합니다. 이러한 혁신을 통해 우리의 로봇 운동선수는 시뮬레이션에서 현실로 놀라운 충실도로 들어 올리기, 던지기, 끌기를 학습합니다.

## 핵심 내용
로봇에서 운동적 위치-조작(loco-manipulation)을 구현하려면 단순히 기준 궤적을 따라 로봇을 안내하는 전통적인 추적 보상(tracking rewards)을 넘어, 진정으로 역동적이고 목표 지향적인 행동을 유도하는 작업 보상(task rewards)으로 전환해야 합니다. "공을 최대한 멀리 던져라" 또는 "무게를 가능한 한 빨리 들어 올려라"와 같은 명령은 로봇이 운동 성능에 내재된 민첩성과 힘을 발휘하도록 강제합니다. 그러나 작업 보상만으로 훈련하면 두 가지 주요 문제가 발생합니다: 이러한 보상은 악용(보상 해킹)되기 쉬우며, 탐색 과정이 충분한 방향성을 갖지 못할 수 있습니다. 이러한 문제를 해결하기 위해 우리는 2단계 훈련 파이프라인을 제안합니다. 첫째, Unsupervised Actuator Net(UAN)을 도입하여 토크 감지에 접근할 필요 없이 실제 데이터를 활용해 복잡한 구동 메커니즘에 대한 시뮬레이션-현실 격차(sim-to-real gap)를 해소합니다. UAN은 학습된 행동이 견고하고 전이 가능하도록 보장하여 보상 해킹을 완화합니다. 둘째, 기준 궤적을 초기 힌트로 활용하여 탐색을 안내하는 사전 훈련 및 미세 조정 전략을 사용합니다. 이러한 혁신을 통해 우리의 로봇 운동선수는 시뮬레이션에서 현실로 놀라운 충실도로 들어 올리기, 던지기, 끌기를 학습합니다.

## 参考
- http://arxiv.org/abs/2502.10894v1
