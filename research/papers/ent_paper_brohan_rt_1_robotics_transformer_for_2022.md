---
$id: ent_paper_brohan_rt_1_robotics_transformer_for_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RT-1: Robotics Transformer for Real-World Control at Scale'
  zh: RT-1
  ko: 'RT-1: Robotics Transformer for Real-World Control at Scale'
summary:
  en: 'RT-1: Robotics Transformer for Real-World Control at Scale (RT-1), is a 2022 generalized vision-language-action model
    for robotic manipulation, introduced by Robotics at Google, Everyday Robots, Google Research, Brain Team, and published
    at Robotics - Science and Systems 2022.'
  zh: 'RT-1: Robotics Transformer for Real-World Control at Scale (RT-1), is a 2022 generalized vision-language-action model
    for robotic manipulation, introduced by Robotics at Google, Everyday Robots, Google Research, Brain Team, and published
    at Robotics - Science and Systems 2022.'
  ko: 'RT-1: Robotics Transformer for Real-World Control at Scale (RT-1), is a 2022 generalized vision-language-action model
    for robotic manipulation, introduced by Robotics at Google, Everyday Robots, Google Research, Brain Team, and published
    at Robotics - Science and Systems 2022.'
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
- robotic_manipulation
- rt_1
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2212.06817v2.
sources:
- id: src_001
  type: website
  title: RT-1 source
  url: https://doi.org/10.15607/RSS.2023.XIX.025
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
By transferring knowledge from large, diverse, task-agnostic datasets, modern machine learning models can solve specific downstream tasks either zero-shot or with small task-specific datasets to a high level of performance. While this capability has been demonstrated in other fields such as computer vision, natural language processing or speech recognition, it remains to be shown in robotics, where the generalization capabilities of the models are particularly critical due to the difficulty of collecting real-world robotic data. We argue that one of the keys to the success of such general robotic models lies with open-ended task-agnostic training, combined with high-capacity architectures that can absorb all of the diverse, robotic data. In this paper, we present a model class, dubbed Robotics Transformer, that exhibits promising scalable model properties. We verify our conclusions in a study of different model classes and their ability to generalize as a function of the data size, model size, and data diversity based on a large-scale data collection on real robots performing real-world tasks. The project's website and videos can be found at robotics-transformer1.github.io

## 核心内容
By transferring knowledge from large, diverse, task-agnostic datasets, modern machine learning models can solve specific downstream tasks either zero-shot or with small task-specific datasets to a high level of performance. While this capability has been demonstrated in other fields such as computer vision, natural language processing or speech recognition, it remains to be shown in robotics, where the generalization capabilities of the models are particularly critical due to the difficulty of collecting real-world robotic data. We argue that one of the keys to the success of such general robotic models lies with open-ended task-agnostic training, combined with high-capacity architectures that can absorb all of the diverse, robotic data. In this paper, we present a model class, dubbed Robotics Transformer, that exhibits promising scalable model properties. We verify our conclusions in a study of different model classes and their ability to generalize as a function of the data size, model size, and data diversity based on a large-scale data collection on real robots performing real-world tasks. The project's website and videos can be found at robotics-transformer1.github.io

## 参考
- http://arxiv.org/abs/2212.06817v2

