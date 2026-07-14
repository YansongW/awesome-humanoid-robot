---
$id: ent_paper_stabilizing_humanoid_robot_tra_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Stabilizing Humanoid Robot Trajectory Generation via Physics-Informed Learning
  zh: Stabilizing Humanoid Robot Trajectory Generation via Physics-Informed Learning
  ko: Stabilizing Humanoid Robot Trajectory Generation via Physics-Informed Learning
summary:
  en: Stabilizing Humanoid Robot Trajectory Generation via Physics-Informed Learning is a 2025 work on locomotion for humanoid
    robots.
  zh: Stabilizing Humanoid Robot Trajectory Generation via Physics-Informed Learning is a 2025 work on locomotion for humanoid
    robots.
  ko: Stabilizing Humanoid Robot Trajectory Generation via Physics-Informed Learning is a 2025 work on locomotion for humanoid
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
- stabilizing_humanoid_robot_tra
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.24697v1.
sources:
- id: src_001
  type: paper
  title: Stabilizing Humanoid Robot Trajectory Generation via Physics-Informed Learning (arXiv)
  url: https://arxiv.org/abs/2509.24697
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent trends in humanoid robot control have successfully employed imitation learning to enable the learned generation of smooth, human-like trajectories from human data. While these approaches make more realistic motions possible, they are limited by the amount of available motion data, and do not incorporate prior knowledge about the physical laws governing the system and its interactions with the environment. Thus they may violate such laws, leading to divergent trajectories and sliding contacts which limit real-world stability. We address such limitations via a two-pronged learning strategy which leverages the known physics of the system and fundamental control principles. First, we encode physics priors during supervised imitation learning to promote trajectory feasibility. Second, we minimize drift at inference time by applying a proportional-integral controller directly to the generated output state. We validate our method on various locomotion behaviors for the ergoCub humanoid robot, where a physics-informed loss encourages zero contact foot velocity. Our experiments demonstrate that the proposed approach is compatible with multiple controllers on a real robot and significantly improves the accuracy and physical constraint conformity of generated trajectories.

## 核心内容
Recent trends in humanoid robot control have successfully employed imitation learning to enable the learned generation of smooth, human-like trajectories from human data. While these approaches make more realistic motions possible, they are limited by the amount of available motion data, and do not incorporate prior knowledge about the physical laws governing the system and its interactions with the environment. Thus they may violate such laws, leading to divergent trajectories and sliding contacts which limit real-world stability. We address such limitations via a two-pronged learning strategy which leverages the known physics of the system and fundamental control principles. First, we encode physics priors during supervised imitation learning to promote trajectory feasibility. Second, we minimize drift at inference time by applying a proportional-integral controller directly to the generated output state. We validate our method on various locomotion behaviors for the ergoCub humanoid robot, where a physics-informed loss encourages zero contact foot velocity. Our experiments demonstrate that the proposed approach is compatible with multiple controllers on a real robot and significantly improves the accuracy and physical constraint conformity of generated trajectories.

## 参考
- http://arxiv.org/abs/2509.24697v1

