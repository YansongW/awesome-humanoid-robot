---
$id: rel_ent_paper_hand_eye_autonomous_delivery_l_2025_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_hand_eye_autonomous_delivery_l_2025
  name:
    en: 'Hand-Eye Autonomous Delivery: Learning Humanoid Navigation, Locomotion and Reaching'
    zh: 手眼自主配送｜学习人形机器人导航运动和伸手
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'Hand-Eye Autonomous Delivery: Learning Humanoid Navigation, Locomotion and Reaching uses Model Predictive Control (MPC).'
  zh: 手眼自主配送｜学习人形机器人导航运动和伸手使用模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文采用模型预测控制生成低层控制目标 | 证据: 最后，采用全身控制器（WBC）与模型预测控制（MPC）生成低层控制目标，包括导航目标与到达目标，从而将高层任务指令转化为可执行的关节运动序列。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_hand_eye_autonomous_delivery_l_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_hand_eye_autonomous_delivery_l_2025/
  accessed_at: '2026-07-16'
---
