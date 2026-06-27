---
$id: ent_paper_bjelonic_keep_rollin_whole_body_motion_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Keep Rollin' – Whole-Body Motion Control and Planning for Wheeled Quadrupedal
    Robots
  zh: Keep Rollin'——轮腿四足机器人的全身运动控制与规划
  ko: Keep Rollin' – 바퀴 달린 사족 로봇의 전신 동작 제어 및 계획
summary:
  en: This paper presents an online zero-moment-point motion optimizer and a hierarchical
    whole-body controller that tightly integrate the nonholonomic rolling constraints
    of torque-controlled wheels on the quadrupedal robot ANYmal, enabling dynamic
    hybrid walking and driving up to 4 m/s with an 83% reduction in cost of transport
    compared to legged gaits.
  zh: 本文提出了一种在线零力矩点运动优化器与分层全身控制器，将ANYmal四足机器人上扭矩控制轮子的非完整滚动约束紧密集成，实现了动态混合行走与驱动，最高速度达4
    m/s，运输成本相比纯步态降低83%。
  ko: 본 논문은 ANYmal 사족 로봇의 토크 제어 휠의 비홀onomic 롤링 구속 조건을 긴밀히 통합한 온라인 영점모멘트점 동작 최적화기와
    계층적 전신 제어기를 제안하여, 최대 4 m/s의 동적 하이브리드 보행 및 주행을 실현하고 사족 보행 대비 운송 비용을 83% 감소시켰다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- wheeled_quadruped
- whole_body_control
- motion_optimization
- zmp_based_planning
- hierarchical_controller
- torque_control
- nonholonomic_constraints
- hybrid_locomotion
- anymal
- receding_horizon_planning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from metadata and abstract; full-text verification pending human
    review.
sources:
- id: src_001
  type: paper
  title: Keep Rollin' – Whole-Body Motion Control and Planning for Wheeled Quadrupedal
    Robots
  url: https://arxiv.org/abs/1809.03557
  date: '2019'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

The paper introduces a unified control and planning framework for wheeled quadrupedal robots, aiming to combine the efficiency of driving with the versatility of legged locomotion. The authors develop an online zero-moment point (ZMP) based motion optimizer that continuously updates center-of-mass and wheel reference trajectories in a receding-horizon fashion. These references are then tracked by a hierarchical whole-body controller that solves prioritized quadratic programs to compute generalized accelerations and contact forces while explicitly enforcing the nonholonomic rolling constraints of the wheels.

The implementation is carried out on ANYmal, a fully torque-controlled quadrupedal robot with non-steerable wheels attached to its legs. Because the wheels are torque-controlled, the controller can exploit wheel degrees of freedom together with the leg joints, producing intuitive trajectories that improve robustness and dynamic performance. The system is evaluated on flat and inclined terrains as well as over steps, demonstrating that the integrated approach outperforms legged counterparts in speed and energy efficiency.

The authors report a maximum speed of 4 m/s and an 83% reduction in the cost of transport relative to legged gaits, underscoring the practical benefits of wheeled-legged locomotion when the wheels are tightly integrated into planning and control.

## Key Contributions

- First demonstration of dynamic hybrid locomotion over flat, inclined, and rough terrain for a wheeled quadrupedal robot.
- Online ZMP-based motion optimization tightly integrated with wheel degrees of freedom.
- Hierarchical whole-body controller that handles nonholonomic rolling constraints and torque control of all joints including wheels.
- Unified driving and walking framework without changing underlying dynamics or balance principles.
- Experimental validation on ANYmal achieving 4 m/s speed and 83% cost-of-transport reduction versus legged gaits.

## Relevance to Humanoid Robotics

Although the experiments are performed on a quadruped, the methodological contributions are directly relevant to humanoid robotics. The combination of whole-body trajectory optimization, hierarchical task-space control, and explicit handling of nonholonomic constraints provides a transferable foundation for humanoid platforms equipped with wheeled appendages or mobile bases. Efficient hybrid locomotion is especially attractive for industrial humanoids that must cover large distances quickly while retaining the ability to step over obstacles.

The paper also illustrates the importance of torque-controlled end-effectors and receding-horizon planning in dynamic legged systems, both of which are central to current humanoid locomotion research. Its limitations—such as decoupled COM and foothold optimization and non-steerable wheels—highlight open problems that humanoid implementations would need to address.
