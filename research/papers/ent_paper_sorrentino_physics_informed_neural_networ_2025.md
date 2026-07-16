---
$id: ent_paper_sorrentino_physics_informed_neural_networ_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Physics-Informed Neural Networks with Unscented Kalman Filter for Sensorless Joint Torque Estimation in Humanoid Robots
  zh: 基于物理信息神经网络与无迹卡尔曼滤波的人形机器人无传感器关节力矩估计
  ko: 물리 정보 신경망과 무향 칼만 필터를 활용한 휴로이드 로봇의 무센서 관절 토크 추정
summary:
  en: This paper proposes a real-time sensorless whole-body torque control framework for humanoid robots with electric motors
    and harmonic drives, combining PINNs for nonlinear friction modeling and a floating-base UKF that uses PINN friction estimates
    as direct measurements; experiments on ergoCub show improved torque tracking, energy efficiency, and disturbance rejection
    compared to RNEA and position control.
  zh: 本文面向配备电机与谐波减速器的人形机器人，提出了一种实时无传感器全身力矩控制框架，结合物理信息神经网络（PINN）进行非线性摩擦建模，并将PINN摩擦估计作为直接测量输入无迹卡尔曼滤波器（UKF）；ergoCub机器人实验表明，相较于递归牛顿-欧拉算法（RNEA）和位置控制，该方法在力矩跟踪精度、能效和抗扰动性方面均有提升。
  ko: 본 논문은 전기 모터와 하모닉 드라이브를 갖춘 휴로이드 로봇을 위한 실시간 무센서 전신 토크 제어 프레임워크를 제안한다. 비선형 마찰 모델링을 위한 물리 정보 신경망(PINN)과 PINN 마찰 추정치를 직접
    측정값으로 활용하는 무향 칼만 필터(UKF)를 결합하였으며, ergoCub 로봇 실험에서 RNEA 및 위치 제어 대비 토크 추적 정확도, 에너지 효율, 외란 거부 성능이 향상되었음을 보였다.
domains:
- 07_ai_models_algorithms
- 02_components
- 05_mass_production
- 08_software_middleware
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- physics_informed_neural_networks
- unscented_kalman_filter
- sensorless_torque_control
- whole_body_torque_control
- friction_modeling
- harmonic_drive
- ergocub
- humanoid_robot
- real_time_control
- recursive_newton_euler
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.10105v1.
sources:
- id: src_001
  type: paper
  title: Physics-Informed Neural Networks with Unscented Kalman Filter for Sensorless Joint Torque Estimation in Humanoid
    Robots
  url: https://arxiv.org/abs/2507.10105
  date: '2025'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_component_harmonic_drive_reducer
  relationship: integrates
  description:
    en: The framework is designed for systems with electric motors and high-ratio harmonic drives.
    zh: 该框架面向配备电机和高减速比谐波减速器的系统而设计。
    ko: 해당 프레임워크는 전기 모터와 고감속비 하모닉 드라이브를 갖춘 시스템을 대상으로 설계되었다.
theoretical_depth:
- system
---
## 概述
This paper presents a novel framework for whole-body torque control of humanoid robots without joint torque sensors, designed for systems with electric motors and high-ratio harmonic drives. The approach integrates Physics-Informed Neural Networks (PINNs) for friction modeling and Unscented Kalman Filtering (UKF) for joint torque estimation, within a real-time torque control architecture. PINNs estimate nonlinear static and dynamic friction from joint and motor velocity readings, capturing effects like motor actuation without joint movement. The UKF utilizes PINN-based friction estimates as direct measurement inputs, improving torque estimation robustness. Experimental validation on the ergoCub humanoid robot demonstrates improved torque tracking accuracy, enhanced energy efficiency, and superior disturbance rejection compared to the state-of-the-art Recursive Newton-Euler Algorithm (RNEA), using a dynamic balancing experiment. The framework's scalability is shown by consistent performance across robots with similar hardware but different friction characteristics, without re-identification. Furthermore, a comparative analysis with position control highlights the advantages of the proposed torque control approach. The results establish the method as a scalable and practical solution for sensorless torque control in humanoid robots, ensuring torque tracking, adaptability, and stability in dynamic environments.

## 核心内容
This paper presents a novel framework for whole-body torque control of humanoid robots without joint torque sensors, designed for systems with electric motors and high-ratio harmonic drives. The approach integrates Physics-Informed Neural Networks (PINNs) for friction modeling and Unscented Kalman Filtering (UKF) for joint torque estimation, within a real-time torque control architecture. PINNs estimate nonlinear static and dynamic friction from joint and motor velocity readings, capturing effects like motor actuation without joint movement. The UKF utilizes PINN-based friction estimates as direct measurement inputs, improving torque estimation robustness. Experimental validation on the ergoCub humanoid robot demonstrates improved torque tracking accuracy, enhanced energy efficiency, and superior disturbance rejection compared to the state-of-the-art Recursive Newton-Euler Algorithm (RNEA), using a dynamic balancing experiment. The framework's scalability is shown by consistent performance across robots with similar hardware but different friction characteristics, without re-identification. Furthermore, a comparative analysis with position control highlights the advantages of the proposed torque control approach. The results establish the method as a scalable and practical solution for sensorless torque control in humanoid robots, ensuring torque tracking, adaptability, and stability in dynamic environments.

## 参考
- http://arxiv.org/abs/2507.10105v1

