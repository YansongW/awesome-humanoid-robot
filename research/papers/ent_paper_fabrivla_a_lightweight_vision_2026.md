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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.08575v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    en/ko body retranslated from zh deep-read (707 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2607.08575v2

## Overview
The core innovation of FabriVLA lies in its lightweight architecture: it employs InternVL3.5 as the vision-language backbone, paired with a flow-matching action head. This action head processes interactions among action tokens through a gated self-attention mechanism, while integrating shallow VLM layers to enhance spatial context information. The model is trained via single-stage joint optimization, starting from a pretrained VLM and a randomly initialized action head. On the Meta-World MT50 benchmark, which includes 50 diverse tasks, FabriVLA achieves a 90.0% tier-average success rate, demonstrating that a compact model based on a 1B-scale VLM can effectively replace massive multi-billion-parameter backbones.

## Content
### Method
- **Architecture**: FabriVLA consists of an InternVL3.5 vision-language backbone and a flow-matching action head. The action head incorporates a gated self-attention mechanism to handle dependencies among action tokens and enriches spatial context through the integration of shallow VLM layers.
- **Training**: It adopts a single-stage joint optimization strategy, starting from a pretrained VLM and a randomly initialized action head, without the need for staged training.

### Experimental Setup
- **Benchmark**: Meta-World MT50, comprising 50 distinct manipulation tasks.
- **Evaluation Metric**: Tier-average success rate.

### Key Results
- **Performance**: Achieves a 90.0% tier-average success rate on Meta-World MT50.
- **Scale Advantage**: The model is based on a 1B-parameter VLM, achieving strong performance without relying on VLA backbones with billions of parameters.

### Conclusion
FabriVLA demonstrates the effectiveness of compact VLA models in precise multi-task manipulation, significantly reducing parameter scale while maintaining high performance through lightweight design.

## 개요
FabriVLA의 핵심 혁신은 경량화된 아키텍처에 있습니다: InternVL3.5를 시각-언어 백본으로 사용하고, 스트림 매칭 동작 헤드를 결합합니다. 이 동작 헤드는 게이트 자기 주의 메커니즘을 통해 동작 토큰 간의 상호작용을 처리하며, 얕은 VLM 레이어를 통합하여 공간 컨텍스트 정보를 강화합니다. 모델은 사전 훈련된 VLM과 무작위 초기화된 동작 헤드로 시작하여 단일 단계 공동 최적화로 훈련됩니다. 50가지 다양한 작업을 포함하는 Meta-World MT50 벤치마크에서 FabriVLA는 90.0%의 계층 평균 성공률을 달성하여, 1B 규모 VLM 기반의 컴팩트 모델이 거대한 다중 파라미터 백본을 효과적으로 대체할 수 있음을 보여줍니다.

## 핵심 내용
### 방법
- **아키텍처**: FabriVLA는 InternVL3.5 시각-언어 백본 네트워크와 스트림 매칭 동작 헤드로 구성됩니다. 동작 헤드는 게이트 자기 주의 메커니즘을 포함하여 동작 토큰 간의 의존성을 처리하고, 얕은 VLM 레이어 융합을 통해 공간 컨텍스트를 풍부하게 합니다.
- **훈련**: 사전 훈련된 VLM과 무작위 초기화된 동작 헤드로 시작하는 단일 단계 공동 최적화 전략을 채택하며, 단계별 훈련이 필요하지 않습니다.

### 실험 설정
- **벤치마크**: Meta-World MT50, 50가지 다양한 조작 작업 포함.
- **평가 지표**: 계층 평균 성공률(tier-average success rate).

### 주요 결과
- **성능**: Meta-World MT50에서 90.0%의 계층 평균 성공률 달성.
- **규모 이점**: 모델은 1B 파라미터 규모의 VLM을 기반으로 하며, 수십억 파라미터의 VLA 백본에 의존하지 않고도 강력한 성능을 구현합니다.

### 결론
FabriVLA는 컴팩트한 VLA 모델이 정밀한 다중 작업 조작에서 효과적임을 입증하며, 경량화 설계를 통해 높은 성능을 유지하면서 파라미터 규모를 크게 줄였습니다.
