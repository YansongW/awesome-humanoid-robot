---
$id: rel_ent_paper_wang_wam_survey_2026_mentions_ent_paper_cen_worldvla_towards_autoregressiv_2025
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_wang_wam_survey_2026
  name:
    en: 'World Action Models: The Next Frontier in Embodied AI'
    zh: 世界动作模型：具身智能的下一个前沿
target:
  id: ent_paper_cen_worldvla_towards_autoregressiv_2025
  name:
    en: 'WorldVLA: Towards Autoregressive Action World Model'
    zh: WorldVLA
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'World Action Models: The Next Frontier in Embodied AI mentions WorldVLA: Towards Autoregressive Action World Model.'
  zh: 世界动作模型：具身智能的下一个前沿提及WorldVLA。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据中列举了WorldVLA的模态特定因果掩码作为自回归方法的一个例子，但没有明确说明源论文使用或基于WorldVLA。
    | 证据: - **Autoregressive**：GR-1/GR-2的显式解耦表示、CoT-VLA的混合注意力路由、WorldVLA的模态特定因果掩码'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_wang_wam_survey_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_wang_wam_survey_2026/
  accessed_at: '2026-08-06'
---
