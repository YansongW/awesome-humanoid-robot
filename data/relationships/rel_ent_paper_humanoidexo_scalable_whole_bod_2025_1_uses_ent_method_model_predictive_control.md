---
$id: rel_ent_paper_humanoidexo_scalable_whole_bod_2025_1_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_humanoidexo_scalable_whole_bod_2025_1
  name:
    en: 'HumanoidExo: Scalable Whole-Body Humanoid Manipulation via Wearable Exoskeleton'
    zh: HumanoidExo｜通过可穿戴外骨骼进行可扩展的全身人形操作
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 09_data_datasets
  target_domain: 07_ai_models_algorithms
description:
  en: 'HumanoidExo: Scalable Whole-Body Humanoid Manipulation via Wearable Exoskeleton uses Model Predictive Control (MPC).'
  zh: HumanoidExo｜通过可穿戴外骨骼进行可扩展的全身人形操作使用模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文框架内嵌了模型预测控制（MPC）模块来确保动力学约束。 | 证据: 此外，框架内嵌了全身控制器（WBC）与模型预测控制（MPC）模块，确保生成的动作满足动力学约束与稳定性要求。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_humanoidexo_scalable_whole_bod_2025_1
  url: https://kg.rounds-tech.com/entry/ent_paper_humanoidexo_scalable_whole_bod_2025_1/
  accessed_at: '2026-07-16'
---
