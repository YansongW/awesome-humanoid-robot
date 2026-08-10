---
$id: ent_paper_eschenbach_metric_based_imitation_learnin_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Metric-Based Imitation Learning Between Two Dissimilar Anthropomorphic Robotic Arms
  zh: 基于度量的两个不同拟人机器人手臂之间的模仿学习
  ko: 두 개의 상이한 의인화 로봇 팔 간의 메트릭 기반 모방 학습
summary:
  en: This paper introduces a distance measure between dissimilar robotic embodiments to solve the correspondence problem
    in imitation learning, applying it to static-pose imitation via neural networks and dynamic-motion imitation via PPO-based
    reinforcement learning in simulation.
  zh: 本文提出了一种用于解决模仿学习中对应问题的距离度量，该度量适用于不同形态的机器人实体。研究将该度量作为损失函数用于静态姿态模仿，并作为反馈信号用于基于PPO的强化学习动态运动模仿。实验在两个不同形态的仿人机械臂之间进行仿真验证。
  ko: 본 논문은 모방 학습의 대응 문제를 해결하기 위해 상이한 로봇 실체 간 거리 측정을 제안하고, 이를 신경망 기반 정적 자세 모방 및 PPO 강화 학습 기반 동적 동작 모방에 적용한다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- imitation_learning
- cross_embodiment
- motion_retargeting
- anthropomorphic_arms
- correspondence_problem
- distance_measure
- proximal_policy_optimization
- deep_reinforcement_learning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2003.02638v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (701 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Metric-Based Imitation Learning Between Two Dissimilar Anthropomorphic Robotic Arms
  url: https://arxiv.org/abs/2003.02638
  date: '2020'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
本文针对模仿学习中的对应问题，提出了一种能够衡量不同机器人实体之间相似性的距离度量。该度量被应用于两个不同形态的仿人机械臂的模仿任务中：对于静态姿态模仿，将其作为神经网络训练的损失函数；对于动态运动模仿，则将其作为基于PPO的无模型深度强化学习框架中的反馈信号。实验结果表明，该距离度量能够有效描述不同实体之间的相似性，并通过距离最小化学习到有效的模仿策略。

## 核心内容
### 研究背景与问题
- 模仿学习面临的核心挑战是**对应问题**：当专家和学习者的机器人实体不同（如形态、动力学、自由度等差异）时，如何建立对应的状态和动作。
- 现有方法如**kinesthetic teaching**（动觉示教）和**teleoperation**（遥操作）通常绕开对应问题，直接在目标机器人上操作。

### 方法
- 提出一种**距离度量**，用于量化两个不同机器人实体之间的相似性。
- **静态姿态模仿**：将该距离度量作为神经网络的损失函数，通过最小化距离来学习姿态映射。
- **动态运动模仿**：将该距离度量作为反馈信号，集成到**PPO-based**（基于近端策略优化）的无模型深度强化学习框架中，通过距离最小化学习运动策略。

### 实验设置
- 在仿真环境中进行实验，使用两个**不同形态的仿人机械臂**（anthropomorphic robotic arms）。
- 分别测试静态姿态模仿和动态运动模仿任务。

### 关键结果与结论
- 该距离度量能够有效描述不同机器人实体之间的相似性。
- 通过距离最小化，成功学习到有效的模仿策略，验证了方法的可行性。

## Overview
The development of autonomous robotic systems that can learn from human demonstrations to imitate a desired behavior - rather than being manually programmed - has huge technological potential. One major challenge in imitation learning is the correspondence problem: how to establish corresponding states and actions between expert and learner, when the embodiments of the agents are different (morphology, dynamics, degrees of freedom, etc.). Many existing approaches in imitation learning circumvent the correspondence problem, for example, kinesthetic teaching or teleoperation, which are performed on the robot. In this work we explicitly address the correspondence problem by introducing a distance measure between dissimilar embodiments. This measure is then used as a loss function for static pose imitation and as a feedback signal within a model-free deep reinforcement learning framework for dynamic movement imitation between two anthropomorphic robotic arms in simulation. We find that the measure is well suited for describing the similarity between embodiments and for learning imitation policies by distance minimization.

## 参考
- http://arxiv.org/abs/2003.02638v1

## 개요
본 논문은 모방 학습에서의 대응 문제를 해결하기 위해, 서로 다른 로봇 개체 간의 유사성을 측정할 수 있는 거리 척도를 제안한다. 이 척도는 서로 다른 형태를 가진 두 개의 인간형 로봇 팔의 모방 작업에 적용된다: 정적 자세 모방의 경우 신경망 훈련의 손실 함수로 사용되며, 동적 운동 모방의 경우 PPO 기반의 모델 프리(model-free) 심층 강화 학습 프레임워크에서 피드백 신호로 사용된다. 실험 결과, 이 거리 척도는 서로 다른 개체 간의 유사성을 효과적으로 설명할 수 있으며, 거리 최소화를 통해 효과적인 모방 정책을 학습할 수 있음을 보여준다.

## 핵심 내용
### 연구 배경 및 문제
- 모방 학습이 직면한 핵심 과제는 **대응 문제**이다: 전문가와 학습자의 로봇 개체가 다를 때(형태, 동역학, 자유도 등의 차이), 상태와 행동 간의 대응을 어떻게 설정할 것인가의 문제이다.
- 기존 방법인 **kinesthetic teaching**(운동 감각 시범) 및 **teleoperation**(원격 조작)은 일반적으로 대응 문제를 우회하여 대상 로봇에서 직접 조작한다.

### 방법
- 서로 다른 두 로봇 개체 간의 유사성을 정량화하는 **거리 척도**를 제안한다.
- **정적 자세 모방**: 이 거리 척도를 신경망의 손실 함수로 사용하여, 거리 최소화를 통해 자세 매핑을 학습한다.
- **동적 운동 모방**: 이 거리 척도를 피드백 신호로 사용하여, **PPO 기반**(근접 정책 최적화 기반)의 모델 프리 심층 강화 학습 프레임워크에 통합하고, 거리 최소화를 통해 운동 정책을 학습한다.

### 실험 설정
- 시뮬레이션 환경에서 실험을 수행하며, 서로 다른 형태를 가진 두 개의 **인간형 로봇 팔**(anthropomorphic robotic arms)을 사용한다.
- 정적 자세 모방과 동적 운동 모방 작업을 각각 테스트한다.

### 주요 결과 및 결론
- 이 거리 척도는 서로 다른 로봇 개체 간의 유사성을 효과적으로 설명할 수 있다.
- 거리 최소화를 통해 효과적인 모방 정책을 성공적으로 학습하여, 방법의 타당성을 검증하였다.
