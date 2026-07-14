---
$id: ent_paper_hierarchical_planning_and_cont_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Hierarchical Planning and Control for Box Loco-Manipulation
  zh: Hierarchical Planning and Control for Box Loco-Manipulation
  ko: Hierarchical Planning and Control for Box Loco-Manipulation
summary:
  en: Hierarchical Planning and Control for Box Loco-Manipulation is a 2023 work on physics-based character animation for
    humanoid robots.
  zh: Hierarchical Planning and Control for Box Loco-Manipulation is a 2023 work on physics-based character animation for
    humanoid robots.
  ko: Hierarchical Planning and Control for Box Loco-Manipulation is a 2023 work on physics-based character animation for
    humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- hierarchical_planning_and_cont
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2306.09532v2.
sources:
- id: src_001
  type: paper
  title: Hierarchical Planning and Control for Box Loco-Manipulation (arXiv)
  url: https://arxiv.org/abs/2306.09532
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Humans perform everyday tasks using a combination of locomotion and manipulation skills. Building a system that can handle both skills is essential to creating virtual humans. We present a physically-simulated human capable of solving box rearrangement tasks, which requires a combination of both skills. We propose a hierarchical control architecture, where each level solves the task at a different level of abstraction, and the result is a physics-based simulated virtual human capable of rearranging boxes in a cluttered environment. The control architecture integrates a planner, diffusion models, and physics-based motion imitation of sparse motion clips using deep reinforcement learning. Boxes can vary in size, weight, shape, and placement height. Code and trained control policies are provided.

## 核心内容
Humans perform everyday tasks using a combination of locomotion and manipulation skills. Building a system that can handle both skills is essential to creating virtual humans. We present a physically-simulated human capable of solving box rearrangement tasks, which requires a combination of both skills. We propose a hierarchical control architecture, where each level solves the task at a different level of abstraction, and the result is a physics-based simulated virtual human capable of rearranging boxes in a cluttered environment. The control architecture integrates a planner, diffusion models, and physics-based motion imitation of sparse motion clips using deep reinforcement learning. Boxes can vary in size, weight, shape, and placement height. Code and trained control policies are provided.

## 参考
- http://arxiv.org/abs/2306.09532v2

