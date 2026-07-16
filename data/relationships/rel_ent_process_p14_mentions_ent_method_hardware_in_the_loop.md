---
$id: rel_ent_process_p14_mentions_ent_method_hardware_in_the_loop
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_process_p14
  name:
    en: Software & Integration
    zh: 软件中间件与系统集成（Software & Integration）
target:
  id: ent_method_hardware_in_the_loop
  name:
    en: Hardware-in-the-Loop (HIL)
    zh: 硬件在环测试（HIL）
domains:
  source_domain: 08_software_middleware
  target_domain: 04_assembly_integration_testing
description:
  en: Software & Integration mentions Hardware-in-the-Loop (HIL).
  zh: 软件中间件与系统集成（Software & Integration）提及硬件在环测试（HIL）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: - **方法 / 工具**：GitLab CI、Docker、SIL/HIL 自动化测试、代码覆盖率'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p14
  url: https://kg.rounds-tech.com/entry/ent_process_p14/
  accessed_at: '2026-07-16'
---
