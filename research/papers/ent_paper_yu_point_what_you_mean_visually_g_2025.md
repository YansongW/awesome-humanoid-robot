---
$id: ent_paper_yu_point_what_you_mean_visually_g_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Point What You Mean: Visually Grounded Instruction Policy'
  zh: Point-VLA
  ko: 'Point What You Mean: Visually Grounded Instruction Policy'
summary:
  en: 'Point What You Mean: Visually Grounded Instruction Policy (Point-VLA), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Tongji University, Shanghai Jiao Tong University, Spirit AI, Tsinghua University.'
  zh: 'Point What You Mean: Visually Grounded Instruction Policy (Point-VLA), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Tongji University, Shanghai Jiao Tong University, Spirit AI, Tsinghua University.'
  ko: 'Point What You Mean: Visually Grounded Instruction Policy (Point-VLA), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Tongji University, Shanghai Jiao Tong University, Spirit AI, Tsinghua University.'
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
- point_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.18933v2.
sources:
- id: src_001
  type: paper
  title: 'Point What You Mean: Visually Grounded Instruction Policy (arXiv)'
  url: https://arxiv.org/abs/2512.18933
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Point-VLA source
  url: https://doi.org/10.48550/arXiv.2512.18933
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models align vision and language with embodied control, but their object referring ability remains limited when relying solely on text prompt, especially in cluttered or out-of-distribution (OOD) scenes. In this study, we introduce the Point-VLA, a plug-and-play policy that augments language instructions with explicit visual cues (e.g., bounding boxes) to resolve referential ambiguity and enable precise object-level grounding. To efficiently scale visually grounded datasets, we further develop an automatic data annotation pipeline requiring minimal human effort. We evaluate Point-VLA on diverse real-world referring tasks and observe consistently stronger performance than text-only instruction VLAs, particularly in cluttered or unseen-object scenarios, with robust generalization. These results demonstrate that Point-VLA effectively resolves object referring ambiguity through pixel-level visual grounding, achieving more generalizable embodied control.

## 核心内容
Vision-Language-Action (VLA) models align vision and language with embodied control, but their object referring ability remains limited when relying solely on text prompt, especially in cluttered or out-of-distribution (OOD) scenes. In this study, we introduce the Point-VLA, a plug-and-play policy that augments language instructions with explicit visual cues (e.g., bounding boxes) to resolve referential ambiguity and enable precise object-level grounding. To efficiently scale visually grounded datasets, we further develop an automatic data annotation pipeline requiring minimal human effort. We evaluate Point-VLA on diverse real-world referring tasks and observe consistently stronger performance than text-only instruction VLAs, particularly in cluttered or unseen-object scenarios, with robust generalization. These results demonstrate that Point-VLA effectively resolves object referring ambiguity through pixel-level visual grounding, achieving more generalizable embodied control.

## 参考
- http://arxiv.org/abs/2512.18933v2

