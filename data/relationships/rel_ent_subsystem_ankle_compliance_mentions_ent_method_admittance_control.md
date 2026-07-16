---
$id: rel_ent_subsystem_ankle_compliance_mentions_ent_method_admittance_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_subsystem_ankle_compliance
  name:
    en: Ankle Compliance Mechanism
    zh: 脚踝柔顺机构
target:
  id: ent_method_admittance_control
  name:
    en: Admittance Control
    zh: 导纳控制
domains:
  source_domain: 06_design_engineering
  target_domain: 07_ai_models_algorithms
description:
  en: Ankle Compliance Mechanism mentions Admittance Control.
  zh: 脚踝柔顺机构提及导纳控制。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据中提到了Admittance Control，但未明确说明Ankle Compliance
    Mechanism与它的具体关系。 | 证据: note "Terminology: Stop, Recede, Admittance Control, Emergency Stop"'
sources:
- id: src_001
  type: other
  title: KG body of ent_subsystem_ankle_compliance
  url: https://kg.rounds-tech.com/entry/ent_subsystem_ankle_compliance/
  accessed_at: '2026-07-16'
---
