---
$id: ent_interior_point_method
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: algorithm
names:
  en: Interior-point method
  zh: 内点法
  ko: 내점법
summary:
  en: A family of optimization algorithms that solve constrained problems by following a smooth central path strictly inside the feasible region via barrier or penalty functions.
  zh: 一类优化算法，通过障碍或惩罚函数在可行域内部沿光滑中心路径求解约束优化问题。
  ko: 장벽 또는 페널티 함수를 통해 실행 가능 영역 내에서 매끄러운 중심 경로를 따라 제약 최적화 문제를 푸는 최적화 알고리즘 집합.
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
- interior_point
- barrier_method
- central_path
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
- id: ent_constraint_qualification
  relationship: requires
  description:
    en: Convergence theory for interior-point methods typically assumes constraint qualifications to ensure the KKT system is well-posed.
    zh: 内点法的收敛理论通常假设约束规范，以保证 KKT 系统良态。
    ko: 내점법의 수렴 이론은 일반적으로 KKT 체계가 양호하게 정의되도록 제약 자격을 가정합니다.
- id: ent_active_set_method
  relationship: is_alternative_to
  description:
    en: Active-set methods explicitly track binding constraints, whereas interior-point methods avoid the boundary entirely via barrier terms.
    zh: 起作用集法显式追踪起作用约束，而内点法通过障碍项完全避开边界。
    ko: 활성 집합법은 명시적으로 구속 제약을 추적하는 반면, 내점법은 장벽 항을 통해 경계를 완전히 피합니다.
---

# Interior-point method / 内点法 / 내점법

## 抽象

> **生活实例**：想象在走廊里始终沿正中间行走：不触碰任何墙壁，沿着虚线中线前进。内点法以同样方式求解问题，与每条约束边界保持安全距离。
>
> **自然语言逻辑**：内点法用光滑障碍项替代不等式约束，当接近边界时障碍项趋于无穷。逐渐减小障碍参数，迭代点沿中心路径趋向约束最优解。现代原始-对偶变体同时更新原始变量、对偶变量和障碍参数，使用牛顿步。

## 形式化定义 / Formal Definition

Consider

$$\min_x f(x) \quad \text{s.t.} \quad h(x)=0, \; g(x) \le 0.$$

Replace inequalities by a logarithmic barrier:

$$\min_{x} \; f(x) - \mu \sum_j \log(-g_j(x)) \quad \text{s.t.} \quad h(x)=0,$$

with barrier parameter $\mu > 0$. The perturbed KKT conditions are

$$\nabla f(x) + \nabla h(x)\lambda + \nabla g(x)\mu = 0,$$
$$h(x) = 0,$$
$$g_j(x) \mu_j + \mu = 0 \quad \forall j,$$

where $\mu_j$ are dual variables for the inequalities. Primal-dual interior-point methods apply damped Newton steps to this system while driving $\mu \to 0$.

## 关键符号与直觉对应

| 符号 | 名称 | 直觉含义 |
|------|------|----------|
| $\mu$ | 障碍参数 | 控制迭代点与约束边界距离的标量 |
| $\log(-g_j(x))$ | 对数障碍 | 接近边界时趋于无穷的惩罚项 |
| $\lambda$ | 等式对偶变量 | 等式约束对应的 Lagrange 乘子 |
| $\mu_j$ | 不等式对偶变量 | 不等式约束对应的非负乘子 |
| $\nabla h(x)$ | 等式约束雅可比 | 等式约束梯度组成的矩阵 |
| Central path | 中心路径 | 不同障碍参数下最优解形成的曲线 |

## 与其他知识点的关系

- `requires` → [ent_constraint_qualification]
- `is_alternative_to` → [ent_active_set_method]

## 参考文献

1. J. Nocedal and S. J. Wright, Numerical Optimization, 2nd ed., Springer, 2006
