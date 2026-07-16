---
$id: rel_ent_paper_splitadapter_load_aware_humano_2026_mentions_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_splitadapter_load_aware_humano_2026
  name:
    en: 'SplitAdapter: Load-Aware Humanoid Loco-Manipulation via Factorized Adaptation'
    zh: SplitAdapter｜通过因子化适应进行负载感知的人形移动操作
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 06_design_engineering
  target_domain: 07_ai_models_algorithms
description:
  en: 'SplitAdapter: Load-Aware Humanoid Loco-Manipulation via Factorized Adaptation mentions Model Predictive Control (MPC).'
  zh: SplitAdapter｜通过因子化适应进行负载感知的人形移动操作提及模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据仅提到传统MPC难以适应负载变化，并未说明该论文直接使用或依赖MPC。 | 证据:
    人形机器人的移动操作（loco-manipulation）要求同时协调上肢操作与下肢运动，而负载变化会显著改变机器人的动力学特性，导致传统全身控制器（WBC）或模型预测控制（MPC）难以实时适应。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_splitadapter_load_aware_humano_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_splitadapter_load_aware_humano_2026/
  accessed_at: '2026-07-16'
---
