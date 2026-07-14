---
$id: ent_paper_symphony_a_heuristic_normalize_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Symphony: A Heuristic Normalized Calibrated Advantage Actor and Critic Algorithm in application for Humanoid Robots'
  zh: 'Symphony: A Heuristic Normalized Calibrated Advantage Actor and Critic Algorithm in application for Humanoid Robots'
  ko: 'Symphony: A Heuristic Normalized Calibrated Advantage Actor and Critic Algorithm in application for Humanoid Robots'
summary:
  en: 'Symphony: A Heuristic Normalized Calibrated Advantage Actor and Critic Algorithm in application for Humanoid Robots
    is a 2025 work on locomotion for humanoid robots.'
  zh: 'Symphony: A Heuristic Normalized Calibrated Advantage Actor and Critic Algorithm in application for Humanoid Robots
    is a 2025 work on locomotion for humanoid robots.'
  ko: 'Symphony: A Heuristic Normalized Calibrated Advantage Actor and Critic Algorithm in application for Humanoid Robots
    is a 2025 work on locomotion for humanoid robots.'
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
- symphony
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.10477v8.
sources:
- id: src_001
  type: paper
  title: 'Symphony: A Heuristic Normalized Calibrated Advantage Actor and Critic Algorithm in application for Humanoid Robots
    (arXiv)'
  url: https://arxiv.org/abs/2512.10477
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In our work we implicitly suggest that it is a misconception to think that humans learn fast. The learning process takes time. Babies start learning to move in the restricted fluid environment of the womb. Children are often limited by underdeveloped body. Even adults are not allowed to participate in complex competitions right away. However, with robots, when learning from scratch, we often don't have the privilege of waiting for tens of millions of steps. "Swaddling" regularization is responsible for restraining an agent in rapid but unstable development penalizing action strength in a specific way not affecting actions directly. The Symphony, Transitional-policy Deterministic Actor and Critic algorithm, is a concise combination of different ideas for possibility of training humanoid robots from scratch with Sample Efficiency, Sample Proximity and Safety of Actions in mind. It is well known that continuous increase in Gaussian noise without appropriate smoothing is harmful for motors and gearboxes. Compared to Stochastic algorithms, we set limited parametric noise and promote a reduced strength of actions, safely increasing entropy, since the actions are submerged in weaker noise. When actions require more extreme values, actions rise above the weak noise. Training becomes empirically much safer for both the environment around and the robot's mechanisms. We use Fading Replay Buffer: using a fixed formula containing the hyperbolic tangent, we adjust the batch sampling probability: the memory contains a recent memory and a long-term memory trail. Fading Replay Buffer allows us to use Temporal Advantage when we improve the current Critic Network prediction compared to the exponential moving average. Temporal Advantage allows us to update the Actor and Critic in one pass, as well as combine the Actor and Critic in one Object and implement their Losses in one line.

## 核心内容
In our work we implicitly suggest that it is a misconception to think that humans learn fast. The learning process takes time. Babies start learning to move in the restricted fluid environment of the womb. Children are often limited by underdeveloped body. Even adults are not allowed to participate in complex competitions right away. However, with robots, when learning from scratch, we often don't have the privilege of waiting for tens of millions of steps. "Swaddling" regularization is responsible for restraining an agent in rapid but unstable development penalizing action strength in a specific way not affecting actions directly. The Symphony, Transitional-policy Deterministic Actor and Critic algorithm, is a concise combination of different ideas for possibility of training humanoid robots from scratch with Sample Efficiency, Sample Proximity and Safety of Actions in mind. It is well known that continuous increase in Gaussian noise without appropriate smoothing is harmful for motors and gearboxes. Compared to Stochastic algorithms, we set limited parametric noise and promote a reduced strength of actions, safely increasing entropy, since the actions are submerged in weaker noise. When actions require more extreme values, actions rise above the weak noise. Training becomes empirically much safer for both the environment around and the robot's mechanisms. We use Fading Replay Buffer: using a fixed formula containing the hyperbolic tangent, we adjust the batch sampling probability: the memory contains a recent memory and a long-term memory trail. Fading Replay Buffer allows us to use Temporal Advantage when we improve the current Critic Network prediction compared to the exponential moving average. Temporal Advantage allows us to update the Actor and Critic in one pass, as well as combine the Actor and Critic in one Object and implement their Losses in one line.

## 参考
- http://arxiv.org/abs/2512.10477v8

