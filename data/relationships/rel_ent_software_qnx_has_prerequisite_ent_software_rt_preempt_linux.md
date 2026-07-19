---
$id: rel_ent_software_qnx_has_prerequisite_ent_software_rt_preempt_linux
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_software_qnx
  name:
    en: QNX
    zh: QNX
target:
  id: ent_software_rt_preempt_linux
  name:
    en: Linux RT-PREEMPT
    zh: Linux RT-PREEMPT
domains:
  source_domain: 08_software_middleware
  target_domain: 08_software_middleware
description:
  en: QNX has prerequisite Linux RT-PREEMPT.
  zh: QNX前置依赖Linux RT-PREEMPT。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: RT-PREEMPT Linux展示了如何将通用操作系统改造为实时系统，与QNX的微内核实时设计形成对比学习。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
