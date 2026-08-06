---
$id: rel_ent_paper_palm_e_embodied_multimodal_language_mode_2023_uses_ent_paper_lynch_interactive_language_talking_t_2022
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_palm_e_embodied_multimodal_language_mode_2023
  name:
    en: 'PaLM-E: An Embodied Multimodal Language Model'
    zh: 'PaLM-E: An Embodied Multimodal Language Model'
target:
  id: ent_paper_lynch_interactive_language_talking_t_2022
  name:
    en: 'Interactive Language: Talking to Robots in Real Time'
    zh: Interactive Language
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'PaLM-E: An Embodied Multimodal Language Model uses Interactive Language: Talking to Robots in Real Time.'
  zh: 'PaLM-E: An Embodied Multimodal Language Model使用Interactive Language。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: PaLM-E使用Interactive Language作为低层策略来执行动作。 | 证据:
    - 推理循环：PaLM-E 以 1 Hz 输出语言子目标，低层策略（RT-1 或 Interactive Language）以 5 Hz 执行动作；每 40 步（10 Hz 持续 4 秒）请求新指令。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_palm_e_embodied_multimodal_language_mode_2023
  url: https://kg.rounds-tech.com/entry/ent_paper_palm_e_embodied_multimodal_language_mode_2023/
  accessed_at: '2026-08-06'
---
