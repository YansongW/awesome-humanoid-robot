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

## Overview
Soft robots have drawn significant attention recently for their ability to achieve rich shapes when interacting with complex environments. However, their elasticity and flexibility compared to rigid robots also pose significant challenges for precise and robust shape control in real-time. Motivated by their potential to operate in highly-constrained environments, as in search-and-rescue operations, this work addresses these challenges of soft robots by developing a model-based full-shape controller, validated and demonstrated by experiments. A five-actuator planar soft robot was constructed with planar piezoelectric layers bonded to a steel foil substrate, enabling inchworm-like motion. The controller uses a soft-body continuous model for shape planning and control, given target shapes and/or environmental constraints, such as crawling under overhead barriers or "roof" safety lines. An approach to background model calibrations is developed to address deviations of actual robot shape due to material parameter variations and drift. Full experimental shape control and optimal movement under a roof safety line are demonstrated, where the robot maximizes its speed within the overhead constraint. The mean-squared error between the measured and target shapes improves from ~0.05 cm$^{2}$ without calibration to ~0.01 cm$^{2}$ with calibration. Simulation-based validation is also performed with various different roof shapes.

## Content
Soft robots have drawn significant attention recently for their ability to achieve rich shapes when interacting with complex environments. However, their elasticity and flexibility compared to rigid robots also pose significant challenges for precise and robust shape control in real-time. Motivated by their potential to operate in highly-constrained environments, as in search-and-rescue operations, this work addresses these challenges of soft robots by developing a model-based full-shape controller, validated and demonstrated by experiments. A five-actuator planar soft robot was constructed with planar piezoelectric layers bonded to a steel foil substrate, enabling inchworm-like motion. The controller uses a soft-body continuous model for shape planning and control, given target shapes and/or environmental constraints, such as crawling under overhead barriers or "roof" safety lines. An approach to background model calibrations is developed to address deviations of actual robot shape due to material parameter variations and drift. Full experimental shape control and optimal movement under a roof safety line are demonstrated, where the robot maximizes its speed within the overhead constraint. The mean-squared error between the measured and target shapes improves from ~0.05 cm$^{2}$ without calibration to ~0.01 cm$^{2}$ with calibration. Simulation-based validation is also performed with various different roof shapes.

## 개요
소프트 로봇은 복잡한 환경과 상호작용할 때 다양한 형상을 구현할 수 있는 능력으로 최근 큰 주목을 받고 있습니다. 그러나 강체 로봇에 비해 탄성과 유연성이 뛰어나기 때문에 실시간으로 정밀하고 강건한 형상 제어에 상당한 도전 과제가 있습니다. 수색 및 구조 작업과 같이 고도로 제약된 환경에서 작동할 수 있는 잠재력에 동기 부여되어, 본 연구는 모델 기반 전 형상 제어기를 개발하여 소프트 로봇의 이러한 도전 과제를 해결하고, 실험을 통해 검증 및 시연합니다. 강철 호일 기판에 평면 압전 층을 접합하여 다섯 개의 액추에이터를 가진 평면 소프트 로봇을 제작하였으며, 이는 애벌레와 같은 움직임을 가능하게 합니다. 제어기는 목표 형상 및/또는 환경적 제약(예: 머리 위 장벽 또는 "지붕" 안전선 아래를 기어가는 경우)이 주어졌을 때 형상 계획 및 제어를 위해 소프트 바디 연속체 모델을 사용합니다. 재료 매개변수 변동 및 드리프트로 인한 실제 로봇 형상의 편차를 해결하기 위해 배경 모델 보정 접근법이 개발되었습니다. 지붕 안전선 아래에서의 완전한 실험적 형상 제어 및 최적 이동이 시연되었으며, 로봇은 머리 위 제약 조건 내에서 속도를 최대화합니다. 측정된 형상과 목표 형상 간의 평균 제곱 오차는 보정 없이 약 0.05 cm$^{2}$에서 보정 후 약 0.01 cm$^{2}$로 개선됩니다. 다양한 지붕 형상을 사용한 시뮬레이션 기반 검증도 수행되었습니다.

## 핵심 내용
소프트 로봇은 복잡한 환경과 상호작용할 때 다양한 형상을 구현할 수 있는 능력으로 최근 큰 주목을 받고 있습니다. 그러나 강체 로봇에 비해 탄성과 유연성이 뛰어나기 때문에 실시간으로 정밀하고 강건한 형상 제어에 상당한 도전 과제가 있습니다. 수색 및 구조 작업과 같이 고도로 제약된 환경에서 작동할 수 있는 잠재력에 동기 부여되어, 본 연구는 모델 기반 전 형상 제어기를 개발하여 소프트 로봇의 이러한 도전 과제를 해결하고, 실험을 통해 검증 및 시연합니다. 강철 호일 기판에 평면 압전 층을 접합하여 다섯 개의 액추에이터를 가진 평면 소프트 로봇을 제작하였으며, 이는 애벌레와 같은 움직임을 가능하게 합니다. 제어기는 목표 형상 및/또는 환경적 제약(예: 머리 위 장벽 또는 "지붕" 안전선 아래를 기어가는 경우)이 주어졌을 때 형상 계획 및 제어를 위해 소프트 바디 연속체 모델을 사용합니다. 재료 매개변수 변동 및 드리프트로 인한 실제 로봇 형상의 편차를 해결하기 위해 배경 모델 보정 접근법이 개발되었습니다. 지붕 안전선 아래에서의 완전한 실험적 형상 제어 및 최적 이동이 시연되었으며, 로봇은 머리 위 제약 조건 내에서 속도를 최대화합니다. 측정된 형상과 목표 형상 간의 평균 제곱 오차는 보정 없이 약 0.05 cm$^{2}$에서 보정 후 약 0.01 cm$^{2}$로 개선됩니다. 다양한 지붕 형상을 사용한 시뮬레이션 기반 검증도 수행되었습니다.
