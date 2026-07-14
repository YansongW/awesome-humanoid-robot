---
$id: ent_paper_dreamdojo_a_generalist_robot_w_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos'
  zh: 世界模型开始变成机器人策略的试验场
  ko: 'DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos'
summary:
  en: 'DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos is a knowledge node related to paper in the
    humanoid robot value chain.'
  zh: 'Being able to simulate the outcomes of actions in varied environments will revolutionize the development of generalist
    agents at scale. However, modeling these world dynamics, especially for dexterous robotics tasks, poses significant challenges
    due to limited data coverage and scarce action labels. As an endeavor towards this end, we introduce DreamDojo, a foundation
    world model that learns diverse interactions and dexterous controls from 44k hours of egocentric human videos. Our data
    mixture represents the largest video dataset to date for world model pretraining, spanning a wide range of daily scenarios
    with diverse objects and skills. To address the scarcity of action labels, we introduce continuous latent actions as unified
    proxy actions, enhancing interaction knowledge transfer from '
  ko: 'DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos is a knowledge node related to paper in the
    humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- compliance
- contact_rich
- fall_recovery
- load_carrying
- safety
- whole_body_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.06949v1.
sources:
- id: src_001
  type: paper
  title: 'DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos (arXiv)'
  url: https://arxiv.org/abs/2602.06949
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 世界模型开始变成机器人策略的试验场 project page
  url: https://dreamdojo-world.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Being able to simulate the outcomes of actions in varied environments will revolutionize the development of generalist agents at scale. However, modeling these world dynamics, especially for dexterous robotics tasks, poses significant challenges due to limited data coverage and scarce action labels. As an endeavor towards this end, we introduce DreamDojo, a foundation world model that learns diverse interactions and dexterous controls from 44k hours of egocentric human videos. Our data mixture represents the largest video dataset to date for world model pretraining, spanning a wide range of daily scenarios with diverse objects and skills. To address the scarcity of action labels, we introduce continuous latent actions as unified proxy actions, enhancing interaction knowledge transfer from unlabeled videos. After post-training on small-scale target robot data, DreamDojo demonstrates a strong understanding of physics and precise action controllability. We also devise a distillation pipeline that accelerates DreamDojo to a real-time speed of 10.81 FPS and further improves context consistency. Our work enables several important applications based on generative world models, including live teleoperation, policy evaluation, and model-based planning. Systematic evaluation on multiple challenging out-of-distribution (OOD) benchmarks verifies the significance of our method for simulating open-world, contact-rich tasks, paving the way for general-purpose robot world models.

## 核心内容
Being able to simulate the outcomes of actions in varied environments will revolutionize the development of generalist agents at scale. However, modeling these world dynamics, especially for dexterous robotics tasks, poses significant challenges due to limited data coverage and scarce action labels. As an endeavor towards this end, we introduce DreamDojo, a foundation world model that learns diverse interactions and dexterous controls from 44k hours of egocentric human videos. Our data mixture represents the largest video dataset to date for world model pretraining, spanning a wide range of daily scenarios with diverse objects and skills. To address the scarcity of action labels, we introduce continuous latent actions as unified proxy actions, enhancing interaction knowledge transfer from unlabeled videos. After post-training on small-scale target robot data, DreamDojo demonstrates a strong understanding of physics and precise action controllability. We also devise a distillation pipeline that accelerates DreamDojo to a real-time speed of 10.81 FPS and further improves context consistency. Our work enables several important applications based on generative world models, including live teleoperation, policy evaluation, and model-based planning. Systematic evaluation on multiple challenging out-of-distribution (OOD) benchmarks verifies the significance of our method for simulating open-world, contact-rich tasks, paving the way for general-purpose robot world models.

## 参考
- http://arxiv.org/abs/2602.06949v1

