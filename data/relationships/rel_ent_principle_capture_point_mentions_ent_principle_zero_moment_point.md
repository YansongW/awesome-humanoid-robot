---
$id: rel_ent_principle_capture_point_mentions_ent_principle_zero_moment_point
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_principle_capture_point
  name:
    en: Capture Point
    zh: 捕获点
target:
  id: ent_principle_zero_moment_point
  name:
    en: Zero Moment Point (ZMP)
    zh: 零力矩点（ZMP）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 06_design_engineering
description:
  en: Capture Point mentions Zero Moment Point (ZMP).
  zh: 捕获点提及零力矩点（ZMP）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: 在**线性倒立摆模型（Linear Inverted Pendulum Model, LIPM）**中，假设质心高度
    $z_c$ 恒定，且质点通过无质量杆连接到地面上的 ZMP。'
sources:
- id: src_001
  type: other
  title: KG body of ent_principle_capture_point
  url: https://kg.rounds-tech.com/entry/ent_principle_capture_point/
  accessed_at: '2026-07-16'
---
