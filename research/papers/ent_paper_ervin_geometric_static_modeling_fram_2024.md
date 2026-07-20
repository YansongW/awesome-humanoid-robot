---
$id: ent_paper_ervin_geometric_static_modeling_fram_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Geometric Static Modeling Framework for Piecewise-Continuous Curved-Link Multi
    Point-of-Contact Tensegrity Robots
  zh: 分段连续曲杆多接触点张拉整体机器人的几何静态建模框架
  ko: 조각별 연속 곡선 링크 다중 접촉점 텐서그리티 로봇의 기하학적 정적 모델링 프레임워크
summary:
  en: Derives closed-form geometric static models for the TeXploR tensegrity robot,
    which uses two semi-circular curved links and two changing ground contacts, and
    validates the models on a tetherless prototype with a mean absolute error of 4.36°.
  zh: 为使用两个半圆形曲杆和两个变化地面接触点的 TeXploR 张拉整体机器人推导闭式几何静态模型，并在无绳样机上验证，平均绝对误差为 4.36°。
  ko: 두 개의 반원형 곡선 링크와 두 개의 변화하는 지면 접촉점을 갖는 TeXploR 텐서그리티 로봇에 대해 폐형 기하학적 정적 모델을 도출하고,
    테더리스 프로토타입에서 평균 절대 오차 4.36°로 검증함.
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
  notes: AI-extracted from the paper abstract and user-provided metadata; full text
    was not independently read. Requires human review before full verification.
sources:
- id: src_001
  type: paper
  title: Geometric Static Modeling Framework for Piecewise-Continuous Curved-Link
    Multi Point-of-Contact Tensegrity Robots
  url: https://arxiv.org/abs/2407.01865
  date: '2024'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---

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
