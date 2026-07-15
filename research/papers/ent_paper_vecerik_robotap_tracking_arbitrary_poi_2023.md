---
$id: ent_paper_vecerik_robotap_tracking_arbitrary_poi_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboTAP: Tracking Arbitrary Points for Few-Shot Visual Imitation'
  zh: RoboTAP
  ko: 'RoboTAP: Tracking Arbitrary Points for Few-Shot Visual Imitation'
summary:
  en: 'RoboTAP: Tracking Arbitrary Points for Few-Shot Visual Imitation (RoboTAP), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, Department of Computer Science at University College London,
    and published at ICRA 2023.'
  zh: 'RoboTAP: Tracking Arbitrary Points for Few-Shot Visual Imitation (RoboTAP), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, Department of Computer Science at University College London,
    and published at ICRA 2023.'
  ko: 'RoboTAP: Tracking Arbitrary Points for Few-Shot Visual Imitation (RoboTAP), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, Department of Computer Science at University College London,
    and published at ICRA 2023.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- robotap
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2308.15975v2.
sources:
- id: src_001
  type: website
  title: RoboTAP source
  url: https://doi.org/10.1109/ICRA57147.2024.10611409
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
For robots to be useful outside labs and specialized factories we need a way to teach them new useful behaviors quickly. Current approaches lack either the generality to onboard new tasks without task-specific engineering, or else lack the data-efficiency to do so in an amount of time that enables practical use. In this work we explore dense tracking as a representational vehicle to allow faster and more general learning from demonstration. Our approach utilizes Track-Any-Point (TAP) models to isolate the relevant motion in a demonstration, and parameterize a low-level controller to reproduce this motion across changes in the scene configuration. We show this results in robust robot policies that can solve complex object-arrangement tasks such as shape-matching, stacking, and even full path-following tasks such as applying glue and sticking objects together, all from demonstrations that can be collected in minutes.

## 核心内容
For robots to be useful outside labs and specialized factories we need a way to teach them new useful behaviors quickly. Current approaches lack either the generality to onboard new tasks without task-specific engineering, or else lack the data-efficiency to do so in an amount of time that enables practical use. In this work we explore dense tracking as a representational vehicle to allow faster and more general learning from demonstration. Our approach utilizes Track-Any-Point (TAP) models to isolate the relevant motion in a demonstration, and parameterize a low-level controller to reproduce this motion across changes in the scene configuration. We show this results in robust robot policies that can solve complex object-arrangement tasks such as shape-matching, stacking, and even full path-following tasks such as applying glue and sticking objects together, all from demonstrations that can be collected in minutes.

## 参考
- http://arxiv.org/abs/2308.15975v2

