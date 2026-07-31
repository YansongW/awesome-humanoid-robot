---
$id: rel_ent_robot_system_bruce_compares_with_ent_robot_system_toddlerbot
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: compares_with
source:
  id: ent_robot_system_bruce
  name:
    en: BRUCE (Bipedal Robot Unit with Compliance Enhanced)
    zh: BRUCE 儿童尺寸人形机器人
target:
  id: ent_robot_system_toddlerbot
  name:
    en: ToddlerBot
    zh: ToddlerBot 幼儿机器人
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: BRUCE (Bipedal Robot Unit with Compliance Enhanced) compares with ToddlerBot.
  zh: BRUCE 儿童尺寸人形机器人compares_withToddlerBot 幼儿机器人。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据提到第三方论文对比表包含ToddlerBot，表明BRUCE与ToddlerBot进行了比较。
    | 证据: 硬件成本方面，第三方论文对比表（ToddlerBot, arXiv:2502.'
sources:
- id: src_001
  type: other
  title: KG body of ent_robot_system_bruce
  url: https://kg.rounds-tech.com/entry/ent_robot_system_bruce/
  accessed_at: '2026-07-31'
---
