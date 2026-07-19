---
$id: rel_ent_method_hardware_in_the_loop_has_prerequisite_ent_method_sim_to_real
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_method_hardware_in_the_loop
  name:
    en: Hardware-in-the-Loop (HIL)
    zh: 硬件在环测试（HIL）
target:
  id: ent_method_sim_to_real
  name:
    en: Sim-to-Real Transfer
    zh: Sim-to-Real迁移
domains:
  source_domain: 04_assembly_integration_testing
  target_domain: 07_ai_models_algorithms
description:
  en: Hardware-in-the-Loop (HIL) has prerequisite Sim-to-Real Transfer.
  zh: 硬件在环测试（HIL）前置依赖Sim-to-Real迁移。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: HIL是连接仿真与真实硬件的桥梁，理解Sim-to-Real的挑战有助于设计有效的HIL测试。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
