---
$id: ent_paper_traversing_narrow_paths_a_two_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Traversing Narrow Paths: A Two-Stage RL Framework for Robust and Safe Humanoid Walking'
  zh: 'Traversing Narrow Paths: A Two-Stage RL Framework for Robust and Safe Humanoid Walking'
  ko: 'Traversing Narrow Paths: A Two-Stage RL Framework for Robust and Safe Humanoid Walking'
summary:
  en: 'Traversing Narrow Paths: A Two-Stage RL Framework for Robust and Safe Humanoid Walking is a 2025 work on locomotion
    for humanoid robots.'
  zh: 'Traversing Narrow Paths: A Two-Stage RL Framework for Robust and Safe Humanoid Walking is a 2025 work on locomotion
    for humanoid robots.'
  ko: 'Traversing Narrow Paths: A Two-Stage RL Framework for Robust and Safe Humanoid Walking is a 2025 work on locomotion
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
- traversing_narrow_paths
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.20661v4.
sources:
- id: src_001
  type: paper
  title: 'Traversing Narrow Paths: A Two-Stage RL Framework for Robust and Safe Humanoid Walking (arXiv)'
  url: https://arxiv.org/abs/2508.20661
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Traversing narrow paths is challenging for humanoid robots due to the sparse and safety-critical footholds required. Purely template-based or end-to-end reinforcement learning-based methods suffer from such harsh terrains. This paper proposes a two stage training framework for such narrow path traversing tasks, coupling a template-based foothold planner with a low-level foothold tracker from Stage-I training and a lightweight perception aided foothold modifier from Stage-II training. With the curriculum setup from flat ground to narrow paths across stages, the resulted controller in turn learns to robustly track and safely modify foothold targets to ensure precise foot placement over narrow paths. This framework preserves the interpretability from the physics-based template and takes advantage of the generalization capability from reinforcement learning, resulting in easy sim-to-real transfer. The learned policies outperform purely template-based or reinforcement learning-based baselines in terms of success rate, centerline adherence and safety margins. Validation on a Unitree G1 humanoid robot yields successful traversal of a 0.2m wide and 3m long beam for 20 trials without any failure.

## 核心内容
Traversing narrow paths is challenging for humanoid robots due to the sparse and safety-critical footholds required. Purely template-based or end-to-end reinforcement learning-based methods suffer from such harsh terrains. This paper proposes a two stage training framework for such narrow path traversing tasks, coupling a template-based foothold planner with a low-level foothold tracker from Stage-I training and a lightweight perception aided foothold modifier from Stage-II training. With the curriculum setup from flat ground to narrow paths across stages, the resulted controller in turn learns to robustly track and safely modify foothold targets to ensure precise foot placement over narrow paths. This framework preserves the interpretability from the physics-based template and takes advantage of the generalization capability from reinforcement learning, resulting in easy sim-to-real transfer. The learned policies outperform purely template-based or reinforcement learning-based baselines in terms of success rate, centerline adherence and safety margins. Validation on a Unitree G1 humanoid robot yields successful traversal of a 0.2m wide and 3m long beam for 20 trials without any failure.

## 参考
- http://arxiv.org/abs/2508.20661v4

