---
$id: rel_ent_method_design_for_manufacturing_mentions_ent_method_value_analysis_value_engineering
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_method_design_for_manufacturing
  name:
    en: Design for Manufacturing (DFM)
    zh: 可制造性设计（DFM）
target:
  id: ent_method_value_analysis_value_engineering
  name:
    en: Value Analysis / Value Engineering (VA/VE)
    zh: 价值分析/价值工程（VA/VE）
domains:
  source_domain: 03_manufacturing_processes
  target_domain: 05_mass_production
description:
  en: Design for Manufacturing (DFM) mentions Value Analysis / Value Engineering (VA/VE).
  zh: 可制造性设计（DFM）提及价值分析/价值工程（VA/VE）。
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
