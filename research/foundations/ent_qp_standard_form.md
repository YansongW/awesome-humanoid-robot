---
$id: "ent_qp_standard_form"
$schema: "../../data/schema/v1/entry_schema.json"
$version: 1

type: "formalism"

names:
  en: "Standard Quadratic Program (QP)"
  zh: "标准二次规划（QP）"
  ko: "표준 이차 계획법(QP)"

summary:
  en: "A convex optimization problem where a quadratic objective is minimized subject to linear equality and inequality constraints."
  zh: "在等式与不等式线性约束下最小化二次目标函数的凸优化问题。"
  ko: "등식 및 부등식 선형 제약 조건 하에서 이차 목적 함수를 최소화하는 볼록 최적화 문제."

domains:
  - "00_foundations"

layers:
  - "foundations"

functional_roles:
  - "knowledge"

theoretical_depth:
  - "formalism"

tags:
  - "optimization"
  - "quadratic_program"
  - "convex_optimization"
  - "wbc"

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-25"
  confidence: "high"
  notes: "Standard form used throughout robotics, control, and operations research."

sources:
  - id: "src_nocedal_wright_2006"
    type: "other"
    title: "J. Nocedal and S. J. Wright, Numerical Optimization, 2nd ed., Springer, 2006"
    url: "https://doi.org/10.1007/978-0-387-40065-5"
    date: "2006-01-01"
    accessed_at: "2026-06-25"

---

# 标准二次规划（QP）

## 抽象

> **生活实例**：想象你在一个房间里找一把最舒服的椅子坐下，但你必须满足两个条件：椅子要在地毯上（等式约束，精确满足），而且不能超出房间边界（不等式约束，不能越界）。如果你的“舒适度”可以用一个二次函数衡量（比如离暖气越近越舒服，但太近会烫），那么这个问题就是一个二次规划问题。
>
> **自然语言逻辑**：二次规划的目标函数由两部分组成：二次项 $x^\top H x$ 描述“曲率”带来的非线性影响，线性项 $g^\top x$ 描述“坡度”。约束是线性的，因此可行域是一个多面体。如果 $H$ 是半正定的，整个问题就像一只碗放在多边形里，最低点唯一且容易找到。

## 形式化定义

标准二次规划问题写作：

$$
\min_{x} \; \frac{1}{2} x^{\top} H x + g^{\top} x
\quad \text{s.t.} \quad A x = b, \; C x \le d.
$$

其中：

- $x \in \mathbb{R}^n$：决策变量
- $H \in \mathbb{R}^{n \times n}$：Hessian 矩阵，通常要求对称半正定（$H \succeq 0$）以保证凸性
- $g \in \mathbb{R}^n$：梯度向量
- $A \in \mathbb{R}^{m \times n}, b \in \mathbb{R}^m$：等式约束
- $C \in \mathbb{R}^{p \times n}, d \in \mathbb{R}^p$：不等式约束

若 $H$ 正定且约束可行，则存在唯一全局最优解。

## 关键符号与直觉对应

| 符号 | 名称 | 直觉含义 |
|------|------|----------|
| $x$ | 决策变量 | 要找的“最优位置” |
| $H$ | Hessian | 目标函数的“弯曲程度” |
| $g$ | Gradient | 目标函数的“坡度方向” |
| $A x = b$ | 等式约束 | 必须精确站在某条线上 |
| $C x \le d$ | 不等式约束 | 不能越过的房间边界 |

## 与其他知识点的关系

- `solved_by` → Active-set method, interior-point method
- `has_prerequisite` → KKT conditions
- `has_prerequisite` → Convex analysis / Linear algebra
- `formalizes` → Whole-body control (WBC), model predictive control (MPC), portfolio optimization, etc.
