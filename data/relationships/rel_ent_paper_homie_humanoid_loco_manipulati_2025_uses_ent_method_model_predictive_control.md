---
$id: rel_ent_paper_homie_humanoid_loco_manipulati_2025_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_homie_humanoid_loco_manipulati_2025
  name:
    en: 'HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit'
    zh: HOMIE｜具有同构外骨骼驾驶舱的人形移动操作
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 06_design_engineering
  target_domain: 07_ai_models_algorithms
description:
  en: 'HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit uses Model Predictive Control (MPC).'
  zh: HOMIE｜具有同构外骨骼驾驶舱的人形移动操作使用模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: HOMIE论文中明确提到将模型预测控制（MPC）嵌入训练部署链路。 | 证据: 关键创新在于将全身控制器（WBC）与模型预测控制（MPC）嵌入同一训练部署链路，使得高层策略（如导航目标）可直接转化为低层控制器目标，消除了传统架构中策略与控制器的接口断层。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_homie_humanoid_loco_manipulati_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_homie_humanoid_loco_manipulati_2025/
  accessed_at: '2026-07-16'
---
