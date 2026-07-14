---
$id: ent_paper_humanoid_parkour_learning_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Humanoid Parkour Learning
  zh: Humanoid Parkour Learning
  ko: Humanoid Parkour Learning
summary:
  en: Humanoid Parkour Learning is a 2024 work on locomotion for humanoid robots.
  zh: Humanoid Parkour Learning is a 2024 work on locomotion for humanoid robots.
  ko: Humanoid Parkour Learning is a 2024 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- humanoid_parkour_learning
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.10759v2.
sources:
- id: src_001
  type: paper
  title: Humanoid Parkour Learning (arXiv)
  url: https://arxiv.org/abs/2406.10759
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Humanoid Parkour Learning project page
  url: https://humanoid4parkour.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Parkour is a grand challenge for legged locomotion, even for quadruped robots, requiring active perception and various maneuvers to overcome multiple challenging obstacles. Existing methods for humanoid locomotion either optimize a trajectory for a single parkour track or train a reinforcement learning policy only to walk with a significant amount of motion references. In this work, we propose a framework for learning an end-to-end vision-based whole-body-control parkour policy for humanoid robots that overcomes multiple parkour skills without any motion prior. Using the parkour policy, the humanoid robot can jump on a 0.42m platform, leap over hurdles, 0.8m gaps, and much more. It can also run at 1.8m/s in the wild and walk robustly on different terrains. We test our policy in indoor and outdoor environments to demonstrate that it can autonomously select parkour skills while following the rotation command of the joystick. We override the arm actions and show that this framework can easily transfer to humanoid mobile manipulation tasks. Videos can be found at https://humanoid4parkour.github.io

## 核心内容
Parkour is a grand challenge for legged locomotion, even for quadruped robots, requiring active perception and various maneuvers to overcome multiple challenging obstacles. Existing methods for humanoid locomotion either optimize a trajectory for a single parkour track or train a reinforcement learning policy only to walk with a significant amount of motion references. In this work, we propose a framework for learning an end-to-end vision-based whole-body-control parkour policy for humanoid robots that overcomes multiple parkour skills without any motion prior. Using the parkour policy, the humanoid robot can jump on a 0.42m platform, leap over hurdles, 0.8m gaps, and much more. It can also run at 1.8m/s in the wild and walk robustly on different terrains. We test our policy in indoor and outdoor environments to demonstrate that it can autonomously select parkour skills while following the rotation command of the joystick. We override the arm actions and show that this framework can easily transfer to humanoid mobile manipulation tasks. Videos can be found at https://humanoid4parkour.github.io

## 参考
- http://arxiv.org/abs/2406.10759v2

