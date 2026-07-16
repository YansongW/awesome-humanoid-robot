---
$id: rel_ent_process_p3_1_3_uses_ent_software_pinocchio
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_process_p3_1_3
  name:
    en: Preliminary analysis of kinematics and dynamics
    zh: 运动学与动力学初步分析
target:
  id: ent_software_pinocchio
  name:
    en: Pinocchio
    zh: Pinocchio
domains:
  source_domain: 06_design_engineering
  target_domain: 08_software_middleware
description:
  en: Preliminary analysis of kinematics and dynamics uses Pinocchio.
  zh: 运动学与动力学初步分析使用Pinocchio。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 源方法使用了目标软件平台Pinocchio | 证据: **方法 / 工具**：解析法、Matlab/Python、Pinocchio/RBDL、典型动作仿真'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p3_1_3
  url: https://kg.rounds-tech.com/entry/ent_process_p3_1_3/
  accessed_at: '2026-07-16'
---
