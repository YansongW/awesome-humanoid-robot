---
$id: rel_ent_kkt_conditions_uses_ent_lagrangian
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_kkt_conditions
  name:
    en: Karush-Kuhn-Tucker (KKT) Conditions
    zh: Karush-Kuhn-Tucker（KKT）条件
target:
  id: ent_lagrangian
  name:
    en: Lagrangian
    zh: 拉格朗日量
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Karush-Kuhn-Tucker (KKT) Conditions uses Lagrangian.
  zh: Karush-Kuhn-Tucker（KKT）条件使用拉格朗日量。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: KKT条件使用拉格朗日函数将约束加入目标函数。 | 证据: | $\mathcal{L}$
    | Lagrangian | 把约束“惩罚”加进目标后的总能量 |'
sources:
- id: src_001
  type: other
  title: KG body of ent_kkt_conditions
  url: https://kg.rounds-tech.com/entry/ent_kkt_conditions/
  accessed_at: '2026-07-16'
---
