---
$id: ent_paper_wu_do_what_you_say_steering_visio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification'
  zh: SEAL
  ko: 'Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification'
summary:
  en: 'Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification (SEAL),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by University of Utah, NVIDIA.'
  zh: 'Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification (SEAL),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by University of Utah, NVIDIA.'
  ko: 'Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification (SEAL),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by University of Utah, NVIDIA.'
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
- seal
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.16281v2.
sources:
- id: src_001
  type: paper
  title: 'Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification (arXiv)'
  url: https://arxiv.org/abs/2510.16281
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SEAL source
  url: https://doi.org/10.48550/arXiv.2510.16281
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Reasoning Vision Language Action (VLA) models improve robotic instruction-following by generating step-by-step textual plans before low-level actions, an approach inspired by Chain-of-Thought (CoT) reasoning in language models. Yet even with a correct textual plan, the generated actions can still miss the intended outcomes in the plan, especially in out-of-distribution (OOD) scenarios. We formalize this phenomenon as a lack of embodied CoT faithfulness, and introduce a training-free, runtime policy steering method for reasoning-action alignment. Given a reasoning VLA's intermediate textual plan, our framework samples multiple candidate action sequences from the same model, predicts their outcomes via simulation, and uses a pre-trained Vision-Language Model (VLM) to select the sequence whose outcome best aligns with the VLA's own textual plan. Only executing action sequences that align with the textual reasoning turns our base VLA's natural action diversity from a source of error into a strength, boosting robustness to semantic and visual OOD perturbations and enabling novel behavior composition without costly re-training. We also contribute a reasoning-annotated extension of LIBERO-100, environment variations tailored for OOD evaluation, and demonstrate up to 15% performance gain over prior work on behavior composition tasks and scales with compute and data diversity. Project Website at: https://yilin-wu98.github.io/steering-reasoning-vla/

## 核心内容
Reasoning Vision Language Action (VLA) models improve robotic instruction-following by generating step-by-step textual plans before low-level actions, an approach inspired by Chain-of-Thought (CoT) reasoning in language models. Yet even with a correct textual plan, the generated actions can still miss the intended outcomes in the plan, especially in out-of-distribution (OOD) scenarios. We formalize this phenomenon as a lack of embodied CoT faithfulness, and introduce a training-free, runtime policy steering method for reasoning-action alignment. Given a reasoning VLA's intermediate textual plan, our framework samples multiple candidate action sequences from the same model, predicts their outcomes via simulation, and uses a pre-trained Vision-Language Model (VLM) to select the sequence whose outcome best aligns with the VLA's own textual plan. Only executing action sequences that align with the textual reasoning turns our base VLA's natural action diversity from a source of error into a strength, boosting robustness to semantic and visual OOD perturbations and enabling novel behavior composition without costly re-training. We also contribute a reasoning-annotated extension of LIBERO-100, environment variations tailored for OOD evaluation, and demonstrate up to 15% performance gain over prior work on behavior composition tasks and scales with compute and data diversity. Project Website at: https://yilin-wu98.github.io/steering-reasoning-vla/

## 参考
- http://arxiv.org/abs/2510.16281v2

