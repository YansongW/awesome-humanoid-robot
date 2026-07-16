---
$id: rel_ent_process_p12_requires_ent_process_p12_1_1
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: requires
source:
  id: ent_process_p12
  name:
    en: VLA / WAM / AI algorithm integration (AI & Perception)
    zh: VLA / WAM / AI 算法集成（AI & Perception）
target:
  id: ent_process_p12_1_1
  name:
    en: Sensor Selection and Calibration
    zh: 传感器选型与标定
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: VLA / WAM / AI algorithm integration (AI & Perception) requires Sensor Selection and Calibration.
  zh: VLA / WAM / AI 算法集成（AI & Perception）requires传感器选型与标定。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 源方法需要传感器选型与标定作为上游输入 | 证据: 1 输入梳理与目标量化**：整理「传感器选型与标定」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确
    Owner 与里程碑。'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p12
  url: https://kg.rounds-tech.com/entry/ent_process_p12/
  accessed_at: '2026-07-16'
---
