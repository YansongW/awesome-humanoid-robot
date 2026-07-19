---
$id: rel_ent_technology_umi_gripper_interface_2024_has_prerequisite_ent_technology_aloha_teleoperation_system_2023
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_technology_umi_gripper_interface_2024
  name:
    en: UMI Gripper Interface
    zh: UMI 夹爪接口
target:
  id: ent_technology_aloha_teleoperation_system_2023
  name:
    en: ALOHA Teleoperation System
    zh: ALOHA 遥操作系统
domains:
  source_domain: 09_data_datasets
  target_domain: 09_data_datasets
description:
  en: UMI Gripper Interface has prerequisite ALOHA Teleoperation System.
  zh: UMI 夹爪接口前置依赖ALOHA 遥操作系统。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: UMI是ALOHA遥操作系统的轻量化变体'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
