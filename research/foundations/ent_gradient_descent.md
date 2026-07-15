---
$id: ent_gradient_descent
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: algorithm
names:
  en: Gradient Descent
  zh: 梯度下降法
  ko: 경사 하강법
summary:
  en: An iterative first-order optimization algorithm that updates parameters in the direction of the negative gradient of
    the objective.
  zh: '> **生活实例**：想象你在山上蒙着眼睛找最低点。你伸出手感受脚下哪个方向最陡，然后朝相反方向（下坡）迈一小步；走完之后再次感受，再迈一步。只要你每次步长合适，最终就会走到山谷底部。梯度下降就是这个过程的数学化：损失函数相当于山的高度，梯度相当于“最陡方向”，负梯度方向就是“下坡方向”。
    > > **自然语言逻辑**：要最小化一个可微函数，我们先算出当前位置的梯度（函数增长最快的方向），然后朝相反方向移动一小段距离。移动的距离由学习率控制。如果学习率太大，会在山谷两边来回震荡；如果太小，收敛会很慢。对凸且光滑的函数，梯度下降在合适步长下能保证收敛到全局最小值。'
  ko: 목적 함수의 음의 기울기 방향으로 매개변수를 반복적으로 업데이트하는 1차 최적화 알고리즘.
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
- gradient_descent
- machine_learning
- backpropagation
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body restructured into standard sections by scripts/restructure_entry_bodies.py.
sources:
- id: src_boyd_vandenberghe_2004
  type: other
  title: S. Boyd and L. Vandenberghe, Convex Optimization, Cambridge University Press, 2004
  url: https://web.stanford.edu/~boyd/cvxbook/
  date: '2004-01-01'
  accessed_at: '2026-06-25'
---

## 概述
# 梯度下降法

## 核心内容
## 抽象

> **生活实例**：想象你在山上蒙着眼睛找最低点。你伸出手感受脚下哪个方向最陡，然后朝相反方向（下坡）迈一小步；走完之后再次感受，再迈一步。只要你每次步长合适，最终就会走到山谷底部。梯度下降就是这个过程的数学化：损失函数相当于山的高度，梯度相当于“最陡方向”，负梯度方向就是“下坡方向”。
>
> **自然语言逻辑**：要最小化一个可微函数，我们先算出当前位置的梯度（函数增长最快的方向），然后朝相反方向移动一小段距离。移动的距离由学习率控制。如果学习率太大，会在山谷两边来回震荡；如果太小，收敛会很慢。对凸且光滑的函数，梯度下降在合适步长下能保证收敛到全局最小值。

## 形式化定义

给定可微目标函数 $L(\theta)$，梯度下降迭代为：

$$
\theta_{t+1} = \theta_t - \eta \nabla_\theta L(\theta_t),
$$

其中：

- $\theta_t$：第 $t$ 步的参数
- $\eta > 0$：学习率（步长）
- $\nabla_\theta L(\theta_t)$：损失函数关于参数的梯度

对于凸且 $L$-光滑（梯度 Lipschitz 连续）的函数，若取固定步长 $\eta \le 1/L$，则收敛速率为 $O(1/T)$：

$$
L(\theta_T) - L(\theta^\star) \le \frac{\|\theta_0 - \theta^\star\|^2}{2 \eta T}.
$$

## 关键符号与直觉对应

| 符号 | 名称 | 直觉含义 |
|------|------|----------|
| $\theta$ | 参数 | 我们在山上所处的位置 |
| $L(\theta)$ | 损失/目标函数 | 山的高度 |
| $\nabla_\theta L$ | 梯度 | 最陡上升方向 |
| $-\nabla_\theta L$ | 负梯度 | 最陡下降方向 |
| $\eta$ | 学习率 | 每一步迈多大 |
| $T$ | 迭代次数 | 走了多少步 |

## 与其他知识点的关系

- `uses` → Chain rule（链式法则，通过 backpropagation 计算梯度）
- `uses` → Automatic differentiation（自动微分实现）
- `builds_on` → Stochastic gradient descent（随机梯度下降）
- `builds_on` → Adam optimizer（带动量的改进版）
- `minimizes` → Behavior cloning objective, cross-entropy loss, MSE loss
- `has_prerequisite` → Multivariable calculus

## 参考
- [S. Boyd and L. Vandenberghe, Convex Optimization, Cambridge University Press, 2004](https://web.stanford.edu/~boyd/cvxbook/)


