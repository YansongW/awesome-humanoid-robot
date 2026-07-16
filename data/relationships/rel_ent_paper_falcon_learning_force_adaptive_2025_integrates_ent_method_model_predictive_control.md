---
$id: rel_ent_paper_falcon_learning_force_adaptive_2025_integrates_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: integrates
source:
  id: ent_paper_falcon_learning_force_adaptive_2025
  name:
    en: 'FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation'
    zh: FALCON｜学习力自适应人形移动操作
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 06_design_engineering
  target_domain: 07_ai_models_algorithms
description:
  en: 'FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation integrates Model Predictive Control (MPC).'
  zh: FALCON｜学习力自适应人形移动操作integrates模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: FALCON将全身控制器（WBC）与模型预测控制（MPC）集成到统一链路中。 | 证据:
    该工作的主要贡献在于将全身控制器（WBC）与模型预测控制（MPC）集成到统一的训练与部署链路中，从而有效弥合高层任务目标与底层关节动作之间的语义鸿沟。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_falcon_learning_force_adaptive_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_falcon_learning_force_adaptive_2025/
  accessed_at: '2026-07-16'
---
