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
  zh: 本文针对平面圆形移动机器人的编队控制问题，提出了一种基于梯度法的分布式控制律。该控制律仅利用视觉传感器获取的相邻机器人内角/方位测量值，在实现刚性编队的同时保证邻接机器人间的碰撞避免，并证明了误差动力学的局部指数收敛性。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2005.04694v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
该研究将机器人建模为等半径圆盘而非质点，通过低成本视觉传感器测量相邻机器人圆盘的内角信息。基于这些角度测量值设计的梯度控制律，能够驱动机器人形成期望的刚性编队，同时内在地确保邻接机器人不发生碰撞。理论分析证明了误差系统具有指数收敛特性，并通过四台圆形机器人组成矩形编队的仿真实验验证了方法的有效性。

## 核心内容
### 问题建模
- 将平面移动机器人建模为半径相等的圆盘，区别于传统质点模型
- 每个机器人通过视觉传感器获取相邻机器人圆盘的内角测量值（interior angle measurements）

### 控制方法
- 提出基于梯度法的分布式控制律（gradient-based distributed control law）
- 控制输入仅依赖相邻机器人的内角/方位测量值，无需全局位置信息
- 控制律设计天然包含碰撞避免机制，无需额外势函数

### 理论分析
- 证明了关联误差系统的局部指数收敛性（local exponential convergence）
- 收敛性分析基于误差动力学的线性化方法

### 仿真验证
- 采用四台圆形移动机器人进行矩形编队仿真
- 仿真结果验证了控制律在编队形成和碰撞避免方面的有效性

## Overview
In this letter, we investigate the formation control problem of mobile robots moving in the plane where, instead of assuming robots to be simple points, each robot is assumed to have the form of a disk with equal radius. Based on interior angle measurements of the neighboring robots' disk, which can be obtained from low-cost vision sensors, we propose a gradient-based distributed control law and show the exponential convergence property of the associated error system. By construction, the proposed control law has the appealing property of ensuring collision avoidance between neighboring robots. We also present simulation results for {a team} of four circular mobile robots forming a rectangular shape.

## Overview
In this letter, we investigate the formation control problem of mobile robots moving in the plane where, instead of assuming robots to be simple points, each robot is assumed to have the form of a disk with equal radius. Based on interior angle measurements of the neighboring robots' disk, which can be obtained from low-cost vision sensors, we propose a gradient-based distributed control law and show the exponential convergence property of the associated error system. By construction, the proposed control law has the appealing property of ensuring collision avoidance between neighboring robots. We also present simulation results for a team of four circular mobile robots forming a rectangular shape.

## Content
In this letter, we investigate the formation control problem of mobile robots moving in the plane where, instead of assuming robots to be simple points, each robot is assumed to have the form of a disk with equal radius. Based on interior angle measurements of the neighboring robots' disk, which can be obtained from low-cost vision sensors, we propose a gradient-based distributed control law and show the exponential convergence property of the associated error system. By construction, the proposed control law has the appealing property of ensuring collision avoidance between neighboring robots. We also present simulation results for a team of four circular mobile robots forming a rectangular shape.

## 개요
본 논문에서는 평면상에서 이동하는 모바일 로봇의 포메이션 제어 문제를 연구하며, 로봇을 단순한 점으로 가정하는 대신 각 로봇이 동일한 반지름을 가진 원반 형태를 갖는다고 가정한다. 저비용 비전 센서로부터 얻을 수 있는 이웃 로봇 원반의 내각 측정값을 기반으로, 기울기 기반 분산 제어 법칙을 제안하고 관련 오차 시스템의 지수 수렴 특성을 보인다. 제안된 제어 법칙은 구성상 이웃 로봇 간 충돌 회피를 보장하는 장점을 가진다. 또한 직사각형 형태를 형성하는 4개의 원형 모바일 로봇 팀에 대한 시뮬레이션 결과를 제시한다.

## 핵심 내용
본 논문에서는 평면상에서 이동하는 모바일 로봇의 포메이션 제어 문제를 연구하며, 로봇을 단순한 점으로 가정하는 대신 각 로봇이 동일한 반지름을 가진 원반 형태를 갖는다고 가정한다. 저비용 비전 센서로부터 얻을 수 있는 이웃 로봇 원반의 내각 측정값을 기반으로, 기울기 기반 분산 제어 법칙을 제안하고 관련 오차 시스템의 지수 수렴 특성을 보인다. 제안된 제어 법칙은 구성상 이웃 로봇 간 충돌 회피를 보장하는 장점을 가진다. 또한 직사각형 형태를 형성하는 4개의 원형 모바일 로봇 팀에 대한 시뮬레이션 결과를 제시한다.

## 参考
- http://arxiv.org/abs/2005.04694v1
