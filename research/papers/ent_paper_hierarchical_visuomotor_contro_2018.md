---
$id: ent_paper_hierarchical_visuomotor_contro_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Hierarchical visuomotor control of humanoids
  zh: Hierarchical visuomotor control of humanoids
  ko: Hierarchical visuomotor control of humanoids
summary:
  en: Hierarchical visuomotor control of humanoids is a 2018 work on physics-based character animation for humanoid robots.
  zh: Hierarchical visuomotor control of humanoids is a 2018 work on physics-based character animation for humanoid robots.
  ko: Hierarchical visuomotor control of humanoids is a 2018 work on physics-based character animation for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- hierarchical_visuomotor_contro
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1811.09656v2.
sources:
- id: src_001
  type: paper
  title: Hierarchical visuomotor control of humanoids (arXiv)
  url: https://arxiv.org/abs/1811.09656
  date: '2018'
  accessed_at: '2026-07-01'
---
## 概述
We aim to build complex humanoid agents that integrate perception, motor control, and memory. In this work, we partly factor this problem into low-level motor control from proprioception and high-level coordination of the low-level skills informed by vision. We develop an architecture capable of surprisingly flexible, task-directed motor control of a relatively high-DoF humanoid body by combining pre-training of low-level motor controllers with a high-level, task-focused controller that switches among low-level sub-policies. The resulting system is able to control a physically-simulated humanoid body to solve tasks that require coupling visual perception from an unstabilized egocentric RGB camera during locomotion in the environment. For a supplementary video link, see https://youtu.be/7GISvfbykLE .

## 核心内容
We aim to build complex humanoid agents that integrate perception, motor control, and memory. In this work, we partly factor this problem into low-level motor control from proprioception and high-level coordination of the low-level skills informed by vision. We develop an architecture capable of surprisingly flexible, task-directed motor control of a relatively high-DoF humanoid body by combining pre-training of low-level motor controllers with a high-level, task-focused controller that switches among low-level sub-policies. The resulting system is able to control a physically-simulated humanoid body to solve tasks that require coupling visual perception from an unstabilized egocentric RGB camera during locomotion in the environment. For a supplementary video link, see https://youtu.be/7GISvfbykLE .

## 参考
- http://arxiv.org/abs/1811.09656v2

