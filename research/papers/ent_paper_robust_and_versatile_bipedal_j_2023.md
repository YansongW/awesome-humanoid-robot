---
$id: ent_paper_robust_and_versatile_bipedal_j_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robust and Versatile Bipedal Jumping Control through Reinforcement Learning
  zh: Robust and Versatile Bipedal Jumping Control through Reinforcement Learning
  ko: Robust and Versatile Bipedal Jumping Control through Reinforcement Learning
summary:
  en: Robust and Versatile Bipedal Jumping Control through Reinforcement Learning is a 2023 work on locomotion for humanoid
    robots.
  zh: Robust and Versatile Bipedal Jumping Control through Reinforcement Learning is a 2023 work on locomotion for humanoid
    robots.
  ko: Robust and Versatile Bipedal Jumping Control through Reinforcement Learning is a 2023 work on locomotion for humanoid
    robots.
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
- robust_and_versatile_bipedal_j
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2302.09450v2.
sources:
- id: src_001
  type: paper
  title: Robust and Versatile Bipedal Jumping Control through Reinforcement Learning (arXiv)
  url: https://arxiv.org/abs/2302.09450
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
This work aims to push the limits of agility for bipedal robots by enabling a torque-controlled bipedal robot to perform robust and versatile dynamic jumps in the real world. We present a reinforcement learning framework for training a robot to accomplish a large variety of jumping tasks, such as jumping to different locations and directions. To improve performance on these challenging tasks, we develop a new policy structure that encodes the robot's long-term input/output (I/O) history while also providing direct access to a short-term I/O history. In order to train a versatile jumping policy, we utilize a multi-stage training scheme that includes different training stages for different objectives. After multi-stage training, the policy can be directly transferred to a real bipedal Cassie robot. Training on different tasks and exploring more diverse scenarios lead to highly robust policies that can exploit the diverse set of learned maneuvers to recover from perturbations or poor landings during real-world deployment. Such robustness in the proposed policy enables Cassie to succeed in completing a variety of challenging jump tasks in the real world, such as standing long jumps, jumping onto elevated platforms, and multi-axes jumps.

## 核心内容
This work aims to push the limits of agility for bipedal robots by enabling a torque-controlled bipedal robot to perform robust and versatile dynamic jumps in the real world. We present a reinforcement learning framework for training a robot to accomplish a large variety of jumping tasks, such as jumping to different locations and directions. To improve performance on these challenging tasks, we develop a new policy structure that encodes the robot's long-term input/output (I/O) history while also providing direct access to a short-term I/O history. In order to train a versatile jumping policy, we utilize a multi-stage training scheme that includes different training stages for different objectives. After multi-stage training, the policy can be directly transferred to a real bipedal Cassie robot. Training on different tasks and exploring more diverse scenarios lead to highly robust policies that can exploit the diverse set of learned maneuvers to recover from perturbations or poor landings during real-world deployment. Such robustness in the proposed policy enables Cassie to succeed in completing a variety of challenging jump tasks in the real world, such as standing long jumps, jumping onto elevated platforms, and multi-axes jumps.

## 参考
- http://arxiv.org/abs/2302.09450v2

