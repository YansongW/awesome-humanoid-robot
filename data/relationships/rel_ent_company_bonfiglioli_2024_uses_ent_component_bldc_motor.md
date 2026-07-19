---
$id: rel_ent_company_bonfiglioli_2024_uses_ent_component_bldc_motor
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_company_bonfiglioli_2024
  name:
    en: Bonfiglioli
    zh: 邦飞利
target:
  id: ent_component_bldc_motor
  name:
    en: Brushless DC Motor
    zh: 无刷直流电机
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Bonfiglioli uses Brushless DC Motor.
  zh: 邦飞利使用无刷直流电机。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: Bonfiglioli的驱动系统通常使用无刷直流电机'
sources:
- id: src_001
  type: other
  title: KG body of ent_company_bonfiglioli_2024
  url: https://kg.rounds-tech.com/entry/ent_company_bonfiglioli_2024/
  accessed_at: '2026-07-17'
---
