---
$id: ent_paper_eco_energy_constrained_optimiz_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking'
  zh: 'ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking'
  ko: 'ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking'
summary:
  en: 'ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking is a 2026 work on locomotion
    for humanoid robots, with open-source code available.'
  zh: 'ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking is a 2026 work on locomotion
    for humanoid robots, with open-source code available.'
  ko: 'ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking is a 2026 work on locomotion
    for humanoid robots, with open-source code available.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- eco
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.06445v1.
sources:
- id: src_001
  type: paper
  title: 'ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking (arXiv)'
  url: https://arxiv.org/abs/2602.06445
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking project page'
  url: https://sites.google.com/view/eco-humanoid
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Achieving stable and energy-efficient locomotion is essential for humanoid robots to operate continuously in real-world applications. Existing MPC and RL approaches often rely on energy-related metrics embedded within a multi-objective optimization framework, which require extensive hyperparameter tuning and often result in suboptimal policies. To address these challenges, we propose ECO (Energy-Constrained Optimization), a constrained RL framework that separates energy-related metrics from rewards, reformulating them as explicit inequality constraints. This method provides a clear and interpretable physical representation of energy costs, enabling more efficient and intuitive hyperparameter tuning for improved energy efficiency. ECO introduces dedicated constraints for energy consumption and reference motion, enforced by the Lagrangian method, to achieve stable, symmetric, and energy-efficient walking for humanoid robots. We evaluated ECO against MPC, standard RL with reward shaping, and four state-of-the-art constrained RL methods. Experiments, including sim-to-sim and sim-to-real transfers on the kid-sized humanoid robot BRUCE, demonstrate that ECO significantly reduces energy consumption compared to baselines while maintaining robust walking performance. These results highlight a substantial advancement in energy-efficient humanoid locomotion. All experimental demonstrations can be found on the project website: https://sites.google.com/view/eco-humanoid.

## 核心内容
Achieving stable and energy-efficient locomotion is essential for humanoid robots to operate continuously in real-world applications. Existing MPC and RL approaches often rely on energy-related metrics embedded within a multi-objective optimization framework, which require extensive hyperparameter tuning and often result in suboptimal policies. To address these challenges, we propose ECO (Energy-Constrained Optimization), a constrained RL framework that separates energy-related metrics from rewards, reformulating them as explicit inequality constraints. This method provides a clear and interpretable physical representation of energy costs, enabling more efficient and intuitive hyperparameter tuning for improved energy efficiency. ECO introduces dedicated constraints for energy consumption and reference motion, enforced by the Lagrangian method, to achieve stable, symmetric, and energy-efficient walking for humanoid robots. We evaluated ECO against MPC, standard RL with reward shaping, and four state-of-the-art constrained RL methods. Experiments, including sim-to-sim and sim-to-real transfers on the kid-sized humanoid robot BRUCE, demonstrate that ECO significantly reduces energy consumption compared to baselines while maintaining robust walking performance. These results highlight a substantial advancement in energy-efficient humanoid locomotion. All experimental demonstrations can be found on the project website: https://sites.google.com/view/eco-humanoid.

## 参考
- http://arxiv.org/abs/2602.06445v1

