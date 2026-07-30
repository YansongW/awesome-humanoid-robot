---
$id: ent_paper_sridhar_regent_a_retrieval_augmented_g_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'REGENT: A Retrieval-Augmented Generalist Agent That Can Act In-Context in New Environments'
  zh: REGENT
  ko: 'REGENT: A Retrieval-Augmented Generalist Agent That Can Act In-Context in New Environments'
summary:
  en: 'REGENT: A Retrieval-Augmented Generalist Agent That Can Act In-Context in New Environments (REGENT), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by University of Pennsylvania, and published at ICLR25.'
  zh: REGENT 是宾夕法尼亚大学于 2024 年提出、发表在 ICLR25 上的大型视觉-语言-动作模型，用于机器人操控。其核心贡献在于通过检索增强和上下文学习，使模型无需微调即可快速适应新环境，且参数量减少 3 倍、预训练数据量减少一个数量级，性能显著超越当前最先进的通用智能体。
  ko: 'REGENT: A Retrieval-Augmented Generalist Agent That Can Act In-Context in New Environments (REGENT), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by University of Pennsylvania, and published at ICLR25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- regent
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.04759v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: REGENT source
  url: https://openreview.net/forum?id=NxyfSW6mLK
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
REGENT 提出了一种半参数化智能体架构，核心思想是利用检索机制为快速适应提供强大先验。该模型基于 Transformer 策略，在查询和检索到的邻居序列上进行训练，从而在未见过的机器人和游戏环境中通过检索增强和上下文学习实现泛化。实验表明，即使简单的基于检索的 1-最近邻智能体也能成为当前最先进通用智能体的强大基线，而 REGENT 在此基础上进一步提升了性能。

## 核心内容
### 方法
- **核心思想**：利用检索机制作为快速适应的先验，使模型无需微调即可通过上下文学习适应新环境。
- **架构**：构建半参数化智能体 REGENT，基于 Transformer 策略，在查询和检索到的邻居序列上进行训练。
- **关键发现**：即使简单的基于检索的 1-最近邻智能体也能成为当前最先进通用智能体的强大基线。

### 实验设置
- **任务**：在未见过的机器人操控和游戏环境中进行测试。
- **对比基线**：与当前最先进的通用智能体进行比较。
- **评估指标**：任务成功率、泛化能力、参数量和预训练数据量。

### 关键结果
- **性能**：REGENT 显著优于当前最先进的通用智能体。
- **效率**：参数量减少 3 倍，预训练数据量减少一个数量级。
- **泛化能力**：通过检索增强和上下文学习，成功泛化到未见过的环境。

### 结论
REGENT 证明了检索增强和上下文学习是构建通用智能体的有效途径，能够在显著降低模型规模和训练数据需求的同时，实现甚至超越现有方法的性能。

## Overview
Building generalist agents that can rapidly adapt to new environments is a key challenge for deploying AI in the digital and real worlds. Is scaling current agent architectures the most effective way to build generalist agents? We propose a novel approach to pre-train relatively small policies on relatively small datasets and adapt them to unseen environments via in-context learning, without any finetuning. Our key idea is that retrieval offers a powerful bias for fast adaptation. Indeed, we demonstrate that even a simple retrieval-based 1-nearest neighbor agent offers a surprisingly strong baseline for today's state-of-the-art generalist agents. From this starting point, we construct a semi-parametric agent, REGENT, that trains a transformer-based policy on sequences of queries and retrieved neighbors. REGENT can generalize to unseen robotics and game-playing environments via retrieval augmentation and in-context learning, achieving this with up to 3x fewer parameters and up to an order-of-magnitude fewer pre-training datapoints, significantly outperforming today's state-of-the-art generalist agents. Website: https://kaustubhsridhar.github.io/regent-research

## 개요
디지털 및 실제 세계에 AI를 배포하기 위해 새로운 환경에 빠르게 적응할 수 있는 범용 에이전트를 구축하는 것은 핵심 과제입니다. 현재의 에이전트 아키텍처를 확장하는 것이 범용 에이전트를 구축하는 가장 효과적인 방법일까요? 우리는 상대적으로 작은 데이터셋에서 상대적으로 작은 정책을 사전 학습하고, 미세 조정 없이 문맥 내 학습을 통해 보지 못한 환경에 적응하는 새로운 접근 방식을 제안합니다. 핵심 아이디어는 검색이 빠른 적응을 위한 강력한 편향을 제공한다는 것입니다. 실제로, 단순한 검색 기반 1-최근접 이웃 에이전트조차도 오늘날 최첨단 범용 에이전트에 대해 놀라울 정도로 강력한 기준선을 제공한다는 것을 입증합니다. 이 출발점에서 우리는 쿼리와 검색된 이웃의 시퀀스에 대해 트랜스포머 기반 정책을 훈련하는 반파라메트릭 에이전트 REGENT를 구축합니다. REGENT는 검색 증강 및 문맥 내 학습을 통해 보지 못한 로봇 공학 및 게임 플레이 환경에 일반화할 수 있으며, 최대 3배 적은 파라미터와 최대 한 자릿수 적은 사전 학습 데이터 포인트로 이를 달성하여 오늘날 최첨단 범용 에이전트를 크게 능가합니다. 웹사이트: https://kaustubhsridhar.github.io/regent-research

## 핵심 내용
디지털 및 실제 세계에 AI를 배포하기 위해 새로운 환경에 빠르게 적응할 수 있는 범용 에이전트를 구축하는 것은 핵심 과제입니다. 현재의 에이전트 아키텍처를 확장하는 것이 범용 에이전트를 구축하는 가장 효과적인 방법일까요? 우리는 상대적으로 작은 데이터셋에서 상대적으로 작은 정책을 사전 학습하고, 미세 조정 없이 문맥 내 학습을 통해 보지 못한 환경에 적응하는 새로운 접근 방식을 제안합니다. 핵심 아이디어는 검색이 빠른 적응을 위한 강력한 편향을 제공한다는 것입니다. 실제로, 단순한 검색 기반 1-최근접 이웃 에이전트조차도 오늘날 최첨단 범용 에이전트에 대해 놀라울 정도로 강력한 기준선을 제공한다는 것을 입증합니다. 이 출발점에서 우리는 쿼리와 검색된 이웃의 시퀀스에 대해 트랜스포머 기반 정책을 훈련하는 반파라메트릭 에이전트 REGENT를 구축합니다. REGENT는 검색 증강 및 문맥 내 학습을 통해 보지 못한 로봇 공학 및 게임 플레이 환경에 일반화할 수 있으며, 최대 3배 적은 파라미터와 최대 한 자릿수 적은 사전 학습 데이터 포인트로 이를 달성하여 오늘날 최첨단 범용 에이전트를 크게 능가합니다. 웹사이트: https://kaustubhsridhar.github.io/regent-research

## 参考
- http://arxiv.org/abs/2412.04759v2
