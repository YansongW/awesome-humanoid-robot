---
$id: rel_ent_paper_bill_of_materials_2024_is_part_of_ent_robot_system_tesla_optimus
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_paper_bill_of_materials_2024
  name:
    en: Bill of Materials
    zh: 物料清单
    ko: Bill of Materials
target:
  id: ent_robot_system_tesla_optimus
  name:
    en: Tesla Optimus
    zh: Tesla Optimus
    ko: 테슬라 옵티머스
domains:
  source:
  - 03_manufacturing_processes
  - 06_design_engineering
  target:
  - 05_mass_production
  - 06_design_engineering
  - 11_applications_markets
description:
  en: BOM structures all parts and subassemblies of Tesla Optimus.
  zh: BOM结构化Tesla Optimus的所有零件和子装配件。
  ko: BOM은 Tesla Optimus의 모든 부품 및 하위 조립품을 구조화합니다.
verification:
  confidence: medium
  notes: bulk-added confidence on 2026-07-17 by backfill_rel_confidence.py; pending human review
  status: partially_verified
  sources: []
  reviewed_by: ai_autonomous
  reviewed_at: '2026-07-02T00:21:22.207515+00:00'
sources:
- type: website
  url: ''
  description: Workflow relationship curated from public project pages and literature.
  id: curated_workflow_relationship
---





