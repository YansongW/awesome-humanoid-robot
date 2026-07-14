---
$id: ent_paper_fasttd3_simple_fast_and_capabl_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FastTD3: Simple, Fast, and Capable Reinforcement Learning for Humanoid Control'
  zh: 'FastTD3: Simple, Fast, and Capable Reinforcement Learning for Humanoid Control'
  ko: 'FastTD3: Simple, Fast, and Capable Reinforcement Learning for Humanoid Control'
summary:
  en: 'FastTD3: Simple, Fast, and Capable Reinforcement Learning for Humanoid Control is a 2025 work on locomotion for humanoid
    robots.'
  zh: 'FastTD3: Simple, Fast, and Capable Reinforcement Learning for Humanoid Control is a 2025 work on locomotion for humanoid
    robots.'
  ko: 'FastTD3: Simple, Fast, and Capable Reinforcement Learning for Humanoid Control is a 2025 work on locomotion for humanoid
    robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- fasttd3
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.22642v3.
sources:
- id: src_001
  type: paper
  title: 'FastTD3: Simple, Fast, and Capable Reinforcement Learning for Humanoid Control (arXiv)'
  url: https://arxiv.org/abs/2505.22642
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'FastTD3: Simple, Fast, and Capable Reinforcement Learning for Humanoid Control project page'
  url: https://younggyo.me/fast_td3/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning (RL) has driven significant progress in robotics, but its complexity and long training times remain major bottlenecks. In this report, we introduce FastTD3, a simple, fast, and capable RL algorithm that significantly speeds up training for humanoid robots in popular suites such as HumanoidBench, IsaacLab, and MuJoCo Playground. Our recipe is remarkably simple: we train an off-policy TD3 agent with several modifications -- parallel simulation, large-batch updates, a distributional critic, and carefully tuned hyperparameters. FastTD3 solves a range of HumanoidBench tasks in under 3 hours on a single A100 GPU, while remaining stable during training. We also provide a lightweight and easy-to-use implementation of FastTD3 to accelerate RL research in robotics.

## 核心内容
Reinforcement learning (RL) has driven significant progress in robotics, but its complexity and long training times remain major bottlenecks. In this report, we introduce FastTD3, a simple, fast, and capable RL algorithm that significantly speeds up training for humanoid robots in popular suites such as HumanoidBench, IsaacLab, and MuJoCo Playground. Our recipe is remarkably simple: we train an off-policy TD3 agent with several modifications -- parallel simulation, large-batch updates, a distributional critic, and carefully tuned hyperparameters. FastTD3 solves a range of HumanoidBench tasks in under 3 hours on a single A100 GPU, while remaining stable during training. We also provide a lightweight and easy-to-use implementation of FastTD3 to accelerate RL research in robotics.

## 参考
- http://arxiv.org/abs/2505.22642v3

