---
$id: ent_paper_vision_in_action_learning_acti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Vision in Action: Learning Active Perception from Human Demonstrations'
  zh: 'Vision in Action: Learning Active Perception from Human Demonstrations'
  ko: 'Vision in Action: Learning Active Perception from Human Demonstrations'
summary:
  en: 'Vision in Action: Learning Active Perception from Human Demonstrations is a 2025 work on manipulation for humanoid
    robots.'
  zh: 'Vision in Action: Learning Active Perception from Human Demonstrations is a 2025 work on manipulation for humanoid
    robots.'
  ko: 'Vision in Action: Learning Active Perception from Human Demonstrations is a 2025 work on manipulation for humanoid
    robots.'
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
- manipulation
- vision_in_action
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.15666v1.
sources:
- id: src_001
  type: paper
  title: 'Vision in Action: Learning Active Perception from Human Demonstrations (arXiv)'
  url: https://arxiv.org/abs/2506.15666
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We present Vision in Action (ViA), an active perception system for bimanual robot manipulation. ViA learns task-relevant active perceptual strategies (e.g., searching, tracking, and focusing) directly from human demonstrations. On the hardware side, ViA employs a simple yet effective 6-DoF robotic neck to enable flexible, human-like head movements. To capture human active perception strategies, we design a VR-based teleoperation interface that creates a shared observation space between the robot and the human operator. To mitigate VR motion sickness caused by latency in the robot's physical movements, the interface uses an intermediate 3D scene representation, enabling real-time view rendering on the operator side while asynchronously updating the scene with the robot's latest observations. Together, these design elements enable the learning of robust visuomotor policies for three complex, multi-stage bimanual manipulation tasks involving visual occlusions, significantly outperforming baseline systems.

## 核心内容
We present Vision in Action (ViA), an active perception system for bimanual robot manipulation. ViA learns task-relevant active perceptual strategies (e.g., searching, tracking, and focusing) directly from human demonstrations. On the hardware side, ViA employs a simple yet effective 6-DoF robotic neck to enable flexible, human-like head movements. To capture human active perception strategies, we design a VR-based teleoperation interface that creates a shared observation space between the robot and the human operator. To mitigate VR motion sickness caused by latency in the robot's physical movements, the interface uses an intermediate 3D scene representation, enabling real-time view rendering on the operator side while asynchronously updating the scene with the robot's latest observations. Together, these design elements enable the learning of robust visuomotor policies for three complex, multi-stage bimanual manipulation tasks involving visual occlusions, significantly outperforming baseline systems.

## 参考
- http://arxiv.org/abs/2506.15666v1

