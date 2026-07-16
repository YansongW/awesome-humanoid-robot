---
$id: rel_ent_application_industrial_manufacturing_uses_ent_robot_boston_dynamics_atlas_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_application_industrial_manufacturing
  name:
    en: Industrial Manufacturing
    zh: 工业制造
target:
  id: ent_robot_boston_dynamics_atlas_2024
  name:
    en: Boston Dynamics Atlas
    zh: 波士顿动力 Atlas
domains:
  source_domain: 11_applications_markets
  target_domain: 06_design_engineering
description:
  en: Industrial Manufacturing uses Boston Dynamics Atlas.
  zh: 工业制造使用波士顿动力 Atlas。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 工业制造应用场景使用了波士顿动力Atlas机器人。 | 证据: - **Boston Dynamics
    Atlas**：使用嵌入式实时计算机处理状态估计与步态控制，液压/电动执行器由专用驱动板闭环控制，强调高动态运动的确定性。'
sources:
- id: src_001
  type: other
  title: KG body of ent_application_industrial_manufacturing
  url: https://kg.rounds-tech.com/entry/ent_application_industrial_manufacturing/
  accessed_at: '2026-07-16'
---
