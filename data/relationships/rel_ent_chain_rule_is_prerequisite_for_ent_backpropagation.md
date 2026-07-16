---
$id: rel_ent_chain_rule_is_prerequisite_for_ent_backpropagation
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_prerequisite_for
source:
  id: ent_chain_rule
  name:
    en: Chain rule
    zh: 链式法则
target:
  id: ent_backpropagation
  name:
    en: Backpropagation
    zh: 反向传播
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Chain rule is prerequisite for Backpropagation.
  zh: 链式法则is_prerequisite_for反向传播。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: 反向传播反复应用链式法则，计算损失对所有网络参数的梯度。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_chain_rule
  url: https://kg.rounds-tech.com/entry/ent_chain_rule/
  accessed_at: '2026-07-16'
---
