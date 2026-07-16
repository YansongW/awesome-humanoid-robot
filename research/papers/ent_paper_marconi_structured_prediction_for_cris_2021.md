---
$id: ent_paper_marconi_structured_prediction_for_cris_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Structured Prediction for CRiSP Inverse Kinematics Learning with Misspecified Robot Models
  zh: 针对模型误设机器人的CRiSP逆运动学学习的结构化预测
  ko: 잘못 명시된 로봇 모델을 위한 CRiSP 역기구학 학습의 구조화 예측
summary:
  en: Introduces CRiSP-FK, a structured prediction algorithm that combines kernel regression with a possibly misspecified
    forward kinematics model to learn constrained inverse kinematics for redundant robot arms, supported by generalization
    guarantees and empirical evaluation on 5-DoF planar and 7-DoF Franka Emika Panda manipulators.
  zh: 提出CRiSP-FK结构化预测算法，将非参数核回归与可能不准确的正运动学模型相结合，通过约束L-BFGS-B优化前向运动学损失，学习冗余机械臂的约束逆运动学；并给出泛化保证，在5自由度平面与7自由度Franka Emika Panda机械臂上验证。
  ko: 비모수 커널 회귀와 잘못 명시될 수 있는 순방향 기구학 모델을 결합하여 구속 조건 하의 중복 로봇 팔 역기구학을 학습하는 CRiSP-FK 구조화 예측 알고리즘을 제안하고, 일반화 보장과 5자유도 평면 매니퓰레이터
    및 7자유도 Franka Emika Panda 팔에서의 실증 평가를 제공한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- inverse_kinematics
- structured_prediction
- kernel_regression
- forward_kinematics
- model_misspecification
- redundant_manipulator
- robot_arm
- trajectory_reconstruction
- l_bfgs_b
- constrained_optimization
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2102.12942v3.
sources:
- id: src_001
  type: paper
  title: Structured Prediction for CRiSP Inverse Kinematics Learning with Misspecified Robot Models
  url: https://arxiv.org/abs/2102.12942
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
With the recent advances in machine learning, problems that traditionally would require accurate modeling to be solved analytically can now be successfully approached with data-driven strategies. Among these, computing the inverse kinematics of a redundant robot arm poses a significant challenge due to the non-linear structure of the robot, the hard joint constraints and the non-invertible kinematics map. Moreover, most learning algorithms consider a completely data-driven approach, while often useful information on the structure of the robot is available and should be positively exploited. In this work, we present a simple, yet effective, approach for learning the inverse kinematics. We introduce a structured prediction algorithm that combines a data-driven strategy with the model provided by a forward kinematics function -- even when this function is misspecified -- to accurately solve the problem. The proposed approach ensures that predicted joint configurations are well within the robot's constraints. We also provide statistical guarantees on the generalization properties of our estimator as well as an empirical evaluation of its performance on trajectory reconstruction tasks.

## 核心内容
With the recent advances in machine learning, problems that traditionally would require accurate modeling to be solved analytically can now be successfully approached with data-driven strategies. Among these, computing the inverse kinematics of a redundant robot arm poses a significant challenge due to the non-linear structure of the robot, the hard joint constraints and the non-invertible kinematics map. Moreover, most learning algorithms consider a completely data-driven approach, while often useful information on the structure of the robot is available and should be positively exploited. In this work, we present a simple, yet effective, approach for learning the inverse kinematics. We introduce a structured prediction algorithm that combines a data-driven strategy with the model provided by a forward kinematics function -- even when this function is misspecified -- to accurately solve the problem. The proposed approach ensures that predicted joint configurations are well within the robot's constraints. We also provide statistical guarantees on the generalization properties of our estimator as well as an empirical evaluation of its performance on trajectory reconstruction tasks.

## 参考
- http://arxiv.org/abs/2102.12942v3

