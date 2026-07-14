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

