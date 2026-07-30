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
  zh: 本文提出一种针对轮式四足机器人ANYmal的在线零力矩点运动优化器与分层全身控制器，通过紧密集成非完整滚动约束，实现了动态混合行走与驱动，最高速度达4 m/s，运输成本较纯腿式步态降低83%。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1809.03557v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
该研究开发了结合行走与驱动优势的轮式四足机器人动态运动策略。其优化框架将车轮引入的额外自由度紧密整合，基于零力矩点的运动优化器持续更新参考轨迹，并由分层全身控制器通过求解包含非完整滚动约束的优先级任务序列，计算最优广义加速度与接触力。在完全力矩控制的ANYmal机器人（腿部安装非转向轮）上进行的实验表明，该方法在平坦、倾斜地形及台阶上均能生成直观的运动轨迹，相比其他轮腿式机器人实现更鲁棒、更动态的运动，并以4 m/s速度和83%的运输成本降幅证明了轮腿式机器人的优越性。

## 核心内容
### 方法架构
- **运动优化器**：基于零力矩点（ZMP）的在线优化框架，持续更新全身参考轨迹，将车轮的非完整滚动约束作为关键优化条件。
- **分层全身控制器**：通过求解优先级任务序列（包括非完整滚动约束、身体姿态、足端力分配等），计算最优广义加速度与接触力，实现精确轨迹跟踪。

### 实验设置
- **平台**：ANYmal四足机器人，所有关节均为力矩控制，腿部末端安装无转向功能的驱动轮。
- **测试场景**：平坦地面、倾斜地形（坡度未明确）、台阶跨越。

### 关键结果
- **速度**：最高达4 m/s，显著高于纯腿式步态。
- **能效**：运输成本（Cost of Transport）较纯腿式步态降低83%。
- **鲁棒性**：在复杂地形中生成更直观的运动轨迹，动态稳定性优于其他轮腿式机器人（如未具名的对比系统）。

### 结论
将车轮滚动约束紧密集成到运动控制与规划框架中，可充分发挥轮腿式机器人的混合运动优势，在速度与能效上均超越传统腿式机器人。

## Overview
We show dynamic locomotion strategies for wheeled quadrupedal robots, which combine the advantages of both walking and driving. The developed optimization framework tightly integrates the additional degrees of freedom introduced by the wheels. Our approach relies on a zero-moment point based motion optimization which continuously updates reference trajectories. The reference motions are tracked by a hierarchical whole-body controller which computes optimal generalized accelerations and contact forces by solving a sequence of prioritized tasks including the nonholonomic rolling constraints. Our approach has been tested on ANYmal, a quadrupedal robot that is fully torque-controlled including the non-steerable wheels attached to its legs. We conducted experiments on flat and inclined terrains as well as over steps, whereby we show that integrating the wheels into the motion control and planning framework results in intuitive motion trajectories, which enable more robust and dynamic locomotion compared to other wheeled-legged robots. Moreover, with a speed of 4 m/s and a reduction of the cost of transport by 83 % we prove the superiority of wheeled-legged robots compared to their legged counterparts.

## 개요
바퀴 달린 사족 로봇을 위한 동적 보행 전략을 제시하며, 이는 보행과 주행의 장점을 결합합니다. 개발된 최적화 프레임워크는 바퀴로 인해 추가된 자유도를 긴밀하게 통합합니다. 우리의 접근 방식은 영점 모멘트 기반 동작 최적화에 의존하며, 이는 참조 궤적을 지속적으로 업데이트합니다. 참조 동작은 계층적 전신 제어기에 의해 추적되며, 이는 비홀로노믹 구름 제약 조건을 포함한 우선순위가 지정된 일련의 작업을 해결하여 최적의 일반화 가속도와 접촉력을 계산합니다. 우리의 접근 방식은 다리에 부착된 조향 불가능한 바퀴를 포함하여 완전히 토크 제어되는 사족 로봇 ANYmal에서 테스트되었습니다. 평지와 경사 지형, 그리고 단차를 넘는 실험을 수행했으며, 바퀴를 동작 제어 및 계획 프레임워크에 통합하면 직관적인 동작 궤적이 생성되어 다른 바퀴 달린 보행 로봇에 비해 더 견고하고 동적인 보행이 가능함을 보여줍니다. 또한, 4m/s의 속도와 83%의 운송 비용 절감을 통해 바퀴 달린 보행 로봇이 순수 보행 로봇보다 우수함을 입증합니다.

## 핵심 내용
바퀴 달린 사족 로봇을 위한 동적 보행 전략을 제시하며, 이는 보행과 주행의 장점을 결합합니다. 개발된 최적화 프레임워크는 바퀴로 인해 추가된 자유도를 긴밀하게 통합합니다. 우리의 접근 방식은 영점 모멘트 기반 동작 최적화에 의존하며, 이는 참조 궤적을 지속적으로 업데이트합니다. 참조 동작은 계층적 전신 제어기에 의해 추적되며, 이는 비홀로노믹 구름 제약 조건을 포함한 우선순위가 지정된 일련의 작업을 해결하여 최적의 일반화 가속도와 접촉력을 계산합니다. 우리의 접근 방식은 다리에 부착된 조향 불가능한 바퀴를 포함하여 완전히 토크 제어되는 사족 로봇 ANYmal에서 테스트되었습니다. 평지와 경사 지형, 그리고 단차를 넘는 실험을 수행했으며, 바퀴를 동작 제어 및 계획 프레임워크에 통합하면 직관적인 동작 궤적이 생성되어 다른 바퀴 달린 보행 로봇에 비해 더 견고하고 동적인 보행이 가능함을 보여줍니다. 또한, 4m/s의 속도와 83%의 운송 비용 절감을 통해 바퀴 달린 보행 로봇이 순수 보행 로봇보다 우수함을 입증합니다.

## 参考
- http://arxiv.org/abs/1809.03557v2
