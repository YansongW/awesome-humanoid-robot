---
$id: rel_ent_robot_system_poppy_humanoid_has_prerequisite_ent_method_inverse_kinematics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_robot_system_poppy_humanoid
  name:
    en: Poppy Humanoid
    zh: Poppy 人形机器人
target:
  id: ent_method_inverse_kinematics
  name:
    en: Inverse Kinematics
    zh: 逆运动学
domains:
  source_domain: 02_components
  target_domain: 06_design_engineering
description:
  en: Poppy Humanoid has prerequisite Inverse Kinematics.
  zh: Poppy 人形机器人前置依赖逆运动学。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: Poppy的运动规划和姿态控制需要逆向运动学。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
