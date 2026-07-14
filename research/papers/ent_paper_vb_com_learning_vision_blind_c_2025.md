---
$id: ent_paper_vb_com_learning_vision_blind_c_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VB-Com: Learning Vision-Blind Composite Humanoid Locomotion Against Deficient Perception'
  zh: 'VB-Com: Learning Vision-Blind Composite Humanoid Locomotion Against Deficient Perception'
  ko: 'VB-Com: Learning Vision-Blind Composite Humanoid Locomotion Against Deficient Perception'
summary:
  en: 'VB-Com: Learning Vision-Blind Composite Humanoid Locomotion Against Deficient Perception is a 2025 work on locomotion
    for humanoid robots.'
  zh: 'VB-Com: Learning Vision-Blind Composite Humanoid Locomotion Against Deficient Perception is a 2025 work on locomotion
    for humanoid robots.'
  ko: 'VB-Com: Learning Vision-Blind Composite Humanoid Locomotion Against Deficient Perception is a 2025 work on locomotion
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- vb_com
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.14814v2.
sources:
- id: src_001
  type: paper
  title: 'VB-Com: Learning Vision-Blind Composite Humanoid Locomotion Against Deficient Perception (arXiv)'
  url: https://arxiv.org/abs/2502.14814
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'VB-Com: Learning Vision-Blind Composite Humanoid Locomotion Against Deficient Perception project page'
  url: https://renjunli99.github.io/vbcom.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The performance of legged locomotion is closely tied to the accuracy and comprehensiveness of state observations. Blind policies, which rely solely on proprioception, are considered highly robust due to the reliability of proprioceptive observations. However, these policies significantly limit locomotion speed and often require collisions with the terrain to adapt. In contrast, Vision policies allows the robot to plan motions in advance and respond proactively to unstructured terrains with an online perception module. However, perception is often compromised by noisy real-world environments, potential sensor failures, and the limitations of current simulations in presenting dynamic or deformable terrains. Humanoid robots, with high degrees of freedom and inherently unstable morphology, are particularly susceptible to misguidance from deficient perception, which can result in falls or termination on challenging dynamic terrains. To leverage the advantages of both vision and blind policies, we propose VB-Com, a composite framework that enables humanoid robots to determine when to rely on the vision policy and when to switch to the blind policy under perceptual deficiency. We demonstrate that VB-Com effectively enables humanoid robots to traverse challenging terrains and obstacles despite perception deficiencies caused by dynamic terrains or perceptual noise.

## 核心内容
The performance of legged locomotion is closely tied to the accuracy and comprehensiveness of state observations. Blind policies, which rely solely on proprioception, are considered highly robust due to the reliability of proprioceptive observations. However, these policies significantly limit locomotion speed and often require collisions with the terrain to adapt. In contrast, Vision policies allows the robot to plan motions in advance and respond proactively to unstructured terrains with an online perception module. However, perception is often compromised by noisy real-world environments, potential sensor failures, and the limitations of current simulations in presenting dynamic or deformable terrains. Humanoid robots, with high degrees of freedom and inherently unstable morphology, are particularly susceptible to misguidance from deficient perception, which can result in falls or termination on challenging dynamic terrains. To leverage the advantages of both vision and blind policies, we propose VB-Com, a composite framework that enables humanoid robots to determine when to rely on the vision policy and when to switch to the blind policy under perceptual deficiency. We demonstrate that VB-Com effectively enables humanoid robots to traverse challenging terrains and obstacles despite perception deficiencies caused by dynamic terrains or perceptual noise.

## 参考
- http://arxiv.org/abs/2502.14814v2

