---
$id: ent_backpropagation
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: algorithm
names:
  en: Backpropagation
  zh: 反向传播
  ko: 역전파
summary:
  en: An efficient algorithm for computing the gradient of a loss function with respect to all parameters of a feedforward neural network by applying the chain rule layer by layer in reverse order.
  zh: 一种高效算法，通过按逆序逐层应用链式法则，计算损失函数对前馈神经网络所有参数的梯度。
  ko: 피드포워드 신경망의 모든 매개변수에 대한 손실 함수의 기울기를 계산하기 위해 연쇄 법칙을 역순으로 층별로 적용하는 효율적인 알고리즘.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- method
tags:
- deep_learning
- gradient
- backpropagation
- chain_rule
- neural_network
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard foundational knowledge; reviewed against standard references.
sources:
- id: src_rumelhart_1986
  type: paper
  title: D. E. Rumelhart, G. E. Hinton, and R. J. Williams, 'Learning Representations by Back-propagating Errors', Nature, vol. 323, pp. 533–536, 1986
  url: https://doi.org/10.1038/323533a0
  date: '1986-01-01'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_chain_rule
  relationship: uses
  description:
    en: Backpropagation is essentially the systematic reverse application of the chain rule across the layers of a computational graph.
    zh: 反向传播本质上是链式法则在计算图各层上的系统性反向应用。
    ko: 역전파는 기본적으로 계산 그래프의 층을 가로지르는 연쇄 법칙의 체계적인 역방향 적용입니다.
---

# Backpropagation / 反向传播 / 역전파

## 生活实例 + 自然语言阐述逻辑

> **生活实例**：想象一排多米诺骨牌：要知道最后一块为何倒下，你问前一块，前一块再问更前一块，一直追溯到起点。反向传播正是以这种方式将误差信号反向传遍网络。
>
> **自然语言逻辑**：神经网络是许多简单可微层的复合。反向传播不独立计算每个参数的梯度，而是复用中间结果：先计算损失（前向传播），再将误差梯度从输出传回输入（反向传播），沿途累积参数梯度。

## 形式化定义 / Formal Definition

Let a neural network compute $\hat{\mathbf{y}} = f_L(f_{L-1}(\cdots f_1(\mathbf{x}; \mathbf{W}_1) \cdots; \mathbf{W}_{L-1}); \mathbf{W}_L)$, where $f_\ell$ is layer $\ell$ with parameters $\mathbf{W}_\ell$ and $\mathcal{L}(\hat{\mathbf{y}}, \mathbf{y})$ is the loss.

Define $\mathbf{z}_\ell = f_\ell(\mathbf{z}_{\ell-1}; \mathbf{W}_\ell)$. The forward pass computes $\mathbf{z}_1, \dots, \mathbf{z}_L$ and $\mathcal{L}$. The backward pass computes

$$\boldsymbol{\delta}_\ell = \frac{\partial \mathcal{L}}{\partial \mathbf{z}_\ell} = \frac{\partial \mathbf{z}_{\ell+1}}{\partial \mathbf{z}_\ell}^{\top} \boldsymbol{\delta}_{\ell+1},$$

starting from $\boldsymbol{\delta}_L = \partial \mathcal{L} / \partial \mathbf{z}_L$. Parameter gradients are

$$\frac{\partial \mathcal{L}}{\partial \mathbf{W}_\ell} = \frac{\partial \mathbf{z}_\ell}{\partial \mathbf{W}_\ell}^{\top} \boldsymbol{\delta}_\ell.$$

Because each $\boldsymbol{\delta}_\ell$ is computed once and reused for both $\mathbf{W}_\ell$ and $\boldsymbol{\delta}_{\ell-1}$, the total cost is roughly twice the cost of a forward evaluation.

## 关键符号与直觉对应

| 符号 | 名称 | 直觉含义 |
|------|------|----------|
| $\mathbf{W}_\ell$ | 第 ℓ 层参数 | 权重、偏置等可学习参数 |
| $\mathbf{z}_\ell$ | 第 ℓ 层输出 | 网络第 ℓ 层的激活值 |
| $\mathcal{L}$ | 损失函数 | 预测与真实标签之间的误差度量 |
| $\boldsymbol{\delta}_\ell$ | 第 ℓ 层误差信号 | 损失对第 ℓ 层输出的梯度 |
| $\frac{\partial \mathbf{z}_{\ell+1}}{\partial \mathbf{z}_\ell}$ | 层间雅可比 | 相邻两层输出之间的导数 |
| $L$ | 网络层数 | 网络的总层数 |

## 与其他知识点的关系

- `uses` → [ent_chain_rule]

## 参考文献

1. D. E. Rumelhart, G. E. Hinton, and R. J. Williams, 'Learning Representations by Back-propagating Errors', Nature, vol. 323, pp. 533–536, 1986
