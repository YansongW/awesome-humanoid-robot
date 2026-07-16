---
$id: rel_ent_concept_demo_to_product_gap_mentions_ent_robot_system_tesla_optimus
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_concept_demo_to_product_gap
  name:
    en: Demo-to-Product Gap
    zh: 演示指标与产品指标的鸿沟
target:
  id: ent_robot_system_tesla_optimus
  name:
    en: Tesla Optimus
    zh: Tesla Optimus
domains:
  source_domain: 11_applications_markets
  target_domain: 05_mass_production
description:
  en: Demo-to-Product Gap mentions Tesla Optimus.
  zh: 演示指标与产品指标的鸿沟提及Tesla Optimus。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据中提到了Tesla Optimus，但只是作为例子列出，没有明确的关系方向。 | 证据:
    - **Tesla Optimus**：2026 年 1 月 21 日，Gen 3 在弗里蒙特工厂启动量产；Model S/X 产线被改造为 Optimus 生产线，目标年产能 100 万台；得州 Gigafactory 在建专用工厂，目标年产能
    1000 万台。'
sources:
- id: src_001
  type: other
  title: KG body of ent_concept_demo_to_product_gap
  url: https://kg.rounds-tech.com/entry/ent_concept_demo_to_product_gap/
  accessed_at: '2026-07-16'
---
