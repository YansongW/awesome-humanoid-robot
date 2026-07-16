---
$id: rel_ent_process_p15_mentions_ent_process_p16_1_1
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_process_p15
  name:
    en: Integration & V & V testing
    zh: 整机集成与验证测试（Integration & V&V）
target:
  id: ent_process_p16_1_1
  name:
    en: DFM/DFA review
    zh: DFM/DFA 评审
domains:
  source_domain: 04_assembly_integration_testing
  target_domain: 05_mass_production
description:
  en: Integration & V & V testing mentions DFM/DFA review.
  zh: 整机集成与验证测试（Integration & V&V）提及DFM/DFA 评审。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p4_wiki_ch13. Evidence: 在 Wiki 第 13 章同一小节共现'
sources:
- id: src_001
  type: other
  title: Wiki 第 13 章
  url: https://kg.rounds-tech.com/wiki/chapters/chapter-13/
  accessed_at: '2026-07-16'
---
