---
$id: ent_paper_zheng_piezoelectric_soft_robot_inchw_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Piezoelectric Soft Robot Inchworm Motion by Tuning Ground Friction through
    Robot Shape: Quasi-Static Modeling and Experimental Validation'
  zh: 通过机器人形状调节地面摩擦的压电软体机器人尺蠖运动：准静态建模与实验验证
  ko: '로봇 형상을 통한 지면 마찰 튜닝을 이용한 압전 소프트 로봇 인치웜 운동: 준정적 모델링 및 실험적 검증'
summary:
  en: Zheng et al. present a sub-millimeter-thick soft robot driven by five coordinated
    piezoelectric actuators on a steel foil substrate, using shape-controlled ground
    friction to achieve bidirectional inchworm crawling, and validate a gravity-inclusive
    Euler-Bernoulli quasi-static model against experiments.
  zh: Zheng 等人展示了一种厚度不足 0.5 毫米的软体机器人，该机器人在钢箔基底上集成五个压电执行器，通过形状控制地面摩擦实现双向尺蠖爬行，并验证了包含重力的欧拉-伯努利准静态模型。
  ko: Zheng 등은 강박 기판 위에 5개의 압전 액추에이터를 조화롭게 구동하는 수백 마이크로미터 두께의 소프트 로봇을 제안하고, 형상에 의한
    지면 마찰 제어로 양방향 인치웜 이동을 구현하며 중력을 포함한 Euler-Bernoulli 준정적 모델을 실험으로 검증하였다.
domains:
- 02_components
- 06_design_engineering
- 03_manufacturing_processes
layers:
- midstream
- upstream
functional_roles:
- knowledge
tags:
- piezoelectric_actuator
- pzt
- soft_robot
- inchworm_locomotion
- friction_tuning
- thin_film
- quasi_static_modeling
- ground_contact_modeling
- steel_foil
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from metadata and abstract; full-text review is needed to confirm
    section-level citations and exact numerical claims.
sources:
- id: src_001
  type: paper
  title: 'Piezoelectric Soft Robot Inchworm Motion by Tuning Ground Friction through
    Robot Shape: Quasi-Static Modeling and Experimental Validation'
  url: https://arxiv.org/abs/2111.00944
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

The authors build an electrically driven soft robot less than 0.5 mm thick by laminating five independent piezoelectric actuators onto a common steel foil. By coordinating the actuators, the robot changes its curvature, redistributes ground contact forces, and creates static-friction asymmetry between its two ends. This friction asymmetry lets one end anchor to the ground while the rest of the body expands or contracts, producing inchworm-inspired crawling.

A complete quasi-static analytical model is derived using Euler-Bernoulli beam theory and includes gravitational loading and ground-contact forces. The model predicts robot shape, normal-force distribution, and resulting displacement without fitting parameters. After validating the model experimentally, the authors sequence the five actuators collectively to demonstrate forward and backward inchworm motion.

The work also reports a scaling analysis and shows that adding end masses can increase friction asymmetry from roughly 30% to 70%, offering a route to smaller and faster piezoelectric soft robots.

## Key Contributions

- A shape-based friction-tuning mechanism that anchors one end of the robot by increasing ground contact force while the other end slides.
- A first-principle quasi-static soft-body model including gravity and ground-contact forces, validated against experiments without fitting parameters.
- Experimental demonstration of bidirectional inchworm motion and scaling analysis for smaller/faster piezoelectric soft robots.
- Analysis showing that added end masses can boost friction asymmetry from ~30% to ~70%.

## Relevance to Humanoid Robotics

Although the prototype is not a humanoid, its thin-film piezoelectric lamination, scalable fabrication, and integrated power/control electronics roadmap are relevant to low-profile, lightweight actuation modules. These modules could be adapted for humanoid robot joints, flexible skins, or auxiliary locomotion systems where compact, compliant actuation is required.
