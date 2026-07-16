---
$id: rel_ent_robot_system_openloong_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_robot_system_openloong
  name:
    en: OpenLoong (Qinglong) Open-Source Humanoid Robot
    zh: OpenLoong / 青龙开源人形机器人
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: OpenLoong's open-source whole-body dynamics control framework OpenLoong-Dyn-Control is built on
    MPC plus WBC and is deployable in MuJoCo simulation.
  zh: OpenLoong 开源的全身动力学控制框架 OpenLoong-Dyn-Control 基于 MPC + WBC 构建，可部署于 MuJoCo 仿真。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 来源档案 data/roadmap/research/openloong-qinglong.md 确认 OpenLoong-Dyn-Control 基于 MPC + WBC。
sources:
- id: src_001
  type: website
  title: OpenLoong-Dyn-Control GitHub Repository
  url: https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/main/README-zh.md
  accessed_at: '2026-07-01'
---
