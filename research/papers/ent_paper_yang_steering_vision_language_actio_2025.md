---
$id: ent_paper_yang_steering_vision_language_actio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach'
  zh: TACO
  ko: 'Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach'
summary:
  en: 'Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach (TACO), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Artificial Intelligence, China Telecom, University of Science
    and Technology of China, Tsinghua University, The Hong Kong University of Science and Technology.'
  zh: TACO 是一种 2025 年提出的视觉-语言-动作大模型，由多家中国机构联合开发，用于机器人操作。其核心创新在于提出“反探索”测试时缩放方法，通过隐式推理在潜在空间中迭代，无需链式思维或专门训练数据，即可在测试时动态扩展计算量。
  ko: 'Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach (TACO), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Artificial Intelligence, China Telecom, University of Science
    and Technology of China, Tsinghua University, The Hong Kong University of Science and Technology.'
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
- robotic_manipulation
- taco
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.05171v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach (arXiv)'
  url: https://arxiv.org/abs/2502.05171
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: TACO source
  url: https://doi.org/10.48550/arXiv.2502.05171
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
TACO 模型通过循环块迭代实现测试时计算缩放，与主流通过生成更多 token 扩展计算的方式不同。该方法在潜在空间中进行隐式推理，无需链式思维所需的专门训练数据，且能处理难以用语言表达的推理类型。模型规模达 35 亿参数，训练于 8000 亿 token，在推理基准测试中性能显著提升，计算量等效于 50 亿参数模型。

## 核心内容
### 方法架构
- 模型采用循环块迭代架构，在潜在空间中隐式推理，测试时可展开至任意深度。
- 与链式思维方法不同，无需专门训练数据，支持小上下文窗口，能捕捉难以用语言表达的推理类型。

### 实验设置
- 模型规模：35 亿参数，训练数据量：8000 亿 token。
- 对比基线：主流推理模型（通过生成更多 token 扩展计算）。

### 关键结果
- 在推理基准测试中，性能提升显著，有时甚至达到戏剧性效果。
- 计算量等效于 50 亿参数模型，表明测试时缩放的有效性。

### 结论
TACO 通过反探索策略实现测试时计算缩放，为机器人操作中的视觉-语言-动作模型提供了新范式，无需复杂训练数据即可提升推理能力。

## Overview
We study a novel language model architecture that is capable of scaling test-time computation by implicitly reasoning in latent space. Our model works by iterating a recurrent block, thereby unrolling to arbitrary depth at test-time. This stands in contrast to mainstream reasoning models that scale up compute by producing more tokens. Unlike approaches based on chain-of-thought, our approach does not require any specialized training data, can work with small context windows, and can capture types of reasoning that are not easily represented in words. We scale a proof-of-concept model to 3.5 billion parameters and 800 billion tokens. We show that the resulting model can improve its performance on reasoning benchmarks, sometimes dramatically, up to a computation load equivalent to 50 billion parameters.

## 개요
우리는 잠재 공간에서 암시적으로 추론함으로써 테스트 시 계산을 확장할 수 있는 새로운 언어 모델 아키텍처를 연구합니다. 우리의 모델은 순환 블록을 반복하여 테스트 시 임의의 깊이로 전개됩니다. 이는 더 많은 토큰을 생성하여 계산을 확장하는 주류 추론 모델과 대조됩니다. 사고 사슬 기반 접근 방식과 달리, 우리의 접근 방식은 특수한 훈련 데이터가 필요하지 않으며, 작은 컨텍스트 윈도우로도 작동할 수 있고, 단어로 쉽게 표현되지 않는 유형의 추론을 포착할 수 있습니다. 우리는 개념 증명 모델을 35억 개의 매개변수와 8000억 개의 토큰으로 확장합니다. 그 결과 모델이 추론 벤치마크에서 성능을 향상시킬 수 있음을 보여주며, 때로는 500억 개의 매개변수에 해당하는 계산 부하까지 극적으로 향상됩니다.

## 핵심 내용
우리는 잠재 공간에서 암시적으로 추론함으로써 테스트 시 계산을 확장할 수 있는 새로운 언어 모델 아키텍처를 연구합니다. 우리의 모델은 순환 블록을 반복하여 테스트 시 임의의 깊이로 전개됩니다. 이는 더 많은 토큰을 생성하여 계산을 확장하는 주류 추론 모델과 대조됩니다. 사고 사슬 기반 접근 방식과 달리, 우리의 접근 방식은 특수한 훈련 데이터가 필요하지 않으며, 작은 컨텍스트 윈도우로도 작동할 수 있고, 단어로 쉽게 표현되지 않는 유형의 추론을 포착할 수 있습니다. 우리는 개념 증명 모델을 35억 개의 매개변수와 8000억 개의 토큰으로 확장합니다. 그 결과 모델이 추론 벤치마크에서 성능을 향상시킬 수 있음을 보여주며, 때로는 500억 개의 매개변수에 해당하는 계산 부하까지 극적으로 향상됩니다.

## 参考
- http://arxiv.org/abs/2502.05171v2
