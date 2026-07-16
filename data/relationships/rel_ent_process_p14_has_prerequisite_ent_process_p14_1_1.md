---
$id: rel_ent_process_p14_has_prerequisite_ent_process_p14_1_1
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_process_p14
  name:
    en: Software & Integration
    zh: 软件中间件与系统集成（Software & Integration）
target:
  id: ent_process_p14_1_1
  name:
    en: Selection and adaptation of middleware
    zh: 中间件选型与适配
domains:
  source_domain: 08_software_middleware
  target_domain: 08_software_middleware
description:
  en: Software & Integration has prerequisite Selection and adaptation of middleware.
  zh: 软件中间件与系统集成（Software & Integration）前置依赖中间件选型与适配。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据说明Software & Integration需要整理Selection and
    adaptation of middleware的输入与目标，表明后者是前者的前提。 | 证据: 1 输入梳理与目标量化**：整理「中间件选型与适配」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner
    与里程碑。'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p14
  url: https://kg.rounds-tech.com/entry/ent_process_p14/
  accessed_at: '2026-07-16'
---
