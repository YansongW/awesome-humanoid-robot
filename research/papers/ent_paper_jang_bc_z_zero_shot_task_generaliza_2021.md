---
$id: ent_paper_jang_bc_z_zero_shot_task_generaliza_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning'
  zh: BC-Z
  ko: 'BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning'
summary:
  en: 'BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning (BC-Z), is a 2021 generalized vision-language-action
    model for robotic manipulation, introduced by UC Berkeley, Stanford University, and published at CoRL 2021.'
  zh: 'BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning (BC-Z), is a 2021 generalized vision-language-action
    model for robotic manipulation, introduced by UC Berkeley, Stanford University, and published at CoRL 2021.'
  ko: 'BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning (BC-Z), is a 2021 generalized vision-language-action
    model for robotic manipulation, introduced by UC Berkeley, Stanford University, and published at CoRL 2021.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- bc_z
- generalist_policy
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: BC-Z: Zero-Shot Task Generalization
    with Robotic Imitation Learning.'
sources:
- id: src_001
  type: paper
  title: BC-Z source
  url: https://proceedings.mlr.press/v164/jang22a.html
  date: '2021'
  accessed_at: '2026-07-01'
---
## 概述
In this paper, we study the problem of enabling a vision-based robotic manipulation system to generalize to novel tasks, a long-standing challenge in robot learning. We approach the challenge from an imitation learning perspective, aiming to study how scaling and broadening the data collected can facilitate such generalization. To that end, we develop an interactive and flexible imitation learning system that can learn from both demonstrations and interventions and can be conditioned on different forms of information that convey the task, including pre-trained embeddings of natural language or videos of humans performing the task. When scaling data collection on a real robot to more than 100 distinct tasks, we find that this system can perform 24 unseen manipulation tasks with an average success rate of 44%, without any robot demonstrations for those tasks.

## 核心内容
In this paper, we study the problem of enabling a vision-based robotic manipulation system to generalize to novel tasks, a long-standing challenge in robot learning. We approach the challenge from an imitation learning perspective, aiming to study how scaling and broadening the data collected can facilitate such generalization. To that end, we develop an interactive and flexible imitation learning system that can learn from both demonstrations and interventions and can be conditioned on different forms of information that convey the task, including pre-trained embeddings of natural language or videos of humans performing the task. When scaling data collection on a real robot to more than 100 distinct tasks, we find that this system can perform 24 unseen manipulation tasks with an average success rate of 44%, without any robot demonstrations for those tasks.

## 参考
- Semantic Scholar search: BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning

