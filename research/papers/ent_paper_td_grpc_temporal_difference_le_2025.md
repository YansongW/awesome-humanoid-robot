---
$id: ent_paper_td_grpc_temporal_difference_le_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TD-GRPC: Temporal Difference Learning with Group Relative Policy Constraint for Humanoid Locomotion'
  zh: 'TD-GRPC: Temporal Difference Learning with Group Relative Policy Constraint for Humanoid Locomotion'
  ko: 'TD-GRPC: Temporal Difference Learning with Group Relative Policy Constraint for Humanoid Locomotion'
summary:
  en: 'TD-GRPC: Temporal Difference Learning with Group Relative Policy Constraint for Humanoid Locomotion is a 2025 work
    on locomotion for humanoid robots.'
  zh: 'TD-GRPC: Temporal Difference Learning with Group Relative Policy Constraint for Humanoid Locomotion is a 2025 work
    on locomotion for humanoid robots.'
  ko: 'TD-GRPC: Temporal Difference Learning with Group Relative Policy Constraint for Humanoid Locomotion is a 2025 work
    on locomotion for humanoid robots.'
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
- td_grpc
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.13549v1.
sources:
- id: src_001
  type: paper
  title: 'TD-GRPC: Temporal Difference Learning with Group Relative Policy Constraint for Humanoid Locomotion (arXiv)'
  url: https://arxiv.org/abs/2505.13549
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Robot learning in high-dimensional control settings, such as humanoid locomotion, presents persistent challenges for reinforcement learning (RL) algorithms due to unstable dynamics, complex contact interactions, and sensitivity to distributional shifts during training. Model-based methods, \textit{e.g.}, Temporal-Difference Model Predictive Control (TD-MPC), have demonstrated promising results by combining short-horizon planning with value-based learning, enabling efficient solutions for basic locomotion tasks. However, these approaches remain ineffective in addressing policy mismatch and instability introduced by off-policy updates. Thus, in this work, we introduce Temporal-Difference Group Relative Policy Constraint (TD-GRPC), an extension of the TD-MPC framework that unifies Group Relative Policy Optimization (GRPO) with explicit Policy Constraints (PC). TD-GRPC applies a trust-region constraint in the latent policy space to maintain consistency between the planning priors and learned rollouts, while leveraging group-relative ranking to assess and preserve the physical feasibility of candidate trajectories. Unlike prior methods, TD-GRPC achieves robust motions without modifying the underlying planner, enabling flexible planning and policy learning. We validate our method across a locomotion task suite ranging from basic walking to highly dynamic movements on the 26-DoF Unitree H1-2 humanoid robot. Through simulation results, TD-GRPC demonstrates its improvements in stability and policy robustness with sampling efficiency while training for complex humanoid control tasks.

## 核心内容
Robot learning in high-dimensional control settings, such as humanoid locomotion, presents persistent challenges for reinforcement learning (RL) algorithms due to unstable dynamics, complex contact interactions, and sensitivity to distributional shifts during training. Model-based methods, \textit{e.g.}, Temporal-Difference Model Predictive Control (TD-MPC), have demonstrated promising results by combining short-horizon planning with value-based learning, enabling efficient solutions for basic locomotion tasks. However, these approaches remain ineffective in addressing policy mismatch and instability introduced by off-policy updates. Thus, in this work, we introduce Temporal-Difference Group Relative Policy Constraint (TD-GRPC), an extension of the TD-MPC framework that unifies Group Relative Policy Optimization (GRPO) with explicit Policy Constraints (PC). TD-GRPC applies a trust-region constraint in the latent policy space to maintain consistency between the planning priors and learned rollouts, while leveraging group-relative ranking to assess and preserve the physical feasibility of candidate trajectories. Unlike prior methods, TD-GRPC achieves robust motions without modifying the underlying planner, enabling flexible planning and policy learning. We validate our method across a locomotion task suite ranging from basic walking to highly dynamic movements on the 26-DoF Unitree H1-2 humanoid robot. Through simulation results, TD-GRPC demonstrates its improvements in stability and policy robustness with sampling efficiency while training for complex humanoid control tasks.

## 参考
- http://arxiv.org/abs/2505.13549v1

