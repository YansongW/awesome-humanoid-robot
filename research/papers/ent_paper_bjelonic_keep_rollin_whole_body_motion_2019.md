---
$id: ent_paper_bjelonic_keep_rollin_whole_body_motion_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Keep Rollin' – Whole-Body Motion Control and Planning for Wheeled Quadrupedal Robots
  zh: Keep Rollin'——轮腿四足机器人的全身运动控制与规划
  ko: Keep Rollin' – 바퀴 달린 사족 로봇의 전신 동작 제어 및 계획
summary:
  en: This paper presents an online zero-moment-point motion optimizer and a hierarchical whole-body controller that tightly
    integrate the nonholonomic rolling constraints of torque-controlled wheels on the quadrupedal robot ANYmal, enabling dynamic
    hybrid walking and driving up to 4 m/s with an 83% reduction in cost of transport compared to legged gaits.
  zh: 本文提出了一种在线零力矩点运动优化器与分层全身控制器，将ANYmal四足机器人上扭矩控制轮子的非完整滚动约束紧密集成，实现了动态混合行走与驱动，最高速度达4 m/s，运输成本相比纯步态降低83%。
  ko: 본 논문은 ANYmal 사족 로봇의 토크 제어 휠의 비홀onomic 롤링 구속 조건을 긴밀히 통합한 온라인 영점모멘트점 동작 최적화기와 계층적 전신 제어기를 제안하여, 최대 4 m/s의 동적 하이브리드 보행
    및 주행을 실현하고 사족 보행 대비 운송 비용을 83% 감소시켰다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1809.03557v2.
sources:
- id: src_001
  type: paper
  title: Keep Rollin' – Whole-Body Motion Control and Planning for Wheeled Quadrupedal Robots
  url: https://arxiv.org/abs/1809.03557
  date: '2019'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
We show dynamic locomotion strategies for wheeled quadrupedal robots, which combine the advantages of both walking and driving. The developed optimization framework tightly integrates the additional degrees of freedom introduced by the wheels. Our approach relies on a zero-moment point based motion optimization which continuously updates reference trajectories. The reference motions are tracked by a hierarchical whole-body controller which computes optimal generalized accelerations and contact forces by solving a sequence of prioritized tasks including the nonholonomic rolling constraints. Our approach has been tested on ANYmal, a quadrupedal robot that is fully torque-controlled including the non-steerable wheels attached to its legs. We conducted experiments on flat and inclined terrains as well as over steps, whereby we show that integrating the wheels into the motion control and planning framework results in intuitive motion trajectories, which enable more robust and dynamic locomotion compared to other wheeled-legged robots. Moreover, with a speed of 4 m/s and a reduction of the cost of transport by 83 % we prove the superiority of wheeled-legged robots compared to their legged counterparts.

## 核心内容
We show dynamic locomotion strategies for wheeled quadrupedal robots, which combine the advantages of both walking and driving. The developed optimization framework tightly integrates the additional degrees of freedom introduced by the wheels. Our approach relies on a zero-moment point based motion optimization which continuously updates reference trajectories. The reference motions are tracked by a hierarchical whole-body controller which computes optimal generalized accelerations and contact forces by solving a sequence of prioritized tasks including the nonholonomic rolling constraints. Our approach has been tested on ANYmal, a quadrupedal robot that is fully torque-controlled including the non-steerable wheels attached to its legs. We conducted experiments on flat and inclined terrains as well as over steps, whereby we show that integrating the wheels into the motion control and planning framework results in intuitive motion trajectories, which enable more robust and dynamic locomotion compared to other wheeled-legged robots. Moreover, with a speed of 4 m/s and a reduction of the cost of transport by 83 % we prove the superiority of wheeled-legged robots compared to their legged counterparts.

## 参考
- http://arxiv.org/abs/1809.03557v2

