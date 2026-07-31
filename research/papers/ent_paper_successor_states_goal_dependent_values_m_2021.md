---
$id: ent_paper_successor_states_goal_dependent_values_m_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Learning Successor States and Goal-Dependent Values: A Mathematical Viewpoint'
  zh: 'Learning Successor States and Goal-Dependent Values: A Mathematical Viewpoint'
  ko: 'Learning Successor States and Goal-Dependent Values: A Mathematical Viewpoint'
summary:
  en: 'In reinforcement learning, temporal difference-based algorithms can be sample-inefficient: for instance, with sparse
    rewards, no learning occurs until a reward is observed.'
  zh: 本文从数学视角系统推导了强化学习中后继状态与目标依赖值函数的时序差分算法，覆盖离散与连续环境。核心贡献包括：提出有限方差估计器解决连续环境中的稀疏奖励问题，揭示后继状态满足的Bellman-Newton算子及其与二阶梯度法的关联，并证明前向-后向低秩参数化方法在方差降低与采样效率上的优势。
  ko: 'In reinforcement learning, temporal difference-based algorithms can be sample-inefficient: for instance, with sparse
    rewards, no learning occurs until a reward is observed.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- successor
- states
- goal
- dependent
- values
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 128 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2101.07123 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2101.07123v1); zh content by DeepSeek from the abstract. Institutions unknown (not in source list).'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2101.07123 Learning Successor States and Goal-Dependent Values: A Mathematical Viewpoint'
  url: https://arxiv.org/abs/2101.07123
  accessed_at: '2026-07-31'
  date: '2021-01-18'
- id: src_002
  type: website
  title: 智元、众擎都在卷的人形机器人运控基座：41篇论文看懂BFM
  url: https://mp.weixin.qq.com/s/Ei32la_vo0UW9Y_QCAqB2g
  accessed_at: '2026-07-31'
---

## 概述

在强化学习中，基于时序差分的算法在稀疏奖励场景下存在样本效率低下的问题，因为直到获得奖励前不会发生学习。本文通过引入后继状态与目标依赖值函数来缓解这一缺陷，前者建模给定策略下从任意状态出发的未来状态占用期望，后者学习如何到达任意目标状态。作者在离散与连续环境中（包括使用函数逼近）正式推导了这两种对象的时序差分算法，特别针对连续环境中目标状态奖励无限稀疏的情况提供了有限方差估计器。研究进一步发现后继状态不仅满足Bellman方程，还满足后向Bellman算子与Bellman-Newton算子，后者类似于二阶梯度下降法，能在获取更多观测时提供值函数的真实更新。在表格情形下，混合使用标准与后向Bellman算子可改善渐近收敛的特征值，而Bellman-Newton算子的收敛速度与环境无关且优于TD。最后，前向-后向低秩参数化方法通过降低方差、提升可采样性、直接建模值函数以及提供状态的双重规范表示，在多个维度上展现出优势。

## 核心内容
### 核心问题与动机
- 传统TD算法在稀疏奖励环境中样本效率低下，因为直到首次获得奖励前不会发生学习。
- 通过学习更丰富的对象（如环境模型或后继状态）可缓解此问题：后继状态建模给定策略下从状态s出发的未来状态占用期望，目标依赖值函数则学习如何到达任意目标状态。

### 方法推导
- 在离散与连续环境中（包括使用函数逼近），正式推导了后继状态与目标依赖值函数的TD算法。
- 连续环境中，精确到达目标状态的奖励变得无限稀疏，但本文提供了有限方差估计器来解决这一问题。
- 后继状态不仅满足标准Bellman方程，还满足后向Bellman算子与Bellman-Newton算子，后者编码了环境中的路径组合性。

### Bellman-Newton算子
- BN算子类似于二阶梯度下降法，在获取更多观测时提供值函数的真实更新，并具有显式的表格界。
- 在表格情形下，使用无穷小学习率时，混合标准与后向Bellman算子可改善渐近收敛的特征值。
- BN算子的渐近收敛速度优于TD，且与环境无关，但其方法更复杂且对采样噪声的鲁棒性较差。

### 前向-后向低秩参数化
- FB方法对后继状态进行低秩参数化，具有以下优势：
  - 降低方差并提升可采样性
  - 直接建模值函数
  - 完全理解其不动点对应长程依赖关系
  - 近似BN方法
  - 作为副产品提供两种状态的规范表示

### 实验设置与结论
- 论文主要提供理论推导与数学分析，未涉及具体实验环境或数据集。
- 关键结论：FB方法在方差、采样效率、值函数建模与状态表示等多个维度上优于传统方法，且与BN方法存在理论联系。

