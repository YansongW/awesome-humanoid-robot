---
$id: rel_ent_paper_cubic_barrier_elasticity_inclusive_dynam_uses_ent_method_sim_to_real
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_cubic_barrier_elasticity_inclusive_dynam
  name:
    en: A Cubic Barrier with Elasticity-Inclusive Dynamic Stiffness
    zh: A Cubic Barrier with Elasticity-Inclusive Dynamic Stiffness
target:
  id: ent_method_sim_to_real
  name:
    en: Sim-to-Real Transfer
    zh: Sim-to-Real迁移
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: A Cubic Barrier with Elasticity-Inclusive Dynamic Stiffness uses Sim-to-Real Transfer.
  zh: A Cubic Barrier with Elasticity-Inclusive Dynamic Stiffness使用Sim-to-Real迁移。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 该接触求解器可用于物理仿真，是sim-to-real流程的一部分。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_cubic_barrier_elasticity_inclusive_dynam
  url: https://kg.rounds-tech.com/entry/ent_paper_cubic_barrier_elasticity_inclusive_dynam/
  accessed_at: '2026-07-31'
---
