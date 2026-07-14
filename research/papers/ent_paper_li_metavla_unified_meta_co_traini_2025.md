---
$id: ent_paper_li_metavla_unified_meta_co_traini_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MetaVLA: Unified Meta Co-training For Efficient Embodied Adaption'
  zh: MetaVLA
  ko: 'MetaVLA: Unified Meta Co-training For Efficient Embodied Adaption'
summary:
  en: 'MetaVLA: Unified Meta Co-training For Efficient Embodied Adaption (MetaVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, Meta Reality Labs, USA.'
  zh: 'MetaVLA: Unified Meta Co-training For Efficient Embodied Adaption (MetaVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, Meta Reality Labs, USA.'
  ko: 'MetaVLA: Unified Meta Co-training For Efficient Embodied Adaption (MetaVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, Meta Reality Labs, USA.'
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
- metavla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.05580v3.
sources:
- id: src_001
  type: paper
  title: 'MetaVLA: Unified Meta Co-training For Efficient Embodied Adaption (arXiv)'
  url: https://arxiv.org/abs/2510.05580
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MetaVLA source
  url: https://doi.org/10.48550/arXiv.2510.05580
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models show promise in embodied reasoning, yet remain far from true generalists-they often require task-specific fine-tuning, incur high compute costs, and generalize poorly to unseen tasks. We propose MetaVLA, a unified, backbone-agnostic post-training framework for efficient and scalable alignment. MetaVLA introduces Context-Aware Meta Co-Training, which consolidates diverse target tasks into a single fine-tuning stage while leveraging structurally diverse auxiliary tasks to improve in-domain generalization. Unlike naive multi-task SFT, MetaVLA integrates a lightweight meta-learning mechanism-derived from Attentive Neural Processes-to enable rapid adaptation from diverse contexts with minimal architectural change or inference overhead. On the LIBERO benchmark, MetaVLA with six auxiliary tasks outperforms OpenVLA by up to 8.0% on long-horizon tasks, reduces training steps from 240K to 75K, and cuts GPU time by ~76%. These results show that scalable, low-resource post-training is achievable-paving the way toward general-purpose embodied agents. Code will be available.

## 核心内容
Vision-Language-Action (VLA) models show promise in embodied reasoning, yet remain far from true generalists-they often require task-specific fine-tuning, incur high compute costs, and generalize poorly to unseen tasks. We propose MetaVLA, a unified, backbone-agnostic post-training framework for efficient and scalable alignment. MetaVLA introduces Context-Aware Meta Co-Training, which consolidates diverse target tasks into a single fine-tuning stage while leveraging structurally diverse auxiliary tasks to improve in-domain generalization. Unlike naive multi-task SFT, MetaVLA integrates a lightweight meta-learning mechanism-derived from Attentive Neural Processes-to enable rapid adaptation from diverse contexts with minimal architectural change or inference overhead. On the LIBERO benchmark, MetaVLA with six auxiliary tasks outperforms OpenVLA by up to 8.0% on long-horizon tasks, reduces training steps from 240K to 75K, and cuts GPU time by ~76%. These results show that scalable, low-resource post-training is achievable-paving the way toward general-purpose embodied agents. Code will be available.

## 参考
- http://arxiv.org/abs/2510.05580v3

