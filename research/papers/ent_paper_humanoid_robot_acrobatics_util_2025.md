---
$id: ent_paper_humanoid_robot_acrobatics_util_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics
  zh: Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics
  ko: Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics
summary:
  en: Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics is a 2025 work on physics-based character
    animation for humanoid robots.
  zh: Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics is a 2025 work on physics-based character
    animation for humanoid robots.
  ko: Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics is a 2025 work on physics-based character
    animation for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- humanoid_robot_acrobatics_util
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.08258v1.
sources:
- id: src_001
  type: paper
  title: Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics (arXiv)
  url: https://arxiv.org/abs/2508.08258
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Endowing humanoid robots with the ability to perform highly dynamic motions akin to human-level acrobatics has been a long-standing challenge. Successfully performing these maneuvers requires close consideration of the underlying physics in both trajectory optimization for planning and control during execution. This is particularly challenging due to humanoids' high degree-of-freedom count and associated exponentially scaling complexities, which makes planning on the explicit equations of motion intractable. Typical workarounds include linearization methods and model approximations. However, neither are sufficient because they produce degraded performance on the true robotic system. This paper presents a control architecture comprising trajectory optimization and whole-body control, intermediated by a matching model abstraction, that enables the execution of acrobatic maneuvers, including constraint and posture behaviors, conditioned on the unabbreviated equations of motion of the articulated rigid body model. A review of underlying modeling and control methods is given, followed by implementation details including model abstraction, trajectory optimization and whole-body controller. The system's effectiveness is analyzed in simulation.

## 核心内容
Endowing humanoid robots with the ability to perform highly dynamic motions akin to human-level acrobatics has been a long-standing challenge. Successfully performing these maneuvers requires close consideration of the underlying physics in both trajectory optimization for planning and control during execution. This is particularly challenging due to humanoids' high degree-of-freedom count and associated exponentially scaling complexities, which makes planning on the explicit equations of motion intractable. Typical workarounds include linearization methods and model approximations. However, neither are sufficient because they produce degraded performance on the true robotic system. This paper presents a control architecture comprising trajectory optimization and whole-body control, intermediated by a matching model abstraction, that enables the execution of acrobatic maneuvers, including constraint and posture behaviors, conditioned on the unabbreviated equations of motion of the articulated rigid body model. A review of underlying modeling and control methods is given, followed by implementation details including model abstraction, trajectory optimization and whole-body controller. The system's effectiveness is analyzed in simulation.

## 参考
- http://arxiv.org/abs/2508.08258v1

