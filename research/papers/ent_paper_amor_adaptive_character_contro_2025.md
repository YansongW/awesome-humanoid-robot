---
$id: ent_paper_amor_adaptive_character_contro_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AMOR: Adaptive Character Control through Multi-Objective Reinforcement Learning'
  zh: 'AMOR: Adaptive Character Control through Multi-Objective Reinforcement Learning'
  ko: 'AMOR: Adaptive Character Control through Multi-Objective Reinforcement Learning'
summary:
  en: 'AMOR: Adaptive Character Control through Multi-Objective Reinforcement Learning is a 2025 work on physics-based character
    animation for humanoid robots.'
  zh: 'AMOR: Adaptive Character Control through Multi-Objective Reinforcement Learning is a 2025 work on physics-based character
    animation for humanoid robots.'
  ko: 'AMOR: Adaptive Character Control through Multi-Objective Reinforcement Learning is a 2025 work on physics-based character
    animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- amor
- character_animation
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.23708v1.
sources:
- id: src_001
  type: paper
  title: 'AMOR: Adaptive Character Control through Multi-Objective Reinforcement Learning (arXiv)'
  url: https://arxiv.org/abs/2505.23708
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning (RL) has significantly advanced the control of physics-based and robotic characters that track kinematic reference motion. However, methods typically rely on a weighted sum of conflicting reward functions, requiring extensive tuning to achieve a desired behavior. Due to the computational cost of RL, this iterative process is a tedious, time-intensive task. Furthermore, for robotics applications, the weights need to be chosen such that the policy performs well in the real world, despite inevitable sim-to-real gaps. To address these challenges, we propose a multi-objective reinforcement learning framework that trains a single policy conditioned on a set of weights, spanning the Pareto front of reward trade-offs. Within this framework, weights can be selected and tuned after training, significantly speeding up iteration time. We demonstrate how this improved workflow can be used to perform highly dynamic motions with a robot character. Moreover, we explore how weight-conditioned policies can be leveraged in hierarchical settings, using a high-level policy to dynamically select weights according to the current task. We show that the multi-objective policy encodes a diverse spectrum of behaviors, facilitating efficient adaptation to novel tasks.

## 核心内容
Reinforcement learning (RL) has significantly advanced the control of physics-based and robotic characters that track kinematic reference motion. However, methods typically rely on a weighted sum of conflicting reward functions, requiring extensive tuning to achieve a desired behavior. Due to the computational cost of RL, this iterative process is a tedious, time-intensive task. Furthermore, for robotics applications, the weights need to be chosen such that the policy performs well in the real world, despite inevitable sim-to-real gaps. To address these challenges, we propose a multi-objective reinforcement learning framework that trains a single policy conditioned on a set of weights, spanning the Pareto front of reward trade-offs. Within this framework, weights can be selected and tuned after training, significantly speeding up iteration time. We demonstrate how this improved workflow can be used to perform highly dynamic motions with a robot character. Moreover, we explore how weight-conditioned policies can be leveraged in hierarchical settings, using a high-level policy to dynamically select weights according to the current task. We show that the multi-objective policy encodes a diverse spectrum of behaviors, facilitating efficient adaptation to novel tasks.

## 参考
- http://arxiv.org/abs/2505.23708v1

