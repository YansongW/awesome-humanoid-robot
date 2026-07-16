---
$id: rel_ent_paper_design_and_control_of_a_bipeda_2024_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_design_and_control_of_a_bipeda_2024
  name:
    en: Design and Control of a Bipedal Robotic Character
    zh: Design and Control of a Bipedal Robotic Character
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 06_design_engineering
  target_domain: 07_ai_models_algorithms
description:
  en: Design and Control of a Bipedal Robotic Character uses Model Predictive Control (MPC).
  zh: Design and Control of a Bipedal Robotic Character使用模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据明确说明上层通过MPC算法实现全身运动规划与平衡调节。 | 证据: 控制层面则采用了分层式架构，底层负责关节级力矩与位置控制，上层则通过模型预测控制（MPC）算法实现全身运动规划与平衡调节。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_design_and_control_of_a_bipeda_2024
  url: https://kg.rounds-tech.com/entry/ent_paper_design_and_control_of_a_bipeda_2024/
  accessed_at: '2026-07-16'
---
