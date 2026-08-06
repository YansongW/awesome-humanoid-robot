---
$id: rel_ent_paper_immersive_social_interaction_vr_llm_assi_2026_uses_ent_software_pinocchio
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_immersive_social_interaction_vr_llm_assi_2026
  name:
    en: Immersive Social Interaction with VR and LLM-Assisted Humanoids
    zh: Immersive Social Interaction with VR and LLM-Assisted Humanoids
target:
  id: ent_software_pinocchio
  name:
    en: Pinocchio
    zh: Pinocchio
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 08_software_middleware
description:
  en: Immersive Social Interaction with VR and LLM-Assisted Humanoids uses Pinocchio.
  zh: Immersive Social Interaction with VR and LLM-Assisted Humanoids使用Pinocchio。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 系统使用Pinocchio进行逆运动学求解。 | 证据: - **重定向与重映射**：人类手腕位姿转换至机器人坐标系，经
    Pinocchio 逆运动学求解关节角度，由 PD 控制器驱动执行。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_immersive_social_interaction_vr_llm_assi_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_immersive_social_interaction_vr_llm_assi_2026/
  accessed_at: '2026-08-06'
---
