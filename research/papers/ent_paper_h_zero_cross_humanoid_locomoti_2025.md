---
$id: ent_paper_h_zero_cross_humanoid_locomoti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'H-Zero: Cross-Humanoid Locomotion Pretraining Enables Few-shot Novel Embodiment Transfer'
  zh: 'H-Zero: Cross-Humanoid Locomotion Pretraining Enables Few-shot Novel Embodiment Transfer'
  ko: 'H-Zero: Cross-Humanoid Locomotion Pretraining Enables Few-shot Novel Embodiment Transfer'
summary:
  en: 'H-Zero: Cross-Humanoid Locomotion Pretraining Enables Few-shot Novel Embodiment Transfer is a 2025 work on locomotion
    for humanoid robots.'
  zh: 'H-Zero: Cross-Humanoid Locomotion Pretraining Enables Few-shot Novel Embodiment Transfer is a 2025 work on locomotion
    for humanoid robots.'
  ko: 'H-Zero: Cross-Humanoid Locomotion Pretraining Enables Few-shot Novel Embodiment Transfer is a 2025 work on locomotion
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- h_zero
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.00971v1.
sources:
- id: src_001
  type: paper
  title: 'H-Zero: Cross-Humanoid Locomotion Pretraining Enables Few-shot Novel Embodiment Transfer (arXiv)'
  url: https://arxiv.org/abs/2512.00971
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The rapid advancement of humanoid robotics has intensified the need for robust and adaptable controllers to enable stable and efficient locomotion across diverse platforms. However, developing such controllers remains a significant challenge because existing solutions are tailored to specific robot designs, requiring extensive tuning of reward functions, physical parameters, and training hyperparameters for each embodiment. To address this challenge, we introduce H-Zero, a cross-humanoid locomotion pretraining pipeline that learns a generalizable humanoid base policy. We show that pretraining on a limited set of embodiments enables zero-shot and few-shot transfer to novel humanoid robots with minimal fine-tuning. Evaluations show that the pretrained policy maintains up to 81% of the full episode duration on unseen robots in simulation while enabling few-shot transfer to unseen humanoids and upright quadrupeds within 30 minutes of fine-tuning.

## 核心内容
The rapid advancement of humanoid robotics has intensified the need for robust and adaptable controllers to enable stable and efficient locomotion across diverse platforms. However, developing such controllers remains a significant challenge because existing solutions are tailored to specific robot designs, requiring extensive tuning of reward functions, physical parameters, and training hyperparameters for each embodiment. To address this challenge, we introduce H-Zero, a cross-humanoid locomotion pretraining pipeline that learns a generalizable humanoid base policy. We show that pretraining on a limited set of embodiments enables zero-shot and few-shot transfer to novel humanoid robots with minimal fine-tuning. Evaluations show that the pretrained policy maintains up to 81% of the full episode duration on unseen robots in simulation while enabling few-shot transfer to unseen humanoids and upright quadrupeds within 30 minutes of fine-tuning.

## 参考
- http://arxiv.org/abs/2512.00971v1

