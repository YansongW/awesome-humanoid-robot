---
$id: rel_ent_process_p4_3_1_is_part_of_ent_process_p4
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_process_p4_3_1
  name:
    en: Design/selection of motor driver
    zh: 电机驱动器设计/选型
target:
  id: ent_process_p4
  name:
    en: Design of Joint Module and Actuator & Drive
    zh: 关节模组与驱动系统设计（Actuator & Drive）
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Design/selection of motor driver is part of Design of Joint Module and Actuator & Drive.
  zh: 电机驱动器设计/选型is_part_of关节模组与驱动系统设计（Actuator & Drive）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明该方法是关节模组与驱动系统设计的一部分 | 证据: **所属阶段/工作包**：关节模组与驱动系统设计（Actuator
    & Drive）'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p4_3_1
  url: https://kg.rounds-tech.com/entry/ent_process_p4_3_1/
  accessed_at: '2026-07-16'
---
