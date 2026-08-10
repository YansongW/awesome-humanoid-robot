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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.10894v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (708 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2502.10894v1

## 개요
전통적인 추적 보상 기반 훈련 방법은 로봇을 참조 궤적을 따라 움직이도록만 유도하여, 진정한 동적 목표 지향 행동을 구현하기 어렵습니다. 본 논문은 두 단계 훈련 프로세스를 제안합니다: 먼저 Unsupervised Actuator Net (UAN)을 도입하여 실제 데이터를 활용하고 토크 센싱에 의존하지 않고 복잡한 구동 메커니즘의 시뮬레이션-현실 전이 문제를 해결합니다; 다음으로 사전 훈련-미세 조정 전략을 채택하여 참조 궤적을 초기 프롬프트로 사용해 탐색을 유도합니다. 이 방법은 작업 보상이 쉽게 악용되는(보상 해킹) 문제와 탐색 방향 부족 문제를 효과적으로 완화하여, 로봇이 역도, 투척, 끌기 등의 운동 조작 기술을 학습할 수 있게 하고, 시뮬레이션-현실 전이에서 높은 충실도를 유지합니다.

## 핵심 내용
### 핵심 과제
- 전통적인 추적 보상은 로봇을 참조 궤적을 따라 움직이도록만 유도하여, 진정한 동적 목표 지향 행동을 구동할 수 없음
- 작업 보상(예: "공을 최대한 멀리 던지기", "물건을 최대한 빨리 들어 올리기")은 민첩성과 힘을 자극할 수 있지만 두 가지 주요 문제가 있음:
  - 보상 해킹: 작업 보상이 쉽게 악용되어 의도하지 않은 행동을 초래함
  - 탐색 방향 부족: 효과적인 유도가 없으면 탐색 과정이 비효율에 빠질 수 있음

### 방법 아키텍처
#### 1단계: Unsupervised Actuator Net (UAN)
- 실제 세계 데이터를 활용하여 토크 센싱에 의존하지 않고 복잡한 구동 메커니즘의 시뮬레이션-현실 격차를 해소
- 학습된 행동이 견고하고 전이 가능하도록 보장하여 보상 해킹 문제를 효과적으로 완화

#### 2단계: 사전 훈련-미세 조정 전략
- 참조 궤적을 초기 프롬프트로 사용하여 탐색 과정을 유도
- 사전 훈련 단계에서 기초 행동을 구축한 후, 미세 조정을 통해 작업 보상을 최적화

### 실험 설정 및 결과
- 로봇 운동선수가 시뮬레이션 환경에서 역도, 투척, 끌기 등의 운동 조작 기술을 학습
- 시뮬레이션에서 현실로 전이할 때 행동이 높은 충실도를 유지하여 UAN과 사전 훈련-미세 조정 전략의 효과를 검증
- 이 방법은 로봇이 실제 운동선수에 필적하는 민첩성과 힘 성능을 발휘할 수 있게 함
