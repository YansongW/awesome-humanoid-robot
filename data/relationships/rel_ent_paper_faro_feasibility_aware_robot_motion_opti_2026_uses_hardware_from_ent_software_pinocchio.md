---
$id: rel_ent_paper_faro_feasibility_aware_robot_motion_opti_2026_uses_hardware_from_ent_software_pinocchio
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses_hardware_from
source:
  id: ent_paper_faro_feasibility_aware_robot_motion_opti_2026
  name:
    en: 'FARO: Feasibility-Aware Robot Motion Optimization'
    zh: 'FARO: Feasibility-Aware Robot Motion Optimization'
target:
  id: ent_software_pinocchio
  name:
    en: Pinocchio
    zh: Pinocchio
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 08_software_middleware
description:
  en: 'FARO: Feasibility-Aware Robot Motion Optimization uses hardware from Pinocchio.'
  zh: 'FARO: Feasibility-Aware Robot Motion Optimizationuses_hardware_fromPinocchio。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明论文在实现中使用Pinocchio进行运动学/动力学计算。 | 证据: 实现层面：KSO
    用 acados 的 SQP，TO 用 Hippo SQP，模式/边优化用 Ipopt，运动学/动力学用 Pinocchio，NLP 构建用 CasADi，碰撞距离用 coal。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_faro_feasibility_aware_robot_motion_opti_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_faro_feasibility_aware_robot_motion_opti_2026/
  accessed_at: '2026-08-06'
---
