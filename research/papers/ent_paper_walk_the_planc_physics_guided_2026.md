---
$id: ent_paper_walk_the_planc_physics_guided_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Walk the PLANC: Physics-Guided RL for Agile Humanoid Locomotion on Constrained Footholds'
  zh: 'Walk the PLANC: Physics-Guided RL for Agile Humanoid Locomotion on Constrained Footholds'
  ko: 'Walk the PLANC: Physics-Guided RL for Agile Humanoid Locomotion on Constrained Footholds'
summary:
  en: 'Walk the PLANC: Physics-Guided RL for Agile Humanoid Locomotion on Constrained Footholds is a 2026 work on locomotion
    for humanoid robots.'
  zh: 'Walk the PLANC: Physics-Guided RL for Agile Humanoid Locomotion on Constrained Footholds is a 2026 work on locomotion
    for humanoid robots.'
  ko: 'Walk the PLANC: Physics-Guided RL for Agile Humanoid Locomotion on Constrained Footholds is a 2026 work on locomotion
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
- walk_the_planc
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.06286v1.
sources:
- id: src_001
  type: paper
  title: 'Walk the PLANC: Physics-Guided RL for Agile Humanoid Locomotion on Constrained Footholds (arXiv)'
  url: https://arxiv.org/abs/2601.06286
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Bipedal humanoid robots must precisely coordinate balance, timing, and contact decisions when locomoting on constrained footholds such as stepping stones, beams, and planks -- even minor errors can lead to catastrophic failure. Classical optimization and control pipelines handle these constraints well but depend on highly accurate mathematical representations of terrain geometry, making them prone to error when perception is noisy or incomplete. Meanwhile, reinforcement learning has shown strong resilience to disturbances and modeling errors, yet end-to-end policies rarely discover the precise foothold placement and step sequencing required for discontinuous terrain. These contrasting limitations motivate approaches that guide learning with physics-based structure rather than relying purely on reward shaping. In this work, we introduce a locomotion framework in which a reduced-order stepping planner supplies dynamically consistent motion targets that steer the RL training process via Control Lyapunov Function (CLF) rewards. This combination of structured footstep planning and data-driven adaptation produces accurate, agile, and hardware-validated stepping-stone locomotion on a humanoid robot, substantially improving reliability compared to conventional model-free reinforcement-learning baselines.

## 核心内容
Bipedal humanoid robots must precisely coordinate balance, timing, and contact decisions when locomoting on constrained footholds such as stepping stones, beams, and planks -- even minor errors can lead to catastrophic failure. Classical optimization and control pipelines handle these constraints well but depend on highly accurate mathematical representations of terrain geometry, making them prone to error when perception is noisy or incomplete. Meanwhile, reinforcement learning has shown strong resilience to disturbances and modeling errors, yet end-to-end policies rarely discover the precise foothold placement and step sequencing required for discontinuous terrain. These contrasting limitations motivate approaches that guide learning with physics-based structure rather than relying purely on reward shaping. In this work, we introduce a locomotion framework in which a reduced-order stepping planner supplies dynamically consistent motion targets that steer the RL training process via Control Lyapunov Function (CLF) rewards. This combination of structured footstep planning and data-driven adaptation produces accurate, agile, and hardware-validated stepping-stone locomotion on a humanoid robot, substantially improving reliability compared to conventional model-free reinforcement-learning baselines.

## 参考
- http://arxiv.org/abs/2601.06286v1

