---
$id: ent_paper_hub_learning_extreme_humanoid_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HuB: Learning Extreme Humanoid Balance'
  zh: 'HuB: Learning Extreme Humanoid Balance'
  ko: 'HuB: Learning Extreme Humanoid Balance'
summary:
  en: 'HuB: Learning Extreme Humanoid Balance is a 2025 work on loco-manipulation and whole-body-control for humanoid robots.'
  zh: 'HuB: Learning Extreme Humanoid Balance is a 2025 work on loco-manipulation and whole-body-control for humanoid robots.'
  ko: 'HuB: Learning Extreme Humanoid Balance is a 2025 work on loco-manipulation and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hub
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.07294v2.
sources:
- id: src_001
  type: paper
  title: 'HuB: Learning Extreme Humanoid Balance (arXiv)'
  url: https://arxiv.org/abs/2505.07294
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'HuB: Learning Extreme Humanoid Balance project page'
  url: https://hub-robot.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The human body demonstrates exceptional motor capabilities-such as standing steadily on one foot or performing a high kick with the leg raised over 1.5 meters-both requiring precise balance control. While recent research on humanoid control has leveraged reinforcement learning to track human motions for skill acquisition, applying this paradigm to balance-intensive tasks remains challenging. In this work, we identify three key obstacles: instability from reference motion errors, learning difficulties due to morphological mismatch, and the sim-to-real gap caused by sensor noise and unmodeled dynamics. To address these challenges, we propose HuB (Humanoid Balance), a unified framework that integrates reference motion refinement, balance-aware policy learning, and sim-to-real robustness training, with each component targeting a specific challenge. We validate our approach on the Unitree G1 humanoid robot across challenging quasi-static balance tasks, including extreme single-legged poses such as Swallow Balance and Bruce Lee's Kick. Our policy remains stable even under strong physical disturbances-such as a forceful soccer strike-while baseline methods consistently fail to complete these tasks. Project website: https://hub-robot.github.io

## 核心内容
The human body demonstrates exceptional motor capabilities-such as standing steadily on one foot or performing a high kick with the leg raised over 1.5 meters-both requiring precise balance control. While recent research on humanoid control has leveraged reinforcement learning to track human motions for skill acquisition, applying this paradigm to balance-intensive tasks remains challenging. In this work, we identify three key obstacles: instability from reference motion errors, learning difficulties due to morphological mismatch, and the sim-to-real gap caused by sensor noise and unmodeled dynamics. To address these challenges, we propose HuB (Humanoid Balance), a unified framework that integrates reference motion refinement, balance-aware policy learning, and sim-to-real robustness training, with each component targeting a specific challenge. We validate our approach on the Unitree G1 humanoid robot across challenging quasi-static balance tasks, including extreme single-legged poses such as Swallow Balance and Bruce Lee's Kick. Our policy remains stable even under strong physical disturbances-such as a forceful soccer strike-while baseline methods consistently fail to complete these tasks. Project website: https://hub-robot.github.io

## 参考
- http://arxiv.org/abs/2505.07294v2

