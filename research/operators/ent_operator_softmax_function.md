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
  en: A differentiable operator that converts a vector of real-valued scores into a probability distribution, emphasizing
    the largest values while keeping all probabilities positive and summing to one.
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
  notes: Standard operator in machine learning and attention mechanisms. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_bishop_2006
  type: paper
  title: Bishop, Pattern Recognition and Machine Learning
  url: https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/
  date: '2006'
  accessed_at: '2026-06-26'
---

## 概述
一种可微算子，将实值分数向量转换为概率分布，突出最大值，同时保持所有概率为正且和为 1。

## 核心内容
### Softmax 函数的定义与定位
Softmax 函数属于 **运营商** 类型，英文名称为 *Softmax Function*。
一种可微算子，将实值分数向量转换为概率分布，突出最大值，同时保持所有概率为正且和为 1。

### Softmax 函数的关键信息
以下整理了关于Softmax 函数的详细说明，供中英文读者参考。

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

| Symbol | Name | Intuition |
|--------|------|-----------|
| \(z_i\) | Logit / score | The model's raw preference for candidate \(i\). |
| \(e^{z_i}\) | Unnormalized probability | Converts the score to a positive value and amplifies differences. |
| \(\sum_j e^{z_j}\) | Normalization constant | The total preference across all candidates. |
| \(\sigma(z)_i\) | Softmax probability | The final attention / selection weight for candidate \(i\). |

## 符号直觉

| 符号 | 名称 | 直觉含义 |
|------|------|----------|
| \(z_i\) | Logit / 分数 | 模型对第 \(i\) 个候选的“原始偏好” |
| \(e^{z_i}\) | 未归一化概率 | 把分数转成正数并放大差异 |
| \(\sum_j e^{z_j}\) | 归一化常数 | 所有候选的“总偏好” |
| \(\sigma(z)_i\) | Softmax 概率 | 第 \(i\) 个候选的最终注意力/选择权重 |

## Relevance to Humanoid Robotics

In humanoid VLAs, softmax converts decoder logits into action-token probabilities and normalizes attention weights when fusing visual, linguistic, and proprioceptive cues. It is the operator that turns raw scores into interpretable, probabilistic decisions.

## 参考
- [Bishop, Pattern Recognition and Machine Learning](https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/)

Softmax 函数的相关技术仍在快速发展。从系统科学角度看，它与其他operator相互耦合，共同决定了人形机器人的整体性能。深入理解其原理、边界条件与工程约束，是将实验室样机转化为可量产产品的必要环节。

## 개요
실수 값 점수 벡터를 확률 분포로 변환하는 미분 가능 연산자로, 최댓값을 강조하면서도 모든 확률이 양수이고 합이 1이 되도록 유지합니다.

## 핵심 내용
### Softmax 함수의 정의와 위치
Softmax 함수는 **연산자** 유형에 속하며, 영문 명칭은 *Softmax Function*입니다.
실수 값 점수 벡터를 확률 분포로 변환하는 미분 가능 연산자로, 최댓값을 강조하면서도 모든 확률이 양수이고 합이 1이 되도록 유지합니다.

### Softmax 함수의 주요 정보
다음은 Softmax 함수에 대한 상세 설명을 정리한 것으로, 중·영문 독자 모두 참고할 수 있습니다.

## 추상

> **생활 예시**: 시험 후 교사가 백분율 점수를 순위 비율로 변환해야 한다고 가정해 보세요. Softmax는 "온화한 순위 변환기"와 같습니다. 최고 점수가 가장 큰 비율을 차지하지만, 다른 점수들도 완전히 0으로 압축되지 않고 일부를 유지합니다.
>
> **자연어 논리**: 임의의 실수 벡터에 대해 먼저 지수를 취하고(양수 보장), 그런 다음 총합으로 나눕니다(합이 1이 되도록 보장). 지수는 차이를 증폭시키지만, argmax처럼 비최댓값 정보를 완전히 소멸시키지 않으므로 "핵심을 강조"하면서도 미분 가능성을 유지할 수 있습니다.

## 기호 직관

| 기호 | 명칭 | 직관적 의미 |
|------|------|----------|
| \(z_i\) | 로짓 / 점수 | 모델이 \(i\)번째 후보에 대한 "원시 선호도" |
| \(e^{z_i}\) | 비정규화 확률 | 점수를 양수로 변환하고 차이를 증폭 |
| \(\sum_j e^{z_j}\) | 정규화 상수 | 모든 후보의 "총 선호도" |
| \(\sigma(z)_i\) | Softmax 확률 | \(i\)번째 후보의 최종 주의/선택 가중치 |
