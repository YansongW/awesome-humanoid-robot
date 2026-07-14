---
$id: ent_paper_zhang_robochemist_long_horizon_and_s_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboChemist: Long-Horizon and Safety-Compliant Robotic Chemical Experimentation'
  zh: RoboChemist
  ko: 'RoboChemist: Long-Horizon and Safety-Compliant Robotic Chemical Experimentation'
summary:
  en: 'RoboChemist: Long-Horizon and Safety-Compliant Robotic Chemical Experimentation (RoboChemist), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, and published at CoRL25.'
  zh: 'RoboChemist: Long-Horizon and Safety-Compliant Robotic Chemical Experimentation (RoboChemist), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, and published at CoRL25.'
  ko: 'RoboChemist: Long-Horizon and Safety-Compliant Robotic Chemical Experimentation (RoboChemist), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, and published at CoRL25.'
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
- robochemist
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.08820v1.
sources:
- id: src_001
  type: paper
  title: 'RoboChemist: Long-Horizon and Safety-Compliant Robotic Chemical Experimentation (arXiv)'
  url: https://arxiv.org/abs/2509.08820
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RoboChemist source
  url: https://doi.org/10.48550/arXiv.2509.08820
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Robotic chemists promise to both liberate human experts from repetitive tasks and accelerate scientific discovery, yet remain in their infancy. Chemical experiments involve long-horizon procedures over hazardous and deformable substances, where success requires not only task completion but also strict compliance with experimental norms. To address these challenges, we propose \textit{RoboChemist}, a dual-loop framework that integrates Vision-Language Models (VLMs) with Vision-Language-Action (VLA) models. Unlike prior VLM-based systems (e.g., VoxPoser, ReKep) that rely on depth perception and struggle with transparent labware, and existing VLA systems (e.g., RDT, pi0) that lack semantic-level feedback for complex tasks, our method leverages a VLM to serve as (1) a planner to decompose tasks into primitive actions, (2) a visual prompt generator to guide VLA models, and (3) a monitor to assess task success and regulatory compliance. Notably, we introduce a VLA interface that accepts image-based visual targets from the VLM, enabling precise, goal-conditioned control. Our system successfully executes both primitive actions and complete multi-step chemistry protocols. Results show 23.57% higher average success rate and a 0.298 average increase in compliance rate over state-of-the-art VLA baselines, while also demonstrating strong generalization to objects and tasks.

## 核心内容
Robotic chemists promise to both liberate human experts from repetitive tasks and accelerate scientific discovery, yet remain in their infancy. Chemical experiments involve long-horizon procedures over hazardous and deformable substances, where success requires not only task completion but also strict compliance with experimental norms. To address these challenges, we propose \textit{RoboChemist}, a dual-loop framework that integrates Vision-Language Models (VLMs) with Vision-Language-Action (VLA) models. Unlike prior VLM-based systems (e.g., VoxPoser, ReKep) that rely on depth perception and struggle with transparent labware, and existing VLA systems (e.g., RDT, pi0) that lack semantic-level feedback for complex tasks, our method leverages a VLM to serve as (1) a planner to decompose tasks into primitive actions, (2) a visual prompt generator to guide VLA models, and (3) a monitor to assess task success and regulatory compliance. Notably, we introduce a VLA interface that accepts image-based visual targets from the VLM, enabling precise, goal-conditioned control. Our system successfully executes both primitive actions and complete multi-step chemistry protocols. Results show 23.57% higher average success rate and a 0.298 average increase in compliance rate over state-of-the-art VLA baselines, while also demonstrating strong generalization to objects and tasks.

## 参考
- http://arxiv.org/abs/2509.08820v1

