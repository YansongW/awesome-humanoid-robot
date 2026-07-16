---
$id: rel_ent_paper_visualmimic_visual_humanoid_lo_2025_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_visualmimic_visual_humanoid_lo_2025
  name:
    en: 'VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation'
    zh: VisualMimic｜通过运动跟踪和生成进行视觉人形移动操作
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation uses Model Predictive Control (MPC).'
  zh: VisualMimic｜通过运动跟踪和生成进行视觉人形移动操作使用模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文使用模型预测控制（MPC）生成高精度的动作序列。 | 证据: 第一阶段，教师策略在特权信息（如精确的物体位姿、关节力矩、未来轨迹）下进行训练，通过全身控制器（WBC）或模型预测控制（MPC）生成高精度的动作序列。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_visualmimic_visual_humanoid_lo_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_visualmimic_visual_humanoid_lo_2025/
  accessed_at: '2026-07-16'
---
