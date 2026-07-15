---
$id: ent_paper_zhao_vlas_vision_language_action_mo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLAS: Vision-Language-Action Model With Speech Instructions For Customized Robot Manipulation'
  zh: VLAS
  ko: 'VLAS: Vision-Language-Action Model With Speech Instructions For Customized Robot Manipulation'
summary:
  en: 'VLAS: Vision-Language-Action Model With Speech Instructions For Customized Robot Manipulation (VLAS), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Xi''an Jiaotong University, and published at ICLR25.'
  zh: 'VLAS: Vision-Language-Action Model With Speech Instructions For Customized Robot Manipulation (VLAS), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Xi''an Jiaotong University, and published at ICLR25.'
  ko: 'VLAS: Vision-Language-Action Model With Speech Instructions For Customized Robot Manipulation (VLAS), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Xi''an Jiaotong University, and published at ICLR25.'
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
- vlas
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.13508v2.
sources:
- id: src_001
  type: paper
  title: VLAS source
  url: https://openreview.net/forum?id=K4FAFNRpko
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action models (VLAs) have become increasingly popular in robot manipulation for their end-to-end design and remarkable performance. However, existing VLAs rely heavily on vision-language models (VLMs) that only support text-based instructions, neglecting the more natural speech modality for human-robot interaction. Traditional speech integration methods usually involves a separate speech recognition system, which complicates the model and introduces error propagation. Moreover, the transcription procedure would lose non-semantic information in the raw speech, such as voiceprint, which may be crucial for robots to successfully complete customized tasks. To overcome above challenges, we propose VLAS, a novel end-to-end VLA that integrates speech recognition directly into the robot policy model. VLAS allows the robot to understand spoken commands through inner speech-text alignment and produces corresponding actions to fulfill the task. We also present two new datasets, SQA and CSI, to support a three-stage tuning process for speech instructions, which empowers VLAS with the ability of multimodal interaction across text, image, speech, and robot actions. Taking a step further, a voice retrieval-augmented generation (RAG) paradigm is designed to enable our model to effectively handle tasks that require individual-specific knowledge. Our extensive experiments show that VLAS can effectively accomplish robot manipulation tasks with diverse speech commands, offering a seamless and customized interaction experience.

## 核心内容
Vision-language-action models (VLAs) have become increasingly popular in robot manipulation for their end-to-end design and remarkable performance. However, existing VLAs rely heavily on vision-language models (VLMs) that only support text-based instructions, neglecting the more natural speech modality for human-robot interaction. Traditional speech integration methods usually involves a separate speech recognition system, which complicates the model and introduces error propagation. Moreover, the transcription procedure would lose non-semantic information in the raw speech, such as voiceprint, which may be crucial for robots to successfully complete customized tasks. To overcome above challenges, we propose VLAS, a novel end-to-end VLA that integrates speech recognition directly into the robot policy model. VLAS allows the robot to understand spoken commands through inner speech-text alignment and produces corresponding actions to fulfill the task. We also present two new datasets, SQA and CSI, to support a three-stage tuning process for speech instructions, which empowers VLAS with the ability of multimodal interaction across text, image, speech, and robot actions. Taking a step further, a voice retrieval-augmented generation (RAG) paradigm is designed to enable our model to effectively handle tasks that require individual-specific knowledge. Our extensive experiments show that VLAS can effectively accomplish robot manipulation tasks with diverse speech commands, offering a seamless and customized interaction experience.

## 参考
- http://arxiv.org/abs/2502.13508v2

