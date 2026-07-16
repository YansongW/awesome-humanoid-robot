---
$id: rel_ent_human_level_actuation_score_evaluates_on_ent_human_equivalence_envelope
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_human_level_actuation_score
  name:
    en: Human-Level Actuation Score
    zh: 类人驱动评分
target:
  id: ent_human_equivalence_envelope
  name:
    en: Human-Equivalence Envelope
    zh: 人等效包络
domains:
  source_domain: 10_evaluation_benchmarks
  target_domain: 10_evaluation_benchmarks
description:
  en: Human-Level Actuation Score is evaluated on Human-Equivalence Envelope.
  zh: 类人驱动评分评测于人等效包络。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 人类级驱动能力评分基准评估了人类等效包络技术。 | 证据: - **Human-Equivalence
    Envelope coverage**: Ability to meet human torque and power simultaneously at task-relevant postures and rates.'
sources:
- id: src_001
  type: other
  title: KG body of ent_human_level_actuation_score
  url: https://kg.rounds-tech.com/entry/ent_human_level_actuation_score/
  accessed_at: '2026-07-16'
---
