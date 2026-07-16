---
$id: rel_ent_process_p16_1_1_uses_ent_paper_design_for_manufacturing_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_process_p16_1_1
  name:
    en: DFM/DFA review
    zh: DFM/DFA 评审
target:
  id: ent_paper_design_for_manufacturing_2024
  name:
    en: Design for Manufacturing
    zh: 面向制造的设计
domains:
  source_domain: 05_mass_production
  target_domain: 03_manufacturing_processes
description:
  en: DFM/DFA review uses Design for Manufacturing.
  zh: DFM/DFA 评审使用面向制造的设计。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明DFM/DFA review使用Design for Manufacturing作为方法/工具。
    | 证据: **Method/Tool**: Design for Manufacturing/Assembly Analysis, Assembly Time Estimation'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p16_1_1
  url: https://kg.rounds-tech.com/entry/ent_process_p16_1_1/
  accessed_at: '2026-07-16'
---
