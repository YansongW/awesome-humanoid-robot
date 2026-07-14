---
$id: ent_paper_reduced_order_model_guided_rl_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reduced-Order Model-Guided RL for Demonstration-Free Humanoid Locomotion
  zh: Reduced-Order Model-Guided RL for Demonstration-Free Humanoid Locomotion
  ko: Reduced-Order Model-Guided RL for Demonstration-Free Humanoid Locomotion
summary:
  en: Reduced-Order Model-Guided RL for Demonstration-Free Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.
  zh: Reduced-Order Model-Guided RL for Demonstration-Free Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.
  ko: Reduced-Order Model-Guided RL for Demonstration-Free Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.
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
- reduced_order_model_guided_rl
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.19023v1.
sources:
- id: src_001
  type: paper
  title: Reduced-Order Model-Guided RL for Demonstration-Free Humanoid Locomotion (arXiv)
  url: https://arxiv.org/abs/2509.19023
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We introduce Reduced-Order Model-Guided Reinforcement Learning (ROM-GRL), a two-stage reinforcement learning framework for humanoid walking that requires no motion capture data or elaborate reward shaping. In the first stage, a compact 4-DOF (four-degree-of-freedom) reduced-order model (ROM) is trained via Proximal Policy Optimization. This generates energy-efficient gait templates. In the second stage, those dynamically consistent trajectories guide a full-body policy trained with Soft Actor--Critic augmented by an adversarial discriminator, ensuring the student's five-dimensional gait feature distribution matches the ROM's demonstrations. Experiments at 1 meter-per-second and 4 meter-per-second show that ROM-GRL produces stable, symmetric gaits with substantially lower tracking error than a pure-reward baseline. By distilling lightweight ROM guidance into high-dimensional policies, ROM-GRL bridges the gap between reward-only and imitation-based locomotion methods, enabling versatile, naturalistic humanoid behaviors without any human demonstrations.

## 核心内容
We introduce Reduced-Order Model-Guided Reinforcement Learning (ROM-GRL), a two-stage reinforcement learning framework for humanoid walking that requires no motion capture data or elaborate reward shaping. In the first stage, a compact 4-DOF (four-degree-of-freedom) reduced-order model (ROM) is trained via Proximal Policy Optimization. This generates energy-efficient gait templates. In the second stage, those dynamically consistent trajectories guide a full-body policy trained with Soft Actor--Critic augmented by an adversarial discriminator, ensuring the student's five-dimensional gait feature distribution matches the ROM's demonstrations. Experiments at 1 meter-per-second and 4 meter-per-second show that ROM-GRL produces stable, symmetric gaits with substantially lower tracking error than a pure-reward baseline. By distilling lightweight ROM guidance into high-dimensional policies, ROM-GRL bridges the gap between reward-only and imitation-based locomotion methods, enabling versatile, naturalistic humanoid behaviors without any human demonstrations.

## 参考
- http://arxiv.org/abs/2509.19023v1

