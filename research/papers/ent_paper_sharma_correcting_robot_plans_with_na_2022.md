---
$id: ent_paper_sharma_correcting_robot_plans_with_na_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Correcting Robot Plans with Natural Language Feedback
  zh: Language costs
  ko: Correcting Robot Plans with Natural Language Feedback
summary:
  en: Correcting Robot Plans with Natural Language Feedback (Language costs), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by NVIDIA, MIT, University of Utah, University of Washington, and published
    at Robotics - Science and Systems 2022.
  zh: Correcting Robot Plans with Natural Language Feedback (Language costs), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by NVIDIA, MIT, University of Utah, University of Washington, and published
    at Robotics - Science and Systems 2022.
  ko: Correcting Robot Plans with Natural Language Feedback (Language costs), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by NVIDIA, MIT, University of Utah, University of Washington, and published
    at Robotics - Science and Systems 2022.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- language_costs
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2204.05186v1.
sources:
- id: src_001
  type: website
  title: Language costs source
  url: https://doi.org/10.15607/RSS.2022.XVIII.065
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
When humans design cost or goal specifications for robots, they often produce specifications that are ambiguous, underspecified, or beyond planners' ability to solve. In these cases, corrections provide a valuable tool for human-in-the-loop robot control. Corrections might take the form of new goal specifications, new constraints (e.g. to avoid specific objects), or hints for planning algorithms (e.g. to visit specific waypoints). Existing correction methods (e.g. using a joystick or direct manipulation of an end effector) require full teleoperation or real-time interaction. In this paper, we explore natural language as an expressive and flexible tool for robot correction. We describe how to map from natural language sentences to transformations of cost functions. We show that these transformations enable users to correct goals, update robot motions to accommodate additional user preferences, and recover from planning errors. These corrections can be leveraged to get 81% and 93% success rates on tasks where the original planner failed, with either one or two language corrections. Our method makes it possible to compose multiple constraints and generalizes to unseen scenes, objects, and sentences in simulated environments and real-world environments.

## 核心内容
When humans design cost or goal specifications for robots, they often produce specifications that are ambiguous, underspecified, or beyond planners' ability to solve. In these cases, corrections provide a valuable tool for human-in-the-loop robot control. Corrections might take the form of new goal specifications, new constraints (e.g. to avoid specific objects), or hints for planning algorithms (e.g. to visit specific waypoints). Existing correction methods (e.g. using a joystick or direct manipulation of an end effector) require full teleoperation or real-time interaction. In this paper, we explore natural language as an expressive and flexible tool for robot correction. We describe how to map from natural language sentences to transformations of cost functions. We show that these transformations enable users to correct goals, update robot motions to accommodate additional user preferences, and recover from planning errors. These corrections can be leveraged to get 81% and 93% success rates on tasks where the original planner failed, with either one or two language corrections. Our method makes it possible to compose multiple constraints and generalizes to unseen scenes, objects, and sentences in simulated environments and real-world environments.

## 参考
- http://arxiv.org/abs/2204.05186v1

