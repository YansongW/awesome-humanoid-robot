---
$id: rel_ent_process_p13_mentions_ent_method_fmea
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_process_p13
  name:
    en: Electronics & Power Systems
    zh: 电子电气与能源系统（Electronics & Power）
target:
  id: ent_method_fmea
  name:
    en: Failure Mode and Effects Analysis (FMEA)
    zh: 失效模式与影响分析（FMEA）
domains:
  source_domain: 02_components
  target_domain: 05_mass_production
description:
  en: Electronics & Power Systems mentions Failure Mode and Effects Analysis (FMEA).
  zh: 电子电气与能源系统（Electronics & Power）提及失效模式与影响分析（FMEA）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: - **完成标准 / 输出物**：安全系统原理图、FMEA、急停响应时间 < 目标'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p13
  url: https://kg.rounds-tech.com/entry/ent_process_p13/
  accessed_at: '2026-07-16'
---
