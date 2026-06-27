---
$id: ent_paper_sorrentino_physics_informed_neural_networ_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Physics-Informed Neural Networks with Unscented Kalman Filter for Sensorless
    Joint Torque Estimation in Humanoid Robots
  zh: 基于物理信息神经网络与无迹卡尔曼滤波的人形机器人无传感器关节力矩估计
  ko: 물리 정보 신경망과 무향 칼만 필터를 활용한 휴로이드 로봇의 무센서 관절 토크 추정
summary:
  en: This paper proposes a real-time sensorless whole-body torque control framework
    for humanoid robots with electric motors and harmonic drives, combining PINNs
    for nonlinear friction modeling and a floating-base UKF that uses PINN friction
    estimates as direct measurements; experiments on ergoCub show improved torque
    tracking, energy efficiency, and disturbance rejection compared to RNEA and position
    control.
  zh: 本文面向配备电机与谐波减速器的人形机器人，提出了一种实时无传感器全身力矩控制框架，结合物理信息神经网络（PINN）进行非线性摩擦建模，并将PINN摩擦估计作为直接测量输入无迹卡尔曼滤波器（UKF）；ergoCub机器人实验表明，相较于递归牛顿-欧拉算法（RNEA）和位置控制，该方法在力矩跟踪精度、能效和抗扰动性方面均有提升。
  ko: 본 논문은 전기 모터와 하모닉 드라이브를 갖춘 휴로이드 로봇을 위한 실시간 무센서 전신 토크 제어 프레임워크를 제안한다. 비선형 마찰 모델링을
    위한 물리 정보 신경망(PINN)과 PINN 마찰 추정치를 직접 측정값으로 활용하는 무향 칼만 필터(UKF)를 결합하였으며, ergoCub
    로봇 실험에서 RNEA 및 위치 제어 대비 토크 추적 정확도, 에너지 효율, 외란 거부 성능이 향상되었음을 보였다.
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
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: AI-extracted from the arXiv full text; requires human review before full
    verification.
sources:
- id: src_001
  type: paper
  title: Physics-Informed Neural Networks with Unscented Kalman Filter for Sensorless
    Joint Torque Estimation in Humanoid Robots
  url: https://arxiv.org/abs/2507.10105
  date: '2025'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_component_harmonic_drive_reducer
  relationship: integrates
  description:
    en: The framework is designed for systems with electric motors and high-ratio
      harmonic drives.
    zh: 该框架面向配备电机和高减速比谐波减速器的系统而设计。
    ko: 해당 프레임워크는 전기 모터와 고감속비 하모닉 드라이브를 갖춘 시스템을 대상으로 설계되었다.
theoretical_depth:
- system
---



## Overview

Many humanoid robots omit joint torque sensors because of cost, integration complexity, and sensor limitations, which forces rigid position-based strategies that struggle in dynamic contact. This paper introduces a real-time sensorless whole-body torque-control framework for electric-motor/harmonic-drive humanoids. It combines a Physics-Informed Neural Network (PINN) that models nonlinear static and dynamic friction from buffered motor and joint velocities, and a floating-base Unscented Kalman Filter (UKF) that treats the PINN friction estimates as direct measurements to estimate joint torques.

The control architecture couples a high-level momentum-based controller running at 100 Hz with a low-level PI torque controller running at 1 kHz; motor currents are regulated at 20 kHz. Experiments on the ergoCub humanoid control 18 joints using feet, waist, and arm IMUs, feet force/torque sensors, motor-current sensors, and joint/motor encoders. Six configurations—feedforward, RNEA with and without friction compensation, UKF with and without friction compensation, feedforward PINN, RNEA-PINN, and UKF-PINN—are compared in a dynamic balancing task. The fully integrated UKF-PINN configuration achieves the best torque tracking accuracy, energy efficiency, and disturbance rejection, and the same trained model transfers to a second ergoCub robot without re-identification.

The authors acknowledge remaining limitations: running the UKF in real time adds computational cost, validation is currently restricted to balancing tasks with walking and broader locomotion left as future work, and the primary experiments are performed on ergoCub robots.

## Key Contributions

- Extension of PINN-based friction modeling to all leg joints using motor and joint velocity buffers, enabling capture of static friction when the motor is actuated but the joint remains stationary.
- A floating-base UKF formulation that incorporates PINN-predicted friction torques as direct measurement inputs rather than treating friction as an unmodeled disturbance.
- A unified real-time torque-control architecture that synergistically integrates PINN friction estimation and UKF torque estimation.
- Experimental demonstration on the ergoCub humanoid that the framework outperforms RNEA-based estimation and position control, and generalizes across two ergoCub robots with different friction characteristics without re-identification.

## Relevance to Humanoid Robotics

Sensorless whole-body torque control removes the need for per-joint torque sensors, lowering hardware cost and integration complexity—both critical for mass production of humanoid robots. The framework's ability to maintain consistent performance across robots with similar hardware but different friction characteristics without re-identification reduces deployment overhead. By improving compliance, energy efficiency, and disturbance rejection, the approach also supports safe and adaptive operation in unstructured human environments.
