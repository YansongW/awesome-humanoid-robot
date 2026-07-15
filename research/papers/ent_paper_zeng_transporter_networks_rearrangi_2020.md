---
$id: ent_paper_zeng_transporter_networks_rearrangi_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Transporter Networks: Rearranging the Visual World for Robotic Manipulation'
  zh: Transporter Networks
  ko: 'Transporter Networks: Rearranging the Visual World for Robotic Manipulation'
summary:
  en: 'Transporter Networks: Rearranging the Visual World for Robotic Manipulation (Transporter Networks), is a 2020 generalized
    vision-language-action model for robotic manipulation, introduced by Robotics at Google, and published at CoRL 2020.'
  zh: 'Transporter Networks: Rearranging the Visual World for Robotic Manipulation (Transporter Networks), is a 2020 generalized
    vision-language-action model for robotic manipulation, introduced by Robotics at Google, and published at CoRL 2020.'
  ko: 'Transporter Networks: Rearranging the Visual World for Robotic Manipulation (Transporter Networks), is a 2020 generalized
    vision-language-action model for robotic manipulation, introduced by Robotics at Google, and published at CoRL 2020.'
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
- transporter_networks
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2010.14406v3.
sources:
- id: src_001
  type: paper
  title: Transporter Networks source
  url: https://proceedings.mlr.press/v155/zeng21a.html
  date: '2020'
  accessed_at: '2026-07-01'
---
## 概述
Robotic manipulation can be formulated as inducing a sequence of spatial displacements: where the space being moved can encompass an object, part of an object, or end effector. In this work, we propose the Transporter Network, a simple model architecture that rearranges deep features to infer spatial displacements from visual input - which can parameterize robot actions. It makes no assumptions of objectness (e.g. canonical poses, models, or keypoints), it exploits spatial symmetries, and is orders of magnitude more sample efficient than our benchmarked alternatives in learning vision-based manipulation tasks: from stacking a pyramid of blocks, to assembling kits with unseen objects; from manipulating deformable ropes, to pushing piles of small objects with closed-loop feedback. Our method can represent complex multi-modal policy distributions and generalizes to multi-step sequential tasks, as well as 6DoF pick-and-place. Experiments on 10 simulated tasks show that it learns faster and generalizes better than a variety of end-to-end baselines, including policies that use ground-truth object poses. We validate our methods with hardware in the real world. Experiment videos and code are available at https://transporternets.github.io

## 核心内容
Robotic manipulation can be formulated as inducing a sequence of spatial displacements: where the space being moved can encompass an object, part of an object, or end effector. In this work, we propose the Transporter Network, a simple model architecture that rearranges deep features to infer spatial displacements from visual input - which can parameterize robot actions. It makes no assumptions of objectness (e.g. canonical poses, models, or keypoints), it exploits spatial symmetries, and is orders of magnitude more sample efficient than our benchmarked alternatives in learning vision-based manipulation tasks: from stacking a pyramid of blocks, to assembling kits with unseen objects; from manipulating deformable ropes, to pushing piles of small objects with closed-loop feedback. Our method can represent complex multi-modal policy distributions and generalizes to multi-step sequential tasks, as well as 6DoF pick-and-place. Experiments on 10 simulated tasks show that it learns faster and generalizes better than a variety of end-to-end baselines, including policies that use ground-truth object poses. We validate our methods with hardware in the real world. Experiment videos and code are available at https://transporternets.github.io

## 参考
- http://arxiv.org/abs/2010.14406v3

