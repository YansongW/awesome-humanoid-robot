---
$id: ent_paper_phuma_physically_grounded_huma_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PHUMA: Physically-Grounded Humanoid Locomotion Dataset'
  zh: 'PHUMA: Physically-Grounded Humanoid Locomotion Dataset'
  ko: 'PHUMA: Physically-Grounded Humanoid Locomotion Dataset'
summary:
  en: 'PHUMA: Physically-Grounded Humanoid Locomotion Dataset is a 2025 work on locomotion for humanoid robots.'
  zh: 'PHUMA: Physically-Grounded Humanoid Locomotion Dataset is a 2025 work on locomotion for humanoid robots.'
  ko: 'PHUMA: Physically-Grounded Humanoid Locomotion Dataset is a 2025 work on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- phuma
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.26236v2.
sources:
- id: src_001
  type: paper
  title: 'PHUMA: Physically-Grounded Humanoid Locomotion Dataset (arXiv)'
  url: https://arxiv.org/abs/2510.26236
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Motion imitation is a promising approach for humanoid locomotion, enabling agents to acquire humanlike behaviors. Existing methods typically rely on high-quality motion capture datasets such as AMASS, but these are scarce and expensive, limiting scalability and diversity. Recent studies attempt to scale data collection by converting large-scale internet videos, exemplified by Humanoid-X. However, they often suffer from physical artifacts such as floating, penetration, and foot skating, which hinder stable imitation. To address this, we introduce PHUMA, a Physically Reliable HUMAnoid locomotion dataset produced by a two-stage pipeline combining physics-aware curation and physics-constrained retargeting, aggregating both motion capture and internet video into a physically reliable, 73-hour corpus. On motion tracking benchmarks, PHUMA-trained policies achieve higher success rates than those trained on AMASS and Humanoid-X, and successfully transfer zero-shot to a real Unitree G1. The code is available at https://davian-robotics.github.io/PHUMA.

## 核心内容
Motion imitation is a promising approach for humanoid locomotion, enabling agents to acquire humanlike behaviors. Existing methods typically rely on high-quality motion capture datasets such as AMASS, but these are scarce and expensive, limiting scalability and diversity. Recent studies attempt to scale data collection by converting large-scale internet videos, exemplified by Humanoid-X. However, they often suffer from physical artifacts such as floating, penetration, and foot skating, which hinder stable imitation. To address this, we introduce PHUMA, a Physically Reliable HUMAnoid locomotion dataset produced by a two-stage pipeline combining physics-aware curation and physics-constrained retargeting, aggregating both motion capture and internet video into a physically reliable, 73-hour corpus. On motion tracking benchmarks, PHUMA-trained policies achieve higher success rates than those trained on AMASS and Humanoid-X, and successfully transfer zero-shot to a real Unitree G1. The code is available at https://davian-robotics.github.io/PHUMA.

## 参考
- http://arxiv.org/abs/2510.26236v2

