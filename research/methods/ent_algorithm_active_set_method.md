---
$id: ent_algorithm_active_set_method
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: algorithm
names:
  en: Active-Set Method for Quadratic Programming
  zh: 二次规划的积极集法
  ko: 이차 계획법의 활성 집합법
summary:
  en: An iterative algorithm for solving QPs that maintains a working set of active constraints and solves equality-constrained subproblems until optimality conditions are satisfied.
  zh: 一种求解二次规划的迭代算法，维护一个活动约束工作集，并求解等式约束子问题直到满足最优性条件。
  ko: 활성 제약 조건의 작업 집합을 유지하고 최적성 조건이 만족될 때까지 등식 제약 하위 문제를 푸는 QP를 위한 반복 알고리즘이다.
domains:
- 07_ai_models_algorithms
- 00_foundations
layers:
- intelligence
- foundations
functional_roles:
- knowledge
tags:
- active_set
- quadratic_programming
- optimization_algorithm
- kkt_conditions
- humanoid_control
theoretical_depth:
- method
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Standard QP algorithm.
sources:
- id: src_001
  type: paper
  title: 'Nocedal and Wright, Numerical Optimization'
  url: https://link.springer.com/book/10.1007/978-0-387-40065-5
  date: '2006'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_foundation_convex_optimization
  relationship: has_prerequisite
  description:
    en: Active-set methods rely on convex QP theory and KKT conditions.
    zh: 积极集法依赖于凸 QP 理论与 KKT 条件。
    ko: 활성 집합법은 볼록 QP 이론과 KKT 조건에 의존한다.
- id: ent_formalism_inverse_dynamics_qp
  relationship: solves
  description:
    en: Active-set methods can solve the inverse-dynamics QP formulation.
    zh: 积极集法可用于求解逆动力学 QP 形式化。
    ko: 활성 집합법은 역동역학 QP 공식화를 풀 수 있다.
---

## 抽象

> **生活实例**：想象你在一条有很多规矩的跑道上找最快路线。积极集法就像你边走边判断哪些规矩“正在影响你”（ active ），哪些暂时没影响；你只在当前影响你的规矩里求解，直到找到一条既遵守规矩又最优的路。
>
> **自然语言逻辑**：QP 的解通常位于某些不等式约束的边界上。积极集法猜测哪些约束在解处是 active 的，把问题转化为等式约束 QP 求解，然后检查 KKT 条件，逐步修正 active 集合直到收敛。

## Overview

The active-set method is one of the two main families of QP solvers (the other being interior-point methods). It is particularly efficient when the number of active constraints at the solution is small relative to the problem size. Each iteration solves a linear system derived from the KKT conditions of the current active set.

## Relevance to Humanoid Robotics

Real-time WBC requires solving QPs in milliseconds. Active-set methods can exploit warm-starting from the previous control tick, making them popular in robotics implementations.
