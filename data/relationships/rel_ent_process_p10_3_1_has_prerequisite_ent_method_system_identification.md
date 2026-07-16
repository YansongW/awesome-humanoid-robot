---
$id: rel_ent_process_p10_3_1_has_prerequisite_ent_method_system_identification
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_process_p10_3_1
  name:
    en: System Identification and Parameter Calibration
    zh: 系统辨识与参数校准
target:
  id: ent_method_system_identification
  name:
    en: System Identification
    zh: 系统辨识
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: System Identification and Parameter Calibration has prerequisite System Identification.
  zh: 系统辨识与参数校准前置依赖系统辨识。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据提到需要为“系统辨识与参数标定”组织上游输入和参考标准，表明“系统辨识”是其上游或前提。
    | 证据: - Organize upstream inputs, reference standards, and resources required for "System Identification and Parameter
    Calibration," convert completion criteria into quantifiable acceptance indicators, and clarify the Owner and milestones.'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p10_3_1
  url: https://kg.rounds-tech.com/entry/ent_process_p10_3_1/
  accessed_at: '2026-07-16'
---
