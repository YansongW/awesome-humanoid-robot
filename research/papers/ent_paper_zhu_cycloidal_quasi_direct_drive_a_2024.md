---
$id: ent_paper_zhu_cycloidal_quasi_direct_drive_a_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Cycloidal Quasi-Direct Drive Actuator Designs with Learning-based Torque Estimation
    for Legged Robotics
  zh: 面向足式机器人的摆线准直驱执行器设计与基于学习的扭矩估计
  ko: 족운동 로봇을 위한 사이클로이드 의사직구동 액추에이터 설계 및 학습 기반 토크 추정
summary:
  en: This paper presents a 10:1 Cycloidal Quasi-Direct Drive (C-QDD) actuator for
    legged robots and a GRU-based Actuator Network that estimates output torque from
    actuator state history to reduce the sim-to-real gap caused by cycloidal gear
    nonlinearities.
  zh: 本文提出了一种面向足式机器人的10:1摆线准直驱（C-QDD）执行器，以及一种基于门控循环单元（GRU）的执行器网络，该网络利用执行器状态历史估计输出扭矩，以减少摆线齿轮非线性引起的仿真到现实差距。
  ko: 이 논문은 족운동 로봇을 위한 10:1 사이클로이드 의사직구동(C-QDD) 액추에이터와, 사이클로이드 기어 비선형성으로 인한 시뮬레이션-현실
    간격을 줄이기 위해 액추에이터 상태 이력으로부터 출력 토크를 추정하는 GRU 기반 액추에이터 네트워크를 제시한다.
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
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full paper text not independently
    reviewed. Requires human review before final verification.
sources:
- id: src_001
  type: paper
  title: Cycloidal Quasi-Direct Drive Actuator Designs with Learning-based Torque
    Estimation for Legged Robotics
  url: https://arxiv.org/abs/2410.16591
  date: '2024'
  accessed_at: '2026-06-25'
---


## Overview

This paper presents the design, fabrication, and experimental validation of a Cycloidal Quasi-Direct Drive (C-QDD) actuator intended for dynamic legged locomotion and climbing. The actuator integrates a brushless DC motor with a 10:1 single-stage cycloidal gearbox to achieve high torque density and mechanical robustness while maintaining a lightweight form factor. Key fabricated components include a cycloidal disk and a non-pinwheel outer cycloid ring made from 4140 alloy steel, plus output pins/precision shoulder screws made from 18-8 stainless steel. A CubeMars Driver Board-V2.1 is used for motor control.

To address the complex nonlinear dynamics introduced by the cycloidal drive—such as torque ripple and backlash—the authors develop a learning-based torque estimation framework using a Gated Recurrent Unit (GRU) Actuator Network. Two variants are evaluated: PV-GRU, which uses position and velocity history, and PVA-GRU, which additionally incorporates acceleration measurements. The network learns to predict output torque from actuator state history, thereby reducing the sim-to-real gap for reinforcement learning control of legged systems.

The paper reports experimental hardware characterization covering mechanical, electrical, backlash, backdrivability, and torque-estimation performance. Results include a measured peak torque of 89.9 Nm, which fell short of the 120 Nm target due to current limits on the CubeMars driver board, and verification that the learned estimator captures high-frequency torque ripple better than analytical baselines.

## Key Contributions

- Design of a compact 10:1 Cycloidal Quasi-Direct Drive actuator suitable for dynamic legged locomotion and climbing.
- Development of a GRU-based Actuator Network (PV-GRU / PVA-GRU) that estimates output torque from actuator state history and captures nonlinear high-frequency effects such as torque ripple.
- Experimental hardware verification of mechanical, electrical, backlash, backdrivability, and torque-estimation performance.

## Relevance to Humanoid Robotics

Humanoid robots require compact, high-torque-density, and impact-resilient joint actuators that can accurately report or estimate joint torque for dynamic balance and whole-body control. The C-QDD actuator directly addresses these requirements by combining cycloidal gearing's high torque density and mechanical robustness with a proprioceptive, learning-based torque model. Its lightweight form factor and backdrivability make it suitable for the hip, knee, and ankle joints of scalable dynamic humanoids.

The GRU-based torque estimator further narrows the sim-to-real gap, enabling more sample-efficient reinforcement learning for locomotion and manipulation behaviors on physical humanoid platforms. By capturing complex cycloidal-drive dynamics such as torque ripple, the approach supports more agile and adaptive control policies that transfer reliably from simulation to hardware.
