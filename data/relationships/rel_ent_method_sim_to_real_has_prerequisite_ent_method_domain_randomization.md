---
$id: rel_ent_method_sim_to_real_has_prerequisite_ent_method_domain_randomization
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_method_sim_to_real
  name:
    en: Sim-to-Real Transfer
    zh: Sim-to-Real迁移
target:
  id: ent_method_domain_randomization
  name:
    en: Domain Randomization
    zh: 域随机化
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Sim-to-Real Transfer has prerequisite Domain Randomization.
  zh: Sim-to-Real迁移前置依赖域随机化。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 域随机化是Sim-to-Transfer的核心技术，通过在仿真中变化参数使策略泛化到真实环境。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
