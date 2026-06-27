---
$id: ent_foundation_convex_optimization
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: foundation
names:
  en: Convex Optimization
  zh: 凸优化
  ko: 볼록 최적화
summary:
  en: The mathematical discipline of minimizing convex functions over convex sets, guaranteeing that any local optimum is also global.
  zh: 在凸集上最小化凸函数的数学学科，保证任何局部最优也是全局最优。
  ko: 볼록 집합 위에서 볼록 함수를 최소화하는 수학 분야로, 모든 국소 최적해가 전역 최적해임을 보장한다.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
tags:
- convex_optimization
- quadratic_programming
- kkt_conditions
- optimization_theory
- humanoid_control
theoretical_depth:
- foundation
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Foundational for QP solvers used in WBC.
sources:
- id: src_001
  type: paper
  title: 'Boyd and Vandenberghe, Convex Optimization'
  url: https://web.stanford.edu/~boyd/cvxbook/
  date: '2004'
  accessed_at: '2026-06-26'
---

## 抽象

> **生活实例**：想象你在一座只有一个山谷的山里找最低点。只要你一直往下走，最终一定会到达谷底——这就是凸优化的好处：没有“假谷底”骗你。
>
> **自然语言逻辑**：如果目标函数是凸的、可行域也是凸的，那么任何局部最小都是全局最小；KKT 条件在 mild 条件下成为最优的充分条件；QP 是凸优化的一类重要特例。

## Overview

Convex optimization studies problems of the form `min f(x) s.t. x ∈ C`, where `f` is a convex function and `C` is a convex set. Quadratic programming, linear programming, and second-order cone programming are all special cases. Convexity enables efficient algorithms with global optimality certificates.

## Relevance to Humanoid Robotics

Whole-body control, trajectory optimization, and model-predictive control all rely on convex optimization. Understanding convexity is essential for knowing when a controller will find a reliable solution in real time.
