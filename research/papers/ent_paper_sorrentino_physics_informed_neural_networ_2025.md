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
  zh: 本文提出一种面向人形机器人无关节力矩传感器的全身力矩控制框架，结合Physics-Informed Neural Networks (PINNs)进行非线性摩擦建模，并利用浮基Unscented Kalman Filter (UKF)将PINN摩擦估计作为直接测量输入。在ergoCub机器人上的实验表明，该方法相比Recursive
    Newton-Euler Algorithm (RNEA)和位置控制，在力矩跟踪精度、能效和抗干扰能力上均有提升。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.10105v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
该框架专为配备电机和高减速比谐波驱动的人形机器人设计，无需关节力矩传感器即可实现实时全身力矩控制。核心创新在于PINNs从关节和电机速度读数中估计非线性静动态摩擦，捕捉电机空转等效应，而UKF则将这些估计作为直接测量输入，增强力矩估计的鲁棒性。在ergoCub机器人上的动态平衡实验中，该方法在力矩跟踪精度、能效和抗干扰能力上均优于当前最先进的RNEA。此外，框架展现出良好的可扩展性，可在硬件相似但摩擦特性不同的机器人上直接应用，无需重新识别参数。

## 核心内容
### 方法架构
- **PINNs摩擦建模**：利用Physics-Informed Neural Networks从关节和电机速度读数中估计非线性静动态摩擦，包括电机空转（电机转动但关节不动）等复杂效应。
- **UKF力矩估计**：采用浮基Unscented Kalman Filter，将PINN的摩擦估计作为直接测量输入，提升力矩估计的鲁棒性和实时性。
- **控制架构**：在实时力矩控制框架中集成上述模块，实现无传感器全身力矩控制。

### 实验设置
- **机器人平台**：ergoCub人形机器人，配备电机和高减速比谐波驱动。
- **对比方法**：与Recursive Newton-Euler Algorithm (RNEA)和传统位置控制进行对比。
- **实验任务**：动态平衡实验，评估力矩跟踪精度、能效和抗干扰能力。

### 关键结果
- **力矩跟踪**：相比RNEA，PINN+UKF框架显著提升了力矩跟踪精度。
- **能效**：在动态平衡实验中，该方法比位置控制更节能。
- **抗干扰能力**：在外部扰动下，该方法展现出更优的稳定性和恢复能力。
- **可扩展性**：在硬件相似但摩擦特性不同的机器人上直接应用，无需重新识别参数，验证了框架的通用性。

### 结论
该框架为无传感器力矩控制提供了可扩展且实用的解决方案，在动态环境中确保了力矩跟踪精度、适应性和稳定性，适用于人形机器人的全身控制。

## Overview
This paper presents a novel framework for whole-body torque control of humanoid robots without joint torque sensors, designed for systems with electric motors and high-ratio harmonic drives. The approach integrates Physics-Informed Neural Networks (PINNs) for friction modeling and Unscented Kalman Filtering (UKF) for joint torque estimation, within a real-time torque control architecture. PINNs estimate nonlinear static and dynamic friction from joint and motor velocity readings, capturing effects like motor actuation without joint movement. The UKF utilizes PINN-based friction estimates as direct measurement inputs, improving torque estimation robustness. Experimental validation on the ergoCub humanoid robot demonstrates improved torque tracking accuracy, enhanced energy efficiency, and superior disturbance rejection compared to the state-of-the-art Recursive Newton-Euler Algorithm (RNEA), using a dynamic balancing experiment. The framework's scalability is shown by consistent performance across robots with similar hardware but different friction characteristics, without re-identification. Furthermore, a comparative analysis with position control highlights the advantages of the proposed torque control approach. The results establish the method as a scalable and practical solution for sensorless torque control in humanoid robots, ensuring torque tracking, adaptability, and stability in dynamic environments.

## 개요
본 논문은 관절 토크 센서가 없는 휴머노이드 로봇의 전신 토크 제어를 위한 새로운 프레임워크를 제시하며, 전기 모터와 고비율 하모닉 드라이브를 갖춘 시스템을 위해 설계되었습니다. 이 접근법은 물리 정보 신경망(PINN)을 마찰 모델링에, 무향 칼만 필터(UKF)를 관절 토크 추정에 통합하여 실시간 토크 제어 아키텍처 내에서 작동합니다. PINN은 관절 및 모터 속도 판독값으로부터 비선형 정적 및 동적 마찰을 추정하여, 관절 움직임 없이 모터 작동과 같은 효과를 포착합니다. UKF는 PINN 기반 마찰 추정치를 직접 측정 입력으로 활용하여 토크 추정의 견고성을 향상시킵니다. ergoCub 휴머노이드 로봇에 대한 실험적 검증은 동적 균형 실험을 통해 최신 기술인 재귀 뉴턴-오일러 알고리즘(RNEA)과 비교하여 향상된 토크 추적 정확도, 향상된 에너지 효율성, 그리고 우수한 외란 제거 성능을 입증했습니다. 프레임워크의 확장성은 유사한 하드웨어를 가지지만 마찰 특성이 다른 로봇들에서 재식별 없이 일관된 성능을 보여줌으로써 입증되었습니다. 또한, 위치 제어와의 비교 분석을 통해 제안된 토크 제어 접근법의 장점이 강조되었습니다. 결과는 이 방법이 휴머노이드 로봇의 센서리스 토크 제어를 위한 확장 가능하고 실용적인 솔루션임을 확립하며, 동적 환경에서 토크 추적, 적응성 및 안정성을 보장합니다.

## 핵심 내용
본 논문은 관절 토크 센서가 없는 휴머노이드 로봇의 전신 토크 제어를 위한 새로운 프레임워크를 제시하며, 전기 모터와 고비율 하모닉 드라이브를 갖춘 시스템을 위해 설계되었습니다. 이 접근법은 물리 정보 신경망(PINN)을 마찰 모델링에, 무향 칼만 필터(UKF)를 관절 토크 추정에 통합하여 실시간 토크 제어 아키텍처 내에서 작동합니다. PINN은 관절 및 모터 속도 판독값으로부터 비선형 정적 및 동적 마찰을 추정하여, 관절 움직임 없이 모터 작동과 같은 효과를 포착합니다. UKF는 PINN 기반 마찰 추정치를 직접 측정 입력으로 활용하여 토크 추정의 견고성을 향상시킵니다. ergoCub 휴머노이드 로봇에 대한 실험적 검증은 동적 균형 실험을 통해 최신 기술인 재귀 뉴턴-오일러 알고리즘(RNEA)과 비교하여 향상된 토크 추적 정확도, 향상된 에너지 효율성, 그리고 우수한 외란 제거 성능을 입증했습니다. 프레임워크의 확장성은 유사한 하드웨어를 가지지만 마찰 특성이 다른 로봇들에서 재식별 없이 일관된 성능을 보여줌으로써 입증되었습니다. 또한, 위치 제어와의 비교 분석을 통해 제안된 토크 제어 접근법의 장점이 강조되었습니다. 결과는 이 방법이 휴머노이드 로봇의 센서리스 토크 제어를 위한 확장 가능하고 실용적인 솔루션임을 확립하며, 동적 환경에서 토크 추적, 적응성 및 안정성을 보장합니다.

## 参考
- http://arxiv.org/abs/2507.10105v1
