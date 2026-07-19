---
$id: rel_ent_robot_system_openloong_has_prerequisite_ent_paper_zero_moment_point_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_robot_system_openloong
  name:
    en: OpenLoong (Qinglong) Open-Source Humanoid Robot
    zh: OpenLoong / 青龙开源人形机器人
target:
  id: ent_paper_zero_moment_point_2024
  name:
    en: Zero Moment Point
    zh: 零力矩点
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: OpenLoong (Qinglong) Open-Source Humanoid Robot has prerequisite Zero Moment Point.
  zh: OpenLoong / 青龙开源人形机器人前置依赖零力矩点。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 全尺寸人形机器人的双足行走需要ZMP稳定性控制。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
