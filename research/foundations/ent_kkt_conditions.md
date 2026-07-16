---
$id: ent_kkt_conditions
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: theorem
names:
  en: Karush-Kuhn-Tucker (KKT) Conditions
  zh: Karush-Kuhn-Tucker（KKT）条件
  ko: Karush-Kuhn-Tucker (KKT) 조건
summary:
  en: Necessary (and sufficient under convexity/constraint qualification) optimality conditions for constrained nonlinear
    programs.
  zh: '> 生活实例：想象你在一个商场里想找到离出口最近的位置，但被告知“不能走进任何商店内部”（不等式约束），同时“必须站在过道的中线上”（等式约束）。KKT 条件就是一套判断标准：如果你站的位置真的最优，那么要么你不在边界上（约束根本不影响你），要么边界像一堵墙把你“顶”在最优位置，墙对你的反作用力（Lagrange
    乘子）刚好平衡了目标函数的“拉力”。 > > 自然语言逻辑：把带约束的优化问题写成一个“总能量”——拉格朗日函数；然后分别对原变量和乘子求导并令其为零；再要求不等式乘子非负、不等式约束被满足，并且“要么约束起作用，要么乘子为零”。这组条件就是
    KKT 条件。在凸问题和合适的约束规范下，满足 KKT 条件就等价于找到了全局最优解。'
  ko: 제약이 있는 비선형 계획법의 최적성 필요조건(볼록성 및 제약 자격이 있으면 충분조건이기도 함).
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- principle
tags:
- optimization
- constrained_optimization
- lagrange_multipliers
- kkt
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body restructured into standard sections by scripts/restructure_entry_bodies.py.
sources:
- id: src_nocedal_wright_2006
  type: other
  title: J. Nocedal and S. J. Wright, Numerical Optimization, 2nd ed., Springer, 2006
  url: https://doi.org/10.1007/978-0-387-40065-5
  date: '2006-01-01'
  accessed_at: '2026-06-25'
---

## 概述
# Karush-Kuhn-Tucker（KKT）条件

## 核心内容
## 抽象

> **生活实例**：想象你在一个商场里想找到离出口最近的位置，但被告知“不能走进任何商店内部”（不等式约束），同时“必须站在过道的中线上”（等式约束）。KKT 条件就是一套判断标准：如果你站的位置真的最优，那么要么你不在边界上（约束根本不影响你），要么边界像一堵墙把你“顶”在最优位置，墙对你的反作用力（Lagrange 乘子）刚好平衡了目标函数的“拉力”。
>
> **自然语言逻辑**：把带约束的优化问题写成一个“总能量”——拉格朗日函数；然后分别对原变量和乘子求导并令其为零；再要求不等式乘子非负、不等式约束被满足，并且“要么约束起作用，要么乘子为零”。这组条件就是 KKT 条件。在凸问题和合适的约束规范下，满足 KKT 条件就等价于找到了全局最优解。

## 形式化定义

考虑约束优化问题：

$$
\min_{x} \; f(x) \quad \text{s.t.} \quad h_i(x) = 0 \; (i=1,\dots,m), \quad g_j(x) \le 0 \; (j=1,\dots,p).
$$

定义 Lagrangian：

$$
\mathcal{L}(x, \lambda, \mu) = f(x) + \sum_{i=1}^{m} \lambda_i h_i(x) + \sum_{j=1}^{p} \mu_j g_j(x).
$$

若 $x^\star$ 为局部最优且满足约束规范（如 LICQ 或 Slater's condition），则存在乘子 $\lambda^\star, \mu^\star$ 使得：

1. **Stationarity**：$\nabla_x \mathcal{L}(x^\star, \lambda^\star, \mu^\star) = 0$。
2. **Primal feasibility**：$h_i(x^\star) = 0$，$g_j(x^\star) \le 0$。
3. **Dual feasibility**：$\mu_j^\star \ge 0$。
4. **Complementary slackness**：$\mu_j^\star g_j(x^\star) = 0$。

## 关键符号与直觉对应

