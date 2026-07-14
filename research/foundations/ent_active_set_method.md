---
$id: ent_active_set_method
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: algorithm
names:
  en: Active-set method
  zh: 起作用集法
  ko: 활성 집합법
summary:
  en: An iterative optimization algorithm that tracks the set of constraints that are active at the solution and solves a
    sequence of equality-constrained subproblems.
  zh: 一种迭代优化算法，追踪在最优解处起作用（取等号）的约束集合，并通过求解一系列等式约束子问题逼近最优解。
  ko: 최적해에서 활성(등호를 만족하는) 제약 집합을 추적하고 일련의 등식 제약 부분 문제를 풀어 최적해를 접근하는 반복 최적화 알고리즘.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- method
tags:
- optimization
- constrained_optimization
- active_set
- qp
- inequality_constraints
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
related_entities:
- id: ent_constraint_qualification
  relationship: requires
  description:
    en: Reliable convergence of active-set QP iterations usually assumes a constraint qualification such as LICQ on the working
      set.
    zh: 起作用集 QP 迭代的可靠收敛通常假设工作集上满足 LICQ 等约束规范。
    ko: 활성 집합 QP 반복의 신뢰할 수 있는 수렴은 일반적으로 작업 집합에서 LICQ와 같은 제약 자격을 가정합니다.
- id: ent_interior_point_method
  relationship: is_alternative_to
  description:
    en: Interior-point methods solve the same constrained problems by staying strictly inside the feasible region rather than
      tracking active sets.
    zh: 内点法通过始终严格位于可行域内部来求解同一类约束问题，而非追踪起作用集。
    ko: 내점법은 활성 집합을 추적하는 대신 실행 가능 영역 내에서 엄격하게 머무륾며 동일한 제약 문제를 풉니다.
---
## 概述
# Active-set method / 起作用集法 / 활성 집합법

## 核心内容
## 抽象

> **生活实例**：想象拼拼图时先猜哪些块接触边框（起作用约束），只拼这些边框块，再检查内部是否有块凸出。不断交换边框块，直到整幅图完整。
>
> **自然语言逻辑**：起作用集法在每次迭代中假设哪些不等式约束取等号，然后在该工作集上求解等式约束子问题。若结果违反某个先前不起作用的约束，则将其加入工作集；若某起作用约束对应的乘子符号错误，则将其移除。重复直到满足 KKT 条件。

## 形式化定义 / Formal Definition

Consider the convex quadratic program (QP)

$$\min_x \; \frac{1}{2} x^{\top} H x + g^{\top} x \quad \text{s.t.} \quad A x = b, \; C x \le d.$$

At iteration $k$ let $\mathcal{W}_k$ be the **working set** of equality constraints and active inequality constraints. Solve

$$\min_p \; \frac{1}{2} p^{\top} H p + (H x_k + g)^{\top} p \quad \text{s.t.} \quad A p = 0, \; C_{\mathcal{W}_k} p = 0.$$

Update $x_{k+1} = x_k + \alpha_k p_k$ with a step length chosen so no inequality is violated. Add to or remove constraints from $\mathcal{W}_k$ based on blocking constraints and Lagrange-multiplier signs. Repeat until stationarity, feasibility, and dual feasibility hold.

## 关键符号与直觉对应

| 符号 | 名称 | 直觉含义 |
|------|------|----------|
| $\mathcal{W}_k$ | 工作集 | 当前被当作等式处理的约束集合 |
| $p_k$ | 搜索方向 | 在工作集约束下使目标下降的步进方向 |
| $\alpha_k$ | 步长 | 沿搜索方向移动的距离，需不违反未加入工作集的不等式 |
| $C_{\mathcal{W}_k}$ | 工作集不等式 | 当前被激活的不等式约束行 |
| $\mu_j$ | 不等式乘子 | 判断对应不等式是否应从工作集中删除的指标 |
| KKT | KKT 条件 | 最优性判定标准 |

## 与其他知识点的关系

- `requires` → [ent_constraint_qualification]
- `is_alternative_to` → [ent_interior_point_method]

## 参考文献

1. J. Nocedal and S. J. Wright, Numerical Optimization, 2nd ed., Springer, 2006

