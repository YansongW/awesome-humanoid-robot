---
$id: ent_paper_legged_robot_state_estimation_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Legged Robot State-Estimation Through Combined Forward Kinematic and Preintegrated Contact Factors
  zh: Legged Robot State-Estimation Through Combined Forward Kinematic and Preintegrated Contact Factors
  ko: Legged Robot State-Estimation Through Combined Forward Kinematic and Preintegrated Contact Factors
summary:
  en: Legged Robot State-Estimation Through Combined Forward Kinematic and Preintegrated Contact Factors is a 2017 work on
    state estimation for humanoid robots.
  zh: Legged Robot State-Estimation Through Combined Forward Kinematic and Preintegrated Contact Factors is a 2017 work on
    state estimation for humanoid robots.
  ko: Legged Robot State-Estimation Through Combined Forward Kinematic and Preintegrated Contact Factors is a 2017 work on
    state estimation for humanoid robots.
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
- legged_robot_state_estimation
- slam
- state_estimation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1712.05873v2.
sources:
- id: src_001
  type: paper
  title: Legged Robot State-Estimation Through Combined Forward Kinematic and Preintegrated Contact Factors (arXiv)
  url: https://arxiv.org/abs/1712.05873
  date: '2017'
  accessed_at: '2026-07-01'
---
## 概述
State-of-the-art robotic perception systems have achieved sufficiently good performance using Inertial Measurement Units (IMUs), cameras, and nonlinear optimization techniques, that they are now being deployed as technologies. However, many of these methods rely significantly on vision and often fail when visual tracking is lost due to lighting or scarcity of features. This paper presents a state-estimation technique for legged robots that takes into account the robot's kinematic model as well as its contact with the environment. We introduce forward kinematic factors and preintegrated contact factors into a factor graph framework that can be incrementally solved in real-time. The forward kinematic factor relates the robot's base pose to a contact frame through noisy encoder measurements. The preintegrated contact factor provides odometry measurements of this contact frame while accounting for possible foot slippage. Together, the two developed factors constrain the graph optimization problem allowing the robot's trajectory to be estimated. The paper evaluates the method using simulated and real sensory IMU and kinematic data from experiments with a Cassie-series robot designed by Agility Robotics. These preliminary experiments show that using the proposed method in addition to IMU decreases drift and improves localization accuracy, suggesting that its use can enable successful recovery from a loss of visual tracking.

## 核心内容
State-of-the-art robotic perception systems have achieved sufficiently good performance using Inertial Measurement Units (IMUs), cameras, and nonlinear optimization techniques, that they are now being deployed as technologies. However, many of these methods rely significantly on vision and often fail when visual tracking is lost due to lighting or scarcity of features. This paper presents a state-estimation technique for legged robots that takes into account the robot's kinematic model as well as its contact with the environment. We introduce forward kinematic factors and preintegrated contact factors into a factor graph framework that can be incrementally solved in real-time. The forward kinematic factor relates the robot's base pose to a contact frame through noisy encoder measurements. The preintegrated contact factor provides odometry measurements of this contact frame while accounting for possible foot slippage. Together, the two developed factors constrain the graph optimization problem allowing the robot's trajectory to be estimated. The paper evaluates the method using simulated and real sensory IMU and kinematic data from experiments with a Cassie-series robot designed by Agility Robotics. These preliminary experiments show that using the proposed method in addition to IMU decreases drift and improves localization accuracy, suggesting that its use can enable successful recovery from a loss of visual tracking.

## 参考
- http://arxiv.org/abs/1712.05873v2

## Overview
State-of-the-art robotic perception systems have achieved sufficiently good performance using Inertial Measurement Units (IMUs), cameras, and nonlinear optimization techniques, that they are now being deployed as technologies. However, many of these methods rely significantly on vision and often fail when visual tracking is lost due to lighting or scarcity of features. This paper presents a state-estimation technique for legged robots that takes into account the robot's kinematic model as well as its contact with the environment. We introduce forward kinematic factors and preintegrated contact factors into a factor graph framework that can be incrementally solved in real-time. The forward kinematic factor relates the robot's base pose to a contact frame through noisy encoder measurements. The preintegrated contact factor provides odometry measurements of this contact frame while accounting for possible foot slippage. Together, the two developed factors constrain the graph optimization problem allowing the robot's trajectory to be estimated. The paper evaluates the method using simulated and real sensory IMU and kinematic data from experiments with a Cassie-series robot designed by Agility Robotics. These preliminary experiments show that using the proposed method in addition to IMU decreases drift and improves localization accuracy, suggesting that its use can enable successful recovery from a loss of visual tracking.

