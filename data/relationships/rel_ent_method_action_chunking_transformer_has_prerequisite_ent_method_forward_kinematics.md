---
$id: rel_ent_method_action_chunking_transformer_has_prerequisite_ent_method_forward_kinematics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_method_action_chunking_transformer
  name:
    en: Action Chunking with Transformers (ACT)
    zh: 动作分块变压器（ACT）
target:
  id: ent_method_forward_kinematics
  name:
    en: Forward Kinematics
    zh: 正运动学
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 06_design_engineering
description:
  en: Action Chunking with Transformers (ACT) has prerequisite Forward Kinematics.
  zh: 动作分块变压器（ACT）前置依赖正运动学。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 正向运动学提供了动作序列预测所需的空间几何理解'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
