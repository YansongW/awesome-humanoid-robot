---
$id: ent_paper_success_in_humanoid_reinforcem_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Success in Humanoid Reinforcement Learning under Partial Observation
  zh: Success in Humanoid Reinforcement Learning under Partial Observation
  ko: Success in Humanoid Reinforcement Learning under Partial Observation
summary:
  en: Success in Humanoid Reinforcement Learning under Partial Observation is a 2025 work on locomotion for humanoid robots.
  zh: Success in Humanoid Reinforcement Learning under Partial Observation is a 2025 work on locomotion for humanoid robots.
  ko: Success in Humanoid Reinforcement Learning under Partial Observation is a 2025 work on locomotion for humanoid robots.
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
- success_in_humanoid_reinforcem
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.18883v1.
sources:
- id: src_001
  type: paper
  title: Success in Humanoid Reinforcement Learning under Partial Observation (arXiv)
  url: https://arxiv.org/abs/2507.18883
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning has been widely applied to robotic control, but effective policy learning under partial observability remains a major challenge, especially in high-dimensional tasks like humanoid locomotion. To date, no prior work has demonstrated stable training of humanoid policies with incomplete state information in the benchmark Gymnasium Humanoid-v4 environment. The objective in this environment is to walk forward as fast as possible without falling, with rewards provided for staying upright and moving forward, and penalties incurred for excessive actions and external contact forces. This research presents the first successful instance of learning under partial observability in this environment. The learned policy achieves performance comparable to state-of-the-art results with full state access, despite using only one-third to two-thirds of the original states. Moreover, the policy exhibits adaptability to robot properties, such as variations in body part masses. The key to this success is a novel history encoder that processes a fixed-length sequence of past observations in parallel. Integrated into a standard model-free algorithm, the encoder enables performance on par with fully observed baselines. We hypothesize that it reconstructs essential contextual information from recent observations, thereby enabling robust decision-making.

## 核心内容
Reinforcement learning has been widely applied to robotic control, but effective policy learning under partial observability remains a major challenge, especially in high-dimensional tasks like humanoid locomotion. To date, no prior work has demonstrated stable training of humanoid policies with incomplete state information in the benchmark Gymnasium Humanoid-v4 environment. The objective in this environment is to walk forward as fast as possible without falling, with rewards provided for staying upright and moving forward, and penalties incurred for excessive actions and external contact forces. This research presents the first successful instance of learning under partial observability in this environment. The learned policy achieves performance comparable to state-of-the-art results with full state access, despite using only one-third to two-thirds of the original states. Moreover, the policy exhibits adaptability to robot properties, such as variations in body part masses. The key to this success is a novel history encoder that processes a fixed-length sequence of past observations in parallel. Integrated into a standard model-free algorithm, the encoder enables performance on par with fully observed baselines. We hypothesize that it reconstructs essential contextual information from recent observations, thereby enabling robust decision-making.

## 参考
- http://arxiv.org/abs/2507.18883v1

