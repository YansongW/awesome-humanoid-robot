---
$id: rel_ent_paper_cwi_composite_humanoid_whole_body_imitat_2026_mentions_ent_paper_amass
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_cwi_composite_humanoid_whole_body_imitat_2026
  name:
    en: 'CWI: Composite Humanoid Whole-Body Imitation System for Loco-manipulation'
    zh: 'CWI: Composite Humanoid Whole-Body Imitation System for Loco-manipulation'
target:
  id: ent_paper_amass
  name:
    en: AMASS
    zh: AMASS
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'CWI: Composite Humanoid Whole-Body Imitation System for Loco-manipulation mentions AMASS.'
  zh: 'CWI: Composite Humanoid Whole-Body Imitation System for Loco-manipulation提及AMASS。'
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: 其核心贡献在于将上半身与下半身的运动数据来源和奖励角色彻底解耦：上半身直接使用完整未过滤的
    AMASS 动作捕捉语料库，下半身则仅用少量精选行走/蹲起片段配合对抗运动先验（AMP）约束，最终通过教师-学生蒸馏得到可由双手姿态和速度/高度指令控制的便携式全身策略。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_cwi_composite_humanoid_whole_body_imitat_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_cwi_composite_humanoid_whole_body_imitat_2026/
  accessed_at: '2026-08-06'
---
