---
$id: rel_ent_paper_dreamtrajectory_trajectory_guided_action_2026_evaluates_on_ent_benchmark_maniskill
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_dreamtrajectory_trajectory_guided_action_2026
  name:
    en: 'DreamTrajectory: Trajectory-Guided Action Generation with World Model Alignment for Mobile Manipulation'
    zh: 'DreamTrajectory: Trajectory-Guided Action Generation with World Model Alignment for Mobile Manipulation'
target:
  id: ent_benchmark_maniskill
  name:
    en: ManiSkill
    zh: ManiSkill
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 10_evaluation_benchmarks
description:
  en: 'DreamTrajectory: Trajectory-Guided Action Generation with World Model Alignment for Mobile Manipulation is evaluated
    on ManiSkill.'
  zh: 'DreamTrajectory: Trajectory-Guided Action Generation with World Model Alignment for Mobile Manipulation评测于ManiSkill。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文在ManiSkill benchmark的set_table套件上进行仿真评估。 |
    证据: 仿真采用 ManiSkill-HAB（MS-HAB）benchmark 的 set_table 套件，使用 Fetch 移动操作机器人，覆盖 6 个子任务（pick apple、pick bowl、open fridge、close
    fridge、open counter、close counter），每个方法每任务评估 100 个 episode，共 600 episodes/方法。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_dreamtrajectory_trajectory_guided_action_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_dreamtrajectory_trajectory_guided_action_2026/
  accessed_at: '2026-08-06'
---
