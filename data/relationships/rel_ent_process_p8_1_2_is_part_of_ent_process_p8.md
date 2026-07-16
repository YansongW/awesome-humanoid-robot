---
$id: rel_ent_process_p8_1_2_is_part_of_ent_process_p8
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_process_p8_1_2
  name:
    en: FEA model preparation
    zh: FEA 模型准备
target:
  id: ent_process_p8
  name:
    en: Structural FEA and iteration
    zh: 结构强度仿真与迭代（Structural FEA）
domains:
  source_domain: 06_design_engineering
  target_domain: 06_design_engineering
description:
  en: FEA model preparation is part of Structural FEA and iteration.
  zh: FEA 模型准备is_part_of结构强度仿真与迭代（Structural FEA）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明有限元模型准备属于结构强度仿真与迭代阶段。 | 证据: **所属阶段/工作包**：结构强度仿真与迭代（Structural
    FEA）'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p8_1_2
  url: https://kg.rounds-tech.com/entry/ent_process_p8_1_2/
  accessed_at: '2026-07-16'
---
