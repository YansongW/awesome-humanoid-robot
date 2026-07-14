---
$id: ent_paper_learning_a_vision_based_footst_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning a Vision-Based Footstep Planner for Hierarchical Walking Control
  zh: Learning a Vision-Based Footstep Planner for Hierarchical Walking Control
  ko: Learning a Vision-Based Footstep Planner for Hierarchical Walking Control
summary:
  en: Learning a Vision-Based Footstep Planner for Hierarchical Walking Control is a 2025 work on locomotion for humanoid
    robots.
  zh: Learning a Vision-Based Footstep Planner for Hierarchical Walking Control is a 2025 work on locomotion for humanoid
    robots.
  ko: Learning a Vision-Based Footstep Planner for Hierarchical Walking Control is a 2025 work on locomotion for humanoid
    robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_a_vision_based_footst
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.12215v1.
sources:
- id: src_001
  type: paper
  title: Learning a Vision-Based Footstep Planner for Hierarchical Walking Control (arXiv)
  url: https://arxiv.org/abs/2510.12215
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Mobile robot navigation in dynamic human environments requires policies that balance adaptability to diverse behaviors with compliance to safety constraints. We hypothesize that integrating data-driven rewards with rule-based objectives enables navigation policies to achieve a more effective balance of adaptability and safety. To this end, we develop a framework that learns a density-based reward from positive and negative demonstrations and augments it with rule-based objectives for obstacle avoidance and goal reaching. A sampling-based lookahead controller produces supervisory actions that are both safe and adaptive, which are subsequently distilled into a compact student policy suitable for real-time operation with uncertainty estimates. Experiments in synthetic and elevator co-boarding simulations show consistent gains in success rate and time efficiency over baselines, and real-world demonstrations with human participants confirm the practicality of deployment. A video illustrating this work can be found on our project page https://chanwookim971024.github.io/PioneeR/.

## 核心内容
Mobile robot navigation in dynamic human environments requires policies that balance adaptability to diverse behaviors with compliance to safety constraints. We hypothesize that integrating data-driven rewards with rule-based objectives enables navigation policies to achieve a more effective balance of adaptability and safety. To this end, we develop a framework that learns a density-based reward from positive and negative demonstrations and augments it with rule-based objectives for obstacle avoidance and goal reaching. A sampling-based lookahead controller produces supervisory actions that are both safe and adaptive, which are subsequently distilled into a compact student policy suitable for real-time operation with uncertainty estimates. Experiments in synthetic and elevator co-boarding simulations show consistent gains in success rate and time efficiency over baselines, and real-world demonstrations with human participants confirm the practicality of deployment. A video illustrating this work can be found on our project page https://chanwookim971024.github.io/PioneeR/.

## 参考
- http://arxiv.org/abs/2510.12215v1

