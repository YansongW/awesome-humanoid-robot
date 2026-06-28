---
$id: ent_paper_zheng_model_based_control_of_planar_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Model-Based Control of Planar Piezoelectric Inchworm Soft Robot for Crawling
    in Constrained Environments
  zh: 受限环境中平面压电尺蠖软体机器人爬行运动的模型化控制
  ko: 제한된 환경에서 크롤링을 위한 평면 압전 인치웜 소프트 로봇의 모델 기반 제어
summary:
  en: Zheng et al. present a model-based full-shape controller for a five-actuator
    planar piezoelectric soft robot, using a continuous soft-body model and Bayesian
    optimization to select actuator voltages for target shapes, an implicit loss-based
    shape planner for crawling under overhead roof constraints, and background model
    calibration via online linear regression to compensate material variations and
    drift.
  zh: Zheng等人提出了一种五执行器平面压电软体机器人的基于模型全形状控制器，利用连续软体模型与贝叶斯优化选择执行器电压以逼近目标形状，并采用基于距离损失的隐式形状规划器在头顶障碍物下爬行，同时通过在线线性回归进行背景模型校准以补偿材料变化和漂移。
  ko: Zheng 등은 5개 액추에이터 평면 압전 소프트 로봇을 위한 모델 기반 전체 형상 제어기를 제안한다. 연속 소프트 바디 모델과 베이지안
    최적화를 사용해 목표 형상에 대한 액추에이터 전압을 선택하고, 천장 장애물 아래 크롤링을 위한 거리 기반 손실 암시적 형상 플래너를 적용하며,
    재료 변화와 드리프트를 보상하기 위해 온라인 선형 회귀를 통한 배경 모델 보정을 수행한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 06_design_engineering
layers:
- intelligence
- foundations
functional_roles:
- knowledge
- intelligence
tags:
- model_based_control
- soft_robotics
- full_shape_control
- piezoelectric_actuation
- inchworm_locomotion
- constrained_environment_planning
- bayesian_optimization
- online_calibration
- soft_body_model
- shape_planning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from arXiv abstract and full text; requires human review before
    verification.
sources:
- id: src_001
  type: paper
  title: Model-Based Control of Planar Piezoelectric Inchworm Soft Robot for Crawling
    in Constrained Environments
  url: https://arxiv.org/abs/2203.15198
  date: '2022'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

This paper develops a model-based full-shape controller for a planar, five-actuator piezoelectric soft robot that performs inchworm-like crawling. The robot is built from five 100 mm-long, 300 µm-thick piezoelectric macrofiber composite units bonded to a 50 µm-thick flexible steel foil; high-friction films on the underside of the two ends provide the anchoring needed for locomotion. The controller relies on a continuous soft-body model in function space to predict the robot shape under piezoelectric actuation, gravity, and ground contact.

Two control tasks are addressed. The first is target-shape control, formulated as an L2-norm minimization between the model-predicted shape and a desired target shape; because evaluating the physics-based loss is expensive, the authors use Bayesian optimization to select the five actuator voltages. The second task is crawling under an overhead barrier (a "roof"). Here the controller performs implicit shape planning by replacing the target-shape loss with a collision-avoidance loss that heavily penalizes roof penetration while minimizing clearance to the roof safety line, thereby maximizing speed without collision.

To handle deviations caused by material and fabrication variations as well as drift, the authors augment the physics-based model with a voltage-linear correction term and update its coefficients using online linear regression. The paper reports full experimental shape-control demonstrations and crawling under a step-shaped roof on an acrylic board, plus simulation validation for slanted and sinusoidal roofs.

## Key Contributions

- First model-based full-shape controller for electrostatic soft robots using a continuous soft-body model in function space.
- L2-norm target-shape controller solved with Bayesian optimization to select actuator voltages.
- Implicit shape-planning controller for crawling under overhead roof constraints using a collision-avoidance loss function.
- Background model calibration approach that augments the physics-based shape model with a linear correction term updated by online linear regression.
- Experimental validation of target-shape control and crawling under a step-shaped roof, with simulation validation for slanted and sinusoidal roofs.

## Relevance to Humanoid Robotics

Although the demonstration platform is a planar soft inchworm robot, the control methodology is directly relevant to humanoid robotics. Model-based full-shape control, online calibration against material drift, and constrained-environment shape planning are core capabilities for compliant humanoid body segments and soft actuators that must operate safely in cluttered or confined spaces. The techniques for balancing collision avoidance with task performance translate to adaptive motion planning and whole-body control in humanoid deployment scenarios.
