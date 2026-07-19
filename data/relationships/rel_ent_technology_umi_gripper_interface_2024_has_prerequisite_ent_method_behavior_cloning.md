---
$id: rel_ent_technology_umi_gripper_interface_2024_has_prerequisite_ent_method_behavior_cloning
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_technology_umi_gripper_interface_2024
  name:
    en: UMI Gripper Interface
    zh: UMI 夹爪接口
target:
  id: ent_method_behavior_cloning
  name:
    en: Behavior Cloning
    zh: 行为克隆
domains:
  source_domain: 09_data_datasets
  target_domain: 07_ai_models_algorithms
description:
  en: UMI Gripper Interface has prerequisite Behavior Cloning.
  zh: UMI 夹爪接口前置依赖行为克隆。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: UMI夹爪界面采集的演示数据通常用于行为克隆训练'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
