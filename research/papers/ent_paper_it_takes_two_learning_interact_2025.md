---
$id: ent_paper_it_takes_two_learning_interact_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'It Takes Two: Learning Interactive Whole-Body Control Between Humanoid Robots'
  zh: 'It Takes Two: Learning Interactive Whole-Body Control Between Humanoid Robots'
  ko: 'It Takes Two: Learning Interactive Whole-Body Control Between Humanoid Robots'
summary:
  en: 'It Takes Two: Learning Interactive Whole-Body Control Between Humanoid Robots is a 2025 work on loco-manipulation and
    whole-body-control for humanoid robots.'
  zh: 'It Takes Two: Learning Interactive Whole-Body Control Between Humanoid Robots is a 2025 work on loco-manipulation and
    whole-body-control for humanoid robots.'
  ko: 'It Takes Two: Learning Interactive Whole-Body Control Between Humanoid Robots is a 2025 work on loco-manipulation and
    whole-body-control for humanoid robots.'
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
- it_takes_two
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.10206v1.
sources:
- id: src_001
  type: paper
  title: 'It Takes Two: Learning Interactive Whole-Body Control Between Humanoid Robots (arXiv)'
  url: https://arxiv.org/abs/2510.10206
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The true promise of humanoid robotics lies beyond single-agent autonomy: two or more humanoids must engage in physically grounded, socially meaningful whole-body interactions that echo the richness of human social interaction. However, single-humanoid methods suffer from the isolation issue, ignoring inter-agent dynamics and causing misaligned contacts, interpenetrations, and unrealistic motions. To address this, we present Harmanoid , a dual-humanoid motion imitation framework that transfers interacting human motions to two robots while preserving both kinematic fidelity and physical realism. Harmanoid comprises two key components: (i) contact-aware motion retargeting, which restores inter-body coordination by aligning SMPL contacts with robot vertices, and (ii) interaction-driven motion controller, which leverages interaction-specific rewards to enforce coordinated keypoints and physically plausible contacts. By explicitly modeling inter-agent contacts and interaction-aware dynamics, Harmanoid captures the coupled behaviors between humanoids that single-humanoid frameworks inherently overlook. Experiments demonstrate that Harmanoid significantly improves interactive motion imitation, surpassing existing single-humanoid frameworks that largely fail in such scenarios.

## 核心内容
The true promise of humanoid robotics lies beyond single-agent autonomy: two or more humanoids must engage in physically grounded, socially meaningful whole-body interactions that echo the richness of human social interaction. However, single-humanoid methods suffer from the isolation issue, ignoring inter-agent dynamics and causing misaligned contacts, interpenetrations, and unrealistic motions. To address this, we present Harmanoid , a dual-humanoid motion imitation framework that transfers interacting human motions to two robots while preserving both kinematic fidelity and physical realism. Harmanoid comprises two key components: (i) contact-aware motion retargeting, which restores inter-body coordination by aligning SMPL contacts with robot vertices, and (ii) interaction-driven motion controller, which leverages interaction-specific rewards to enforce coordinated keypoints and physically plausible contacts. By explicitly modeling inter-agent contacts and interaction-aware dynamics, Harmanoid captures the coupled behaviors between humanoids that single-humanoid frameworks inherently overlook. Experiments demonstrate that Harmanoid significantly improves interactive motion imitation, surpassing existing single-humanoid frameworks that largely fail in such scenarios.

## 参考
- http://arxiv.org/abs/2510.10206v1

