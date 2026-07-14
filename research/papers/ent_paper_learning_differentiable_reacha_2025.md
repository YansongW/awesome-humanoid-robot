---
$id: ent_paper_learning_differentiable_reacha_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation
  zh: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation
  ko: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation
summary:
  en: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.
  zh: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.
  ko: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.
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
- learning_differentiable_reacha
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.11275v1.
sources:
- id: src_001
  type: paper
  title: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation (arXiv)
  url: https://arxiv.org/abs/2508.11275
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
To reduce the computational cost of humanoid motion generation, we introduce a new approach to representing robot kinematic reachability: the differentiable reachability map. This map is a scalar-valued function defined in the task space that takes positive values only in regions reachable by the robot's end-effector. A key feature of this representation is that it is continuous and differentiable with respect to task-space coordinates, enabling its direct use as constraints in continuous optimization for humanoid motion planning. We describe a method to learn such differentiable reachability maps from a set of end-effector poses generated using a robot's kinematic model, using either a neural network or a support vector machine as the learning model. By incorporating the learned reachability map as a constraint, we formulate humanoid motion generation as a continuous optimization problem. We demonstrate that the proposed approach efficiently solves various motion planning problems, including footstep planning, multi-contact motion planning, and loco-manipulation planning for humanoid robots.

## 核心内容
To reduce the computational cost of humanoid motion generation, we introduce a new approach to representing robot kinematic reachability: the differentiable reachability map. This map is a scalar-valued function defined in the task space that takes positive values only in regions reachable by the robot's end-effector. A key feature of this representation is that it is continuous and differentiable with respect to task-space coordinates, enabling its direct use as constraints in continuous optimization for humanoid motion planning. We describe a method to learn such differentiable reachability maps from a set of end-effector poses generated using a robot's kinematic model, using either a neural network or a support vector machine as the learning model. By incorporating the learned reachability map as a constraint, we formulate humanoid motion generation as a continuous optimization problem. We demonstrate that the proposed approach efficiently solves various motion planning problems, including footstep planning, multi-contact motion planning, and loco-manipulation planning for humanoid robots.

## 参考
- http://arxiv.org/abs/2508.11275v1

