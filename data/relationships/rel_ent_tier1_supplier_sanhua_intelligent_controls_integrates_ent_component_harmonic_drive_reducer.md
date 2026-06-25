---
$id: rel_ent_tier1_supplier_sanhua_intelligent_controls_integrates_ent_component_harmonic_drive_reducer
$schema: "../../../../../data/schema/v1/relationship_schema.json"
$version: 1

type: integrates

source:
  id: ent_tier1_supplier_sanhua_intelligent_controls
  name:
    en: Sanhua Intelligent Controls
    zh: 三花智控
    ko: 산화 인텔리전트 컨트롤스

target:
  id: ent_component_harmonic_drive_reducer
  name:
    en: Harmonic Drive Reducer
    zh: 谐波减速器
    ko: 하모닉 드라이브 감속기

domains:
  source_domain: 02_components
  target_domain: 02_components

description:
  en: Sanhua's actuator assemblies for humanoid robots are understood to integrate harmonic drive reducers sourced from specialized reducer suppliers.
  zh: 三花智控为人形机器人提供的执行器总成据信集成了来自专业减速器供应商的谐波减速器。
  ko: 산화 인텔리전트 컨트롤스의 휴이노이드 로봇용 액추에이터 어셈블리는 전문 감속기 공급업체로부터 조달한 하모닉 드라이브 감속기를 통합하는 것으로 파악됨.

verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: Inferred from supply-chain analyses of Optimus actuator architecture; Sanhua does not publicly detail its sub-supplier relationships.

sources:
  - id: src_002_sanhua_optimusk
    type: report
    title: Tesla Optimus Supply Chain - Who Makes the Parts?
    url: https://optimusk.blog/blog/tesla-optimus-suppliers/
    date: '2026-06-01'
    accessed_at: '2026-06-25'
  - id: src_001_sanhua_36kr
    type: report
    title: Elon Musk Places $685M Order with Sanhua
    url: https://eu.36kr.com/en/p/3510288514980998
    date: '2025-10-15'
    accessed_at: '2026-06-25'
---
