---
$id: ent_paper_fabrivla_a_lightweight_vision_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FabriVLA: A Lightweight Vision-Language-Action Model for Precise Multi-Task Manipulation'
  zh: 'FabriVLA: A Lightweight Vision-Language-Action Model for Precise Multi-Task Manipulation'
  ko: 'FabriVLA: A Lightweight Vision-Language-Action Model for Precise Multi-Task Manipulation'
summary:
  en: 'arXiv:2607.08575v2 Announce Type: replace Abstract: We present FabriVLA, a lightweight Vision-Language-Action model
    for Precise Multi-Task Manipulation. FabriVLA combines an InternVL3.5 vision-language backbone with a flow-matching action
    head featuring gated self-attention across action tokens and shallow VLM layer fusion for enriched spatial context. The
    model is trained via single stage joint optimization from a pretrained VLM and randomly initialized action head. On the
    Meta-World MT50 benchmark spanning 50 diverse manipulation tasks, FabriVLA achieves a tier-average success rate of 90.0%,
    demonstrating that a compact VLA built on a 1B scale VLM can achieve strong performance without relying on multi billion
    parameter VLA backbones.'
  zh: FabriVLA 是一个轻量级视觉-语言-动作模型，专为精确的多任务操作设计。它由 InternVL3.5 视觉-语言骨干网络与流匹配动作头组成，后者包含门控自注意力机制和浅层 VLM 层融合。在 Meta-World MT50 基准上，该模型以
    1B 参数规模实现了 90.0% 的平均成功率，证明了紧凑型 VLA 无需依赖数十亿参数即可达到强性能。
  ko: 'arXiv:2607.08575v2 Announce Type: replace Abstract: We present FabriVLA, a lightweight Vision-Language-Action model
    for Precise Multi-Task Manipulation. FabriVLA combines an InternVL3.5 vision-language backbone with a flow-matching action
    head featuring gated self-attention across action tokens and shallow VLM layer fusion for enriched spatial context. The
    model is trained via single stage joint optimization from a pretrained VLM and randomly initialized action head. On the
    Meta-World MT50 benchmark spanning 50 diverse manipulation tasks, FabriVLA achieves a tier-average success rate of 90.0%,
    demonstrating that a compact VLA built on a 1B scale VLM can achieve strong performance without relying on multi billion
    parameter VLA backbones.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- fabrivla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.08575v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'FabriVLA: A Lightweight Vision-Language-Action Model for Precise Multi-Task Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.08575
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
FabriVLA 的核心创新在于其轻量化架构：采用 InternVL3.5 作为视觉-语言骨干，并搭配一个流匹配动作头。该动作头通过门控自注意力机制处理动作令牌间的交互，同时融合浅层 VLM 层以增强空间上下文信息。模型通过单阶段联合优化进行训练，从预训练的 VLM 和随机初始化的动作头开始。在包含 50 种不同任务的 Meta-World MT50 基准上，FabriVLA 取得了 90.0% 的层级平均成功率，表明基于 1B 规模 VLM 的紧凑模型能够有效替代庞大的多参数骨干网络。

## 核心内容
### 方法
- **架构**：FabriVLA 由 InternVL3.5 视觉-语言骨干网络和流匹配动作头组成。动作头包含门控自注意力机制，用于处理动作令牌间的依赖关系，并通过浅层 VLM 层融合来丰富空间上下文。
- **训练**：采用单阶段联合优化策略，从预训练的 VLM 和随机初始化的动作头开始，无需分阶段训练。

### 实验设置
- **基准**：Meta-World MT50，包含 50 种不同的操作任务。
- **评估指标**：层级平均成功率（tier-average success rate）。

### 关键结果
- **性能**：在 Meta-World MT50 上达到 90.0% 的层级平均成功率。
- **规模优势**：模型基于 1B 参数规模的 VLM，无需依赖数十亿参数的 VLA 骨干网络即可实现强性能。

### 结论
FabriVLA 证明了紧凑型 VLA 模型在精确多任务操作中的有效性，通过轻量化设计在保持高性能的同时显著降低了参数规模。

## Overview
We present FabriVLA, a lightweight Vision-Language-Action model for Precise Multi-Task Manipulation. FabriVLA combines an InternVL3.5 vision-language backbone with a flow-matching action head featuring gated self-attention across action tokens and shallow VLM layer fusion for enriched spatial context. The model is trained via single stage joint optimization from a pretrained VLM and randomly initialized action head. On the Meta-World MT50 benchmark spanning 50 diverse manipulation tasks, FabriVLA achieves a tier-average success rate of 90.0%, demonstrating that a compact VLA built on a 1B scale VLM can achieve strong performance without relying on multi billion parameter VLA backbones.

## 개요
본 논문에서는 정밀한 다중 작업 조작을 위한 경량 비전-언어-행동 모델인 FabriVLA를 제시합니다. FabriVLA는 InternVL3.5 비전-언어 백본과 플로우 매칭 행동 헤드를 결합하며, 이 헤드는 행동 토큰 간 게이트 자기 주의 메커니즘과 향상된 공간적 맥락을 위한 얕은 VLM 계층 융합을 특징으로 합니다. 모델은 사전 훈련된 VLM과 무작위 초기화된 행동 헤드로부터 단일 단계 공동 최적화를 통해 훈련됩니다. 50가지 다양한 조작 작업을 포함하는 Meta-World MT50 벤치마크에서 FabriVLA는 계층 평균 성공률 90.0%를 달성하여, 1B 규모 VLM 기반의 소형 VLA가 수십억 파라미터 VLA 백본에 의존하지 않고도 강력한 성능을 낼 수 있음을 입증합니다.

## 핵심 내용
본 논문에서는 정밀한 다중 작업 조작을 위한 경량 비전-언어-행동 모델인 FabriVLA를 제시합니다. FabriVLA는 InternVL3.5 비전-언어 백본과 플로우 매칭 행동 헤드를 결합하며, 이 헤드는 행동 토큰 간 게이트 자기 주의 메커니즘과 향상된 공간적 맥락을 위한 얕은 VLM 계층 융합을 특징으로 합니다. 모델은 사전 훈련된 VLM과 무작위 초기화된 행동 헤드로부터 단일 단계 공동 최적화를 통해 훈련됩니다. 50가지 다양한 조작 작업을 포함하는 Meta-World MT50 벤치마크에서 FabriVLA는 계층 평균 성공률 90.0%를 달성하여, 1B 규모 VLM 기반의 소형 VLA가 수십억 파라미터 VLA 백본에 의존하지 않고도 강력한 성능을 낼 수 있음을 입증합니다.

## 参考
- http://arxiv.org/abs/2607.08575v2
