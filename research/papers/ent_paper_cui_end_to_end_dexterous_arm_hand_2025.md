---
$id: ent_paper_cui_end_to_end_dexterous_arm_hand_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'End-to-End Dexterous Arm-Hand VLA Policies via Shared Autonomy: VR Teleoperation Augmented by Autonomous Hand VLA Policy
    for Efficient Data Collection'
  zh: DexGrasp-VLA
  ko: 'End-to-End Dexterous Arm-Hand VLA Policies via Shared Autonomy: VR Teleoperation Augmented by Autonomous Hand VLA Policy
    for Efficient Data Collection'
summary:
  en: 'End-to-End Dexterous Arm-Hand VLA Policies via Shared Autonomy: VR Teleoperation Augmented by Autonomous Hand VLA Policy
    for Efficient Data Collection (DexGrasp-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by ByteDance Seed.'
  zh: 'End-to-End Dexterous Arm-Hand VLA Policies via Shared Autonomy: VR Teleoperation Augmented by Autonomous Hand VLA Policy
    for Efficient Data Collection (DexGrasp-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by ByteDance Seed.'
  ko: 'End-to-End Dexterous Arm-Hand VLA Policies via Shared Autonomy: VR Teleoperation Augmented by Autonomous Hand VLA Policy
    for Efficient Data Collection (DexGrasp-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by ByteDance Seed.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dexgrasp_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.00139v2.
sources:
- id: src_001
  type: paper
  title: 'End-to-End Dexterous Arm-Hand VLA Policies via Shared Autonomy: VR Teleoperation Augmented by Autonomous Hand VLA
    Policy for Efficient Data Collection (arXiv)'
  url: https://arxiv.org/abs/2511.00139
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DexGrasp-VLA source
  url: https://doi.org/10.48550/arXiv.2511.00139
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Achieving human-like dexterous manipulation remains a major challenge for general-purpose robots. While Vision-Language-Action (VLA) models show potential in learning skills from demonstrations, their scalability is limited by scarce high-quality training data. Existing data collection methods face inherent constraints: manual teleoperation overloads human operators, while automated planning often produces unnatural motions. We propose a Shared Autonomy framework that divides control between macro and micro motions. A human operator guides the robot's arm pose through intuitive VR teleoperation, while an autonomous DexGrasp-VLA policy handles fine-grained hand control using real-time tactile and visual feedback. This division significantly reduces cognitive load and enables efficient collection of high-quality coordinated arm-hand demonstrations. Using this data, we train an end-to-end VLA policy enhanced with our novel Arm-Hand Feature Enhancement module, which captures both distinct and shared representations of macro and micro movements for more natural coordination. Our Corrective Teleoperation system enables continuous policy improvement through human-in-the-loop failure recovery. Experiments demonstrate that our framework generates high-quality data with minimal manpower and achieves a 90% success rate across diverse objects, including unseen instances. Comprehensive evaluations validate the system's effectiveness in developing dexterous manipulation capabilities.

## 核心内容
Achieving human-like dexterous manipulation remains a major challenge for general-purpose robots. While Vision-Language-Action (VLA) models show potential in learning skills from demonstrations, their scalability is limited by scarce high-quality training data. Existing data collection methods face inherent constraints: manual teleoperation overloads human operators, while automated planning often produces unnatural motions. We propose a Shared Autonomy framework that divides control between macro and micro motions. A human operator guides the robot's arm pose through intuitive VR teleoperation, while an autonomous DexGrasp-VLA policy handles fine-grained hand control using real-time tactile and visual feedback. This division significantly reduces cognitive load and enables efficient collection of high-quality coordinated arm-hand demonstrations. Using this data, we train an end-to-end VLA policy enhanced with our novel Arm-Hand Feature Enhancement module, which captures both distinct and shared representations of macro and micro movements for more natural coordination. Our Corrective Teleoperation system enables continuous policy improvement through human-in-the-loop failure recovery. Experiments demonstrate that our framework generates high-quality data with minimal manpower and achieves a 90% success rate across diverse objects, including unseen instances. Comprehensive evaluations validate the system's effectiveness in developing dexterous manipulation capabilities.

## 参考
- http://arxiv.org/abs/2511.00139v2

