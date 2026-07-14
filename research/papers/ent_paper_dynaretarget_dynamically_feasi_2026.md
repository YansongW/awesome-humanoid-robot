---
$id: ent_paper_dynaretarget_dynamically_feasi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DynaRetarget: Dynamically-Feasible Retargeting using Sampling-Based Trajectory Optimization'
  zh: 'DynaRetarget: Dynamically-Feasible Retargeting using Sampling-Based Trajectory Optimization'
  ko: 'DynaRetarget: Dynamically-Feasible Retargeting using Sampling-Based Trajectory Optimization'
summary:
  en: 'DynaRetarget: Dynamically-Feasible Retargeting using Sampling-Based Trajectory Optimization is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'DynaRetarget: Dynamically-Feasible Retargeting using Sampling-Based Trajectory Optimization is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'DynaRetarget: Dynamically-Feasible Retargeting using Sampling-Based Trajectory Optimization is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dynaretarget
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.06827v3.
sources:
- id: src_001
  type: paper
  title: 'DynaRetarget: Dynamically-Feasible Retargeting using Sampling-Based Trajectory Optimization (arXiv)'
  url: https://arxiv.org/abs/2602.06827
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
In this paper, we introduce DynaRetarget, a complete pipeline for retargeting human motions to humanoid control policies. The core component of DynaRetarget is a novel Sampling-Based Trajectory Optimization (SBTO) framework that refines imperfect kinematic trajectories into dynamically feasible motions. SBTO incrementally advances the optimization horizon, enabling optimization over the entire trajectory for long-horizon tasks. We validate DynaRetarget by successfully retargeting hundreds of humanoid-object demonstrations and achieving higher success rates than the state of the art. The framework also generalizes across varying object properties, such as mass, size, and geometry, using the same tracking objective. This ability to robustly retarget diverse demonstrations opens the door to generating large-scale synthetic datasets of humanoid loco-manipulation trajectories, addressing a major bottleneck in real-world data collection.

## 核心内容
In this paper, we introduce DynaRetarget, a complete pipeline for retargeting human motions to humanoid control policies. The core component of DynaRetarget is a novel Sampling-Based Trajectory Optimization (SBTO) framework that refines imperfect kinematic trajectories into dynamically feasible motions. SBTO incrementally advances the optimization horizon, enabling optimization over the entire trajectory for long-horizon tasks. We validate DynaRetarget by successfully retargeting hundreds of humanoid-object demonstrations and achieving higher success rates than the state of the art. The framework also generalizes across varying object properties, such as mass, size, and geometry, using the same tracking objective. This ability to robustly retarget diverse demonstrations opens the door to generating large-scale synthetic datasets of humanoid loco-manipulation trajectories, addressing a major bottleneck in real-world data collection.

## 参考
- http://arxiv.org/abs/2602.06827v3

