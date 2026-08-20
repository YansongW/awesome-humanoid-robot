---
$id: rel_ent_paper_open_television_teleoperation_2024_uses_ent_method_action_chunking_transformer
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_open_television_teleoperation_2024
  name:
    en: 'Open-TeleVision: Teleoperation with Immersive Active Visual Feedback'
    zh: Open-TeleVision｜具有沉浸式主动视觉反馈的远程操作
target:
  id: ent_method_action_chunking_transformer
  name:
    en: Action Chunking with Transformers (ACT)
    zh: 动作分块变压器（ACT）
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: 'Open-TeleVision: Teleoperation with Immersive Active Visual Feedback uses Action Chunking with Transformers.'
  zh: 学习人对人的实时全身远程操作。使用基于Transformer的动作分块。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: Open-TeleVision论文使用ACT（Action Chunking with
    Transformers）进行表示学习。 | 证据: 表示学习层采用 ACT（Action Chunking with Transformers）与行为克隆方法，将原始观测映射到潜在动作空间。 | WP3 2026-08-06: endpoint
    rewritten (ent_paper_open_television_teleoperation_2024→ent_paper_open_television_teleoperation_2024, ent_method_action_chunking_transformer→ent_method_action_chunking_transformer)
    after merge. Original file rel_ent_paper_open_television_teleoperation_2024_2_uses_ent_paper_action_chunking_with_transform_2023.
    | WP4 2026-08-11: endpoint id rewritten (ent_paper_open_television_teleoperation_2024→ent_paper_open_television_teleoperation_2024,
    ent_method_action_chunking_transformer→ent_method_action_chunking_transformer); original file rel_ent_paper_open_television_teleoperation_2024_uses_ent_paper_action_chunking_with_transform_2023.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_open_television_teleoperation_2024
  url: https://kg.rounds-tech.com/entry/ent_paper_open_television_teleoperation_2024/
  accessed_at: '2026-07-16'
---
