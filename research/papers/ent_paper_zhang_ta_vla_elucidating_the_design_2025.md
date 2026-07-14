---
$id: ent_paper_zhang_ta_vla_elucidating_the_design_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models'
  zh: TA-VLA
  ko: 'TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models'
summary:
  en: 'TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models (TA-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing Academy of Artificial Intelligence, BAAI, Institute for AI Industry
    Research (AIR), Tsinghua Univeristy, Nanyang Technological University, and published at CoRL25.'
  zh: 'TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models (TA-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing Academy of Artificial Intelligence, BAAI, Institute for AI Industry
    Research (AIR), Tsinghua Univeristy, Nanyang Technological University, and published at CoRL25.'
  ko: 'TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models (TA-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing Academy of Artificial Intelligence, BAAI, Institute for AI Industry
    Research (AIR), Tsinghua Univeristy, Nanyang Technological University, and published at CoRL25.'
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
- robotic_manipulation
- ta_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.07962v1.
sources:
- id: src_001
  type: paper
  title: 'TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2509.07962
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: TA-VLA source
  url: https://doi.org/10.48550/arXiv.2509.07962
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Many robotic manipulation tasks require sensing and responding to force signals such as torque to assess whether the task has been successfully completed and to enable closed-loop control. However, current Vision-Language-Action (VLA) models lack the ability to integrate such subtle physical feedback. In this work, we explore Torque-aware VLA models, aiming to bridge this gap by systematically studying the design space for incorporating torque signals into existing VLA architectures. We identify and evaluate several strategies, leading to three key findings. First, introducing torque adapters into the decoder consistently outperforms inserting them into the encoder.Third, inspired by joint prediction and planning paradigms in autonomous driving, we propose predicting torque as an auxiliary output, which further improves performance. This strategy encourages the model to build a physically grounded internal representation of interaction dynamics. Extensive quantitative and qualitative experiments across contact-rich manipulation benchmarks validate our findings.

## 核心内容
Many robotic manipulation tasks require sensing and responding to force signals such as torque to assess whether the task has been successfully completed and to enable closed-loop control. However, current Vision-Language-Action (VLA) models lack the ability to integrate such subtle physical feedback. In this work, we explore Torque-aware VLA models, aiming to bridge this gap by systematically studying the design space for incorporating torque signals into existing VLA architectures. We identify and evaluate several strategies, leading to three key findings. First, introducing torque adapters into the decoder consistently outperforms inserting them into the encoder.Third, inspired by joint prediction and planning paradigms in autonomous driving, we propose predicting torque as an auxiliary output, which further improves performance. This strategy encourages the model to build a physically grounded internal representation of interaction dynamics. Extensive quantitative and qualitative experiments across contact-rich manipulation benchmarks validate our findings.

## 参考
- http://arxiv.org/abs/2509.07962v1

