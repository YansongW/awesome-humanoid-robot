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

## Overview
Localization and mapping of an environment are crucial tasks for any robot operating in unstructured environments. Time-of-flight (ToF) sensors (e.g., lidar) have proven useful in mobile robotics, where high-resolution sensors can be used for simultaneous localization and mapping. In soft and continuum robotics, however, these high-resolution sensors are too large for practical use. This, combined with the deformable nature of such robots, has resulted in continuum robot (CR) localization and mapping in unstructured environments being a largely untouched area. In this work, we present a localization technique for CRs that relies on small, low-resolution ToF sensors distributed along the length of the robot. By fusing measurement information with a robot shape prior, we show that accurate localization is possible despite each sensor experiencing frequent degenerate scenarios. We achieve an average localization error of 2.5cm in position and 7.2° in rotation across all experimental conditions with a 53cm long robot. We demonstrate that the results are repeated across multiple environments, in both simulation and real-world experiments, and study robustness in the estimation to deviations in the prior map.

## Content
Localization and mapping of an environment are crucial tasks for any robot operating in unstructured environments. Time-of-flight (ToF) sensors (e.g., lidar) have proven useful in mobile robotics, where high-resolution sensors can be used for simultaneous localization and mapping. In soft and continuum robotics, however, these high-resolution sensors are too large for practical use. This, combined with the deformable nature of such robots, has resulted in continuum robot (CR) localization and mapping in unstructured environments being a largely untouched area. In this work, we present a localization technique for CRs that relies on small, low-resolution ToF sensors distributed along the length of the robot. By fusing measurement information with a robot shape prior, we show that accurate localization is possible despite each sensor experiencing frequent degenerate scenarios. We achieve an average localization error of 2.5cm in position and 7.2° in rotation across all experimental conditions with a 53cm long robot. We demonstrate that the results are repeated across multiple environments, in both simulation and real-world experiments, and study robustness in the estimation to deviations in the prior map.

## 개요
비정형 환경에서 작동하는 모든 로봇에게 환경의 위치 추정 및 매핑은 핵심적인 작업입니다. ToF(Time-of-Flight) 센서(예: 라이다)는 고해상도 센서를 사용하여 동시적 위치 추정 및 매핑이 가능한 모바일 로봇 분야에서 유용함이 입증되었습니다. 그러나 소프트 로봇 및 연속체 로봇 분야에서는 이러한 고해상도 센서가 실용적으로 사용되기에는 너무 큽니다. 여기에 로봇의 변형 가능한 특성이 더해져, 비정형 환경에서 연속체 로봇(CR)의 위치 추정 및 매핑은 거의 연구되지 않은 분야로 남아 있습니다. 본 연구에서는 로봇 길이를 따라 분포된 소형 저해상도 ToF 센서에 의존하는 CR용 위치 추정 기술을 제시합니다. 측정 정보를 로봇 형상 사전 정보와 융합함으로써, 각 센서가 빈번한 퇴화 시나리오를 겪음에도 불구하고 정확한 위치 추정이 가능함을 보여줍니다. 길이 53cm 로봇을 사용한 모든 실험 조건에서 평균 위치 오차 2.5cm, 회전 오차 7.2°를 달성했습니다. 시뮬레이션과 실제 실험 모두에서 여러 환경에 걸쳐 결과가 반복됨을 입증하고, 사전 맵의 편차에 대한 추정의 강건성을 연구합니다.

## 핵심 내용
비정형 환경에서 작동하는 모든 로봇에게 환경의 위치 추정 및 매핑은 핵심적인 작업입니다. ToF(Time-of-Flight) 센서(예: 라이다)는 고해상도 센서를 사용하여 동시적 위치 추정 및 매핑이 가능한 모바일 로봇 분야에서 유용함이 입증되었습니다. 그러나 소프트 로봇 및 연속체 로봇 분야에서는 이러한 고해상도 센서가 실용적으로 사용되기에는 너무 큽니다. 여기에 로봇의 변형 가능한 특성이 더해져, 비정형 환경에서 연속체 로봇(CR)의 위치 추정 및 매핑은 거의 연구되지 않은 분야로 남아 있습니다. 본 연구에서는 로봇 길이를 따라 분포된 소형 저해상도 ToF 센서에 의존하는 CR용 위치 추정 기술을 제시합니다. 측정 정보를 로봇 형상 사전 정보와 융합함으로써, 각 센서가 빈번한 퇴화 시나리오를 겪음에도 불구하고 정확한 위치 추정이 가능함을 보여줍니다. 길이 53cm 로봇을 사용한 모든 실험 조건에서 평균 위치 오차 2.5cm, 회전 오차 7.2°를 달성했습니다. 시뮬레이션과 실제 실험 모두에서 여러 환경에 걸쳐 결과가 반복됨을 입증하고, 사전 맵의 편차에 대한 추정의 강건성을 연구합니다.
