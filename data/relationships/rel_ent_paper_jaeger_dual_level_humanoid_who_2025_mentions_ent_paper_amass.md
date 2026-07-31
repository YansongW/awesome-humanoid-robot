---
$id: rel_ent_paper_jaeger_dual_level_humanoid_who_2025_mentions_ent_paper_amass
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_jaeger_dual_level_humanoid_who_2025
  name:
    en: 'JAEGER: Dual-Level Humanoid Whole-Body Controller'
    zh: 'JAEGER: Dual-Level Humanoid Whole-Body Controller'
target:
  id: ent_paper_amass
  name:
    en: AMASS
    zh: AMASS
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'JAEGER: Dual-Level Humanoid Whole-Body Controller mentions AMASS.'
  zh: 'JAEGER: Dual-Level Humanoid Whole-Body Controller提及AMASS。'
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: 训练过程中，研究团队利用 AMASS 人体运动数据集，通过高效的重定向网络将人体姿态映射到人形机器人，并采用课程学习策略——先进行监督学习初始化，再通过强化学习进一步探索优化。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_jaeger_dual_level_humanoid_who_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_jaeger_dual_level_humanoid_who_2025/
  accessed_at: '2026-07-31'
---
