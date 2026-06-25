---
$id: "rel_ent_tech_li_battery_humanoid_enables_ent_robot_system_tesla_optimus"
$schema: "../../../../../data/schema/v1/relationship_schema.json"
$version: 1

type: "enables"

source:
  id: "ent_tech_li_battery_humanoid"
  name:
    en: "Lithium-Ion Battery System for Humanoid Robots"
    zh: "人形机器人锂离子电池系统"
    ko: "휴로이드 로봇용 리튬 이온 배터리 시스템"

target:
  id: "ent_robot_system_tesla_optimus"
  name:
    en: "Tesla Optimus"
    zh: "特斯拉 Optimus"
    ko: "테슬라 옵티머스"

domains:
  source_domain: "02_components"
  target_domain: "02_components"

description:
  en: "Tesla Optimus relies on an onboard lithium-ion battery pack for mobility and actuation; the 2.3 kWh pack enables approximately two hours of dynamic runtime."
  zh: "特斯拉 Optimus 依靠机载锂离子电池组实现移动和驱动；2.3 kWh 电池组支持约两小时的动态运行时间。"
  ko: "Tesla Optimus는 이동과 구동을 위해 온보드 리튬 이온 배터리 팩에 의존하며, 2.3 kWh 팩은 약 2시간의 동적 런타임을 가능하게 함."

verification:
  status: "partially_verified"
  reviewed_by: "ai"
  reviewed_at: "2026-06-25"
  confidence: "medium"
  notes: "Capacity and runtime figures are estimates from industry analysis."

sources:
  - id: "src_interact_analysis_li_batteries_2026"
    type: "report"
    title: "Humanoid robots and lithium-ion batteries: Long-term commitment or short-term convenience?"
    url: "https://interactanalysis.com/insight/humanoid-robots-and-lithium-ion-batteries/"
    date: "2026-01-30"
    accessed_at: "2026-06-25"
---
