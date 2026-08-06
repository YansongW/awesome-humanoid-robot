---
$id: rel_ent_paper_gigaworld_0_world_models_data_engine_2025_uses_ent_tech_mimicgen
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_gigaworld_0_world_models_data_engine_2025
  name:
    en: 'GigaWorld-0: World Models as Data Engine to Empower Embodied AI'
    zh: 'GigaWorld-0: World Models as Data Engine to Empower Embodied AI'
target:
  id: ent_tech_mimicgen
  name:
    en: MimicGen
    zh: MimicGen
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 08_software_middleware
description:
  en: 'GigaWorld-0: World Models as Data Engine to Empower Embodied AI uses MimicGen.'
  zh: 'GigaWorld-0: World Models as Data Engine to Empower Embodied AI使用MimicGen。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文使用MimicGen框架来扩展种子轨迹。 | 证据: - **动作生成（Act）**：两层级管线，使用
    MimicGen 框架将种子轨迹扩展到新物体姿态和场景布局，复杂场景则用遥操作演示作为强化学习冷启动数据。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_gigaworld_0_world_models_data_engine_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_gigaworld_0_world_models_data_engine_2025/
  accessed_at: '2026-08-06'
---
