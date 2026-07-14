---
$id: ent_paper_tact_humanoid_whole_body_conta_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality'
  zh: 'TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality'
  ko: 'TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality'
summary:
  en: 'TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  zh: 'TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  ko: 'TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- loco_manipulation
- tact
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.15146v1.
sources:
- id: src_001
  type: paper
  title: 'TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality (arXiv)'
  url: https://arxiv.org/abs/2506.15146
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Manipulation with whole-body contact by humanoid robots offers distinct advantages, including enhanced stability and reduced load. On the other hand, we need to address challenges such as the increased computational cost of motion generation and the difficulty of measuring broad-area contact. We therefore have developed a humanoid control system that allows a humanoid robot equipped with tactile sensors on its upper body to learn a policy for whole-body manipulation through imitation learning based on human teleoperation data. This policy, named tactile-modality extended ACT (TACT), has a feature to take multiple sensor modalities as input, including joint position, vision, and tactile measurements. Furthermore, by integrating this policy with retargeting and locomotion control based on a biped model, we demonstrate that the life-size humanoid robot RHP7 Kaleido is capable of achieving whole-body contact manipulation while maintaining balance and walking. Through detailed experimental verification, we show that inputting both vision and tactile modalities into the policy contributes to improving the robustness of manipulation involving broad and delicate contact.

## 核心内容
Manipulation with whole-body contact by humanoid robots offers distinct advantages, including enhanced stability and reduced load. On the other hand, we need to address challenges such as the increased computational cost of motion generation and the difficulty of measuring broad-area contact. We therefore have developed a humanoid control system that allows a humanoid robot equipped with tactile sensors on its upper body to learn a policy for whole-body manipulation through imitation learning based on human teleoperation data. This policy, named tactile-modality extended ACT (TACT), has a feature to take multiple sensor modalities as input, including joint position, vision, and tactile measurements. Furthermore, by integrating this policy with retargeting and locomotion control based on a biped model, we demonstrate that the life-size humanoid robot RHP7 Kaleido is capable of achieving whole-body contact manipulation while maintaining balance and walking. Through detailed experimental verification, we show that inputting both vision and tactile modalities into the policy contributes to improving the robustness of manipulation involving broad and delicate contact.

## 参考
- http://arxiv.org/abs/2506.15146v1

