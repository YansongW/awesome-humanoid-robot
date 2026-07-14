---
$id: ent_paper_state_nav_stability_aware_trav_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain'
  zh: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain'
  ko: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain'
summary:
  en: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain is a 2025 work on navigation
    for humanoid robots, with open-source code available.'
  zh: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain is a 2025 work on navigation
    for humanoid robots, with open-source code available.'
  ko: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain is a 2025 work on navigation
    for humanoid robots, with open-source code available.'
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
- navigation
- state_nav
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.01046v4.
sources:
- id: src_001
  type: paper
  title: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain (arXiv)'
  url: https://arxiv.org/abs/2506.01046
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Bipedal robots have advantages in maneuvering human-centered environments, but face greater failure risk compared to other stable mobile platforms such as wheeled or quadrupedal robots. While learning-based traversability has been widely studied for these platforms, bipedal traversability has instead relied on manually designed rules with limited consideration of locomotion stability on rough terrain. In this work, we present the first learning-based traversability estimation and risk-sensitive navigation framework for bipedal robots operating in diverse, uneven environments. TravFormer, a transformer-based neural network, is trained to predict bipedal instability with uncertainty, enabling risk-aware and adaptive planning. Based on the network, we define traversability as stability-aware command velocity-the fastest command velocity that keeps instability below a user-defined limit. This velocity-based traversability is integrated into a hierarchical planner that combines traversability-informed Rapid Random Tree Star (TravRRT*) for time-efficient planning and Model Predictive Control (MPC) for safe execution. We validate our method in MuJoCo simulation and the real world, demonstrating improved navigation performance, with enhanced robustness and time efficiency across varying terrains compared to existing methods.

## 核心内容
Bipedal robots have advantages in maneuvering human-centered environments, but face greater failure risk compared to other stable mobile platforms such as wheeled or quadrupedal robots. While learning-based traversability has been widely studied for these platforms, bipedal traversability has instead relied on manually designed rules with limited consideration of locomotion stability on rough terrain. In this work, we present the first learning-based traversability estimation and risk-sensitive navigation framework for bipedal robots operating in diverse, uneven environments. TravFormer, a transformer-based neural network, is trained to predict bipedal instability with uncertainty, enabling risk-aware and adaptive planning. Based on the network, we define traversability as stability-aware command velocity-the fastest command velocity that keeps instability below a user-defined limit. This velocity-based traversability is integrated into a hierarchical planner that combines traversability-informed Rapid Random Tree Star (TravRRT*) for time-efficient planning and Model Predictive Control (MPC) for safe execution. We validate our method in MuJoCo simulation and the real world, demonstrating improved navigation performance, with enhanced robustness and time efficiency across varying terrains compared to existing methods.

## 参考
- http://arxiv.org/abs/2506.01046v4

