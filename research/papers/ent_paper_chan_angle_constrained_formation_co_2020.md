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
  en: Proposes a gradient-based distributed control law for planar circular mobile
    robots that uses only interior angle/bearing measurements from vision sensors
    to achieve rigid formations while guaranteeing collision avoidance between neighbors,
    and proves local exponential convergence of the error dynamics.
  zh: 提出了一种基于梯度的分布式控制律，仅利用视觉传感器获取的相邻机器人圆盘内角/方位测量，使平面圆形移动机器人形成刚性编队并保证相邻机器人之间的避碰，并证明了误差动态的局部指数收敛性。
  ko: 비전 센서로부터 얻은 이웃 로봇 원판의 내각/방위 측정만을 사용하여 평면 상의 원형 이동 로봇이 강성 대형을 형성하고 이웃 간 충돌 회피를
    보장하는 기울기 기반 분산 제어법칙을 제안하고, 오차 동역학의 국소 지수 수렴성을 증명한다.
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
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from arXiv full text (2005.04694); requires human review before
    verification.
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

## Overview

This 2020 letter by Nelson P.K. Chan, Bayu Jayawardhana, and Hector Garcia de Marina addresses formation control for mobile robots that have circular disk geometry rather than being modeled as points. Each robot is assumed to have the same radius and single-integrator planar dynamics. The robots detect two tangent points on the surface of each neighbor, which yields two relative bearing/unit-vector measurements. From these bearings an interior angle is computed, and the authors propose a gradient-based distributed control law built from angle-based potential functions. The control law requires no range information and can be implemented using only the available bearing measurements.

The angle-based potential function is designed so that its denominator term cos(θij) − 1/2 grows unbounded as the inter-center distance approaches twice the robot radius. This creates a barrier-like effect that guarantees collision avoidance between neighboring robots as long as the initial distance exceeds 2r. The authors show that the resulting error dynamics are locally exponentially stable around the desired internal-angle constraints obtained from a minimally and infinitesimally rigid target formation. A simulation with four circular robots forming a rectangular shape illustrates the convergence and collision-avoidance properties.

## Key Contributions

- Models robots as circular disks of equal radius rather than point masses, and exploits interior angle measurements between neighboring disks.
- Proposes a gradient-based distributed control law implementable with only relative bearing/unit-vector measurements, without requiring range information.
- Guarantees collision avoidance between neighboring robots by design through a barrier-like potential term that becomes unbounded as the distance approaches twice the robot radius.
- Proves local exponential convergence of the internal angle error dynamics for minimally and infinitesimally rigid target formations.
- Demonstrates the approach in simulation with four circular mobile robots forming a rectangular shape.

## Relevance to Humanoid Robotics

Although the paper studies planar circular robots, its distributed coordination principles are directly relevant to managing fleets or swarms of humanoid robots during logistics, deployment, and operation in shared industrial environments. Humanoid fleets must maintain safe geometric formations while moving through warehouses, factory floors, or staging areas, and collision avoidance between neighboring robots is essential. The bearing-only, vision-sensor-based implementation aligns with the sensing modalities often available on humanoid platforms, where low-cost cameras can provide relative bearing information without accurate ranging. The rigidity-theoretic framework for angle-constrained formations can be adapted or extended to higher-level motion coordination algorithms for humanoid groups.
