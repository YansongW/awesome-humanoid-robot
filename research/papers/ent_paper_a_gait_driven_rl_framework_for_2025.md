---
$id: ent_paper_a_gait_driven_rl_framework_for_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Gait Driven RL Framework for Humanoid Robots
  zh: A Gait Driven RL Framework for Humanoid Robots
  ko: A Gait Driven RL Framework for Humanoid Robots
summary:
  en: A Gait Driven RL Framework for Humanoid Robots is a 2025 work on locomotion for humanoid robots.
  zh: A Gait Driven RL Framework for Humanoid Robots is a 2025 work on locomotion for humanoid robots.
  ko: A Gait Driven RL Framework for Humanoid Robots is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a_gait_driven_rl_framework_for
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.08416v2.
sources:
- id: src_001
  type: paper
  title: A Gait Driven RL Framework for Humanoid Robots (arXiv)
  url: https://arxiv.org/abs/2506.08416
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This paper presents a real-time gait driven training framework for humanoid robots. First, we introduce a novel gait planner that incorporates dynamics to design the desired joint trajectory. In the gait design process, the 3D robot model is decoupled into two 2D models, which are then approximated as hybrid inverted pendulums (H-LIP) for trajectory planning. The gait planner operates in parallel in real time within the robot's learning environment. Second, based on this gait planner, we design three effective reward functions within a reinforcement learning framework, forming a reward composition to achieve periodic bipedal gait. This reward composition reduces the robot's learning time and enhances locomotion performance. Finally, a gait design example, along with simulation and experimental comparisons, is presented to demonstrate the effectiveness of the proposed method.

## 核心内容
This paper presents a real-time gait driven training framework for humanoid robots. First, we introduce a novel gait planner that incorporates dynamics to design the desired joint trajectory. In the gait design process, the 3D robot model is decoupled into two 2D models, which are then approximated as hybrid inverted pendulums (H-LIP) for trajectory planning. The gait planner operates in parallel in real time within the robot's learning environment. Second, based on this gait planner, we design three effective reward functions within a reinforcement learning framework, forming a reward composition to achieve periodic bipedal gait. This reward composition reduces the robot's learning time and enhances locomotion performance. Finally, a gait design example, along with simulation and experimental comparisons, is presented to demonstrate the effectiveness of the proposed method.

## 参考
- http://arxiv.org/abs/2506.08416v2

