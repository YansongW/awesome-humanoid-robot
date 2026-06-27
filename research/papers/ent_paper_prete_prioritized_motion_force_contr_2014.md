---
$id: ent_paper_prete_prioritized_motion_force_contr_2014
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Prioritized Motion-Force Control of Constrained Fully-Actuated Robots: "Task
    Space Inverse Dynamics"'
  zh: 受约束全驱动机器人的优先级运动-力控制：“任务空间逆动力学”
  ko: '구속된 완전 구동 로봇의 우선순위 운동-힘 제어: “작업 공간 역역학”'
summary:
  en: Introduces Task Space Inverse Dynamics (TSID), an optimal whole-body torque
    control framework for fully-actuated robots that decouples acceleration-level
    inverse kinematics from joint-space inverse dynamics to support prioritized motion/force
    control with soft and rigid contacts.
  zh: 提出任务空间逆动力学（TSID），一种面向全驱动机器人的最优全身力矩控制框架，通过将加速度级逆运动学与关节空间逆动力学解耦，支持柔性和刚性接触下的优先级运动/力控制。
  ko: 가속도 수준 역기구학과 관절 공간 역역학을 분리하여 부드러운 접촉과 경성 접촉이 있는 우선순위 운동/힘 제어를 지원하는 완전 구동 로봇을
    위한 최적 전신 토크 제어 프레임워크인 작업 공간 역역학(TSID)을 제안한다.
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
- whole_body_control
- task_space_inverse_dynamics
- operational_space_inverse_dynamics
- inverse_dynamics
- motion_force_control
- prioritized_control
- contact_dynamics
- fully_actuated_robots
- torque_control
- humanoid_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata; exact in-paper citations and section
    numbers require human review against the full text before verification.
sources:
- id: src_001
  type: paper
  title: 'Prioritized Motion-Force Control of Constrained Fully-Actuated Robots: "Task
    Space Inverse Dynamics"'
  url: https://arxiv.org/abs/1410.3863
  date: '2014'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper proposes Task Space Inverse Dynamics (TSID), a control framework for prioritized multi-task motion and force control of fully-actuated robots. The core idea is that, for fully-actuated systems, computing operational-space inverse dynamics is equivalent to solving acceleration-level inverse kinematics and then joint-space inverse dynamics. By decoupling kinematics and dynamics, TSID can efficiently compute optimal joint torques using recursive algorithms while handling both motion and force tasks, soft and rigid contacts, and free or constrained robots.

The authors position TSID against existing approaches: some prior frameworks are not optimal for secondary tasks, others are optimal but kinematic and therefore ignore dynamics and force control, and still others are optimal and force-aware but computationally slower. TSID is claimed to combine optimality, force control, and O(n) efficiency. Simulation tests on a 23-degree-of-freedom humanoid compare TSID with the Unifying Framework and the Whole-Body Control Framework, reportedly showing improvements in both optimality and computational efficiency.

## Key Contributions

- Proposed the Task Space Inverse Dynamics (TSID) framework for prioritized multi-task motion/force control of fully-actuated robots.
- Proved that operational-space inverse dynamics is equivalent to acceleration-level inverse kinematics followed by joint-space inverse dynamics for fully-actuated robots.
- Achieved both optimality and O(n) computational efficiency using the Recursive Newton-Euler Algorithm.
- Supported soft/rigid contacts and free/constrained robots within a unified formulation.
- Validated the framework through simulation comparisons with the Unifying Framework and Whole-Body Control Framework on a 23-DoF humanoid.

## Relevance to Humanoid Robotics

TSID is directly relevant to humanoid robotics because it provides an efficient, optimal whole-body torque controller that can manage multiple prioritized tasks simultaneously while respecting contact forces. Humanoid robots must coordinate many degrees of freedom, maintain balance, and interact with environments through contacts, all under real-time constraints. By decoupling kinematic prioritization from inverse dynamics and achieving linear-time complexity, TSID addresses key computational and control challenges for fully-actuated humanoid platforms.

However, the paper explicitly restricts its scope to fully-actuated robots and does not treat floating-base or underactuated systems, which are common in humanoid locomotion. It also neglects inequality constraints such as joint limits and torque bounds, and it only guarantees instantaneous optimality rather than planning over a horizon. These limitations mean that, while foundational for torque-level whole-body control, TSID may require extensions for deployment on typical free-floating humanoids.
