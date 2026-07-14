---
$id: ent_paper_more_mixture_of_residual_exper_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MoRE: Mixture of Residual Experts for Humanoid Lifelike Gaits Learning on Complex Terrains'
  zh: 'MoRE: Mixture of Residual Experts for Humanoid Lifelike Gaits Learning on Complex Terrains'
  ko: 'MoRE: Mixture of Residual Experts for Humanoid Lifelike Gaits Learning on Complex Terrains'
summary:
  en: 'MoRE: Mixture of Residual Experts for Humanoid Lifelike Gaits Learning on Complex Terrains is a 2025 work on locomotion
    for humanoid robots.'
  zh: 'MoRE: Mixture of Residual Experts for Humanoid Lifelike Gaits Learning on Complex Terrains is a 2025 work on locomotion
    for humanoid robots.'
  ko: 'MoRE: Mixture of Residual Experts for Humanoid Lifelike Gaits Learning on Complex Terrains is a 2025 work on locomotion
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- more
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.08840v2.
sources:
- id: src_001
  type: paper
  title: 'MoRE: Mixture of Residual Experts for Humanoid Lifelike Gaits Learning on Complex Terrains (arXiv)'
  url: https://arxiv.org/abs/2506.08840
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'MoRE: Mixture of Residual Experts for Humanoid Lifelike Gaits Learning on Complex Terrains project page'
  url: https://more-humanoid.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots have demonstrated robust locomotion capabilities using Reinforcement Learning (RL)-based approaches. Further, to obtain human-like behaviors, existing methods integrate human motion-tracking or motion prior in the RL framework. However, these methods are limited in flat terrains with proprioception only, restricting their abilities to traverse challenging terrains with human-like gaits. In this work, we propose a novel framework using a mixture of latent residual experts with multi-discriminators to train an RL policy, which is capable of traversing complex terrains in controllable lifelike gaits with exteroception. Our two-stage training pipeline first teaches the policy to traverse complex terrains using a depth camera, and then enables gait-commanded switching between human-like gait patterns. We also design gait rewards to adjust human-like behaviors like robot base height. Simulation and real-world experiments demonstrate that our framework exhibits exceptional performance in traversing complex terrains, and achieves seamless transitions between multiple human-like gait patterns.

## 核心内容
Humanoid robots have demonstrated robust locomotion capabilities using Reinforcement Learning (RL)-based approaches. Further, to obtain human-like behaviors, existing methods integrate human motion-tracking or motion prior in the RL framework. However, these methods are limited in flat terrains with proprioception only, restricting their abilities to traverse challenging terrains with human-like gaits. In this work, we propose a novel framework using a mixture of latent residual experts with multi-discriminators to train an RL policy, which is capable of traversing complex terrains in controllable lifelike gaits with exteroception. Our two-stage training pipeline first teaches the policy to traverse complex terrains using a depth camera, and then enables gait-commanded switching between human-like gait patterns. We also design gait rewards to adjust human-like behaviors like robot base height. Simulation and real-world experiments demonstrate that our framework exhibits exceptional performance in traversing complex terrains, and achieves seamless transitions between multiple human-like gait patterns.

## 参考
- http://arxiv.org/abs/2506.08840v2

