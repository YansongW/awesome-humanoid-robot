---
$id: rel_ent_tier1_supplier_sanhua_intelligent_controls_supplies_ent_robot_system_tesla_optimus
$schema: "../../../../../data/schema/v1/relationship_schema.json"
$version: 1

type: supplies

source:
  id: ent_tier1_supplier_sanhua_intelligent_controls
  name:
    en: Sanhua Intelligent Controls
    zh: 三花智控
    ko: 산화 인텔리전트 컨트롤스

target:
  id: ent_robot_system_tesla_optimus
  name:
    en: Tesla Optimus
    zh: 特斯拉 Optimus
    ko: 테슬라 옵티머스

domains:
  source_domain: 02_components
  target_domain: 04_assembly_integration_testing

description:
  en: Sanhua Intelligent Controls is reported to supply linear and rotary actuator assemblies for the Tesla Optimus humanoid robot.
  zh: 据报道，三花智控为特斯拉 Optimus 人形机器人供应线性与旋转执行器总成。
  ko: 보도에 따른다면 산화 인텔리전트 컨트롤스는 테슬라 옵티머스 휴이노이드 로봇용 선형 및 회전 액추에이터 어셈블리를 공급함.

verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: Based on industry supply-chain reports; the specific order value and exclusivity claims are disputed by Sanhua.

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
