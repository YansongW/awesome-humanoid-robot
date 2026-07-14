---
$id: ent_paper_fan_long_vla_unleashing_long_horiz_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation'
  zh: Long-VLA
  ko: 'Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation'
summary:
  en: 'Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation (Long-VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Zhejiang University, and published at
    CoRL25.'
  zh: 'Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation (Long-VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Zhejiang University, and published at
    CoRL25.'
  ko: 'Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation (Long-VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Zhejiang University, and published at
    CoRL25.'
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
- long_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.19958v2.
sources:
- id: src_001
  type: paper
  title: 'Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation (arXiv)'
  url: https://arxiv.org/abs/2508.19958
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Long-VLA source
  url: https://doi.org/10.48550/arXiv.2508.19958
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have become a cornerstone in robotic policy learning, leveraging large-scale multimodal data for robust and scalable control. However, existing VLA frameworks primarily address short-horizon tasks, and their effectiveness on long-horizon, multi-step robotic manipulation remains limited due to challenges in skill chaining and subtask dependencies. In this work, we introduce Long-VLA, the first end-to-end VLA model specifically designed for long-horizon robotic tasks. Our approach features a novel phase-aware input masking strategy that adaptively segments each subtask into moving and interaction phases, enabling the model to focus on phase-relevant sensory cues and enhancing subtask compatibility. This unified strategy preserves the scalability and data efficiency of VLA training, and our architecture-agnostic module can be seamlessly integrated into existing VLA models. We further propose the L-CALVIN benchmark to systematically evaluate long-horizon manipulation. Extensive experiments on both simulated and real-world tasks demonstrate that Long-VLA significantly outperforms prior state-of-the-art methods, establishing a new baseline for long-horizon robotic control.

## 核心内容
Vision-Language-Action (VLA) models have become a cornerstone in robotic policy learning, leveraging large-scale multimodal data for robust and scalable control. However, existing VLA frameworks primarily address short-horizon tasks, and their effectiveness on long-horizon, multi-step robotic manipulation remains limited due to challenges in skill chaining and subtask dependencies. In this work, we introduce Long-VLA, the first end-to-end VLA model specifically designed for long-horizon robotic tasks. Our approach features a novel phase-aware input masking strategy that adaptively segments each subtask into moving and interaction phases, enabling the model to focus on phase-relevant sensory cues and enhancing subtask compatibility. This unified strategy preserves the scalability and data efficiency of VLA training, and our architecture-agnostic module can be seamlessly integrated into existing VLA models. We further propose the L-CALVIN benchmark to systematically evaluate long-horizon manipulation. Extensive experiments on both simulated and real-world tasks demonstrate that Long-VLA significantly outperforms prior state-of-the-art methods, establishing a new baseline for long-horizon robotic control.

## 参考
- http://arxiv.org/abs/2508.19958v2

