---
$id: rel_ent_paper_whole_body_control_tsid_hqp_extends_ent_method_hierarchical_qp_wbc
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: extends
source:
  id: ent_paper_whole_body_control_tsid_hqp
  name:
    en: Whole-Body Control / TSID / HQP
    zh: Whole-Body Control / TSID / HQP
target:
  id: ent_method_hierarchical_qp_wbc
  name:
    en: Hierarchical QP Whole-Body Control
    zh: 分层二次规划全身控制
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Whole-Body Control / TSID / HQP extends Hierarchical QP Whole-Body Control.
  zh: Whole-Body Control / TSID / HQPextends分层二次规划全身控制。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: HQP是分层QP全身控制的一种形式。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_whole_body_control_tsid_hqp
  url: https://kg.rounds-tech.com/entry/ent_paper_whole_body_control_tsid_hqp/
  accessed_at: '2026-07-31'
---
