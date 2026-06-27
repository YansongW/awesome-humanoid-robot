---
$id: ent_paper_marconi_structured_prediction_for_cris_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Structured Prediction for CRiSP Inverse Kinematics Learning with Misspecified
    Robot Models
  zh: 针对模型误设机器人的CRiSP逆运动学学习的结构化预测
  ko: 잘못 명시된 로봇 모델을 위한 CRiSP 역기구학 학습의 구조화 예측
summary:
  en: Introduces CRiSP-FK, a structured prediction algorithm that combines kernel
    regression with a possibly misspecified forward kinematics model to learn constrained
    inverse kinematics for redundant robot arms, supported by generalization guarantees
    and empirical evaluation on 5-DoF planar and 7-DoF Franka Emika Panda manipulators.
  zh: 提出CRiSP-FK结构化预测算法，将非参数核回归与可能不准确的正运动学模型相结合，通过约束L-BFGS-B优化前向运动学损失，学习冗余机械臂的约束逆运动学；并给出泛化保证，在5自由度平面与7自由度Franka
    Emika Panda机械臂上验证。
  ko: 비모수 커널 회귀와 잘못 명시될 수 있는 순방향 기구학 모델을 결합하여 구속 조건 하의 중복 로봇 팔 역기구학을 학습하는 CRiSP-FK
    구조화 예측 알고리즘을 제안하고, 일반화 보장과 5자유도 평면 매니퓰레이터 및 7자유도 Franka Emika Panda 팔에서의 실증 평가를
    제공한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; not independently cross-checked
    against the PDF.
sources:
- id: src_001
  type: paper
  title: Structured Prediction for CRiSP Inverse Kinematics Learning with Misspecified
    Robot Models
  url: https://arxiv.org/abs/2102.12942
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

The paper tackles the problem of learning inverse kinematics (IK) for redundant robot arms. Such problems are ill-posed because the forward kinematics map is non-invertible, joint limits impose hard constraints, and accurate analytic models are often unavailable. The authors propose CRiSP-FK, a structured prediction method that fuses a non-parametric kernel regressor with a forward kinematics model that may be imperfect. At inference time, predicted joint configurations are refined by minimizing a forward-kinematics loss subject to joint constraints via L-BFGS-B.

The approach is presented as a principled way to inject available structural knowledge into a data-driven learner. The authors prove universal consistency and derive excess risk bounds for the estimator. Empirical validation is performed on both a 5-DoF planar manipulator and a 7-DoF Franka Emika Panda arm, using trajectory reconstruction tasks to assess robustness to model misspecification.

## Key Contributions

- Introduces a structured prediction approach that exploits partial or inaccurate forward kinematics side information.
- Extends inverse kinematics learning to both end-effector position and orientation.
- Proves universal consistency and excess risk bounds for the proposed estimator.
- Empirically validates robustness to model misspecification on 2D and 3D trajectory reconstruction tasks.

## Relevance to Humanoid Robotics

Accurate and robust inverse kinematics solvers are core building blocks for humanoid robot motion control. By combining learning with imperfect but available kinematic models, the method could reduce reliance on perfectly calibrated models during mass production and deployment. However, the paper focuses on manipulator arms rather than full humanoid platforms, and the reported 0.7 s per-query latency would need acceleration for real-time whole-body control.
