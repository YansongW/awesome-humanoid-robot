---
$id: rel_ent_technology_quasi_direct_drive_actuator_2024_uses_ent_robot_system_berkeley_humanoid_lite
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_technology_quasi_direct_drive_actuator_2024
  name:
    en: Quasi Direct Drive Actuator
    zh: 准直驱执行器
target:
  id: ent_robot_system_berkeley_humanoid_lite
  name:
    en: Berkeley Humanoid Lite
    zh: 伯克利轻量人形机器人
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 02_components
description:
  en: Quasi Direct Drive Actuator uses Berkeley Humanoid Lite.
  zh: 准直驱执行器使用伯克利轻量人形机器人。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据说明Berkeley Humanoid Lite使用自研摆线QDD（即准直驱执行器），因此该执行器被机器人系统使用。
    | 证据: - **Berkeley Humanoid Lite**（`ent_robot_system_berkeley_humanoid_lite`）：6512（10 台）与 5010（12 台）两种自研摆线 QDD，结构件可桌面
    FDM 打印；'
sources:
- id: src_001
  type: other
  title: KG body of ent_technology_quasi_direct_drive_actuator_2024
  url: https://kg.rounds-tech.com/entry/ent_technology_quasi_direct_drive_actuator_2024/
  accessed_at: '2026-08-06'
---
