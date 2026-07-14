---
$id: ent_paper_yang_instructvla_vision_language_ac_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation'
  zh: InstructVLA
  ko: 'InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation'
summary:
  en: 'InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation (InstructVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by University of Science and Technology of China,
    Zhejiang University, Shanghai Artificial Intelligence Laboratory.'
  zh: 'InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation (InstructVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by University of Science and Technology of China,
    Zhejiang University, Shanghai Artificial Intelligence Laboratory.'
  ko: 'InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation (InstructVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by University of Science and Technology of China,
    Zhejiang University, Shanghai Artificial Intelligence Laboratory.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- instructvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.17520v2.
sources:
- id: src_001
  type: paper
  title: 'InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation (arXiv)'
  url: https://arxiv.org/abs/2507.17520
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: InstructVLA source
  url: https://doi.org/10.48550/arXiv.2507.17520
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
To operate effectively in the real world, robots should integrate multimodal reasoning with precise action generation. However, existing vision-language-action (VLA) models often sacrifice one for the other, narrow their abilities to task-specific manipulation data, and suffer catastrophic forgetting of pre-trained vision-language capabilities. To bridge this gap, we introduce InstructVLA, an end-to-end VLA model that preserves the flexible reasoning of large vision-language models (VLMs) while delivering leading manipulation performance with the help of embodied reasoning. InstructVLA introduces a novel training paradigm, Vision-Language-Action Instruction Tuning (VLA-IT), which employs multimodal training with mixture-of-experts adaptation to jointly optimize embodied reasoning and action generation on both standard VLM corpora and a curated 650K-sample VLA-IT dataset. On in-domain SimplerEnv tasks, InstructVLA achieves 33% improvement over SpatialVLA. To evaluate generalization, we introduce SimplerEnv-Instruct, an 80-task benchmark requiring closed-loop control and high-level instruction understanding, where it outperforms a fine-tuned OpenVLA by 96% and an action expert aided by GPT-4o by 29%. Additionally, InstructVLA surpasses baseline VLMs on multimodal tasks and exhibits inference-time scaling by leveraging textual reasoning to boost manipulation performance in both simulated and real-world settings. These results demonstrate InstructVLA's potential for bridging intuitive and steerable human-robot interaction with efficient policy learning.

## 核心内容
To operate effectively in the real world, robots should integrate multimodal reasoning with precise action generation. However, existing vision-language-action (VLA) models often sacrifice one for the other, narrow their abilities to task-specific manipulation data, and suffer catastrophic forgetting of pre-trained vision-language capabilities. To bridge this gap, we introduce InstructVLA, an end-to-end VLA model that preserves the flexible reasoning of large vision-language models (VLMs) while delivering leading manipulation performance with the help of embodied reasoning. InstructVLA introduces a novel training paradigm, Vision-Language-Action Instruction Tuning (VLA-IT), which employs multimodal training with mixture-of-experts adaptation to jointly optimize embodied reasoning and action generation on both standard VLM corpora and a curated 650K-sample VLA-IT dataset. On in-domain SimplerEnv tasks, InstructVLA achieves 33% improvement over SpatialVLA. To evaluate generalization, we introduce SimplerEnv-Instruct, an 80-task benchmark requiring closed-loop control and high-level instruction understanding, where it outperforms a fine-tuned OpenVLA by 96% and an action expert aided by GPT-4o by 29%. Additionally, InstructVLA surpasses baseline VLMs on multimodal tasks and exhibits inference-time scaling by leveraging textual reasoning to boost manipulation performance in both simulated and real-world settings. These results demonstrate InstructVLA's potential for bridging intuitive and steerable human-robot interaction with efficient policy learning.

## 参考
- http://arxiv.org/abs/2507.17520v2

