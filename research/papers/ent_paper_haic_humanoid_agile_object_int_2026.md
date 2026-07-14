---
$id: ent_paper_haic_humanoid_agile_object_int_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model'
  zh: 对象也有自己的动力学
  ko: 'HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model'
summary:
  en: 'HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model is a knowledge node related to paper
    in the humanoid robot value chain.'
  zh: Humanoid robots show promise for complex whole-body tasks in unstructured environments. Although Human-Object Interaction
    (HOI) has advanced, most methods focus on fully actuated objects rigidly coupled to the robot, ignoring underactuated
    objects with independent dynamics and non-holonomic constraints. These introduce control challenges from coupling forces
    and occlusions. We present HAIC, a unified framework for robust interaction across diverse object dynamics without external
    state estimation. Our key contribution is a dynamics predictor that estimates high-order object states (velocity, acceleration)
    solely from proprioceptive history. These predictions are projected onto static geometric priors to form a spatially grounded
    dynamic occupancy map, enabling the policy to infer collision
  ko: 'HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model is a knowledge node related to paper
    in the humanoid robot value chain.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.11758v2.
sources:
- id: src_001
  type: paper
  title: 'HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model (arXiv)'
  url: https://arxiv.org/abs/2602.11758
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 对象也有自己的动力学 project page
  url: https://haic-humanoid.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Humanoid robots show promise for complex whole-body tasks in unstructured environments. Although Human-Object Interaction (HOI) has advanced, most methods focus on fully actuated objects rigidly coupled to the robot, ignoring underactuated objects with independent dynamics and non-holonomic constraints. These introduce control challenges from coupling forces and occlusions. We present HAIC, a unified framework for robust interaction across diverse object dynamics without external state estimation. Our key contribution is a dynamics predictor that estimates high-order object states (velocity, acceleration) solely from proprioceptive history. These predictions are projected onto static geometric priors to form a spatially grounded dynamic occupancy map, enabling the policy to infer collision boundaries and contact affordances in blind spots. We use asymmetric fine-tuning, where a world model continuously adapts to the student policy's exploration, ensuring robust state estimation under distribution shifts. Experiments on a humanoid robot show HAIC achieves high success rates in agile tasks (skateboarding, cart pushing/pulling under various loads) by proactively compensating for inertial perturbations, and also masters multi-object long-horizon tasks like carrying a box across varied terrain by predicting the dynamics of multiple objects.

## 核心内容
Humanoid robots show promise for complex whole-body tasks in unstructured environments. Although Human-Object Interaction (HOI) has advanced, most methods focus on fully actuated objects rigidly coupled to the robot, ignoring underactuated objects with independent dynamics and non-holonomic constraints. These introduce control challenges from coupling forces and occlusions. We present HAIC, a unified framework for robust interaction across diverse object dynamics without external state estimation. Our key contribution is a dynamics predictor that estimates high-order object states (velocity, acceleration) solely from proprioceptive history. These predictions are projected onto static geometric priors to form a spatially grounded dynamic occupancy map, enabling the policy to infer collision boundaries and contact affordances in blind spots. We use asymmetric fine-tuning, where a world model continuously adapts to the student policy's exploration, ensuring robust state estimation under distribution shifts. Experiments on a humanoid robot show HAIC achieves high success rates in agile tasks (skateboarding, cart pushing/pulling under various loads) by proactively compensating for inertial perturbations, and also masters multi-object long-horizon tasks like carrying a box across varied terrain by predicting the dynamics of multiple objects.

## 参考
- http://arxiv.org/abs/2602.11758v2

