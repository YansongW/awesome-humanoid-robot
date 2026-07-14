---
$id: ent_paper_lessmimic_long_horizon_humanoi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LessMimic: Long-Horizon Humanoid Interaction with Unified Distance Field Representations'
  zh: 'LessMimic: Long-Horizon Humanoid Interaction with Unified Distance Field Representations'
  ko: 'LessMimic: Long-Horizon Humanoid Interaction with Unified Distance Field Representations'
summary:
  en: 'LessMimic: Long-Horizon Humanoid Interaction with Unified Distance Field Representations is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'LessMimic: Long-Horizon Humanoid Interaction with Unified Distance Field Representations is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'LessMimic: Long-Horizon Humanoid Interaction with Unified Distance Field Representations is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
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
- lessmimic
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.21723v1.
sources:
- id: src_001
  type: paper
  title: 'LessMimic: Long-Horizon Humanoid Interaction with Unified Distance Field Representations (arXiv)'
  url: https://arxiv.org/abs/2602.21723
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'LessMimic: Long-Horizon Humanoid Interaction with Unified Distance Field Representations project page'
  url: https://yzhu.io/preprint/humanoid2026lessmimic/
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots that autonomously interact with physical environments over extended horizons represent a central goal of embodied intelligence. Existing approaches rely on reference motions or task-specific rewards, tightly coupling policies to particular object geometries and precluding multi-skill generalization within a single framework. A unified interaction representation enabling reference-free inference, geometric generalization, and long-horizon skill composition within one policy remains an open challenge. Here we show that Distance Field (DF) provides such a representation: LessMimic conditions a single whole-body policy on DF-derived geometric cues--surface distances, gradients, and velocity decompositions--removing the need for motion references, with interaction latents encoded via a Variational Auto-Encoder (VAE) and post-trained using Adversarial Interaction Priors (AIP) under Reinforcement Learning (RL). Through DAgger-style distillation that aligns DF latents with egocentric depth features, LessMimic further transfers seamlessly to vision-only deployment without motion capture (MoCap) infrastructure. A single LessMimic policy achieves 80--100% success across object scales from 0.4x to 1.6x on PickUp and SitStand where baselines degrade sharply, attains 62.1% success on 5 task instances trajectories, and remains viable up to 40 sequentially composed tasks. By grounding interaction in local geometry rather than demonstrations, LessMimic offers a scalable path toward humanoid robots that generalize, compose skills, and recover from failures in unstructured environments.

## 核心内容
Humanoid robots that autonomously interact with physical environments over extended horizons represent a central goal of embodied intelligence. Existing approaches rely on reference motions or task-specific rewards, tightly coupling policies to particular object geometries and precluding multi-skill generalization within a single framework. A unified interaction representation enabling reference-free inference, geometric generalization, and long-horizon skill composition within one policy remains an open challenge. Here we show that Distance Field (DF) provides such a representation: LessMimic conditions a single whole-body policy on DF-derived geometric cues--surface distances, gradients, and velocity decompositions--removing the need for motion references, with interaction latents encoded via a Variational Auto-Encoder (VAE) and post-trained using Adversarial Interaction Priors (AIP) under Reinforcement Learning (RL). Through DAgger-style distillation that aligns DF latents with egocentric depth features, LessMimic further transfers seamlessly to vision-only deployment without motion capture (MoCap) infrastructure. A single LessMimic policy achieves 80--100% success across object scales from 0.4x to 1.6x on PickUp and SitStand where baselines degrade sharply, attains 62.1% success on 5 task instances trajectories, and remains viable up to 40 sequentially composed tasks. By grounding interaction in local geometry rather than demonstrations, LessMimic offers a scalable path toward humanoid robots that generalize, compose skills, and recover from failures in unstructured environments.

## 参考
- http://arxiv.org/abs/2602.21723v1

