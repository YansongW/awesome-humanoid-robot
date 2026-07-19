---
$id: rel_ent_method_whole_body_control_has_prerequisite_ent_method_impedance_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_method_whole_body_control
  name:
    en: Whole-Body Control (WBC)
    zh: 全身控制（WBC）
target:
  id: ent_method_impedance_control
  name:
    en: Impedance Control
    zh: 阻抗控制
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Whole-Body Control (WBC) has prerequisite Impedance Control.
  zh: 全身控制（WBC）前置依赖阻抗控制。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 全身控制常结合阻抗控制来管理接触力和柔顺性，实现安全的物理交互。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
