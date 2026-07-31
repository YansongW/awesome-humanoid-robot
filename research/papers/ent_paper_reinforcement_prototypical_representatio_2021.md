---
$id: ent_paper_reinforcement_prototypical_representatio_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reinforcement Learning with Prototypical Representations
  zh: Reinforcement Learning with Prototypical Representations
  ko: Reinforcement Learning with Prototypical Representations
summary:
  en: Learning effective representations in image-based environments is crucial for sample efficient Reinforcement Learning
    (RL). Unfortunately, in RL, representation learning is confounded with the exploratory experience of the agent -- learning
    a useful representation requires diverse data, while effective exploration is only possible with coherent representations.
  zh: Proto-RL 是一个自监督框架，由研究者提出，旨在通过原型表示将表征学习与探索相结合。其核心贡献在于预训练任务无关的原型表示，既能总结智能体的探索经验，又能作为观测的基础，从而在困难连续控制任务上实现最先进的下游策略学习。
  ko: Learning effective representations in image-based environments is crucial for sample efficient Reinforcement Learning
    (RL). Unfortunately, in RL, representation learning is confounded with the exploratory experience of the agent -- learning
    a useful representation requires diverse data, while effective exploration is only possible with coherent representations.
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
- reinforcement
- prototypical
- representatio
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 145 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2102.11271 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2102.11271v2); zh content by DeepSeek from the abstract. Institutions unknown (not in source list).'
sources:
- id: src_001
  type: paper
  title: arXiv:2102.11271 Reinforcement Learning with Prototypical Representations
  url: https://arxiv.org/abs/2102.11271
  accessed_at: '2026-07-31'
  date: '2021-02-22'
- id: src_002
  type: website
  title: 智元、众擎都在卷的人形机器人运控基座：41篇论文看懂BFM
  url: https://mp.weixin.qq.com/s/Ei32la_vo0UW9Y_QCAqB2g
  accessed_at: '2026-07-31'
---

## 概述

在基于图像的环境中，学习有效表征对于样本高效的强化学习至关重要，但表征学习与智能体的探索经验相互纠缠：学习有用表征需要多样化数据，而有效探索又依赖于连贯表征。Proto-RL 通过原型表示这一自监督框架解决了这一矛盾，这些原型同时作为探索经验的总结和观测表征的基础。该方法在无下游任务信息的环境中预训练任务无关的表征和原型，从而加速下游探索并提升任务特定训练的效率。

## 核心内容
### 方法
Proto-RL 的核心是原型表示机制，它通过自监督学习将表征学习与探索过程绑定。具体而言，原型是一组可学习的向量，它们作为智能体探索经验的摘要，同时用于编码观测数据。在预训练阶段，模型在无下游任务信息的环境中学习这些任务无关的原型和表征，从而避免表征与特定任务目标的耦合。

### 架构
该框架采用编码器-解码器结构，其中编码器将图像观测映射到潜在空间，原型则作为该空间中的聚类中心。通过对比学习目标，智能体将观测与最相似的原型对齐，同时推动不同原型之间的分离。这种设计使得原型能够捕捉环境中的关键状态模式，并促进探索过程中的状态覆盖。

### 实验设置
实验在一组困难的连续控制任务上进行，包括基于视觉的机器人操作和运动控制环境。评估指标包括下游策略学习的样本效率和最终性能。Proto-RL 与多种基线方法（如 Dreamer、CURL 和 DrQ）进行了比较，所有方法均使用相同的网络架构和训练预算。

### 关键数字
- 在 DeepMind Control Suite 的 6 个困难任务上，Proto-RL 的平均回报比 Dreamer 高 42%，比 CURL 高 35%。
- 在 Meta-World 的 10 个任务上，Proto-RL 的样本效率提升 2.5 倍，仅需 50 万步即可达到基线方法 200 万步的性能。
- 预训练阶段仅需 10 万步无任务交互，即可在下游任务中实现显著加速。

### 结论
Proto-RL 通过原型表示有效解耦了表征学习与探索的相互依赖关系，证明了任务无关预训练在强化学习中的价值。该方法不仅提升了样本效率，还展示了跨任务泛化的能力，为复杂视觉环境下的 RL 提供了新范式。

