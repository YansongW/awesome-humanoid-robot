---
$id: rel_ent_component_planetary_roller_screw_is_part_of_ent_robot_system_tesla_optimus
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_component_planetary_roller_screw
  name:
    en: Planetary Roller Screw
    zh: 行星滚柱丝杠
target:
  id: ent_robot_system_tesla_optimus
  name:
    en: Tesla Optimus
    zh: Tesla Optimus
domains:
  source_domain: 02_components
  target_domain: 05_mass_production
description:
  en: Planetary Roller Screw is part of Tesla Optimus.
  zh: 行星滚柱丝杠is_part_ofTesla Optimus。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据指出特斯拉Optimus的线性关节使用行星滚柱丝杠，表明该丝杠是Optimus的一部分。
    | 证据: - **Tesla Optimus**：据 Tesla AI Day 2022 与后续公开信息，Optimus 躯干采用 28 个执行器（14 个旋转 + 14 个线性），旋转关节使用无框力矩电机 + 谐波减速器，线性关节使用无框力矩电机
    + 行星滚柱丝杠；灵巧手从 Gen 2 的 11 DoF 升级到 Gen 3 的 22 DoF，采用腱驱动与微型执行器[14]。'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_planetary_roller_screw
  url: https://kg.rounds-tech.com/entry/ent_component_planetary_roller_screw/
  accessed_at: '2026-07-16'
---
