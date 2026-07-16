---
$id: rel_ent_process_p1_1_3_mentions_ent_standard_iec_61508
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_process_p1_1_3
  name:
    en: Mapping of regulations, standards and safety requirements
    zh: 法规、标准与安全需求映射
target:
  id: ent_standard_iec_61508
  name:
    en: IEC 61508
    zh: IEC 61508
domains:
  source_domain: 06_design_engineering
  target_domain: 12_policy_regulation_ethics
description:
  en: Mapping of regulations, standards and safety requirements mentions IEC 61508.
  zh: 法规、标准与安全需求映射提及IEC 61508。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据中仅列出多个标准，没有明确说明源方法使用了目标标准。 | 证据: **方法 / 工具**：ISO
    10218-1/2、ISO/TS 15066、IEC 61508、IEC 62368、CE/FCC/UL 差距分析'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p1_1_3
  url: https://kg.rounds-tech.com/entry/ent_process_p1_1_3/
  accessed_at: '2026-07-16'
---
