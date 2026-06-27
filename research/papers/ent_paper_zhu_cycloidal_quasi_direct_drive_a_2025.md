---
$id: ent_paper_zhu_cycloidal_quasi_direct_drive_a_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Cycloidal Quasi-Direct Drive Actuator Designs with Learning-based Torque Estimation
    for Legged Robotics
  zh: 面向足式机器人的摆线准直驱执行器设计与基于学习的扭矩估计
  ko: 족운동 로봇을 위한 학습 기반 토크 추정이 적용된 사이클로이드 준직접구동 액추에이터 설계
summary:
  en: This paper designs a 10:1 cycloidal quasi-direct-drive actuator for legged robots
    and proposes a GRU-based Actuator Network that estimates nonlinear output torque
    from historical actuator states to reduce the sim-to-real gap caused by cycloidal-drive
    dynamics.
  zh: 本文设计了一种10:1减速比的摆线准直驱执行器用于足式机器人，并提出基于GRU的执行器网络，通过历史执行器状态估计非线性输出扭矩，以减小摆线传动动力学引起的仿真到现实差距。
  ko: 본 논문은 족운동 로봇을 위한 10:1 감속비의 사이클로이드 준직접구동 액추에이터를 설계하고, 과거 액추에이터 상태로부터 비선형 출력 토크를
    추정하여 사이클로이드 구동 역학으로 인한 시뮬레이션-현실 간격을 줄이는 GRU 기반 액추에이터 네트워크를 제안한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review against
    the full paper before verification.
sources:
- id: src_001
  type: paper
  title: Cycloidal Quasi-Direct Drive Actuator Designs with Learning-based Torque
    Estimation for Legged Robotics
  url: https://arxiv.org/abs/2410.16591
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Cycloidal gears offer high torque density and mechanical robustness, making them attractive for legged robots that must handle high dynamic loads while remaining lightweight. This paper integrates a cycloidal reduction stage into the Quasi-Direct Drive framework to create a Cycloidal Quasi-Direct Drive (C-QDD) actuator. The design targets a 10:1 gear ratio using 4140 alloy steel cycloid disks and rings, 18-8 stainless steel output pins, a counterbalancing disk, a BLDC motor, and a CubeMars driver board. The authors argue that the resulting actuator preserves the high bandwidth and low backlash desirable for dynamic locomotion while improving impact tolerance and torque density.

A central challenge is that cycloidal drives introduce nonlinear torque-output dynamics, including torque ripple and oscillations, which are difficult to model accurately in simulation and therefore widen the sim-to-real gap for reinforcement learning. To address this, the authors develop a torque estimation framework based on a Gated Recurrent Unit (GRU) Actuator Network. The network takes historical actuator states as input and predicts the actuator's output torque, capturing high-frequency ripple and other unmodeled effects. The paper compares two input configurations: PV-GRU, which uses position and velocity histories, and PVA-GRU, which additionally includes acceleration.

The proposed actuator and estimator are validated on hardware. The prototype achieves a peak torque of 89.9 Nm, and the torque estimator is evaluated against measured output torque to verify its accuracy. The authors report static and dynamic back-driving torques of 1.99 Nm and 1.36 Nm, respectively, and note that the peak torque is below the 120 Nm BLDC-limited design target because of the driver board current limit.

## Key Contributions

- Design of a Cycloidal Quasi-Direct Drive actuator tailored for dynamic locomotion and climbing.
- GRU-based torque estimation framework that predicts nonlinear, high-frequency torque ripple.
- Hardware verification of actuator performance and torque estimation accuracy.

## Relevance to Humanoid Robotics

The high torque density and impact resistance of the C-QDD actuator are directly applicable to leg actuation in humanoid robots, where joints must deliver large torques during walking, running, and falling while keeping mass low. Accurate torque estimation is equally important for humanoid control because reinforcement-learning policies trained in simulation depend on faithful actuator models to transfer to real hardware. By learning the unmodeled cycloidal dynamics from data, the GRU-based estimator can help close the sim-to-real gap for humanoid leg controllers.

The authors explicitly frame the work as relevant to mass production and deployment, noting that reliable actuators and sim-to-real policy transfer are critical for scaling humanoid robots. Although the prototype does not yet reach its 120 Nm target and exhibits higher back-driving torque than some comparable QDD actuators, the combination of a robust cycloidal transmission with a data-driven torque model provides a plausible pathway for next-generation humanoid leg hardware.
