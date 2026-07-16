---
$id: ent_paper_physics_informed_neural_networ_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Physics-Informed Neural Networks with Unscented Kalman Filter for Sensorless Joint Torque Estimation
  zh: Physics-Informed Neural Networks with Unscented Kalman Filter for Sensorless Joint Torque Estimation
  ko: Physics-Informed Neural Networks with Unscented Kalman Filter for Sensorless Joint Torque Estimation
summary:
  en: Physics-Informed Neural Networks with Unscented Kalman Filter for Sensorless Joint Torque Estimation is a 2025 work
    on state estimation for humanoid robots.
  zh: Physics-Informed Neural Networks with Unscented Kalman Filter for Sensorless Joint Torque Estimation is a 2025 work
    on state estimation for humanoid robots.
  ko: Physics-Informed Neural Networks with Unscented Kalman Filter for Sensorless Joint Torque Estimation is a 2025 work
    on state estimation for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- physics_informed_neural_networ
- slam
- state_estimation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.10105v1.
sources:
- id: src_001
  type: paper
  title: Physics-Informed Neural Networks with Unscented Kalman Filter for Sensorless Joint Torque Estimation (arXiv)
  url: https://arxiv.org/abs/2507.10105
  date: '2025'
  accessed_at: '2026-07-01'
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
본 논문은 전기 모터와 고비율 하모닉 드라이브를 갖춘 시스템을 위해 설계된, 관절 토크 센서가 없는 휴머노이드 로봇의 전신 토크 제어를 위한 새로운 프레임워크를 제시합니다. 이 접근법은 물리 정보 신경망(PINN)을 마찰 모델링에, 무향 칼만 필터(UKF)를 관절 토크 추정에 통합하며, 실시간 토크 제어 아키텍처 내에서 작동합니다. PINN은 관절 및 모터 속도 판독값으로부터 비선형 정적 및 동적 마찰을 추정하여, 관절 움직임 없이 모터 작동과 같은 효과를 포착합니다. UKF는 PINN 기반 마찰 추정치를 직접 측정 입력으로 활용하여 토크 추정의 강건성을 향상시킵니다. ergoCub 휴머노이드 로봇에 대한 실험적 검증은 동적 균형 실험을 통해 최신 기술인 재귀 뉴턴-오일러 알고리즘(RNEA)과 비교하여 향상된 토크 추적 정확도, 향상된 에너지 효율성, 그리고 우수한 외란 제거 성능을 입증했습니다. 프레임워크의 확장성은 유사한 하드웨어를 가지지만 마찰 특성이 다른 로봇들에서 재식별 없이 일관된 성능을 보임으로써 입증되었습니다. 또한, 위치 제어와의 비교 분석을 통해 제안된 토크 제어 접근법의 장점을 강조합니다. 결과는 이 방법을 휴머노이드 로봇의 센서리스 토크 제어를 위한 확장 가능하고 실용적인 솔루션으로 확립하며, 동적 환경에서 토크 추적, 적응성 및 안정성을 보장합니다.

## 핵심 내용
본 논문은 전기 모터와 고비율 하모닉 드라이브를 갖춘 시스템을 위해 설계된, 관절 토크 센서가 없는 휴머노이드 로봇의 전신 토크 제어를 위한 새로운 프레임워크를 제시합니다. 이 접근법은 물리 정보 신경망(PINN)을 마찰 모델링에, 무향 칼만 필터(UKF)를 관절 토크 추정에 통합하며, 실시간 토크 제어 아키텍처 내에서 작동합니다. PINN은 관절 및 모터 속도 판독값으로부터 비선형 정적 및 동적 마찰을 추정하여, 관절 움직임 없이 모터 작동과 같은 효과를 포착합니다. UKF는 PINN 기반 마찰 추정치를 직접 측정 입력으로 활용하여 토크 추정의 강건성을 향상시킵니다. ergoCub 휴머노이드 로봇에 대한 실험적 검증은 동적 균형 실험을 통해 최신 기술인 재귀 뉴턴-오일러 알고리즘(RNEA)과 비교하여 향상된 토크 추적 정확도, 향상된 에너지 효율성, 그리고 우수한 외란 제거 성능을 입증했습니다. 프레임워크의 확장성은 유사한 하드웨어를 가지지만 마찰 특성이 다른 로봇들에서 재식별 없이 일관된 성능을 보임으로써 입증되었습니다. 또한, 위치 제어와의 비교 분석을 통해 제안된 토크 제어 접근법의 장점을 강조합니다. 결과는 이 방법을 휴머노이드 로봇의 센서리스 토크 제어를 위한 확장 가능하고 실용적인 솔루션으로 확립하며, 동적 환경에서 토크 추적, 적응성 및 안정성을 보장합니다.
