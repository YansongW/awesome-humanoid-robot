---
$id: ent_paper_ervin_geometric_static_modeling_fram_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Geometric Static Modeling Framework for Piecewise-Continuous Curved-Link Multi Point-of-Contact Tensegrity Robots
  zh: 分段连续曲杆多接触点张拉整体机器人的几何静态建模框架
  ko: 조각별 연속 곡선 링크 다중 접촉점 텐서그리티 로봇의 기하학적 정적 모델링 프레임워크
summary:
  en: Derives closed-form geometric static models for the TeXploR tensegrity robot, which uses two semi-circular curved links
    and two changing ground contacts, and validates the models on a tetherless prototype with a mean absolute error of 4.36°.
  zh: 本文为TeXploR张拉整体机器人推导了闭式几何静力学模型，该机器人采用两个半圆形弯曲连杆和两个可变地面接触点。通过无系绳原型验证，模型平均绝对误差为4.36°。
  ko: 두 개의 반원형 곡선 링크와 두 개의 변화하는 지면 접촉점을 갖는 TeXploR 텐서그리티 로봇에 대해 폐형 기하학적 정적 모델을 도출하고, 테더리스 프로토타입에서 평균 절대 오차 4.36°로 검증함.
domains:
- 06_design_engineering
- 02_components
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- tensegrity
- curved_link
- rolling_robot
- geometric_modeling
- multi_contact
- static_equilibrium
- lie_group_kinematics
- compliant_structure
- closed_form_solution
- texplor
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: AI-extracted from the paper abstract and user-provided metadata; full text was not independently read. Requires human
    review before full verification. [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Geometric Static Modeling Framework for Piecewise-Continuous Curved-Link Multi Point-of-Contact Tensegrity Robots
  url: https://arxiv.org/abs/2407.01865
  date: '2024'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---
## 概述
该研究针对分段连续弯曲连杆多接触点张拉整体机器人，提出了一个几何静力学建模框架。以TeXploR机器人为对象，利用其半圆形弯曲连杆和可变地面接触点的结构特性，推导出闭式静力学模型。通过无系绳原型实验验证，模型预测与实测结果的平均绝对误差仅为4.36°，证明了该框架的有效性。

## 核心内容
### 方法
- 针对TeXploR张拉整体机器人，其结构包含两个半圆形弯曲连杆和两个可变地面接触点。
- 基于几何约束与静力平衡条件，推导出闭式解析模型，无需迭代求解。

### 实验设置
- 使用无系绳原型进行验证，测量机器人姿态与模型预测值对比。
- 评估指标为平均绝对误差（MAE）。

### 关键结果
- 模型预测与实测姿态的平均绝对误差为4.36°，验证了框架的准确性。
- 该闭式模型可高效用于实时控制与运动规划。

### 结论
- 提出的几何静力学建模框架适用于分段连续弯曲连杆多接触点张拉整体机器人，为类似结构提供了通用建模方法。

## Overview


## Overview
This paper studies the Tensegrity eXploratory Robot (TeXploR), a rolling tensegrity system made of two semi-circular curved links connected by twelve prestressed cables and actuated by internal masses that shift along each link. Its unusual geometry creates piecewise-continuous contacts with the ground and produces a four-state hybrid rolling behavior, making conventional spherical-tensegrity models insufficient. The authors develop a geometric static model using Lie-group kinematics and holonomic constraints to obtain closed-form equilibrium solutions for all four hybrid states, without requiring numerical exploration. A tetherless physical prototype built from tough PLA links, Delrin sliders, GT2 timing belts, NEMA17 stepper motors, an Arduino Nano33 IoT, and a LiPo battery is used to validate the MATLAB simulations.

## Key Contributions
- First geometric and kinematic modeling of a non-spherical two-point-of-contact rolling system.
- Closed-form static equilibrium solutions for all four hybrid states without numerical exploration.
- Experimental validation on a tetherless TeXploR prototype with a mean absolute error of 4.36°.
- Generalizable framework adaptable to different curved-link tensegrity morphologies, including variations in shape, number of links, and arc length.

## Relevance to Humanoid Robotics
Although TeXploR is a rolling tensegrity platform rather than a bipedal humanoid, the modeling advances are directly useful for compliant humanoid subsystems. The closed-form multi-contact equilibrium analysis and geometric treatment of cable-driven, curved compliant links can inform the design of lightweight impact-resistant joints, end effectors, and deployable limbs in future humanoids. The work also demonstrates how to handle hybrid contact-state transitions through internal mass redistribution, a problem shared by humanoid balance and foot-roll control.

## References
- [Geometric Static Modeling Framework for Piecewise-Continuous Curved-Link Multi Point-of-Contact Tensegrity Robots](https://arxiv.org/abs/2407.01865) (accessed 2026-07-01)

## 개요
본 연구는 분절 연속 굽힘 링크 다중 접촉점 텐세그리티 로봇을 대상으로 기하학적 정역학 모델링 프레임워크를 제안한다. TeXploR 로봇을 대상으로, 반원형 굽힘 링크와 가변 지면 접촉점의 구조적 특성을 활용하여 폐쇄형 정역학 모델을 유도하였다. 무계류 프로토타입 실험을 통해 검증한 결과, 모델 예측과 실측 결과의 평균 절대 오차가 4.36°에 불과하여 해당 프레임워크의 유효성을 입증하였다.

## 핵심 내용
### 방법
- TeXploR 텐세그리티 로봇을 대상으로, 그 구조는 두 개의 반원형 굽힘 링크와 두 개의 가변 지면 접촉점을 포함한다.
- 기하학적 구속 조건과 정역학적 평형 조건을 기반으로 반복 계산 없이 폐쇄형 해석 모델을 유도하였다.

### 실험 설정
- 무계류 프로토타입을 사용하여 검증을 수행하고, 로봇 자세를 측정하여 모델 예측값과 비교하였다.
- 평가 지표는 평균 절대 오차(MAE)이다.

### 주요 결과
- 모델 예측과 실측 자세의 평균 절대 오차는 4.36°로, 프레임워크의 정확성을 입증하였다.
- 해당 폐쇄형 모델은 실시간 제어 및 운동 계획에 효율적으로 사용될 수 있다.

### 결론
- 제안된 기하학적 정역학 모델링 프레임워크는 분절 연속 굽힘 링크 다중 접촉점 텐세그리티 로봇에 적용 가능하며, 유사한 구조에 대한 일반적인 모델링 방법을 제공한다.
