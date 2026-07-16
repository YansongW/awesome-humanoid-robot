---
$id: ent_self_attention_equation
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: equation
names:
  en: Scaled Dot-Product Self-Attention
  zh: 缩放点积自注意力
  ko: 스케일드 닷프로덕트 셀프 어텐션
summary:
  en: The core equation of the Transformer that computes a weighted sum of values based on query-key compatibility.
  zh: '> 生活实例：你在读一句话时，每个字都会“回头看”整句话，并根据相关性决定把注意力放在哪些字上。例如“我把苹果吃了”中，“吃”更关注“苹果”而不是“我”。Self-attention 就是让模型自动学习这种“谁该看谁”的权重机制。缩放因子
    $1/\sqrt{d_k}$ 相当于防止大家太兴奋：如果 Query 和 Key 的维度很高，点积会容易变得极大，导致 softmax 变成“非黑即白”，模型就学不到微妙的注意力分布。 > > 自然语言逻辑：把输入序列分别投影成 Query、Key、Value
    三组向量；Query 和 Key 做点积得到相似度；用 softmax 归一化得到注意力权重；权重乘以 Value 得到输出。$QK^\top/\sqrt{d_k}$ 这一步同时完成了“匹配”和“缩放”，让训练更稳定。'
  ko: Transformer의 핵심 방정식으로, Query와 Key의 유사도에 따라 Value를 가중합합니다.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- formalism
tags:
- transformer
- attention
- deep_learning
- vla
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body restructured into standard sections by scripts/restructure_entry_bodies.py.
sources:
- id: src_vaswani_2017
  type: paper
  title: Vaswani et al., Attention Is All You Need, NeurIPS 2017
  url: https://arxiv.org/abs/1706.03762
  date: '2017-06-12'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_operator_softmax_function
  relationship: uses
  description:
    en: Self-attention uses the softmax operator to normalize attention weights.
    zh: 自注意力使用 softmax 算子对注意力权重进行归一化。
    ko: 셀프 어텐션은 어텐션 가중치를 정규화하기 위해 소프트맥스 연산자를 사용한다.
- id: ent_principle_maximum_likelihood_estimation
  relationship: derived_from
  description:
    en: The attention mechanism is trained by objectives derived from maximum likelihood estimation.
    zh: 注意力机制通过源自最大似然估计的目标函数进行训练。
    ko: 어텐션 메커니즘은 최대우도추정에서 유래한 목적 함수로 학습된다.
---

## 概述
# 缩放点积自注意力方程

## 核心内容
## 抽象

> **生活实例**：你在读一句话时，每个字都会“回头看”整句话，并根据相关性决定把注意力放在哪些字上。例如“我把苹果吃了”中，“吃”更关注“苹果”而不是“我”。Self-attention 就是让模型自动学习这种“谁该看谁”的权重机制。缩放因子 $1/\sqrt{d_k}$ 相当于防止大家太兴奋：如果 Query 和 Key 的维度很高，点积会容易变得极大，导致 softmax 变成“非黑即白”，模型就学不到微妙的注意力分布。
>
> **自然语言逻辑**：把输入序列分别投影成 Query、Key、Value 三组向量；Query 和 Key 做点积得到相似度；用 softmax 归一化得到注意力权重；权重乘以 Value 得到输出。$QK^\top/\sqrt{d_k}$ 这一步同时完成了“匹配”和“缩放”，让训练更稳定。

## 形式化定义

给定输入表示矩阵 $X \in \mathbb{R}^{n \times d_{\text{model}}}$，以及可学习投影矩阵 $W_Q, W_K, W_V$，计算：

$$
Q = X W_Q, \quad K = X W_K, \quad V = X W_V,
$$

$$
\text{Attention}(Q, K, V) = \operatorname{softmax}\!\left( \frac{Q K^\top}{\sqrt{d_k}} \right) V.
$$

其中：

