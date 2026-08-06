---
$id: rel_ent_method_whole_body_control_uses_ent_software_pinocchio
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_method_whole_body_control
  name:
    en: Whole-Body Control (WBC)
    zh: 全身控制（WBC）
target:
  id: ent_software_pinocchio
  name:
    en: Pinocchio
    zh: Pinocchio
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 08_software_middleware
description:
  en: Whole-Body Control (WBC) uses Pinocchio.
  zh: 全身控制（WBC）使用Pinocchio。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据显示TSID（一种WBC实现）基于Pinocchio，因此WBC使用Pinocchio。
    | 证据: | 开源实现 | TSID（C++，BSD-2-Clause，基于 Pinocchio） | 含人形/四足示例 | TSID GitHub README |'
sources:
- id: src_001
  type: other
  title: KG body of ent_method_whole_body_control
  url: https://kg.rounds-tech.com/entry/ent_method_whole_body_control/
  accessed_at: '2026-08-06'
---
