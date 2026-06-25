---
$id: rel_ent_component_manufacturer_nidec_drive_technology_produces_ent_component_harmonic_drive_reducer
$schema: "../../../../../data/schema/v1/relationship_schema.json"
$version: 1

type: produces

source:
  id: ent_component_manufacturer_nidec_drive_technology
  name:
    en: Nidec Drive Technology
    zh: 尼得科传动技术
    ko: 니덱 드라이브 테크놀로지

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
  en: Nidec Drive Technology produces the FLEXWAVE family of strain-wave gear reducers, which are a type of harmonic drive reducer used in humanoid robot joints.
  zh: 尼得科传动技术生产 FLEXWAVE 系列应变波齿轮减速器，这是一种用于人形机器人关节的谐波减速器。
  ko: 니덱 드라이브 테크놀로지는 휴이노이드 로봇 관절에 사용되는 하모닉 드라이브 감속기의 일종인 FLEXWAVE 스트레인 웨이브 기어 감속기 제품군을 생산함.

verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: Confirmed by Nidec's official product page; specific humanoid OEM adoption is not disclosed.

sources:
  - id: src_001_nidec_official
    type: website
    title: Nidec - Highly Developed Humanoid Robots
    url: https://www.nidec-dtc.com/humanoid-robots/
    date: '2026'
    accessed_at: '2026-06-25'
---
