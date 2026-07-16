---
$id: rel_ent_component_safety_mcu_requires_ent_standard_iso_13849
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: requires
source:
  id: ent_component_safety_mcu
  name:
    en: Safety Microcontroller Unit (Safety MCU)
    zh: 安全MCU
target:
  id: ent_standard_iso_13849
  name:
    en: ISO 13849
    zh: ISO 13849
domains:
  source_domain: 02_components
  target_domain: 12_policy_regulation_ethics
description:
  en: Safety Microcontroller Unit (Safety MCU) requires ISO 13849.
  zh: 安全MCUrequiresISO 13849。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明计算平台需要满足ISO 13849标准，安全MCU是计算平台的一部分，因此需要该标准。
    | 证据: 随着机器人进入家庭和工厂，计算平台需要同时满足功能安全（ISO 13849、IEC 61508）和网络安全（IEC 62443）要求。'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_safety_mcu
  url: https://kg.rounds-tech.com/entry/ent_component_safety_mcu/
  accessed_at: '2026-07-16'
---
