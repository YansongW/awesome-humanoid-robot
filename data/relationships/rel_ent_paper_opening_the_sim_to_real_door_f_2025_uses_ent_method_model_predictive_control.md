---
$id: rel_ent_paper_opening_the_sim_to_real_door_f_2025_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_opening_the_sim_to_real_door_f_2025
  name:
    en: Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer
    zh: 打开仿真到现实世界的人形像素到动作策略传输之门
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 06_design_engineering
  target_domain: 07_ai_models_algorithms
description:
  en: Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer uses Model Predictive Control (MPC).
  zh: 打开仿真到现实世界的人形像素到动作策略传输之门使用模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 该论文将模型预测控制（MPC）的输出编码为可训练的轨迹序列。 | 证据: 关键技术创新的核心在于两点：其一，设计了一种可复用的全身轨迹表示方法，将遥操作/外骨骼数据、全身控制器（WBC）与模型预测控制（MPC）的输出统一编码为可训练的轨迹序列，并引入闭环纠错机制与人类干预信号，确保数据质量与策略安全性；其二，提出了一种分层蒸馏策略，不仅迁移动作输出，还隐式传递了教师策略对多模态观测的融合能力与对动态环境的适应策略，从而显著降低学生策略在真实部署中的域漂移风险。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_opening_the_sim_to_real_door_f_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_opening_the_sim_to_real_door_f_2025/
  accessed_at: '2026-07-16'
---
