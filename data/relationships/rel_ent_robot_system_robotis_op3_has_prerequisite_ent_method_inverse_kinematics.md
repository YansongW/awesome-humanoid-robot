---
$id: rel_ent_robot_system_robotis_op3_has_prerequisite_ent_method_inverse_kinematics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_robot_system_robotis_op3
  name:
    en: ROBOTIS OP3 (DARwIn-OP Series)
    zh: ROBOTIS OP3 人形机器人（DARwIn-OP 系列）
target:
  id: ent_method_inverse_kinematics
  name:
    en: Inverse Kinematics
    zh: 逆运动学
domains:
  source_domain: 02_components
  target_domain: 06_design_engineering
description:
  en: ROBOTIS OP3 (DARwIn-OP Series) has prerequisite Inverse Kinematics.
  zh: ROBOTIS OP3 人形机器人（DARwIn-OP 系列）前置依赖逆运动学。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: OP3的步态规划和操作需要逆向运动学求解。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
