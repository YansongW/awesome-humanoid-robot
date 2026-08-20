---
$id: rel_ent_process_cnc_machining_mentions_ent_method_design_for_manufacturing
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
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
  en: CNC Precision Machining cites Design for Manufacturing.
  zh: CNC精密机加工引用面向制造的设计。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 相关论文为精密加工提供设计参考 | WP2.3 2026-08-06: type retyped
    cites->mentions after DeepSeek review. Reason: ''提供设计参考''只支撑 mentions. Original file rel_ent_process_cnc_machining_cites_ent_paper_design_for_manufacturing_2024.
    | WP4 2026-08-11: endpoint id rewritten (ent_process_cnc_machining→ent_process_cnc_machining, ent_method_design_for_manufacturing→ent_method_design_for_manufacturing);
    original file rel_ent_process_cnc_machining_mentions_ent_paper_design_for_manufacturing_2024.'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_cnc_machining
  url: https://kg.rounds-tech.com/entry/ent_process_cnc_machining/
  accessed_at: '2026-07-16'
---
