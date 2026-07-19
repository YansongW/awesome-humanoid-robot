---
$id: rel_ent_component_tactile_sensor_array_2024_has_prerequisite_ent_foundation_probability_theory
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_component_tactile_sensor_array_2024
  name:
    en: Tactile Sensor Array
    zh: 触觉传感器阵列
target:
  id: ent_foundation_probability_theory
  name:
    en: Probability Theory
    zh: 概率论
domains:
  source_domain: 02_components
  target_domain: 00_foundations
description:
  en: Tactile Sensor Array has prerequisite Probability Theory.
  zh: 触觉传感器阵列前置依赖概率论。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 触觉传感器信号处理中的噪声建模和滤波需要概率论。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
