---
$id: rel_ent_paper_textop_real_time_interactive_t_2026_1_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_textop_real_time_interactive_t_2026_1
  name:
    en: 'TextOp: Real-time Interactive Text-Driven Humanoid Robot Motion Generation and Control'
    zh: TextOp｜实时交互式文本驱动的仿人机器人运动生成和控制
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'TextOp: Real-time Interactive Text-Driven Humanoid Robot Motion Generation and Control uses Model Predictive Control
    (MPC).'
  zh: TextOp｜实时交互式文本驱动的仿人机器人运动生成和控制使用模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 源论文TextOp提到其生成的轨迹由模型预测控制（MPC）进行底层跟踪与稳定控制。 |
    证据: 模型以语言指令为条件，在动作分布中采样出全身关节轨迹，随后由全身控制器（WBC）或模型预测控制（MPC）进行底层跟踪与稳定控制。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_textop_real_time_interactive_t_2026_1
  url: https://kg.rounds-tech.com/entry/ent_paper_textop_real_time_interactive_t_2026_1/
  accessed_at: '2026-07-16'
---
