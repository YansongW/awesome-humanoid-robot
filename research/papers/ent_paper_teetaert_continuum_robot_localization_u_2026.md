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
  en: This paper presents a continuous-time factor-graph-based MAP estimation framework that fuses sparse distributed time-of-flight
    sensor measurements and gyroscope data with a robot shape prior to localize continuum robots in unstructured environments,
    achieving 2.5 cm positional and 7.2° rotational error on a 53 cm robot.
  zh: 本文提出了一种连续时间因子图最大后验估计框架，将稀疏分布式飞行时间传感器测量值、陀螺仪数据与机器人形状先验相融合，以在非结构化环境中实现连续体机器人定位，在53厘米长的机器人上达到了2.5厘米的位置误差和7.2°的旋转误差。
  ko: 본 논문은 비구조화 환경에서 연속체 로봇의 위치추정을 위해 희소 분산식 시간측정 센서 측정값과 자이로스코프 데이터를 로봇 형상 사전정보와 융합하는 연속시간 요인그래프 기반 MAP 추정 프레임워크를 제안하며,
    53cm 길이 로봇에서 위치 오차 2.5cm, 회전 오차 7.2°를 달성한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.07209v2.
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
## 概述
Localization and mapping of an environment are crucial tasks for any robot operating in unstructured environments. Time-of-flight (ToF) sensors (e.g.,~lidar) have proven useful in mobile robotics, where high-resolution sensors can be used for simultaneous localization and mapping. In soft and continuum robotics, however, these high-resolution sensors are too large for practical use. This, combined with the deformable nature of such robots, has resulted in continuum robot (CR) localization and mapping in unstructured environments being a largely untouched area. In this work, we present a localization technique for CRs that relies on small, low-resolution ToF sensors distributed along the length of the robot. By fusing measurement information with a robot shape prior, we show that accurate localization is possible despite each sensor experiencing frequent degenerate scenarios. We achieve an average localization error of 2.5cm in position and 7.2° in rotation across all experimental conditions with a 53cm long robot. We demonstrate that the results are repeated across multiple environments, in both simulation and real-world experiments, and study robustness in the estimation to deviations in the prior map.

## 核心内容
Localization and mapping of an environment are crucial tasks for any robot operating in unstructured environments. Time-of-flight (ToF) sensors (e.g.,~lidar) have proven useful in mobile robotics, where high-resolution sensors can be used for simultaneous localization and mapping. In soft and continuum robotics, however, these high-resolution sensors are too large for practical use. This, combined with the deformable nature of such robots, has resulted in continuum robot (CR) localization and mapping in unstructured environments being a largely untouched area. In this work, we present a localization technique for CRs that relies on small, low-resolution ToF sensors distributed along the length of the robot. By fusing measurement information with a robot shape prior, we show that accurate localization is possible despite each sensor experiencing frequent degenerate scenarios. We achieve an average localization error of 2.5cm in position and 7.2° in rotation across all experimental conditions with a 53cm long robot. We demonstrate that the results are repeated across multiple environments, in both simulation and real-world experiments, and study robustness in the estimation to deviations in the prior map.

## 参考
- http://arxiv.org/abs/2602.07209v2

