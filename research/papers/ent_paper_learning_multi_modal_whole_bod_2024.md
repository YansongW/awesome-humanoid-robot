---
$id: ent_paper_learning_multi_modal_whole_bod_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots
  zh: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots
  ko: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots
summary:
  en: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots is a 2024 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots is a 2024 work on loco-manipulation and whole-body-control
    for humanoid robots.
  ko: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots is a 2024 work on loco-manipulation and whole-body-control
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_multi_modal_whole_bod
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2408.07295v4.
sources:
- id: src_001
  type: paper
  title: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots (arXiv)
  url: https://arxiv.org/abs/2408.07295
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots project page
  url: https://masked-humanoid.github.io/mhc/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
A major challenge in humanoid robotics is designing a unified interface for commanding diverse whole-body behaviors, from precise footstep sequences to partial-body mimicry and joystick teleoperation. We introduce the Masked Humanoid Controller (MHC), a learned whole-body controller that exposes a simple yet expressive interface: the specification of masked target trajectories over selected subsets of the robot's state variables. This unified abstraction allows high-level systems to issue commands in a flexible format that accommodates multi-modal inputs such as optimized trajectories, motion capture clips, re-targeted video, and real-time joystick signals. The MHC is trained in simulation using a curriculum that spans this full range of modalities, enabling robust execution of partially specified behaviors while maintaining balance and disturbance rejection. We demonstrate the MHC both in simulation and on the real-world Digit V3 humanoid, showing that a single learned controller is capable of executing such diverse whole-body commands in the real world through a common representational interface.

## 核心内容
A major challenge in humanoid robotics is designing a unified interface for commanding diverse whole-body behaviors, from precise footstep sequences to partial-body mimicry and joystick teleoperation. We introduce the Masked Humanoid Controller (MHC), a learned whole-body controller that exposes a simple yet expressive interface: the specification of masked target trajectories over selected subsets of the robot's state variables. This unified abstraction allows high-level systems to issue commands in a flexible format that accommodates multi-modal inputs such as optimized trajectories, motion capture clips, re-targeted video, and real-time joystick signals. The MHC is trained in simulation using a curriculum that spans this full range of modalities, enabling robust execution of partially specified behaviors while maintaining balance and disturbance rejection. We demonstrate the MHC both in simulation and on the real-world Digit V3 humanoid, showing that a single learned controller is capable of executing such diverse whole-body commands in the real world through a common representational interface.

## 参考
- http://arxiv.org/abs/2408.07295v4

