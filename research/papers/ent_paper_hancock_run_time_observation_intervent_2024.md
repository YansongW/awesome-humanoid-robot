---
$id: ent_paper_hancock_run_time_observation_intervent_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Run-time Observation Interventions Make Vision-Language-Action Models More Visually Robust
  zh: BYOVLA
  ko: Run-time Observation Interventions Make Vision-Language-Action Models More Visually Robust
summary:
  en: Run-time Observation Interventions Make Vision-Language-Action Models More Visually Robust (BYOVLA), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Princeton University, and published at ICRA 2024.
  zh: Run-time Observation Interventions Make Vision-Language-Action Models More Visually Robust (BYOVLA), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Princeton University, and published at ICRA 2024.
  ko: Run-time Observation Interventions Make Vision-Language-Action Models More Visually Robust (BYOVLA), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Princeton University, and published at ICRA 2024.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- byovla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.01971v1.
sources:
- id: src_001
  type: website
  title: BYOVLA source
  url: https://doi.org/10.1109/ICRA55743.2025.11128017
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models trained on large-scale internet data and robot demonstrations have the potential to serve as generalist robot policies. However, despite their large-scale training, VLAs are often brittle to task-irrelevant visual details such as distractor objects or background colors. We introduce Bring Your Own VLA (BYOVLA): a run-time intervention scheme that (1) dynamically identifies regions of the input image that the model is sensitive to, and (2) minimally alters task-irrelevant regions to reduce the model's sensitivity using automated image editing tools. Our approach is compatible with any off the shelf VLA without model fine-tuning or access to the model's weights. Hardware experiments on language-instructed manipulation tasks demonstrate that BYOVLA enables state-of-the-art VLA models to nearly retain their nominal performance in the presence of distractor objects and backgrounds, which otherwise degrade task success rates by up to 40%. Website with additional information, videos, and code: https://aasherh.github.io/byovla/ .

## 核心内容
Vision-language-action (VLA) models trained on large-scale internet data and robot demonstrations have the potential to serve as generalist robot policies. However, despite their large-scale training, VLAs are often brittle to task-irrelevant visual details such as distractor objects or background colors. We introduce Bring Your Own VLA (BYOVLA): a run-time intervention scheme that (1) dynamically identifies regions of the input image that the model is sensitive to, and (2) minimally alters task-irrelevant regions to reduce the model's sensitivity using automated image editing tools. Our approach is compatible with any off the shelf VLA without model fine-tuning or access to the model's weights. Hardware experiments on language-instructed manipulation tasks demonstrate that BYOVLA enables state-of-the-art VLA models to nearly retain their nominal performance in the presence of distractor objects and backgrounds, which otherwise degrade task success rates by up to 40%. Website with additional information, videos, and code: https://aasherh.github.io/byovla/ .

## 参考
- http://arxiv.org/abs/2410.01971v1

