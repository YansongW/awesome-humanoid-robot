---
$id: rel_ent_process_p7_2_3_uses_ent_component_dexterous_hand_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_process_p7_2_3
  name:
    en: Simulation of manipulation and grasping
    zh: 操作与抓取仿真
target:
  id: ent_component_dexterous_hand_2024
  name:
    en: Dexterous Hand
    zh: 灵巧手
domains:
  source_domain: 08_software_middleware
  target_domain: 02_components
description:
  en: Simulation of manipulation and grasping uses Dexterous Hand.
  zh: 操作与抓取仿真使用灵巧手。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 仿真操作与抓取方法使用了灵巧手模型 | 证据: **Method/Tool**: Arm/Dexterous
    Hand Model, Grasp Pose Generation, Contact Force Feedback'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p7_2_3
  url: https://kg.rounds-tech.com/entry/ent_process_p7_2_3/
  accessed_at: '2026-07-16'
---
