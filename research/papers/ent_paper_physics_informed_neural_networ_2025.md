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
  zh: 本文提出一种结合物理信息神经网络（PINNs）与无迹卡尔曼滤波（UKF）的无传感器关节力矩估计框架，用于人形机器人全身力矩控制。该方法通过PINNs建模非线性摩擦，并利用UKF将摩擦估计作为直接测量输入，在ergoCub人形机器人上验证了力矩跟踪精度、能效和抗干扰能力的提升，且无需重新辨识即可适应不同摩擦特性的机器人。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.10105v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Physics-Informed Neural Networks with Unscented Kalman Filter for Sensorless Joint Torque Estimation (arXiv)
  url: https://arxiv.org/abs/2507.10105
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对采用电机和高减速比谐波驱动的人形机器人系统，提出了一种无需关节力矩传感器的力矩控制方案。核心创新在于将PINNs用于摩擦建模，从关节和电机速度读数中估计非线性静态与动态摩擦，包括无关节运动时的电机驱动效应。随后，UKF利用PINN的摩擦估计作为直接测量输入，增强了力矩估计的鲁棒性。在ergoCub人形机器人上的动态平衡实验中，该方法在力矩跟踪精度、能效和抗干扰能力上均优于当前最先进的递归牛顿-欧拉算法（RNEA）。此外，该框架在具有不同摩擦特性的相似硬件机器人上表现出一致的性能，无需重新辨识，验证了其可扩展性。

## 核心内容
### 方法架构
- **PINNs摩擦建模**：利用物理信息神经网络（PINNs）从关节和电机速度读数中估计非线性静态与动态摩擦，能够捕捉电机驱动但关节未运动时的摩擦效应。
- **UKF力矩估计**：无迹卡尔曼滤波（UKF）将PINNs的摩擦估计作为直接测量输入，提升力矩估计的鲁棒性，并与实时力矩控制架构集成。

### 实验设置
- **平台**：在ergoCub人形机器人上进行动态平衡实验验证。
- **对比基准**：与当前最先进的递归牛顿-欧拉算法（RNEA）进行对比。

### 关键结果
- **力矩跟踪**：相比RNEA，该方法显著提升了力矩跟踪精度。
- **能效**：在动态平衡实验中，能量效率得到增强。
- **抗干扰能力**：展现出更优的扰动抑制性能。
- **可扩展性**：在具有不同摩擦特性的相似硬件机器人上表现一致，无需重新辨识模型参数。
- **对比分析**：与位置控制方法的比较进一步凸显了所提力矩控制方法的优势。

### 结论
该框架被证明是一种可扩展且实用的人形机器人无传感器力矩控制方案，能够在动态环境中确保力矩跟踪、适应性和稳定性。

## Overview
This paper presents a novel framework for whole-body torque control of humanoid robots without joint torque sensors, designed for systems with electric motors and high-ratio harmonic drives. The approach integrates Physics-Informed Neural Networks (PINNs) for friction modeling and Unscented Kalman Filtering (UKF) for joint torque estimation, within a real-time torque control architecture. PINNs estimate nonlinear static and dynamic friction from joint and motor velocity readings, capturing effects like motor actuation without joint movement. The UKF utilizes PINN-based friction estimates as direct measurement inputs, improving torque estimation robustness. Experimental validation on the ergoCub humanoid robot demonstrates improved torque tracking accuracy, enhanced energy efficiency, and superior disturbance rejection compared to the state-of-the-art Recursive Newton-Euler Algorithm (RNEA), using a dynamic balancing experiment. The framework's scalability is shown by consistent performance across robots with similar hardware but different friction characteristics, without re-identification. Furthermore, a comparative analysis with position control highlights the advantages of the proposed torque control approach. The results establish the method as a scalable and practical solution for sensorless torque control in humanoid robots, ensuring torque tracking, adaptability, and stability in dynamic environments.

## 개요
본 논문은 전기 모터와 고비율 하모닉 드라이브를 갖춘 시스템을 위해 설계된, 관절 토크 센서가 없는 휴머노이드 로봇의 전신 토크 제어를 위한 새로운 프레임워크를 제시합니다. 이 접근법은 물리 정보 신경망(PINN)을 마찰 모델링에, 무향 칼만 필터(UKF)를 관절 토크 추정에 통합하며, 실시간 토크 제어 아키텍처 내에서 작동합니다. PINN은 관절 및 모터 속도 판독값으로부터 비선형 정적 및 동적 마찰을 추정하여, 관절 움직임 없이 모터 작동과 같은 효과를 포착합니다. UKF는 PINN 기반 마찰 추정치를 직접 측정 입력으로 활용하여 토크 추정의 강건성을 향상시킵니다. ergoCub 휴머노이드 로봇에 대한 실험적 검증은 동적 균형 실험을 통해 최신 기술인 재귀 뉴턴-오일러 알고리즘(RNEA)과 비교하여 향상된 토크 추적 정확도, 향상된 에너지 효율성, 그리고 우수한 외란 제거 성능을 입증했습니다. 프레임워크의 확장성은 유사한 하드웨어를 가지지만 마찰 특성이 다른 로봇들에서 재식별 없이 일관된 성능을 보임으로써 입증되었습니다. 또한, 위치 제어와의 비교 분석을 통해 제안된 토크 제어 접근법의 장점을 강조합니다. 결과는 이 방법을 휴머노이드 로봇의 센서리스 토크 제어를 위한 확장 가능하고 실용적인 솔루션으로 확립하며, 동적 환경에서 토크 추적, 적응성 및 안정성을 보장합니다.

## 핵심 내용
본 논문은 전기 모터와 고비율 하모닉 드라이브를 갖춘 시스템을 위해 설계된, 관절 토크 센서가 없는 휴머노이드 로봇의 전신 토크 제어를 위한 새로운 프레임워크를 제시합니다. 이 접근법은 물리 정보 신경망(PINN)을 마찰 모델링에, 무향 칼만 필터(UKF)를 관절 토크 추정에 통합하며, 실시간 토크 제어 아키텍처 내에서 작동합니다. PINN은 관절 및 모터 속도 판독값으로부터 비선형 정적 및 동적 마찰을 추정하여, 관절 움직임 없이 모터 작동과 같은 효과를 포착합니다. UKF는 PINN 기반 마찰 추정치를 직접 측정 입력으로 활용하여 토크 추정의 강건성을 향상시킵니다. ergoCub 휴머노이드 로봇에 대한 실험적 검증은 동적 균형 실험을 통해 최신 기술인 재귀 뉴턴-오일러 알고리즘(RNEA)과 비교하여 향상된 토크 추적 정확도, 향상된 에너지 효율성, 그리고 우수한 외란 제거 성능을 입증했습니다. 프레임워크의 확장성은 유사한 하드웨어를 가지지만 마찰 특성이 다른 로봇들에서 재식별 없이 일관된 성능을 보임으로써 입증되었습니다. 또한, 위치 제어와의 비교 분석을 통해 제안된 토크 제어 접근법의 장점을 강조합니다. 결과는 이 방법을 휴머노이드 로봇의 센서리스 토크 제어를 위한 확장 가능하고 실용적인 솔루션으로 확립하며, 동적 환경에서 토크 추적, 적응성 및 안정성을 보장합니다.

## 参考
- http://arxiv.org/abs/2507.10105v1
