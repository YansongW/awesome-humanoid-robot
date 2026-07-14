---
$id: ent_paper_pimbs_efficient_body_schema_le_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PIMBS: Efficient Body Schema Learning for Musculoskeletal Humanoids'
  zh: 'PIMBS: Efficient Body Schema Learning for Musculoskeletal Humanoids'
  ko: 'PIMBS: Efficient Body Schema Learning for Musculoskeletal Humanoids'
summary:
  en: 'PIMBS: Efficient Body Schema Learning for Musculoskeletal Humanoids is a 2025 work on hardware design for humanoid
    robots.'
  zh: 'PIMBS: Efficient Body Schema Learning for Musculoskeletal Humanoids is a 2025 work on hardware design for humanoid
    robots.'
  ko: 'PIMBS: Efficient Body Schema Learning for Musculoskeletal Humanoids is a 2025 work on hardware design for humanoid
    robots.'
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- hardware_design
- humanoid
- pimbs
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.20343v2.
sources:
- id: src_001
  type: paper
  title: 'PIMBS: Efficient Body Schema Learning for Musculoskeletal Humanoids (arXiv)'
  url: https://arxiv.org/abs/2506.20343
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Musculoskeletal humanoids are robots that closely mimic the human musculoskeletal system, offering various advantages such as variable stiffness control, redundancy, and flexibility. However, their body structure is complex, and muscle paths often significantly deviate from geometric models. To address this, numerous studies have been conducted to learn body schema, particularly the relationships among joint angles, muscle tension, and muscle length. These studies typically rely solely on data collected from the actual robot, but this data collection process is labor-intensive, and learning becomes difficult when the amount of data is limited. Therefore, in this study, we propose a method that applies the concept of Physics-Informed Neural Networks (PINNs) to the learning of body schema in musculoskeletal humanoids, enabling high-accuracy learning even with a small amount of data. By utilizing not only data obtained from the actual robot but also the physical laws governing the relationship between torque and muscle tension under the assumption of correct joint structure, more efficient learning becomes possible. We apply the proposed method to both simulation and an actual musculoskeletal humanoid and discuss its effectiveness and characteristics.

## 核心内容
Musculoskeletal humanoids are robots that closely mimic the human musculoskeletal system, offering various advantages such as variable stiffness control, redundancy, and flexibility. However, their body structure is complex, and muscle paths often significantly deviate from geometric models. To address this, numerous studies have been conducted to learn body schema, particularly the relationships among joint angles, muscle tension, and muscle length. These studies typically rely solely on data collected from the actual robot, but this data collection process is labor-intensive, and learning becomes difficult when the amount of data is limited. Therefore, in this study, we propose a method that applies the concept of Physics-Informed Neural Networks (PINNs) to the learning of body schema in musculoskeletal humanoids, enabling high-accuracy learning even with a small amount of data. By utilizing not only data obtained from the actual robot but also the physical laws governing the relationship between torque and muscle tension under the assumption of correct joint structure, more efficient learning becomes possible. We apply the proposed method to both simulation and an actual musculoskeletal humanoid and discuss its effectiveness and characteristics.

## 参考
- http://arxiv.org/abs/2506.20343v2

