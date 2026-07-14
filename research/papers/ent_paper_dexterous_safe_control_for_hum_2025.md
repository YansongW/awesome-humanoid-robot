---
$id: ent_paper_dexterous_safe_control_for_hum_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Dexterous Safe Control for Humanoids in Cluttered Environments via Projected Safe Set Algorithm
  zh: Dexterous Safe Control for Humanoids in Cluttered Environments via Projected Safe Set Algorithm
  ko: Dexterous Safe Control for Humanoids in Cluttered Environments via Projected Safe Set Algorithm
summary:
  en: Dexterous Safe Control for Humanoids in Cluttered Environments via Projected Safe Set Algorithm is a 2025 work on manipulation
    for humanoid robots.
  zh: Dexterous Safe Control for Humanoids in Cluttered Environments via Projected Safe Set Algorithm is a 2025 work on manipulation
    for humanoid robots.
  ko: Dexterous Safe Control for Humanoids in Cluttered Environments via Projected Safe Set Algorithm is a 2025 work on manipulation
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
- dexterous_safe_control_for_hum
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.02858v1.
sources:
- id: src_001
  type: paper
  title: Dexterous Safe Control for Humanoids in Cluttered Environments via Projected Safe Set Algorithm (arXiv)
  url: https://arxiv.org/abs/2502.02858
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
It is critical to ensure safety for humanoid robots in real-world applications without compromising performance. In this paper, we consider the problem of dexterous safety, featuring limb-level geometry constraints for avoiding both external and self-collisions in cluttered environments. Compared to safety with simplified bounding geometries in sprase environments, dexterous safety produces numerous constraints which often lead to infeasible constraint sets when solving for safe robot control. To address this issue, we propose Projected Safe Set Algorithm (p-SSA), an extension of classical safe control algorithms to multi-constraint cases. p-SSA relaxes conflicting constraints in a principled manner, minimizing safety violations to guarantee feasible robot control. We verify our approach in simulation and on a real Unitree G1 humanoid robot performing complex collision avoidance tasks. Results show that p-SSA enables the humanoid to operate robustly in challenging situations with minimal safety violations and directly generalizes to various tasks with zero parameter tuning.

## 核心内容
It is critical to ensure safety for humanoid robots in real-world applications without compromising performance. In this paper, we consider the problem of dexterous safety, featuring limb-level geometry constraints for avoiding both external and self-collisions in cluttered environments. Compared to safety with simplified bounding geometries in sprase environments, dexterous safety produces numerous constraints which often lead to infeasible constraint sets when solving for safe robot control. To address this issue, we propose Projected Safe Set Algorithm (p-SSA), an extension of classical safe control algorithms to multi-constraint cases. p-SSA relaxes conflicting constraints in a principled manner, minimizing safety violations to guarantee feasible robot control. We verify our approach in simulation and on a real Unitree G1 humanoid robot performing complex collision avoidance tasks. Results show that p-SSA enables the humanoid to operate robustly in challenging situations with minimal safety violations and directly generalizes to various tasks with zero parameter tuning.

## 参考
- http://arxiv.org/abs/2502.02858v1

