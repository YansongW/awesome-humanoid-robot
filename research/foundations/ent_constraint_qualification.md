---
$id: ent_constraint_qualification
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: concept
names:
  en: Constraint qualification
  zh: 约束规范
  ko: 제약 자격
summary:
  en: A regularity condition on the constraints of an optimization problem that guarantees the validity of the Karush-Kuhn-Tucker necessary optimality conditions at a local optimum.
  zh: 优化问题约束的一种正则性条件，保证在局部最优处 Karush-Kuhn-Tucker 最优性必要条件的有效性。
  ko: 최적화 문제의 제약에 대한 정칙성 조건으로, 국부 최적해에서 Karush-Kuhn-Tucker 필요 최적성 조건의 타당성을 보장합니다.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- foundation
tags:
- optimization
- constrained_optimization
- regularity
- licq
- slater
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard foundational knowledge; reviewed against standard references.
sources:
- id: src_nocedal_wright_2006
  type: other
  title: J. Nocedal and S. J. Wright, Numerical Optimization, 2nd ed., Springer, 2006
  url: https://doi.org/10.1007/978-0-387-40065-5
  date: '2006-01-01'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_active_set_method
  relationship: is_prerequisite_for
  description:
    en: Active-set methods exploit the set of active constraints whose gradients must satisfy a constraint qualification for reliable iteration.
    zh: 起作用集方法利用起作用约束集合，其梯度需满足约束规范以保证迭代可靠。
    ko: 활성 집합법은 기울기가 제약 자격을 만족해야 신뢰할 수 있는 반복이 가능한 활성 제약 집합을 활용합니다.
- id: ent_interior_point_method
  relationship: is_prerequisite_for
  description:
    en: Interior-point methods maintain strict inequality feasibility and therefore rely implicitly on constraint qualifications to guarantee convergence to KKT points.
    zh: 内点法保持严格不等式可行性，因此隐式依赖约束规范以保证收敛到 KKT 点。
    ko: 내점법은 엄격한 부등식 실행 가능성을 유지하므로 KKT 점으로의 수렴을 보장하기 위해 제약 자격에 암묵적으로 의존합니다.
---

# Constraint qualification / 约束规范 / 제약 자격

## 生活实例 + 自然语言阐述逻辑

> **生活实例**：想象一个有门的迷宫：约束规范就是“门必须间距合理且不卡死”的规则。如果门卡死（约束退化），通常的出口指示牌（KKT 条件）可能指向错误方向。
>
> **自然语言逻辑**：KKT 条件只有在可行集局部性质良好时才是必要的。约束规范是几何假设，例如 LICQ（起作用约束梯度线性无关）、MFCQ，或凸问题中的 Slater 条件，它们排除目标函数梯度无法表示为约束梯度组合的病理情形。

## 形式化定义 / Formal Definition

Consider the constrained problem

$$\min_x f(x) \quad \text{s.t.} \quad h_i(x)=0 \; (i \in \mathcal{E}), \; g_j(x) \le 0 \; (j \in \mathcal{I}).$$

A **constraint qualification** (CQ) is any condition on $\{h_i\}$ and $\{g_j\}$ at a feasible point $x^\star$ that implies the KKT conditions hold for every smooth objective $f$ having a local minimum at $x^\star$.

Common examples:

- **LICQ** (Linear Independence CQ): The gradients of active equality constraints and active inequality constraints are linearly independent at $x^\star$.
- **MFCQ** (Mangasarian-Fromovitz CQ): There exists a vector $d$ such that $\nabla h_i(x^\star)^{\top} d = 0$ and $\nabla g_j(x^\star)^{\top} d < 0$ for active inequalities.
- **Slater's condition** (for convex problems with affine equalities): There exists a strictly feasible point $x$ with $g_j(x)<0$.

## 关键符号与直觉对应

| 符号 | 名称 | 直觉含义 |
|------|------|----------|
| $\mathcal{E}$ | 等式约束指标集 | 所有等式约束的下标集合 |
| $\mathcal{I}$ | 不等式约束指标集 | 所有不等式约束的下标集合 |
| $\mathcal{A}(x^\star)$ | 起作用集 | 在 $x^\star$ 处取等号的不等式约束 |
| $\nabla g_j(x^\star)$ | 约束梯度 | 约束函数在最优点的梯度 |
| $d$ | 可行方向 | 满足约束局部线性化条件的方向 |
| LICQ | 线性无关约束规范 | 起作用约束梯度线性无关的正则条件 |

## 与其他知识点的关系

- `is_prerequisite_for` → [ent_active_set_method]
- `is_prerequisite_for` → [ent_interior_point_method]

## 参考文献

1. J. Nocedal and S. J. Wright, Numerical Optimization, 2nd ed., Springer, 2006
