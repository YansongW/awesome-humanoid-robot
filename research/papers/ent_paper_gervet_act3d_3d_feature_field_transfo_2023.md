---
$id: ent_paper_gervet_act3d_3d_feature_field_transfo_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Act3D: 3D Feature Field Transformers for Multi-Task Robotic Manipulation'
  zh: Act3D
  ko: 'Act3D: 3D Feature Field Transformers for Multi-Task Robotic Manipulation'
summary:
  en: 'Act3D: 3D Feature Field Transformers for Multi-Task Robotic Manipulation (Act3D), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, and published at CoRL 2023.'
  zh: 'Act3D: 3D Feature Field Transformers for Multi-Task Robotic Manipulation (Act3D), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, and published at CoRL 2023.'
  ko: 'Act3D: 3D Feature Field Transformers for Multi-Task Robotic Manipulation (Act3D), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, and published at CoRL 2023.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- act3d
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2306.17817v2.
sources:
- id: src_001
  type: paper
  title: Act3D source
  url: https://proceedings.mlr.press/v229/gervet23a.html
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
3D perceptual representations are well suited for robot manipulation as they easily encode occlusions and simplify spatial reasoning. Many manipulation tasks require high spatial precision in end-effector pose prediction, which typically demands high-resolution 3D feature grids that are computationally expensive to process. As a result, most manipulation policies operate directly in 2D, foregoing 3D inductive biases. In this paper, we introduce Act3D, a manipulation policy transformer that represents the robot's workspace using a 3D feature field with adaptive resolutions dependent on the task at hand. The model lifts 2D pre-trained features to 3D using sensed depth, and attends to them to compute features for sampled 3D points. It samples 3D point grids in a coarse to fine manner, featurizes them using relative-position attention, and selects where to focus the next round of point sampling. In this way, it efficiently computes 3D action maps of high spatial resolution. Act3D sets a new state-of-the-art in RL-Bench, an established manipulation benchmark, where it achieves 10% absolute improvement over the previous SOTA 2D multi-view policy on 74 RLBench tasks and 22% absolute improvement with 3x less compute over the previous SOTA 3D policy. We quantify the importance of relative spatial attention, large-scale vision-language pre-trained 2D backbones, and weight tying across coarse-to-fine attentions in ablative experiments. Code and videos are available on our project website: https://act3d.github.io/.

## 核心内容
3D perceptual representations are well suited for robot manipulation as they easily encode occlusions and simplify spatial reasoning. Many manipulation tasks require high spatial precision in end-effector pose prediction, which typically demands high-resolution 3D feature grids that are computationally expensive to process. As a result, most manipulation policies operate directly in 2D, foregoing 3D inductive biases. In this paper, we introduce Act3D, a manipulation policy transformer that represents the robot's workspace using a 3D feature field with adaptive resolutions dependent on the task at hand. The model lifts 2D pre-trained features to 3D using sensed depth, and attends to them to compute features for sampled 3D points. It samples 3D point grids in a coarse to fine manner, featurizes them using relative-position attention, and selects where to focus the next round of point sampling. In this way, it efficiently computes 3D action maps of high spatial resolution. Act3D sets a new state-of-the-art in RL-Bench, an established manipulation benchmark, where it achieves 10% absolute improvement over the previous SOTA 2D multi-view policy on 74 RLBench tasks and 22% absolute improvement with 3x less compute over the previous SOTA 3D policy. We quantify the importance of relative spatial attention, large-scale vision-language pre-trained 2D backbones, and weight tying across coarse-to-fine attentions in ablative experiments. Code and videos are available on our project website: https://act3d.github.io/.

## 参考
- http://arxiv.org/abs/2306.17817v2

