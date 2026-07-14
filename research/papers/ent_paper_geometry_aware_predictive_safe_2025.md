---
$id: ent_paper_geometry_aware_predictive_safe_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Geometry-Aware Predictive Safety Filters on Humanoids
  zh: Geometry-Aware Predictive Safety Filters on Humanoids
  ko: Geometry-Aware Predictive Safety Filters on Humanoids
summary:
  en: Geometry-Aware Predictive Safety Filters on Humanoids is a 2025 work on locomotion for humanoid robots.
  zh: Geometry-Aware Predictive Safety Filters on Humanoids is a 2025 work on locomotion for humanoid robots.
  ko: Geometry-Aware Predictive Safety Filters on Humanoids is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- geometry_aware_predictive_safe
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.11129v1.
sources:
- id: src_001
  type: paper
  title: Geometry-Aware Predictive Safety Filters on Humanoids (arXiv)
  url: https://arxiv.org/abs/2508.11129
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Autonomous navigation through unstructured and dynamically-changing environments is a complex task that continues to present many challenges for modern roboticists. In particular, legged robots typically possess manipulable asymmetric geometries which must be considered during safety-critical trajectory planning. This work proposes a predictive safety filter: a nonlinear model predictive control (MPC) algorithm for online trajectory generation with geometry-aware safety constraints based on control barrier functions (CBFs). Critically, our method leverages Poisson safety functions to numerically synthesize CBF constraints directly from perception data. We extend the theoretical framework for Poisson safety functions to incorporate temporal changes in the domain by reformulating the static Dirichlet problem for Poisson's equation as a parameterized moving boundary value problem. Furthermore, we employ Minkowski set operations to lift the domain into a configuration space that accounts for robot geometry. Finally, we implement our real-time predictive safety filter on humanoid and quadruped robots in various safety-critical scenarios. The results highlight the versatility of Poisson safety functions, as well as the benefit of CBF constrained model predictive safety-critical controllers.

## 核心内容
Autonomous navigation through unstructured and dynamically-changing environments is a complex task that continues to present many challenges for modern roboticists. In particular, legged robots typically possess manipulable asymmetric geometries which must be considered during safety-critical trajectory planning. This work proposes a predictive safety filter: a nonlinear model predictive control (MPC) algorithm for online trajectory generation with geometry-aware safety constraints based on control barrier functions (CBFs). Critically, our method leverages Poisson safety functions to numerically synthesize CBF constraints directly from perception data. We extend the theoretical framework for Poisson safety functions to incorporate temporal changes in the domain by reformulating the static Dirichlet problem for Poisson's equation as a parameterized moving boundary value problem. Furthermore, we employ Minkowski set operations to lift the domain into a configuration space that accounts for robot geometry. Finally, we implement our real-time predictive safety filter on humanoid and quadruped robots in various safety-critical scenarios. The results highlight the versatility of Poisson safety functions, as well as the benefit of CBF constrained model predictive safety-critical controllers.

## 参考
- http://arxiv.org/abs/2508.11129v1

