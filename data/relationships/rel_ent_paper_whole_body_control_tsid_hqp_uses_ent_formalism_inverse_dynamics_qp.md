---
$id: rel_ent_paper_whole_body_control_tsid_hqp_uses_ent_formalism_inverse_dynamics_qp
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_whole_body_control_tsid_hqp
  name:
    en: Whole-Body Control / TSID / HQP
    zh: Whole-Body Control / TSID / HQP
target:
  id: ent_formalism_inverse_dynamics_qp
  name:
    en: Inverse-Dynamics QP Formulation
    zh: 逆动力学二次规划形式化
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Whole-Body Control / TSID / HQP uses Inverse-Dynamics QP Formulation.
  zh: Whole-Body Control / TSID / HQP使用逆动力学二次规划形式化。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: TSID和HQP通常使用逆动力学QP公式。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_whole_body_control_tsid_hqp
  url: https://kg.rounds-tech.com/entry/ent_paper_whole_body_control_tsid_hqp/
  accessed_at: '2026-07-31'
---