## Content
State-of-the-art robotic perception systems have achieved sufficiently good performance using Inertial Measurement Units (IMUs), cameras, and nonlinear optimization techniques, that they are now being deployed as technologies. However, many of these methods rely significantly on vision and often fail when visual tracking is lost due to lighting or scarcity of features. This paper presents a state-estimation technique for legged robots that takes into account the robot's kinematic model as well as its contact with the environment. We introduce forward kinematic factors and preintegrated contact factors into a factor graph framework that can be incrementally solved in real-time. The forward kinematic factor relates the robot's base pose to a contact frame through noisy encoder measurements. The preintegrated contact factor provides odometry measurements of this contact frame while accounting for possible foot slippage. Together, the two developed factors constrain the graph optimization problem allowing the robot's trajectory to be estimated. The paper evaluates the method using simulated and real sensory IMU and kinematic data from experiments with a Cassie-series robot designed by Agility Robotics. These preliminary experiments show that using the proposed method in addition to IMU decreases drift and improves localization accuracy, suggesting that its use can enable successful recovery from a loss of visual tracking.

## 개요
최첨단 로봇 인식 시스템은 관성 측정 장치(IMU), 카메라 및 비선형 최적화 기법을 사용하여 충분히 우수한 성능을 달성했으며, 이제 기술로 배포되고 있습니다. 그러나 이러한 방법 중 상당수는 시각에 크게 의존하며, 조명이나 특징 부족으로 인해 시각적 추적이 손실될 때 종종 실패합니다. 본 논문은 로봇의 운동학적 모델과 환경과의 접촉을 고려한 보행 로봇용 상태 추정 기법을 제시합니다. 우리는 전방 운동학적 요인과 사전 통합 접촉 요인을 요인 그래프 프레임워크에 도입하여 실시간으로 점진적으로 해결할 수 있도록 합니다. 전방 운동학적 요인은 노이즈가 있는 엔코더 측정을 통해 로봇의 베이스 자세를 접촉 프레임과 연결합니다. 사전 통합 접촉 요인은 발 미끄러짐 가능성을 고려하면서 이 접촉 프레임의 주행 거리 측정을 제공합니다. 함께 개발된 두 요인은 그래프 최적화 문제를 제약하여 로봇의 궤적을 추정할 수 있게 합니다. 본 논문은 Agility Robotics가 설계한 Cassie 시리즈 로봇 실험에서 얻은 시뮬레이션 및 실제 센서 IMU와 운동학적 데이터를 사용하여 방법을 평가합니다. 이러한 예비 실험은 제안된 방법을 IMU와 함께 사용하면 드리프트를 줄이고 위치 추정 정확도를 향상시켜 시각적 추적 손실로부터 성공적인 복구를 가능하게 함을 보여줍니다.

## 핵심 내용
최첨단 로봇 인식 시스템은 관성 측정 장치(IMU), 카메라 및 비선형 최적화 기법을 사용하여 충분히 우수한 성능을 달성했으며, 이제 기술로 배포되고 있습니다. 그러나 이러한 방법 중 상당수는 시각에 크게 의존하며, 조명이나 특징 부족으로 인해 시각적 추적이 손실될 때 종종 실패합니다. 본 논문은 로봇의 운동학적 모델과 환경과의 접촉을 고려한 보행 로봇용 상태 추정 기법을 제시합니다. 우리는 전방 운동학적 요인과 사전 통합 접촉 요인을 요인 그래프 프레임워크에 도입하여 실시간으로 점진적으로 해결할 수 있도록 합니다. 전방 운동학적 요인은 노이즈가 있는 엔코더 측정을 통해 로봇의 베이스 자세를 접촉 프레임과 연결합니다. 사전 통합 접촉 요인은 발 미끄러짐 가능성을 고려하면서 이 접촉 프레임의 주행 거리 측정을 제공합니다. 함께 개발된 두 요인은 그래프 최적화 문제를 제약하여 로봇의 궤적을 추정할 수 있게 합니다. 본 논문은 Agility Robotics가 설계한 Cassie 시리즈 로봇 실험에서 얻은 시뮬레이션 및 실제 센서 IMU와 운동학적 데이터를 사용하여 방법을 평가합니다. 이러한 예비 실험은 제안된 방법을 IMU와 함께 사용하면 드리프트를 줄이고 위치 추정 정확도를 향상시켜 시각적 추적 손실로부터 성공적인 복구를 가능하게 함을 보여줍니다.
