---
$id: ent_paper_rl_with_data_bootstrapping_for_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: RL with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation
  zh: RL with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation
  ko: RL with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation
summary:
  en: RL with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation is a 2025 work on navigation for
    humanoid robots.
  zh: RL with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation is a 2025 work on navigation for
    humanoid robots.
  ko: RL with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation is a 2025 work on navigation for
    humanoid robots.
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
- navigation
- rl_with_data_bootstrapping_for
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.02206v1.
sources:
- id: src_001
  type: paper
  title: RL with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation (arXiv)
  url: https://arxiv.org/abs/2506.02206
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Safe and real-time navigation is fundamental for humanoid robot applications. However, existing bipedal robot navigation frameworks often struggle to balance computational efficiency with the precision required for stable locomotion. We propose a novel hierarchical framework that continuously generates dynamic subgoals to guide the robot through cluttered environments. Our method comprises a high-level reinforcement learning (RL) planner for subgoal selection in a robot-centric coordinate system and a low-level Model Predictive Control (MPC) based planner which produces robust walking gaits to reach these subgoals. To expedite and stabilize the training process, we incorporate a data bootstrapping technique that leverages a model-based navigation approach to generate a diverse, informative dataset. We validate our method in simulation using the Agility Robotics Digit humanoid across multiple scenarios with random obstacles. Results show that our framework significantly improves navigation success rates and adaptability compared to both the original model-based method and other learning-based methods.

## 核心内容
Safe and real-time navigation is fundamental for humanoid robot applications. However, existing bipedal robot navigation frameworks often struggle to balance computational efficiency with the precision required for stable locomotion. We propose a novel hierarchical framework that continuously generates dynamic subgoals to guide the robot through cluttered environments. Our method comprises a high-level reinforcement learning (RL) planner for subgoal selection in a robot-centric coordinate system and a low-level Model Predictive Control (MPC) based planner which produces robust walking gaits to reach these subgoals. To expedite and stabilize the training process, we incorporate a data bootstrapping technique that leverages a model-based navigation approach to generate a diverse, informative dataset. We validate our method in simulation using the Agility Robotics Digit humanoid across multiple scenarios with random obstacles. Results show that our framework significantly improves navigation success rates and adaptability compared to both the original model-based method and other learning-based methods.

## 参考
- http://arxiv.org/abs/2506.02206v1

