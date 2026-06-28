---
$id: ent_paper_li_source_seeking_control_of_unic_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Source Seeking Control of Unicycle Robots with 3D-printed Flexible Piezoresistive
    Sensors
  zh: 基于3D打印柔性压阻传感器的独轮机器人源搜索控制
  ko: 3D 프린팅된 유연한 압저항 센서를 탑재한 유니사이클 로봇의 신호원 탐색 제어
summary:
  en: Presents projected gradient-ascent and extremum-seeking control laws for a unicycle
    robot using 3D-printed flexible graphene-based piezoresistive airflow sensors,
    with asymptotic convergence proofs and experimental validation.
  zh: 该论文针对装有3D打印柔性石墨烯压阻气流传感器的独轮机器人，提出并验证了投影梯度上升与极值搜索源搜索控制律，给出了渐近收敛证明与实验验证。
  ko: 3D 프린팅된 유연한 그래핀 기반 압저항 기류 센서가 장착된 유니사이클 로봇을 위해 투영 경사 상승법 및 극값 탐색 제어 법칙을 제안하고,
    점근적 수렴성을 증명하며 실험적으로 검증하였다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
- component
tags:
- source_seeking
- gradient_ascent
- extremum_seeking_control
- airflow_sensor
- piezoresistive_sensor
- flexible_electronics
- 3d_printed_sensor
- unicycle_robot
- mobile_robot
- gps_denied_navigation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text review is needed
    before final verification.
sources:
- id: src_001
  type: paper
  title: Source Seeking Control of Unicycle Robots with 3D-printed Flexible Piezoresistive
    Sensors
  url: https://arxiv.org/abs/2104.14267
  date: '2021'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

The paper develops source-seeking control algorithms for a unicycle mobile robot equipped with 3D-printed flexible graphene-based piezoresistive airflow sensors. It proposes a projected gradient-ascent control law that uses instantaneous local gradient measurements from the airflow sensors to command both the longitudinal and angular velocities of the robot. For cases of partial sensor failure, it combines Extremum-Seeking Control (ESC) with the projected gradient-ascent framework, relying only on flow-magnitude information. Both control laws are accompanied by asymptotic convergence proofs under assumptions on the local potential field.

The sensor subsystem is built around a soft polymeric cantilever body fabricated on a Formlabs Form 3 SLA 3D printer using flexible resin and a graphene-nanoplatelet dispersion. The resulting piezoresistive sensor is integrated into a Wheatstone bridge and read through a quad-channel analog differential input shield on an Arduino 328 controller. The robot platform is a Nexus mobile robot with 100mm Mecanum wheels driven by Faulhaber 12V motors with optical encoders; computation and communication use the Robot Operating System (ROS). Experimental validation uses an HBM 36-inch industrial drum fan as a stationary airflow source and a PCE-423 airflow meter for reference.

Simulations and onboard experiments demonstrate convergence toward the airflow source, including the partial sensor-failure scenario addressed by the ESC-based controller.

## Key Contributions

- Projected gradient-ascent control law using instantaneous local gradient for both longitudinal and angular robot velocities.
- ESC-based projected gradient-ascent control law for fault-tolerant source seeking under partial sensor failure.
- Asymptotic convergence proofs for both proposed control laws.
- Design, fabrication, and onboard integration of 3D-printed flexible graphene-based piezoresistive airflow sensors.
- Simulation and experimental validation on a unicycle mobile robot platform.

## Relevance to Humanoid Robotics

The source-seeking control framework and low-cost 3D-printed flexible airflow sensors can be adapted for humanoid robots to localize airflow or chemical sources in GPS-denied environments, supporting autonomous navigation and environmental interaction for mass-produced humanoid platforms. The sensor fabrication approach is compatible with body-conformable integration on humanoid limbs or torso, and the gradient-based navigation strategy could extend to odor, gas, or thermal source localization tasks relevant to service and inspection humanoids.
