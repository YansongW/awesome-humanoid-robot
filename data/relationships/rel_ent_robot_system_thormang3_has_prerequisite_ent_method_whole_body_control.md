---
$id: rel_ent_robot_system_thormang3_has_prerequisite_ent_method_whole_body_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_robot_system_thormang3
  name:
    en: THORMANG3
    zh: THORMANG3 全尺寸人形机器人
target:
  id: ent_method_whole_body_control
  name:
    en: Whole-Body Control (WBC)
    zh: 全身控制（WBC）
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: THORMANG3 has prerequisite Whole-Body Control (WBC).
  zh: THORMANG3 全尺寸人形机器人前置依赖全身控制（WBC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 全身控制（WBC）是协调THORMANG3多自由度运动的核心方法。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
