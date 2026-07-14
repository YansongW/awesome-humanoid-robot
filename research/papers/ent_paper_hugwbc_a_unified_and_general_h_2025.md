---
$id: ent_paper_hugwbc_a_unified_and_general_h_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HugWBC: A Unified and General Humanoid Whole-Body Controller'
  zh: 'HugWBC: A Unified and General Humanoid Whole-Body Controller'
  ko: 'HugWBC: A Unified and General Humanoid Whole-Body Controller'
summary:
  en: 'HugWBC: A Unified and General Humanoid Whole-Body Controller is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: 'HugWBC: A Unified and General Humanoid Whole-Body Controller is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  ko: 'HugWBC: A Unified and General Humanoid Whole-Body Controller is a 2025 work on loco-manipulation and whole-body-control
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
- hugwbc
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.03206v3.
sources:
- id: src_001
  type: paper
  title: 'HugWBC: A Unified and General Humanoid Whole-Body Controller (arXiv)'
  url: https://arxiv.org/abs/2502.03206
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Locomotion is a fundamental skill for humanoid robots. However, most existing works make locomotion a single, tedious, unextendable, and unconstrained movement. This limits the kinematic capabilities of humanoid robots. In contrast, humans possess versatile athletic abilities-running, jumping, hopping, and finely adjusting gait parameters such as frequency and foot height. In this paper, we investigate solutions to bring such versatility into humanoid locomotion and thereby propose HugWBC: a unified and general humanoid whole-body controller for versatile locomotion. By designing a general command space in the aspect of tasks and behaviors, along with advanced techniques like symmetrical loss and intervention training for learning a whole-body humanoid controlling policy in simulation, HugWBC enables real-world humanoid robots to produce various natural gaits, including walking, jumping, standing, and hopping, with customizable parameters such as frequency, foot swing height, further combined with different body height, waist rotation, and body pitch. Beyond locomotion, HugWBC also supports real-time interventions from external upper-body controllers like teleoperation, enabling loco-manipulation with precision under any locomotive behavior. Extensive experiments validate the high tracking accuracy and robustness of HugWBC with/without upper-body intervention for all commands, and we further provide an in-depth analysis of how the various commands affect humanoid movement and offer insights into the relationships between these commands. To our knowledge, HugWBC is the first humanoid whole-body controller that supports such versatile locomotion behaviors with high robustness and flexibility.

## 核心内容
Locomotion is a fundamental skill for humanoid robots. However, most existing works make locomotion a single, tedious, unextendable, and unconstrained movement. This limits the kinematic capabilities of humanoid robots. In contrast, humans possess versatile athletic abilities-running, jumping, hopping, and finely adjusting gait parameters such as frequency and foot height. In this paper, we investigate solutions to bring such versatility into humanoid locomotion and thereby propose HugWBC: a unified and general humanoid whole-body controller for versatile locomotion. By designing a general command space in the aspect of tasks and behaviors, along with advanced techniques like symmetrical loss and intervention training for learning a whole-body humanoid controlling policy in simulation, HugWBC enables real-world humanoid robots to produce various natural gaits, including walking, jumping, standing, and hopping, with customizable parameters such as frequency, foot swing height, further combined with different body height, waist rotation, and body pitch. Beyond locomotion, HugWBC also supports real-time interventions from external upper-body controllers like teleoperation, enabling loco-manipulation with precision under any locomotive behavior. Extensive experiments validate the high tracking accuracy and robustness of HugWBC with/without upper-body intervention for all commands, and we further provide an in-depth analysis of how the various commands affect humanoid movement and offer insights into the relationships between these commands. To our knowledge, HugWBC is the first humanoid whole-body controller that supports such versatile locomotion behaviors with high robustness and flexibility.

## 参考
- http://arxiv.org/abs/2502.03206v3

