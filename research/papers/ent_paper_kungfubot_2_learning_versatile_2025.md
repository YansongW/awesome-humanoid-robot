---
$id: ent_paper_kungfubot_2_learning_versatile_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'KungfuBot 2: Learning Versatile Motion Skills for Humanoid Whole-Body Control'
  zh: 'KungfuBot 2: Learning Versatile Motion Skills for Humanoid Whole-Body Control'
  ko: 'KungfuBot 2: Learning Versatile Motion Skills for Humanoid Whole-Body Control'
summary:
  en: 'KungfuBot 2: Learning Versatile Motion Skills for Humanoid Whole-Body Control is a 2025 work on loco-manipulation and
    whole-body-control for humanoid robots.'
  zh: 'KungfuBot 2: Learning Versatile Motion Skills for Humanoid Whole-Body Control is a 2025 work on loco-manipulation and
    whole-body-control for humanoid robots.'
  ko: 'KungfuBot 2: Learning Versatile Motion Skills for Humanoid Whole-Body Control is a 2025 work on loco-manipulation and
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
- kungfubot_2
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.16638v1.
sources:
- id: src_001
  type: paper
  title: 'KungfuBot 2: Learning Versatile Motion Skills for Humanoid Whole-Body Control (arXiv)'
  url: https://arxiv.org/abs/2509.16638
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Learning versatile whole-body skills by tracking various human motions is a fundamental step toward general-purpose humanoid robots. This task is particularly challenging because a single policy must master a broad repertoire of motion skills while ensuring stability over long-horizon sequences. To this end, we present VMS, a unified whole-body controller that enables humanoid robots to learn diverse and dynamic behaviors within a single policy. Our framework integrates a hybrid tracking objective that balances local motion fidelity with global trajectory consistency, and an Orthogonal Mixture-of-Experts (OMoE) architecture that encourages skill specialization while enhancing generalization across motions. A segment-level tracking reward is further introduced to relax rigid step-wise matching, enhancing robustness when handling global displacements and transient inaccuracies. We validate VMS extensively in both simulation and real-world experiments, demonstrating accurate imitation of dynamic skills, stable performance over minute-long sequences, and strong generalization to unseen motions. These results highlight the potential of VMS as a scalable foundation for versatile humanoid whole-body control. The project page is available at https://kungfubot2-humanoid.github.io.

## 核心内容
Learning versatile whole-body skills by tracking various human motions is a fundamental step toward general-purpose humanoid robots. This task is particularly challenging because a single policy must master a broad repertoire of motion skills while ensuring stability over long-horizon sequences. To this end, we present VMS, a unified whole-body controller that enables humanoid robots to learn diverse and dynamic behaviors within a single policy. Our framework integrates a hybrid tracking objective that balances local motion fidelity with global trajectory consistency, and an Orthogonal Mixture-of-Experts (OMoE) architecture that encourages skill specialization while enhancing generalization across motions. A segment-level tracking reward is further introduced to relax rigid step-wise matching, enhancing robustness when handling global displacements and transient inaccuracies. We validate VMS extensively in both simulation and real-world experiments, demonstrating accurate imitation of dynamic skills, stable performance over minute-long sequences, and strong generalization to unseen motions. These results highlight the potential of VMS as a scalable foundation for versatile humanoid whole-body control. The project page is available at https://kungfubot2-humanoid.github.io.

## 参考
- http://arxiv.org/abs/2509.16638v1

