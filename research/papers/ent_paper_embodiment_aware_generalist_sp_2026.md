---
$id: ent_paper_embodiment_aware_generalist_sp_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Embodiment-Aware Generalist Specialist Distillation for Unified Humanoid Whole-Body Control
  zh: Embodiment-Aware Generalist Specialist Distillation for Unified Humanoid Whole-Body Control
  ko: Embodiment-Aware Generalist Specialist Distillation for Unified Humanoid Whole-Body Control
summary:
  en: Embodiment-Aware Generalist Specialist Distillation for Unified Humanoid Whole-Body Control is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.
  zh: Embodiment-Aware Generalist Specialist Distillation for Unified Humanoid Whole-Body Control is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.
  ko: Embodiment-Aware Generalist Specialist Distillation for Unified Humanoid Whole-Body Control is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- embodiment_aware_generalist_sp
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.02960v2.
sources:
- id: src_001
  type: paper
  title: Embodiment-Aware Generalist Specialist Distillation for Unified Humanoid Whole-Body Control (arXiv)
  url: https://arxiv.org/abs/2602.02960
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid Whole-Body Controllers trained with reinforcement learning (RL) have recently achieved remarkable performance, yet many target a single robot embodiment. Variations in dynamics, degrees of freedom (DoFs), and kinematic topology still hinder a single policy from commanding diverse humanoids. Moreover, obtaining a generalist policy that not only transfers across embodiments but also supports richer behaviors-beyond simple walking to squatting, leaning-remains especially challenging. In this work, we tackle these obstacles by introducing EAGLE, an iterative generalist-specialist distillation framework that produces a single unified policy that controls multiple heterogeneous humanoids without per-robot reward tuning. During each cycle, embodiment-specific specialists are forked from the current generalist, refined on their respective robots, and new skills are distilled back into the generalist by training on the pooled embodiment set. Repeating this loop until performance convergence produces a robust Whole-Body Controller validated on robots such as Unitree H1, G1, and Fourier N1. We conducted experiments on five different robots in simulation and four in real-world settings. Through quantitative evaluations, EAGLE achieves high tracking accuracy and robustness compared to other methods, marking a step toward scalable, fleet-level humanoid control. See more details at https://eagle-wbc.github.io/

## 核心内容
Humanoid Whole-Body Controllers trained with reinforcement learning (RL) have recently achieved remarkable performance, yet many target a single robot embodiment. Variations in dynamics, degrees of freedom (DoFs), and kinematic topology still hinder a single policy from commanding diverse humanoids. Moreover, obtaining a generalist policy that not only transfers across embodiments but also supports richer behaviors-beyond simple walking to squatting, leaning-remains especially challenging. In this work, we tackle these obstacles by introducing EAGLE, an iterative generalist-specialist distillation framework that produces a single unified policy that controls multiple heterogeneous humanoids without per-robot reward tuning. During each cycle, embodiment-specific specialists are forked from the current generalist, refined on their respective robots, and new skills are distilled back into the generalist by training on the pooled embodiment set. Repeating this loop until performance convergence produces a robust Whole-Body Controller validated on robots such as Unitree H1, G1, and Fourier N1. We conducted experiments on five different robots in simulation and four in real-world settings. Through quantitative evaluations, EAGLE achieves high tracking accuracy and robustness compared to other methods, marking a step toward scalable, fleet-level humanoid control. See more details at https://eagle-wbc.github.io/

## 参考
- http://arxiv.org/abs/2602.02960v2

