---
$id: ent_paper_intelligence_06_a_vla_that_learns_from_expe_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'π0.6*: a VLA That Learns From Experience'
  zh: π0.6*
  ko: 'π0.6*: a VLA That Learns From Experience'
summary:
  en: 'π0.6*: a VLA That Learns From Experience (π0.6*), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Physical Intelligence.'
  zh: 'π0.6*: a VLA That Learns From Experience (π0.6*), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Physical Intelligence.'
  ko: 'π0.6*: a VLA That Learns From Experience (π0.6*), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Physical Intelligence.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- '06'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.14759v2.
sources:
- id: src_001
  type: paper
  title: 'π0.6*: a VLA That Learns From Experience (arXiv)'
  url: https://arxiv.org/abs/2511.14759
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: π0.6* source
  url: https://doi.org/10.48550/arXiv.2511.14759
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We study how vision-language-action (VLA) models can improve through real-world deployments via reinforcement learning (RL). We present a general-purpose method, RL with Experience and Corrections via Advantage-conditioned Policies (RECAP), that provides for RL training of VLAs via advantage conditioning. Our method incorporates heterogeneous data into the self-improvement process, including demonstrations, data from on-policy collection, and expert teleoperated interventions provided during autonomous execution. RECAP starts by pre-training a generalist VLA with offline RL, which we call $π^{*}_{0.6}$, that can then be specialized to attain high performance on downstream tasks through on-robot data collection. We show that the $π^{*}_{0.6}$ model trained with the full RECAP method can fold laundry in real homes, reliably assemble boxes, and make espresso drinks using a professional espresso machine. On some of the hardest tasks, RECAP more than doubles task throughput and roughly halves the task failure rate.

## 核心内容
We study how vision-language-action (VLA) models can improve through real-world deployments via reinforcement learning (RL). We present a general-purpose method, RL with Experience and Corrections via Advantage-conditioned Policies (RECAP), that provides for RL training of VLAs via advantage conditioning. Our method incorporates heterogeneous data into the self-improvement process, including demonstrations, data from on-policy collection, and expert teleoperated interventions provided during autonomous execution. RECAP starts by pre-training a generalist VLA with offline RL, which we call $π^{*}_{0.6}$, that can then be specialized to attain high performance on downstream tasks through on-robot data collection. We show that the $π^{*}_{0.6}$ model trained with the full RECAP method can fold laundry in real homes, reliably assemble boxes, and make espresso drinks using a professional espresso machine. On some of the hardest tasks, RECAP more than doubles task throughput and roughly halves the task failure rate.

## 参考
- http://arxiv.org/abs/2511.14759v2

