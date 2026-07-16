---
$id: rel_ent_subsystem_leg_mechanism_uses_ent_method_inverse_kinematics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_subsystem_leg_mechanism
  name:
    en: Leg Mechanism
    zh: 腿部机构
target:
  id: ent_method_inverse_kinematics
  name:
    en: Inverse Kinematics
    zh: 逆运动学
domains:
  source_domain: 06_design_engineering
  target_domain: 06_design_engineering
description:
  en: Leg Mechanism uses Inverse Kinematics.
  zh: 腿部机构使用逆运动学。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 腿部机构的设计和运动学分析需要使用逆运动学方法。'
sources:
- id: src_001
  type: other
  title: KG body of ent_subsystem_leg_mechanism
  url: https://kg.rounds-tech.com/entry/ent_subsystem_leg_mechanism/
  accessed_at: '2026-07-16'
---
