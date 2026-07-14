---
$id: ent_paper_learning_social_navigation_fro_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications
  zh: Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications
  ko: Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications
summary:
  en: Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications is a 2025 work on
    navigation for humanoid robots.
  zh: Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications is a 2025 work on
    navigation for humanoid robots.
  ko: Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications is a 2025 work on
    navigation for humanoid robots.
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
- learning_social_navigation_fro
- navigation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.06779v1.
sources:
- id: src_001
  type: paper
  title: Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications (arXiv)
  url: https://arxiv.org/abs/2508.06779
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Bipedal robots demonstrate potential in navigating challenging terrains through dynamic ground contact. However, current frameworks often depend solely on proprioception or use manually designed visual pipelines, which are fragile in real-world settings and complicate real-time footstep planning in unstructured environments. To address this problem, we present a vision-based hierarchical control framework that integrates a reinforcement learning high-level footstep planner, which generates footstep commands based on a local elevation map, with a low-level Operational Space Controller that tracks the generated trajectories. We utilize the Angular Momentum Linear Inverted Pendulum model to construct a low-dimensional state representation to capture an informative encoding of the dynamics while reducing complexity. We evaluate our method across different terrain conditions using the underactuated bipedal robot Cassie and investigate the capabilities and challenges of our approach through simulation and hardware experiments.

## 核心内容
Bipedal robots demonstrate potential in navigating challenging terrains through dynamic ground contact. However, current frameworks often depend solely on proprioception or use manually designed visual pipelines, which are fragile in real-world settings and complicate real-time footstep planning in unstructured environments. To address this problem, we present a vision-based hierarchical control framework that integrates a reinforcement learning high-level footstep planner, which generates footstep commands based on a local elevation map, with a low-level Operational Space Controller that tracks the generated trajectories. We utilize the Angular Momentum Linear Inverted Pendulum model to construct a low-dimensional state representation to capture an informative encoding of the dynamics while reducing complexity. We evaluate our method across different terrain conditions using the underactuated bipedal robot Cassie and investigate the capabilities and challenges of our approach through simulation and hardware experiments.

## 参考
- http://arxiv.org/abs/2508.06779v1

