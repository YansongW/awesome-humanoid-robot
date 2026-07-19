---
$id: rel_ent_component_7dof_arm_2024_uses_ent_method_dexterous_manipulation
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_component_7dof_arm_2024
  name:
    en: 7-DoF Robotic Arm
    zh: 七自由度机械臂
target:
  id: ent_method_dexterous_manipulation
  name:
    en: Dexterous Manipulation
    zh: 灵巧操作
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: 7-DoF Robotic Arm uses Dexterous Manipulation.
  zh: 七自由度机械臂使用灵巧操作。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link_retry. Evidence: 7自由度机械臂用于灵巧操作任务，利用其冗余自由度。'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_7dof_arm_2024
  url: https://kg.rounds-tech.com/entry/ent_component_7dof_arm_2024/
  accessed_at: '2026-07-17'
---
