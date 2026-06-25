---
$id: "rel_ent_material_al_mg_alloy_humanoid_enables_ent_robot_system_tesla_optimus"
$schema: "../../../../../data/schema/v1/relationship_schema.json"
$version: 1

type: "enables"

source:
  id: "ent_material_al_mg_alloy_humanoid"
  name:
    en: "Aluminum-Magnesium Alloy for Humanoid Robot Lightweight Structure"
    zh: "人形机器人轻量化结构用铝镁合金"
    ko: "휴로이드 로봇 경량 구조용 알루미늄-마그네슘 합금"

target:
  id: "ent_robot_system_tesla_optimus"
  name:
    en: "Tesla Optimus"
    zh: "特斯拉 Optimus"
    ko: "테슬라 옵티머스"

domains:
  source_domain: "01_raw_materials"
  target_domain: "02_components"

description:
  en: "Aluminum-magnesium alloys are reported to be used in Tesla Optimus-Gen2 limb skeletons, contributing to weight reduction while maintaining rigidity."
  zh: "据报道，铝镁合金用于特斯拉 Optimus-Gen2 的肢体骨架，有助于在保持刚度的同时减轻重量。"
  ko: "알루미늄-마그네슘 합금은 Tesla Optimus-Gen2의 사지 골격에 사용되어 강성을 유지하면서 중량을 줄이는 데 기여한다고 볏됨."

verification:
  status: "partially_verified"
  reviewed_by: "ai"
  reviewed_at: "2026-06-25"
  confidence: "medium"
  notes: "Specific product application is based on industry trade coverage, not official Tesla disclosure."

sources:
  - id: "src_aluminium_china_metal_materials_2025"
    type: "website"
    title: "Metal Materials for Humanoid Robots: Applications and Market Outlook of Aluminum"
    url: "https://www.aluminiumchina.com/en-gb/news-center/industry-news/2025/4/5.html"
    date: "2025-04-05"
    accessed_at: "2026-06-25"
---
