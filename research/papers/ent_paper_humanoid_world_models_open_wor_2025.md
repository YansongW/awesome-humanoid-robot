---
$id: ent_paper_humanoid_world_models_open_wor_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Humanoid World Models: Open World Foundation Models for Humanoid Robotics'
  zh: 'Humanoid World Models: Open World Foundation Models for Humanoid Robotics'
  ko: 'Humanoid World Models: Open World Foundation Models for Humanoid Robotics'
summary:
  en: 'Humanoid World Models: Open World Foundation Models for Humanoid Robotics is a 2025 work on simulation benchmark for
    humanoid robots.'
  zh: 'Humanoid World Models: Open World Foundation Models for Humanoid Robotics is a 2025 work on simulation benchmark for
    humanoid robots.'
  ko: 'Humanoid World Models: Open World Foundation Models for Humanoid Robotics is a 2025 work on simulation benchmark for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmark
- humanoid
- humanoid_world_models
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.01182v2.
sources:
- id: src_001
  type: paper
  title: 'Humanoid World Models: Open World Foundation Models for Humanoid Robotics (arXiv)'
  url: https://arxiv.org/abs/2506.01182
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots, with their human-like form, are uniquely suited for interacting in environments built for people. However, enabling humanoids to reason, plan, and act in complex open-world settings remains a challenge. World models, models that predict the future outcome of a given action, can support these capabilities by serving as a dynamics model in long-horizon planning and generating synthetic data for policy learning. We introduce Humanoid World Models (HWM), a family of lightweight, open-source models that forecast future egocentric video conditioned on humanoid control tokens. We train two types of generative models, Masked Transformers and Flow-Matching, on 100 hours of humanoid demonstrations. Additionally, we explore architectural variants with different attention mechanisms and parameter-sharing strategies. Our parameter-sharing techniques reduce model size by 33-53% with minimal impact on performance or visual fidelity. HWMs are designed to be trained and deployed in practical academic and small-lab settings, such as 1-2 GPUs.

## 核心内容
Humanoid robots, with their human-like form, are uniquely suited for interacting in environments built for people. However, enabling humanoids to reason, plan, and act in complex open-world settings remains a challenge. World models, models that predict the future outcome of a given action, can support these capabilities by serving as a dynamics model in long-horizon planning and generating synthetic data for policy learning. We introduce Humanoid World Models (HWM), a family of lightweight, open-source models that forecast future egocentric video conditioned on humanoid control tokens. We train two types of generative models, Masked Transformers and Flow-Matching, on 100 hours of humanoid demonstrations. Additionally, we explore architectural variants with different attention mechanisms and parameter-sharing strategies. Our parameter-sharing techniques reduce model size by 33-53% with minimal impact on performance or visual fidelity. HWMs are designed to be trained and deployed in practical academic and small-lab settings, such as 1-2 GPUs.

## 参考
- http://arxiv.org/abs/2506.01182v2

