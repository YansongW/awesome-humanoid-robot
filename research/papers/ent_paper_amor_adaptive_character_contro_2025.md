---
$id: ent_paper_amor_adaptive_character_contro_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AMOR: Adaptive Character Control through Multi-Objective Reinforcement Learning'
  zh: 'AMOR: Adaptive Character Control through Multi-Objective Reinforcement Learning'
  ko: 'AMOR: Adaptive Character Control through Multi-Objective Reinforcement Learning'
summary:
  en: 'AMOR: Adaptive Character Control through Multi-Objective Reinforcement Learning is a 2025 work on physics-based character
    animation for humanoid robots.'
  zh: 'AMOR: Adaptive Character Control through Multi-Objective Reinforcement Learning is a 2025 work on physics-based character
    animation for humanoid robots.'
  ko: 'AMOR: Adaptive Character Control through Multi-Objective Reinforcement Learning is a 2025 work on physics-based character
    animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- amor
- character_animation
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.23708v1.
sources:
- id: src_001
  type: paper
  title: 'AMOR: Adaptive Character Control through Multi-Objective Reinforcement Learning (arXiv)'
  url: https://arxiv.org/abs/2505.23708
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning (RL) has significantly advanced the control of physics-based and robotic characters that track kinematic reference motion. However, methods typically rely on a weighted sum of conflicting reward functions, requiring extensive tuning to achieve a desired behavior. Due to the computational cost of RL, this iterative process is a tedious, time-intensive task. Furthermore, for robotics applications, the weights need to be chosen such that the policy performs well in the real world, despite inevitable sim-to-real gaps. To address these challenges, we propose a multi-objective reinforcement learning framework that trains a single policy conditioned on a set of weights, spanning the Pareto front of reward trade-offs. Within this framework, weights can be selected and tuned after training, significantly speeding up iteration time. We demonstrate how this improved workflow can be used to perform highly dynamic motions with a robot character. Moreover, we explore how weight-conditioned policies can be leveraged in hierarchical settings, using a high-level policy to dynamically select weights according to the current task. We show that the multi-objective policy encodes a diverse spectrum of behaviors, facilitating efficient adaptation to novel tasks.

## 核心内容
Reinforcement learning (RL) has significantly advanced the control of physics-based and robotic characters that track kinematic reference motion. However, methods typically rely on a weighted sum of conflicting reward functions, requiring extensive tuning to achieve a desired behavior. Due to the computational cost of RL, this iterative process is a tedious, time-intensive task. Furthermore, for robotics applications, the weights need to be chosen such that the policy performs well in the real world, despite inevitable sim-to-real gaps. To address these challenges, we propose a multi-objective reinforcement learning framework that trains a single policy conditioned on a set of weights, spanning the Pareto front of reward trade-offs. Within this framework, weights can be selected and tuned after training, significantly speeding up iteration time. We demonstrate how this improved workflow can be used to perform highly dynamic motions with a robot character. Moreover, we explore how weight-conditioned policies can be leveraged in hierarchical settings, using a high-level policy to dynamically select weights according to the current task. We show that the multi-objective policy encodes a diverse spectrum of behaviors, facilitating efficient adaptation to novel tasks.

## 参考
- http://arxiv.org/abs/2505.23708v1

## Overview
Reinforcement learning (RL) has significantly advanced the control of physics-based and robotic characters that track kinematic reference motion. However, methods typically rely on a weighted sum of conflicting reward functions, requiring extensive tuning to achieve a desired behavior. Due to the computational cost of RL, this iterative process is a tedious, time-intensive task. Furthermore, for robotics applications, the weights need to be chosen such that the policy performs well in the real world, despite inevitable sim-to-real gaps. To address these challenges, we propose a multi-objective reinforcement learning framework that trains a single policy conditioned on a set of weights, spanning the Pareto front of reward trade-offs. Within this framework, weights can be selected and tuned after training, significantly speeding up iteration time. We demonstrate how this improved workflow can be used to perform highly dynamic motions with a robot character. Moreover, we explore how weight-conditioned policies can be leveraged in hierarchical settings, using a high-level policy to dynamically select weights according to the current task. We show that the multi-objective policy encodes a diverse spectrum of behaviors, facilitating efficient adaptation to novel tasks.

