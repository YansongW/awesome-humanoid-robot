---
$id: ent_paper_agrawal_constrained_nonlinear_kaczmarz_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Constrained Nonlinear Kaczmarz Projection on Intersections of Manifolds for
    Coordinated Multi-Robot Mobile Manipulation
  zh: 受约束非线性Kaczmarz流形交集投影用于协调多机器人移动操作
  ko: 다중 이동 조작 로봇의 협조를 위한 다양체 교차에 대한 제약 비선형 Kaczmarz 투영
summary:
  en: This paper presents a manifold-based constraint formulation and a constrained
    nonlinear Kaczmarz (cNKZ) projection method for coordinated mobile manipulation,
    integrated with a sampling-based planner to solve dozens of constraints for 3–6
    mobile manipulators and validated on TurtleBot3 Waffle Pi robots with OpenMANIPULATOR-X
    arms.
  zh: 本文提出了一种基于流形的约束建模方法以及受约束非线性Kaczmarz（cNKZ）投影方法，用于协调移动操作；该方法与基于采样的运动规划器相结合，可同时求解3至6台移动操作臂（18至36自由度）的数十个约束，并在TurtleBot3
    Waffle Pi与OpenMANIPULATOR-X硬件上进行了验证。
  ko: 본 논문은 다중 이동 조작 로봇의 협조를 위한 다양체 기반 제약 공식화와 제약 비선형 Kaczmarz(cNKZ) 투영법을 제안하며, 샘플링
    기반 경로 계획기와 통합하여 3~6대의 이동 조작 로봇(18~36자유도)에 수십 개의 제약을 동시에 해결하고 TurtleBot3 Waffle
    Pi 및 OpenMANIPULATOR-X 하드웨어에서 검증하였다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- constrained_motion_planning
- multi_robot_manipulation
- coordinated_manipulation
- mobile_manipulation
- kaczmarz_projection
- manifold_constraints
- sampling_based_planning
- whole_body_planning
- humanoid_applicable
- turtlebot3
- openmanipulator_x
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the supplied abstract and metadata; full-text verification
    is required before promotion to verified.
sources:
- id: src_001
  type: paper
  title: Constrained Nonlinear Kaczmarz Projection on Intersections of Manifolds for
    Coordinated Multi-Robot Mobile Manipulation
  url: https://arxiv.org/abs/2410.21630v2
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Cooperative manipulation by multiple mobile manipulators must satisfy many simultaneous constraints arising from robot structure, task geometry, and operational requirements. The authors model these constraints as a family of implicit manifolds and seek configurations that lie on the intersection of those manifolds. To reach this intersection efficiently, they introduce the constrained nonlinear Kaczmarz (cNKZ) projection method, which iteratively projects a candidate configuration onto each constraint manifold while using manifold-specific residual thresholds to decide convergence. The projection operator is embedded inside a sampling-based motion planner so that the planner can grow a tree of constraint-satisfying configurations and produce feasible coordinated trajectories.

Experiments are performed in simulation with teams of 3–6 mobile manipulators (18–36 degrees of freedom) and up to 80 nonlinear constraints. The cNKZ-based planner reportedly achieves up to a 92% success rate in cluttered environments, whereas baseline approaches fail to find solutions. The authors also validate the method on hardware with three TurtleBot3 Waffle Pi mobile bases equipped with OpenMANIPULATOR-X arms. Limitations noted include discarded collision-free projections, unmodeled payload dynamics, wheel slippage during execution, and open questions about online execution and scalability to larger teams.

The work is positioned as a general constrained motion-planning framework; although evaluated on wheeled mobile manipulators, the manifold formulation and projection technique are argued to be applicable to other high-DoF systems, including humanoid robots, dual-arm setups, and cluttered industrial environments.

## Key Contributions

• Unified manifold formulation that represents structural, task-induced, and robot-specific operational constraints within a single mathematical family.
• Constrained nonlinear Kaczmarz (cNKZ) projection technique with per-manifold residual thresholds for finding constraint-satisfying configurations.
• Centralized sampling-based constrained motion planning algorithm that integrates cNKZ into an RRT-style planner for cooperative multi-robot manipulation.
• Simulation experiments on 3–6 mobile manipulators (18–36 DoF) with up to 80 nonlinear constraints and real-hardware validation on three TurtleBot3 Waffle Pi robots with OpenMANIPULATOR-X arms.

## Relevance to Humanoid Robotics

The manifold-based constraint formulation is domain-agnostic and can encode whole-body balance, limb coordination, contact, and environmental constraints that are central to humanoid robots. The cNKZ projection scales to high-DoF problems, making it a candidate building block for humanoid whole-body motion planning and dual-arm coordination in cluttered factory or warehouse settings. Because the method is integrated with a sampling-based planner, it can potentially be reused for humanoid tasks that combine locomotion, manipulation, and collision avoidance under many simultaneous constraints.
