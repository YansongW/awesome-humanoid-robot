---
$id: rel_ent_paper_agile_a_comprehensive_workflow_2026_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_agile_a_comprehensive_workflow_2026
  name:
    en: 'AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning'
    zh: AGILE｜人形移动操作学习的综合工作流程
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning uses Model Predictive Control (MPC).'
  zh: AGILE｜人形移动操作学习的综合工作流程使用模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 该论文结合模型预测控制（MPC）生成平滑且稳定的关节目标。 | 证据: 随后，利用 PPO
    等强化学习算法训练低层控制器，并结合全身控制器（WBC）与模型预测控制（MPC）生成平滑且稳定的关节目标。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_agile_a_comprehensive_workflow_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_agile_a_comprehensive_workflow_2026/
  accessed_at: '2026-07-16'
---
