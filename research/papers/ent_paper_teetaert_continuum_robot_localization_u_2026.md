---
$id: ent_paper_teetaert_continuum_robot_localization_u_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Continuum Robot Localization using Distributed Time-of-Flight Sensors
  zh: 基于分布式飞行时间传感器的连续体机器人定位
  ko: 분산식 시간측정 센서를 활용한 연속체 로봇 위치추정
summary:
  en: This paper presents a continuous-time factor-graph-based MAP estimation framework
    that fuses sparse distributed time-of-flight sensor measurements and gyroscope
    data with a robot shape prior to localize continuum robots in unstructured environments,
    achieving 2.5 cm positional and 7.2° rotational error on a 53 cm robot.
  zh: 本文提出了一种连续时间因子图最大后验估计框架，将稀疏分布式飞行时间传感器测量值、陀螺仪数据与机器人形状先验相融合，以在非结构化环境中实现连续体机器人定位，在53厘米长的机器人上达到了2.5厘米的位置误差和7.2°的旋转误差。
  ko: 본 논문은 비구조화 환경에서 연속체 로봇의 위치추정을 위해 희소 분산식 시간측정 센서 측정값과 자이로스코프 데이터를 로봇 형상 사전정보와
    융합하는 연속시간 요인그래프 기반 MAP 추정 프레임워크를 제안하며, 53cm 길이 로봇에서 위치 오차 2.5cm, 회전 오차 7.2°를 달성한다.
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
- continuum_robot
- time_of_flight
- localization
- state_estimation
- factor_graph
- soft_robotics
- distributed_sensing
- sensor_fusion
- shape_prior
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text verification
    not performed.
sources:
- id: src_001
  type: paper
  title: Continuum Robot Localization using Distributed Time-of-Flight Sensors
  url: https://arxiv.org/abs/2602.07209
  date: '2026'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

Continuum robot (CR) localization and mapping in unstructured environments has remained largely unexplored because conventional high-resolution time-of-flight sensors are too large and heavy for soft, deformable robots, while small, low-resolution onboard sensors frequently produce geometrically degenerate measurements. This work addresses the problem by distributing multiple small time-of-flight sensors along the length of a continuum robot and fusing their sparse range readings with a robot shape prior within a continuous-time factor-graph-based maximum a posteriori (MAP) estimation framework. The estimator also incorporates gyroscope data to constrain orientation, enabling accurate localization despite individual sensors encountering frequent degenerate scenarios such as limited field of view or featureless surfaces.

The authors validate the approach across simulation and real-world experiments using a 53 cm long soft, extensible continuum robot equipped with VL53L5CX ToF sensors and an ISM330BX IMU. The reported average localization error is 2.5 cm in position and 7.2° in rotation across all experimental conditions. The experiments cover multiple cluttered environments and include robustness studies in which the prior map is intentionally perturbed or partially mismatched to evaluate estimation sensitivity.

## Key Contributions

- A continuous-time, factor-graph-based MAP estimation framework that integrates sparse distributed ToF measurements with a robot shape prior for continuum robot localization.
- The first real-world demonstration of onboard-only localization of a soft, extensible continuum robot in cluttered environments using distributed low-resolution ToF and inertial sensing.
- Validation across simulated and physical platforms, including robustness studies with partial prior-map mismatch and multiple environments.

## Relevance to Humanoid Robotics

Although the paper focuses on continuum robots rather than rigid humanoids, its core techniques are transferable to future humanoid systems that incorporate soft or flexible actuators, limbs, or manipulators. Distributed, low-cost ToF sensing combined with continuous-time state estimation and shape-prior fusion offers a template for localizing and estimating the shape of deformable substructures within a humanoid robot. As humanoid designs increasingly adopt compliant materials and continuum-style appendages for safe interaction, methods like this one may inform perception, localization, and body-state estimation subsystems.
