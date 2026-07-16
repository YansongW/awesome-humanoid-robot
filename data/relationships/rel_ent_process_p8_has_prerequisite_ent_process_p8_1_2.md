---
$id: rel_ent_process_p8_has_prerequisite_ent_process_p8_1_2
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_process_p8
  name:
    en: Structural FEA and iteration
    zh: 结构强度仿真与迭代（Structural FEA）
target:
  id: ent_process_p8_1_2
  name:
    en: FEA model preparation
    zh: FEA 模型准备
domains:
  source_domain: 06_design_engineering
  target_domain: 06_design_engineering
description:
  en: Structural FEA and iteration has prerequisite FEA model preparation.
  zh: 结构强度仿真与迭代（Structural FEA）前置依赖FEA 模型准备。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 结构FEA与迭代需要FEA模型准备作为上游输入 | 证据: 1 输入梳理与目标量化**：整理「FEA
    模型准备」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p8
  url: https://kg.rounds-tech.com/entry/ent_process_p8/
  accessed_at: '2026-07-16'
---
