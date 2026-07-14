---
$id: ent_paper_park_acg_action_coherence_guidance_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ACG: Action Coherence Guidance for Flow-based VLA models'
  zh: ACG
  ko: 'ACG: Action Coherence Guidance for Flow-based VLA models'
summary:
  en: 'ACG: Action Coherence Guidance for Flow-based VLA models (ACG), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by KAIST AI.'
  zh: 'ACG: Action Coherence Guidance for Flow-based VLA models (ACG), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by KAIST AI.'
  ko: 'ACG: Action Coherence Guidance for Flow-based VLA models (ACG), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by KAIST AI.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- acg
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.22201v2.
sources:
- id: src_001
  type: paper
  title: 'ACG: Action Coherence Guidance for Flow-based VLA models (arXiv)'
  url: https://arxiv.org/abs/2510.22201
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ACG source
  url: https://doi.org/10.48550/arXiv.2510.22201
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Diffusion and flow matching models have emerged as powerful robot policies, enabling Vision-Language-Action (VLA) models to generalize across diverse scenes and instructions. Yet, when trained via imitation learning, their high generative capacity makes them sensitive to noise in human demonstrations: jerks, pauses, and jitter which reduce action coherence. Reduced action coherence causes instability and trajectory drift during deployment, failures that are catastrophic in fine-grained manipulation where precision is crucial. In this paper, we present Action Coherence Guidance (ACG) for VLA models, a training-free test-time guidance algorithm that improves action coherence and thereby yields performance gains. Evaluated on RoboCasa, DexMimicGen, and real-world SO-101 tasks, ACG consistently improves action coherence and boosts success rates across diverse manipulation tasks. Code and project page are available at https://github.com/DAVIAN-Robotics/ACG and https://DAVIAN-Robotics.github.io/ACG , respectively.

## 核心内容
Diffusion and flow matching models have emerged as powerful robot policies, enabling Vision-Language-Action (VLA) models to generalize across diverse scenes and instructions. Yet, when trained via imitation learning, their high generative capacity makes them sensitive to noise in human demonstrations: jerks, pauses, and jitter which reduce action coherence. Reduced action coherence causes instability and trajectory drift during deployment, failures that are catastrophic in fine-grained manipulation where precision is crucial. In this paper, we present Action Coherence Guidance (ACG) for VLA models, a training-free test-time guidance algorithm that improves action coherence and thereby yields performance gains. Evaluated on RoboCasa, DexMimicGen, and real-world SO-101 tasks, ACG consistently improves action coherence and boosts success rates across diverse manipulation tasks. Code and project page are available at https://github.com/DAVIAN-Robotics/ACG and https://DAVIAN-Robotics.github.io/ACG , respectively.

## 参考
- http://arxiv.org/abs/2510.22201v2

