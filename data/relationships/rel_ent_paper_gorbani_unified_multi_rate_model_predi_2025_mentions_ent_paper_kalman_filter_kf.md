---
$id: rel_ent_paper_gorbani_unified_multi_rate_model_predi_2025_mentions_ent_paper_kalman_filter_kf
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_gorbani_unified_multi_rate_model_predi_2025
  name:
    en: Unified Multi-Rate Model Predictive Control for a Jet-Powered Humanoid Robot
    zh: 喷气动力人形机器人的统一多速率模型预测控制
target:
  id: ent_paper_kalman_filter_kf
  name:
    en: Kalman Filter (KF)
    zh: 与 Extended Kalman Filter (EKF) 经典论文、教材与权威教程
domains:
  source_domain: 06_design_engineering
  target_domain: 07_ai_models_algorithms
description:
  en: Unified Multi-Rate Model Predictive Control for a Jet-Powered Humanoid Robot mentions Kalman Filter (KF).
  zh: 喷气动力人形机器人的统一多速率模型预测控制提及与 Extended Kalman Filter (EKF) 经典论文、教材与权威教程。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: - **复现核对点**：首先确认喷气动力学模型（式12）的h和g函数形式及EKF识别参数，这是MPC预测模型的核心；其次检查多速率约束实现——确保u_s,0在中间迭代被正确固定为上次计算值，否则会退化为单速率。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_gorbani_unified_multi_rate_model_predi_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_gorbani_unified_multi_rate_model_predi_2025/
  accessed_at: '2026-08-06'
---
