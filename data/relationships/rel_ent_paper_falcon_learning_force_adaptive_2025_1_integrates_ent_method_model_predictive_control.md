---
$id: rel_ent_paper_falcon_learning_force_adaptive_2025_1_integrates_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: integrates
source:
  id: ent_paper_falcon_learning_force_adaptive_2025_1
  name:
    en: 'FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation'
    zh: FALCON｜学习力自适应人形移动操作
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation integrates Model Predictive Control (MPC).'
  zh: FALCON｜学习力自适应人形移动操作integrates模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: FALCON将全身控制器（WBC）与模型预测控制（MPC）纳入同一可训练、可复用的架构。
    | 证据: 该研究通过整合本体状态、关节序列、人类视频与动捕轨迹、遥操作及外骨骼数据，构建了一套端到端的训练与部署链路，其核心贡献在于将全身控制器（WBC）与模型预测控制（MPC）纳入同一可训练、可复用的架构，从而显著降低高层任务规划与低层关节控制之间的语义与执行断点。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_falcon_learning_force_adaptive_2025_1
  url: https://kg.rounds-tech.com/entry/ent_paper_falcon_learning_force_adaptive_2025_1/
  accessed_at: '2026-07-16'
---
