---
$id: ent_chain_rule
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: theorem
names:
  en: Chain rule
  zh: 链式法则
  ko: 연쇄 법칙
summary:
  en: A fundamental calculus rule that gives the derivative of a composition of functions as the product of the derivatives of the composed functions.
  zh: 一个基本微积分法则，给出复合函数导数等于各组成函数导数的乘积。
  ko: 함수의 합성에 대한 도함수를 구성 함수들의 도함수 곱으로 주는 기본 미적분 법칙.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- foundation
tags:
- calculus
- differentiation
- chain_rule
- backpropagation
- composition
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard foundational knowledge; reviewed against standard references.
sources:
- id: src_rudin_1976
  type: other
  title: W. Rudin, Principles of Mathematical Analysis, 3rd ed., McGraw-Hill, 1976
  url: https://doi.org/10.2307/2683801
  date: '1976-01-01'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_backpropagation
  relationship: is_prerequisite_for
  description:
    en: Backpropagation applies the chain rule repeatedly to compute gradients of a loss with respect to all network parameters.
    zh: 反向传播反复应用链式法则，计算损失对所有网络参数的梯度。
    ko: 역전파는 손실에 대한 모든 네트워크 매개변수의 기울기를 계산하기 위해 연쇄 법칙을 반복적으로 적용합니다.
---

# Chain rule / 链式法则 / 연쇄 법칙

## 抽象

> **生活实例**：想象一连串齿轮：最后一个齿轮的转速取决于每对相邻齿轮之间的齿比。链式法则指出总齿比等于各齿比的乘积。
>
> **自然语言逻辑**：大多数有意义的函数由简单函数复合而成。链式法则使我们能够计算输入的微小变化如何通过复合的每一层传播，从而产生输出的变化。它是反向传播和灵敏度分析的数学引擎。

## 形式化定义 / Formal Definition

Let $f: \mathbb{R}^n \to \mathbb{R}^m$ and $g: \mathbb{R}^m \to \mathbb{R}^p$ be differentiable functions. The derivative of the composition $h = g \circ f$ at $\mathbf{x}$ is the matrix product

$$Dh(\mathbf{x}) = Dg(f(\mathbf{x})) \cdot Df(\mathbf{x}).$$

For real-valued functions of one variable,

$$\frac{d}{dx} g(f(x)) = g'(f(x)) \, f'(x).$$

For nested vector functions $\mathbf{y} = \mathbf{f}(\mathbf{x})$, $z = g(\mathbf{y})$ the gradient with respect to $\mathbf{x}$ is

$$\nabla_\mathbf{x} z = \bigl(Df(\mathbf{x})\bigr)^{\top} \nabla_\mathbf{y} g(\mathbf{y}).$$

## 关键符号与直觉对应

| 符号 | 名称 | 直觉含义 |
|------|------|----------|
| $f, g$ | 可微函数 | 构成复合的函数 |
| $Dh$ | 复合函数导数 | 输出对输入的雅可比矩阵 |
| $Df$ | 雅可比矩阵 | 函数各分量对输入的偏导数矩阵 |
| $g'(f(x))$ | 外层导数 | 在外层函数求值点处的导数 |
| $f'(x)$ | 内层导数 | 内层函数在输入处的导数 |
| $\nabla$ | 梯度 | 多元函数各偏导数组成的向量 |

## 与其他知识点的关系

- `is_prerequisite_for` → [ent_backpropagation]

## 参考文献

1. W. Rudin, Principles of Mathematical Analysis, 3rd ed., McGraw-Hill, 1976
