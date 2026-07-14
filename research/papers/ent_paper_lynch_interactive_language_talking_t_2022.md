---
$id: ent_paper_lynch_interactive_language_talking_t_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Interactive Language: Talking to Robots in Real Time'
  zh: Interactive Language
  ko: 'Interactive Language: Talking to Robots in Real Time'
summary:
  en: 'Interactive Language: Talking to Robots in Real Time (Interactive Language), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by Robotics at Google.'
  zh: 'Interactive Language: Talking to Robots in Real Time (Interactive Language), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by Robotics at Google.'
  ko: 'Interactive Language: Talking to Robots in Real Time (Interactive Language), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by Robotics at Google.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- interactive_language
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2210.06407v1.
sources:
- id: src_001
  type: paper
  title: 'Interactive Language: Talking to Robots in Real Time (arXiv)'
  url: https://arxiv.org/abs/2210.06407
  date: '2022'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Interactive Language source
  url: https://doi.org/10.48550/arXiv.2210.06407
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
We present a framework for building interactive, real-time, natural language-instructable robots in the real world, and we open source related assets (dataset, environment, benchmark, and policies). Trained with behavioral cloning on a dataset of hundreds of thousands of language-annotated trajectories, a produced policy can proficiently execute an order of magnitude more commands than previous works: specifically we estimate a 93.5% success rate on a set of 87,000 unique natural language strings specifying raw end-to-end visuo-linguo-motor skills in the real world. We find that the same policy is capable of being guided by a human via real-time language to address a wide range of precise long-horizon rearrangement goals, e.g. "make a smiley face out of blocks". The dataset we release comprises nearly 600,000 language-labeled trajectories, an order of magnitude larger than prior available datasets. We hope the demonstrated results and associated assets enable further advancement of helpful, capable, natural-language-interactable robots. See videos at https://interactive-language.github.io.

## 核心内容
We present a framework for building interactive, real-time, natural language-instructable robots in the real world, and we open source related assets (dataset, environment, benchmark, and policies). Trained with behavioral cloning on a dataset of hundreds of thousands of language-annotated trajectories, a produced policy can proficiently execute an order of magnitude more commands than previous works: specifically we estimate a 93.5% success rate on a set of 87,000 unique natural language strings specifying raw end-to-end visuo-linguo-motor skills in the real world. We find that the same policy is capable of being guided by a human via real-time language to address a wide range of precise long-horizon rearrangement goals, e.g. "make a smiley face out of blocks". The dataset we release comprises nearly 600,000 language-labeled trajectories, an order of magnitude larger than prior available datasets. We hope the demonstrated results and associated assets enable further advancement of helpful, capable, natural-language-interactable robots. See videos at https://interactive-language.github.io.

## 参考
- http://arxiv.org/abs/2210.06407v1

