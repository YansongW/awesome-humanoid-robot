---
$id: ent_paper_ke_3d_diffuser_actor_policy_diffu_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '3D Diffuser Actor: Policy Diffusion with 3D Scene Representations'
  zh: 3D Diffuser Actor
  ko: '3D Diffuser Actor: Policy Diffusion with 3D Scene Representations'
summary:
  en: '3D Diffuser Actor: Policy Diffusion with 3D Scene Representations (3D Diffuser Actor), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, and published at CoRL 2024.'
  zh: '3D Diffuser Actor: Policy Diffusion with 3D Scene Representations (3D Diffuser Actor), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, and published at CoRL 2024.'
  ko: '3D Diffuser Actor: Policy Diffusion with 3D Scene Representations (3D Diffuser Actor), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, and published at CoRL 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- 3d_diffuser_actor
- generalist_policy
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2402.10885v3.
sources:
- id: src_001
  type: paper
  title: 3D Diffuser Actor source
  url: https://proceedings.mlr.press/v270/ke25a.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Diffusion policies are conditional diffusion models that learn robot action distributions conditioned on the robot and environment state. They have recently shown to outperform both deterministic and alternative action distribution learning formulations. 3D robot policies use 3D scene feature representations aggregated from a single or multiple camera views using sensed depth. They have shown to generalize better than their 2D counterparts across camera viewpoints. We unify these two lines of work and present 3D Diffuser Actor, a neural policy equipped with a novel 3D denoising transformer that fuses information from the 3D visual scene, a language instruction and proprioception to predict the noise in noised 3D robot pose trajectories. 3D Diffuser Actor sets a new state-of-the-art on RLBench with an absolute performance gain of 18.1% over the current SOTA on a multi-view setup and an absolute gain of 13.1% on a single-view setup. On the CALVIN benchmark, it improves over the current SOTA by a 9% relative increase. It also learns to control a robot manipulator in the real world from a handful of demonstrations. Through thorough comparisons with the current SOTA policies and ablations of our model, we show 3D Diffuser Actor's design choices dramatically outperform 2D representations, regression and classification objectives, absolute attentions, and holistic non-tokenized 3D scene embeddings.

## 核心内容
Diffusion policies are conditional diffusion models that learn robot action distributions conditioned on the robot and environment state. They have recently shown to outperform both deterministic and alternative action distribution learning formulations. 3D robot policies use 3D scene feature representations aggregated from a single or multiple camera views using sensed depth. They have shown to generalize better than their 2D counterparts across camera viewpoints. We unify these two lines of work and present 3D Diffuser Actor, a neural policy equipped with a novel 3D denoising transformer that fuses information from the 3D visual scene, a language instruction and proprioception to predict the noise in noised 3D robot pose trajectories. 3D Diffuser Actor sets a new state-of-the-art on RLBench with an absolute performance gain of 18.1% over the current SOTA on a multi-view setup and an absolute gain of 13.1% on a single-view setup. On the CALVIN benchmark, it improves over the current SOTA by a 9% relative increase. It also learns to control a robot manipulator in the real world from a handful of demonstrations. Through thorough comparisons with the current SOTA policies and ablations of our model, we show 3D Diffuser Actor's design choices dramatically outperform 2D representations, regression and classification objectives, absolute attentions, and holistic non-tokenized 3D scene embeddings.

## 参考
- http://arxiv.org/abs/2402.10885v3

