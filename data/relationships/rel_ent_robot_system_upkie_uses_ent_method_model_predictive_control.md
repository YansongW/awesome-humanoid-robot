---
$id: rel_ent_robot_system_upkie_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_robot_system_upkie
  name:
    en: Upkie Wheeled Biped Robot
    zh: Upkie 轮足双足机器人
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: Upkie ships with an out-of-the-box MPC (qpmpc) balancing controller example, alongside PID and reinforcement-learning
    examples.
  zh: Upkie 开箱自带 MPC（qpmpc）平衡控制示例，与 PID、强化学习示例并列提供。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 来源档案 data/roadmap/research/upkie.md 确认自带 PID/MPC(qpmpc)/RL 三种平衡控制范式示例。
sources:
- id: src_001
  type: website
  title: upkie on PyPI
  url: https://pypi.org/project/upkie/
  accessed_at: '2026-07-01'
---
