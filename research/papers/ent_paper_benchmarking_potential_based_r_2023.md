---
$id: ent_paper_benchmarking_potential_based_r_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Benchmarking Potential Based Rewards for Learning Humanoid Locomotion
  zh: Benchmarking Potential Based Rewards for Learning Humanoid Locomotion
  ko: Benchmarking Potential Based Rewards for Learning Humanoid Locomotion
summary:
  en: Benchmarking Potential Based Rewards for Learning Humanoid Locomotion is a 2023 work on locomotion for humanoid robots.
  zh: Benchmarking Potential Based Rewards for Learning Humanoid Locomotion is a 2023 work on locomotion for humanoid robots.
  ko: Benchmarking Potential Based Rewards for Learning Humanoid Locomotion is a 2023 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmarking_potential_based_r
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2307.10142v1.
sources:
- id: src_001
  type: paper
  title: Benchmarking Potential Based Rewards for Learning Humanoid Locomotion (arXiv)
  url: https://arxiv.org/abs/2307.10142
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
The main challenge in developing effective reinforcement learning (RL) pipelines is often the design and tuning the reward functions. Well-designed shaping reward can lead to significantly faster learning. Naively formulated rewards, however, can conflict with the desired behavior and result in overfitting or even erratic performance if not properly tuned. In theory, the broad class of potential based reward shaping (PBRS) can help guide the learning process without affecting the optimal policy. Although several studies have explored the use of potential based reward shaping to accelerate learning convergence, most have been limited to grid-worlds and low-dimensional systems, and RL in robotics has predominantly relied on standard forms of reward shaping. In this paper, we benchmark standard forms of shaping with PBRS for a humanoid robot. We find that in this high-dimensional system, PBRS has only marginal benefits in convergence speed. However, the PBRS reward terms are significantly more robust to scaling than typical reward shaping approaches, and thus easier to tune.

## 核心内容
The main challenge in developing effective reinforcement learning (RL) pipelines is often the design and tuning the reward functions. Well-designed shaping reward can lead to significantly faster learning. Naively formulated rewards, however, can conflict with the desired behavior and result in overfitting or even erratic performance if not properly tuned. In theory, the broad class of potential based reward shaping (PBRS) can help guide the learning process without affecting the optimal policy. Although several studies have explored the use of potential based reward shaping to accelerate learning convergence, most have been limited to grid-worlds and low-dimensional systems, and RL in robotics has predominantly relied on standard forms of reward shaping. In this paper, we benchmark standard forms of shaping with PBRS for a humanoid robot. We find that in this high-dimensional system, PBRS has only marginal benefits in convergence speed. However, the PBRS reward terms are significantly more robust to scaling than typical reward shaping approaches, and thus easier to tune.

## 参考
- http://arxiv.org/abs/2307.10142v1

