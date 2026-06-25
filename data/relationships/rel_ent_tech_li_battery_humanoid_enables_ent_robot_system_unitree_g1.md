---
$id: "rel_ent_tech_li_battery_humanoid_enables_ent_robot_system_unitree_g1"
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
  id: "ent_robot_system_unitree_g1"
  name:
    en: "Unitree G1"
    zh: "宇树 G1"
    ko: "유니트리 G1"

domains:
  source_domain: "02_components"
  target_domain: "02_components"

description:
  en: "Unitree G1 uses an onboard 864 Wh battery pack to power its joints and locomotion."
  zh: "宇树 G1 使用机载 864 Wh 电池组为其关节和运动供电。"
  ko: "Unitree G1은 관절과 로코모션에 전력을 공급하기 위해 온보드 864 Wh 배터리 팩을 사용함."

verification:
  status: "partially_verified"
  reviewed_by: "ai"
  reviewed_at: "2026-06-25"
  confidence: "medium"
  notes: "Capacity figure is from industry analysis."

sources:
  - id: "src_interact_analysis_li_batteries_2026"
    type: "report"
    title: "Humanoid robots and lithium-ion batteries: Long-term commitment or short-term convenience?"
    url: "https://interactanalysis.com/insight/humanoid-robots-and-lithium-ion-batteries/"
    date: "2026-01-30"
    accessed_at: "2026-06-25"
---
