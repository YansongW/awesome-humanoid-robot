---
$id: ent_paper_coordinated_humanoid_robot_loc_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy
  zh: Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy
  ko: Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy
summary:
  en: Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy is a 2025 work on locomotion
    for humanoid robots.
  zh: Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy is a 2025 work on locomotion
    for humanoid robots.
  ko: Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy is a 2025 work on locomotion
    for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- coordinated_humanoid_robot_loc
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.01247v2.
sources:
- id: src_001
  type: paper
  title: Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy (arXiv)
  url: https://arxiv.org/abs/2508.01247
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The human nervous system exhibits bilateral symmetry, enabling coordinated and balanced movements. However, existing Deep Reinforcement Learning (DRL) methods for humanoid robots neglect morphological symmetry of the robot, leading to uncoordinated and suboptimal behaviors. Inspired by human motor control, we propose Symmetry Equivariant Policy (SE-Policy), a new DRL framework that embeds strict symmetry equivariance in the actor and symmetry invariance in the critic without additional hyperparameters. SE-Policy enforces consistent behaviors across symmetric observations, producing temporally and spatially coordinated motions with higher task performance. Extensive experiments on velocity tracking tasks, conducted in both simulation and real-world deployment with the Unitree G1 humanoid robot, demonstrate that SE-Policy improves tracking accuracy by up to 40% compared to state-of-the-art baselines, while achieving superior spatial-temporal coordination. These results demonstrate the effectiveness of SE-Policy and its broad applicability to humanoid robots.

## 核心内容
The human nervous system exhibits bilateral symmetry, enabling coordinated and balanced movements. However, existing Deep Reinforcement Learning (DRL) methods for humanoid robots neglect morphological symmetry of the robot, leading to uncoordinated and suboptimal behaviors. Inspired by human motor control, we propose Symmetry Equivariant Policy (SE-Policy), a new DRL framework that embeds strict symmetry equivariance in the actor and symmetry invariance in the critic without additional hyperparameters. SE-Policy enforces consistent behaviors across symmetric observations, producing temporally and spatially coordinated motions with higher task performance. Extensive experiments on velocity tracking tasks, conducted in both simulation and real-world deployment with the Unitree G1 humanoid robot, demonstrate that SE-Policy improves tracking accuracy by up to 40% compared to state-of-the-art baselines, while achieving superior spatial-temporal coordination. These results demonstrate the effectiveness of SE-Policy and its broad applicability to humanoid robots.

## 参考
- http://arxiv.org/abs/2508.01247v2

