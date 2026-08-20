---
$id: rel_ent_method_model_predictive_control_requires_ent_component_inertial_measurement_unit_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: requires
source:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
target:
  id: ent_component_inertial_measurement_unit_2024
  name:
    en: Inertial Measurement Unit
    zh: 惯性测量单元
domains:
  source:
  - 07_ai_models_algorithms
  - 06_design_engineering
  target:
  - 02_components
  - 06_design_engineering
description:
  en: MPC requires IMU feedback for state estimation.
  zh: MPC需要IMU反馈进行状态估计。
  ko: MPC는 상태 추정을 위해 IMU 피드백이 필요합니다.
verification:
  confidence: medium
  notes: 'bulk-added confidence on 2026-07-17 by backfill_rel_confidence.py; pending human review | WP4 2026-08-11: endpoint
    id rewritten (ent_method_model_predictive_control→ent_method_model_predictive_control, ent_component_inertial_measurement_unit_2024→ent_component_inertial_measurement_unit_2024);
    original file rel_ent_paper_model_predictive_control_2024_requires_ent_component_inertial_measurement_unit_2024.'
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
