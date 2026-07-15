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
  zh: 'REGENT: A Retrieval-Augmented Generalist Agent That Can Act In-Context in New Environments (REGENT), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by University of Pennsylvania, and published at ICLR25.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.04759v2.
sources:
- id: src_001
  type: paper
  title: REGENT source
  url: https://openreview.net/forum?id=NxyfSW6mLK
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Building generalist agents that can rapidly adapt to new environments is a key challenge for deploying AI in the digital and real worlds. Is scaling current agent architectures the most effective way to build generalist agents? We propose a novel approach to pre-train relatively small policies on relatively small datasets and adapt them to unseen environments via in-context learning, without any finetuning. Our key idea is that retrieval offers a powerful bias for fast adaptation. Indeed, we demonstrate that even a simple retrieval-based 1-nearest neighbor agent offers a surprisingly strong baseline for today's state-of-the-art generalist agents. From this starting point, we construct a semi-parametric agent, REGENT, that trains a transformer-based policy on sequences of queries and retrieved neighbors. REGENT can generalize to unseen robotics and game-playing environments via retrieval augmentation and in-context learning, achieving this with up to 3x fewer parameters and up to an order-of-magnitude fewer pre-training datapoints, significantly outperforming today's state-of-the-art generalist agents. Website: https://kaustubhsridhar.github.io/regent-research

## 核心内容
Building generalist agents that can rapidly adapt to new environments is a key challenge for deploying AI in the digital and real worlds. Is scaling current agent architectures the most effective way to build generalist agents? We propose a novel approach to pre-train relatively small policies on relatively small datasets and adapt them to unseen environments via in-context learning, without any finetuning. Our key idea is that retrieval offers a powerful bias for fast adaptation. Indeed, we demonstrate that even a simple retrieval-based 1-nearest neighbor agent offers a surprisingly strong baseline for today's state-of-the-art generalist agents. From this starting point, we construct a semi-parametric agent, REGENT, that trains a transformer-based policy on sequences of queries and retrieved neighbors. REGENT can generalize to unseen robotics and game-playing environments via retrieval augmentation and in-context learning, achieving this with up to 3x fewer parameters and up to an order-of-magnitude fewer pre-training datapoints, significantly outperforming today's state-of-the-art generalist agents. Website: https://kaustubhsridhar.github.io/regent-research

## 参考
- http://arxiv.org/abs/2412.04759v2

