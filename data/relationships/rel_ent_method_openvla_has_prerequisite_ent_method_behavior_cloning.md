---
$id: rel_ent_method_openvla_has_prerequisite_ent_method_behavior_cloning
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_method_openvla
  name:
    en: OpenVLA
    zh: OpenVLA
target:
  id: ent_method_behavior_cloning
  name:
    en: Behavior Cloning
    zh: 行为克隆
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: OpenVLA has prerequisite Behavior Cloning.
  zh: OpenVLA前置依赖行为克隆。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: OpenVLA基于行为克隆范式，从专家演示中学习视觉-语言-动作映射。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
