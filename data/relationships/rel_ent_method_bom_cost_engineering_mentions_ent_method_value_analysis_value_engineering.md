---
$id: rel_ent_method_bom_cost_engineering_mentions_ent_method_value_analysis_value_engineering
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_method_bom_cost_engineering
  name:
    en: BOM Cost Engineering
    zh: BOM成本工程
target:
  id: ent_method_value_analysis_value_engineering
  name:
    en: Value Analysis / Value Engineering (VA/VE)
    zh: 价值分析/价值工程（VA/VE）
domains:
  source_domain: 05_mass_production
  target_domain: 05_mass_production
description:
  en: BOM Cost Engineering mentions Value Analysis / Value Engineering (VA/VE).
  zh: BOM成本工程提及价值分析/价值工程（VA/VE）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p4_wiki_ch30. Evidence: 在 Wiki 第 30 章同一小节共现'
sources:
- id: src_001
  type: other
  title: Wiki 第 30 章
  url: https://kg.rounds-tech.com/wiki/chapters/chapter-30/
  accessed_at: '2026-07-16'
---
