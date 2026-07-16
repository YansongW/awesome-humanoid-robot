---
$id: ent_paper_coordinated_humanoid_robot_loc_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy
  zh: Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy
  ko: Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy
summary:
  en: Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy is a 2025 work on locomotion
    for humanoid robots.
  zh: Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy is a 2025 work on locomotion
    for humanoid robots.
  ko: Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy is a 2025 work on locomotion
    for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- coordinated_humanoid_robot_loc
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.01247v2.
sources:
- id: src_001
  type: paper
  title: Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy (arXiv)
  url: https://arxiv.org/abs/2508.01247
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The human nervous system exhibits bilateral symmetry, enabling coordinated and balanced movements. However, existing Deep Reinforcement Learning (DRL) methods for humanoid robots neglect morphological symmetry of the robot, leading to uncoordinated and suboptimal behaviors. Inspired by human motor control, we propose Symmetry Equivariant Policy (SE-Policy), a new DRL framework that embeds strict symmetry equivariance in the actor and symmetry invariance in the critic without additional hyperparameters. SE-Policy enforces consistent behaviors across symmetric observations, producing temporally and spatially coordinated motions with higher task performance. Extensive experiments on velocity tracking tasks, conducted in both simulation and real-world deployment with the Unitree G1 humanoid robot, demonstrate that SE-Policy improves tracking accuracy by up to 40% compared to state-of-the-art baselines, while achieving superior spatial-temporal coordination. These results demonstrate the effectiveness of SE-Policy and its broad applicability to humanoid robots.

## 核心内容
The human nervous system exhibits bilateral symmetry, enabling coordinated and balanced movements. However, existing Deep Reinforcement Learning (DRL) methods for humanoid robots neglect morphological symmetry of the robot, leading to uncoordinated and suboptimal behaviors. Inspired by human motor control, we propose Symmetry Equivariant Policy (SE-Policy), a new DRL framework that embeds strict symmetry equivariance in the actor and symmetry invariance in the critic without additional hyperparameters. SE-Policy enforces consistent behaviors across symmetric observations, producing temporally and spatially coordinated motions with higher task performance. Extensive experiments on velocity tracking tasks, conducted in both simulation and real-world deployment with the Unitree G1 humanoid robot, demonstrate that SE-Policy improves tracking accuracy by up to 40% compared to state-of-the-art baselines, while achieving superior spatial-temporal coordination. These results demonstrate the effectiveness of SE-Policy and its broad applicability to humanoid robots.

## 参考
- http://arxiv.org/abs/2508.01247v2

## Overview
The human nervous system exhibits bilateral symmetry, enabling coordinated and balanced movements. However, existing Deep Reinforcement Learning (DRL) methods for humanoid robots neglect morphological symmetry of the robot, leading to uncoordinated and suboptimal behaviors. Inspired by human motor control, we propose Symmetry Equivariant Policy (SE-Policy), a new DRL framework that embeds strict symmetry equivariance in the actor and symmetry invariance in the critic without additional hyperparameters. SE-Policy enforces consistent behaviors across symmetric observations, producing temporally and spatially coordinated motions with higher task performance. Extensive experiments on velocity tracking tasks, conducted in both simulation and real-world deployment with the Unitree G1 humanoid robot, demonstrate that SE-Policy improves tracking accuracy by up to 40% compared to state-of-the-art baselines, while achieving superior spatial-temporal coordination. These results demonstrate the effectiveness of SE-Policy and its broad applicability to humanoid robots.

## Content
The human nervous system exhibits bilateral symmetry, enabling coordinated and balanced movements. However, existing Deep Reinforcement Learning (DRL) methods for humanoid robots neglect morphological symmetry of the robot, leading to uncoordinated and suboptimal behaviors. Inspired by human motor control, we propose Symmetry Equivariant Policy (SE-Policy), a new DRL framework that embeds strict symmetry equivariance in the actor and symmetry invariance in the critic without additional hyperparameters. SE-Policy enforces consistent behaviors across symmetric observations, producing temporally and spatially coordinated motions with higher task performance. Extensive experiments on velocity tracking tasks, conducted in both simulation and real-world deployment with the Unitree G1 humanoid robot, demonstrate that SE-Policy improves tracking accuracy by up to 40% compared to state-of-the-art baselines, while achieving superior spatial-temporal coordination. These results demonstrate the effectiveness of SE-Policy and its broad applicability to humanoid robots.

## 개요
인간의 신경계는 양측 대칭성을 나타내며, 이를 통해 조화롭고 균형 잡힌 움직임이 가능합니다. 그러나 기존의 인간형 로봇을 위한 심층 강화 학습(DRL) 방법은 로봇의 형태적 대칭성을 무시하여 비조화적이고 최적이 아닌 행동을 초래합니다. 인간의 운동 제어에서 영감을 받아, 우리는 추가 하이퍼파라미터 없이 액터에 엄격한 대칭 등변성(symmetry equivariance)을, 크리틱에 대칭 불변성(symmetry invariance)을 내장한 새로운 DRL 프레임워크인 SE-Policy(Symmetry Equivariant Policy)를 제안합니다. SE-Policy는 대칭적인 관찰에 걸쳐 일관된 행동을 강제하여, 시간적 및 공간적으로 조화로운 움직임과 더 높은 작업 성능을 생성합니다. Unitree G1 인간형 로봇을 사용한 시뮬레이션 및 실제 환경 배포에서 수행된 속도 추적 작업에 대한 광범위한 실험은, SE-Policy가 최첨단 기준선과 비교하여 추적 정확도를 최대 40% 향상시키면서 우수한 시공간 조정을 달성함을 보여줍니다. 이러한 결과는 SE-Policy의 효과성과 인간형 로봇에 대한 광범위한 적용 가능성을 입증합니다.

## 핵심 내용
인간의 신경계는 양측 대칭성을 나타내며, 이를 통해 조화롭고 균형 잡힌 움직임이 가능합니다. 그러나 기존의 인간형 로봇을 위한 심층 강화 학습(DRL) 방법은 로봇의 형태적 대칭성을 무시하여 비조화적이고 최적이 아닌 행동을 초래합니다. 인간의 운동 제어에서 영감을 받아, 우리는 추가 하이퍼파라미터 없이 액터에 엄격한 대칭 등변성(symmetry equivariance)을, 크리틱에 대칭 불변성(symmetry invariance)을 내장한 새로운 DRL 프레임워크인 SE-Policy(Symmetry Equivariant Policy)를 제안합니다. SE-Policy는 대칭적인 관찰에 걸쳐 일관된 행동을 강제하여, 시간적 및 공간적으로 조화로운 움직임과 더 높은 작업 성능을 생성합니다. Unitree G1 인간형 로봇을 사용한 시뮬레이션 및 실제 환경 배포에서 수행된 속도 추적 작업에 대한 광범위한 실험은, SE-Policy가 최첨단 기준선과 비교하여 추적 정확도를 최대 40% 향상시키면서 우수한 시공간 조정을 달성함을 보여줍니다. 이러한 결과는 SE-Policy의 효과성과 인간형 로봇에 대한 광범위한 적용 가능성을 입증합니다.
