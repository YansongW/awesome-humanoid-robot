---
$id: rel_ent_process_p13_1_2_mentions_ent_method_design_for_manufacturing
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_process_p13_1_2
  name:
    en: In-house/Third-party PCB Design
    zh: 自研/外购 PCB 设计
target:
  id: ent_method_design_for_manufacturing
  name:
    en: Design for Manufacturing (DFM)
    zh: 可制造性设计（DFM）
domains:
  source_domain: 02_components
  target_domain: 03_manufacturing_processes
description:
  en: In-house/Third-party PCB Design mentions Design for Manufacturing (DFM).
  zh: 自研/外购 PCB 设计提及可制造性设计（DFM）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: Schematic diagram, PCB layout, bill of materials,
    DFM report'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p13_1_2
  url: https://kg.rounds-tech.com/entry/ent_process_p13_1_2/
  accessed_at: '2026-07-16'
---
