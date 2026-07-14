---
$id: ent_paper_li_a_self_correcting_vision_langu_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation
  zh: SC-VLA
  ko: A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation
summary:
  en: A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation (SC-VLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Peking University.
  zh: A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation (SC-VLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Peking University.
  ko: A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation (SC-VLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Peking University.
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
- sc_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2405.17418v2.
sources:
- id: src_001
  type: paper
  title: A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation (arXiv)
  url: https://arxiv.org/abs/2405.17418
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Recently, some studies have integrated Multimodal Large Language Models into robotic manipulation, constructing vision-language-action models (VLAs) to interpret multimodal information and predict SE(3) poses. While VLAs have shown promising progress, they may suffer from failures when faced with novel and complex tasks. To emulate human-like reasoning for more robust manipulation, we propose the self-corrected (SC-)VLA framework, which integrates fast system for directly predicting actions and slow system for reflecting on failed actions within a single VLA policy. For the fast system, we incorporate parameter-efficient fine-tuning to equip the model with pose prediction capabilities while preserving the inherent reasoning abilities of MLLMs. For the slow system, we propose a Chain-of-Thought training strategy for failure correction, designed to mimic human reflection after a manipulation failure. Specifically, our model learns to identify the causes of action failures, adaptively seek expert feedback, reflect on the current failure scenario, and iteratively generate corrective actions, step by step. Furthermore, a continuous policy learning method is designed based on successfully corrected samples, enhancing the fast system's adaptability to the current configuration. We compare SC-VLA with the previous SOTA VLA in both simulation and real-world tasks, demonstrating an efficient correction process and improved manipulation accuracy on both seen and unseen tasks.

## 核心内容
Recently, some studies have integrated Multimodal Large Language Models into robotic manipulation, constructing vision-language-action models (VLAs) to interpret multimodal information and predict SE(3) poses. While VLAs have shown promising progress, they may suffer from failures when faced with novel and complex tasks. To emulate human-like reasoning for more robust manipulation, we propose the self-corrected (SC-)VLA framework, which integrates fast system for directly predicting actions and slow system for reflecting on failed actions within a single VLA policy. For the fast system, we incorporate parameter-efficient fine-tuning to equip the model with pose prediction capabilities while preserving the inherent reasoning abilities of MLLMs. For the slow system, we propose a Chain-of-Thought training strategy for failure correction, designed to mimic human reflection after a manipulation failure. Specifically, our model learns to identify the causes of action failures, adaptively seek expert feedback, reflect on the current failure scenario, and iteratively generate corrective actions, step by step. Furthermore, a continuous policy learning method is designed based on successfully corrected samples, enhancing the fast system's adaptability to the current configuration. We compare SC-VLA with the previous SOTA VLA in both simulation and real-world tasks, demonstrating an efficient correction process and improved manipulation accuracy on both seen and unseen tasks.

## 参考
- http://arxiv.org/abs/2405.17418v2

