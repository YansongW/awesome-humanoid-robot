---
$id: rel_ent_process_p16_1_1_mentions_ent_method_design_for_manufacturing
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_process_p16_1_1
  name:
    en: DFM/DFA review
    zh: DFM/DFA 评审
target:
  id: ent_method_design_for_manufacturing
  name:
    en: Design for Manufacturing (DFM)
    zh: 可制造性设计（DFM）
domains:
  source_domain: 05_mass_production
  target_domain: 03_manufacturing_processes
description:
  en: DFM/DFA review mentions Design for Manufacturing (DFM).
  zh: DFM/DFA 评审提及可制造性设计（DFM）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: DFM/DFA reports, engineering change lists, cost
    impact assessments'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p16_1_1
  url: https://kg.rounds-tech.com/entry/ent_process_p16_1_1/
  accessed_at: '2026-07-16'
---
