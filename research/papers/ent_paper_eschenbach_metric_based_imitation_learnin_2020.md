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
  zh: 本文提出了一种用于不同机器人实体之间的距离度量，以解决模仿学习中的对应问题，并将其应用于基于神经网络的静态姿态模仿和基于PPO强化学习的动态运动模仿。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2003.02638v1.
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
The development of autonomous robotic systems that can learn from human demonstrations to imitate a desired behavior - rather than being manually programmed - has huge technological potential. One major challenge in imitation learning is the correspondence problem: how to establish corresponding states and actions between expert and learner, when the embodiments of the agents are different (morphology, dynamics, degrees of freedom, etc.). Many existing approaches in imitation learning circumvent the correspondence problem, for example, kinesthetic teaching or teleoperation, which are performed on the robot. In this work we explicitly address the correspondence problem by introducing a distance measure between dissimilar embodiments. This measure is then used as a loss function for static pose imitation and as a feedback signal within a model-free deep reinforcement learning framework for dynamic movement imitation between two anthropomorphic robotic arms in simulation. We find that the measure is well suited for describing the similarity between embodiments and for learning imitation policies by distance minimization.

## 核心内容
The development of autonomous robotic systems that can learn from human demonstrations to imitate a desired behavior - rather than being manually programmed - has huge technological potential. One major challenge in imitation learning is the correspondence problem: how to establish corresponding states and actions between expert and learner, when the embodiments of the agents are different (morphology, dynamics, degrees of freedom, etc.). Many existing approaches in imitation learning circumvent the correspondence problem, for example, kinesthetic teaching or teleoperation, which are performed on the robot. In this work we explicitly address the correspondence problem by introducing a distance measure between dissimilar embodiments. This measure is then used as a loss function for static pose imitation and as a feedback signal within a model-free deep reinforcement learning framework for dynamic movement imitation between two anthropomorphic robotic arms in simulation. We find that the measure is well suited for describing the similarity between embodiments and for learning imitation policies by distance minimization.

## 参考
- http://arxiv.org/abs/2003.02638v1

