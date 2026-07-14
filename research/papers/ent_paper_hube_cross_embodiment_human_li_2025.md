---
$id: ent_paper_hube_cross_embodiment_human_li_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HuBE: Cross-Embodiment Human-like Behavior Execution for Humanoid Robots'
  zh: 'HuBE: Cross-Embodiment Human-like Behavior Execution for Humanoid Robots'
  ko: 'HuBE: Cross-Embodiment Human-like Behavior Execution for Humanoid Robots'
summary:
  en: 'HuBE: Cross-Embodiment Human-like Behavior Execution for Humanoid Robots is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: 'HuBE: Cross-Embodiment Human-like Behavior Execution for Humanoid Robots is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  ko: 'HuBE: Cross-Embodiment Human-like Behavior Execution for Humanoid Robots is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hube
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.19002v1.
sources:
- id: src_001
  type: paper
  title: 'HuBE: Cross-Embodiment Human-like Behavior Execution for Humanoid Robots (arXiv)'
  url: https://arxiv.org/abs/2508.19002
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Achieving both behavioral similarity and appropriateness in human-like motion generation for humanoid robot remains an open challenge, further compounded by the lack of cross-embodiment adaptability. To address this problem, we propose HuBE, a bi-level closed-loop framework that integrates robot state, goal poses, and contextual situations to generate human-like behaviors, ensuring both behavioral similarity and appropriateness, and eliminating structural mismatches between motion generation and execution. To support this framework, we construct HPose, a context-enriched dataset featuring fine-grained situational annotations. Furthermore, we introduce a bone scaling-based data augmentation strategy that ensures millimeter-level compatibility across heterogeneous humanoid robots. Comprehensive evaluations on multiple commercial platforms demonstrate that HuBE significantly improves motion similarity, behavioral appropriateness, and computational efficiency over state-of-the-art baselines, establishing a solid foundation for transferable and human-like behavior execution across diverse humanoid robots.

## 核心内容
Achieving both behavioral similarity and appropriateness in human-like motion generation for humanoid robot remains an open challenge, further compounded by the lack of cross-embodiment adaptability. To address this problem, we propose HuBE, a bi-level closed-loop framework that integrates robot state, goal poses, and contextual situations to generate human-like behaviors, ensuring both behavioral similarity and appropriateness, and eliminating structural mismatches between motion generation and execution. To support this framework, we construct HPose, a context-enriched dataset featuring fine-grained situational annotations. Furthermore, we introduce a bone scaling-based data augmentation strategy that ensures millimeter-level compatibility across heterogeneous humanoid robots. Comprehensive evaluations on multiple commercial platforms demonstrate that HuBE significantly improves motion similarity, behavioral appropriateness, and computational efficiency over state-of-the-art baselines, establishing a solid foundation for transferable and human-like behavior execution across diverse humanoid robots.

## 参考
- http://arxiv.org/abs/2508.19002v1

