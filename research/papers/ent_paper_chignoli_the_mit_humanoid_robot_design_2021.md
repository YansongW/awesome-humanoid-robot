---
$id: ent_paper_chignoli_the_mit_humanoid_robot_design_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'The MIT Humanoid Robot: Design, Motion Planning, and Control For Acrobatic Behaviors'
  zh: MIT人形机器人：面向杂技行为的设计、运动规划与控制
  ko: 'MIT 휴머노이드 로봇: 곡예 동작을 위한 설계, 운동 계획 및 제어'
summary:
  en: This paper presents the design, actuator-aware kino-dynamic planning, and landing control of the MIT Humanoid robot,
    demonstrating back flips, front flips, and spinning jumps in a realistic dynamics simulation that includes validated actuator
    and battery models.
  zh: Demonstrating acrobatic behavior of a humanoid robot such as flips and spinning jumps requires systematic approaches
    across hardware design, motion planning, and control. In this paper, we present a new humanoid robot design, an actuator-aware
    kino-dynamic motion planner, and a landing controller as part of a practical system design for highly dynamic motion control
    of the humanoid robot. To achieve the impulsive motions, we develop two new proprioceptive actuators and experimentally
    evaluate their performance using our custom-designed dynamometer. The actuator's torque, velocity, and power li
  ko: 본 논문은 MIT 휴머노이드 로봇의 설계, 액추에이터 인식 키노다이나믹 계획법 및 착륙 제어를 제시하며, 경험적으로 검증된 액추에이터 및 배터리 모델을 포함한 사실적인 동역학 시뮬레이션에서 백플립, 프론트플립,
    스핀 점프를 시연한다.
domains:
- 06_design_engineering
- 02_components
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
- system
tags:
- humanoid_robot
- acrobatic_behaviors
- proprioceptive_actuator
- kino_dynamic_planning
- actuator_aware_planning
- centroidal_dynamics
- model_predictive_control
- whole_body_impulse_control
- landing_control
- dynamic_simulation
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2104.09025v1.
sources:
- id: src_001
  type: paper
  title: 'The MIT Humanoid Robot: Design, Motion Planning, and Control For Acrobatic Behaviors'
  url: https://arxiv.org/abs/2104.09025
  date: '2021'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## 概述
Demonstrating acrobatic behavior of a humanoid robot such as flips and spinning jumps requires systematic approaches across hardware design, motion planning, and control. In this paper, we present a new humanoid robot design, an actuator-aware kino-dynamic motion planner, and a landing controller as part of a practical system design for highly dynamic motion control of the humanoid robot. To achieve the impulsive motions, we develop two new proprioceptive actuators and experimentally evaluate their performance using our custom-designed dynamometer. The actuator's torque, velocity, and power limits are reflected in our kino-dynamic motion planner by approximating the configuration-dependent reaction force limits and in our dynamics simulator by including actuator dynamics along with the robot's full-body dynamics. For the landing control, we effectively integrate model-predictive control and whole-body impulse control by connecting them in a dynamically consistent way to accomplish both the long-time horizon optimal control and high-bandwidth full-body dynamics-based feedback. Actuators' torque output over the entire motion are validated based on the velocity-torque model including battery voltage droop and back-EMF voltage. With the carefully designed hardware and control framework, we successfully demonstrate dynamic behaviors such as back flips, front flips, and spinning jumps in our realistic dynamics simulation.

## 核心内容
Demonstrating acrobatic behavior of a humanoid robot such as flips and spinning jumps requires systematic approaches across hardware design, motion planning, and control. In this paper, we present a new humanoid robot design, an actuator-aware kino-dynamic motion planner, and a landing controller as part of a practical system design for highly dynamic motion control of the humanoid robot. To achieve the impulsive motions, we develop two new proprioceptive actuators and experimentally evaluate their performance using our custom-designed dynamometer. The actuator's torque, velocity, and power limits are reflected in our kino-dynamic motion planner by approximating the configuration-dependent reaction force limits and in our dynamics simulator by including actuator dynamics along with the robot's full-body dynamics. For the landing control, we effectively integrate model-predictive control and whole-body impulse control by connecting them in a dynamically consistent way to accomplish both the long-time horizon optimal control and high-bandwidth full-body dynamics-based feedback. Actuators' torque output over the entire motion are validated based on the velocity-torque model including battery voltage droop and back-EMF voltage. With the carefully designed hardware and control framework, we successfully demonstrate dynamic behaviors such as back flips, front flips, and spinning jumps in our realistic dynamics simulation.

## 参考
- http://arxiv.org/abs/2104.09025v1


