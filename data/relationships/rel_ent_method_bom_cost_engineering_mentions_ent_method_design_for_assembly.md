---
$id: rel_ent_method_bom_cost_engineering_mentions_ent_method_design_for_assembly
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_method_bom_cost_engineering
  name:
    en: BOM Cost Engineering
    zh: BOM成本工程
target:
  id: ent_method_design_for_assembly
  name:
    en: Design for Assembly (DFA)
    zh: 可装配性设计（DFA）
domains:
  source_domain: 05_mass_production
  target_domain: 03_manufacturing_processes
description:
  en: BOM Cost Engineering mentions Design for Assembly (DFA).
  zh: BOM成本工程提及可装配性设计（DFA）。
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
