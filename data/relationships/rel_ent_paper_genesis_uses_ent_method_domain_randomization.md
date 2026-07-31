---
$id: rel_ent_paper_genesis_uses_ent_method_domain_randomization
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_genesis
  name:
    en: Genesis
    zh: 生态辨析：GENE-26.5（Genesis AI）与 Genesis 物理仿真（Genesis-Embodied-AI）
target:
  id: ent_method_domain_randomization
  name:
    en: Domain Randomization
    zh: 域随机化
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Genesis uses Domain Randomization.
  zh: 生态辨析：GENE-26.5（Genesis AI）与 Genesis 物理仿真（Genesis-Embodied-AI）使用域随机化。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 生成环境可能使用域随机化增强泛化。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_genesis
  url: https://kg.rounds-tech.com/entry/ent_paper_genesis/
  accessed_at: '2026-07-31'
---
