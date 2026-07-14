---
$id: ent_paper_softmimic_learning_compliant_w_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SoftMimic: Learning Compliant Whole-body Control from Examples'
  zh: 'SoftMimic: Learning Compliant Whole-body Control from Examples'
  ko: 'SoftMimic: Learning Compliant Whole-body Control from Examples'
summary:
  en: 'SoftMimic: Learning Compliant Whole-body Control from Examples is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: 'SoftMimic: Learning Compliant Whole-body Control from Examples is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  ko: 'SoftMimic: Learning Compliant Whole-body Control from Examples is a 2025 work on loco-manipulation and whole-body-control
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
- softmimic
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.17792v1.
sources:
- id: src_001
  type: paper
  title: 'SoftMimic: Learning Compliant Whole-body Control from Examples (arXiv)'
  url: https://arxiv.org/abs/2510.17792
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We introduce SoftMimic, a framework for learning compliant whole-body control policies for humanoid robots from example motions. Imitating human motions with reinforcement learning allows humanoids to quickly learn new skills, but existing methods incentivize stiff control that aggressively corrects deviations from a reference motion, leading to brittle and unsafe behavior when the robot encounters unexpected contacts. In contrast, SoftMimic enables robots to respond compliantly to external forces while maintaining balance and posture. Our approach leverages an inverse kinematics solver to generate an augmented dataset of feasible compliant motions, which we use to train a reinforcement learning policy. By rewarding the policy for matching compliant responses rather than rigidly tracking the reference motion, SoftMimic learns to absorb disturbances and generalize to varied tasks from a single motion clip. We validate our method through simulations and real-world experiments, demonstrating safe and effective interaction with the environment.

## 核心内容
We introduce SoftMimic, a framework for learning compliant whole-body control policies for humanoid robots from example motions. Imitating human motions with reinforcement learning allows humanoids to quickly learn new skills, but existing methods incentivize stiff control that aggressively corrects deviations from a reference motion, leading to brittle and unsafe behavior when the robot encounters unexpected contacts. In contrast, SoftMimic enables robots to respond compliantly to external forces while maintaining balance and posture. Our approach leverages an inverse kinematics solver to generate an augmented dataset of feasible compliant motions, which we use to train a reinforcement learning policy. By rewarding the policy for matching compliant responses rather than rigidly tracking the reference motion, SoftMimic learns to absorb disturbances and generalize to varied tasks from a single motion clip. We validate our method through simulations and real-world experiments, demonstrating safe and effective interaction with the environment.

## 参考
- http://arxiv.org/abs/2510.17792v1

