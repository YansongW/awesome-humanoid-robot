---
$id: ent_paper_shridhar_perceiver_actor_a_multi_task_t_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation'
  zh: PerAct
  ko: 'Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation'
summary:
  en: 'Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation (PerAct), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by University of Washington, NVIDIA, and published at CoRL 2022.'
  zh: 'Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation (PerAct), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by University of Washington, NVIDIA, and published at CoRL 2022.'
  ko: 'Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation (PerAct), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by University of Washington, NVIDIA, and published at CoRL 2022.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- peract
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2209.05451v2.
sources:
- id: src_001
  type: paper
  title: PerAct source
  url: https://proceedings.mlr.press/v205/shridhar23a.html
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
Transformers have revolutionized vision and natural language processing with their ability to scale with large datasets. But in robotic manipulation, data is both limited and expensive. Can manipulation still benefit from Transformers with the right problem formulation? We investigate this question with PerAct, a language-conditioned behavior-cloning agent for multi-task 6-DoF manipulation. PerAct encodes language goals and RGB-D voxel observations with a Perceiver Transformer, and outputs discretized actions by ``detecting the next best voxel action''. Unlike frameworks that operate on 2D images, the voxelized 3D observation and action space provides a strong structural prior for efficiently learning 6-DoF actions. With this formulation, we train a single multi-task Transformer for 18 RLBench tasks (with 249 variations) and 7 real-world tasks (with 18 variations) from just a few demonstrations per task. Our results show that PerAct significantly outperforms unstructured image-to-action agents and 3D ConvNet baselines for a wide range of tabletop tasks.

## 核心内容
Transformers have revolutionized vision and natural language processing with their ability to scale with large datasets. But in robotic manipulation, data is both limited and expensive. Can manipulation still benefit from Transformers with the right problem formulation? We investigate this question with PerAct, a language-conditioned behavior-cloning agent for multi-task 6-DoF manipulation. PerAct encodes language goals and RGB-D voxel observations with a Perceiver Transformer, and outputs discretized actions by ``detecting the next best voxel action''. Unlike frameworks that operate on 2D images, the voxelized 3D observation and action space provides a strong structural prior for efficiently learning 6-DoF actions. With this formulation, we train a single multi-task Transformer for 18 RLBench tasks (with 249 variations) and 7 real-world tasks (with 18 variations) from just a few demonstrations per task. Our results show that PerAct significantly outperforms unstructured image-to-action agents and 3D ConvNet baselines for a wide range of tabletop tasks.

## 参考
- http://arxiv.org/abs/2209.05451v2

