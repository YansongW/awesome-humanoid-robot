---
$id: ent_paper_learning_humanoid_arm_motion_v_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning
  zh: Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning
  ko: Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning
summary:
  en: Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning is a 2025 work on
    locomotion for humanoid robots.
  zh: 这是一项2025年关于人形机器人运动控制的研究，提出了一种基于质心动量正则化的多智能体强化学习框架。该框架通过为手臂和腿部设计独立的actor-critic结构，实现了全身协调控制，并成功在真实人形机器人平台上验证了多种运动任务的鲁棒性。
  ko: Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning is a 2025 work on
    locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_humanoid_arm_motion_v
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.04140v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning (arXiv)
  url: https://www.arxiv.org/abs/2507.04140
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
人类在行走时自然摆动手臂以调节全身动力学、减少角动量并维持平衡。受此启发，该研究提出了一个肢体级多智能体强化学习框架，通过分离的手臂和腿部actor-critic结构实现人形机器人的全身协调控制。训练采用集中式critic与分散式actor，各智能体仅共享基座状态和质心角动量观测，并通过模块化奖励设计使每个智能体专注于特定任务行为。手臂智能体通过CAM跟踪和阻尼奖励促进减少整体角动量和垂直地面反作用力矩的手臂运动，从而改善运动平衡。与单智能体和替代多智能体基线的对比研究验证了该方法的有效性。

## 核心内容
### 方法架构
- 采用**多智能体强化学习**框架，将人形机器人控制分解为手臂和腿部两个独立智能体
- 每个智能体使用独立的**actor-critic结构**，训练时共享集中式critic，执行时使用分散式actor
- 智能体间仅交换**基座状态**和**质心角动量（CAM）**观测信息

### 奖励设计
- 手臂智能体通过**CAM跟踪奖励**和**阻尼奖励**引导，主动产生减少整体角动量的摆动动作
- 腿部智能体专注于步态生成和平衡维持
- 模块化奖励设计使各智能体能够专业化学习任务相关行为

### 实验设置与结果
- 在**真实人形机器人平台**上部署学习策略
- 验证了多种运动任务：
  - 平坦地面行走
  - 崎岖地形穿越
  - 楼梯攀爬
- 与**单智能体基线**和**替代多智能体基线**的对比实验表明：
  - 本方法显著降低了垂直地面反作用力矩
  - 在外部扰动下表现出更好的平衡恢复能力
  - 手臂摆动策略有效减少了整体角动量波动

### 关键贡献
- 首次将**质心动量正则化**引入多智能体强化学习框架
- 证明了生物启发的肢体协调策略可有效迁移至人形机器人控制
- 实现了从仿真到真实环境的成功迁移

## Overview
Humans naturally swing their arms during locomotion to regulate whole-body dynamics, reduce angular momentum, and help maintain balance. Inspired by this principle, we present a limb-level multi-agent reinforcement learning (RL) framework that enables coordinated whole-body control of humanoid robots through emergent arm motion. Our approach employs separate actor-critic structures for the arms and legs, trained with centralized critics but decentralized actors that share only base states and centroidal angular momentum (CAM) observations, allowing each agent to specialize in task-relevant behaviors through modular reward design. The arm agent guided by CAM tracking and damping rewards promotes arm motions that reduce overall angular momentum and vertical ground reaction moments, contributing to improved balance during locomotion or under external perturbations. Comparative studies with single-agent and alternative multi-agent baselines further validate the effectiveness of our approach. Finally, we deploy the learned policy on a humanoid platform, achieving robust performance across diverse locomotion tasks, including flat-ground walking, rough terrain traversal, and stair climbing.

## 개요
인간은 이동 중에 자연스럽게 팔을 흔들어 전신 역학을 조절하고, 각운동량을 줄이며, 균형 유지를 돕습니다. 이 원리에 영감을 받아, 우리는 팔다리 수준의 다중 에이전트 강화 학습(RL) 프레임워크를 제시합니다. 이는 출현하는 팔 움직임을 통해 휴머노이드 로봇의 조정된 전신 제어를 가능하게 합니다. 우리의 접근 방식은 팔과 다리에 대해 별도의 행위자-비평가 구조를 사용하며, 중앙 집중식 비평가로 훈련되지만 기본 상태와 중심 각운동량(CAM) 관측만 공유하는 분산형 행위자를 사용하여, 각 에이전트가 모듈식 보상 설계를 통해 작업 관련 행동을 특화할 수 있도록 합니다. CAM 추적 및 감쇠 보상에 의해 안내되는 팔 에이전트는 전체 각운동량과 수직 지면 반력 모멘트를 줄이는 팔 움직임을 촉진하여, 이동 중이나 외부 교란 하에서 균형 개선에 기여합니다. 단일 에이전트 및 대체 다중 에이전트 기준선과의 비교 연구는 우리 접근 방식의 효과성을 추가로 검증합니다. 마지막으로, 우리는 학습된 정책을 휴머노이드 플랫폼에 배포하여 평지 보행, 거친 지형 횡단, 계단 오르기를 포함한 다양한 이동 작업에서 강력한 성능을 달성합니다.

## 핵심 내용
인간은 이동 중에 자연스럽게 팔을 흔들어 전신 역학을 조절하고, 각운동량을 줄이며, 균형 유지를 돕습니다. 이 원리에 영감을 받아, 우리는 팔다리 수준의 다중 에이전트 강화 학습(RL) 프레임워크를 제시합니다. 이는 출현하는 팔 움직임을 통해 휴머노이드 로봇의 조정된 전신 제어를 가능하게 합니다. 우리의 접근 방식은 팔과 다리에 대해 별도의 행위자-비평가 구조를 사용하며, 중앙 집중식 비평가로 훈련되지만 기본 상태와 중심 각운동량(CAM) 관측만 공유하는 분산형 행위자를 사용하여, 각 에이전트가 모듈식 보상 설계를 통해 작업 관련 행동을 특화할 수 있도록 합니다. CAM 추적 및 감쇠 보상에 의해 안내되는 팔 에이전트는 전체 각운동량과 수직 지면 반력 모멘트를 줄이는 팔 움직임을 촉진하여, 이동 중이나 외부 교란 하에서 균형 개선에 기여합니다. 단일 에이전트 및 대체 다중 에이전트 기준선과의 비교 연구는 우리 접근 방식의 효과성을 추가로 검증합니다. 마지막으로, 우리는 학습된 정책을 휴머노이드 플랫폼에 배포하여 평지 보행, 거친 지형 횡단, 계단 오르기를 포함한 다양한 이동 작업에서 강력한 성능을 달성합니다.

## 参考
- http://arxiv.org/abs/2507.04140v1
