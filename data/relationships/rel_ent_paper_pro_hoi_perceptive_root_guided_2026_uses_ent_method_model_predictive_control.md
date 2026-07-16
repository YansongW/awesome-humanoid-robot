---
$id: rel_ent_paper_pro_hoi_perceptive_root_guided_2026_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_pro_hoi_perceptive_root_guided_2026
  name:
    en: 'Pro-HOI: Perceptive Root-guided Humanoid-Object Interaction'
    zh: Pro-HOI｜感知根引导的人形物体交互
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'Pro-HOI: Perceptive Root-guided Humanoid-Object Interaction uses Model Predictive Control (MPC).'
  zh: Pro-HOI｜感知根引导的人形物体交互使用模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: Pro-HOI底层采用模型预测控制（MPC）来保证运动学与动力学可行性。 | 证据: 底层采用全身控制器（WBC）或模型预测控制（MPC）保证运动学与动力学可行性，上层则通过逆运动学（IK）与动作重定向模块将采样轨迹映射至具体执行空间。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_pro_hoi_perceptive_root_guided_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_pro_hoi_perceptive_root_guided_2026/
  accessed_at: '2026-07-16'
---
