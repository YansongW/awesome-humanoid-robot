---
$id: rel_ent_tech_on_device_vla_inference_has_prerequisite_ent_software_ros_2_middleware_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_tech_on_device_vla_inference
  name:
    en: On-Device VLA Inference
    zh: 端侧 VLA 推理
target:
  id: ent_software_ros_2_middleware_2024
  name:
    en: ROS 2 Middleware
    zh: ROS 2 中间件
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 08_software_middleware
description:
  en: On-Device VLA Inference has prerequisite ROS 2 Middleware.
  zh: 端侧 VLA 推理前置依赖ROS 2 中间件。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: ROS 2提供了机器人软件框架的基础，VLA推理需要在此框架下集成视觉和语言模型。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
