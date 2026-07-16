---
$id: rel_ent_subsystem_leg_mechanism_uses_ent_principle_zero_moment_point
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_subsystem_leg_mechanism
  name:
    en: Leg Mechanism
    zh: 腿部机构
target:
  id: ent_principle_zero_moment_point
  name:
    en: Zero Moment Point (ZMP)
    zh: 零力矩点（ZMP）
domains:
  source_domain: 06_design_engineering
  target_domain: 06_design_engineering
description:
  en: Leg Mechanism uses Zero Moment Point (ZMP).
  zh: 腿部机构使用零力矩点（ZMP）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 腿部机构支撑行走时，零力矩点原理用于稳定性分析。'
sources:
- id: src_001
  type: other
  title: KG body of ent_subsystem_leg_mechanism
  url: https://kg.rounds-tech.com/entry/ent_subsystem_leg_mechanism/
  accessed_at: '2026-07-16'
---
