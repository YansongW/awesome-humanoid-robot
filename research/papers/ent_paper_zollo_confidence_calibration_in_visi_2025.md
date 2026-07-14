---
$id: ent_paper_zollo_confidence_calibration_in_visi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Confidence Calibration in Vision-Language-Action Models
  zh: Confidence Calibration in Vision-Language-Action Models
  ko: Confidence Calibration in Vision-Language-Action Models
summary:
  en: Confidence Calibration in Vision-Language-Action Models (Confidence Calibration in Vision-Language-Action Models), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Columbia University.
  zh: Confidence Calibration in Vision-Language-Action Models (Confidence Calibration in Vision-Language-Action Models), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Columbia University.
  ko: Confidence Calibration in Vision-Language-Action Models (Confidence Calibration in Vision-Language-Action Models), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Columbia University.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- confidence_calibration_in_visi
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.17383v2.
sources:
- id: src_001
  type: paper
  title: Confidence Calibration in Vision-Language-Action Models (arXiv)
  url: https://arxiv.org/abs/2507.17383
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Confidence Calibration in Vision-Language-Action Models source
  url: https://doi.org/10.48550/arXiv.2507.17383
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Trustworthy robot behavior requires not only high levels of task success but also that the robot can reliably quantify how likely it is to succeed. To this end, we present a first-of-its-kind study of confidence calibration in vision-language-action (VLA) foundation models, which map visual observations and natural language instructions to low-level robot motor commands. We establish a confidence baseline for VLAs, examine how task success relates to calibration error and how calibration evolves over time, and introduce two lightweight techniques to remedy the miscalibration we observe: prompt ensembles and action-wise Platt scaling. Our aim in this study is to begin to develop the tools and conceptual understanding necessary to render VLAs both highly performant and highly trustworthy via reliable uncertainty quantification.

## 核心内容
Trustworthy robot behavior requires not only high levels of task success but also that the robot can reliably quantify how likely it is to succeed. To this end, we present a first-of-its-kind study of confidence calibration in vision-language-action (VLA) foundation models, which map visual observations and natural language instructions to low-level robot motor commands. We establish a confidence baseline for VLAs, examine how task success relates to calibration error and how calibration evolves over time, and introduce two lightweight techniques to remedy the miscalibration we observe: prompt ensembles and action-wise Platt scaling. Our aim in this study is to begin to develop the tools and conceptual understanding necessary to render VLAs both highly performant and highly trustworthy via reliable uncertainty quantification.

## 参考
- http://arxiv.org/abs/2507.17383v2

