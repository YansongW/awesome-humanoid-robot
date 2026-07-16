---
$id: ent_paper_thirugnanam_duality_based_convex_optimizat_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Duality-based Convex Optimization for Real-time Obstacle Avoidance between Polytopes with Control Barrier Functions
  zh: 基于对偶的凸优化控制障碍函数实时多面体避障
  ko: 제어 장벽 함수를 이용한 다면체 간 실시간 장애물 회피를 위한 이중성 기반 볼록 최적화
summary:
  en: Proposes a duality-based nonsmooth control barrier function framework that reformulates minimum-distance constraints
    between polytopes into a convex quadratic program, enabling real-time safety-critical obstacle avoidance for control-affine
    nonlinear systems.
  zh: Developing controllers for obstacle avoidance between polytopes is a challenging and necessary problem for navigation
    in tight spaces. Traditional approaches can only formulate the obstacle avoidance problem as an offline optimization problem.
    To address these challenges, we propose a duality-based safety-critical optimal control using nonsmooth control barrier
    functions for obstacle avoidance between polytopes, which can be solved in real-time with a QP-based optimization problem.
    A dual optimization problem is introduced to represent the minimum distance between polytopes and the Lagrangian
  ko: 제어 아핀 비선형 시스템을 위해 다면체 간 최소 거리 제약을 볼록 이차 계획법으로 재구성하는 이중성 기반 비연속 제어 장벽 함수 프레임워크를 제안하여 실시간 안전 필수 장애물 회피를 가능하게 함.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- intelligence
- knowledge
tags:
- control_barrier_function
- nonsmooth_cbf
- quadratic_programming
- obstacle_avoidance
- polytope
- real_time_control
- safety_critical_control
- nonlinear_control
- motion_planning
- moving_sofa_problem
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2107.08360v4.
sources:
- id: src_001
  type: paper
  title: Duality-based Convex Optimization for Real-time Obstacle Avoidance between Polytopes with Control Barrier Functions
  url: https://arxiv.org/abs/2107.08360
  date: '2022'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## 概述
Developing controllers for obstacle avoidance between polytopes is a challenging and necessary problem for navigation in tight spaces. Traditional approaches can only formulate the obstacle avoidance problem as an offline optimization problem. To address these challenges, we propose a duality-based safety-critical optimal control using nonsmooth control barrier functions for obstacle avoidance between polytopes, which can be solved in real-time with a QP-based optimization problem. A dual optimization problem is introduced to represent the minimum distance between polytopes and the Lagrangian function for the dual form is applied to construct a control barrier function. We validate the obstacle avoidance with the proposed dual formulation for L-shaped (sofa-shaped) controlled robot in a corridor environment. We demonstrate real-time tight obstacle avoidance with non-conservative maneuvers on a moving sofa (piano) problem with nonlinear dynamics.

## 核心内容
Developing controllers for obstacle avoidance between polytopes is a challenging and necessary problem for navigation in tight spaces. Traditional approaches can only formulate the obstacle avoidance problem as an offline optimization problem. To address these challenges, we propose a duality-based safety-critical optimal control using nonsmooth control barrier functions for obstacle avoidance between polytopes, which can be solved in real-time with a QP-based optimization problem. A dual optimization problem is introduced to represent the minimum distance between polytopes and the Lagrangian function for the dual form is applied to construct a control barrier function. We validate the obstacle avoidance with the proposed dual formulation for L-shaped (sofa-shaped) controlled robot in a corridor environment. We demonstrate real-time tight obstacle avoidance with non-conservative maneuvers on a moving sofa (piano) problem with nonlinear dynamics.

## 参考
- http://arxiv.org/abs/2107.08360v4


