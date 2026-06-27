---
$id: ent_foundation_probability_theory
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: foundation
names:
  en: Probability Theory
  zh: 概率论
  ko: 확률론
summary:
  en: The mathematical foundation for reasoning about uncertainty, random variables, distributions, and expectations, underlying all probabilistic models in machine learning and robotics.
  zh: 关于不确定性、随机变量、分布和期望的数学基础，是机器人和机器学习中所有概率模型的根基。
  ko: 불확실성, 확률 변수, 분포, 기댓값에 관한 수학적 기초로, 로보틱스와 머신러닝의 모든 확률적 모델의 근간이 된다.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
tags:
- probability_theory
- random_variables
- distributions
- expectation
- vla
theoretical_depth:
- foundation
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Foundational for statistical machine learning.
sources:
- id: src_wasserman_2004
  type: paper
  title: 'Wasserman, All of Statistics'
  url: https://www.stat.cmu.edu/~larry/all-of-statistics/
  date: '2004'
  accessed_at: '2026-06-26'
---

## 抽象

> **生活实例**：天气预报说“明天 70% 下雨”。概率论就是研究如何用数字表达这种不确定性的学问——它不能告诉你明天一定下不下雨，但能帮你做出带伞还是不带伞的理性决策。
>
> **自然语言逻辑**：随机变量描述可能结果；概率分布给出各结果的可能性；期望和方差刻画长期行为和波动；贝叶斯定理让我们根据新证据更新信念；这些工具构成了机器学习损失函数和推断算法的数学基础。

## Overview

Probability theory provides the language for describing uncertainty. It defines probability spaces, random variables, joint and conditional distributions, and expectations. In machine learning, it justifies objectives such as maximum likelihood and Bayesian inference.

## Relevance to Humanoid Robotics

Humanoid robots operate in stochastic environments with noisy sensors, uncertain dynamics, and variable human intent. Probability theory underlies state estimation, reinforcement learning, and the generative action models in VLAs, enabling robots to reason and act under uncertainty.
