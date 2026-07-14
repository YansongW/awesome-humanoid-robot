---
$id: ent_paper_unified_humanoid_fall_safety_p_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Unified Humanoid Fall-Safety Policy from a Few Demonstrations
  zh: Unified Humanoid Fall-Safety Policy from a Few Demonstrations
  ko: Unified Humanoid Fall-Safety Policy from a Few Demonstrations
summary:
  en: Unified Humanoid Fall-Safety Policy from a Few Demonstrations is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: Unified Humanoid Fall-Safety Policy from a Few Demonstrations is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
  ko: Unified Humanoid Fall-Safety Policy from a Few Demonstrations is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
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
- loco_manipulation
- unified_humanoid_fall_safety_p
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.07407v1.
sources:
- id: src_001
  type: paper
  title: Unified Humanoid Fall-Safety Policy from a Few Demonstrations (arXiv)
  url: https://arxiv.org/abs/2511.07407
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Falling is an inherent risk of humanoid mobility. Maintaining stability is thus a primary safety focus in robot control and learning, yet no existing approach fully averts loss of balance. When instability does occur, prior work addresses only isolated aspects of falling: avoiding falls, choreographing a controlled descent, or standing up afterward. Consequently, humanoid robots lack integrated strategies for impact mitigation and prompt recovery when real falls defy these scripts. We aim to go beyond keeping balance to make the entire fall-and-recovery process safe and autonomous: prevent falls when possible, reduce impact when unavoidable, and stand up when fallen. By fusing sparse human demonstrations with reinforcement learning and an adaptive diffusion-based memory of safe reactions, we learn adaptive whole-body behaviors that unify fall prevention, impact mitigation, and rapid recovery in one policy. Experiments in simulation and on a Unitree G1 demonstrate robust sim-to-real transfer, lower impact forces, and consistently fast recovery across diverse disturbances, pointing towards safer, more resilient humanoids in real environments. Videos are available at https://firm2025.github.io/.

## 核心内容
Falling is an inherent risk of humanoid mobility. Maintaining stability is thus a primary safety focus in robot control and learning, yet no existing approach fully averts loss of balance. When instability does occur, prior work addresses only isolated aspects of falling: avoiding falls, choreographing a controlled descent, or standing up afterward. Consequently, humanoid robots lack integrated strategies for impact mitigation and prompt recovery when real falls defy these scripts. We aim to go beyond keeping balance to make the entire fall-and-recovery process safe and autonomous: prevent falls when possible, reduce impact when unavoidable, and stand up when fallen. By fusing sparse human demonstrations with reinforcement learning and an adaptive diffusion-based memory of safe reactions, we learn adaptive whole-body behaviors that unify fall prevention, impact mitigation, and rapid recovery in one policy. Experiments in simulation and on a Unitree G1 demonstrate robust sim-to-real transfer, lower impact forces, and consistently fast recovery across diverse disturbances, pointing towards safer, more resilient humanoids in real environments. Videos are available at https://firm2025.github.io/.

## 参考
- http://arxiv.org/abs/2511.07407v1

