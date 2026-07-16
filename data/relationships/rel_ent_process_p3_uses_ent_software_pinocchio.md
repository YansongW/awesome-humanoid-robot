---
$id: rel_ent_process_p3_uses_ent_software_pinocchio
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_process_p3
  name:
    en: System Architecture and Electromechanical Master Design (System / Preliminary Design)
    zh: 系统架构与机电总体设计（System / Preliminary Design）
target:
  id: ent_software_pinocchio
  name:
    en: Pinocchio
    zh: Pinocchio
domains:
  source_domain: 06_design_engineering
  target_domain: 08_software_middleware
description:
  en: System Architecture and Electromechanical Master Design (System / Preliminary Design) uses Pinocchio.
  zh: 系统架构与机电总体设计（System / Preliminary Design）使用Pinocchio。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 源方法在证据中列出了Pinocchio作为工具。 | 证据: - **方法 / 工具**：解析法、Matlab/Python、Pinocchio/RBDL、典型动作仿真'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p3
  url: https://kg.rounds-tech.com/entry/ent_process_p3/
  accessed_at: '2026-07-16'
---
