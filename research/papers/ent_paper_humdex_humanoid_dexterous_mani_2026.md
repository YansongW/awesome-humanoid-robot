---
$id: ent_paper_humdex_humanoid_dexterous_mani_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumDex: Humanoid Dexterous Manipulation Made Easy'
  zh: 'HumDex: Humanoid Dexterous Manipulation Made Easy'
  ko: 'HumDex: Humanoid Dexterous Manipulation Made Easy'
summary:
  en: 'HumDex: Humanoid Dexterous Manipulation Made Easy is a 2026 work on manipulation for humanoid robots.'
  zh: 'HumDex: Humanoid Dexterous Manipulation Made Easy is a 2026 work on manipulation for humanoid robots.'
  ko: 'HumDex: Humanoid Dexterous Manipulation Made Easy is a 2026 work on manipulation for humanoid robots.'
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
- humdex
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.12260v2.
sources:
- id: src_001
  type: paper
  title: 'HumDex: Humanoid Dexterous Manipulation Made Easy (arXiv)'
  url: https://arxiv.org/abs/2603.12260
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
This paper investigates humanoid whole-body dexterous manipulation, where the efficient collection of high-quality demonstration data remains a central bottleneck. Existing teleoperation systems often suffer from limited portability, occlusion, or insufficient precision, which hinders their applicability to complex whole-body tasks. To address these challenges, we introduce HumDex, a portable teleoperation system designed for humanoid whole-body dexterous manipulation. Our system leverages IMU-based motion tracking to address the portability-precision trade-off, enabling accurate full-body tracking while remaining easy to deploy. For dexterous hand control, we further introduce a learning-based retargeting method that generates smooth and natural hand motions without manual parameter tuning. Beyond teleoperation, HumDex enables efficient collection of human motion data. Building on this capability, we propose a two-stage imitation learning framework that first pre-trains on diverse human motion data to learn generalizable priors, and then fine-tunes on robot data to bridge the embodiment gap for precise execution. We demonstrate that this approach significantly improves generalization to new configurations, objects, and backgrounds with minimal data acquisition costs. The entire system is fully reproducible and open-sourced at https://github.com/physical-superintelligence-lab/humdex.

## 核心内容
This paper investigates humanoid whole-body dexterous manipulation, where the efficient collection of high-quality demonstration data remains a central bottleneck. Existing teleoperation systems often suffer from limited portability, occlusion, or insufficient precision, which hinders their applicability to complex whole-body tasks. To address these challenges, we introduce HumDex, a portable teleoperation system designed for humanoid whole-body dexterous manipulation. Our system leverages IMU-based motion tracking to address the portability-precision trade-off, enabling accurate full-body tracking while remaining easy to deploy. For dexterous hand control, we further introduce a learning-based retargeting method that generates smooth and natural hand motions without manual parameter tuning. Beyond teleoperation, HumDex enables efficient collection of human motion data. Building on this capability, we propose a two-stage imitation learning framework that first pre-trains on diverse human motion data to learn generalizable priors, and then fine-tunes on robot data to bridge the embodiment gap for precise execution. We demonstrate that this approach significantly improves generalization to new configurations, objects, and backgrounds with minimal data acquisition costs. The entire system is fully reproducible and open-sourced at https://github.com/physical-superintelligence-lab/humdex.

## 参考
- http://arxiv.org/abs/2603.12260v2

