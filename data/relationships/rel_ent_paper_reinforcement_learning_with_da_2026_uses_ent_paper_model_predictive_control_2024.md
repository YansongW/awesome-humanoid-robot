---
$id: rel_ent_paper_reinforcement_learning_with_da_2026_uses_ent_paper_model_predictive_control_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_reinforcement_learning_with_da_2026
  name:
    en: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation
    zh: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation
target:
  id: ent_paper_model_predictive_control_2024
  name:
    en: Model Predictive Control
    zh: 模型预测控制
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation uses Model Predictive
    Control.
  zh: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation使用模型预测控制。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文使用基于MPC的低层规划器来生成稳健的行走步态。 | 证据: Our method
    comprises a high-level reinforcement learning (RL) planner for subgoal selection in a robot-centric coordinate system
    and a low-level Model Predictive Control (MPC) based planner which produces robust walking gaits to reach these subgoals.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_reinforcement_learning_with_da_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_reinforcement_learning_with_da_2026/
  accessed_at: '2026-07-16'
---
