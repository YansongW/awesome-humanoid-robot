---
$id: rel_ent_paper_twist2_scalable_portable_and_h_2025_2_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_twist2_scalable_portable_and_h_2025_2
  name:
    en: 'TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System'
    zh: TWIST2｜可扩展、便携式、整体的人形数据收集系统
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: 'TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System uses Model Predictive Control (MPC).'
  zh: TWIST2｜可扩展、便携式、整体的人形数据收集系统使用模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: TWIST2系统通过模型预测控制（MPC）将学习到的动作映射到低层控制。 | 证据: TWIST2
    的核心框架分为三个层次：首先，系统将来自相机、动捕设备、遥操作手柄及外骨骼的多模态数据统一编码为结构化表征，确保不同来源的信息在特征空间中对齐；其次，利用 ACT（Action Chunking with Transformers）与行为克隆模仿学习，从人类演示数据中提取动作先验，同时引入
    VLA（Vision-Language-Action）多模态动作模型，将视觉语言理解与机器人状态（如关节角度、力矩）融合；最后，通过全身控制器（WBC）与模型预测控制（MPC）将学习到的动作映射'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_twist2_scalable_portable_and_h_2025_2
  url: https://kg.rounds-tech.com/entry/ent_paper_twist2_scalable_portable_and_h_2025_2/
  accessed_at: '2026-07-16'
---
