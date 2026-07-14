---
$id: ent_paper_one_policy_but_many_worlds_a_s_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'One Policy but Many Worlds: A Scalable Unified Policy for Versatile Humanoid Locomotion'
  zh: 'One Policy but Many Worlds: A Scalable Unified Policy for Versatile Humanoid Locomotion'
  ko: 'One Policy but Many Worlds: A Scalable Unified Policy for Versatile Humanoid Locomotion'
summary:
  en: 'One Policy but Many Worlds: A Scalable Unified Policy for Versatile Humanoid Locomotion is a 2025 work on locomotion
    for humanoid robots.'
  zh: 'One Policy but Many Worlds: A Scalable Unified Policy for Versatile Humanoid Locomotion is a 2025 work on locomotion
    for humanoid robots.'
  ko: 'One Policy but Many Worlds: A Scalable Unified Policy for Versatile Humanoid Locomotion is a 2025 work on locomotion
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
- one_policy_but_many_worlds
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.18780v3.
sources:
- id: src_001
  type: paper
  title: 'One Policy but Many Worlds: A Scalable Unified Policy for Versatile Humanoid Locomotion (arXiv)'
  url: https://arxiv.org/abs/2505.18780
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Achieving versatile humanoid locomotion with a single policy presents a critical scalability challenge. Prevailing methods often rely on distilling multiple terrain-specific teacher policies into a unified student policy. However, while such distillation captures basic locomotion primitives, it struggles to organically compose these skills to adapt to complex environments, resulting in poor generalization to novel composite terrains unseen during training. To overcome this, we present DreamPolicy, a unified framework that integrates offline data with a diffusion-based world model, enabling a single policy to master both known and unseen terrains. Central to our approach is a terrain-aware world model, driven by an autoregressive diffusion world model trained on aggregated rollouts from specialized policies. This model synthesizes physically plausible future trajectories, which serve as dynamic objectives for a conditioned policy, thereby bypassing manual reward engineering. Unlike distillation, our world model captures generalizable locomotion skills, allowing for robust zero-shot transfer to unseen composite terrains. DreamPolicy naturally scales with data availability. As the offline dataset expands, the diffusion world model continuously acquires richer skills. Experiments demonstrate that DreamPolicy outperforms the strongest baseline by up to 27\% on unseen terrains and 38\% on combined terrains. By unifying world model-based planning and policy learning, DreamPolicy breaks the "one task, one policy" bottleneck and establishes a scalable, data-driven paradigm for generalist humanoid control.

## 核心内容
Achieving versatile humanoid locomotion with a single policy presents a critical scalability challenge. Prevailing methods often rely on distilling multiple terrain-specific teacher policies into a unified student policy. However, while such distillation captures basic locomotion primitives, it struggles to organically compose these skills to adapt to complex environments, resulting in poor generalization to novel composite terrains unseen during training. To overcome this, we present DreamPolicy, a unified framework that integrates offline data with a diffusion-based world model, enabling a single policy to master both known and unseen terrains. Central to our approach is a terrain-aware world model, driven by an autoregressive diffusion world model trained on aggregated rollouts from specialized policies. This model synthesizes physically plausible future trajectories, which serve as dynamic objectives for a conditioned policy, thereby bypassing manual reward engineering. Unlike distillation, our world model captures generalizable locomotion skills, allowing for robust zero-shot transfer to unseen composite terrains. DreamPolicy naturally scales with data availability. As the offline dataset expands, the diffusion world model continuously acquires richer skills. Experiments demonstrate that DreamPolicy outperforms the strongest baseline by up to 27\% on unseen terrains and 38\% on combined terrains. By unifying world model-based planning and policy learning, DreamPolicy breaks the "one task, one policy" bottleneck and establishes a scalable, data-driven paradigm for generalist humanoid control.

## 参考
- http://arxiv.org/abs/2505.18780v3

