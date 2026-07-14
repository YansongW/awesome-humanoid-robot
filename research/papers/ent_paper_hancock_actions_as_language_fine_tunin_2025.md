---
$id: ent_paper_hancock_actions_as_language_fine_tunin_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting'
  zh: VLM2VLA
  ko: 'Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting'
summary:
  en: 'Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting (VLM2VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Princeton University.'
  zh: 'Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting (VLM2VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Princeton University.'
  ko: 'Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting (VLM2VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Princeton University.'
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
- vision_language_action
- vla
- vlm2vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.22195v1.
sources:
- id: src_001
  type: paper
  title: 'Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting (arXiv)'
  url: https://arxiv.org/abs/2509.22195
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLM2VLA source
  url: https://doi.org/10.48550/arXiv.2509.22195
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Fine-tuning vision-language models (VLMs) on robot teleoperation data to create vision-language-action (VLA) models is a promising paradigm for training generalist policies, but it suffers from a fundamental tradeoff: learning to produce actions often diminishes the VLM's foundational reasoning and multimodal understanding, hindering generalization to novel scenarios, instruction following, and semantic understanding. We argue that this catastrophic forgetting is due to a distribution mismatch between the VLM's internet-scale pretraining corpus and the robotics fine-tuning data. Inspired by this observation, we introduce VLM2VLA: a VLA training paradigm that first resolves this mismatch at the data level by representing low-level actions with natural language. This alignment makes it possible to train VLAs solely with Low-Rank Adaptation (LoRA), thereby minimally modifying the VLM backbone and averting catastrophic forgetting. As a result, the VLM can be fine-tuned on robot teleoperation data without fundamentally altering the underlying architecture and without expensive co-training on internet-scale VLM datasets. Through extensive Visual Question Answering (VQA) studies and over 800 real-world robotics experiments, we demonstrate that VLM2VLA preserves the VLM's core capabilities, enabling zero-shot generalization to novel tasks that require open-world semantic reasoning and multilingual instruction following.

## 核心内容
Fine-tuning vision-language models (VLMs) on robot teleoperation data to create vision-language-action (VLA) models is a promising paradigm for training generalist policies, but it suffers from a fundamental tradeoff: learning to produce actions often diminishes the VLM's foundational reasoning and multimodal understanding, hindering generalization to novel scenarios, instruction following, and semantic understanding. We argue that this catastrophic forgetting is due to a distribution mismatch between the VLM's internet-scale pretraining corpus and the robotics fine-tuning data. Inspired by this observation, we introduce VLM2VLA: a VLA training paradigm that first resolves this mismatch at the data level by representing low-level actions with natural language. This alignment makes it possible to train VLAs solely with Low-Rank Adaptation (LoRA), thereby minimally modifying the VLM backbone and averting catastrophic forgetting. As a result, the VLM can be fine-tuned on robot teleoperation data without fundamentally altering the underlying architecture and without expensive co-training on internet-scale VLM datasets. Through extensive Visual Question Answering (VQA) studies and over 800 real-world robotics experiments, we demonstrate that VLM2VLA preserves the VLM's core capabilities, enabling zero-shot generalization to novel tasks that require open-world semantic reasoning and multilingual instruction following.

## 参考
- http://arxiv.org/abs/2509.22195v1

