---
$id: rel_ent_paper_homie_humanoid_loco_manipulati_2025_1_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_homie_humanoid_loco_manipulati_2025_1
  name:
    en: 'HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit'
    zh: HOMIE｜具有同构外骨骼驾驶舱的人形移动操作
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 09_data_datasets
  target_domain: 07_ai_models_algorithms
description:
  en: 'HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit uses Model Predictive Control (MPC).'
  zh: HOMIE｜具有同构外骨骼驾驶舱的人形移动操作使用模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: HOMIE论文中明确提到全身控制层集成模型预测控制（MPC）以将参考轨迹转化为关节力矩指令。
    | 证据: 全身控制层则集成全身控制器（WBC）与模型预测控制（MPC），负责将高层策略输出的参考轨迹转化为底层关节力矩指令。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_homie_humanoid_loco_manipulati_2025_1
  url: https://kg.rounds-tech.com/entry/ent_paper_homie_humanoid_loco_manipulati_2025_1/
  accessed_at: '2026-07-16'
---
