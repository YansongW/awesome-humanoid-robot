---
$id: ent_paper_real_world_humanoid_locomotion_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Real-World Humanoid Locomotion with Reinforcement Learning
  zh: Real-World Humanoid Locomotion with Reinforcement Learning
  ko: Real-World Humanoid Locomotion with Reinforcement Learning
summary:
  en: Real-World Humanoid Locomotion with Reinforcement Learning is a 2023 work on locomotion for humanoid robots.
  zh: Real-World Humanoid Locomotion with Reinforcement Learning is a 2023 work on locomotion for humanoid robots.
  ko: Real-World Humanoid Locomotion with Reinforcement Learning is a 2023 work on locomotion for humanoid robots.
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
- real_world_humanoid_locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2303.03381v2.
sources:
- id: src_001
  type: paper
  title: Real-World Humanoid Locomotion with Reinforcement Learning (arXiv)
  url: https://arxiv.org/abs/2303.03381
  date: '2023'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Real-World Humanoid Locomotion with Reinforcement Learning project page
  url: https://learning-humanoid-locomotion.github.io/
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots that can autonomously operate in diverse environments have the potential to help address labour shortages in factories, assist elderly at homes, and colonize new planets. While classical controllers for humanoid robots have shown impressive results in a number of settings, they are challenging to generalize and adapt to new environments. Here, we present a fully learning-based approach for real-world humanoid locomotion. Our controller is a causal transformer that takes the history of proprioceptive observations and actions as input and predicts the next action. We hypothesize that the observation-action history contains useful information about the world that a powerful transformer model can use to adapt its behavior in-context, without updating its weights. We train our model with large-scale model-free reinforcement learning on an ensemble of randomized environments in simulation and deploy it to the real world zero-shot. Our controller can walk over various outdoor terrains, is robust to external disturbances, and can adapt in context.

## 核心内容
Humanoid robots that can autonomously operate in diverse environments have the potential to help address labour shortages in factories, assist elderly at homes, and colonize new planets. While classical controllers for humanoid robots have shown impressive results in a number of settings, they are challenging to generalize and adapt to new environments. Here, we present a fully learning-based approach for real-world humanoid locomotion. Our controller is a causal transformer that takes the history of proprioceptive observations and actions as input and predicts the next action. We hypothesize that the observation-action history contains useful information about the world that a powerful transformer model can use to adapt its behavior in-context, without updating its weights. We train our model with large-scale model-free reinforcement learning on an ensemble of randomized environments in simulation and deploy it to the real world zero-shot. Our controller can walk over various outdoor terrains, is robust to external disturbances, and can adapt in context.

## 参考
- http://arxiv.org/abs/2303.03381v2

