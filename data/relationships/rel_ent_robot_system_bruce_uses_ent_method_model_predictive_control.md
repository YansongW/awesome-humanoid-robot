---
$id: rel_ent_robot_system_bruce_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_robot_system_bruce
  name:
    en: BRUCE (Bipedal Robot Unit with Compliance Enhanced)
    zh: BRUCE 儿童尺寸人形机器人
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: BRUCE runs a variable-frequency MPC locomotion control algorithm supporting walking, running and
    jumping.
  zh: BRUCE 运行可变周期（variable-frequency）MPC 运控算法，支持行走/跑步/跳跃等高动态行为。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 来源档案 data/roadmap/research/bruce-westwood.md 确认可变周期 MPC 运控算法。
sources:
- id: src_001
  type: website
  title: BRUCE at World Robot Conference
  url: https://www.worldrobotconference.com/ex/product/244.html
  accessed_at: '2026-07-01'
---
