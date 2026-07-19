---
$id: rel_ent_robot_system_openloong_has_prerequisite_ent_robot_system_odri_bolt
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_robot_system_openloong
  name:
    en: OpenLoong (Qinglong) Open-Source Humanoid Robot
    zh: OpenLoong / 青龙开源人形机器人
target:
  id: ent_robot_system_odri_bolt
  name:
    en: ODRI Bolt (Open Dynamic Robot Initiative)
    zh: ODRI Bolt 开源双足机器人
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: OpenLoong (Qinglong) Open-Source Humanoid Robot has prerequisite ODRI Bolt (Open Dynamic Robot Initiative).
  zh: OpenLoong / 青龙开源人形机器人前置依赖ODRI Bolt 开源双足机器人。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: OpenLoong参考了ODRI Bolt的开源硬件和软件架构。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
