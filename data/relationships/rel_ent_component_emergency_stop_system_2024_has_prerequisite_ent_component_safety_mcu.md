---
$id: rel_ent_component_emergency_stop_system_2024_has_prerequisite_ent_component_safety_mcu
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_component_emergency_stop_system_2024
  name:
    en: Emergency Stop System
    zh: 急停系统
target:
  id: ent_component_safety_mcu
  name:
    en: Safety Microcontroller Unit (Safety MCU)
    zh: 安全MCU
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Emergency Stop System has prerequisite Safety Microcontroller Unit (Safety MCU).
  zh: 急停系统前置依赖安全MCU。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 安全MCU是紧急停止系统的核心控制单元，负责监控和触发安全动作。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
