---
$id: rel_ent_paper_huang_voxposer_composable_3d_value_m_2023_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_huang_voxposer_composable_3d_value_m_2023
  name:
    en: 'VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models'
    zh: VoxPoser
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models uses Model Predictive Control (MPC).'
  zh: VoxPoser使用模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 该论文采用模型预测控制（MPC）或类似方法进行规划，即使用了MPC方法。 | 证据: -
    **规划框架**：采用模型预测控制（MPC）或类似方法，在价值图上进行梯度下降或采样优化，生成平滑轨迹。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_huang_voxposer_composable_3d_value_m_2023
  url: https://kg.rounds-tech.com/entry/ent_paper_huang_voxposer_composable_3d_value_m_2023/
  accessed_at: '2026-07-31'
---
