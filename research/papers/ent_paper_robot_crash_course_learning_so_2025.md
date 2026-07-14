---
$id: ent_paper_robot_crash_course_learning_so_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Robot Crash Course: Learning Soft and Stylized Falling'
  zh: 'Robot Crash Course: Learning Soft and Stylized Falling'
  ko: 'Robot Crash Course: Learning Soft and Stylized Falling'
summary:
  en: 'Robot Crash Course: Learning Soft and Stylized Falling is a 2025 work on loco-manipulation and whole-body-control for
    humanoid robots.'
  zh: 'Robot Crash Course: Learning Soft and Stylized Falling is a 2025 work on loco-manipulation and whole-body-control for
    humanoid robots.'
  ko: 'Robot Crash Course: Learning Soft and Stylized Falling is a 2025 work on loco-manipulation and whole-body-control for
    humanoid robots.'
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
- loco_manipulation
- robot_crash_course
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.10635v1.
sources:
- id: src_001
  type: paper
  title: 'Robot Crash Course: Learning Soft and Stylized Falling (arXiv)'
  url: https://arxiv.org/abs/2511.10635
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Despite recent advances in robust locomotion, bipedal robots operating in the real world remain at risk of falling. While most research focuses on preventing such events, we instead concentrate on the phenomenon of falling itself. Specifically, we aim to reduce physical damage to the robot while providing users with control over a robot's end pose. To this end, we propose a robot agnostic reward function that balances the achievement of a desired end pose with impact minimization and the protection of critical robot parts during reinforcement learning. To make the policy robust to a broad range of initial falling conditions and to enable the specification of an arbitrary and unseen end pose at inference time, we introduce a simulation-based sampling strategy of initial and end poses. Through simulated and real-world experiments, our work demonstrates that even bipedal robots can perform controlled, soft falls.

## 核心内容
Despite recent advances in robust locomotion, bipedal robots operating in the real world remain at risk of falling. While most research focuses on preventing such events, we instead concentrate on the phenomenon of falling itself. Specifically, we aim to reduce physical damage to the robot while providing users with control over a robot's end pose. To this end, we propose a robot agnostic reward function that balances the achievement of a desired end pose with impact minimization and the protection of critical robot parts during reinforcement learning. To make the policy robust to a broad range of initial falling conditions and to enable the specification of an arbitrary and unseen end pose at inference time, we introduce a simulation-based sampling strategy of initial and end poses. Through simulated and real-world experiments, our work demonstrates that even bipedal robots can perform controlled, soft falls.

## 参考
- http://arxiv.org/abs/2511.10635v1

