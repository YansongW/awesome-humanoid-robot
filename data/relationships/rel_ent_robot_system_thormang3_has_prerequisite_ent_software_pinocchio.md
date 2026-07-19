---
$id: rel_ent_robot_system_thormang3_has_prerequisite_ent_software_pinocchio
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_robot_system_thormang3
  name:
    en: THORMANG3
    zh: THORMANG3 全尺寸人形机器人
target:
  id: ent_software_pinocchio
  name:
    en: Pinocchio
    zh: Pinocchio
domains:
  source_domain: 02_components
  target_domain: 08_software_middleware
description:
  en: THORMANG3 has prerequisite Pinocchio.
  zh: THORMANG3 全尺寸人形机器人前置依赖Pinocchio。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: Pinocchio库用于刚体动力学和运动学计算，是控制全尺寸人形机器人所必需的基础工具。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
