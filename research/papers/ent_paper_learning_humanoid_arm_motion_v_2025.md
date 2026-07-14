---
$id: ent_paper_learning_humanoid_arm_motion_v_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning
  zh: Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning
  ko: Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning
summary:
  en: Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning is a 2025 work on
    locomotion for humanoid robots.
  zh: Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning is a 2025 work on
    locomotion for humanoid robots.
  ko: Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning is a 2025 work on
    locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_humanoid_arm_motion_v
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.04140v1.
sources:
- id: src_001
  type: paper
  title: Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning (arXiv)
  url: https://www.arxiv.org/abs/2507.04140
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humans naturally swing their arms during locomotion to regulate whole-body dynamics, reduce angular momentum, and help maintain balance. Inspired by this principle, we present a limb-level multi-agent reinforcement learning (RL) framework that enables coordinated whole-body control of humanoid robots through emergent arm motion. Our approach employs separate actor-critic structures for the arms and legs, trained with centralized critics but decentralized actors that share only base states and centroidal angular momentum (CAM) observations, allowing each agent to specialize in task-relevant behaviors through modular reward design. The arm agent guided by CAM tracking and damping rewards promotes arm motions that reduce overall angular momentum and vertical ground reaction moments, contributing to improved balance during locomotion or under external perturbations. Comparative studies with single-agent and alternative multi-agent baselines further validate the effectiveness of our approach. Finally, we deploy the learned policy on a humanoid platform, achieving robust performance across diverse locomotion tasks, including flat-ground walking, rough terrain traversal, and stair climbing.

## 核心内容
Humans naturally swing their arms during locomotion to regulate whole-body dynamics, reduce angular momentum, and help maintain balance. Inspired by this principle, we present a limb-level multi-agent reinforcement learning (RL) framework that enables coordinated whole-body control of humanoid robots through emergent arm motion. Our approach employs separate actor-critic structures for the arms and legs, trained with centralized critics but decentralized actors that share only base states and centroidal angular momentum (CAM) observations, allowing each agent to specialize in task-relevant behaviors through modular reward design. The arm agent guided by CAM tracking and damping rewards promotes arm motions that reduce overall angular momentum and vertical ground reaction moments, contributing to improved balance during locomotion or under external perturbations. Comparative studies with single-agent and alternative multi-agent baselines further validate the effectiveness of our approach. Finally, we deploy the learned policy on a humanoid platform, achieving robust performance across diverse locomotion tasks, including flat-ground walking, rough terrain traversal, and stair climbing.

## 参考
- http://arxiv.org/abs/2507.04140v1

