---
$id: rel_ent_paper_hypermotion_learning_hybrid_be_2024_mentions_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_hypermotion_learning_hybrid_be_2024
  name:
    en: 'HYPERmotion: Learning Hybrid Behavior Planning for Autonomous Loco-manipulation'
    zh: HYPERmotion｜学习自主移动操作的混合行为规划
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'HYPERmotion: Learning Hybrid Behavior Planning for Autonomous Loco-manipulation mentions Model Predictive Control (MPC).'
  zh: HYPERmotion｜学习自主移动操作的混合行为规划提及模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据中提及现有系统使用模型预测控制（MPC），但并未说明HYPERmotion论文本身使用或基于MPC。
    | 证据: 然而，现有系统通常将任务规划与运动控制分离：高层规划依赖预定义规则或有限状态机，缺乏对动态场景的适应性；底层控制则多采用模型预测控制（MPC）或全身控制器（WBC），难以处理长时域、多约束的复杂任务。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_hypermotion_learning_hybrid_be_2024
  url: https://kg.rounds-tech.com/entry/ent_paper_hypermotion_learning_hybrid_be_2024/
  accessed_at: '2026-07-16'
---
