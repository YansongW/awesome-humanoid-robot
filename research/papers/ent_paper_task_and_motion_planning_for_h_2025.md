---
$id: ent_paper_task_and_motion_planning_for_h_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Task and Motion Planning for Humanoid Loco-manipulation
  zh: Task and Motion Planning for Humanoid Loco-manipulation
  ko: Task and Motion Planning for Humanoid Loco-manipulation
summary:
  en: Task and Motion Planning for Humanoid Loco-manipulation is a 2025 work on loco-manipulation and whole-body-control for
    humanoid robots.
  zh: Task and Motion Planning for Humanoid Loco-manipulation is a 2025 work on loco-manipulation and whole-body-control for
    humanoid robots.
  ko: Task and Motion Planning for Humanoid Loco-manipulation is a 2025 work on loco-manipulation and whole-body-control for
    humanoid robots.
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
- task_and_motion_planning_for_h
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.14099v1.
sources:
- id: src_001
  type: paper
  title: Task and Motion Planning for Humanoid Loco-manipulation (arXiv)
  url: https://arxiv.org/abs/2508.14099
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This work presents an optimization-based task and motion planning (TAMP) framework that unifies planning for locomotion and manipulation through a shared representation of contact modes. We define symbolic actions as contact mode changes, grounding high-level planning in low-level motion. This enables a unified search that spans task, contact, and motion planning while incorporating whole-body dynamics, as well as all constraints between the robot, the manipulated object, and the environment. Results on a humanoid platform show that our method can generate a broad range of physically consistent loco-manipulation behaviors over long action sequences requiring complex reasoning. To the best of our knowledge, this is the first work that enables the resolution of an integrated TAMP formulation with fully acyclic planning and whole body dynamics with actuation constraints for the humanoid loco-manipulation problem.

## 核心内容
This work presents an optimization-based task and motion planning (TAMP) framework that unifies planning for locomotion and manipulation through a shared representation of contact modes. We define symbolic actions as contact mode changes, grounding high-level planning in low-level motion. This enables a unified search that spans task, contact, and motion planning while incorporating whole-body dynamics, as well as all constraints between the robot, the manipulated object, and the environment. Results on a humanoid platform show that our method can generate a broad range of physically consistent loco-manipulation behaviors over long action sequences requiring complex reasoning. To the best of our knowledge, this is the first work that enables the resolution of an integrated TAMP formulation with fully acyclic planning and whole body dynamics with actuation constraints for the humanoid loco-manipulation problem.

## 参考
- http://arxiv.org/abs/2508.14099v1

