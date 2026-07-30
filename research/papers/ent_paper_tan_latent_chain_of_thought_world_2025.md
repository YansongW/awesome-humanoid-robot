---
$id: ent_paper_tan_latent_chain_of_thought_world_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Latent Chain-of-Thought World Modeling for End-to-End Driving
  zh: LCDrive
  ko: Latent Chain-of-Thought World Modeling for End-to-End Driving
summary:
  en: Latent Chain-of-Thought World Modeling for End-to-End Driving (LCDrive), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by University of Tübingen.
  zh: LCDrive 是图宾根大学于 2025 年提出的端到端驾驶大语言-视觉-动作模型。其核心贡献在于用潜在空间中的动作对齐推理替代自然语言链式思维，通过动作提议令牌与世界模型令牌的交替生成实现推理与决策的统一。该模型在闭环强化学习后训练下，相比文本推理基线实现了更快的推理速度与更优的轨迹质量。
  ko: Latent Chain-of-Thought World Modeling for End-to-End Driving (LCDrive), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by University of Tübingen.
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
- lcdrive
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.10226v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Latent Chain-of-Thought World Modeling for End-to-End Driving (arXiv)
  url: https://arxiv.org/abs/2512.10226
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: LCDrive source
  url: https://doi.org/10.48550/arXiv.2512.10226
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有自动驾驶视觉-语言-动作模型多采用自然语言进行推理时链式思维，但文本可能并非最高效的推理表征。LCDrive 创新性地将链式思维表达为潜在语言，该语言直接捕捉驾驶动作的可能后果。模型通过交替生成两类令牌实现推理：一是与输出动作共享词表的动作提议令牌，二是基于学习到的潜在世界模型表达动作未来结果的世界模型令牌。训练采用两阶段策略：先用真实场景未来轨迹进行冷启动监督，再通过闭环强化学习增强推理能力。

## 核心内容
### 方法架构
- **潜在链式思维机制**：模型在潜在空间中交替生成两类令牌——动作提议令牌（与输出动作共享词表）和世界模型令牌（基于学习到的潜在世界模型表达动作未来结果），实现推理与决策的统一表征。
- **冷启动训练**：利用场景的真实未来轨迹（ground-truth future rollouts）监督动作提议令牌和世界模型令牌的生成，为模型提供初始推理能力。
- **闭环强化学习后训练**：在冷启动基础上，通过交互式强化学习（interactive reinforcement learning）进一步强化模型的推理能力，使其在闭环环境中表现更优。

### 实验设置与关键结果
- **基准测试**：在大规模端到端驾驶基准（large-scale end-to-end driving benchmark）上进行评估。
- **性能对比**：相比非推理基线（non-reasoning baselines）和文本推理基线（text-reasoning baselines），LCDrive 实现：
  - 更快的推理速度（faster inference）
  - 更好的轨迹质量（better trajectory quality）
  - 从交互式强化学习中获得的更大性能提升（larger improvements from interactive reinforcement learning）

### 结论
LCDrive 通过将链式思维推理从自然语言空间迁移至动作对齐的潜在空间，有效解决了文本推理效率低下的问题。其双令牌交替生成机制与两阶段训练策略，为端到端驾驶中的推理时决策提供了新的范式。

## Overview
Recent Vision-Language-Action (VLA) models for autonomous driving explore inference-time reasoning as a way to improve driving performance and safety in challenging scenarios. Most prior work uses natural language to express chain-of-thought (CoT) reasoning before producing driving actions. However, text may not be the most efficient representation for reasoning. In this work, we present Latent-CoT-Drive (LCDrive): a model that expresses CoT in a latent language that captures possible outcomes of the driving actions being considered. Our approach unifies CoT reasoning and decision making by representing both in an action-aligned latent space. Instead of natural language, the model reasons by interleaving (1) action-proposal tokens, which use the same vocabulary as the model's output actions; and (2) world model tokens, which are grounded in a learned latent world model and express future outcomes of these actions. We cold start latent CoT by supervising the model's action proposals and world model tokens based on ground-truth future rollouts of the scene. We then post-train with closed-loop reinforcement learning to strengthen reasoning capabilities. On a large-scale end-to-end driving benchmark, LCDrive achieves faster inference, better trajectory quality, and larger improvements from interactive reinforcement learning compared to both non-reasoning and text-reasoning baselines.

