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
  zh: 'The development of autonomous robotic systems that can learn from human demonstrations to imitate a desired behavior
    - rather than being manually programmed - has huge technological potential. One major challenge in imitation learning
    is the correspondence problem: how to establish corresponding states and actions between expert and learner, when the
    embodiments of the agents are different (morphology, dynamics, degrees of freedom, etc.). Many existing approaches in
    imitation learning circumvent the correspondence problem, for example, kinesthetic teaching or teleoperation, which are
    performed'
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

## Overview
The development of autonomous robotic systems that can learn from human demonstrations to imitate a desired behavior - rather than being manually programmed - has huge technological potential. One major challenge in imitation learning is the correspondence problem: how to establish corresponding states and actions between expert and learner, when the embodiments of the agents are different (morphology, dynamics, degrees of freedom, etc.). Many existing approaches in imitation learning circumvent the correspondence problem, for example, kinesthetic teaching or teleoperation, which are performed on the robot. In this work we explicitly address the correspondence problem by introducing a distance measure between dissimilar embodiments. This measure is then used as a loss function for static pose imitation and as a feedback signal within a model-free deep reinforcement learning framework for dynamic movement imitation between two anthropomorphic robotic arms in simulation. We find that the measure is well suited for describing the similarity between embodiments and for learning imitation policies by distance minimization.

## Content
The development of autonomous robotic systems that can learn from human demonstrations to imitate a desired behavior - rather than being manually programmed - has huge technological potential. One major challenge in imitation learning is the correspondence problem: how to establish corresponding states and actions between expert and learner, when the embodiments of the agents are different (morphology, dynamics, degrees of freedom, etc.). Many existing approaches in imitation learning circumvent the correspondence problem, for example, kinesthetic teaching or teleoperation, which are performed on the robot. In this work we explicitly address the correspondence problem by introducing a distance measure between dissimilar embodiments. This measure is then used as a loss function for static pose imitation and as a feedback signal within a model-free deep reinforcement learning framework for dynamic movement imitation between two anthropomorphic robotic arms in simulation. We find that the measure is well suited for describing the similarity between embodiments and for learning imitation policies by distance minimization.

## 개요
인간의 시연을 통해 학습하여 원하는 행동을 모방할 수 있는 자율 로봇 시스템의 개발(수동 프로그래밍 대신)은 엄청난 기술적 잠재력을 지니고 있습니다. 모방 학습의 주요 과제 중 하나는 대응 문제(correspondence problem)입니다. 즉, 에이전트의 구현체(형태, 동역학, 자유도 등)가 다를 때 전문가와 학습자 간의 상태와 행동을 어떻게 대응시킬 것인가 하는 문제입니다. 모방 학습의 많은 기존 접근 방식은 로봇에서 수행되는 운동 감각 교육(kinaesthetic teaching)이나 원격 조작(teleoperation)과 같이 대응 문제를 우회합니다. 본 연구에서는 서로 다른 구현체 간의 거리 측정(distance measure)을 도입하여 대응 문제를 명시적으로 해결합니다. 이 측정값은 정적 자세 모방을 위한 손실 함수로, 그리고 시뮬레이션에서 두 인간형 로봇 팔 간의 동적 움직임 모방을 위한 모델 프리 심층 강화 학습(model-free deep reinforcement learning) 프레임워크 내에서 피드백 신호로 사용됩니다. 우리는 이 측정값이 구현체 간의 유사성을 설명하고 거리 최소화를 통해 모방 정책을 학습하는 데 적합하다는 것을 발견했습니다.

## 핵심 내용
인간의 시연을 통해 학습하여 원하는 행동을 모방할 수 있는 자율 로봇 시스템의 개발(수동 프로그래밍 대신)은 엄청난 기술적 잠재력을 지니고 있습니다. 모방 학습의 주요 과제 중 하나는 대응 문제(correspondence problem)입니다. 즉, 에이전트의 구현체(형태, 동역학, 자유도 등)가 다를 때 전문가와 학습자 간의 상태와 행동을 어떻게 대응시킬 것인가 하는 문제입니다. 모방 학습의 많은 기존 접근 방식은 로봇에서 수행되는 운동 감각 교육(kinaesthetic teaching)이나 원격 조작(teleoperation)과 같이 대응 문제를 우회합니다. 본 연구에서는 서로 다른 구현체 간의 거리 측정(distance measure)을 도입하여 대응 문제를 명시적으로 해결합니다. 이 측정값은 정적 자세 모방을 위한 손실 함수로, 그리고 시뮬레이션에서 두 인간형 로봇 팔 간의 동적 움직임 모방을 위한 모델 프리 심층 강화 학습(model-free deep reinforcement learning) 프레임워크 내에서 피드백 신호로 사용됩니다. 우리는 이 측정값이 구현체 간의 유사성을 설명하고 거리 최소화를 통해 모방 정책을 학습하는 데 적합하다는 것을 발견했습니다.
