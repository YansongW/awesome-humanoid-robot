---
$id: rel_ent_robot_system_robotis_op3_has_prerequisite_ent_method_forward_kinematics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_robot_system_robotis_op3
  name:
    en: ROBOTIS OP3 (DARwIn-OP Series)
    zh: ROBOTIS OP3 人形机器人（DARwIn-OP 系列）
target:
  id: ent_method_forward_kinematics
  name:
    en: Forward Kinematics
    zh: 正运动学
domains:
  source_domain: 02_components
  target_domain: 06_design_engineering
description:
  en: ROBOTIS OP3 (DARwIn-OP Series) has prerequisite Forward Kinematics.
  zh: ROBOTIS OP3 人形机器人（DARwIn-OP 系列）前置依赖正运动学。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: OP3的运动控制需要正向运动学建模。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
