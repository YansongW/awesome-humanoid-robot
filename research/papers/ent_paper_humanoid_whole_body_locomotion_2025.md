---
$id: ent_paper_humanoid_whole_body_locomotion_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning
  zh: Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning
  ko: Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning
summary:
  en: Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning is a 2025 work on locomotion
    for humanoid robots.
  zh: Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning is a 2025 work on locomotion
    for humanoid robots.
  ko: Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning is a 2025 work on locomotion
    for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- humanoid_whole_body_locomotion
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.17219v2.
sources:
- id: src_001
  type: paper
  title: Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning (arXiv)
  url: https://arxiv.org/abs/2502.17219
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humans possess delicate dynamic balance mechanisms that enable them to maintain stability across diverse terrains and under extreme conditions. However, despite significant advances recently, existing locomotion algorithms for humanoid robots are still struggle to traverse extreme environments, especially in cases that lack external perception (e.g., vision or LiDAR). This is because current methods often rely on gait-based or perception-condition rewards, lacking effective mechanisms to handle unobservable obstacles and sudden balance loss. To address this challenge, we propose a novel whole-body locomotion algorithm based on dynamic balance and Reinforcement Learning (RL) that enables humanoid robots to traverse extreme terrains, particularly narrow pathways and unexpected obstacles, using only proprioception. Specifically, we introduce a dynamic balance mechanism by leveraging an extended measure of Zero-Moment Point (ZMP)-driven rewards and task-driven rewards in a whole-body actor-critic framework, aiming to achieve coordinated actions of the upper and lower limbs for robust locomotion. Experiments conducted on a full-sized Unitree H1-2 robot verify the ability of our method to maintain balance on extremely narrow terrains and under external disturbances, demonstrating its effectiveness in enhancing the robot's adaptability to complex environments. The videos are given at https://whole-body-loco.github.io.

## 核心内容
Humans possess delicate dynamic balance mechanisms that enable them to maintain stability across diverse terrains and under extreme conditions. However, despite significant advances recently, existing locomotion algorithms for humanoid robots are still struggle to traverse extreme environments, especially in cases that lack external perception (e.g., vision or LiDAR). This is because current methods often rely on gait-based or perception-condition rewards, lacking effective mechanisms to handle unobservable obstacles and sudden balance loss. To address this challenge, we propose a novel whole-body locomotion algorithm based on dynamic balance and Reinforcement Learning (RL) that enables humanoid robots to traverse extreme terrains, particularly narrow pathways and unexpected obstacles, using only proprioception. Specifically, we introduce a dynamic balance mechanism by leveraging an extended measure of Zero-Moment Point (ZMP)-driven rewards and task-driven rewards in a whole-body actor-critic framework, aiming to achieve coordinated actions of the upper and lower limbs for robust locomotion. Experiments conducted on a full-sized Unitree H1-2 robot verify the ability of our method to maintain balance on extremely narrow terrains and under external disturbances, demonstrating its effectiveness in enhancing the robot's adaptability to complex environments. The videos are given at https://whole-body-loco.github.io.

## 参考
- http://arxiv.org/abs/2502.17219v2

