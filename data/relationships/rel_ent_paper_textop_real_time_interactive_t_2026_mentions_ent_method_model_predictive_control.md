---
$id: rel_ent_paper_textop_real_time_interactive_t_2026_mentions_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_textop_real_time_interactive_t_2026
  name:
    en: 'TextOp: Real-time Interactive Text-Driven Humanoid Robot Motion Generation and Control'
    zh: TextOp｜实时交互式文本驱动的仿人机器人运动生成和控制
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 06_design_engineering
  target_domain: 07_ai_models_algorithms
description:
  en: 'TextOp: Real-time Interactive Text-Driven Humanoid Robot Motion Generation and Control mentions Model Predictive Control
    (MPC).'
  zh: TextOp｜实时交互式文本驱动的仿人机器人运动生成和控制提及模型预测控制（MPC）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: 在数据采集层，通过遥操作或外骨骼设备同步记录人类操作指令与机器人状态数据；运动生成层采用扩散策略或流匹配模型，将语言指令作为条件信号，在由人类示范数据构建的多模态动作分布中采样出连续的全身轨迹；控制执行层则通过全身控制器（WBC）或模型预测控制器（MPC）将生成的轨迹转化为低层控制目标，驱动机器人关节电机实现稳定运动。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_textop_real_time_interactive_t_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_textop_real_time_interactive_t_2026/
  accessed_at: '2026-07-16'
---
