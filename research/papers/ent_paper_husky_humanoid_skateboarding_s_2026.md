---
$id: ent_paper_husky_humanoid_skateboarding_s_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HUSKY: Humanoid Skateboarding System via Physics-Aware Whole-Body Control'
  zh: 'HUSKY: Humanoid Skateboarding System via Physics-Aware Whole-Body Control'
  ko: 'HUSKY: Humanoid Skateboarding System via Physics-Aware Whole-Body Control'
summary:
  en: 'HUSKY: Humanoid Skateboarding System via Physics-Aware Whole-Body Control is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: 'HUSKY: Humanoid Skateboarding System via Physics-Aware Whole-Body Control is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  ko: 'HUSKY: Humanoid Skateboarding System via Physics-Aware Whole-Body Control is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
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
- husky
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.03205v2.
sources:
- id: src_001
  type: paper
  title: 'HUSKY: Humanoid Skateboarding System via Physics-Aware Whole-Body Control (arXiv)'
  url: https://arxiv.org/abs/2602.03205
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
While current humanoid whole-body control frameworks predominantly rely on the static environment assumptions, addressing tasks characterized by high dynamism and complex interactions presents a formidable challenge. In this paper, we address humanoid skateboarding, a highly challenging task requiring stable dynamic maneuvering on an underactuated wheeled platform. This integrated system is governed by non-holonomic constraints and tightly coupled human-object interactions. Successfully executing this task requires simultaneous mastery of hybrid contact dynamics and robust balance control on a mechanically coupled, dynamically unstable skateboard. To overcome the aforementioned challenges, we propose HUSKY, a learning-based framework that integrates humanoid-skateboard system modeling and physics-aware whole-body control. We first model the coupling relationship between board tilt and truck steering angles, enabling a principled analysis of system dynamics. Building upon this, HUSKY leverages Adversarial Motion Priors (AMP) to learn human-like pushing motions and employs a physics-guided, heading-oriented strategy for lean-to-steer behaviors. Moreover, a trajectory-guided mechanism ensures smooth and stable transitions between pushing and steering. Experimental results on the Unitree G1 humanoid platform demonstrate that our framework enables stable and agile maneuvering on skateboards in real-world scenarios. The project page is available on https://husky-humanoid.github.io/.

## 核心内容
While current humanoid whole-body control frameworks predominantly rely on the static environment assumptions, addressing tasks characterized by high dynamism and complex interactions presents a formidable challenge. In this paper, we address humanoid skateboarding, a highly challenging task requiring stable dynamic maneuvering on an underactuated wheeled platform. This integrated system is governed by non-holonomic constraints and tightly coupled human-object interactions. Successfully executing this task requires simultaneous mastery of hybrid contact dynamics and robust balance control on a mechanically coupled, dynamically unstable skateboard. To overcome the aforementioned challenges, we propose HUSKY, a learning-based framework that integrates humanoid-skateboard system modeling and physics-aware whole-body control. We first model the coupling relationship between board tilt and truck steering angles, enabling a principled analysis of system dynamics. Building upon this, HUSKY leverages Adversarial Motion Priors (AMP) to learn human-like pushing motions and employs a physics-guided, heading-oriented strategy for lean-to-steer behaviors. Moreover, a trajectory-guided mechanism ensures smooth and stable transitions between pushing and steering. Experimental results on the Unitree G1 humanoid platform demonstrate that our framework enables stable and agile maneuvering on skateboards in real-world scenarios. The project page is available on https://husky-humanoid.github.io/.

## 参考
- http://arxiv.org/abs/2602.03205v2

