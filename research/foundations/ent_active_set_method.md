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
  zh: '> 生活实例：想象拼拼图时先猜哪些块接触边框（起作用约束），只拼这些边框块，再检查内部是否有块凸出。不断交换边框块，直到整幅图完整。 > > 自然语言逻辑：起作用集法在每次迭代中假设哪些不等式约束取等号，然后在该工作集上求解等式约束子问题。若结果违反某个先前不起作用的约束，则将其加入工作集；若某起作用约束对应的乘子符号错误，则将其移除。重复直到满足
    KKT 条件。'
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

## 参考
- https://doi.org/10.1007/978-0-387-40065-5

## Overview
# Active-set method / 起作用集法 / 활성 집합법

## Content
## Abstract

> **Life example**: Imagine solving a jigsaw puzzle by first guessing which pieces touch the border (active constraints), assembling only those border pieces, then checking if any inner piece protrudes. Repeatedly swap border pieces until the entire picture is complete.
>
> **Natural language logic**: The active-set method assumes at each iteration which inequality constraints are active (hold with equality), then solves an equality-constrained subproblem on that working set. If the result violates a previously inactive constraint, it is added to the working set; if the multiplier sign for an active constraint is incorrect, it is removed. Repeat until the KKT conditions are satisfied.

## Formal Definition

Consider the convex quadratic program (QP)

$$\min_x \; \frac{1}{2} x^{\top} H x + g^{\top} x \quad \text{s.t.} \quad A x = b, \; C x \le d.$$

At iteration $k$ let $\mathcal{W}_k$ be the **working set** of equality constraints and active inequality constraints. Solve

$$\min_p \; \frac{1}{2} p^{\top} H p + (H x_k + g)^{\top} p \quad \text{s.t.} \quad A p = 0, \; C_{\mathcal{W}_k} p = 0.$$

Update $x_{k+1} = x_k + \alpha_k p_k$ with a step length chosen so no inequality is violated. Add to or remove constraints from $\mathcal{W}_k$ based on blocking constraints and Lagrange-multiplier signs. Repeat until stationarity, feasibility, and dual feasibility hold.

## Key Symbols and Intuitive Correspondence

| Symbol | Name | Intuitive Meaning |
|--------|------|-------------------|
| $\mathcal{W}_k$ | Working set | Set of constraints currently treated as equalities |
| $p_k$ | Search direction | Step direction that decreases the objective under working-set constraints |
| $\alpha_k$ | Step length | Distance moved along the search direction, ensuring no violation of inequalities not in the working set |
| $C_{\mathcal{W}_k}$ | Working-set inequalities | Rows of inequality constraints currently activated |
| $\mu_j$ | Inequality multiplier | Indicator for whether the corresponding inequality should be removed from the working set |
| KKT | KKT conditions | Optimality criteria |

## Relationships with Other Knowledge Points

- `requires` → [ent_constraint_qualification]
- `is_alternative_to` → [ent_interior_point_method]

## References

1. J. Nocedal and S. J. Wright, Numerical Optimization, 2nd ed., Springer, 2006

## 개요
# Active-set method / 起作用集法 / 활성 집합법

## 핵심 내용
## 추상

> **생활 예시**: 퍼즐을 맞출 때 먼저 어떤 조각이 테두리에 닿는지(작용 제약) 추측하여 테두리 조각만 맞추고, 내부에 튀어나온 조각이 있는지 확인하는 과정을 상상해보세요. 테두리 조각을 계속 교체하면서 전체 그림이 완성될 때까지 반복합니다.
>
> **자연어 논리**: 활성 집합법은 각 반복에서 어떤 부등식 제약이 등호를 취하는지 가정한 후, 해당 작업 집합에서 등식 제약 하위 문제를 해결합니다. 결과가 이전에 작용하지 않았던 제약을 위반하면 해당 제약을 작업 집합에 추가하고, 특정 작용 제약에 대응하는 승수의 부호가 잘못된 경우 이를 제거합니다. KKT 조건이 충족될 때까지 반복합니다.

## 형식적 정의 / Formal Definition

볼록 이차 계획법(QP)을 고려합니다.

$$\min_x \; \frac{1}{2} x^{\top} H x + g^{\top} x \quad \text{s.t.} \quad A x = b, \; C x \le d.$$

반복 $k$에서 $\mathcal{W}_k$를 등식 제약과 활성 부등식 제약의 **작업 집합**이라고 합니다. 다음을 해결합니다.

$$\min_p \; \frac{1}{2} p^{\top} H p + (H x_k + g)^{\top} p \quad \text{s.t.} \quad A p = 0, \; C_{\mathcal{W}_k} p = 0.$$

어떤 부등식도 위반되지 않도록 선택된 보폭으로 $x_{k+1} = x_k + \alpha_k p_k$를 업데이트합니다. 차단 제약과 라그랑주 승수 부호에 따라 $\mathcal{W}_k$에 제약을 추가하거나 제거합니다. 정상성, 실행 가능성, 쌍대 실행 가능성이 충족될 때까지 반복합니다.

## 주요 기호와 직관적 대응

| 기호 | 이름 | 직관적 의미 |
|------|------|----------|
| $\mathcal{W}_k$ | 작업 집합 | 현재 등식으로 처리되는 제약 집합 |
| $p_k$ | 탐색 방향 | 작업 집합 제약 하에서 목적 함수를 감소시키는 진행 방향 |
| $\alpha_k$ | 보폭 | 탐색 방향을 따라 이동하는 거리, 작업 집합에 추가되지 않은 부등식을 위반하지 않아야 함 |
| $C_{\mathcal{W}_k}$ | 작업 집합 부등식 | 현재 활성화된 부등식 제약 행 |
| $\mu_j$ | 부등식 승수 | 해당 부등식을 작업 집합에서 제거해야 하는지 판단하는 지표 |
| KKT | KKT 조건 | 최적성 판단 기준 |

## 다른 지식 포인트와의 관계

- `requires` → [ent_constraint_qualification]
- `is_alternative_to` → [ent_interior_point_method]

## 참고 문헌

1. J. Nocedal and S. J. Wright, Numerical Optimization, 2nd ed., Springer, 2006
