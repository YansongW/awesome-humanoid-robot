---
$id: rel_ent_software_mujoco_physics_engine_2022_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_software_mujoco_physics_engine_2022
  name:
    en: MuJoCo Physics Engine
    zh: MuJoCo 物理引擎
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source:
  - 08_software_middleware
  - 07_ai_models_algorithms
  target:
  - 07_ai_models_algorithms
  - 06_design_engineering
description:
  en: MuJoCo is commonly used to prototype and evaluate MPC controllers.
  zh: MuJoCo常用于原型化和评估MPC控制器。
  ko: MuJoCo는 MPC 컨트롤러의 프로토타입 및 평가에 일반적으로 사용됩니다.
verification:
  confidence: medium
  notes: 'bulk-added confidence on 2026-07-17 by backfill_rel_confidence.py; pending human review | WP4 2026-08-11: endpoint
    id rewritten (ent_software_mujoco_physics_engine_2022→ent_software_mujoco_physics_engine_2022, ent_method_model_predictive_control→ent_method_model_predictive_control);
    original file rel_ent_software_mujoco_physics_engine_2022_used_by_ent_paper_model_predictive_control_2024.'
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
