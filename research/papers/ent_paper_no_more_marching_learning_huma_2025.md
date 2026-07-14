---
$id: ent_paper_no_more_marching_learning_huma_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'No More Marching: Learning Humanoid Locomotion for Short-Range SE(2) Targets'
  zh: 'No More Marching: Learning Humanoid Locomotion for Short-Range SE(2) Targets'
  ko: 'No More Marching: Learning Humanoid Locomotion for Short-Range SE(2) Targets'
summary:
  en: 'No More Marching: Learning Humanoid Locomotion for Short-Range SE(2) Targets is a 2025 work on locomotion for humanoid
    robots.'
  zh: 'No More Marching: Learning Humanoid Locomotion for Short-Range SE(2) Targets is a 2025 work on locomotion for humanoid
    robots.'
  ko: 'No More Marching: Learning Humanoid Locomotion for Short-Range SE(2) Targets is a 2025 work on locomotion for humanoid
    robots.'
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
- no_more_marching
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.14098v2.
sources:
- id: src_001
  type: paper
  title: 'No More Marching: Learning Humanoid Locomotion for Short-Range SE(2) Targets (arXiv)'
  url: https://arxiv.org/abs/2508.14098
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoids operating in real-world workspaces must frequently execute task-driven, short-range movements to SE(2) target poses. To be practical, these transitions must be fast, robust, and energy efficient. While learning-based locomotion has made significant progress, most existing methods optimize for velocity-tracking rather than direct pose reaching, resulting in inefficient, marching-style behavior when applied to short-range tasks. In this work, we develop a reinforcement learning approach that directly optimizes humanoid locomotion for SE(2) targets. Central to this approach is a new constellation-based reward function that encourages natural and efficient target-oriented movement. To evaluate performance, we introduce a benchmarking framework that measures energy consumption, time-to-target, and footstep count on a distribution of SE(2) goals. Our results show that the proposed approach consistently outperforms standard methods and enables successful transfer from simulation to hardware, highlighting the importance of targeted reward design for practical short-range humanoid locomotion.

## 核心内容
Humanoids operating in real-world workspaces must frequently execute task-driven, short-range movements to SE(2) target poses. To be practical, these transitions must be fast, robust, and energy efficient. While learning-based locomotion has made significant progress, most existing methods optimize for velocity-tracking rather than direct pose reaching, resulting in inefficient, marching-style behavior when applied to short-range tasks. In this work, we develop a reinforcement learning approach that directly optimizes humanoid locomotion for SE(2) targets. Central to this approach is a new constellation-based reward function that encourages natural and efficient target-oriented movement. To evaluate performance, we introduce a benchmarking framework that measures energy consumption, time-to-target, and footstep count on a distribution of SE(2) goals. Our results show that the proposed approach consistently outperforms standard methods and enables successful transfer from simulation to hardware, highlighting the importance of targeted reward design for practical short-range humanoid locomotion.

## 参考
- http://arxiv.org/abs/2508.14098v2

