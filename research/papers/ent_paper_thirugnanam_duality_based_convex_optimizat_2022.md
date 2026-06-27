---
$id: ent_paper_thirugnanam_duality_based_convex_optimizat_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Duality-based Convex Optimization for Real-time Obstacle Avoidance between Polytopes
    with Control Barrier Functions
  zh: 基于对偶的凸优化控制障碍函数实时多面体避障
  ko: 제어 장벽 함수를 이용한 다면체 간 실시간 장애물 회피를 위한 이중성 기반 볼록 최적화
summary:
  en: Proposes a duality-based nonsmooth control barrier function framework that reformulates
    minimum-distance constraints between polytopes into a convex quadratic program,
    enabling real-time safety-critical obstacle avoidance for control-affine nonlinear
    systems.
  zh: 提出一种基于对偶的非光滑控制障碍函数框架，将多面体间最小距离约束重构为凸二次规划，使控制仿射非线性系统能够实现实时安全关键避障。
  ko: 제어 아핀 비선형 시스템을 위해 다면체 간 최소 거리 제약을 볼록 이차 계획법으로 재구성하는 이중성 기반 비연속 제어 장벽 함수 프레임워크를
    제안하여 실시간 안전 필수 장애물 회피를 가능하게 함.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from full text; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: Duality-based Convex Optimization for Real-time Obstacle Avoidance between
    Polytopes with Control Barrier Functions
  url: https://arxiv.org/abs/2107.08360
  date: '2022'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

The paper addresses real-time, safety-critical obstacle avoidance between polytopes for control-affine nonlinear systems navigating tight spaces. Existing approaches typically formulate this as an offline optimization problem, which prevents online deployment. The authors introduce a dual optimization problem to represent the minimum distance between polytopes and use the Lagrangian of the dual form to construct a Nonsmooth Control Barrier Function (NCBF). This yields a convex quadratic program that can be solved in real time to compute a minimally invasive safe control input.

The safety set is defined as the zero-superlevel set of the squared minimum distance between two polytopes. Because the minimum distance function is locally Lipschitz but nonsmooth, the authors work in the dual space, where the derivative of the distance can be expressed as a linear program. A QP-based feedback control law is then derived, with constraints ensuring that the NCBF condition is satisfied. The formulation is extended to static obstacles and nonconvex robot geometries represented as unions of polytopes.

## Key Contributions

- Reformulated polytope obstacle avoidance for nonlinear affine systems into a duality-based QP with CBFs.
- Established a QP-based control law that guarantees safety by resolving the nonsmooth minimum-distance problem in the dual space.
- Demonstrated real-time 50 Hz tight obstacle avoidance on the nonlinear moving sofa (piano) problem.
- Showed convex QP implementation remains feasible even for nonlinear dynamics, enabling real-time safety-critical control.

## Relevance to Humanoid Robotics

The method enables real-time, non-conservative collision avoidance between polyhedral bodies in cluttered, tight environments. For humanoid robots, this is directly applicable to safe navigation and motion planning in factories, warehouses, and shared human spaces where the robot's limbs or torso must avoid collisions with obstacles, equipment, and people. The convex QP formulation is compatible with online whole-body controllers, making it a candidate building block for safety-critical humanoid locomotion and manipulation pipelines.
