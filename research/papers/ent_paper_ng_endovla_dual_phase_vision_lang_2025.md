---
$id: ent_paper_ng_endovla_dual_phase_vision_lang_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EndoVLA: Dual-Phase Vision-Language-Action Model for Autonomous Tracking in Endoscopy'
  zh: EndoVLA
  ko: 'EndoVLA: Dual-Phase Vision-Language-Action Model for Autonomous Tracking in Endoscopy'
summary:
  en: 'EndoVLA: Dual-Phase Vision-Language-Action Model for Autonomous Tracking in Endoscopy (EndoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by The Chinese University of Hong Kong, Technical University of Munich, and
    published at CoRL25.'
  zh: 'EndoVLA: Dual-Phase Vision-Language-Action Model for Autonomous Tracking in Endoscopy (EndoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by The Chinese University of Hong Kong, Technical University of Munich, and
    published at CoRL25.'
  ko: 'EndoVLA: Dual-Phase Vision-Language-Action Model for Autonomous Tracking in Endoscopy (EndoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by The Chinese University of Hong Kong, Technical University of Munich, and
    published at CoRL25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- endovla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.15206v1.
sources:
- id: src_001
  type: paper
  title: 'EndoVLA: Dual-Phase Vision-Language-Action Model for Autonomous Tracking in Endoscopy (arXiv)'
  url: https://arxiv.org/abs/2505.15206
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: EndoVLA source
  url: https://doi.org/10.48550/arXiv.2505.15206
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In endoscopic procedures, autonomous tracking of abnormal regions and following circumferential cutting markers can significantly reduce the cognitive burden on endoscopists. However, conventional model-based pipelines are fragile for each component (e.g., detection, motion planning) requires manual tuning and struggles to incorporate high-level endoscopic intent, leading to poor generalization across diverse scenes. Vision-Language-Action (VLA) models, which integrate visual perception, language grounding, and motion planning within an end-to-end framework, offer a promising alternative by semantically adapting to surgeon prompts without manual recalibration. Despite their potential, applying VLA models to robotic endoscopy presents unique challenges due to the complex and dynamic anatomical environments of the gastrointestinal (GI) tract. To address this, we introduce EndoVLA, designed specifically for continuum robots in GI interventions. Given endoscopic images and surgeon-issued tracking prompts, EndoVLA performs three core tasks: (1) polyp tracking, (2) delineation and following of abnormal mucosal regions, and (3) adherence to circular markers during circumferential cutting. To tackle data scarcity and domain shifts, we propose a dual-phase strategy comprising supervised fine-tuning on our EndoVLA-Motion dataset and reinforcement fine-tuning with task-aware rewards. Our approach significantly improves tracking performance in endoscopy and enables zero-shot generalization in diverse scenes and complex sequential tasks.

## 核心内容
In endoscopic procedures, autonomous tracking of abnormal regions and following circumferential cutting markers can significantly reduce the cognitive burden on endoscopists. However, conventional model-based pipelines are fragile for each component (e.g., detection, motion planning) requires manual tuning and struggles to incorporate high-level endoscopic intent, leading to poor generalization across diverse scenes. Vision-Language-Action (VLA) models, which integrate visual perception, language grounding, and motion planning within an end-to-end framework, offer a promising alternative by semantically adapting to surgeon prompts without manual recalibration. Despite their potential, applying VLA models to robotic endoscopy presents unique challenges due to the complex and dynamic anatomical environments of the gastrointestinal (GI) tract. To address this, we introduce EndoVLA, designed specifically for continuum robots in GI interventions. Given endoscopic images and surgeon-issued tracking prompts, EndoVLA performs three core tasks: (1) polyp tracking, (2) delineation and following of abnormal mucosal regions, and (3) adherence to circular markers during circumferential cutting. To tackle data scarcity and domain shifts, we propose a dual-phase strategy comprising supervised fine-tuning on our EndoVLA-Motion dataset and reinforcement fine-tuning with task-aware rewards. Our approach significantly improves tracking performance in endoscopy and enables zero-shot generalization in diverse scenes and complex sequential tasks.

## 参考
- http://arxiv.org/abs/2505.15206v1

