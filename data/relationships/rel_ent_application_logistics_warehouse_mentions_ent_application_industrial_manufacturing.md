---
$id: rel_ent_application_logistics_warehouse_mentions_ent_application_industrial_manufacturing
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_application_logistics_warehouse
  name:
    en: Logistics and Warehouse Automation
    zh: 物流仓储
target:
  id: ent_application_industrial_manufacturing
  name:
    en: Industrial Manufacturing
    zh: 工业制造
domains:
  source_domain: 11_applications_markets
  target_domain: 11_applications_markets
description:
  en: Logistics and Warehouse Automation mentions Industrial Manufacturing.
  zh: 物流仓储提及工业制造。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 物流仓储应用场景常与工业制造场景相关联'
sources:
- id: src_001
  type: other
  title: KG body of ent_application_logistics_warehouse
  url: https://kg.rounds-tech.com/entry/ent_application_logistics_warehouse/
  accessed_at: '2026-07-16'
---
