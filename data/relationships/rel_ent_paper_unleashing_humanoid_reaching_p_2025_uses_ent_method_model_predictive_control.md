---
$id: rel_ent_paper_unleashing_humanoid_reaching_p_2025_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_unleashing_humanoid_reaching_p_2025
  name:
    en: Unleashing Humanoid Reaching Potential via Real-world-Ready Skill Space
    zh: 通过真实部署就绪的技能空间释放人形机器人的潜力
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Unleashing Humanoid Reaching Potential via Real-world-Ready Skill Space uses Model Predictive Control (MPC).
  zh: 通过真实部署就绪的技能空间释放人形机器人的潜力使用模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文使用模型预测控制（MPC）进行实时优化以确保运动符合动力学约束。 | 证据: 框架将高层技能规划与低层运动控制解耦：高层模块负责根据视觉感知结果（如目标物体位置、障碍物分布）选择技能原语（如“抓取”、“放置”），而低层模块则通过扩散模型生成连续关节轨迹，并经由全身控制器（Whole-Body
    Controller）或模型预测控制（MPC）进行实时优化，确保运动符合动力学约束与安全性要求。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_unleashing_humanoid_reaching_p_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_unleashing_humanoid_reaching_p_2025/
  accessed_at: '2026-07-16'
---
