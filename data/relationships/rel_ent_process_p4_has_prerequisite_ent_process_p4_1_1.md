---
$id: rel_ent_process_p4_has_prerequisite_ent_process_p4_1_1
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_process_p4
  name:
    en: Design of Joint Module and Actuator & Drive
    zh: 关节模组与驱动系统设计（Actuator & Drive）
target:
  id: ent_process_p4_1_1
  name:
    en: Specification of joint performance requirements
    zh: 关节性能需求精化
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Design of Joint Module and Actuator & Drive has prerequisite Specification of joint performance requirements.
  zh: 关节模组与驱动系统设计（Actuator & Drive）前置依赖关节性能需求精化。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 源方法需要目标作为输入或前提 | 证据: 1 输入梳理与目标量化**：整理「关节性能需求精化」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确
    Owner 与里程碑。'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p4
  url: https://kg.rounds-tech.com/entry/ent_process_p4/
  accessed_at: '2026-07-16'
---
