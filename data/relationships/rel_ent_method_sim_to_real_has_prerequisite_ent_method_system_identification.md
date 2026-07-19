---
$id: rel_ent_method_sim_to_real_has_prerequisite_ent_method_system_identification
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_method_sim_to_real
  name:
    en: Sim-to-Real Transfer
    zh: Sim-to-Real迁移
target:
  id: ent_method_system_identification
  name:
    en: System Identification
    zh: 系统辨识
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Sim-to-Real Transfer has prerequisite System Identification.
  zh: Sim-to-Real迁移前置依赖系统辨识。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 系统辨识帮助缩小仿真与真实之间的差距，是Sim-to-Real成功的关键步骤。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
