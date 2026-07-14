---
$id: ent_paper_mitra_mechanistic_finetuning_of_visi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Mechanistic Finetuning of Vision-Language-Action Models via Few-Shot Demonstrations
  zh: Mechanistic Finetuning of Vision-Language-Action Models via Few-Shot Demonstrations
  ko: Mechanistic Finetuning of Vision-Language-Action Models via Few-Shot Demonstrations
summary:
  en: Mechanistic Finetuning of Vision-Language-Action Models via Few-Shot Demonstrations (Mechanistic Finetuning of Vision-Language-Action
    Models via Few-Shot Demonstrations), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by Carnegie Mellon University, University of Southern California, University of California, Berkeley, MIT-IBM Watson AI
    Lab.
  zh: Mechanistic Finetuning of Vision-Language-Action Models via Few-Shot Demonstrations (Mechanistic Finetuning of Vision-Language-Action
    Models via Few-Shot Demonstrations), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by Carnegie Mellon University, University of Southern California, University of California, Berkeley, MIT-IBM Watson AI
    Lab.
  ko: Mechanistic Finetuning of Vision-Language-Action Models via Few-Shot Demonstrations (Mechanistic Finetuning of Vision-Language-Action
    Models via Few-Shot Demonstrations), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by Carnegie Mellon University, University of Southern California, University of California, Berkeley, MIT-IBM Watson AI
    Lab.
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
- mechanistic_finetuning_of_visi
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.22697v1.
sources:
- id: src_001
  type: paper
  title: Mechanistic Finetuning of Vision-Language-Action Models via Few-Shot Demonstrations (arXiv)
  url: https://arxiv.org/abs/2511.22697
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Mechanistic Finetuning of Vision-Language-Action Models via Few-Shot Demonstrations source
  url: https://doi.org/10.48550/arXiv.2511.22697
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language Action (VLAs) models promise to extend the remarkable success of vision-language models (VLMs) to robotics. Yet, unlike VLMs in the vision-language domain, VLAs for robotics require finetuning to contend with varying physical factors like robot embodiment, environment characteristics, and spatial relationships of each task. Existing fine-tuning methods lack specificity, adapting the same set of parameters regardless of a task's visual, linguistic, and physical characteristics. Inspired by functional specificity in neuroscience, we hypothesize that it is more effective to finetune sparse model representations specific to a given task. In this work, we introduce Robotic Steering, a finetuning approach grounded in mechanistic interpretability that leverages few-shot demonstrations to identify and selectively finetune task-specific attention heads aligned with the physical, visual, and linguistic requirements of robotic tasks. Through comprehensive on-robot evaluations with a Franka Emika robot arm, we demonstrate that Robotic Steering outperforms LoRA while achieving superior robustness under task variation, reduced computational cost, and enhanced interpretability for adapting VLAs to diverse robotic tasks.

## 核心内容
Vision-Language Action (VLAs) models promise to extend the remarkable success of vision-language models (VLMs) to robotics. Yet, unlike VLMs in the vision-language domain, VLAs for robotics require finetuning to contend with varying physical factors like robot embodiment, environment characteristics, and spatial relationships of each task. Existing fine-tuning methods lack specificity, adapting the same set of parameters regardless of a task's visual, linguistic, and physical characteristics. Inspired by functional specificity in neuroscience, we hypothesize that it is more effective to finetune sparse model representations specific to a given task. In this work, we introduce Robotic Steering, a finetuning approach grounded in mechanistic interpretability that leverages few-shot demonstrations to identify and selectively finetune task-specific attention heads aligned with the physical, visual, and linguistic requirements of robotic tasks. Through comprehensive on-robot evaluations with a Franka Emika robot arm, we demonstrate that Robotic Steering outperforms LoRA while achieving superior robustness under task variation, reduced computational cost, and enhanced interpretability for adapting VLAs to diverse robotic tasks.

## 参考
- http://arxiv.org/abs/2511.22697v1

