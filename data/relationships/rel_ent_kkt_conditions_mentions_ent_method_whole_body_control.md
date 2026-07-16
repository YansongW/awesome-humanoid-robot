---
$id: rel_ent_kkt_conditions_mentions_ent_method_whole_body_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_kkt_conditions
  name:
    en: Karush-Kuhn-Tucker (KKT) Conditions
    zh: Karush-Kuhn-Tucker（KKT）条件
target:
  id: ent_method_whole_body_control
  name:
    en: Whole-Body Control (WBC)
    zh: 全身控制（WBC）
domains:
  source_domain: 00_foundations
  target_domain: 07_ai_models_algorithms
description:
  en: Karush-Kuhn-Tucker (KKT) Conditions mentions Whole-Body Control (WBC).
  zh: Karush-Kuhn-Tucker（KKT）条件提及全身控制（WBC）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: - `uses_theorem` → 在 WBC、MPC、经济模型等带约束优化问题中广泛使用'
sources:
- id: src_001
  type: other
  title: KG body of ent_kkt_conditions
  url: https://kg.rounds-tech.com/entry/ent_kkt_conditions/
  accessed_at: '2026-07-16'
---