## Overview
With the recent advances in machine learning, problems that traditionally would require accurate modeling to be solved analytically can now be successfully approached with data-driven strategies. Among these, computing the inverse kinematics of a redundant robot arm poses a significant challenge due to the non-linear structure of the robot, the hard joint constraints and the non-invertible kinematics map. Moreover, most learning algorithms consider a completely data-driven approach, while often useful information on the structure of the robot is available and should be positively exploited. In this work, we present a simple, yet effective, approach for learning the inverse kinematics. We introduce a structured prediction algorithm that combines a data-driven strategy with the model provided by a forward kinematics function -- even when this function is misspecified -- to accurately solve the problem. The proposed approach ensures that predicted joint configurations are well within the robot's constraints. We also provide statistical guarantees on the generalization properties of our estimator as well as an empirical evaluation of its performance on trajectory reconstruction tasks.

## Content
With the recent advances in machine learning, problems that traditionally would require accurate modeling to be solved analytically can now be successfully approached with data-driven strategies. Among these, computing the inverse kinematics of a redundant robot arm poses a significant challenge due to the non-linear structure of the robot, the hard joint constraints and the non-invertible kinematics map. Moreover, most learning algorithms consider a completely data-driven approach, while often useful information on the structure of the robot is available and should be positively exploited. In this work, we present a simple, yet effective, approach for learning the inverse kinematics. We introduce a structured prediction algorithm that combines a data-driven strategy with the model provided by a forward kinematics function -- even when this function is misspecified -- to accurately solve the problem. The proposed approach ensures that predicted joint configurations are well within the robot's constraints. We also provide statistical guarantees on the generalization properties of our estimator as well as an empirical evaluation of its performance on trajectory reconstruction tasks.

## 개요
최근 기계 학습의 발전으로 인해, 전통적으로 정확한 모델링이 필요했던 문제들도 이제 데이터 기반 전략을 통해 성공적으로 접근할 수 있게 되었습니다. 그중에서도, 중복 로봇 팔의 역기구학 계산은 로봇의 비선형 구조, 엄격한 관절 제약 조건, 그리고 역변환이 불가능한 기구학 맵으로 인해 상당한 도전 과제가 됩니다. 또한, 대부분의 학습 알고리즘은 완전히 데이터 기반 접근법을 고려하지만, 로봇 구조에 대한 유용한 정보가 종종 존재하며 이를 적극적으로 활용해야 합니다. 본 연구에서는 역기구학 학습을 위한 간단하면서도 효과적인 접근법을 제시합니다. 우리는 데이터 기반 전략과 순기구학 함수(이 함수가 잘못 지정된 경우에도)가 제공하는 모델을 결합하여 문제를 정확히 해결하는 구조화된 예측 알고리즘을 소개합니다. 제안된 접근법은 예측된 관절 구성이 로봇의 제약 조건 내에 잘 있도록 보장합니다. 또한, 추정기의 일반화 특성에 대한 통계적 보장과 궤적 재구성 작업에서의 성능에 대한 경험적 평가를 제공합니다.

## 핵심 내용
최근 기계 학습의 발전으로 인해, 전통적으로 정확한 모델링이 필요했던 문제들도 이제 데이터 기반 전략을 통해 성공적으로 접근할 수 있게 되었습니다. 그중에서도, 중복 로봇 팔의 역기구학 계산은 로봇의 비선형 구조, 엄격한 관절 제약 조건, 그리고 역변환이 불가능한 기구학 맵으로 인해 상당한 도전 과제가 됩니다. 또한, 대부분의 학습 알고리즘은 완전히 데이터 기반 접근법을 고려하지만, 로봇 구조에 대한 유용한 정보가 종종 존재하며 이를 적극적으로 활용해야 합니다. 본 연구에서는 역기구학 학습을 위한 간단하면서도 효과적인 접근법을 제시합니다. 우리는 데이터 기반 전략과 순기구학 함수(이 함수가 잘못 지정된 경우에도)가 제공하는 모델을 결합하여 문제를 정확히 해결하는 구조화된 예측 알고리즘을 소개합니다. 제안된 접근법은 예측된 관절 구성이 로봇의 제약 조건 내에 잘 있도록 보장합니다. 또한, 추정기의 일반화 특성에 대한 통계적 보장과 궤적 재구성 작업에서의 성능에 대한 경험적 평가를 제공합니다.
