---
$id: ent_paper_sorrentino_ukf_based_sensor_fusion_for_jo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: UKF-Based Sensor Fusion for Joint-Torque Sensorless Humanoid Robots
  zh: 基于无迹卡尔曼滤波的仿人机器人无关节力矩传感器力矩估计
  ko: UKF 기반 관절 토크 센서가 없는 휴머노이드 로봇을 위한 센서 융합
summary:
  en: Proposes an Unscented Kalman Filter-based sensor fusion method for online joint-torque
    estimation in humanoid robots that lack joint-torque sensors, and validates the
    approach experimentally on the ergoCub humanoid within a two-level torque-control
    architecture.
  zh: 提出一种基于无迹卡尔曼滤波的多传感器融合方法，用于无关节力矩传感器的仿人机器人在线关节力矩估计，并在ergoCub仿人机器人的双层力矩控制架构中进行了实验验证。
  ko: 관절 토크 센서가 없는 휴머노이드 로봇의 온라인 관절 토크 추정을 위한 무향 칼만 필터 기반 센서 융합법을 제안하고, ergoCub 휴머노이드의
    이중 토크 제어 아키텍처에서 실험적으로 검증한다.
domains:
- 08_software_middleware
- 02_components
- 05_mass_production
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- sensor_fusion
- unscented_kalman_filter
- joint_torque_estimation
- torque_control
- sensorless_humanoid
- floating_base_dynamics
- ergocub
- force_torque_sensors
- human_robot_interaction
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the provided metadata/abstract; requires human review against
    the full paper before final verification.
sources:
- id: src_001
  type: paper
  title: UKF-Based Sensor Fusion for Joint-Torque Sensorless Humanoid Robots
  url: https://arxiv.org/abs/2402.18380
  date: '2024'
  accessed_at: '2026-06-26'
---


## Overview

Humanoid robots designed for compliant physical interaction typically require accurate joint-torque feedback, yet many platforms do not include dedicated joint-torque sensors because of cost, packaging, or mechanical-complexity constraints. This paper presents an Unscented Kalman Filter (UKF) based sensor-fusion framework that estimates joint torques online without requiring torque sensors at every joint. The estimator treats the joint-torque estimation problem as a stochastic state-estimation task within a floating-base dynamics model.

At the feature level, the UKF fuses heterogeneous sensor streams—joint encoders, motor currents, force/torque sensors, accelerometers, and gyroscopes—while also accounting for non-directly measurable effects such as external contacts. The framework is intended to be flexible with respect to the available sensor suit: it can incorporate distributed, non-collocated force/torque sensors and does not require a fixed sensor layout. By representing process and measurement uncertainty explicitly, the method aims to produce joint-torque estimates that are directly usable in control architectures for human-robot interaction.

The authors integrate the proposed estimator into a two-level task-space torque-control architecture and evaluate it on the new ergoCub humanoid robot developed at Istituto Italiano di Tecnologia. Extensive tests are reported with the robot mounted on a pole, comparing the UKF approach against a deterministic baseline based on the recursive Newton-Euler algorithm. Reported root-mean-square torque-tracking errors range from 0.05 Nm to 2.5 Nm, even when external contacts are present.

## Key Contributions

- UKF-based stochastic sensor fusion for online joint-torque estimation without joint-torque sensors.
- Integration of distributed, non-collocated force/torque sensors and implicit estimation of external contacts.
- Fusion of heterogeneous measurements including motor currents, inertial sensors, and force/torque sensors.
- Experimental validation on the ergoCub humanoid robot within a two-level torque-control architecture.
- Empirical demonstration of lower torque-tracking errors than the deterministic recursive Newton-Euler approach.

## Relevance to Humanoid Robotics

The work provides a software-based route to torque-controlled behavior on humanoids that are not equipped with joint-torque sensors. Reducing reliance on dedicated torque sensors can lower hardware cost and mechanical complexity, which is relevant to scaling humanoid robots toward mass production and broader deployment. Accurate, sensorless torque estimation also supports safer and more compliant human-robot interaction by enabling force-sensitive control loops on platforms that would otherwise lack the required sensing.
