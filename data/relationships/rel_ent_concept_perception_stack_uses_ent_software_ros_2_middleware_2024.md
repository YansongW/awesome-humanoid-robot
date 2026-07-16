---
$id: rel_ent_concept_perception_stack_uses_ent_software_ros_2_middleware_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_concept_perception_stack
  name:
    en: Perception Stack
    zh: 感知栈
target:
  id: ent_software_ros_2_middleware_2024
  name:
    en: ROS 2 Middleware
    zh: ROS 2 中间件
domains:
  source_domain: 08_software_middleware
  target_domain: 08_software_middleware
description:
  en: Perception Stack uses ROS 2 Middleware.
  zh: 感知栈使用ROS 2 中间件。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 感知堆栈依赖ROS 2中间件进行传感器数据通信和集成。'
sources:
- id: src_001
  type: other
  title: KG body of ent_concept_perception_stack
  url: https://kg.rounds-tech.com/entry/ent_concept_perception_stack/
  accessed_at: '2026-07-16'
---
