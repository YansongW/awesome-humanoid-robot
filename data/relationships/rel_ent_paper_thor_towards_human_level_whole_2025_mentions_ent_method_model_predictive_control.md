---
$id: rel_ent_paper_thor_towards_human_level_whole_2025_mentions_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_thor_towards_human_level_whole_2025
  name:
    en: 'Thor: Towards Human-Level Whole-Body Reactions for Intense Contact-Rich Environments'
    zh: Thor｜在强烈接触的环境中实现人类水平的全身反应
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 06_design_engineering
  target_domain: 07_ai_models_algorithms
description:
  en: 'Thor: Towards Human-Level Whole-Body Reactions for Intense Contact-Rich Environments mentions Model Predictive Control
    (MPC).'
  zh: Thor｜在强烈接触的环境中实现人类水平的全身反应提及模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据中仅将MPC作为现有方法之一进行讨论，并未表明源论文使用或基于MPC。 | 证据:
    现有方法主要依赖基于模型预测控制（MPC）的全身控制器或基于强化学习的策略训练，但二者均面临显著局限：MPC对接触动力学建模精度要求极高，难以处理非结构化接触；RL策略则容易陷入局部最优，且在多模态动作分布中缺乏有效的探索与采样机制。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_thor_towards_human_level_whole_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_thor_towards_human_level_whole_2025/
  accessed_at: '2026-07-16'
---
