---
$id: rel_ent_robot_system_upkie_compares_with_ent_robot_system_berkeley_humanoid_lite
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: compares_with
source:
  id: ent_robot_system_upkie
  name:
    en: Upkie Wheeled Biped Robot
    zh: Upkie 轮足双足机器人
target:
  id: ent_robot_system_berkeley_humanoid_lite
  name:
    en: Berkeley Humanoid Lite
    zh: 伯克利轻量人形机器人
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Upkie Wheeled Biped Robot compares with Berkeley Humanoid Lite.
  zh: Upkie 轮足双足机器人compares_with伯克利轻量人形机器人。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据将Upkie作为进阶纯双足（如Berkeley Humanoid Lite）前的练兵平台，隐含比较关系。
    | 证据: - 适合：想在真实硬件上学平衡控制/RL 部署的个人开发者与课程项目；可作为进阶纯双足（如 Berkeley Humanoid Lite）前的练兵平台。'
sources:
- id: src_001
  type: other
  title: KG body of ent_robot_system_upkie
  url: https://kg.rounds-tech.com/entry/ent_robot_system_upkie/
  accessed_at: '2026-07-31'
---
