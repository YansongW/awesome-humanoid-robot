---
$id: ent_paper_ficht_centroidal_state_estimation_an_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Centroidal State Estimation and Control for Hardware-constrained Humanoid Robots
  zh: 面向硬件受限人形机器人的质心状态估计与控制
  ko: 하드웨어 제약이 있는 휴머노이드 로봇을 위한 중심 상태 추정 및 제어
summary:
  en: Introduces centroidal state estimation and control methods for humanoid robots
    with hardware limitations, combining a five-mass model with approximate limb dynamics
    to enable accurate CoM and CoP estimation and reactive stepping without force
    sensing.
  zh: 针对硬件受限的人形机器人，提出了一种结合五质量模型与近似肢体动力学的质心状态估计与控制方法，可在无力传感器的条件下实现准确的质心/压力中心估计与反应式步态平衡。
  ko: 하드웨어 제약이 있는 휴머노이드 로봇을 위해 5질량 모델과 근사된 사지 역학을 결합한 중심 상태 추정 및 제어 방법을 제안하여, 힘 센서
    없이도 정확한 질량 중심/압력 중심 추정과 반응형 보행 균형을 실현한다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- centroidal_state_estimation
- humanoid_balance_control
- push_recovery
- hardware_constrained_robots
- five_mass_model
- center_of_pressure
- capture_point
- nimbro_op2x
- robocup_2023
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review against
    the full paper before verification.
sources:
- id: src_001
  type: paper
  title: Centroidal State Estimation and Control for Hardware-constrained Humanoid
    Robots
  url: https://arxiv.org/abs/2312.11019
  date: '2023'
  accessed_at: '2026-06-26'
---

## Overview

This paper addresses the challenge of achieving robust bipedal balance on humanoid robots that lack high-end sensing and actuation hardware. The authors develop a centroidal state estimator based on a five-mass model augmented with approximate dynamics for each limb, which allows the robot's CoM, angular momentum, and Center of Pressure to be estimated without direct force or contact sensing. Building on these estimates, the paper presents a feedforward control scheme that compensates for poor joint tracking, control latency, and dynamic loading effects. Finally, feedback mechanisms—including a CoM-ZMP/CMP controller and tilt-compensating step feedback—are used to cope with the kinematic restrictions of the 18-DoF NimbRo-OP2X platform.

The methods are evaluated both in MuJoCo simulation and on the physical NimbRo-OP2X robot. Simulation comparisons are made against the Capture Steps framework, while hardware validation includes reactive stepping and push-recovery experiments conducted at RoboCup 2023 in Bordeaux, France. The work demonstrates that accurate centroidal estimation and control can significantly improve balance on low-cost, sensor-limited humanoids.

Key design choices are driven by the robot's specific constraints: it uses a double 4-bar linkage parallel leg mechanism with only 18 degrees of freedom, lacks force/torque sensors at the feet or ankles, and has limited joint tracking accuracy. The estimator relies instead on IMU and joint encoder data, making it suitable for platforms with minimal instrumentation.

## Key Contributions

- A five-mass centroidal state estimator that incorporates limb dynamics to improve CoM and inertia estimates without force sensors.
- A centroidal-state feedforward scheme that compensates for joint tracking inaccuracies, latency, and dynamic loading.
- Tilt-compensating step feedback for humanoids with kinematic restrictions such as locked foot pitch.
- Hardware validation on NimbRo-OP2X, including push-recovery trials at RoboCup 2023.

## Relevance to Humanoid Robotics

The paper is highly relevant to practical humanoid deployment because it shows that robust bipedal locomotion and push recovery can be achieved despite severe hardware constraints. By reducing dependence on expensive force/torque sensing and high-DoF actuation, the methods lower the cost and complexity barriers for building and controlling humanoid robots. The centroidal modeling and feedback techniques are also broadly applicable to other humanoid platforms with limited sensing or kinematic design trade-offs.
