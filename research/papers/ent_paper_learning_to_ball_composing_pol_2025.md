---
$id: ent_paper_learning_to_ball_composing_pol_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Learning to Ball: Composing Policies for Long-Horizon Basketball Moves'
  zh: 'Learning to Ball: Composing Policies for Long-Horizon Basketball Moves'
  ko: 'Learning to Ball: Composing Policies for Long-Horizon Basketball Moves'
summary:
  en: 'Learning to Ball: Composing Policies for Long-Horizon Basketball Moves is a 2025 work on physics-based character animation
    for humanoid robots.'
  zh: 'Learning to Ball: Composing Policies for Long-Horizon Basketball Moves is a 2025 work on physics-based character animation
    for humanoid robots.'
  ko: 'Learning to Ball: Composing Policies for Long-Horizon Basketball Moves is a 2025 work on physics-based character animation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- learning_to_ball
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.22442v1.
sources:
- id: src_001
  type: paper
  title: 'Learning to Ball: Composing Policies for Long-Horizon Basketball Moves (arXiv)'
  url: https://arxiv.org/abs/2509.22442
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Learning a control policy for a multi-phase, long-horizon task, such as basketball maneuvers, remains challenging for reinforcement learning approaches due to the need for seamless policy composition and transitions between skills. A long-horizon task typically consists of distinct subtasks with well-defined goals, separated by transitional subtasks with unclear goals but critical to the success of the entire task. Existing methods like the mixture of experts and skill chaining struggle with tasks where individual policies do not share significant commonly explored states or lack well-defined initial and terminal states between different phases. In this paper, we introduce a novel policy integration framework to enable the composition of drastically different motor skills in multi-phase long-horizon tasks with ill-defined intermediate states. Based on that, we further introduce a high-level soft router to enable seamless and robust transitions between the subtasks. We evaluate our framework on a set of fundamental basketball skills and challenging transitions. Policies trained by our approach can effectively control the simulated character to interact with the ball and accomplish the long-horizon task specified by real-time user commands, without relying on ball trajectory references.

## 核心内容
Learning a control policy for a multi-phase, long-horizon task, such as basketball maneuvers, remains challenging for reinforcement learning approaches due to the need for seamless policy composition and transitions between skills. A long-horizon task typically consists of distinct subtasks with well-defined goals, separated by transitional subtasks with unclear goals but critical to the success of the entire task. Existing methods like the mixture of experts and skill chaining struggle with tasks where individual policies do not share significant commonly explored states or lack well-defined initial and terminal states between different phases. In this paper, we introduce a novel policy integration framework to enable the composition of drastically different motor skills in multi-phase long-horizon tasks with ill-defined intermediate states. Based on that, we further introduce a high-level soft router to enable seamless and robust transitions between the subtasks. We evaluate our framework on a set of fundamental basketball skills and challenging transitions. Policies trained by our approach can effectively control the simulated character to interact with the ball and accomplish the long-horizon task specified by real-time user commands, without relying on ball trajectory references.

## 参考
- http://arxiv.org/abs/2509.22442v1