## Overview
In reinforcement learning, temporal difference-based algorithms can be sample-inefficient: for instance, with sparse rewards, no learning occurs until a reward is observed. This can be remedied by learning richer objects, such as a model of the environment, or successor states. Successor states model the expected future state occupancy from any given state for a given policy and are related to goal-dependent value functions, which learn how to reach arbitrary states. We formally derive the temporal difference algorithm for successor state and goal-dependent value function learning, either for discrete or for continuous environments with function approximation. Especially, we provide finite-variance estimators even in continuous environments, where the reward for exactly reaching a goal state becomes infinitely sparse. Successor states satisfy more than just the Bellman equation: a backward Bellman operator and a Bellman-Newton (BN) operator encode path compositionality in the environment. The BN operator is akin to second-order gradient descent methods and provides the true update of the value function when acquiring more observations, with explicit tabular bounds. In the tabular case and with infinitesimal learning rates, mixing the usual and backward Bellman operators provably improves eigenvalues for asymptotic convergence, and the asymptotic convergence of the BN operator is provably better than TD, with a rate independent from the environment. However, the BN method is more complex and less robust to sampling noise. Finally, a forward-backward (FB) finite-rank parameterization of successor states enjoys reduced variance and improved samplability, provides a direct model of the value function, has fully understood fixed points corresponding to long-range dependencies, approximates the BN method, and provides two canonical representations of states as a byproduct.

## 参考
- https://arxiv.org/abs/2101.07123
- https://mp.weixin.qq.com/s/Ei32la_vo0UW9Y_QCAqB2g

## 개요

강화 학습에서 시간차 알고리즘 기반 방법은 희소 보상 환경에서 샘플 효율성이 낮은 문제가 있다. 보상을 얻기 전까지는 학습이 발생하지 않기 때문이다. 본 논문은 후속 상태와 목표 의존 가치 함수를 도입하여 이러한 결함을 완화한다. 전자는 주어진 정책 하에서 임의의 상태에서 출발했을 때의 미래 상태 점유 기대값을 모델링하고, 후자는 임의의 목표 상태에 도달하는 방법을 학습한다. 저자는 이산 및 연속 환경(함수 근사 포함)에서 이 두 대상의 시간차 알고리즘을 공식적으로 유도했으며, 특히 연속 환경에서 목표 상태 보상이 무한히 희소한 경우에 대해 유한 분산 추정기를 제공한다. 연구는 또한 후속 상태가 표준 Bellman 방정식뿐만 아니라 후방 Bellman 연산자와 Bellman-Newton 연산자도 만족한다는 것을 발견했으며, 후자는 2차 경사 하강법과 유사하여 더 많은 관측을 얻을 때 가치 함수의 실제 업데이트를 제공한다. 테이블 형태의 경우, 표준 및 후방 Bellman 연산자를 혼합 사용하면 점근 수렴의 고유값이 개선될 수 있고, Bellman-Newton 연산자의 수렴 속도는 환경과 무관하며 TD보다 우수하다. 마지막으로, 전방-후방 저랭크 파라미터화 방법은 분산 감소, 샘플링 가능성 향상, 가치 함수 직접 모델링, 상태의 이중 정규 표현 제공 등 여러 측면에서 장점을 보여준다.

## 핵심 내용
### 핵심 문제와 동기
- 기존 TD 알고리즘은 희소 보상 환경에서 샘플 효율성이 낮다. 첫 보상을 얻기 전까지는 학습이 발생하지 않기 때문이다.
- 더 풍부한 대상(예: 환경 모델 또는 후속 상태)을 학습하면 이 문제를 완화할 수 있다. 후속 상태는 주어진 정책 하에서 상태 s에서 출발했을 때의 미래 상태 점유 기대값을 모델링하고, 목표 의존 가치 함수는 임의의 목표 상태에 도달하는 방법을 학습한다.

### 방법 유도
- 이산 및 연속 환경(함수 근사 포함)에서 후속 상태와 목표 의존 가치 함수의 TD 알고리즘을 공식적으로 유도했다.
- 연속 환경에서는 목표 상태에 정확히 도달하는 보상이 무한히 희소해지지만, 본 논문은 이 문제를 해결하기 위해 유한 분산 추정기를 제공한다.
- 후속 상태는 표준 Bellman 방정식뿐만 아니라 후방 Bellman 연산자와 Bellman-Newton 연산자도 만족하며, 후자는 환경에서 경로의 조합성을 인코딩한다.

### Bellman-Newton 연산자
- BN 연산자는 2차 경사 하강법과 유사하며, 더 많은 관측을 얻을 때 가치 함수의 실제 업데이트를 제공하고 명시적인 테이블 형태의 경계를 가진다.
- 테이블 형태에서 무한소 학습률을 사용할 때, 표준 및 후방 Bellman 연산자를 혼합 사용하면 점근 수렴의 고유값이 개선될 수 있다.
- BN 연산자의 점근 수렴 속도는 TD보다 우수하고 환경과 무관하지만, 방법이 더 복잡하고 샘플링 노이즈에 대한 강건성이 떨어진다.

### 전방-후방 저랭크 파라미터화
- FB 방법은 후속 상태를 저랭크로 파라미터화하며 다음과 같은 장점이 있다:
  - 분산 감소 및 샘플링 가능성 향상
  - 가치 함수 직접 모델링
  - 고정점이 장기 의존 관계에 해당한다는 완전한 이해
  - BN 방법의 근사
  - 부산물로 두 상태의 정규 표현 제공

### 실험 설정 및 결론
- 본 논문은 주로 이론적 유도와 수학적 분석을 제공하며, 구체적인 실험 환경이나 데이터셋은 포함하지 않는다.
- 핵심 결론: FB 방법은 분산, 샘플링 효율성, 가치 함수 모델링 및 상태 표현 등 여러 측면에서 기존 방법보다 우수하며, BN 방법과 이론적 연관성이 있다.
