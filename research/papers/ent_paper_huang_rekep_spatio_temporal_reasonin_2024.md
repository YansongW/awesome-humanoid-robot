---
$id: ent_paper_huang_rekep_spatio_temporal_reasonin_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation'
  zh: ReKep
  ko: 'ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation'
summary:
  en: 'ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation (ReKep), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by Stanford University, Columbia University, and published
    at CoRL 2024.'
  zh: 'ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation (ReKep), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by Stanford University, Columbia University, and published
    at CoRL 2024.'
  ko: 'ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation (ReKep), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by Stanford University, Columbia University, and published
    at CoRL 2024.'
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
- rekep
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.01652v2.
sources:
- id: src_001
  type: paper
  title: ReKep source
  url: https://proceedings.mlr.press/v270/huang25g.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Representing robotic manipulation tasks as constraints that associate the robot and the environment is a promising way to encode desired robot behaviors. However, it remains unclear how to formulate the constraints such that they are 1) versatile to diverse tasks, 2) free of manual labeling, and 3) optimizable by off-the-shelf solvers to produce robot actions in real-time. In this work, we introduce Relational Keypoint Constraints (ReKep), a visually-grounded representation for constraints in robotic manipulation. Specifically, ReKep is expressed as Python functions mapping a set of 3D keypoints in the environment to a numerical cost. We demonstrate that by representing a manipulation task as a sequence of Relational Keypoint Constraints, we can employ a hierarchical optimization procedure to solve for robot actions (represented by a sequence of end-effector poses in SE(3)) with a perception-action loop at a real-time frequency. Furthermore, in order to circumvent the need for manual specification of ReKep for each new task, we devise an automated procedure that leverages large vision models and vision-language models to produce ReKep from free-form language instructions and RGB-D observations. We present system implementations on a wheeled single-arm platform and a stationary dual-arm platform that can perform a large variety of manipulation tasks, featuring multi-stage, in-the-wild, bimanual, and reactive behaviors, all without task-specific data or environment models. Website at https://rekep-robot.github.io/.

## 核心内容
Representing robotic manipulation tasks as constraints that associate the robot and the environment is a promising way to encode desired robot behaviors. However, it remains unclear how to formulate the constraints such that they are 1) versatile to diverse tasks, 2) free of manual labeling, and 3) optimizable by off-the-shelf solvers to produce robot actions in real-time. In this work, we introduce Relational Keypoint Constraints (ReKep), a visually-grounded representation for constraints in robotic manipulation. Specifically, ReKep is expressed as Python functions mapping a set of 3D keypoints in the environment to a numerical cost. We demonstrate that by representing a manipulation task as a sequence of Relational Keypoint Constraints, we can employ a hierarchical optimization procedure to solve for robot actions (represented by a sequence of end-effector poses in SE(3)) with a perception-action loop at a real-time frequency. Furthermore, in order to circumvent the need for manual specification of ReKep for each new task, we devise an automated procedure that leverages large vision models and vision-language models to produce ReKep from free-form language instructions and RGB-D observations. We present system implementations on a wheeled single-arm platform and a stationary dual-arm platform that can perform a large variety of manipulation tasks, featuring multi-stage, in-the-wild, bimanual, and reactive behaviors, all without task-specific data or environment models. Website at https://rekep-robot.github.io/.

## 参考
- http://arxiv.org/abs/2409.01652v2

