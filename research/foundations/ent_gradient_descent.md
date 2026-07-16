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
  zh: '> 生活实例：想象你在山上蒙着眼睛找最低点。你伸出手感受脚下哪个方向最陡，然后朝相反方向（下坡）迈一小步；走完之后再次感受，再迈一步。只要你每次步长合适，最终就会走到山谷底部。梯度下降就是这个过程的数学化：损失函数相当于山的高度，梯度相当于“最陡方向”，负梯度方向就是“下坡方向”。
    > > 自然语言逻辑：要最小化一个可微函数，我们先算出当前位置的梯度（函数增长最快的方向），然后朝相反方向移动一小段距离。移动的距离由学习率控制。如果学习率太大，会在山谷两边来回震荡；如果太小，收敛会很慢。对凸且光滑的函数，梯度下降在合适步长下能保证收敛到全局最小值。'
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

## Overview
# Gradient Descent

## Content
## Abstraction

> **Life Example**: Imagine you are blindfolded on a mountain trying to find the lowest point. You reach out to feel which direction is steepest, then take a small step in the opposite direction (downhill). After stepping, you feel again and take another step. As long as your step size is appropriate each time, you will eventually reach the valley floor. Gradient descent is the mathematical version of this process: the loss function corresponds to the mountain's height, the gradient corresponds to the "steepest direction," and the negative gradient direction is the "downhill direction."
>
> **Natural Language Logic**: To minimize a differentiable function, we first compute the gradient at the current position (the direction of fastest increase of the function), then move a small distance in the opposite direction. The distance moved is controlled by the learning rate. If the learning rate is too large, it will oscillate back and forth across the valley; if too small, convergence will be very slow. For convex and smooth functions, gradient descent with an appropriate step size is guaranteed to converge to the global minimum.

## Formal Definition

Given a differentiable objective function $L(\theta)$, the gradient descent iteration is:

$$
\theta_{t+1} = \theta_t - \eta \nabla_\theta L(\theta_t),
$$

where:

- $\theta_t$: parameters at step $t$
- $\eta > 0$: learning rate (step size)
- $\nabla_\theta L(\theta_t)$: gradient of the loss function with respect to the parameters

For a convex and $L$-smooth (gradient Lipschitz continuous) function, if a fixed step size $\eta \le 1/L$ is used, the convergence rate is $O(1/T)$:

$$
L(\theta_T) - L(\theta^\star) \le \frac{\|\theta_0 - \theta^\star\|^2}{2 \eta T}.
$$

## Key Symbols and Intuitive Correspondence

| Symbol | Name | Intuitive Meaning |
|--------|------|-------------------|
| $\theta$ | Parameters | Our position on the mountain |
| $L(\theta)$ | Loss/Objective Function | Mountain height |
| $\nabla_\theta L$ | Gradient | Direction of steepest ascent |
| $-\nabla_\theta L$ | Negative Gradient | Direction of steepest descent |
| $\eta$ | Learning Rate | How large each step is |
| $T$ | Number of Iterations | How many steps taken |

## Relationships with Other Knowledge Points

- `uses` → Chain rule (computing gradients via backpropagation)
- `uses` → Automatic differentiation (implementation via autodiff)
- `builds_on` → Stochastic gradient descent
- `builds_on` → Adam optimizer (improved version with momentum)
- `minimizes` → Behavior cloning objective, cross-entropy loss, MSE loss
- `has_prerequisite` → Multivariable calculus

## 개요
# 경사 하강법

## 핵심 내용
## 추상

> **생활 예시**: 산에서 눈을 가린 채 가장 낮은 지점을 찾는다고 상상해보세요. 손을 뻗어 어느 방향의 경사가 가장 가파른지 느낀 후, 반대 방향(내리막)으로 작은 걸음을 내딛습니다. 걸음을 내딛은 후 다시 느끼고, 다시 한 걸음 내딛습니다. 매번 보폭이 적절하기만 하면 결국 계곡 바닥에 도달할 수 있습니다. 경사 하강법은 이 과정을 수학적으로 표현한 것입니다. 손실 함수는 산의 높이에 해당하고, 경사는 "가장 가파른 방향"에 해당하며, 음의 경사 방향은 "내리막 방향"입니다.
>
> **자연어 논리**: 미분 가능한 함수를 최소화하기 위해, 먼저 현재 위치의 경사(함수가 가장 빠르게 증가하는 방향)를 계산한 후, 반대 방향으로 작은 거리만큼 이동합니다. 이동 거리는 학습률에 의해 제어됩니다. 학습률이 너무 크면 계곡 양쪽에서 진동하게 되고, 너무 작으면 수렴 속도가 매우 느려집니다. 볼록하고 매끄러운 함수의 경우, 경사 하강법은 적절한 보폭에서 전역 최솟값으로 수렴함을 보장할 수 있습니다.

## 형식적 정의

미분 가능한 목적 함수 $L(\theta)$가 주어졌을 때, 경사 하강법의 반복은 다음과 같습니다:

$$
\theta_{t+1} = \theta_t - \eta \nabla_\theta L(\theta_t),
$$

여기서:

- $\theta_t$: $t$번째 단계의 매개변수
- $\eta > 0$: 학습률(보폭)
- $\nabla_\theta L(\theta_t)$: 매개변수에 대한 손실 함수의 경사

볼록하고 $L$-매끄러운(경사가 Lipschitz 연속) 함수의 경우, 고정 보폭 $\eta \le 1/L$을 사용하면 수렴 속도는 $O(1/T)$입니다:

$$
L(\theta_T) - L(\theta^\star) \le \frac{\|\theta_0 - \theta^\star\|^2}{2 \eta T}.
$$

## 주요 기호와 직관적 대응

| 기호 | 이름 | 직관적 의미 |
|------|------|----------|
| $\theta$ | 매개변수 | 산에서 우리가 위치한 지점 |
| $L(\theta)$ | 손실/목적 함수 | 산의 높이 |
| $\nabla_\theta L$ | 경사 | 가장 가파른 상승 방향 |
| $-\nabla_\theta L$ | 음의 경사 | 가장 가파른 하강 방향 |
| $\eta$ | 학습률 | 각 걸음의 크기 |
| $T$ | 반복 횟수 | 걸음 수 |

## 다른 지식 포인트와의 관계

- `uses` → 연쇄 법칙(Chain rule, 역전파를 통해 경사 계산)
- `uses` → 자동 미분(Automatic differentiation, 구현)
- `builds_on` → 확률적 경사 하강법(Stochastic gradient descent)
- `builds_on` → Adam 최적화기(모멘텀이 추가된 개선 버전)
- `minimizes` → 행동 복제 목적 함수, 교차 엔트로피 손실, 평균 제곱 오차 손실
- `has_prerequisite` → 다변수 미적분학
