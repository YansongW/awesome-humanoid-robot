---
$id: rel_ent_paper_yin_unitracker_learning_universal_2025_evaluates_on_ent_robot_system_unitree_g1
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_yin_unitracker_learning_universal_2025
  name:
    en: 'UniTracker: Learning Universal Whole-Body Motion Tracker for Humanoid Robots'
    zh: UniTracker：面向人形机器人的通用全身运动追踪器
target:
  id: ent_robot_system_unitree_g1
  name:
    en: Unitree G1 Humanoid Robot
    zh: Unitree G1 人形机器人
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 02_components
description:
  en: 'UniTracker: Learning Universal Whole-Body Motion Tracker for Humanoid Robots is evaluated on Unitree G1 Humanoid Robot.'
  zh: UniTracker：面向人形机器人的通用全身运动追踪器评测于Unitree G1 人形机器人。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明UniTracker在Unitree G1人形机器人的仿真与真实环境中进行评估，因此源在目标上评估。
    | 证据: 在 Unitree G1 人形机器人的仿真与真实环境评估中，UniTracker 在运动多样性、跟踪精度和部署鲁棒性上表现优异。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_yin_unitracker_learning_universal_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_yin_unitracker_learning_universal_2025/
  accessed_at: '2026-07-31'
---
