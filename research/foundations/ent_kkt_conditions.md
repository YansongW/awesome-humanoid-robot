---
$id: "ent_kkt_conditions"
$schema: "../../data/schema/v1/entry_schema.json"
$version: 1

type: "theorem"

names:
  en: "Karush-Kuhn-Tucker (KKT) Conditions"
  zh: "Karush-Kuhn-Tucker（KKT）条件"
  ko: "Karush-Kuhn-Tucker (KKT) 조건"

summary:
  en: "Necessary (and sufficient under convexity/constraint qualification) optimality conditions for constrained nonlinear programs."
  zh: "带约束非线性规划的最优性必要条件（在凸性与约束规范下也是充分条件）。"
  ko: "제약이 있는 비선형 계획법의 최적성 필요조건(볼록성 및 제약 자격이 있으면 충분조건이기도 함)."

domains:
  - "00_foundations"

layers:
  - "foundations"

functional_roles:
  - "knowledge"

theoretical_depth:
  - "principle"

tags:
  - "optimization"
  - "constrained_optimization"
  - "lagrange_multipliers"
  - "kkt"

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-25"
  confidence: "high"
  notes: "Standard result in constrained optimization; documented in standard textbooks."

sources:
  - id: "src_nocedal_wright_2006"
    type: "other"
    title: "J. Nocedal and S. J. Wright, Numerical Optimization, 2nd ed., Springer, 2006"
    url: "https://doi.org/10.1007/978-0-387-40065-5"
    date: "2006-01-01"
    accessed_at: "2026-06-25"

---

# Karush-Kuhn-Tucker（KKT）条件

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
