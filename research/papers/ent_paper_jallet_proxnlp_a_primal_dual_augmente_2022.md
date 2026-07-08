---
$id: ent_paper_jallet_proxnlp_a_primal_dual_augmente_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ProxNLP: a primal-dual augmented Lagrangian solver for nonlinear programming
    in Robotics and beyond'
  zh: ProxNLP：面向机器人及更广领域的非线性规划原始-对偶增广拉格朗日求解器
  ko: 'ProxNLP: 로보틱스 및 그 이상의 비선형 프로그래밍을 위한 primal-dual augmented Lagrangian 솔버'
summary:
  en: This paper presents a primal-dual augmented Lagrangian method for inequality-constrained
    nonlinear programs on manifolds and introduces proxnlp, an open-source C++ implementation
    with Eigen, Pinocchio, and CasADi bindings, validated on robot examples including
    Talos pose generation.
  zh: 本文提出了一种流形上不等式约束非线性规划的原始-对偶增广拉格朗日方法，并介绍了开源C++实现proxnlp，该实现具有Eigen、Pinocchio和CasADi绑定，并在包括Talos姿态生成在内的机器人示例上进行了验证。
  ko: 본 논문은 다양체 상에서 부등식 제약이 있는 비선형 계획을 위한 primal-dual augmented Lagrangian 방법을 제시하고,
    Eigen, Pinocchio, CasADi 바인딩을 갖춘 오픈소스 C++ 구현체인 proxnlp를 소개하며, Talos 자세 생성을 포함한
    로봇 예제에서 검증한다.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- proxnlp
- augmented_lagrangian
- primal_dual
- nonlinear_programming
- manifold_optimization
- lie_groups
- optimization_solver
- talos
- humanoid_pose_generation
- trajectory_optimization
- inverse_geometry
- pinocchio
- casadi
- eigen
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from arXiv full text (arXiv:2210.02109v1); requires human review
    before verification.
sources:
- id: src_001
  type: paper
  title: 'ProxNLP: a primal-dual augmented Lagrangian solver for nonlinear programming
    in Robotics and beyond'
  url: https://arxiv.org/abs/2210.02109
  date: '2022'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

This paper introduces a primal-dual augmented Lagrangian method for inequality-constrained nonlinear programming problems defined on manifolds, together with an open-source C++ implementation named proxnlp. The formulation targets robotics applications where generalized coordinates naturally live on Lie groups and where physical and task constraints—such as joint limits, torque limits, friction cones, obstacle avoidance, and contact constraints—must be handled explicitly. The authors build on the classical augmented Lagrangian method of multipliers and its primal-dual variant, extending the latter to inequality constraints and providing a practical Newton-type solver.

The proxnlp library uses Eigen as its linear-algebra backend and exposes interfaces to Pinocchio for rigid-body dynamics and classical matrix Lie groups such as SE(3), as well as to CasADi for formulating costs and constraints. Python bindings are also provided. The paper is labeled as recent work under review and presents an extended version that includes the open-source implementation. The authors note that a separate C++ package dedicated to control problems using their variant of differential dynamic programming (DDP) is still under development.

Experimental validation covers five small-scale robotics examples: a simple barycenter computation on SE(2), a double-pendulum optimal-control problem implemented with proxnlp, Pinocchio, and CasADi, a UR10 reach-and-obstacle-avoidance task, a Talos humanoid pose-generation problem with foot-placement and gripper constraints, and a Solo-12 quadruped inverse-geometry problem over a heightmap with contact-force constraints.

## Key Contributions

- Primal-dual augmented Lagrangian formulation for inequality-constrained optimization on manifolds.
- Open-source C++ solver proxnlp for constrained nonlinear programs in robotics.
- Integration with Eigen, Pinocchio, and CasADi, with Python bindings.
- Experimental validation on SE(2) barycenter, double-pendulum, UR10 obstacle avoidance, Talos pose generation, and Solo-12 inverse geometry.

## Relevance to Humanoid Robotics

Humanoid robots must solve constrained optimization problems on configuration-space manifolds, including whole-body pose generation, trajectory optimization, and inverse dynamics under contact, balance, joint-limit, and torque constraints. The paper explicitly demonstrates Talos pose generation with foot-flatness, foot-lift, and gripper-position constraints, which is representative of core humanoid motion-planning tasks. The manifold-aware formulation makes proxnlp directly applicable to SE(3) base placement and other Lie-group quantities that arise in humanoid control.
