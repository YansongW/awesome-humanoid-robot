---
$id: rel_ent_oem_tesla_sources_from_ent_tier1_supplier_sanhua_intelligent_controls
$schema: "../../../../../data/schema/v1/relationship_schema.json"
$version: 1

type: sources_from

source:
  id: ent_oem_tesla
  name:
    en: Tesla
    zh: 特斯拉
    ko: 테슬라

target:
  id: ent_tier1_supplier_sanhua_intelligent_controls
  name:
    en: Sanhua Intelligent Controls
    zh: 三花智控
    ko: 산화 인텔리전트 컨트롤스

domains:
  source_domain: 06_design_engineering
  target_domain: 02_components

description:
  en: Tesla is understood to source actuator assemblies for Optimus from Tier-1 supplier Sanhua Intelligent Controls.
  zh: 据信，特斯拉从一级供应商三花智控采购 Optimus 的执行器总成。
  ko: 테슬라는 옵티머스용 액추에이터 어셈블리를 Tier-1 공급업체인 산화 인텔리전트 컨트롤스로부터 조달하는 것으로 파악됨.

verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: Inferred from supply-chain reporting; Tesla has not officially confirmed supplier details for Optimus.

sources:
  - id: src_001_sanhua_36kr
    type: report
    title: Elon Musk Places $685M Order with Sanhua
    url: https://eu.36kr.com/en/p/3510288514980998
    date: '2025-10-15'
    accessed_at: '2026-06-25'
  - id: src_002_sanhua_optimusk
    type: report
    title: Tesla Optimus Supply Chain - Who Makes the Parts?
    url: https://optimusk.blog/blog/tesla-optimus-suppliers/
    date: '2026-06-01'
    accessed_at: '2026-06-25'
---
