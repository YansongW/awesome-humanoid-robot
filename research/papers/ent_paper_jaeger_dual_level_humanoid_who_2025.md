---
$id: ent_paper_jaeger_dual_level_humanoid_who_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'JAEGER: Dual-Level Humanoid Whole-Body Controller'
  zh: 'JAEGER: Dual-Level Humanoid Whole-Body Controller'
  ko: 'JAEGER: Dual-Level Humanoid Whole-Body Controller'
summary:
  en: 'JAEGER: Dual-Level Humanoid Whole-Body Controller is a 2025 work on loco-manipulation and whole-body-control for humanoid
    robots.'
  zh: 'JAEGER: Dual-Level Humanoid Whole-Body Controller is a 2025 work on loco-manipulation and whole-body-control for humanoid
    robots.'
  ko: 'JAEGER: Dual-Level Humanoid Whole-Body Controller is a 2025 work on loco-manipulation and whole-body-control for humanoid
    robots.'
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
- jaeger
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.06584v2.
sources:
- id: src_001
  type: paper
  title: 'JAEGER: Dual-Level Humanoid Whole-Body Controller (arXiv)'
  url: https://arxiv.org/abs/2505.06584
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This paper presents JAEGER, a dual-level whole-body controller for humanoid robots that addresses the challenges of training a more robust and versatile policy. Unlike traditional single-controller approaches, JAEGER separates the control of the upper and lower bodies into two independent controllers, so that they can better focus on their distinct tasks. This separation alleviates the dimensionality curse and improves fault tolerance. JAEGER supports both root velocity tracking (coarse-grained control) and local joint angle tracking (fine-grained control), enabling versatile and stable movements. To train the controller, we utilize a human motion dataset (AMASS), retargeting human poses to humanoid poses through an efficient retargeting network, and employ a curriculum learning approach. This method performs supervised learning for initialization, followed by reinforcement learning for further exploration. We conduct our experiments on two humanoid platforms and demonstrate the superiority of our approach against state-of-the-art methods in both simulation and real environments.

## 核心内容
This paper presents JAEGER, a dual-level whole-body controller for humanoid robots that addresses the challenges of training a more robust and versatile policy. Unlike traditional single-controller approaches, JAEGER separates the control of the upper and lower bodies into two independent controllers, so that they can better focus on their distinct tasks. This separation alleviates the dimensionality curse and improves fault tolerance. JAEGER supports both root velocity tracking (coarse-grained control) and local joint angle tracking (fine-grained control), enabling versatile and stable movements. To train the controller, we utilize a human motion dataset (AMASS), retargeting human poses to humanoid poses through an efficient retargeting network, and employ a curriculum learning approach. This method performs supervised learning for initialization, followed by reinforcement learning for further exploration. We conduct our experiments on two humanoid platforms and demonstrate the superiority of our approach against state-of-the-art methods in both simulation and real environments.

## 参考
- http://arxiv.org/abs/2505.06584v2

