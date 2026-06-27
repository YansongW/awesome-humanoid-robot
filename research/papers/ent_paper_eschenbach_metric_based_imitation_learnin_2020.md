---
$id: ent_paper_eschenbach_metric_based_imitation_learnin_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Metric-Based Imitation Learning Between Two Dissimilar Anthropomorphic Robotic
    Arms
  zh: 基于度量的两个不同拟人机器人手臂之间的模仿学习
  ko: 두 개의 상이한 의인화 로봇 팔 간의 메트릭 기반 모방 학습
summary:
  en: This paper introduces a distance measure between dissimilar robotic embodiments
    to solve the correspondence problem in imitation learning, applying it to static-pose
    imitation via neural networks and dynamic-motion imitation via PPO-based reinforcement
    learning in simulation.
  zh: 本文提出了一种用于不同机器人实体之间的距离度量，以解决模仿学习中的对应问题，并将其应用于基于神经网络的静态姿态模仿和基于PPO强化学习的动态运动模仿。
  ko: 본 논문은 모방 학습의 대응 문제를 해결하기 위해 상이한 로봇 실체 간 거리 측정을 제안하고, 이를 신경망 기반 정적 자세 모방 및 PPO
    강화 학습 기반 동적 동작 모방에 적용한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text verification
    needed before promotion to verified.
sources:
- id: src_001
  type: paper
  title: Metric-Based Imitation Learning Between Two Dissimilar Anthropomorphic Robotic
    Arms
  url: https://arxiv.org/abs/2003.02638
  date: '2020'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Imitation learning promises to let robots acquire behaviors from demonstrations rather than manual programming, but a major obstacle is the correspondence problem: how to map states and actions between expert and learner robots that differ in morphology, dynamics, and degrees of freedom. This paper confronts that problem directly by defining a distance measure between dissimilar embodiments. The authors represent embodiment states using frames and twists, and construct correspondences between candidate points on the expert and learner bodies. The resulting distance is used both as a supervised loss for neural-network static-pose imitation and as a reward signal for model-free deep reinforcement learning of dynamic movements. Experiments are conducted in simulation on planar manipulators and on pairs of Franka Emika Panda arms.

The distance measure is designed to capture geometric and kinematic similarity without requiring identical kinematic structures. For static imitation, a neural network maps the learner's joint configuration to a pose that minimizes the distance to the expert pose. For dynamic imitation, the distance is used as the reward within a PPO-based reinforcement learning loop, enabling the learner to reproduce trajectories demonstrated by the expert. The authors note that practical difficulties such as local minima in the distance function and dynamic instability required modifications, including disabling gravity and using a myopic discount factor.

The work situates itself as an alternative to kinesthetic teaching and teleoperation, which avoid the correspondence problem by collecting demonstrations directly on the learner robot. By instead learning a cross-embodiment mapping, the method aims toward more flexible robot programming where a human or another robot can demonstrate behavior on one platform and have it transferred to a different anthropomorphic arm.

## Key Contributions

- Defines embodiment states in terms of frames, twists, and candidate points to enable cross-embodiment comparison.
- Proposes a distance measure between dissimilar embodiments based on frame correspondences.
- Demonstrates static pose imitation by training neural networks with the distance-based loss.
- Demonstrates dynamic motion imitation by using the distance measure as a reward signal in model-free deep reinforcement learning with PPO.
- Evaluates the approach in simulation on planar manipulators and Franka Emika Panda arms.

## Relevance to Humanoid Robotics

Humanoid robots frequently need to replicate behaviors demonstrated by humans or by other robots whose kinematics differ from their own. The correspondence problem is therefore central to motion retargeting, reprogramming, and rapid deployment of humanoids on production lines or in service tasks. This paper's distance-based approach provides a principled way to compare and transfer motions across embodiments, which is directly applicable when the same skill must be executed by humanoids of different sizes, joint layouts, or degrees of freedom.

Because the method is model-free and relies on a learned distance reward, it can in principle be applied whenever a simulator or real-world evaluation of the distance is available. For humanoid applications, this offers a path toward reducing the engineering effort required to port skills across robot platforms, though the simulation-only evaluation and the reported local-minima and dynamic-stability issues indicate that further work is needed before reliable hardware deployment.
