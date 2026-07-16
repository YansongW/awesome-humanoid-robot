---
$id: rel_ent_paper_humanoidexo_scalable_whole_bod_2025_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_humanoidexo_scalable_whole_bod_2025
  name:
    en: 'HumanoidExo: Scalable Whole-Body Humanoid Manipulation via Wearable Exoskeleton'
    zh: HumanoidExo｜通过可穿戴外骨骼进行可扩展的全身人形操作
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'HumanoidExo: Scalable Whole-Body Humanoid Manipulation via Wearable Exoskeleton uses Model Predictive Control (MPC).'
  zh: HumanoidExo｜通过可穿戴外骨骼进行可扩展的全身人形操作使用模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文底层采用模型预测控制（MPC）来确保物理可行性。 | 证据: 底层采用全身控制器（WBC）或模型预测控制（MPC）确保运动学与动力学的物理可行性；上层则通过扩散策略或流匹配网络，将采集到的人类操作数据转化为条件化的动作生成模型。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_humanoidexo_scalable_whole_bod_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_humanoidexo_scalable_whole_bod_2025/
  accessed_at: '2026-07-16'
---
