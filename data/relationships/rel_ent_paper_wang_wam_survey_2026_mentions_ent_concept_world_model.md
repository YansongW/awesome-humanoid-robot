---
$id: rel_ent_paper_wang_wam_survey_2026_mentions_ent_concept_world_model
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_wang_wam_survey_2026
  name:
    en: 'World Action Models: The Next Frontier in Embodied AI'
    zh: 世界动作模型：具身智能的下一个前沿
target:
  id: ent_concept_world_model
  name:
    en: World Model
    zh: 世界模型
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'World Action Models: The Next Frontier in Embodied AI mentions World Model.'
  zh: 世界动作模型：具身智能的下一个前沿提及世界模型。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文通过区分WAM与邻近概念来厘清术语混淆，提及了World Model，但没有明确表示使用或基于它。
    | 证据: 更重要的是，作者通过区分WAM与Video Action Models（VAMs）、Video Policies、Action World Models（AWMs）等邻近概念，厘清了长期存在的术语混淆。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_wang_wam_survey_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_wang_wam_survey_2026/
  accessed_at: '2026-08-06'
---
