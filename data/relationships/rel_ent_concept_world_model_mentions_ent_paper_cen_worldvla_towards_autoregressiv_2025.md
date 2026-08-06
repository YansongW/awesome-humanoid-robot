---
$id: rel_ent_concept_world_model_mentions_ent_paper_cen_worldvla_towards_autoregressiv_2025
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_concept_world_model
  name:
    en: World Model
    zh: 世界模型
target:
  id: ent_paper_cen_worldvla_towards_autoregressiv_2025
  name:
    en: 'WorldVLA: Towards Autoregressive Action World Model'
    zh: WorldVLA
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'World Model mentions WorldVLA: Towards Autoregressive Action World Model.'
  zh: 世界模型提及WorldVLA。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据中提到了WorldVLA论文，但未明确说明世界模型概念与论文之间的具体关系，仅作为相关方向被提及。
    | 证据: - **机器人专用方向**：WorldVLA（`ent_paper_cen_worldvla_towards_autoregressiv_2025`）把世界模型与动作模型统一到自回归框架；WMPO、DREAMSTEER、DynaWM
    等探索 VLA + 世界模型的耦合训练（来源：项目 Wiki 第 20 章；图谱关联论文）；'
sources:
- id: src_001
  type: other
  title: KG body of ent_concept_world_model
  url: https://kg.rounds-tech.com/entry/ent_concept_world_model/
  accessed_at: '2026-08-06'
---
