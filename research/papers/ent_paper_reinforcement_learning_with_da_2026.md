---
$id: ent_paper_reinforcement_learning_with_da_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation
  zh: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation
  ko: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation
summary:
  en: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation is a paper on
    Navigation for humanoid robotics.
  zh: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation is a paper on
    Navigation for humanoid robotics.
  ko: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation is a paper on
    Navigation for humanoid robotics.
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
- reinforcement_learning_with_da
theoretical_depth:
- system
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.02206v1.
sources:
- id: src_001
  type: website
  title: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation
  url: ''
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Safe and real-time navigation is fundamental for humanoid robot applications. However, existing bipedal robot navigation frameworks often struggle to balance computational efficiency with the precision required for stable locomotion. We propose a novel hierarchical framework that continuously generates dynamic subgoals to guide the robot through cluttered environments. Our method comprises a high-level reinforcement learning (RL) planner for subgoal selection in a robot-centric coordinate system and a low-level Model Predictive Control (MPC) based planner which produces robust walking gaits to reach these subgoals. To expedite and stabilize the training process, we incorporate a data bootstrapping technique that leverages a model-based navigation approach to generate a diverse, informative dataset. We validate our method in simulation using the Agility Robotics Digit humanoid across multiple scenarios with random obstacles. Results show that our framework significantly improves navigation success rates and adaptability compared to both the original model-based method and other learning-based methods.

## 核心内容
Safe and real-time navigation is fundamental for humanoid robot applications. However, existing bipedal robot navigation frameworks often struggle to balance computational efficiency with the precision required for stable locomotion. We propose a novel hierarchical framework that continuously generates dynamic subgoals to guide the robot through cluttered environments. Our method comprises a high-level reinforcement learning (RL) planner for subgoal selection in a robot-centric coordinate system and a low-level Model Predictive Control (MPC) based planner which produces robust walking gaits to reach these subgoals. To expedite and stabilize the training process, we incorporate a data bootstrapping technique that leverages a model-based navigation approach to generate a diverse, informative dataset. We validate our method in simulation using the Agility Robotics Digit humanoid across multiple scenarios with random obstacles. Results show that our framework significantly improves navigation success rates and adaptability compared to both the original model-based method and other learning-based methods.

## 参考
- http://arxiv.org/abs/2506.02206v1

