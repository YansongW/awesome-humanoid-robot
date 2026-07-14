---
$id: ent_paper_chan_angle_constrained_formation_co_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Angle-Constrained Formation Control for Circular Mobile Robots
  zh: 圆形移动机器人的角度约束编队控制
  ko: 원형 이동 로봇을 위한 각도 제약 대형 제어
summary:
  en: Proposes a gradient-based distributed control law for planar circular mobile robots that uses only interior angle/bearing
    measurements from vision sensors to achieve rigid formations while guaranteeing collision avoidance between neighbors,
    and proves local exponential convergence of the error dynamics.
  zh: 提出了一种基于梯度的分布式控制律，仅利用视觉传感器获取的相邻机器人圆盘内角/方位测量，使平面圆形移动机器人形成刚性编队并保证相邻机器人之间的避碰，并证明了误差动态的局部指数收敛性。
  ko: 비전 센서로부터 얻은 이웃 로봇 원판의 내각/방위 측정만을 사용하여 평면 상의 원형 이동 로봇이 강성 대형을 형성하고 이웃 간 충돌 회피를 보장하는 기울기 기반 분산 제어법칙을 제안하고, 오차 동역학의 국소
    지수 수렴성을 증명한다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- formation_control
- distributed_control
- collision_avoidance
- bearing_only_control
- angle_based_control
- multi_robot_coordination
- vision_based_sensing
- gradient_based_control
- rigid_formations
- circular_robots
- mobile_robots
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2005.04694v1.
sources:
- id: src_001
  type: paper
  title: Angle-Constrained Formation Control for Circular Mobile Robots
  url: https://arxiv.org/abs/2005.04694
  date: '2020'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
In this letter, we investigate the formation control problem of mobile robots moving in the plane where, instead of assuming robots to be simple points, each robot is assumed to have the form of a disk with equal radius. Based on interior angle measurements of the neighboring robots' disk, which can be obtained from low-cost vision sensors, we propose a gradient-based distributed control law and show the exponential convergence property of the associated error system. By construction, the proposed control law has the appealing property of ensuring collision avoidance between neighboring robots. We also present simulation results for {a team} of four circular mobile robots forming a rectangular shape.

## 核心内容
In this letter, we investigate the formation control problem of mobile robots moving in the plane where, instead of assuming robots to be simple points, each robot is assumed to have the form of a disk with equal radius. Based on interior angle measurements of the neighboring robots' disk, which can be obtained from low-cost vision sensors, we propose a gradient-based distributed control law and show the exponential convergence property of the associated error system. By construction, the proposed control law has the appealing property of ensuring collision avoidance between neighboring robots. We also present simulation results for {a team} of four circular mobile robots forming a rectangular shape.

## 参考
- http://arxiv.org/abs/2005.04694v1

