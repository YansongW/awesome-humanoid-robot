---
$id: rel_ent_paper_pi0_2024_mentions_ent_paper_openvla_2024_1
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_pi0_2024
  name:
    en: 'π0: A Vision-Language-Action Flow Model for General Robot Control'
    zh: π0：用于通用机器人控制的视觉-语言-动作流模型
target:
  id: ent_paper_openvla_2024_1
  name:
    en: OpenVLA
    zh: OpenVLA
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'π0: A Vision-Language-Action Flow Model for General Robot Control mentions OpenVLA.'
  zh: π0：用于通用机器人控制的视觉-语言-动作流模型提及OpenVLA。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: 该模型在 33 亿参数的 PaliGemma VLM 骨干之上新增 3 亿参数的动作专家（Action
    Expert），使用条件流匹配建模连续动作分布，在 10,000+ 小时、7 种机器人配置、68 个任务的混合数据上预训练，并在零样本灵巧操作、语言条件任务和多阶段复杂任务上显著超越 OpenVLA、Octo 等基线。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_pi0_2024
  url: https://kg.rounds-tech.com/entry/ent_paper_pi0_2024/
  accessed_at: '2026-08-06'
---
