---
$id: rel_ent_gradient_descent_uses_ent_chain_rule
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_gradient_descent
  name:
    en: Gradient Descent
    zh: 梯度下降法
target:
  id: ent_chain_rule
  name:
    en: Chain rule
    zh: 链式法则
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Gradient Descent uses Chain rule.
  zh: 梯度下降法使用链式法则。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 梯度下降使用链式法则通过反向传播计算梯度。 | 证据: - `uses` → Chain
    rule（链式法则，通过 backpropagation 计算梯度）'
sources:
- id: src_001
  type: other
  title: KG body of ent_gradient_descent
  url: https://kg.rounds-tech.com/entry/ent_gradient_descent/
  accessed_at: '2026-07-16'
---