## Overview
This paper presents a novel framework for whole-body torque control of humanoid robots without joint torque sensors, designed for systems with electric motors and high-ratio harmonic drives. The approach integrates Physics-Informed Neural Networks (PINNs) for friction modeling and Unscented Kalman Filtering (UKF) for joint torque estimation, within a real-time torque control architecture. PINNs estimate nonlinear static and dynamic friction from joint and motor velocity readings, capturing effects like motor actuation without joint movement. The UKF utilizes PINN-based friction estimates as direct measurement inputs, improving torque estimation robustness. Experimental validation on the ergoCub humanoid robot demonstrates improved torque tracking accuracy, enhanced energy efficiency, and superior disturbance rejection compared to the state-of-the-art Recursive Newton-Euler Algorithm (RNEA), using a dynamic balancing experiment. The framework's scalability is shown by consistent performance across robots with similar hardware but different friction characteristics, without re-identification. Furthermore, a comparative analysis with position control highlights the advantages of the proposed torque control approach. The results establish the method as a scalable and practical solution for sensorless torque control in humanoid robots, ensuring torque tracking, adaptability, and stability in dynamic environments.

## Content
This paper presents a novel framework for whole-body torque control of humanoid robots without joint torque sensors, designed for systems with electric motors and high-ratio harmonic drives. The approach integrates Physics-Informed Neural Networks (PINNs) for friction modeling and Unscented Kalman Filtering (UKF) for joint torque estimation, within a real-time torque control architecture. PINNs estimate nonlinear static and dynamic friction from joint and motor velocity readings, capturing effects like motor actuation without joint movement. The UKF utilizes PINN-based friction estimates as direct measurement inputs, improving torque estimation robustness. Experimental validation on the ergoCub humanoid robot demonstrates improved torque tracking accuracy, enhanced energy efficiency, and superior disturbance rejection compared to the state-of-the-art Recursive Newton-Euler Algorithm (RNEA), using a dynamic balancing experiment. The framework's scalability is shown by consistent performance across robots with similar hardware but different friction characteristics, without re-identification. Furthermore, a comparative analysis with position control highlights the advantages of the proposed torque control approach. The results establish the method as a scalable and practical solution for sensorless torque control in humanoid robots, ensuring torque tracking, adaptability, and stability in dynamic environments.

## 개요
본 논문은 관절 토크 센서가 없는 휴머노이드 로봇의 전신 토크 제어를 위한 새로운 프레임워크를 제시하며, 전기 모터와 고비율 하모닉 드라이브를 갖춘 시스템을 위해 설계되었습니다. 이 접근법은 물리 정보 신경망(PINN)을 마찰 모델링에, 무향 칼만 필터(UKF)를 관절 토크 추정에 통합하여 실시간 토크 제어 아키텍처 내에서 작동합니다. PINN은 관절 및 모터 속도 판독값으로부터 비선형 정적 및 동적 마찰을 추정하여, 관절 움직임 없이 모터 작동과 같은 효과를 포착합니다. UKF는 PINN 기반 마찰 추정치를 직접 측정 입력으로 활용하여 토크 추정의 견고성을 향상시킵니다. ergoCub 휴머노이드 로봇에 대한 실험적 검증은 동적 균형 실험을 통해 최신 기술인 재귀 뉴턴-오일러 알고리즘(RNEA)과 비교하여 향상된 토크 추적 정확도, 향상된 에너지 효율성, 그리고 우수한 외란 제거 성능을 입증했습니다. 프레임워크의 확장성은 유사한 하드웨어를 가지지만 마찰 특성이 다른 로봇들에서 재식별 없이 일관된 성능을 보여줌으로써 입증되었습니다. 또한, 위치 제어와의 비교 분석을 통해 제안된 토크 제어 접근법의 장점이 강조되었습니다. 결과는 이 방법이 휴머노이드 로봇의 센서리스 토크 제어를 위한 확장 가능하고 실용적인 솔루션임을 확립하며, 동적 환경에서 토크 추적, 적응성 및 안정성을 보장합니다.

## 핵심 내용
본 논문은 관절 토크 센서가 없는 휴머노이드 로봇의 전신 토크 제어를 위한 새로운 프레임워크를 제시하며, 전기 모터와 고비율 하모닉 드라이브를 갖춘 시스템을 위해 설계되었습니다. 이 접근법은 물리 정보 신경망(PINN)을 마찰 모델링에, 무향 칼만 필터(UKF)를 관절 토크 추정에 통합하여 실시간 토크 제어 아키텍처 내에서 작동합니다. PINN은 관절 및 모터 속도 판독값으로부터 비선형 정적 및 동적 마찰을 추정하여, 관절 움직임 없이 모터 작동과 같은 효과를 포착합니다. UKF는 PINN 기반 마찰 추정치를 직접 측정 입력으로 활용하여 토크 추정의 견고성을 향상시킵니다. ergoCub 휴머노이드 로봇에 대한 실험적 검증은 동적 균형 실험을 통해 최신 기술인 재귀 뉴턴-오일러 알고리즘(RNEA)과 비교하여 향상된 토크 추적 정확도, 향상된 에너지 효율성, 그리고 우수한 외란 제거 성능을 입증했습니다. 프레임워크의 확장성은 유사한 하드웨어를 가지지만 마찰 특성이 다른 로봇들에서 재식별 없이 일관된 성능을 보여줌으로써 입증되었습니다. 또한, 위치 제어와의 비교 분석을 통해 제안된 토크 제어 접근법의 장점이 강조되었습니다. 결과는 이 방법이 휴머노이드 로봇의 센서리스 토크 제어를 위한 확장 가능하고 실용적인 솔루션임을 확립하며, 동적 환경에서 토크 추적, 적응성 및 안정성을 보장합니다.
