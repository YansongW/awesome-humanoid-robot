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

## Overview
Developing controllers for obstacle avoidance between polytopes is a challenging and necessary problem for navigation in tight spaces. Traditional approaches can only formulate the obstacle avoidance problem as an offline optimization problem. To address these challenges, we propose a duality-based safety-critical optimal control using nonsmooth control barrier functions for obstacle avoidance between polytopes, which can be solved in real-time with a QP-based optimization problem. A dual optimization problem is introduced to represent the minimum distance between polytopes and the Lagrangian function for the dual form is applied to construct a control barrier function. We validate the obstacle avoidance with the proposed dual formulation for L-shaped (sofa-shaped) controlled robot in a corridor environment. We demonstrate real-time tight obstacle avoidance with non-conservative maneuvers on a moving sofa (piano) problem with nonlinear dynamics.

## Content
Developing controllers for obstacle avoidance between polytopes is a challenging and necessary problem for navigation in tight spaces. Traditional approaches can only formulate the obstacle avoidance problem as an offline optimization problem. To address these challenges, we propose a duality-based safety-critical optimal control using nonsmooth control barrier functions for obstacle avoidance between polytopes, which can be solved in real-time with a QP-based optimization problem. A dual optimization problem is introduced to represent the minimum distance between polytopes and the Lagrangian function for the dual form is applied to construct a control barrier function. We validate the obstacle avoidance with the proposed dual formulation for L-shaped (sofa-shaped) controlled robot in a corridor environment. We demonstrate real-time tight obstacle avoidance with non-conservative maneuvers on a moving sofa (piano) problem with nonlinear dynamics.

## 개요
폴리토프 간 장애물 회피를 위한 제어기 개발은 좁은 공간에서의 내비게이션을 위해 도전적이면서도 필수적인 문제입니다. 전통적인 접근 방식은 장애물 회피 문제를 오프라인 최적화 문제로만 공식화할 수 있습니다. 이러한 도전 과제를 해결하기 위해, 우리는 폴리토프 간 장애물 회피를 위한 비평활 제어 장벽 함수를 사용한 이중성 기반의 안전 중요 최적 제어를 제안하며, 이는 QP 기반 최적화 문제로 실시간으로 해결할 수 있습니다. 폴리토프 간 최소 거리를 나타내기 위해 이중 최적화 문제를 도입하고, 이중 형태에 대한 라그랑지안 함수를 적용하여 제어 장벽 함수를 구성합니다. 우리는 복도 환경에서 L자형(소파형) 제어 로봇에 대해 제안된 이중 공식을 사용하여 장애물 회피를 검증합니다. 비선형 동역학을 가진 움직이는 소파(피아노) 문제에서 비보수적 기동을 통한 실시간 밀착 장애물 회피를 시연합니다.

## 핵심 내용
폴리토프 간 장애물 회피를 위한 제어기 개발은 좁은 공간에서의 내비게이션을 위해 도전적이면서도 필수적인 문제입니다. 전통적인 접근 방식은 장애물 회피 문제를 오프라인 최적화 문제로만 공식화할 수 있습니다. 이러한 도전 과제를 해결하기 위해, 우리는 폴리토프 간 장애물 회피를 위한 비평활 제어 장벽 함수를 사용한 이중성 기반의 안전 중요 최적 제어를 제안하며, 이는 QP 기반 최적화 문제로 실시간으로 해결할 수 있습니다. 폴리토프 간 최소 거리를 나타내기 위해 이중 최적화 문제를 도입하고, 이중 형태에 대한 라그랑지안 함수를 적용하여 제어 장벽 함수를 구성합니다. 우리는 복도 환경에서 L자형(소파형) 제어 로봇에 대해 제안된 이중 공식을 사용하여 장애물 회피를 검증합니다. 비선형 동역학을 가진 움직이는 소파(피아노) 문제에서 비보수적 기동을 통한 실시간 밀착 장애물 회피를 시연합니다.
