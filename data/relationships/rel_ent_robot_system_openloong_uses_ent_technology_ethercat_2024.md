---
$id: rel_ent_robot_system_openloong_uses_ent_technology_ethercat_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_robot_system_openloong
  name:
    en: OpenLoong (Qinglong) Open-Source Humanoid Robot
    zh: OpenLoong / 青龙开源人形机器人
target:
  id: ent_technology_ethercat_2024
  name:
    en: EtherCAT
    zh: EtherCAT
domains:
  source_domain: 02_components
  target_domain: 08_software_middleware
description:
  en: The OpenLoong/Qinglong humanoid uses EtherCAT as its fieldbus, corroborated by industry analysis
    and the loong_driver_sdk repository.
  zh: OpenLoong / 青龙人形机器人采用 EtherCAT 总线，行业分析文章与 loong_driver_sdk 仓库均可佐证。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 来源档案 data/roadmap/research/openloong-qinglong.md 确认 EtherCAT 总线（行业分析与 SDK 仓库佐证）。
sources:
- id: src_001
  type: website
  title: OpenLoong on AtomGit
  url: https://atomgit.com/openloong
  accessed_at: '2026-07-01'
---
