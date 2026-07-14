---
$id: ent_paper_zhu_cycloidal_quasi_direct_drive_a_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Cycloidal Quasi-Direct Drive Actuator Designs with Learning-based Torque Estimation for Legged Robotics
  zh: 面向足式机器人的摆线准直驱执行器设计与基于学习的扭矩估计
  ko: 족운동 로봇을 위한 학습 기반 토크 추정이 적용된 사이클로이드 준직접구동 액추에이터 설계
summary:
  en: This paper designs a 10:1 cycloidal quasi-direct-drive actuator for legged robots and proposes a GRU-based Actuator
    Network that estimates nonlinear output torque from historical actuator states to reduce the sim-to-real gap caused by
    cycloidal-drive dynamics.
  zh: 本文设计了一种10:1减速比的摆线准直驱执行器用于足式机器人，并提出基于GRU的执行器网络，通过历史执行器状态估计非线性输出扭矩，以减小摆线传动动力学引起的仿真到现实差距。
  ko: 본 논문은 족운동 로봇을 위한 10:1 감속비의 사이클로이드 준직접구동 액추에이터를 설계하고, 과거 액추에이터 상태로부터 비선형 출력 토크를 추정하여 사이클로이드 구동 역학으로 인한 시뮬레이션-현실 간격을 줄이는
    GRU 기반 액추에이터 네트워크를 제안한다.
domains:
- 02_components
- 07_ai_models_algorithms
- 05_mass_production
layers:
- midstream
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- cycloidal_drive
- quasi_direct_drive
- actuator_design
- torque_estimation
- gru
- sim_to_real
- legged_robotics
- humanoid_actuator
- torque_ripple
- impact_resistant
- bldc_motor
- dynamic_locomotion
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.16591v2.
sources:
- id: src_001
  type: paper
  title: Cycloidal Quasi-Direct Drive Actuator Designs with Learning-based Torque Estimation for Legged Robotics
  url: https://arxiv.org/abs/2410.16591
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
This paper presents a novel approach through the design and implementation of Cycloidal Quasi-Direct Drive actuators for legged robotics. The cycloidal gear mechanism, with its inherent high torque density and mechanical robustness, offers significant advantages over conventional designs. By integrating cycloidal gears into the Quasi-Direct Drive framework, we aim to enhance the performance of legged robots, particularly in tasks demanding high torque and dynamic loads, while still keeping them lightweight. Additionally, we develop a torque estimation framework for the actuator using an Actuator Network, which effectively reduces the sim-to-real gap introduced by the cycloidal drive's complex dynamics. This integration is crucial for capturing the complex dynamics of a cycloidal drive, which contributes to improved learning efficiency, agility, and adaptability for reinforcement learning.

## 核心内容
This paper presents a novel approach through the design and implementation of Cycloidal Quasi-Direct Drive actuators for legged robotics. The cycloidal gear mechanism, with its inherent high torque density and mechanical robustness, offers significant advantages over conventional designs. By integrating cycloidal gears into the Quasi-Direct Drive framework, we aim to enhance the performance of legged robots, particularly in tasks demanding high torque and dynamic loads, while still keeping them lightweight. Additionally, we develop a torque estimation framework for the actuator using an Actuator Network, which effectively reduces the sim-to-real gap introduced by the cycloidal drive's complex dynamics. This integration is crucial for capturing the complex dynamics of a cycloidal drive, which contributes to improved learning efficiency, agility, and adaptability for reinforcement learning.

## 参考
- http://arxiv.org/abs/2410.16591v2