- $n$：序列长度
- $d_k$：Query/Key 的维度
- $d_v$：Value 的维度（通常 $d_v = d_k$）
- $\operatorname{softmax}(z_i) = \frac{e^{z_i}}{\sum_j e^{z_j}}$

Multi-head attention 则是将上述过程在 $h$ 个不同子空间并行执行并拼接：

$$
\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h) W^O,
$$

其中 $\text{head}_i = \text{Attention}(Q W_i^Q, K W_i^K, V W_i^V)$。

## 关键符号与直觉对应

| 符号 | 名称 | 直觉含义 |
|------|------|----------|
| $Q$ | Query | “我正在问的问题” |
| $K$ | Key | “每个位置可能回答的问题标签” |
| $V$ | Value | “每个位置实际携带的信息” |
| $QK^\top$ | 点积相似度 | “问题与标签的匹配程度” |
| $1/\sqrt{d_k}$ | 缩放因子 | 防止高维点积过大导致 softmax 饱和 |
| $\operatorname{softmax}$ | 归一化指数 | 把匹配度转成“概率化”的注意力权重 |

## 与其他知识点的关系

- `uses` → Matrix multiplication, softmax operator
- `has_prerequisite` → Linear algebra（线性代数）
- `has_prerequisite` → Probability / measure theory（概率/测度论）
- `instantiates` → Transformer architecture
- `builds_on` → VLA foundation models（GR00T N1, OpenVLA, π0 等）

## 参考
- [Vaswani et al., Attention Is All You Need, NeurIPS 2017](https://arxiv.org/abs/1706.03762)

## Overview
# Scaled Dot-Product Self-Attention Equation

## Content
## Abstract

> **Life example**: When reading a sentence, each word "looks back" at the entire sentence and decides which words to focus on based on relevance. For instance, in "I ate the apple," the word "ate" pays more attention to "apple" than to "I." Self-attention allows the model to automatically learn this "who should look at whom" weighting mechanism. The scaling factor $1/\sqrt{d_k}$ prevents over-excitation: if Query and Key have high dimensions, the dot product can become extremely large, causing softmax to become "all-or-nothing," and the model fails to learn subtle attention distributions.
>
> **Natural language logic**: Project the input sequence into three sets of vectors: Query, Key, and Value; compute similarity via dot product between Query and Key; normalize with softmax to obtain attention weights; multiply weights by Value to get the output. The step $QK^\top/\sqrt{d_k}$ simultaneously accomplishes "matching" and "scaling," making training more stable.

## Formal Definition

Given the input representation matrix $X \in \mathbb{R}^{n \times d_{\text{model}}}$ and learnable projection matrices $W_Q, W_K, W_V$, compute:

$$
Q = X W_Q, \quad K = X W_K, \quad V = X W_V,
$$

$$
\text{Attention}(Q, K, V) = \operatorname{softmax}\!\left( \frac{Q K^\top}{\sqrt{d_k}} \right) V.
$$

Where:

- $n$: sequence length
- $d_k$: dimension of Query/Key
- $d_v$: dimension of Value (typically $d_v = d_k$)
- $\operatorname{softmax}(z_i) = \frac{e^{z_i}}{\sum_j e^{z_j}}$

Multi-head attention executes the above process in parallel across $h$ different subspaces and concatenates the results:

$$
\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h) W^O,
$$

where $\text{head}_i = \text{Attention}(Q W_i^Q, K W_i^K, V W_i^V)$.

## Key Symbols and Intuitive Correspondence

| Symbol | Name | Intuitive Meaning |
|--------|------|-------------------|
| $Q$ | Query | "The question I am asking" |
| $K$ | Key | "The label each position can answer" |
| $V$ | Value | "The actual information each position carries" |
| $QK^\top$ | Dot product similarity | "Degree of match between question and label" |
| $1/\sqrt{d_k}$ | Scaling factor | Prevents high-dimensional dot products from saturating softmax |
| $\operatorname{softmax}$ | Normalized exponential | Converts match scores into "probabilistic" attention weights |