## Content
Reinforcement learning (RL) has significantly advanced the control of physics-based and robotic characters that track kinematic reference motion. However, methods typically rely on a weighted sum of conflicting reward functions, requiring extensive tuning to achieve a desired behavior. Due to the computational cost of RL, this iterative process is a tedious, time-intensive task. Furthermore, for robotics applications, the weights need to be chosen such that the policy performs well in the real world, despite inevitable sim-to-real gaps. To address these challenges, we propose a multi-objective reinforcement learning framework that trains a single policy conditioned on a set of weights, spanning the Pareto front of reward trade-offs. Within this framework, weights can be selected and tuned after training, significantly speeding up iteration time. We demonstrate how this improved workflow can be used to perform highly dynamic motions with a robot character. Moreover, we explore how weight-conditioned policies can be leveraged in hierarchical settings, using a high-level policy to dynamically select weights according to the current task. We show that the multi-objective policy encodes a diverse spectrum of behaviors, facilitating efficient adaptation to novel tasks.

## 개요
강화 학습(RL)은 운동학적 참조 동작을 추적하는 물리 기반 및 로봇 캐릭터의 제어를 크게 발전시켰습니다. 그러나 기존 방법들은 일반적으로 상충되는 보상 함수들의 가중 합에 의존하며, 원하는 행동을 달성하기 위해 광범위한 튜닝이 필요합니다. RL의 계산 비용으로 인해 이 반복적 과정은 지루하고 시간이 많이 소요되는 작업입니다. 더 나아가 로봇 공학 응용에서는 필연적인 시뮬레이션-현실 간극(sim-to-real gap)에도 불구하고 정책이 실제 세계에서 잘 작동하도록 가중치를 선택해야 합니다. 이러한 문제를 해결하기 위해, 우리는 보상 트레이드오프의 파레토 프론트(Pareto front)를 포괄하는 가중치 집합에 조건화된 단일 정책을 훈련하는 다중 목표 강화 학습 프레임워크를 제안합니다. 이 프레임워크 내에서 가중치는 훈련 후에 선택 및 튜닝될 수 있어 반복 시간을 크게 단축시킵니다. 우리는 이 개선된 워크플로우를 사용하여 로봇 캐릭터로 고도로 역동적인 동작을 수행하는 방법을 시연합니다. 또한, 계층적 설정에서 가중치 조건화 정책을 활용하는 방법을 탐구하며, 상위 수준 정책을 사용하여 현재 작업에 따라 동적으로 가중치를 선택합니다. 다중 목표 정책이 다양한 행동 스펙트럼을 인코딩하여 새로운 작업에 대한 효율적인 적응을 촉진함을 보여줍니다.

## 핵심 내용
강화 학습(RL)은 운동학적 참조 동작을 추적하는 물리 기반 및 로봇 캐릭터의 제어를 크게 발전시켰습니다. 그러나 기존 방법들은 일반적으로 상충되는 보상 함수들의 가중 합에 의존하며, 원하는 행동을 달성하기 위해 광범위한 튜닝이 필요합니다. RL의 계산 비용으로 인해 이 반복적 과정은 지루하고 시간이 많이 소요되는 작업입니다. 더 나아가 로봇 공학 응용에서는 필연적인 시뮬레이션-현실 간극(sim-to-real gap)에도 불구하고 정책이 실제 세계에서 잘 작동하도록 가중치를 선택해야 합니다. 이러한 문제를 해결하기 위해, 우리는 보상 트레이드오프의 파레토 프론트(Pareto front)를 포괄하는 가중치 집합에 조건화된 단일 정책을 훈련하는 다중 목표 강화 학습 프레임워크를 제안합니다. 이 프레임워크 내에서 가중치는 훈련 후에 선택 및 튜닝될 수 있어 반복 시간을 크게 단축시킵니다. 우리는 이 개선된 워크플로우를 사용하여 로봇 캐릭터로 고도로 역동적인 동작을 수행하는 방법을 시연합니다. 또한, 계층적 설정에서 가중치 조건화 정책을 활용하는 방법을 탐구하며, 상위 수준 정책을 사용하여 현재 작업에 따라 동적으로 가중치를 선택합니다. 다중 목표 정책이 다양한 행동 스펙트럼을 인코딩하여 새로운 작업에 대한 효율적인 적응을 촉진함을 보여줍니다.
