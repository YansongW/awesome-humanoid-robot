---
$id: ent_paper_chignoli_the_mit_humanoid_robot_design_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'The MIT Humanoid Robot: Design, Motion Planning, and Control For Acrobatic
    Behaviors'
  zh: MIT人形机器人：面向杂技行为的设计、运动规划与控制
  ko: 'MIT 휴머노이드 로봇: 곡예 동작을 위한 설계, 운동 계획 및 제어'
summary:
  en: This paper presents the design, actuator-aware kino-dynamic planning, and landing
    control of the MIT Humanoid robot, demonstrating back flips, front flips, and
    spinning jumps in a realistic dynamics simulation that includes validated actuator
    and battery models.
  zh: 本文介绍了MIT人形机器人的设计、执行器感知运动动力学规划与着陆控制，并在包含经验验证执行器与电池模型的真实感动力学仿真中展示了后空翻、前空翻和旋转跳跃。
  ko: 본 논문은 MIT 휴머노이드 로봇의 설계, 액추에이터 인식 키노다이나믹 계획법 및 착륙 제어를 제시하며, 경험적으로 검증된 액추에이터 및
    배터리 모델을 포함한 사실적인 동역학 시뮬레이션에서 백플립, 프론트플립, 스핀 점프를 시연한다.
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
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from arXiv full text (ar5iv HTML) and provided metadata; requires
    human review before final verification.
sources:
- id: src_001
  type: paper
  title: 'The MIT Humanoid Robot: Design, Motion Planning, and Control For Acrobatic
    Behaviors'
  url: https://arxiv.org/abs/2104.09025
  date: '2021'
  accessed_at: '2026-06-26'
---


## Overview

This 2021 arXiv paper by Chignoli, Kim, Stanger-Jones, and Sangbae Kim presents the MIT Humanoid, a ~0.7 m, ~21 kg humanoid with 5-DoF legs and 3-DoF arms, designed for highly dynamic acrobatic behaviors. The work combines hardware design, an actuator-aware kino-dynamic planner (AAKD), and a hierarchical landing controller. It applies the proprioceptive actuator design principles of the MIT Cheetah robots to a humanoid platform and introduces two custom actuator modules, U10 and U12, whose torque-speed performance is validated with a custom dynamometer using a Futek TRS300 torque sensor.

The AAKD planner optimizes centroidal dynamics and joint kinematics while enforcing configuration-dependent actuator torque-speed limits through an approximate, linearized contact-Jacobian mapping from ground reaction forces to joint torques. This enables feasible takeoff trajectories for back flips, front flips, and spinning jumps. For landing, a quadratic-programming-based model-predictive controller plans reaction force profiles over a 1.5 s horizon using a simplified lumped-mass model, and whole-body impulse control (WBIC) tracks the planned motion with high-bandwidth full-body feedback, prioritizing body orientation over centroidal momentum to maintain dynamical consistency.

All motions are demonstrated in a custom dynamics simulator that includes rotor inertia, actuator torque-speed curves, and battery voltage droop. The authors verify that simulated joint torques remain within empirically validated actuator limits throughout the maneuvers, though they emphasize that the demonstrations are simulation-only and depend on accurate inertial, contact, and state-estimation models for hardware transfer.

## Key Contributions

- Design of the MIT Humanoid robot, applying MIT Cheetah proprioceptive-actuator principles to a humanoid platform.
- Development and dynamometer validation of the U10 and U12 proprioceptive actuator modules.
- Actuator-aware kino-dynamic planner (AAKD) that incorporates configuration-dependent torque-speed limits into centroidal-dynamics trajectory optimization.
- Hierarchical landing controller that dynamically consistently integrates model-predictive control (MPC) and whole-body impulse control (WBIC) for stable landing.
- Realistic dynamics-simulation demonstrations of back flips, front flips, and spinning jumps with verified actuator limits including battery voltage droop and back-EMF effects.

## Relevance to Humanoid Robotics

The work is relevant to humanoid robotics because it extends high-performance proprioceptive actuation, impact-robust hardware design, and whole-body dynamic planning from quadrupeds to bipeds, providing a practical foundation for agile, acrobatic humanoid mobility. By modeling and validating actuator limits, battery droop, and rotor inertia in simulation, it bridges the gap between theoretical motion planning and feasible hardware execution for highly dynamic maneuvers.

The control architecture—combining actuator-aware planning with a long-horizon MPC and high-bandwidth WBIC—offers a template for dynamic behaviors beyond walking, such as parkour or fall recovery. However, the absence of hardware experiments and the reliance on small-angle and single-axis approximations in the landing MPC mean the findings should be treated as a validated simulation study rather than a deployed system.
