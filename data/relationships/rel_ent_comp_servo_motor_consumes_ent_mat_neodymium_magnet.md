---
$id: rel_ent_comp_servo_motor_consumes_ent_mat_neodymium_magnet
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: consumes
source:
  id: ent_comp_servo_motor
  name:
    en: High-Performance Servo Motor
    zh: 高性能伺服电机
target:
  id: ent_mat_neodymium_magnet
  name:
    en: Neodymium-Iron-Boron Magnet
    zh: 钕铁硼磁体
domains:
  source_domain: 02_components
  target_domain: 01_raw_materials
description:
  en: High-Performance Servo Motor consumes Neodymium-Iron-Boron Magnet.
  zh: 高性能伺服电机consumes钕铁硼磁体。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: 高性能伺服电机消耗钕铁硼永磁体。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_comp_servo_motor
  url: https://kg.rounds-tech.com/entry/ent_comp_servo_motor/
  accessed_at: '2026-07-16'
---
