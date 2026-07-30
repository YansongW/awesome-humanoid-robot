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
  en: Proposes an Unscented Kalman Filter-based sensor fusion method for online joint-torque estimation in humanoid robots
    that lack joint-torque sensors, and validates the approach experimentally on the ergoCub humanoid within a two-level torque-control
    architecture.
  zh: 本文提出一种基于Unscented Kalman Filter的传感器融合方法，用于无关节扭矩传感器的人形机器人在线关节扭矩估计。该方法由Istituto Italiano di Tecnologia开发，在ergoCub人形机器人上通过两级扭矩控制架构实验验证，实现了0.05
    Nm至2.5 Nm的低均方根误差。
  ko: 관절 토크 센서가 없는 휴머노이드 로봇의 온라인 관절 토크 추정을 위한 무향 칼만 필터 기반 센서 융합법을 제안하고, ergoCub 휴머노이드의 이중 토크 제어 아키텍처에서 실험적으로 검증한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2402.18380v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: UKF-Based Sensor Fusion for Joint-Torque Sensorless Humanoid Robots
  url: https://arxiv.org/abs/2402.18380
  date: '2024'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
该研究针对缺乏关节扭矩传感器的人形机器人，提出基于Unscented Kalman Filter的传感器融合方法，实现关节扭矩的在线估计。方法融合多模态测量数据（如电流、加速度等），并考虑外部接触等不可直接测量的效应，生成可直接用于人机交互控制架构的关节扭矩。该框架具有灵活性，可集成分布式非共置力/扭矩传感器。在ergoCub人形机器人上的实验表明，该方法在扭矩跟踪中达到0.05 Nm至2.5 Nm的低均方根误差，优于基于递归牛顿-欧拉算法的现有方法。

## 核心内容
### 方法核心
- 基于Unscented Kalman Filter的传感器融合框架，融合多模态测量数据（电流、加速度等）
- 处理不可直接测量的效应（如外部接触），生成适用于控制架构的关节扭矩
- 可集成分布式非共置力/扭矩传感器，具有灵活框架特性

### 实验设置
- 在Istituto Italiano di Tecnologia开发的ergoCub人形机器人上进行验证
- 集成到两级扭矩控制架构中，实现任务空间扭矩控制
- 与基于递归牛顿-欧拉算法的现有方法进行对比

### 关键结果
- 扭矩跟踪均方根误差范围为0.05 Nm至2.5 Nm
- 在存在外部接触的情况下仍保持低误差
- 实验证明该方法在无关节扭矩传感器的人形机器人上有效

## Overview
This paper proposes a novel sensor fusion based on Unscented Kalman Filtering for the online estimation of joint-torques of humanoid robots without joint-torque sensors. At the feature level, the proposed approach considers multimodal measurements (e.g. currents, accelerations, etc.) and non-directly measurable effects, such as external contacts, thus leading to joint torques readily usable in control architectures for human-robot interaction. The proposed sensor fusion can also integrate distributed, non-collocated force/torque sensors, thus being a flexible framework with respect to the underlying robot sensor suit. To validate the approach, we show how the proposed sensor fusion can be integrated into a twolevel torque control architecture aiming at task-space torquecontrol. The performances of the proposed approach are shown through extensive tests on the new humanoid robot ergoCub, currently being developed at Istituto Italiano di Tecnologia. We also compare our strategy with the existing state-of-theart approach based on the recursive Newton-Euler algorithm. Results demonstrate that our method achieves low root mean square errors in torque tracking, ranging from 0.05 Nm to 2.5 Nm, even in the presence of external contacts.

## Overview
This paper proposes a novel sensor fusion based on Unscented Kalman Filtering for the online estimation of joint-torques of humanoid robots without joint-torque sensors. At the feature level, the proposed approach considers multimodal measurements (e.g. currents, accelerations, etc.) and non-directly measurable effects, such as external contacts, thus leading to joint torques readily usable in control architectures for human-robot interaction. The proposed sensor fusion can also integrate distributed, non-collocated force/torque sensors, thus being a flexible framework with respect to the underlying robot sensor suit. To validate the approach, we show how the proposed sensor fusion can be integrated into a two-level torque control architecture aiming at task-space torque control. The performances of the proposed approach are shown through extensive tests on the new humanoid robot ergoCub, currently being developed at Istituto Italiano di Tecnologia. We also compare our strategy with the existing state-of-the-art approach based on the recursive Newton-Euler algorithm. Results demonstrate that our method achieves low root mean square errors in torque tracking, ranging from 0.05 Nm to 2.5 Nm, even in the presence of external contacts.

