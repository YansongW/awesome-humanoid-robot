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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2005.04694v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (532 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2005.04694v1

## 개요
이 연구는 로봇을 질점이 아닌 동일한 반지름을 가진 원판으로 모델링하며, 저비용 시각 센서를 통해 인접 로봇 원판의 내각 정보를 측정합니다. 이러한 각도 측정값을 기반으로 설계된 그래디언트 제어 법칙은 로봇이 원하는 강성 편대를 형성하도록 유도하며, 동시에 인접 로봇 간의 충돌을 내재적으로 방지합니다. 이론적 분석은 오차 시스템이 지수 수렴 특성을 가짐을 증명하며, 네 대의 원형 로봇으로 구성된 직사각형 편대 시뮬레이션을 통해 방법의 유효성을 검증합니다.

## 핵심 내용
### 문제 모델링
- 평면 이동 로봇을 전통적인 질점 모델과 달리 동일한 반지름을 가진 원판으로 모델링
- 각 로봇은 시각 센서를 통해 인접 로봇 원판의 내각 측정값(interior angle measurements)을 획득

### 제어 방법
- 그래디언트 기반 분산 제어 법칙(gradient-based distributed control law) 제안
- 제어 입력은 인접 로봇의 내각/방위 측정값에만 의존하며, 전역 위치 정보가 필요 없음
- 제어 법칙 설계는 추가적인 포텐셜 함수 없이 충돌 회피 메커니즘을 자연스럽게 포함

### 이론적 분석
- 관련 오차 시스템의 국소 지수 수렴성(local exponential convergence) 증명
- 수렴성 분석은 오차 동역학의 선형화 방법에 기반

### 시뮬레이션 검증
- 네 대의 원형 이동 로봇을 사용한 직사각형 편대 시뮬레이션 수행
- 시뮬레이션 결과는 편대 형성 및 충돌 회피 측면에서 제어 법칙의 유효성을 검증
