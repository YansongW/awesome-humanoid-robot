---
$id: ent_paper_liang_mm_act_learn_from_multimodal_p_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MM-ACT: Learn from Multimodal Parallel Generation to Act'
  zh: MM-ACT
  ko: 'MM-ACT: Learn from Multimodal Parallel Generation to Act'
summary:
  en: 'MM-ACT: Learn from Multimodal Parallel Generation to Act (MM-ACT), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Shanghai AI Laboratory, Shanghai Jiao Tong University, The University of Hong Kong,
    University of Science and Technology of China, Fudan University, Zhejiang University.'
  zh: 'MM-ACT: Learn from Multimodal Parallel Generation to Act (MM-ACT), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Shanghai AI Laboratory, Shanghai Jiao Tong University, The University of Hong Kong,
    University of Science and Technology of China, Fudan University, Zhejiang University.'
  ko: 'MM-ACT: Learn from Multimodal Parallel Generation to Act (MM-ACT), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Shanghai AI Laboratory, Shanghai Jiao Tong University, The University of Hong Kong,
    University of Science and Technology of China, Fudan University, Zhejiang University.'
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
- mm_act
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.00975v2.
sources:
- id: src_001
  type: paper
  title: 'MM-ACT: Learn from Multimodal Parallel Generation to Act (arXiv)'
  url: https://arxiv.org/abs/2512.00975
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MM-ACT source
  url: https://doi.org/10.48550/arXiv.2512.00975
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
A generalist robotic policy needs both semantic understanding for task planning and the ability to interact with the environment through predictive capabilities. To tackle this, we present MM-ACT, a unified Vision-Language-Action (VLA) model that integrates text, image, and action in shared token space and performs generation across all three modalities. MM-ACT adopts a re-mask parallel decoding strategy for text and image generation, and employs a one-step parallel decoding strategy for action generation to improve efficiency. We introduce Context-Shared Multimodal Learning, a unified training paradigm that supervises generation in all three modalities from a shared context, enhancing action generation through cross-modal learning. Experiments were conducted on the LIBERO simulation and Franka real-robot setups as well as RoboTwin2.0 to assess in-domain and out-of-domain performances respectively. Our approach achieves a success rate of 96.3% on LIBERO, 72.0% across three tasks of real Franka, and 52.38% across eight bimanual tasks of RoboTwin2.0 with an additional gain of 9.25% from cross-modal learning. We release our codes, models and data at https://github.com/HHYHRHY/MM-ACT.

## 核心内容
A generalist robotic policy needs both semantic understanding for task planning and the ability to interact with the environment through predictive capabilities. To tackle this, we present MM-ACT, a unified Vision-Language-Action (VLA) model that integrates text, image, and action in shared token space and performs generation across all three modalities. MM-ACT adopts a re-mask parallel decoding strategy for text and image generation, and employs a one-step parallel decoding strategy for action generation to improve efficiency. We introduce Context-Shared Multimodal Learning, a unified training paradigm that supervises generation in all three modalities from a shared context, enhancing action generation through cross-modal learning. Experiments were conducted on the LIBERO simulation and Franka real-robot setups as well as RoboTwin2.0 to assess in-domain and out-of-domain performances respectively. Our approach achieves a success rate of 96.3% on LIBERO, 72.0% across three tasks of real Franka, and 52.38% across eight bimanual tasks of RoboTwin2.0 with an additional gain of 9.25% from cross-modal learning. We release our codes, models and data at https://github.com/HHYHRHY/MM-ACT.

## 参考
- http://arxiv.org/abs/2512.00975v2

