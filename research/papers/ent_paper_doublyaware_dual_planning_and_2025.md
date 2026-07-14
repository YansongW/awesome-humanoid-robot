---
$id: ent_paper_doublyaware_dual_planning_and_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DoublyAware: Dual Planning and Policy Awareness for Temporal Difference Learning in Humanoid Locomotion'
  zh: 'DoublyAware: Dual Planning and Policy Awareness for Temporal Difference Learning in Humanoid Locomotion'
  ko: 'DoublyAware: Dual Planning and Policy Awareness for Temporal Difference Learning in Humanoid Locomotion'
summary:
  en: 'DoublyAware: Dual Planning and Policy Awareness for Temporal Difference Learning in Humanoid Locomotion is a 2025 work
    on locomotion for humanoid robots.'
  zh: 'DoublyAware: Dual Planning and Policy Awareness for Temporal Difference Learning in Humanoid Locomotion is a 2025 work
    on locomotion for humanoid robots.'
  ko: 'DoublyAware: Dual Planning and Policy Awareness for Temporal Difference Learning in Humanoid Locomotion is a 2025 work
    on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- doublyaware
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.12095v1.
sources:
- id: src_001
  type: paper
  title: 'DoublyAware: Dual Planning and Policy Awareness for Temporal Difference Learning in Humanoid Locomotion (arXiv)'
  url: https://arxiv.org/abs/2506.12095
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Achieving robust robot learning for humanoid locomotion is a fundamental challenge in model-based reinforcement learning (MBRL), where environmental stochasticity and randomness can hinder efficient exploration and learning stability. The environmental, so-called aleatoric, uncertainty can be amplified in high-dimensional action spaces with complex contact dynamics, and further entangled with epistemic uncertainty in the models during learning phases. In this work, we propose DoublyAware, an uncertainty-aware extension of Temporal Difference Model Predictive Control (TD-MPC) that explicitly decomposes uncertainty into two disjoint interpretable components, i.e., planning and policy uncertainties. To handle the planning uncertainty, DoublyAware employs conformal prediction to filter candidate trajectories using quantile-calibrated risk bounds, ensuring statistical consistency and robustness against stochastic dynamics. Meanwhile, policy rollouts are leveraged as structured informative priors to support the learning phase with Group-Relative Policy Constraint (GRPC) optimizers that impose a group-based adaptive trust-region in the latent action space. This principled combination enables the robot agent to prioritize high-confidence, high-reward behavior while maintaining effective, targeted exploration under uncertainty. Evaluated on the HumanoidBench locomotion suite with the Unitree 26-DoF H1-2 humanoid, DoublyAware demonstrates improved sample efficiency, accelerated convergence, and enhanced motion feasibility compared to RL baselines. Our simulation results emphasize the significance of structured uncertainty modeling for data-efficient and reliable decision-making in TD-MPC-based humanoid locomotion learning.

## 核心内容
Achieving robust robot learning for humanoid locomotion is a fundamental challenge in model-based reinforcement learning (MBRL), where environmental stochasticity and randomness can hinder efficient exploration and learning stability. The environmental, so-called aleatoric, uncertainty can be amplified in high-dimensional action spaces with complex contact dynamics, and further entangled with epistemic uncertainty in the models during learning phases. In this work, we propose DoublyAware, an uncertainty-aware extension of Temporal Difference Model Predictive Control (TD-MPC) that explicitly decomposes uncertainty into two disjoint interpretable components, i.e., planning and policy uncertainties. To handle the planning uncertainty, DoublyAware employs conformal prediction to filter candidate trajectories using quantile-calibrated risk bounds, ensuring statistical consistency and robustness against stochastic dynamics. Meanwhile, policy rollouts are leveraged as structured informative priors to support the learning phase with Group-Relative Policy Constraint (GRPC) optimizers that impose a group-based adaptive trust-region in the latent action space. This principled combination enables the robot agent to prioritize high-confidence, high-reward behavior while maintaining effective, targeted exploration under uncertainty. Evaluated on the HumanoidBench locomotion suite with the Unitree 26-DoF H1-2 humanoid, DoublyAware demonstrates improved sample efficiency, accelerated convergence, and enhanced motion feasibility compared to RL baselines. Our simulation results emphasize the significance of structured uncertainty modeling for data-efficient and reliable decision-making in TD-MPC-based humanoid locomotion learning.

## 参考
- http://arxiv.org/abs/2506.12095v1

