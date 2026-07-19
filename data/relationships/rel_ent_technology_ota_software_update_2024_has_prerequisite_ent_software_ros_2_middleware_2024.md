---
$id: rel_ent_technology_ota_software_update_2024_has_prerequisite_ent_software_ros_2_middleware_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_technology_ota_software_update_2024
  name:
    en: OTA Software Update
    zh: OTA 软件更新
target:
  id: ent_software_ros_2_middleware_2024
  name:
    en: ROS 2 Middleware
    zh: ROS 2 中间件
domains:
  source_domain: 08_software_middleware
  target_domain: 08_software_middleware
description:
  en: OTA Software Update has prerequisite ROS 2 Middleware.
  zh: OTA 软件更新前置依赖ROS 2 中间件。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: OTA更新需要可靠的通信中间件来传输更新包'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
