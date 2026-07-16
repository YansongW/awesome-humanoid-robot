---
$id: rel_ent_paper_unleashing_humanoid_reaching_p_2025_uses_ent_paper_model_predictive_control_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_unleashing_humanoid_reaching_p_2025
  name:
    en: Unleashing Humanoid Reaching Potential via Real-world-Ready Skill Space
    zh: 通过真实部署就绪的技能空间释放人形机器人的潜力
target:
  id: ent_paper_model_predictive_control_2024
  name:
    en: Model Predictive Control
    zh: 模型预测控制
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Unleashing Humanoid Reaching Potential via Real-world-Ready Skill Space uses Model Predictive Control.
  zh: 通过真实部署就绪的技能空间释放人形机器人的潜力使用模型预测控制。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文使用模型预测控制（MPC）进行实时优化以确保运动符合动力学约束。 | 证据: , target
    object position, obstacle distribution), while the low-level module generates continuous joint trajectories through diffusion
    models and performs real-time optimization via a Whole-Body Controller or Model Predictive Control (MPC) to ensure '
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_unleashing_humanoid_reaching_p_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_unleashing_humanoid_reaching_p_2025/
  accessed_at: '2026-07-16'
---
