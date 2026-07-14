---
$id: ent_paper_huang_tactile_vla_unlocking_vision_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Tactile-VLA: Unlocking Vision-Language-Action Model''s Physical Knowledge for Tactile Generalization'
  zh: Tactile-VLA
  ko: 'Tactile-VLA: Unlocking Vision-Language-Action Model''s Physical Knowledge for Tactile Generalization'
summary:
  en: 'Tactile-VLA: Unlocking Vision-Language-Action Model''s Physical Knowledge for Tactile Generalization (Tactile-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, UESTC, Shanghai
    Jiao Tong University.'
  zh: 'Tactile-VLA: Unlocking Vision-Language-Action Model''s Physical Knowledge for Tactile Generalization (Tactile-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, UESTC, Shanghai
    Jiao Tong University.'
  ko: 'Tactile-VLA: Unlocking Vision-Language-Action Model''s Physical Knowledge for Tactile Generalization (Tactile-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, UESTC, Shanghai
    Jiao Tong University.'
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
- tactile_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.09160v1.
sources:
- id: src_001
  type: paper
  title: 'Tactile-VLA: Unlocking Vision-Language-Action Model''s Physical Knowledge for Tactile Generalization (arXiv)'
  url: https://arxiv.org/abs/2507.09160
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Tactile-VLA source
  url: https://doi.org/10.48550/arXiv.2507.09160
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have shown remarkable achievements, driven by the rich implicit knowledge of their vision-language components. However, achieving generalist robotic agents demands precise grounding into physical interactions, especially in contact-rich scenarios where fine-grained force control is essential. We advance VLAs' implicit knowledge beyond identifying what to do, towards guiding how to physically interact with real world. This paper introduces Tactile-VLA, a novel framework that deeply fuses vision, language, action, and tactile sensing. This framework incorporates a hybrid position-force controller to translate the model's intentions into precise physical actions and a reasoning module that allows the robot to adapt its strategy based on tactile feedback. Experiments demonstrate Tactile-VLA's effectiveness and generalizability in three key aspects: (1) enabling tactile-aware instruction following, (2) utilizing tactile-relevant commonsense, and (3) facilitating adaptive tactile-involved reasoning. A key finding is that the VLM's prior knowledge already contains semantic understanding of physical interaction; by connecting it to the robot's tactile sensors with only a few demonstrations, we can activate this prior knowledge to achieve zero-shot generalization in contact-rich tasks.

## 核心内容
Vision-Language-Action (VLA) models have shown remarkable achievements, driven by the rich implicit knowledge of their vision-language components. However, achieving generalist robotic agents demands precise grounding into physical interactions, especially in contact-rich scenarios where fine-grained force control is essential. We advance VLAs' implicit knowledge beyond identifying what to do, towards guiding how to physically interact with real world. This paper introduces Tactile-VLA, a novel framework that deeply fuses vision, language, action, and tactile sensing. This framework incorporates a hybrid position-force controller to translate the model's intentions into precise physical actions and a reasoning module that allows the robot to adapt its strategy based on tactile feedback. Experiments demonstrate Tactile-VLA's effectiveness and generalizability in three key aspects: (1) enabling tactile-aware instruction following, (2) utilizing tactile-relevant commonsense, and (3) facilitating adaptive tactile-involved reasoning. A key finding is that the VLM's prior knowledge already contains semantic understanding of physical interaction; by connecting it to the robot's tactile sensors with only a few demonstrations, we can activate this prior knowledge to achieve zero-shot generalization in contact-rich tasks.

## 参考
- http://arxiv.org/abs/2507.09160v1

