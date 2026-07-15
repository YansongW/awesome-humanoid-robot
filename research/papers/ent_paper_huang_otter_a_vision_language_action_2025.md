---
$id: ent_paper_huang_otter_a_vision_language_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction'
  zh: OTTER
  ko: 'OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction'
summary:
  en: 'OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction (OTTER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of California, Berkeley, Meta AI, and published at ICML25.'
  zh: 'OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction (OTTER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of California, Berkeley, Meta AI, and published at ICML25.'
  ko: 'OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction (OTTER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of California, Berkeley, Meta AI, and published at ICML25.'
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
- otter
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.03734v4.
sources:
- id: src_001
  type: paper
  title: OTTER source
  url: https://openreview.net/forum?id=UHF0km7R5M
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models aim to predict robotic actions based on visual observations and language instructions. Existing approaches require fine-tuning pre-trained visionlanguage models (VLMs) as visual and language features are independently fed into downstream policies, degrading the pre-trained semantic alignments. We propose OTTER, a novel VLA architecture that leverages these existing alignments through explicit, text-aware visual feature extraction. Instead of processing all visual features, OTTER selectively extracts and passes only task-relevant visual features that are semantically aligned with the language instruction to the policy transformer. This allows OTTER to keep the pre-trained vision-language encoders frozen. Thereby, OTTER preserves and utilizes the rich semantic understanding learned from large-scale pre-training, enabling strong zero-shot generalization capabilities. In simulation and real-world experiments, OTTER significantly outperforms existing VLA models, demonstrating strong zeroshot generalization to novel objects and environments. Video, code, checkpoints, and dataset: https://ottervla.github.io/.

## 核心内容
Vision-Language-Action (VLA) models aim to predict robotic actions based on visual observations and language instructions. Existing approaches require fine-tuning pre-trained visionlanguage models (VLMs) as visual and language features are independently fed into downstream policies, degrading the pre-trained semantic alignments. We propose OTTER, a novel VLA architecture that leverages these existing alignments through explicit, text-aware visual feature extraction. Instead of processing all visual features, OTTER selectively extracts and passes only task-relevant visual features that are semantically aligned with the language instruction to the policy transformer. This allows OTTER to keep the pre-trained vision-language encoders frozen. Thereby, OTTER preserves and utilizes the rich semantic understanding learned from large-scale pre-training, enabling strong zero-shot generalization capabilities. In simulation and real-world experiments, OTTER significantly outperforms existing VLA models, demonstrating strong zeroshot generalization to novel objects and environments. Video, code, checkpoints, and dataset: https://ottervla.github.io/.

## 参考
- http://arxiv.org/abs/2503.03734v4

