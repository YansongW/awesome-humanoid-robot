---
$id: rel_ent_method_model_predictive_control_implemented_on_ent_robot_unitree_h1_humanoid_robot_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: implemented_on
source:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
target:
  id: ent_robot_unitree_h1_humanoid_robot_2024
  name:
    en: Unitree H1 Humanoid Robot
    zh: 宇树 H1 人形机器人
domains:
  source:
  - 07_ai_models_algorithms
  - 06_design_engineering
  target:
  - 06_design_engineering
  - 02_components
description:
  en: MPC is used for whole-body motion generation on Unitree H1.
  zh: MPC用于Unitree H1的全身运动生成。
  ko: MPC는 Unitree H1의 전신 동작 생성에 사용됩니다.
verification:
  confidence: medium
  notes: 'bulk-added confidence on 2026-07-17 by backfill_rel_confidence.py; pending human review | WP4 2026-08-11: endpoint
    id rewritten (ent_method_model_predictive_control→ent_method_model_predictive_control, ent_robot_unitree_h1_humanoid_robot_2024→ent_robot_unitree_h1_humanoid_robot_2024);
    original file rel_ent_paper_model_predictive_control_2024_implemented_on_ent_robot_unitree_h1_humanoid_robot_2024.'
  status: partially_verified
  sources: []
  reviewed_by: ai_autonomous
  reviewed_at: '2026-07-02T00:21:22.207515+00:00'
sources:
- type: website
  url: ''
  description: Workflow relationship curated from public project pages and literature.
  id: curated_workflow_relationship
---
