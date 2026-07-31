---
$id: rel_ent_paper_chen_design_and_visual_servoing_con_2024_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_chen_design_and_visual_servoing_con_2024
  name:
    en: Design and Visual Servoing Control of MicroNeuro for Intraventricular Biopsy
    zh: 用于脑室内活检的混合双段柔性神经外科机器人 MicroNeuro 设计与视觉伺服控制
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: Design and Visual Servoing Control of MicroNeuro for Intraventricular Biopsy uses Model Predictive Control (MPC).
  zh: 用于脑室内活检的混合双段柔性神经外科机器人 MicroNeuro 设计与视觉伺服控制使用模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明该论文在控制过程中使用了约束MPC。 | 证据: - **约束模型预测控制（MPC）**：在控制过程中施加约束，增强柔性机器人对动态目标的跟踪能力，并有效抵抗外部干扰。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_chen_design_and_visual_servoing_con_2024
  url: https://kg.rounds-tech.com/entry/ent_paper_chen_design_and_visual_servoing_con_2024/
  accessed_at: '2026-07-31'
---
