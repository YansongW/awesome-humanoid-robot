---
$id: ent_paper_preference_conditioned_multi_o_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Preference-Conditioned Multi-Objective RL for Integrated Command Tracking and Force Compliance in Humanoid Locomotion
  zh: Preference-Conditioned Multi-Objective RL for Integrated Command Tracking and Force Compliance in Humanoid Locomotion
  ko: Preference-Conditioned Multi-Objective RL for Integrated Command Tracking and Force Compliance in Humanoid Locomotion
summary:
  en: Preference-Conditioned Multi-Objective RL for Integrated Command Tracking and Force Compliance in Humanoid Locomotion
    is a 2025 work on locomotion for humanoid robots.
  zh: Preference-Conditioned Multi-Objective RL for Integrated Command Tracking and Force Compliance in Humanoid Locomotion
    is a 2025 work on locomotion for humanoid robots.
  ko: Preference-Conditioned Multi-Objective RL for Integrated Command Tracking and Force Compliance in Humanoid Locomotion
    is a 2025 work on locomotion for humanoid robots.
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
- preference_conditioned_multi_o
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.10851v2.
sources:
- id: src_001
  type: paper
  title: Preference-Conditioned Multi-Objective RL for Integrated Command Tracking and Force Compliance in Humanoid Locomotion
    (arXiv)
  url: https://arxiv.org/abs/2510.10851
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid locomotion requires not only accurate command tracking for navigation but also compliant responses to external forces during human interaction. Despite significant progress, existing RL approaches mainly emphasize robustness, yielding policies that resist external forces but lack compliance particularly challenging for inherently unstable humanoids. In this work, we address this by formulating humanoid locomotion as a multi-objective optimization problem that balances command tracking and external force compliance. We introduce a preference-conditioned multi-objective RL (MORL) framework that enables a single omnidirectional locomotion policy to trade off between command following and force compliance via a user-specified preference input. External forces are modeled via velocity-resistance factor for consistent reward design, and training leverages an encoder-decoder structure that infers task-relevant privileged features from deployable observations. We validate our approach in both simulation and real-world experiments on a humanoid robot. Experimental results in simulation and on hardware show that the framework trains stably and enables deployable preference-conditioned humanoid locomotion.

## 核心内容
Humanoid locomotion requires not only accurate command tracking for navigation but also compliant responses to external forces during human interaction. Despite significant progress, existing RL approaches mainly emphasize robustness, yielding policies that resist external forces but lack compliance particularly challenging for inherently unstable humanoids. In this work, we address this by formulating humanoid locomotion as a multi-objective optimization problem that balances command tracking and external force compliance. We introduce a preference-conditioned multi-objective RL (MORL) framework that enables a single omnidirectional locomotion policy to trade off between command following and force compliance via a user-specified preference input. External forces are modeled via velocity-resistance factor for consistent reward design, and training leverages an encoder-decoder structure that infers task-relevant privileged features from deployable observations. We validate our approach in both simulation and real-world experiments on a humanoid robot. Experimental results in simulation and on hardware show that the framework trains stably and enables deployable preference-conditioned humanoid locomotion.

## 参考
- http://arxiv.org/abs/2510.10851v2

