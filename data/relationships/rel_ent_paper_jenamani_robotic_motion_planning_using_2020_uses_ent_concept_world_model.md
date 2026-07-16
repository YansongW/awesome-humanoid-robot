---
$id: rel_ent_paper_jenamani_robotic_motion_planning_using_2020_uses_ent_concept_world_model
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_jenamani_robotic_motion_planning_using_2020
  name:
    en: Robotic Motion Planning using Learned Critical Sources and Local Sampling
    zh: 基于学习临界源与局部采样的机器人运动规划
target:
  id: ent_concept_world_model
  name:
    en: World Model
    zh: 世界模型
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Robotic Motion Planning using Learned Critical Sources and Local Sampling uses World Model.
  zh: 基于学习临界源与局部采样的机器人运动规划使用世界模型。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 该论文使用条件变分自编码器（LEGO-Global）来学习关键源，这本质上是一种世界模型。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_jenamani_robotic_motion_planning_using_2020
  url: https://kg.rounds-tech.com/entry/ent_paper_jenamani_robotic_motion_planning_using_2020/
  accessed_at: '2026-07-16'
---
