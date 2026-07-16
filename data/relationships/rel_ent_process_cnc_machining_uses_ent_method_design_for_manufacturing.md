---
$id: rel_ent_process_cnc_machining_uses_ent_method_design_for_manufacturing
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_process_cnc_machining
  name:
    en: CNC Precision Machining
    zh: CNC精密机加工
target:
  id: ent_method_design_for_manufacturing
  name:
    en: Design for Manufacturing (DFM)
    zh: 可制造性设计（DFM）
domains:
  source_domain: 03_manufacturing_processes
  target_domain: 03_manufacturing_processes
description:
  en: CNC Precision Machining uses Design for Manufacturing (DFM).
  zh: CNC精密机加工使用可制造性设计（DFM）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 精密加工需要应用面向制造的设计方法'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_cnc_machining
  url: https://kg.rounds-tech.com/entry/ent_process_cnc_machining/
  accessed_at: '2026-07-16'
---
