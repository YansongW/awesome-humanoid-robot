---
$id: rel_ent_company_zeroerr_2024_supplies_ent_component_bldc_motor
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: supplies
source:
  id: ent_company_zeroerr_2024
  name:
    en: ZeroErr
    zh: ZeroErr
target:
  id: ent_component_bldc_motor
  name:
    en: Brushless DC Motor
    zh: 无刷直流电机
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: ZeroErr supplies Brushless DC Motor.
  zh: ZeroErrsupplies无刷直流电机。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link_retry. Evidence: ZeroErr制造高精度机器人关节模块，供应无刷直流电机。'
sources:
- id: src_001
  type: other
  title: KG body of ent_company_zeroerr_2024
  url: https://kg.rounds-tech.com/entry/ent_company_zeroerr_2024/
  accessed_at: '2026-07-17'
---
