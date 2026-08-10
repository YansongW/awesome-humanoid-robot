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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1809.03557v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (698 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/1809.03557v2

## 개요
본 연구는 보행과 구동의 장점을 결합한 바퀴형 사족 로봇의 동적 운동 전략을 개발했다. 해당 최적화 프레임워크는 바퀴가 도입한 추가 자유도를 긴밀하게 통합하며, 영점 모멘트 기반 운동 최적화기가 기준 궤적을 지속적으로 갱신하고, 계층적 전신 제어기가 비홀로노믹 구름 제약을 포함한 우선순위 작업 시퀀스를 풀어 최적의 일반화 가속도와 접촉력을 계산한다. 완전 토크 제어가 적용된 ANYmal 로봇(다리 끝에 비조향 바퀴 장착)에서 수행된 실험은, 해당 방법이 평지, 경사 지형 및 계단에서 직관적인 운동 궤적을 생성하며, 다른 바퀴-다리 로봇보다 더 견고하고 동적인 운동을 구현하고, 4 m/s 속도와 83%의 운송 비용 절감을 통해 바퀴-다리 로봇의 우수성을 입증했다.

## 핵심 내용
### 방법 아키텍처
- **운동 최적화기**: 영점 모멘트(ZMP) 기반 온라인 최적화 프레임워크로, 전신 기준 궤적을 지속적으로 갱신하며 바퀴의 비홀로노믹 구름 제약을 핵심 최적화 조건으로 포함한다.
- **계층적 전신 제어기**: 우선순위 작업 시퀀스(비홀로노믹 구름 제약, 신체 자세, 발끝 힘 분배 등 포함)를 풀어 최적의 일반화 가속도와 접촉력을 계산하고, 정밀한 궤적 추적을 구현한다.

### 실험 설정
- **플랫폼**: ANYmal 사족 로봇, 모든 관절이 토크 제어 방식이며, 다리 끝에는 조향 기능이 없는 구동 바퀴가 장착되어 있다.
- **테스트 시나리오**: 평지, 경사 지형(경사도 미명시), 계단 넘기.

### 주요 결과
- **속도**: 최대 4 m/s로, 순수 다리형 보행보다 현저히 높다.
- **에너지 효율**: 운송 비용(Cost of Transport)이 순수 다리형 보행 대비 83% 감소했다.
- **견고성**: 복잡한 지형에서 더 직관적인 운동 궤적을 생성하며, 다른 바퀴-다리 로봇(예: 익명의 비교 시스템)보다 동적 안정성이 우수하다.

### 결론
바퀴의 구름 제약을 운동 제어 및 계획 프레임워크에 긴밀하게 통합함으로써 바퀴-다리 로봇의 혼합 운동 장점을 최대한 발휘할 수 있으며, 속도와 에너지 효율 모두에서 전통적인 다리형 로봇을 능가한다.
