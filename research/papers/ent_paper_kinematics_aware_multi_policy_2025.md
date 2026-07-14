---
$id: ent_paper_kinematics_aware_multi_policy_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Kinematics-Aware Multi-Policy Reinforcement Learning for Force-Capable Humanoid Loco-Manipulation
  zh: Kinematics-Aware Multi-Policy Reinforcement Learning for Force-Capable Humanoid Loco-Manipulation
  ko: Kinematics-Aware Multi-Policy Reinforcement Learning for Force-Capable Humanoid Loco-Manipulation
summary:
  en: Kinematics-Aware Multi-Policy Reinforcement Learning for Force-Capable Humanoid Loco-Manipulation is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.
  zh: Kinematics-Aware Multi-Policy Reinforcement Learning for Force-Capable Humanoid Loco-Manipulation is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.
  ko: Kinematics-Aware Multi-Policy Reinforcement Learning for Force-Capable Humanoid Loco-Manipulation is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- kinematics_aware_multi_policy
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.21169v1.
sources:
- id: src_001
  type: paper
  title: Kinematics-Aware Multi-Policy Reinforcement Learning for Force-Capable Humanoid Loco-Manipulation (arXiv)
  url: https://arxiv.org/abs/2511.21169
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots, with their human-like morphology, hold great potential for industrial applications. However, existing loco-manipulation methods primarily focus on dexterous manipulation, falling short of the combined requirements for dexterity and proactive force interaction in high-load industrial scenarios. To bridge this gap, we propose a reinforcement learning-based framework with a decoupled three-stage training pipeline, consisting of an upper-body policy, a lower-body policy, and a delta-command policy. To accelerate upper-body training, a heuristic reward function is designed. By implicitly embedding forward kinematics priors, it enables the policy to converge faster and achieve superior performance. For the lower body, a force-based curriculum learning strategy is developed, enabling the robot to actively exert and regulate interaction forces with the environment.

## 核心内容
Humanoid robots, with their human-like morphology, hold great potential for industrial applications. However, existing loco-manipulation methods primarily focus on dexterous manipulation, falling short of the combined requirements for dexterity and proactive force interaction in high-load industrial scenarios. To bridge this gap, we propose a reinforcement learning-based framework with a decoupled three-stage training pipeline, consisting of an upper-body policy, a lower-body policy, and a delta-command policy. To accelerate upper-body training, a heuristic reward function is designed. By implicitly embedding forward kinematics priors, it enables the policy to converge faster and achieve superior performance. For the lower body, a force-based curriculum learning strategy is developed, enabling the robot to actively exert and regulate interaction forces with the environment.

## 参考
- http://arxiv.org/abs/2511.21169v1

