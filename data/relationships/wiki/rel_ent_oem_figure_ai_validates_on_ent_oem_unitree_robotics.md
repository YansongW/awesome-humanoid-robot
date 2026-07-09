---
$id: rel_ent_oem_figure_ai_validates_on_ent_oem_unitree_robotics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: validates_on
source:
  id: ent_oem_figure_ai
  name:
    zh: Figure AI
    en: Figure AI
    ko: 피규어 AI
target:
  id: ent_oem_unitree_robotics
  name:
    zh: 宇树科技
    en: Unitree Robotics
    ko: 유닛리 로보틱스
domains:
  source_domain: 06_design_engineering
  target_domain: 02_components
description:
  zh: Wiki 章节文本提取的跨层关系。
  en: Cross-layer link extracted from Wiki chapter text.
  ko: ''
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-09'
  confidence: low
  notes: Heuristic extraction from Wiki; pending human review.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---

Figure AI **validates_on** 宇树科技。

该关系来自 Wiki 章节的文本提取。
