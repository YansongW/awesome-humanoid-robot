---
$id: rel_ent_software_rt_preempt_linux_has_prerequisite_ent_software_ros_2_middleware_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_software_rt_preempt_linux
  name:
    en: Linux RT-PREEMPT
    zh: Linux RT-PREEMPT
target:
  id: ent_software_ros_2_middleware_2024
  name:
    en: ROS 2 Middleware
    zh: ROS 2 中间件
domains:
  source_domain: 08_software_middleware
  target_domain: 08_software_middleware
description:
  en: Linux RT-PREEMPT has prerequisite ROS 2 Middleware.
  zh: Linux RT-PREEMPT前置依赖ROS 2 中间件。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 理解ROS 2的实时通信机制有助于掌握RT-PREEMPT在机器人系统中的实际应用场景。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