## 개요
최근 자율주행을 위한 Vision-Language-Action(VLA) 모델은 까다로운 시나리오에서 주행 성능과 안전성을 향상시키기 위해 추론 시간 추론을 탐구하고 있습니다. 대부분의 기존 연구는 주행 동작을 생성하기 전에 자연어를 사용하여 사고 사슬(CoT) 추론을 표현합니다. 그러나 텍스트는 추론에 가장 효율적인 표현이 아닐 수 있습니다. 본 연구에서는 고려 중인 주행 동작의 가능한 결과를 포착하는 잠재 언어로 CoT를 표현하는 Latent-CoT-Drive(LCDrive)를 제시합니다. 우리의 접근 방식은 CoT 추론과 의사 결정을 모두 동작 정렬 잠재 공간에서 표현하여 통합합니다. 자연어 대신 모델은 (1) 모델의 출력 동작과 동일한 어휘를 사용하는 동작 제안 토큰과 (2) 학습된 잠재 세계 모델에 기반하여 이러한 동작의 미래 결과를 표현하는 세계 모델 토큰을 교차 배치하여 추론합니다. 우리는 장면의 실제 미래 롤아웃을 기반으로 모델의 동작 제안 및 세계 모델 토큰을 감독하여 잠재 CoT를 콜드 스타트합니다. 그런 다음 폐쇄 루프 강화 학습으로 사후 학습하여 추론 능력을 강화합니다. 대규모 엔드투엔드 주행 벤치마크에서 LCDrive는 비추론 및 텍스트 추론 기준선에 비해 더 빠른 추론, 더 나은 궤적 품질, 상호작용 강화 학습으로부터의 더 큰 개선을 달성합니다.

## 핵심 내용
최근 자율주행을 위한 Vision-Language-Action(VLA) 모델은 까다로운 시나리오에서 주행 성능과 안전성을 향상시키기 위해 추론 시간 추론을 탐구하고 있습니다. 대부분의 기존 연구는 주행 동작을 생성하기 전에 자연어를 사용하여 사고 사슬(CoT) 추론을 표현합니다. 그러나 텍스트는 추론에 가장 효율적인 표현이 아닐 수 있습니다. 본 연구에서는 고려 중인 주행 동작의 가능한 결과를 포착하는 잠재 언어로 CoT를 표현하는 Latent-CoT-Drive(LCDrive)를 제시합니다. 우리의 접근 방식은 CoT 추론과 의사 결정을 모두 동작 정렬 잠재 공간에서 표현하여 통합합니다. 자연어 대신 모델은 (1) 모델의 출력 동작과 동일한 어휘를 사용하는 동작 제안 토큰과 (2) 학습된 잠재 세계 모델에 기반하여 이러한 동작의 미래 결과를 표현하는 세계 모델 토큰을 교차 배치하여 추론합니다. 우리는 장면의 실제 미래 롤아웃을 기반으로 모델의 동작 제안 및 세계 모델 토큰을 감독하여 잠재 CoT를 콜드 스타트합니다. 그런 다음 폐쇄 루프 강화 학습으로 사후 학습하여 추론 능력을 강화합니다. 대규모 엔드투엔드 주행 벤치마크에서 LCDrive는 비추론 및 텍스트 추론 기준선에 비해 더 빠른 추론, 더 나은 궤적 품질, 상호작용 강화 학습으로부터의 더 큰 개선을 달성합니다.

## 参考
- http://arxiv.org/abs/2512.10226v2