## Relationships with Other Knowledge Points

- `uses` → Matrix multiplication, softmax operator
- `has_prerequisite` → Linear algebra
- `has_prerequisite` → Probability / measure theory
- `instantiates` → Transformer architecture
- `builds_on` → VLA foundation models (GR00T N1, OpenVLA, π0, etc.)

## 개요
# 스케일링된 점곱 자기 주의(Scaled Dot-Product Self-Attention) 방정식

## 핵심 내용
## 추상

> **생활 속 예시**: 문장을 읽을 때, 각 단어는 전체 문장을 "되돌아보며" 관련성에 따라 어느 단어에 주의를 기울일지 결정합니다. 예를 들어 "나는 사과를 먹었다"에서 "먹었다"는 "나"보다 "사과"에 더 주목합니다. Self-attention은 모델이 이러한 "누가 누구를 봐야 하는지"에 대한 가중치 메커니즘을 자동으로 학습하게 합니다. 스케일링 인자 $1/\sqrt{d_k}$는 너무 과도해지는 것을 방지합니다. Query와 Key의 차원이 높으면 점곱이 쉽게 매우 커져서 softmax가 "흑백 논리"가 되어 모델이 미묘한 주의 분포를 학습하지 못하게 됩니다.
>
> **자연어 논리**: 입력 시퀀스를 각각 Query, Key, Value 세 개의 벡터 그룹으로 투영합니다. Query와 Key의 점곱으로 유사도를 구하고, softmax로 정규화하여 주의 가중치를 얻습니다. 가중치에 Value를 곱하여 출력을 얻습니다. $QK^\top/\sqrt{d_k}$ 단계는 "매칭"과 "스케일링"을 동시에 수행하여 훈련을 더 안정적으로 만듭니다.

## 형식적 정의

입력 표현 행렬 $X \in \mathbb{R}^{n \times d_{\text{model}}}$과 학습 가능한 투영 행렬 $W_Q, W_K, W_V$가 주어졌을 때, 다음과 같이 계산합니다:

$$
Q = X W_Q, \quad K = X W_K, \quad V = X W_V,
$$

$$
\text{Attention}(Q, K, V) = \operatorname{softmax}\!\left( \frac{Q K^\top}{\sqrt{d_k}} \right) V.
$$

여기서:

- $n$: 시퀀스 길이
- $d_k$: Query/Key의 차원
- $d_v$: Value의 차원 (보통 $d_v = d_k$)
- $\operatorname{softmax}(z_i) = \frac{e^{z_i}}{\sum_j e^{z_j}}$

Multi-head attention은 위 과정을 $h$개의 서로 다른 부분 공간에서 병렬로 수행하고 연결합니다:

$$
\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h) W^O,
$$

여기서 $\text{head}_i = \text{Attention}(Q W_i^Q, K W_i^K, V W_i^V)$입니다.

## 주요 기호와 직관적 대응

| 기호 | 이름 | 직관적 의미 |
|------|------|----------|
| $Q$ | Query | "내가 지금 묻는 질문" |
| $K$ | Key | "각 위치가 답할 수 있는 질문 레이블" |
| $V$ | Value | "각 위치가 실제로 가진 정보" |
| $QK^\top$ | 점곱 유사도 | "질문과 레이블의 일치 정도" |
| $1/\sqrt{d_k}$ | 스케일링 인자 | 고차원 점곱이 너무 커져 softmax가 포화되는 것을 방지 |
| $\operatorname{softmax}$ | 정규화 지수 함수 | 일치도를 "확률화된" 주의 가중치로 변환 |

## 다른 지식 포인트와의 관계

- `uses` → 행렬 곱셈, softmax 연산자
- `has_prerequisite` → 선형대수학
- `has_prerequisite` → 확률/측도론
- `instantiates` → Transformer 아키텍처
- `builds_on` → VLA 기반 모델 (GR00T N1, OpenVLA, π0 등)
