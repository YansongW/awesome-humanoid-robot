---
$id: ent_paper_huang_thinkact_vision_language_actio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning'
  zh: ThinkAct
  ko: 'ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning'
summary:
  en: 'ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning (ThinkAct), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, National Taiwan University.'
  zh: 'ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning (ThinkAct), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, National Taiwan University.'
  ko: 'ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning (ThinkAct), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, National Taiwan University.'
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
- thinkact
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.16815v2.
sources:
- id: src_001
  type: paper
  title: 'ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning (arXiv)'
  url: https://arxiv.org/abs/2507.16815
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ThinkAct source
  url: https://doi.org/10.48550/arXiv.2507.16815
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) reasoning tasks require agents to interpret multimodal instructions, perform long-horizon planning, and act adaptively in dynamic environments. Existing approaches typically train VLA models in an end-to-end fashion, directly mapping inputs to actions without explicit reasoning, which hinders their ability to plan over multiple steps or adapt to complex task variations. In this paper, we propose ThinkAct, a dual-system framework that bridges high-level reasoning with low-level action execution via reinforced visual latent planning. ThinkAct trains a multimodal LLM to generate embodied reasoning plans guided by reinforcing action-aligned visual rewards based on goal completion and trajectory consistency. These reasoning plans are compressed into a visual plan latent that conditions a downstream action model for robust action execution on target environments. Extensive experiments on embodied reasoning and robot manipulation benchmarks demonstrate that ThinkAct enables few-shot adaptation, long-horizon planning, and self-correction behaviors in complex embodied AI tasks.

## 核心内容
Vision-language-action (VLA) reasoning tasks require agents to interpret multimodal instructions, perform long-horizon planning, and act adaptively in dynamic environments. Existing approaches typically train VLA models in an end-to-end fashion, directly mapping inputs to actions without explicit reasoning, which hinders their ability to plan over multiple steps or adapt to complex task variations. In this paper, we propose ThinkAct, a dual-system framework that bridges high-level reasoning with low-level action execution via reinforced visual latent planning. ThinkAct trains a multimodal LLM to generate embodied reasoning plans guided by reinforcing action-aligned visual rewards based on goal completion and trajectory consistency. These reasoning plans are compressed into a visual plan latent that conditions a downstream action model for robust action execution on target environments. Extensive experiments on embodied reasoning and robot manipulation benchmarks demonstrate that ThinkAct enables few-shot adaptation, long-horizon planning, and self-correction behaviors in complex embodied AI tasks.

## 参考
- http://arxiv.org/abs/2507.16815v2

