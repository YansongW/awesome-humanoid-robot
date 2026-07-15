---
$id: ent_paper_li_llara_supercharging_robot_lear_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LLaRA: Supercharging Robot Learning Data for Vision-Language Policy'
  zh: LLaRA
  ko: 'LLaRA: Supercharging Robot Learning Data for Vision-Language Policy'
summary:
  en: 'LLaRA: Supercharging Robot Learning Data for Vision-Language Policy (LLaRA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Stony Brook University, University of Wisconsin-Madison, and published at
    ICLR 2024.'
  zh: 'LLaRA: Supercharging Robot Learning Data for Vision-Language Policy (LLaRA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Stony Brook University, University of Wisconsin-Madison, and published at
    ICLR 2024.'
  ko: 'LLaRA: Supercharging Robot Learning Data for Vision-Language Policy (LLaRA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Stony Brook University, University of Wisconsin-Madison, and published at
    ICLR 2024.'
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
- llara
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.20095v3.
sources:
- id: src_001
  type: paper
  title: LLaRA source
  url: https://openreview.net/forum?id=iVxxgZlXh6
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Vision Language Models (VLMs) have recently been leveraged to generate robotic actions, forming Vision-Language-Action (VLA) models. However, directly adapting a pretrained VLM for robotic control remains challenging, particularly when constrained by a limited number of robot demonstrations. In this work, we introduce LLaRA: Large Language and Robotics Assistant, a framework that formulates robot action policy as visuo-textual conversations and enables an efficient transfer of a pretrained VLM into a powerful VLA, motivated by the success of visual instruction tuning in Computer Vision. First, we present an automated pipeline to generate conversation-style instruction tuning data for robots from existing behavior cloning datasets, aligning robotic actions with image pixel coordinates. Further, we enhance this dataset in a self-supervised manner by defining six auxiliary tasks, without requiring any additional action annotations. We show that a VLM finetuned with a limited amount of such datasets can produce meaningful action decisions for robotic control. Through experiments across multiple simulated and real-world tasks, we demonstrate that LLaRA achieves state-of-the-art performance while preserving the generalization capabilities of large language models. The code, datasets, and pretrained models are available at https://github.com/LostXine/LLaRA.

## 核心内容
Vision Language Models (VLMs) have recently been leveraged to generate robotic actions, forming Vision-Language-Action (VLA) models. However, directly adapting a pretrained VLM for robotic control remains challenging, particularly when constrained by a limited number of robot demonstrations. In this work, we introduce LLaRA: Large Language and Robotics Assistant, a framework that formulates robot action policy as visuo-textual conversations and enables an efficient transfer of a pretrained VLM into a powerful VLA, motivated by the success of visual instruction tuning in Computer Vision. First, we present an automated pipeline to generate conversation-style instruction tuning data for robots from existing behavior cloning datasets, aligning robotic actions with image pixel coordinates. Further, we enhance this dataset in a self-supervised manner by defining six auxiliary tasks, without requiring any additional action annotations. We show that a VLM finetuned with a limited amount of such datasets can produce meaningful action decisions for robotic control. Through experiments across multiple simulated and real-world tasks, we demonstrate that LLaRA achieves state-of-the-art performance while preserving the generalization capabilities of large language models. The code, datasets, and pretrained models are available at https://github.com/LostXine/LLaRA.

## 参考
- http://arxiv.org/abs/2406.20095v3

