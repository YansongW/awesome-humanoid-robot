---
$id: rel_ent_process_p4_has_prerequisite_ent_process_p4_2_2
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_process_p4
  name:
    en: Design of Joint Module and Actuator & Drive
    zh: 关节模组与驱动系统设计（Actuator & Drive）
target:
  id: ent_process_p4_2_2
  name:
    en: Selection of reducer and transmission
    zh: 减速器与传动选型
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Design of Joint Module and Actuator & Drive has prerequisite Selection of reducer and transmission.
  zh: 关节模组与驱动系统设计（Actuator & Drive）前置依赖减速器与传动选型。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明减速器与传动选型需要上游输入和参考标准，因此是关节模组设计的前提。 | 证据:
    1 输入梳理与目标量化**：整理「减速器与传动选型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p4
  url: https://kg.rounds-tech.com/entry/ent_process_p4/
  accessed_at: '2026-07-16'
---
