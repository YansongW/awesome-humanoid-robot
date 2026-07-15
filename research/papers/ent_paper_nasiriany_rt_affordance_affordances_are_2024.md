---
$id: ent_paper_nasiriany_rt_affordance_affordances_are_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation'
  zh: RT-A
  ko: 'RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation'
summary:
  en: 'RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation (RT-A), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, The University of Austin at Texas,
    and published at ICRA25.'
  zh: 'RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation (RT-A), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, The University of Austin at Texas,
    and published at ICRA25.'
  ko: 'RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation (RT-A), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, The University of Austin at Texas,
    and published at ICRA25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- rt_a
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.02704v1.
sources:
- id: src_001
  type: website
  title: RT-A source
  url: https://doi.org/10.1109/ICRA55743.2025.11127525
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
We explore how intermediate policy representations can facilitate generalization by providing guidance on how to perform manipulation tasks. Existing representations such as language, goal images, and trajectory sketches have been shown to be helpful, but these representations either do not provide enough context or provide over-specified context that yields less robust policies. We propose conditioning policies on affordances, which capture the pose of the robot at key stages of the task. Affordances offer expressive yet lightweight abstractions, are easy for users to specify, and facilitate efficient learning by transferring knowledge from large internet datasets. Our method, RT-Affordance, is a hierarchical model that first proposes an affordance plan given the task language, and then conditions the policy on this affordance plan to perform manipulation. Our model can flexibly bridge heterogeneous sources of supervision including large web datasets and robot trajectories. We additionally train our model on cheap-to-collect in-domain affordance images, allowing us to learn new tasks without collecting any additional costly robot trajectories. We show on a diverse set of novel tasks how RT-Affordance exceeds the performance of existing methods by over 50%, and we empirically demonstrate that affordances are robust to novel settings. Videos available at https://snasiriany.me/rt-affordance

## 核心内容
We explore how intermediate policy representations can facilitate generalization by providing guidance on how to perform manipulation tasks. Existing representations such as language, goal images, and trajectory sketches have been shown to be helpful, but these representations either do not provide enough context or provide over-specified context that yields less robust policies. We propose conditioning policies on affordances, which capture the pose of the robot at key stages of the task. Affordances offer expressive yet lightweight abstractions, are easy for users to specify, and facilitate efficient learning by transferring knowledge from large internet datasets. Our method, RT-Affordance, is a hierarchical model that first proposes an affordance plan given the task language, and then conditions the policy on this affordance plan to perform manipulation. Our model can flexibly bridge heterogeneous sources of supervision including large web datasets and robot trajectories. We additionally train our model on cheap-to-collect in-domain affordance images, allowing us to learn new tasks without collecting any additional costly robot trajectories. We show on a diverse set of novel tasks how RT-Affordance exceeds the performance of existing methods by over 50%, and we empirically demonstrate that affordances are robust to novel settings. Videos available at https://snasiriany.me/rt-affordance

## 参考
- http://arxiv.org/abs/2411.02704v1

