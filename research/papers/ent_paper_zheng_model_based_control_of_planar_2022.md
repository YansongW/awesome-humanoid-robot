---
$id: ent_paper_zheng_model_based_control_of_planar_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Model-Based Control of Planar Piezoelectric Inchworm Soft Robot for Crawling in Constrained Environments
  zh: 受限环境中平面压电尺蠖软体机器人爬行运动的模型化控制
  ko: 제한된 환경에서 크롤링을 위한 평면 압전 인치웜 소프트 로봇의 모델 기반 제어
summary:
  en: Zheng et al. present a model-based full-shape controller for a five-actuator planar piezoelectric soft robot, using
    a continuous soft-body model and Bayesian optimization to select actuator voltages for target shapes, an implicit loss-based
    shape planner for crawling under overhead roof constraints, and background model calibration via online linear regression
    to compensate material variations and drift.
  zh: Zheng等人提出了一种五执行器平面压电软体机器人的基于模型全形状控制器，利用连续软体模型与贝叶斯优化选择执行器电压以逼近目标形状，并采用基于距离损失的隐式形状规划器在头顶障碍物下爬行，同时通过在线线性回归进行背景模型校准以补偿材料变化和漂移。
  ko: Zheng 등은 5개 액추에이터 평면 압전 소프트 로봇을 위한 모델 기반 전체 형상 제어기를 제안한다. 연속 소프트 바디 모델과 베이지안 최적화를 사용해 목표 형상에 대한 액추에이터 전압을 선택하고, 천장 장애물
    아래 크롤링을 위한 거리 기반 손실 암시적 형상 플래너를 적용하며, 재료 변화와 드리프트를 보상하기 위해 온라인 선형 회귀를 통한 배경 모델 보정을 수행한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2203.15198v1.
sources:
- id: src_001
  type: paper
  title: Model-Based Control of Planar Piezoelectric Inchworm Soft Robot for Crawling in Constrained Environments
  url: https://arxiv.org/abs/2203.15198
  date: '2022'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
Soft robots have drawn significant attention recently for their ability to achieve rich shapes when interacting with complex environments. However, their elasticity and flexibility compared to rigid robots also pose significant challenges for precise and robust shape control in real-time. Motivated by their potential to operate in highly-constrained environments, as in search-and-rescue operations, this work addresses these challenges of soft robots by developing a model-based full-shape controller, validated and demonstrated by experiments. A five-actuator planar soft robot was constructed with planar piezoelectric layers bonded to a steel foil substrate, enabling inchworm-like motion. The controller uses a soft-body continuous model for shape planning and control, given target shapes and/or environmental constraints, such as crawling under overhead barriers or "roof" safety lines. An approach to background model calibrations is developed to address deviations of actual robot shape due to material parameter variations and drift. Full experimental shape control and optimal movement under a roof safety line are demonstrated, where the robot maximizes its speed within the overhead constraint. The mean-squared error between the measured and target shapes improves from ~0.05 cm$^{2}$ without calibration to ~0.01 cm$^{2}$ with calibration. Simulation-based validation is also performed with various different roof shapes.

## 核心内容
Soft robots have drawn significant attention recently for their ability to achieve rich shapes when interacting with complex environments. However, their elasticity and flexibility compared to rigid robots also pose significant challenges for precise and robust shape control in real-time. Motivated by their potential to operate in highly-constrained environments, as in search-and-rescue operations, this work addresses these challenges of soft robots by developing a model-based full-shape controller, validated and demonstrated by experiments. A five-actuator planar soft robot was constructed with planar piezoelectric layers bonded to a steel foil substrate, enabling inchworm-like motion. The controller uses a soft-body continuous model for shape planning and control, given target shapes and/or environmental constraints, such as crawling under overhead barriers or "roof" safety lines. An approach to background model calibrations is developed to address deviations of actual robot shape due to material parameter variations and drift. Full experimental shape control and optimal movement under a roof safety line are demonstrated, where the robot maximizes its speed within the overhead constraint. The mean-squared error between the measured and target shapes improves from ~0.05 cm$^{2}$ without calibration to ~0.01 cm$^{2}$ with calibration. Simulation-based validation is also performed with various different roof shapes.

## 参考
- http://arxiv.org/abs/2203.15198v1

