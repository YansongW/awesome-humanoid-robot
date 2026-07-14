---
$id: ent_paper_reactor_reinforcement_learning_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ReActor: Reinforcement Learning for Physics-Aware Motion Retargeting'
  zh: 'ReActor: Reinforcement Learning for Physics-Aware Motion Retargeting'
  ko: 'ReActor: Reinforcement Learning for Physics-Aware Motion Retargeting'
summary:
  en: 'ReActor: Reinforcement Learning for Physics-Aware Motion Retargeting is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: 'ReActor: Reinforcement Learning for Physics-Aware Motion Retargeting is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  ko: 'ReActor: Reinforcement Learning for Physics-Aware Motion Retargeting is a 2026 work on loco-manipulation and whole-body-control
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
- loco_manipulation
- reactor
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2605.06593v1.
sources:
- id: src_001
  type: paper
  title: 'ReActor: Reinforcement Learning for Physics-Aware Motion Retargeting (arXiv)'
  url: https://arxiv.org/abs/2605.06593
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Retargeting human kinematic reference motion onto a robot's morphology remains a formidable challenge. Existing methods often produce physical inconsistencies, such as foot sliding, self-collisions, or dynamically infeasible motions, which hinder downstream imitation learning. We propose a bilevel optimization framework that jointly adapts reference motions to a robot's morphology while training a tracking policy using reinforcement learning. To make the optimization tractable, we derive an approximate gradient for the upper-level loss. Our framework requires only a sparse set of semantic rigid-body correspondences and eliminates the need for manual tuning by identifying optimal values for a parameterization expressive enough to preserve characteristic motion across different embodiments. Moreover, by integrating retargeting directly with physics simulation, we produce physically plausible motions that facilitate robust imitation learning. We validate our method in simulation and on hardware, demonstrating challenging motions for morphologies that differ significantly from a human, including retargeting onto a quadruped.

## 核心内容
Retargeting human kinematic reference motion onto a robot's morphology remains a formidable challenge. Existing methods often produce physical inconsistencies, such as foot sliding, self-collisions, or dynamically infeasible motions, which hinder downstream imitation learning. We propose a bilevel optimization framework that jointly adapts reference motions to a robot's morphology while training a tracking policy using reinforcement learning. To make the optimization tractable, we derive an approximate gradient for the upper-level loss. Our framework requires only a sparse set of semantic rigid-body correspondences and eliminates the need for manual tuning by identifying optimal values for a parameterization expressive enough to preserve characteristic motion across different embodiments. Moreover, by integrating retargeting directly with physics simulation, we produce physically plausible motions that facilitate robust imitation learning. We validate our method in simulation and on hardware, demonstrating challenging motions for morphologies that differ significantly from a human, including retargeting onto a quadruped.

## 参考
- http://arxiv.org/abs/2605.06593v1

