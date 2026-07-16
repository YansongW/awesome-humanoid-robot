---
$id: rel_ent_paper_adversarial_locomotion_and_mot_2025_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_adversarial_locomotion_and_mot_2025
  name:
    en: Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning
    zh: 用于人形策略学习的对抗性运动和运动模仿
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 06_design_engineering
  target_domain: 07_ai_models_algorithms
description:
  en: Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning uses Model Predictive Control (MPC).
  zh: 用于人形策略学习的对抗性运动和运动模仿使用模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文中描述通过全身控制器与模型预测控制实现高层规划与底层执行的衔接。 | 证据: 这一过程通过全身控制器（WBC）与模型预测控制（MPC）实现高层规划与底层执行的衔接，从而打破数据采集与策略学习之间的壁垒。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_adversarial_locomotion_and_mot_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_adversarial_locomotion_and_mot_2025/
  accessed_at: '2026-07-16'
---
