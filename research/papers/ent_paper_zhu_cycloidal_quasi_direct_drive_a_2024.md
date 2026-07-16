---
$id: ent_paper_zhu_cycloidal_quasi_direct_drive_a_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Cycloidal Quasi-Direct Drive Actuator Designs with Learning-based Torque Estimation for Legged Robotics
  zh: 面向足式机器人的摆线准直驱执行器设计与基于学习的扭矩估计
  ko: 족운동 로봇을 위한 사이클로이드 의사직구동 액추에이터 설계 및 학습 기반 토크 추정
summary:
  en: This paper presents a 10:1 Cycloidal Quasi-Direct Drive (C-QDD) actuator for legged robots and a GRU-based Actuator
    Network that estimates output torque from actuator state history to reduce the sim-to-real gap caused by cycloidal gear
    nonlinearities.
  zh: 本文提出了一种面向足式机器人的10:1摆线准直驱（C-QDD）执行器，以及一种基于门控循环单元（GRU）的执行器网络，该网络利用执行器状态历史估计输出扭矩，以减少摆线齿轮非线性引起的仿真到现实差距。
  ko: 이 논문은 족운동 로봇을 위한 10:1 사이클로이드 의사직구동(C-QDD) 액추에이터와, 사이클로이드 기어 비선형성으로 인한 시뮬레이션-현실 간격을 줄이기 위해 액추에이터 상태 이력으로부터 출력 토크를 추정하는
    GRU 기반 액추에이터 네트워크를 제시한다.
domains:
- 02_components
- 07_ai_models_algorithms
- 06_design_engineering
- 03_manufacturing_processes
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- component
- intelligence
tags:
- cycloidal_drive
- quasi_direct_drive
- cqdd
- actuator
- torque_estimation
- gru
- actuator_network
- legged_robotics
- sim_to_real
- proprioceptive_actuator
- high_torque_density
- impact_resilience
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.16591v2.
sources:
- id: src_001
  type: paper
  title: Cycloidal Quasi-Direct Drive Actuator Designs with Learning-based Torque Estimation for Legged Robotics
  url: https://arxiv.org/abs/2410.16591
  date: '2024'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
---
## 概述
This paper presents a novel approach through the design and implementation of Cycloidal Quasi-Direct Drive actuators for legged robotics. The cycloidal gear mechanism, with its inherent high torque density and mechanical robustness, offers significant advantages over conventional designs. By integrating cycloidal gears into the Quasi-Direct Drive framework, we aim to enhance the performance of legged robots, particularly in tasks demanding high torque and dynamic loads, while still keeping them lightweight. Additionally, we develop a torque estimation framework for the actuator using an Actuator Network, which effectively reduces the sim-to-real gap introduced by the cycloidal drive's complex dynamics. This integration is crucial for capturing the complex dynamics of a cycloidal drive, which contributes to improved learning efficiency, agility, and adaptability for reinforcement learning.

## 核心内容
This paper presents a novel approach through the design and implementation of Cycloidal Quasi-Direct Drive actuators for legged robotics. The cycloidal gear mechanism, with its inherent high torque density and mechanical robustness, offers significant advantages over conventional designs. By integrating cycloidal gears into the Quasi-Direct Drive framework, we aim to enhance the performance of legged robots, particularly in tasks demanding high torque and dynamic loads, while still keeping them lightweight. Additionally, we develop a torque estimation framework for the actuator using an Actuator Network, which effectively reduces the sim-to-real gap introduced by the cycloidal drive's complex dynamics. This integration is crucial for capturing the complex dynamics of a cycloidal drive, which contributes to improved learning efficiency, agility, and adaptability for reinforcement learning.

## 参考
- http://arxiv.org/abs/2410.16591v2

## Overview
This paper presents a novel approach through the design and implementation of Cycloidal Quasi-Direct Drive actuators for legged robotics. The cycloidal gear mechanism, with its inherent high torque density and mechanical robustness, offers significant advantages over conventional designs. By integrating cycloidal gears into the Quasi-Direct Drive framework, we aim to enhance the performance of legged robots, particularly in tasks demanding high torque and dynamic loads, while still keeping them lightweight. Additionally, we develop a torque estimation framework for the actuator using an Actuator Network, which effectively reduces the sim-to-real gap introduced by the cycloidal drive's complex dynamics. This integration is crucial for capturing the complex dynamics of a cycloidal drive, which contributes to improved learning efficiency, agility, and adaptability for reinforcement learning.

## Content
This paper presents a novel approach through the design and implementation of Cycloidal Quasi-Direct Drive actuators for legged robotics. The cycloidal gear mechanism, with its inherent high torque density and mechanical robustness, offers significant advantages over conventional designs. By integrating cycloidal gears into the Quasi-Direct Drive framework, we aim to enhance the performance of legged robots, particularly in tasks demanding high torque and dynamic loads, while still keeping them lightweight. Additionally, we develop a torque estimation framework for the actuator using an Actuator Network, which effectively reduces the sim-to-real gap introduced by the cycloidal drive's complex dynamics. This integration is crucial for capturing the complex dynamics of a cycloidal drive, which contributes to improved learning efficiency, agility, and adaptability for reinforcement learning.

## 개요
본 논문은 보행 로봇을 위한 사이클로이드 준직접 구동 액추에이터의 설계 및 구현을 통해 새로운 접근법을 제시합니다. 사이클로이드 기어 메커니즘은 본질적으로 높은 토크 밀도와 기계적 견고성을 갖추고 있어 기존 설계에 비해 상당한 이점을 제공합니다. 사이클로이드 기어를 준직접 구동 프레임워크에 통합함으로써, 높은 토크와 동적 하중이 요구되는 작업에서 보행 로봇의 성능을 향상시키면서도 경량성을 유지하는 것을 목표로 합니다. 또한, 액추에이터 네트워크를 사용하여 액추에이터의 토크 추정 프레임워크를 개발함으로써, 사이클로이드 구동의 복잡한 동역학으로 인해 발생하는 시뮬레이션-실제 간 격차를 효과적으로 줄입니다. 이러한 통합은 사이클로이드 구동의 복잡한 동역학을 포착하는 데 필수적이며, 이는 강화 학습의 학습 효율성, 민첩성 및 적응성 향상에 기여합니다.

## 핵심 내용
본 논문은 보행 로봇을 위한 사이클로이드 준직접 구동 액추에이터의 설계 및 구현을 통해 새로운 접근법을 제시합니다. 사이클로이드 기어 메커니즘은 본질적으로 높은 토크 밀도와 기계적 견고성을 갖추고 있어 기존 설계에 비해 상당한 이점을 제공합니다. 사이클로이드 기어를 준직접 구동 프레임워크에 통합함으로써, 높은 토크와 동적 하중이 요구되는 작업에서 보행 로봇의 성능을 향상시키면서도 경량성을 유지하는 것을 목표로 합니다. 또한, 액추에이터 네트워크를 사용하여 액추에이터의 토크 추정 프레임워크를 개발함으로써, 사이클로이드 구동의 복잡한 동역학으로 인해 발생하는 시뮬레이션-실제 간 격차를 효과적으로 줄입니다. 이러한 통합은 사이클로이드 구동의 복잡한 동역학을 포착하는 데 필수적이며, 이는 강화 학습의 학습 효율성, 민첩성 및 적응성 향상에 기여합니다.
