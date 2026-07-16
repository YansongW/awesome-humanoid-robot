---
$id: rel_ent_process_p16_has_prerequisite_ent_process_p16_2_2
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_process_p16
  name:
    en: Pilot & Production Ramp
    zh: 小批量试产与量产准备（Pilot & Production Ramp）
target:
  id: ent_process_p16_2_2
  name:
    en: Establishment of quality control system
    zh: 质量控制体系建立
domains:
  source_domain: 05_mass_production
  target_domain: 05_mass_production
description:
  en: Pilot & Production Ramp has prerequisite Establishment of quality control system.
  zh: 小批量试产与量产准备（Pilot & Production Ramp）前置依赖质量控制体系建立。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明Pilot & Production Ramp需要整理质量控制体系建立的上游输入和资源，因此前者需要后者作为前提。
    | 证据: 1 输入梳理与目标量化**：整理「质量控制体系建立」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p16
  url: https://kg.rounds-tech.com/entry/ent_process_p16/
  accessed_at: '2026-07-16'
---
