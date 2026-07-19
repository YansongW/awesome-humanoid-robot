---
$id: rel_ent_technology_mobile_aloha_2024_has_prerequisite_ent_technology_aloha_teleoperation_system_2023
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_technology_mobile_aloha_2024
  name:
    en: Mobile ALOHA
    zh: Mobile ALOHA
target:
  id: ent_technology_aloha_teleoperation_system_2023
  name:
    en: ALOHA Teleoperation System
    zh: ALOHA 遥操作系统
domains:
  source_domain: 09_data_datasets
  target_domain: 09_data_datasets
description:
  en: Mobile ALOHA has prerequisite ALOHA Teleoperation System.
  zh: Mobile ALOHA前置依赖ALOHA 遥操作系统。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: Mobile ALOHA是ALOHA的移动扩展，必须先理解基础的双臂遥操作原理。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
