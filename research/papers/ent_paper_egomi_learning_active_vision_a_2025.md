---
$id: ent_paper_egomi_learning_active_vision_a_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoMI: Learning Active Vision and Whole-Body Manipulation from Egocentric Human Demonstrations'
  zh: 'EgoMI: Learning Active Vision and Whole-Body Manipulation from Egocentric Human Demonstrations'
  ko: 'EgoMI: Learning Active Vision and Whole-Body Manipulation from Egocentric Human Demonstrations'
summary:
  en: 'EgoMI: Learning Active Vision and Whole-Body Manipulation from Egocentric Human Demonstrations is a 2025 work on manipulation
    for humanoid robots.'
  zh: 'EgoMI: Learning Active Vision and Whole-Body Manipulation from Egocentric Human Demonstrations is a 2025 work on manipulation
    for humanoid robots.'
  ko: 'EgoMI: Learning Active Vision and Whole-Body Manipulation from Egocentric Human Demonstrations is a 2025 work on manipulation
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
- egomi
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.00153v2.
sources:
- id: src_001
  type: paper
  title: 'EgoMI: Learning Active Vision and Whole-Body Manipulation from Egocentric Human Demonstrations (arXiv)'
  url: https://arxiv.org/abs/2511.00153
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Imitation learning from human demonstrations offers a promising approach for robot skill acquisition, but egocentric human data introduces fundamental challenges due to the embodiment gap. During manipulation, humans actively coordinate head and hand movements, continuously reposition their viewpoint and use pre-action visual fixation search strategies to locate relevant objects. These behaviors create dynamic, task-driven head motions that static robot sensing systems cannot replicate, leading to a significant distribution shift that degrades policy performance. We present EgoMI (Egocentric Manipulation Interface), a framework that captures synchronized end-effector and active head trajectories during manipulation tasks, resulting in data that can be retargeted to compatible semi-humanoid robot embodiments. To handle rapid and wide-spanning head viewpoint changes, we introduce a memory-augmented policy that selectively incorporates historical observations. We evaluate our approach on a bimanual robot equipped with an actuated camera head and find that policies with explicit head-motion modeling consistently outperform baseline methods. Results suggest that coordinated hand-eye learning with EgoMI effectively bridges the human-robot embodiment gap for robust imitation learning on semi-humanoid embodiments. Project page: https://egocentric-manipulation-interface.github.io

## 核心内容
Imitation learning from human demonstrations offers a promising approach for robot skill acquisition, but egocentric human data introduces fundamental challenges due to the embodiment gap. During manipulation, humans actively coordinate head and hand movements, continuously reposition their viewpoint and use pre-action visual fixation search strategies to locate relevant objects. These behaviors create dynamic, task-driven head motions that static robot sensing systems cannot replicate, leading to a significant distribution shift that degrades policy performance. We present EgoMI (Egocentric Manipulation Interface), a framework that captures synchronized end-effector and active head trajectories during manipulation tasks, resulting in data that can be retargeted to compatible semi-humanoid robot embodiments. To handle rapid and wide-spanning head viewpoint changes, we introduce a memory-augmented policy that selectively incorporates historical observations. We evaluate our approach on a bimanual robot equipped with an actuated camera head and find that policies with explicit head-motion modeling consistently outperform baseline methods. Results suggest that coordinated hand-eye learning with EgoMI effectively bridges the human-robot embodiment gap for robust imitation learning on semi-humanoid embodiments. Project page: https://egocentric-manipulation-interface.github.io

## 参考
- http://arxiv.org/abs/2511.00153v2

