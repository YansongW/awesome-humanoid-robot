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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.04759v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (667 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2412.04759v2

## 개요
REGENT는 반파라미터적 에이전트 아키텍처를 제안하며, 핵심 아이디어는 검색 메커니즘을 활용하여 빠른 적응을 위한 강력한 사전 지식을 제공하는 것입니다. 이 모델은 Transformer 정책을 기반으로 하며, 쿼리와 검색된 이웃 시퀀스에서 훈련되어, 보지 못한 로봇 및 게임 환경에서 검색 증강과 맥락 학습을 통해 일반화를 달성합니다. 실험은 단순한 검색 기반 1-최근접 이웃 에이전트조차도 현재 최첨단 범용 에이전트의 강력한 기준선이 될 수 있음을 보여주며, REGENT는 이를 바탕으로 성능을 더욱 향상시킵니다.

## 핵심 내용
### 방법
- **핵심 아이디어**: 검색 메커니즘을 빠른 적응을 위한 사전 지식으로 활용하여, 모델이 미세 조정 없이 맥락 학습을 통해 새로운 환경에 적응할 수 있게 합니다.
- **아키텍처**: 반파라미터적 에이전트 REGENT를 구축하며, Transformer 정책을 기반으로 쿼리와 검색된 이웃 시퀀스에서 훈련합니다.
- **주요 발견**: 단순한 검색 기반 1-최근접 이웃 에이전트조차도 현재 최첨단 범용 에이전트의 강력한 기준선이 될 수 있습니다.

### 실험 설정
- **작업**: 보지 못한 로봇 조작 및 게임 환경에서 테스트합니다.
- **비교 기준선**: 현재 최첨단 범용 에이전트와 비교합니다.
- **평가 지표**: 작업 성공률, 일반화 능력, 파라미터 수 및 사전 훈련 데이터 양.

### 주요 결과
- **성능**: REGENT는 현재 최첨단 범용 에이전트보다 현저히 우수합니다.
- **효율성**: 파라미터 수가 3배 감소하고, 사전 훈련 데이터 양이 한 자릿수 줄어듭니다.
- **일반화 능력**: 검색 증강과 맥락 학습을 통해 보지 못한 환경에 성공적으로 일반화합니다.

### 결론
REGENT는 검색 증강과 맥락 학습이 범용 에이전트를 구축하는 효과적인 경로임을 입증하며, 모델 규모와 훈련 데이터 요구 사항을 크게 줄이면서도 기존 방법의 성능을 달성하거나 초과할 수 있습니다.
