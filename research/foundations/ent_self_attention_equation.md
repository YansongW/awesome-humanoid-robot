---
$id: "ent_self_attention_equation"
$schema: "../../data/schema/v1/entry_schema.json"
$version: 1

type: "equation"

names:
  en: "Scaled Dot-Product Self-Attention"
  zh: "缩放点积自注意力"
  ko: "스케일드 닷프로덕트 셀프 어텐션"

summary:
  en: "The core equation of the Transformer that computes a weighted sum of values based on query-key compatibility."
  zh: "Transformer 的核心方程，根据 Query 与 Key 的相似度对 Value 做加权求和。"
  ko: "Transformer의 핵심 방정식으로, Query와 Key의 유사도에 따라 Value를 가중합합니다."

domains:
  - "00_foundations"

layers:
  - "foundations"

functional_roles:
  - "knowledge"

theoretical_depth:
  - "formalism"

tags:
  - "transformer"
  - "attention"
  - "deep_learning"
  - "vla"

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-25"
  confidence: "high"
  notes: "Standard equation from Vaswani et al. 2017."

sources:
  - id: "src_vaswani_2017"
    type: "paper"
    title: "Vaswani et al., Attention Is All You Need, NeurIPS 2017"
    url: "https://arxiv.org/abs/1706.03762"
    date: "2017-06-12"
    accessed_at: "2026-06-25"
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

# 缩放点积自注意力方程

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
