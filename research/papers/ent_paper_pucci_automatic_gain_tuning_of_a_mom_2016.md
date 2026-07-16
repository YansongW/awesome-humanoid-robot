---
$id: ent_paper_pucci_automatic_gain_tuning_of_a_mom_2016
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Automatic Gain Tuning of a Momentum Based Balancing Controller for Humanoid Robots
  zh: 人形机器人基于动量平衡控制器的自动增益调节
  ko: 휴머노이드 로봇을 위한 모멘텀 기반 균형 제어기의 자동 이득 튜닝
summary:
  en: Proposes an automatic gain-tuning method for a momentum-based balancing controller for humanoid robots by linearizing
    the closed-loop constrained joint-space dynamics and optimizing gains to match desired stiffness and damping, validated
    in simulation on the iCub humanoid.
  zh: 提出了一种针对人形机器人基于动量的平衡控制器的自动增益调节方法，通过线性化闭环约束关节空间动力学并优化增益以匹配期望的刚度和阻尼，在iCub人形机器人仿真中进行了验证。
  ko: 휴머노이드 로봇을 위한 모멘텀 기반 균형 제어기의 자동 이득 튜닝 기법을 제안하며, 폐쇄 루프 구속 관절 공간 동역학을 선형화하고 이득을 최적화하여 원하는 강성과 감쇄 특성을 얻으며, iCub 휴머노이드 시뮬레이션으로
    검증함.
domains:
- 07_ai_models_algorithms
- 02_components
- 05_mass_production
layers:
- intelligence
- midstream
- upstream
functional_roles:
- intelligence
- knowledge
tags:
- momentum_based_control
- balancing_controller
- gain_tuning
- floating_base
- centroidal_dynamics
- joint_space_linearization
- symmetric_positive_definite
- icub
- humanoid_robot
- simulation
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1610.02849v3.
sources:
- id: src_001
  type: paper
  title: Automatic Gain Tuning of a Momentum Based Balancing Controller for Humanoid Robots
  url: https://arxiv.org/abs/1610.02849
  date: '2016'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
This paper proposes a technique for automatic gain tuning of a momentum based balancing controller for humanoid robots. The controller ensures the stabilization of the centroidal dynamics and the associated zero dynamics. Then, the closed-loop, constrained joint space dynamics is linearized and the controller's gains are chosen so as to obtain desired properties of the linearized system. Symmetry and positive definiteness constraints of gain matrices are enforced by proposing a tracker for symmetric positive definite matrices. Simulation results are carried out on the humanoid robot iCub.

## 核心内容
This paper proposes a technique for automatic gain tuning of a momentum based balancing controller for humanoid robots. The controller ensures the stabilization of the centroidal dynamics and the associated zero dynamics. Then, the closed-loop, constrained joint space dynamics is linearized and the controller's gains are chosen so as to obtain desired properties of the linearized system. Symmetry and positive definiteness constraints of gain matrices are enforced by proposing a tracker for symmetric positive definite matrices. Simulation results are carried out on the humanoid robot iCub.

## 参考
- http://arxiv.org/abs/1610.02849v3

## Overview
This paper proposes a technique for automatic gain tuning of a momentum based balancing controller for humanoid robots. The controller ensures the stabilization of the centroidal dynamics and the associated zero dynamics. Then, the closed-loop, constrained joint space dynamics is linearized and the controller's gains are chosen so as to obtain desired properties of the linearized system. Symmetry and positive definiteness constraints of gain matrices are enforced by proposing a tracker for symmetric positive definite matrices. Simulation results are carried out on the humanoid robot iCub.

## Content
This paper proposes a technique for automatic gain tuning of a momentum based balancing controller for humanoid robots. The controller ensures the stabilization of the centroidal dynamics and the associated zero dynamics. Then, the closed-loop, constrained joint space dynamics is linearized and the controller's gains are chosen so as to obtain desired properties of the linearized system. Symmetry and positive definiteness constraints of gain matrices are enforced by proposing a tracker for symmetric positive definite matrices. Simulation results are carried out on the humanoid robot iCub.

## 개요
본 논문은 휴머노이드 로봇의 모멘텀 기반 균형 제어기를 위한 자동 이득 조정 기법을 제안합니다. 제어기는 중심 동역학(centroidal dynamics) 및 관련 영점 동역학(zero dynamics)의 안정화를 보장합니다. 그런 다음 폐루프 구속 조인트 공간 동역학을 선형화하고, 선형화된 시스템의 원하는 특성을 얻기 위해 제어기의 이득을 선택합니다. 대칭 및 양의 정부호 제약 조건을 갖는 이득 행렬은 대칭 양의 정부호 행렬 추적기를 제안하여 적용됩니다. 시뮬레이션 결과는 휴머노이드 로봇 iCub에서 수행되었습니다.

## 핵심 내용
본 논문은 휴머노이드 로봇의 모멘텀 기반 균형 제어기를 위한 자동 이득 조정 기법을 제안합니다. 제어기는 중심 동역학 및 관련 영점 동역학의 안정화를 보장합니다. 그런 다음 폐루프 구속 조인트 공간 동역학을 선형화하고, 선형화된 시스템의 원하는 특성을 얻기 위해 제어기의 이득을 선택합니다. 대칭 및 양의 정부호 제약 조건을 갖는 이득 행렬은 대칭 양의 정부호 행렬 추적기를 제안하여 적용됩니다. 시뮬레이션 결과는 휴머노이드 로봇 iCub에서 수행되었습니다.
