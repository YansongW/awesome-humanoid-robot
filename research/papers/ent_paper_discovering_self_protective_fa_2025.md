---
$id: ent_paper_discovering_self_protective_fa_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Discovering Self-Protective Falling Policy for Humanoid Robot via Deep Reinforcement Learning
  zh: Discovering Self-Protective Falling Policy for Humanoid Robot via Deep Reinforcement Learning
  ko: Discovering Self-Protective Falling Policy for Humanoid Robot via Deep Reinforcement Learning
summary:
  en: Discovering Self-Protective Falling Policy for Humanoid Robot via Deep Reinforcement Learning is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.
  zh: Discovering Self-Protective Falling Policy for Humanoid Robot via Deep Reinforcement Learning is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.
  ko: Discovering Self-Protective Falling Policy for Humanoid Robot via Deep Reinforcement Learning is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- discovering_self_protective_fa
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.01336v1.
sources:
- id: src_001
  type: paper
  title: Discovering Self-Protective Falling Policy for Humanoid Robot via Deep Reinforcement Learning (arXiv)
  url: https://arxiv.org/abs/2512.01336
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots have received significant research interests and advancements in recent years. Despite many successes, due to their morphology, dynamics and limitation of control policy, humanoid robots are prone to fall as compared to other embodiments like quadruped or wheeled robots. And its large weight, tall Center of Mass, high Degree-of-Freedom would cause serious hardware damages when falling uncontrolled, to both itself and surrounding objects. Existing researches in this field mostly focus on using control based methods that struggle to cater diverse falling scenarios and may introduce unsuitable human prior. On the other hand, large-scale Deep Reinforcement Learning and Curriculum Learning could be employed to incentivize humanoid agent discovering falling protection policy that fits its own nature and property. In this work, with carefully designed reward functions and domain diversification curriculum, we successfully train humanoid agent to explore falling protection behaviors and discover that by forming a `triangle' structure, the falling damages could be significantly reduced with its rigid-material body. With comprehensive metrics and experiments, we quantify its performance with comparison to other methods, visualize its falling behaviors and successfully transfer it to real world platform.

## 核心内容
Humanoid robots have received significant research interests and advancements in recent years. Despite many successes, due to their morphology, dynamics and limitation of control policy, humanoid robots are prone to fall as compared to other embodiments like quadruped or wheeled robots. And its large weight, tall Center of Mass, high Degree-of-Freedom would cause serious hardware damages when falling uncontrolled, to both itself and surrounding objects. Existing researches in this field mostly focus on using control based methods that struggle to cater diverse falling scenarios and may introduce unsuitable human prior. On the other hand, large-scale Deep Reinforcement Learning and Curriculum Learning could be employed to incentivize humanoid agent discovering falling protection policy that fits its own nature and property. In this work, with carefully designed reward functions and domain diversification curriculum, we successfully train humanoid agent to explore falling protection behaviors and discover that by forming a `triangle' structure, the falling damages could be significantly reduced with its rigid-material body. With comprehensive metrics and experiments, we quantify its performance with comparison to other methods, visualize its falling behaviors and successfully transfer it to real world platform.

## 参考
- http://arxiv.org/abs/2512.01336v1

