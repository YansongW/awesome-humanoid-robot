---
$id: ent_paper_wen_gr_dexter_technical_report_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: GR-Dexter Technical Report
  zh: GR-Dexter
  ko: GR-Dexter Technical Report
summary:
  en: GR-Dexter Technical Report (GR-Dexter), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by ByteDance Seed.
  zh: GR-Dexter Technical Report (GR-Dexter), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by ByteDance Seed.
  ko: GR-Dexter Technical Report (GR-Dexter), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by ByteDance Seed.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- gr_dexter
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.24210v2.
sources:
- id: src_001
  type: paper
  title: GR-Dexter Technical Report (arXiv)
  url: https://arxiv.org/abs/2512.24210
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: GR-Dexter source
  url: https://doi.org/10.48550/arXiv.2512.24210
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models have enabled language-conditioned, long-horizon robot manipulation, but most existing systems are limited to grippers. Scaling VLA policies to bimanual robots with high degree-of-freedom (DoF) dexterous hands remains challenging due to the expanded action space, frequent hand-object occlusions, and the cost of collecting real-robot data. We present GR-Dexter, a holistic hardware-model-data framework for VLA-based generalist manipulation on a bimanual dexterous-hand robot. Our approach combines the design of a compact 21-DoF robotic hand, an intuitive bimanual teleoperation system for real-robot data collection, and a training recipe that leverages teleoperated robot trajectories together with large-scale vision-language and carefully curated cross-embodiment datasets. Across real-world evaluations spanning long-horizon everyday manipulation and generalizable pick-and-place, GR-Dexter achieves strong in-domain performance and improved robustness to unseen objects and unseen instructions. We hope GR-Dexter serves as a practical step toward generalist dexterous-hand robotic manipulation.

## 核心内容
Vision-language-action (VLA) models have enabled language-conditioned, long-horizon robot manipulation, but most existing systems are limited to grippers. Scaling VLA policies to bimanual robots with high degree-of-freedom (DoF) dexterous hands remains challenging due to the expanded action space, frequent hand-object occlusions, and the cost of collecting real-robot data. We present GR-Dexter, a holistic hardware-model-data framework for VLA-based generalist manipulation on a bimanual dexterous-hand robot. Our approach combines the design of a compact 21-DoF robotic hand, an intuitive bimanual teleoperation system for real-robot data collection, and a training recipe that leverages teleoperated robot trajectories together with large-scale vision-language and carefully curated cross-embodiment datasets. Across real-world evaluations spanning long-horizon everyday manipulation and generalizable pick-and-place, GR-Dexter achieves strong in-domain performance and improved robustness to unseen objects and unseen instructions. We hope GR-Dexter serves as a practical step toward generalist dexterous-hand robotic manipulation.

## 参考
- http://arxiv.org/abs/2512.24210v2

