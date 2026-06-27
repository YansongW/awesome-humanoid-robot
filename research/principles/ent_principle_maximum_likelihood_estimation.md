---
$id: ent_principle_maximum_likelihood_estimation
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: principle
names:
  en: Maximum Likelihood Estimation
  zh: 最大似然估计
  ko: 최대우도추정
summary:
  en: A statistical principle that chooses model parameters to maximize the probability of observing the training data, forming the basis of cross-entropy and next-token prediction losses.
  zh: 一种统计原理，选择使训练数据出现概率最大的模型参数，是交叉熵和下一个 token 预测损失的基础。
  ko: 훈련 데이터가 관측될 확률을 최대화하는 모델 매개변수를 선택하는 통계적 원리로, 교차 엔트로피와 다음 토큰 예측 손실의 기초가 된다.
domains:
- 00_foundations
- 07_ai_models_algorithms
layers:
- foundations
- intelligence
functional_roles:
- knowledge
tags:
- maximum_likelihood
- cross_entropy
- next_token_prediction
- statistics
- vla
theoretical_depth:
- principle
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Foundational principle for training autoregressive models.
sources:
- id: src_bishop_2006
  type: paper
  title: 'Bishop, Pattern Recognition and Machine Learning'
  url: https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/
  date: '2006'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_foundation_probability_theory
  relationship: has_prerequisite
  description:
    en: Maximum likelihood estimation is built on probability theory and random variables.
    zh: 最大似然估计建立在概率论和随机变量的基础之上。
    ko: 최대우도추정은 확률론과 확률 변수에 기반한다.
---

## 抽象

> **生活实例**：警察根据线索找嫌疑人，最合理的假设是“最可能产生这些线索的人”。最大似然估计就是这个道理：给定观测到的数据，选择那个最可能生成这些数据的参数。
>
> **自然语言逻辑**：假设数据由某个带参数的分布生成；定义似然函数为该分布在观测数据上的联合概率；通过优化找到使似然最大的参数；在分类和序列建模中，这等价于最小化交叉熵损失。

## Overview

Maximum likelihood estimation (MLE) is a cornerstone of statistical learning. For a dataset \(\mathcal{D} = \{x_i\}_{i=1}^{N}\) assumed to be drawn from a parametric distribution \(p(x; \theta)\), MLE finds:

$$
\hat{\theta}_{\text{MLE}} = \arg\max_{\theta} \prod_{i=1}^{N} p(x_i; \theta)
= \arg\min_{\theta} -\sum_{i=1}^{N} \log p(x_i; \theta).
$$

For discrete action-token prediction, this reduces to minimizing the cross-entropy between the empirical data distribution and the model's predicted distribution.

## Key Characteristics

- MLE provides a principled objective for probabilistic models.
- Minimizing negative log-likelihood is equivalent to minimizing cross-entropy for categorical data.
- It assumes the model family contains a distribution close to the true data distribution.
- With enough data, MLE estimators are consistent and asymptotically efficient under regularity conditions.

## Relevance to Humanoid Robotics

VLAs for humanoid robots are trained by maximizing the likelihood of expert demonstrations. This principle justifies the next-token prediction objective used to learn language-conditioned action policies, making MLE the bridge between probability theory and practical humanoid control learning.
