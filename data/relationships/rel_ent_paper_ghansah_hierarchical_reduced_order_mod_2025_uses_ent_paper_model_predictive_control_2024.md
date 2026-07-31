---
$id: rel_ent_paper_ghansah_hierarchical_reduced_order_mod_2025_uses_ent_paper_model_predictive_control_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_ghansah_hierarchical_reduced_order_mod_2025
  name:
    en: Hierarchical Reduced-Order Model Predictive Control for Robust Locomotion on Humanoid Robots
    zh: 面向人形机器人稳健运动的层级化降阶模型预测控制
target:
  id: ent_paper_model_predictive_control_2024
  name:
    en: Model Predictive Control
    zh: 模型预测控制
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Hierarchical Reduced-Order Model Predictive Control for Robust Locomotion on Humanoid Robots uses Model Predictive Control.
  zh: 面向人形机器人稳健运动的层级化降阶模型预测控制使用模型预测控制。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 该论文扩展并使用了标准SRB-MPC（即Model Predictive Control）作为中层控制器。
    | 证据: - **中层MPC**：将高层生成的ALIP轨迹作为参考，扩展标准SRB-MPC（Single Rigid Body Model Predictive Control）以包含简化的手臂与躯干动力学，运行频率500 Hz。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_ghansah_hierarchical_reduced_order_mod_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_ghansah_hierarchical_reduced_order_mod_2025/
  accessed_at: '2026-07-31'
---
