---
$id: rel_ent_paper__2025_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper__2025
  name:
    en: Humanoid Robot Motion and Operation｜Progress and Challenges in Control Planning and Learning
    zh: 人形机器人运动与操作｜控制规划和学习的进展与挑战
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Humanoid Robot Motion and Operation｜Progress and Challenges in Control Planning and Learning uses Model Predictive Control
    (MPC).
  zh: 人形机器人运动与操作｜控制规划和学习的进展与挑战使用模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文中描述全身控制器与模型预测控制被用于底层轨迹优化。 | 证据: 其中，全身控制器（WBC）与模型预测控制（MPC）被用于底层轨迹优化，确保生成动作满足动力学约束与稳定性要求。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper__2025
  url: https://kg.rounds-tech.com/entry/ent_paper__2025/
  accessed_at: '2026-07-16'
---