## Content
This paper proposes a novel sensor fusion based on Unscented Kalman Filtering for the online estimation of joint-torques of humanoid robots without joint-torque sensors. At the feature level, the proposed approach considers multimodal measurements (e.g. currents, accelerations, etc.) and non-directly measurable effects, such as external contacts, thus leading to joint torques readily usable in control architectures for human-robot interaction. The proposed sensor fusion can also integrate distributed, non-collocated force/torque sensors, thus being a flexible framework with respect to the underlying robot sensor suit. To validate the approach, we show how the proposed sensor fusion can be integrated into a two-level torque control architecture aiming at task-space torque control. The performances of the proposed approach are shown through extensive tests on the new humanoid robot ergoCub, currently being developed at Istituto Italiano di Tecnologia. We also compare our strategy with the existing state-of-the-art approach based on the recursive Newton-Euler algorithm. Results demonstrate that our method achieves low root mean square errors in torque tracking, ranging from 0.05 Nm to 2.5 Nm, even in the presence of external contacts.

## 개요
본 논문은 조인트 토크 센서가 없는 휴머노이드 로봇의 조인트 토크 온라인 추정을 위해 Unscented Kalman Filtering 기반의 새로운 센서 융합을 제안합니다. 특징 수준에서 제안된 접근 방식은 다중 모드 측정(예: 전류, 가속도 등)과 외부 접촉과 같은 직접 측정 불가능한 효과를 고려하여, 인간-로봇 상호작용을 위한 제어 아키텍처에서 즉시 사용 가능한 조인트 토크를 도출합니다. 제안된 센서 융합은 분산된 비공동 배치 힘/토크 센서도 통합할 수 있어, 기본 로봇 센서 구성에 대해 유연한 프레임워크를 제공합니다. 접근 방식의 검증을 위해, 제안된 센서 융합이 작업 공간 토크 제어를 목표로 하는 2단계 토크 제어 아키텍처에 어떻게 통합될 수 있는지 보여줍니다. 제안된 접근 방식의 성능은 현재 Istituto Italiano di Tecnologia에서 개발 중인 새로운 휴머노이드 로봇 ergoCub에 대한 광범위한 테스트를 통해 입증됩니다. 또한 기존의 최첨단 접근 방식인 재귀적 Newton-Euler 알고리즘과 우리의 전략을 비교합니다. 결과는 외부 접촉이 있는 경우에도 우리의 방법이 0.05 Nm에서 2.5 Nm 범위의 낮은 평균 제곱근 오차로 토크 추적을 달성함을 보여줍니다.

## 핵심 내용
본 논문은 조인트 토크 센서가 없는 휴머노이드 로봇의 조인트 토크 온라인 추정을 위해 Unscented Kalman Filtering 기반의 새로운 센서 융합을 제안합니다. 특징 수준에서 제안된 접근 방식은 다중 모드 측정(예: 전류, 가속도 등)과 외부 접촉과 같은 직접 측정 불가능한 효과를 고려하여, 인간-로봇 상호작용을 위한 제어 아키텍처에서 즉시 사용 가능한 조인트 토크를 도출합니다. 제안된 센서 융합은 분산된 비공동 배치 힘/토크 센서도 통합할 수 있어, 기본 로봇 센서 구성에 대해 유연한 프레임워크를 제공합니다. 접근 방식의 검증을 위해, 제안된 센서 융합이 작업 공간 토크 제어를 목표로 하는 2단계 토크 제어 아키텍처에 어떻게 통합될 수 있는지 보여줍니다. 제안된 접근 방식의 성능은 현재 Istituto Italiano di Tecnologia에서 개발 중인 새로운 휴머노이드 로봇 ergoCub에 대한 광범위한 테스트를 통해 입증됩니다. 또한 기존의 최첨단 접근 방식인 재귀적 Newton-Euler 알고리즘과 우리의 전략을 비교합니다. 결과는 외부 접촉이 있는 경우에도 우리의 방법이 0.05 Nm에서 2.5 Nm 범위의 낮은 평균 제곱근 오차로 토크 추적을 달성함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2402.18380v1
