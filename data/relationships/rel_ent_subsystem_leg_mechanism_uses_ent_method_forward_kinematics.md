---
$id: rel_ent_subsystem_leg_mechanism_uses_ent_method_forward_kinematics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_subsystem_leg_mechanism
  name:
    en: Leg Mechanism
    zh: 腿部机构
target:
  id: ent_method_forward_kinematics
  name:
    en: Forward Kinematics
    zh: 正运动学
domains:
  source_domain: 06_design_engineering
  target_domain: 06_design_engineering
description:
  en: Leg Mechanism uses Forward Kinematics.
  zh: 腿部机构使用正运动学。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 腿部机构的运动学建模需要正向运动学来计算末端位置。'
sources:
- id: src_001
  type: other
  title: KG body of ent_subsystem_leg_mechanism
  url: https://kg.rounds-tech.com/entry/ent_subsystem_leg_mechanism/
  accessed_at: '2026-07-16'
---
