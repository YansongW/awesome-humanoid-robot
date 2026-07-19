---
$id: rel_ent_software_qnx_has_prerequisite_ent_software_ros_2_middleware_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_software_qnx
  name:
    en: QNX
    zh: QNX
target:
  id: ent_software_ros_2_middleware_2024
  name:
    en: ROS 2 Middleware
    zh: ROS 2 中间件
domains:
  source_domain: 08_software_middleware
  target_domain: 08_software_middleware
description:
  en: QNX has prerequisite ROS 2 Middleware.
  zh: QNX前置依赖ROS 2 中间件。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: ROS 2提供了分布式通信和实时支持的基础概念，是理解QNX实时操作系统在机器人中应用的前提。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