| 符号 | 名称 | 直觉含义 |
|------|------|----------|
| $f(x)$ | 目标函数 | 想最小化的“代价” |
| $h_i(x)$ | 等式约束 | 必须精确满足的规则 |
| $g_j(x)$ | 不等式约束 | 不能越过的边界 |
| $\lambda_i$ | 等式 Lagrange 乘子 | 等式约束的“反作用力” |
| $\mu_j$ | 不等式 Lagrange 乘子 | 边界墙的“推力”，非负 |
| $\mathcal{L}$ | Lagrangian | 把约束“惩罚”加进目标后的总能量 |

## 与其他知识点的关系

- `derived_from` → Lagrangian（拉格朗日函数）
- `requires` → Constraint qualification（约束规范，如 LICQ、Slater's condition）
- `has_prerequisite` → Multivariable calculus（多元微积分）
- `has_prerequisite` → Convex analysis（凸分析）
- `uses_theorem` → 在 WBC、MPC、经济模型等带约束优化问题中广泛使用

## 参考
- [J. Nocedal and S. J. Wright, Numerical Optimization, 2nd ed., Springer, 2006](https://doi.org/10.1007/978-0-387-40065-5)

## Overview
# Karush-Kuhn-Tucker (KKT) Conditions

## Content
## Abstract

> **Life Example**: Imagine you are in a shopping mall and want to find the location closest to the exit, but you are told "you cannot enter any store" (inequality constraint) and "you must stand on the center line of the aisle" (equality constraint). The KKT conditions are a set of criteria: if your position is truly optimal, then either you are not on the boundary (the constraint does not affect you at all), or the boundary acts like a wall "pushing" you to the optimal position, and the reaction force of the wall (Lagrange multiplier) exactly balances the "pull" of the objective function.
>
> **Natural Language Logic**: Write the constrained optimization problem as a "total energy"—the Lagrangian function; then take derivatives with respect to the original variables and multipliers and set them to zero; further require that the inequality multipliers are non-negative, the inequality constraints are satisfied, and "either the constraint is active or the multiplier is zero." This set of conditions constitutes the KKT conditions. For convex problems and under appropriate constraint qualifications, satisfying the KKT conditions is equivalent to finding the global optimal solution.

## Formal Definition

Consider the constrained optimization problem:

$$
\min_{x} \; f(x) \quad \text{s.t.} \quad h_i(x) = 0 \; (i=1,\dots,m), \quad g_j(x) \le 0 \; (j=1,\dots,p).
$$

Define the Lagrangian:

$$
\mathcal{L}(x, \lambda, \mu) = f(x) + \sum_{i=1}^{m} \lambda_i h_i(x) + \sum_{j=1}^{p} \mu_j g_j(x).
$$

If $x^\star$ is a local optimum and satisfies a constraint qualification (e.g., LICQ or Slater's condition), then there exist multipliers $\lambda^\star, \mu^\star$ such that:

1. **Stationarity**: $\nabla_x \mathcal{L}(x^\star, \lambda^\star, \mu^\star) = 0$.
2. **Primal feasibility**: $h_i(x^\star) = 0$, $g_j(x^\star) \le 0$.
3. **Dual feasibility**: $\mu_j^\star \ge 0$.
4. **Complementary slackness**: $\mu_j^\star g_j(x^\star) = 0$.

## Key Symbols and Intuitive Correspondence

| Symbol | Name | Intuitive Meaning |
|--------|------|-------------------|
| $f(x)$ | Objective function | The "cost" to be minimized |
| $h_i(x)$ | Equality constraint | Rules that must be exactly satisfied |
| $g_j(x)$ | Inequality constraint | Boundaries that cannot be crossed |
| $\lambda_i$ | Equality Lagrange multiplier | "Reaction force" of the equality constraint |
| $\mu_j$ | Inequality Lagrange multiplier | "Push" of the boundary wall, non-negative |
| $\mathcal{L}$ | Lagrangian | Total energy after "penalizing" constraints into the objective |

## Relationships with Other Knowledge Points

- `derived_from` → Lagrangian
- `requires` → Constraint qualification (e.g., LICQ, Slater's condition)
- `has_prerequisite` → Multivariable calculus
- `has_prerequisite` → Convex analysis
- `uses_theorem` → Widely used in constrained optimization problems such as WBC, MPC, economic models, etc.

## 개요
# Karush-Kuhn-Tucker（KKT）조건

## 핵심 내용
## 추상

> **생활 예시**: 쇼핑몰에서 출구와 가장 가까운 위치를 찾고 싶지만, "어떤 매장 내부에도 들어갈 수 없고"(부등식 제약), "반드시 통로의 중앙선 위에 서 있어야 한다"(등식 제약)는 조건이 있다고 상상해보세요. KKT 조건은 다음과 같은 판단 기준입니다: 만약 당신이 서 있는 위치가 정말 최적이라면, 당신이 경계에 있지 않거나(제약이 전혀 영향을 미치지 않음), 경계가 벽처럼 당신을 최적 위치에 "밀어 넣고" 있으며, 벽이 당신에게 가하는 반작용력(Lagrange 승수)이 목적 함수의 "당기는 힘"을 정확히 균형 맞춥니다.
>
> **자연어 논리**: 제약이 있는 최적화 문제를 하나의 "총 에너지"인 라그랑주 함수로 작성합니다. 그런 다음 원래 변수와 승수에 대해 각각 미분하고 0으로 설정합니다. 또한 부등식 승수가 음이 아니어야 하고, 부등식 제약이 충족되어야 하며, "제약이 작용하거나 승수가 0이어야 합니다"라는 조건을 요구합니다. 이 조건들이 바로 KKT 조건입니다. 볼록 문제와 적절한 제약 규격 하에서 KKT 조건을 만족하는 것은 전역 최적해를 찾은 것과 동일합니다.

## 형식적 정의

다음 제약 최적화 문제를 고려합니다:

$$
\min_{x} \; f(x) \quad \text{s.t.} \quad h_i(x) = 0 \; (i=1,\dots,m), \quad g_j(x) \le 0 \; (j=1,\dots,p).
$$

라그랑주 함수를 정의합니다:

$$
\mathcal{L}(x, \lambda, \mu) = f(x) + \sum_{i=1}^{m} \lambda_i h_i(x) + \sum_{j=1}^{p} \mu_j g_j(x).
$$

$x^\star$가 국소 최적해이고 제약 규격(예: LICQ 또는 Slater 조건)을 만족한다면, 승수 $\lambda^\star, \mu^\star$가 존재하여 다음을 만족합니다:

1. **Stationarity**: $\nabla_x \mathcal{L}(x^\star, \lambda^\star, \mu^\star) = 0$.
2. **Primal feasibility**: $h_i(x^\star) = 0$, $g_j(x^\star) \le 0$.
3. **Dual feasibility**: $\mu_j^\star \ge 0$.
4. **Complementary slackness**: $\mu_j^\star g_j(x^\star) = 0$.

## 주요 기호와 직관적 대응

| 기호 | 이름 | 직관적 의미 |
|------|------|----------|
| $f(x)$ | 목적 함수 | 최소화하려는 "비용" |
| $h_i(x)$ | 등식 제약 | 정확히 충족해야 하는 규칙 |
| $g_j(x)$ | 부등식 제약 | 넘을 수 없는 경계 |
| $\lambda_i$ | 등식 Lagrange 승수 | 등식 제약의 "반작용력" |
| $\mu_j$ | 부등식 Lagrange 승수 | 경계 벽의 "밀어내는 힘", 음이 아님 |
| $\mathcal{L}$ | Lagrangian | 제약을 "벌점"으로 목적에 추가한 총 에너지 |

## 다른 지식 포인트와의 관계

- `derived_from` → Lagrangian (라그랑주 함수)
- `requires` → Constraint qualification (제약 규격, 예: LICQ, Slater 조건)
- `has_prerequisite` → Multivariable calculus (다변수 미적분학)
- `has_prerequisite` → Convex analysis (볼록 해석)
- `uses_theorem` → WBC, MPC, 경제 모델 등 제약이 있는 최적화 문제에서 널리 사용됨
