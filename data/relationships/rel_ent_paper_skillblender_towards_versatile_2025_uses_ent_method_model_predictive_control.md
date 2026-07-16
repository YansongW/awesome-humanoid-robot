---
$id: rel_ent_paper_skillblender_towards_versatile_2025_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_skillblender_towards_versatile_2025
  name:
    en: 'SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending'
    zh: SkillBlender｜通过技能混合实现多样化人形全身移动操作
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending uses Model Predictive Control
    (MPC).'
  zh: SkillBlender｜通过技能混合实现多样化人形全身移动操作使用模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明生成的轨迹由模型预测控制（MPC）进行底层执行，说明该论文使用了MPC。 | 证据:
    生成的轨迹进一步由全身控制器（WBC）或模型预测控制（MPC）进行底层执行，确保动作的平滑性与安全性。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_skillblender_towards_versatile_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_skillblender_towards_versatile_2025/
  accessed_at: '2026-07-16'
---
