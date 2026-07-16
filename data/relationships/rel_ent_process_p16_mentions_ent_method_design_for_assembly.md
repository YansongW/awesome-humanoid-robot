---
$id: rel_ent_process_p16_mentions_ent_method_design_for_assembly
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_process_p16
  name:
    en: Pilot & Production Ramp
    zh: 小批量试产与量产准备（Pilot & Production Ramp）
target:
  id: ent_method_design_for_assembly
  name:
    en: Design for Assembly (DFA)
    zh: 可装配性设计（DFA）
domains:
  source_domain: 05_mass_production
  target_domain: 03_manufacturing_processes
description:
  en: Pilot & Production Ramp mentions Design for Assembly (DFA).
  zh: 小批量试产与量产准备（Pilot & Production Ramp）提及可装配性设计（DFA）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: ##### DFM/DFA 评审'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p16
  url: https://kg.rounds-tech.com/entry/ent_process_p16/
  accessed_at: '2026-07-16'
---
