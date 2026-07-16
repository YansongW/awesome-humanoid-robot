---
$id: rel_ent_component_hollow_cup_motor_2024_uses_ent_component_dexterous_hand_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_component_hollow_cup_motor_2024
  name:
    en: Hollow Cup Motor
    zh: 空心杯电机
target:
  id: ent_component_dexterous_hand_2024
  name:
    en: Dexterous Hand
    zh: 灵巧手
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Hollow Cup Motor uses Dexterous Hand.
  zh: 空心杯电机使用灵巧手。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据说明空心杯电机作为灵巧手手指关节的驱动电机，表明灵巧手使用该电机。 | 证据: -
    **Humanoid Robot Dexterous Hands**: Serves as the drive motor for finger joints, providing high-response, low-inertia
    flexion/extension movements.'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_hollow_cup_motor_2024
  url: https://kg.rounds-tech.com/entry/ent_component_hollow_cup_motor_2024/
  accessed_at: '2026-07-16'
---
