---
$id: rel_ent_kkt_conditions_requires_ent_constraint_qualification
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: requires
source:
  id: ent_kkt_conditions
  name:
    en: Karush-Kuhn-Tucker (KKT) Conditions
    zh: Karush-Kuhn-Tucker（KKT）条件
target:
  id: ent_constraint_qualification
  name:
    en: Constraint qualification
    zh: 约束规范
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Karush-Kuhn-Tucker (KKT) Conditions requires Constraint qualification.
  zh: Karush-Kuhn-Tucker（KKT）条件requires约束规范。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: KKT条件需要约束规范（如LICQ）才能成立。 | 证据: - `requires` →
    Constraint qualification（约束规范，如 LICQ、Slater''s condition）'
sources:
- id: src_001
  type: other
  title: KG body of ent_kkt_conditions
  url: https://kg.rounds-tech.com/entry/ent_kkt_conditions/
  accessed_at: '2026-07-16'
---
