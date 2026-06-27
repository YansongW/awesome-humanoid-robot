---
$id: ent_operator_softmax_function
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: operator
names:
  en: Softmax Function
  zh: Softmax 函数
  ko: 소프트맥스 함수
summary:
  en: A differentiable operator that converts a vector of real-valued scores into a probability distribution, emphasizing the largest values while keeping all probabilities positive and summing to one.
  zh: 一种可微算子，将实值分数向量转换为概率分布，突出最大值，同时保持所有概率为正且和为 1。
  ko: 실수 값 점수 벡터를 확률 분포로 변환하여 가장 큰 값을 강조하면서도 모든 확률이 양수이고 합이 1이 되도록 하는 미분 가능한 연산자이다.
domains:
- 00_foundations
- 07_ai_models_algorithms
layers:
- foundations
- intelligence
functional_roles:
- knowledge
tags:
- softmax
- probability_distribution
- attention
- transformer
- vla
theoretical_depth:
- formalism
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Standard operator in machine learning and attention mechanisms.
sources:
- id: src_bishop_2006
  type: paper
  title: 'Bishop, Pattern Recognition and Machine Learning'
  url: https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/
  date: '2006'
  accessed_at: '2026-06-26'
---

## 抽象

> **生活实例**：假设一次考试后，老师要把百分制分数转成排名比例。Softmax 就像一个“温和版的名次转换器”：最高分得到最大比例，但其他人也保留一小部分，而不是直接被压到零。
>
> **自然语言逻辑**：对任意实数向量先取指数（保证正数），再除以总和（保证和为 1）；指数会放大差异，但不会像 argmax 那样完全抹杀非最大值的信息，因此既能“突出重点”又能保持可微分。

## Overview

The softmax operator is ubiquitous in deep learning. It turns logits produced by a linear layer into a categorical probability distribution. In Transformers, softmax appears inside the attention mechanism, where it normalizes query-key compatibility scores into attention weights.

## Formal Definition

Given a vector \(z = (z_1, \dots, z_n) \in \mathbb{R}^n\), the softmax function \(\sigma: \mathbb{R}^n \to \mathbb{R}^n\) is defined component-wise as:

$$
\sigma(z)_i = \frac{e^{z_i}}{\sum_{j=1}^{n} e^{z_j}} \quad \text{for } i = 1, \dots, n.
$$

Properties:

- \(0 < \sigma(z)_i < 1\) for all \(i\).
- \(\sum_{i=1}^{n} \sigma(z)_i = 1\).
- Softmax is invariant to additive shifts: \(\sigma(z + c) = \sigma(z)\) for any scalar \(c\).

## Symbol Intuition

| 符号 | 名称 | 直觉含义 |
|------|------|----------|
| \(z_i\) | Logit / 分数 | 模型对第 \(i\) 个候选的“原始偏好” |
| \(e^{z_i}\) | 未归一化概率 | 把分数转成正数并放大差异 |
| \(\sum_j e^{z_j}\) | 归一化常数 | 所有候选的“总偏好” |
| \(\sigma(z)_i\) | Softmax 概率 | 第 \(i\) 个候选的最终注意力/选择权重 |

## Relevance to Humanoid Robotics

In humanoid VLAs, softmax converts decoder logits into action-token probabilities and normalizes attention weights when fusing visual, linguistic, and proprioceptive cues. It is the operator that turns raw scores into interpretable, probabilistic decisions.
