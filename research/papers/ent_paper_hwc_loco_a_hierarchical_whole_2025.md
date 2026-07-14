---
$id: ent_paper_hwc_loco_a_hierarchical_whole_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion'
  zh: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion'
  ko: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion'
summary:
  en: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion is a 2025 work on locomotion for
    humanoid robots.'
  zh: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion is a 2025 work on locomotion for
    humanoid robots.'
  ko: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion is a 2025 work on locomotion for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- hwc_loco
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.00923v3.
sources:
- id: src_001
  type: paper
  title: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion (arXiv)'
  url: https://arxiv.org/abs/2503.00923
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion project page'
  url: https://simonlinsx.github.io/HWC_Loco/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots, capable of assuming human roles in various workplaces, have become essential to embodied intelligence. However, as robots with complex physical structures, learning a control model that can operate robustly across diverse environments remains inherently challenging, particularly under the discrepancies between training and deployment environments. In this study, we propose HWC-Loco, a robust whole-body control algorithm tailored for humanoid locomotion tasks. By reformulating policy learning as a robust optimization problem, HWC-Loco explicitly learns to recover from safety-critical scenarios. While prioritizing safety guarantees, overly conservative behavior can compromise the robot's ability to complete the given tasks. To tackle this challenge, HWC-Loco leverages a hierarchical policy for robust control. This policy can dynamically resolve the trade-off between goal-tracking and safety recovery, guided by human behavior norms and dynamic constraints. To evaluate the performance of HWC-Loco, we conduct extensive comparisons against state-of-the-art humanoid control models, demonstrating HWC-Loco's superior performance across diverse terrains, robot structures, and locomotion tasks under both simulated and real-world environments.

## 核心内容
Humanoid robots, capable of assuming human roles in various workplaces, have become essential to embodied intelligence. However, as robots with complex physical structures, learning a control model that can operate robustly across diverse environments remains inherently challenging, particularly under the discrepancies between training and deployment environments. In this study, we propose HWC-Loco, a robust whole-body control algorithm tailored for humanoid locomotion tasks. By reformulating policy learning as a robust optimization problem, HWC-Loco explicitly learns to recover from safety-critical scenarios. While prioritizing safety guarantees, overly conservative behavior can compromise the robot's ability to complete the given tasks. To tackle this challenge, HWC-Loco leverages a hierarchical policy for robust control. This policy can dynamically resolve the trade-off between goal-tracking and safety recovery, guided by human behavior norms and dynamic constraints. To evaluate the performance of HWC-Loco, we conduct extensive comparisons against state-of-the-art humanoid control models, demonstrating HWC-Loco's superior performance across diverse terrains, robot structures, and locomotion tasks under both simulated and real-world environments.

## 参考
- http://arxiv.org/abs/2503.00923v3

