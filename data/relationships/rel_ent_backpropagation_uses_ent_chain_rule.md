---
$id: rel_ent_backpropagation_uses_ent_chain_rule
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_backpropagation
  name:
    en: Backpropagation
    zh: 反向传播
target:
  id: ent_chain_rule
  name:
    en: Chain rule
    zh: 链式法则
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Backpropagation uses Chain rule.
  zh: 反向传播使用链式法则。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: 反向传播本质上是链式法则在计算图各层上的系统性反向应用。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_backpropagation
  url: https://kg.rounds-tech.com/entry/ent_backpropagation/
  accessed_at: '2026-07-16'
---
