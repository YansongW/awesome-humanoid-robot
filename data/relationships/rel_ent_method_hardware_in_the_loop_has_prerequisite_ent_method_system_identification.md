---
$id: rel_ent_method_hardware_in_the_loop_has_prerequisite_ent_method_system_identification
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_method_hardware_in_the_loop
  name:
    en: Hardware-in-the-Loop (HIL)
    zh: 硬件在环测试（HIL）
target:
  id: ent_method_system_identification
  name:
    en: System Identification
    zh: 系统辨识
domains:
  source_domain: 04_assembly_integration_testing
  target_domain: 07_ai_models_algorithms
description:
  en: Hardware-in-the-Loop (HIL) has prerequisite System Identification.
  zh: 硬件在环测试（HIL）前置依赖系统辨识。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: HIL需要准确的系统模型来模拟被控对象，系统辨识提供了建立这些模型的方法。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
