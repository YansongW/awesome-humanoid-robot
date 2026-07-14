---
$id: ent_paper_wake_modality_driven_design_for_mul_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Modality-Driven Design for Multi-Step Dexterous Manipulation: Insights from Neuroscience'
  zh: Modality-Driven Design for Multi-Step Dexterous Manipulation
  ko: 'Modality-Driven Design for Multi-Step Dexterous Manipulation: Insights from Neuroscience'
summary:
  en: 'Modality-Driven Design for Multi-Step Dexterous Manipulation: Insights from Neuroscience (Modality-Driven Design for
    Multi-Step Dexterous Manipulation), is a 2024 large vision-language-action model for robotic manipulation.'
  zh: 'Modality-Driven Design for Multi-Step Dexterous Manipulation: Insights from Neuroscience (Modality-Driven Design for
    Multi-Step Dexterous Manipulation), is a 2024 large vision-language-action model for robotic manipulation.'
  ko: 'Modality-Driven Design for Multi-Step Dexterous Manipulation: Insights from Neuroscience (Modality-Driven Design for
    Multi-Step Dexterous Manipulation), is a 2024 large vision-language-action model for robotic manipulation.'
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
- modality_driven_design_for_mul
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.11337v1.
sources:
- id: src_001
  type: paper
  title: 'Modality-Driven Design for Multi-Step Dexterous Manipulation: Insights from Neuroscience (arXiv)'
  url: https://arxiv.org/abs/2412.11337
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Modality-Driven Design for Multi-Step Dexterous Manipulation source
  url: https://doi.org/10.48550/arXiv.2412.11337
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Multi-step dexterous manipulation is a fundamental skill in household scenarios, yet remains an underexplored area in robotics. This paper proposes a modular approach, where each step of the manipulation process is addressed with dedicated policies based on effective modality input, rather than relying on a single end-to-end model. To demonstrate this, a dexterous robotic hand performs a manipulation task involving picking up and rotating a box. Guided by insights from neuroscience, the task is decomposed into three sub-skills, 1)reaching, 2)grasping and lifting, and 3)in-hand rotation, based on the dominant sensory modalities employed in the human brain. Each sub-skill is addressed using distinct methods from a practical perspective: a classical controller, a Vision-Language-Action model, and a reinforcement learning policy with force feedback, respectively. We tested the pipeline on a real robot to demonstrate the feasibility of our approach. The key contribution of this study lies in presenting a neuroscience-inspired, modality-driven methodology for multi-step dexterous manipulation.

## 核心内容
Multi-step dexterous manipulation is a fundamental skill in household scenarios, yet remains an underexplored area in robotics. This paper proposes a modular approach, where each step of the manipulation process is addressed with dedicated policies based on effective modality input, rather than relying on a single end-to-end model. To demonstrate this, a dexterous robotic hand performs a manipulation task involving picking up and rotating a box. Guided by insights from neuroscience, the task is decomposed into three sub-skills, 1)reaching, 2)grasping and lifting, and 3)in-hand rotation, based on the dominant sensory modalities employed in the human brain. Each sub-skill is addressed using distinct methods from a practical perspective: a classical controller, a Vision-Language-Action model, and a reinforcement learning policy with force feedback, respectively. We tested the pipeline on a real robot to demonstrate the feasibility of our approach. The key contribution of this study lies in presenting a neuroscience-inspired, modality-driven methodology for multi-step dexterous manipulation.

## 参考
- http://arxiv.org/abs/2412.11337v1