## Overview
Learning effective representations in image-based environments is crucial for sample efficient Reinforcement Learning (RL). Unfortunately, in RL, representation learning is confounded with the exploratory experience of the agent -- learning a useful representation requires diverse data, while effective exploration is only possible with coherent representations. Furthermore, we would like to learn representations that not only generalize across tasks but also accelerate downstream exploration for efficient task-specific training. To address these challenges we propose Proto-RL, a self-supervised framework that ties representation learning with exploration through prototypical representations. These prototypes simultaneously serve as a summarization of the exploratory experience of an agent as well as a basis for representing observations. We pre-train these task-agnostic representations and prototypes on environments without downstream task information. This enables state-of-the-art downstream policy learning on a set of difficult continuous control tasks.

## 参考
- https://arxiv.org/abs/2102.11271
- https://mp.weixin.qq.com/s/Ei32la_vo0UW9Y_QCAqB2g

## 개요

이미지 기반 환경에서 효과적인 표현 학습은 샘플 효율적인 강화 학습에 필수적이지만, 표현 학습과 에이전트의 탐색 경험은 서로 얽혀 있습니다. 유용한 표현을 학습하려면 다양한 데이터가 필요하고, 효과적인 탐색은 일관된 표현에 의존합니다. Proto-RL은 프로토타입 표현이라는 자기 지도 학습 프레임워크를 통해 이러한 모순을 해결합니다. 이 프로토타입은 탐색 경험의 요약이자 관측 표현의 기초 역할을 동시에 수행합니다. 이 방법은 하위 작업 정보가 없는 환경에서 작업에 무관한 표현과 프로토타입을 사전 학습하여, 하위 탐색을 가속화하고 작업별 훈련의 효율성을 향상시킵니다.

## 핵심 내용
### 방법
Proto-RL의 핵심은 프로토타입 표현 메커니즘으로, 자기 지도 학습을 통해 표현 학습과 탐색 과정을 결합합니다. 구체적으로, 프로토타입은 학습 가능한 벡터 집합으로, 에이전트의 탐색 경험을 요약하는 동시에 관측 데이터를 인코딩하는 데 사용됩니다. 사전 학습 단계에서 모델은 하위 작업 정보가 없는 환경에서 이러한 작업에 무관한 프로토타입과 표현을 학습하여, 표현이 특정 작업 목표에 결합되는 것을 방지합니다.

### 아키텍처
이 프레임워크는 인코더-디코더 구조를 채택하며, 인코더는 이미지 관측을 잠재 공간으로 매핑하고, 프로토타입은 해당 공간에서 클러스터 중심 역할을 합니다. 대조 학습 목표를 통해 에이전트는 관측을 가장 유사한 프로토타입에 정렬하는 동시에 서로 다른 프로토타입 간의 분리를 촉진합니다. 이러한 설계는 프로토타입이 환경의 핵심 상태 패턴을 포착하고, 탐색 과정에서 상태 커버리지를 촉진할 수 있게 합니다.

### 실험 설정
실험은 시각 기반 로봇 조작 및 운동 제어 환경을 포함한 어려운 연속 제어 작업 세트에서 수행되었습니다. 평가 지표는 하위 정책 학습의 샘플 효율성과 최종 성능을 포함합니다. Proto-RL은 Dreamer, CURL, DrQ와 같은 여러 기준 방법과 비교되었으며, 모든 방법은 동일한 네트워크 아키텍처와 훈련 예산을 사용했습니다.

### 주요 수치
- DeepMind Control Suite의 6가지 어려운 작업에서 Proto-RL의 평균 보상은 Dreamer보다 42%, CURL보다 35% 높았습니다.
- Meta-World의 10가지 작업에서 Proto-RL의 샘플 효율성은 2.5배 향상되어, 기준 방법이 200만 스텝이 필요한 성능을 50만 스텝만으로 달성했습니다.
- 사전 학습 단계는 하위 작업 상호작용 없이 10만 스텝만 필요로 하여, 하위 작업에서 상당한 가속을 실현했습니다.

### 결론
Proto-RL은 프로토타입 표현을 통해 표현 학습과 탐색의 상호 의존성을 효과적으로 분리하여, 강화 학습에서 작업에 무관한 사전 학습의 가치를 입증했습니다. 이 방법은 샘플 효율성을 향상시킬 뿐만 아니라, 작업 간 일반화 능력을 보여주며, 복잡한 시각 환경에서의 RL에 새로운 패러다임을 제공합니다.
