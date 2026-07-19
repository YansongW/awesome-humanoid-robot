---
$id: rel_ent_software_humanoidverse_2024_uses_ent_software_mujoco_physics_engine_2022
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_software_humanoidverse_2024
  name:
    en: HumanoidVerse
    zh: HumanoidVerse
target:
  id: ent_software_mujoco_physics_engine_2022
  name:
    en: MuJoCo Physics Engine
    zh: MuJoCo 物理引擎
domains:
  source_domain: 08_software_middleware
  target_domain: 08_software_middleware
description:
  en: HumanoidVerse uses MuJoCo Physics Engine.
  zh: HumanoidVerse使用MuJoCo 物理引擎。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 可能使用MuJoCo作为底层物理引擎 [downgraded to low on 2026-07-17: hedged LLM evidence]'
sources:
- id: src_001
  type: other
  title: KG body of ent_software_humanoidverse_2024
  url: https://kg.rounds-tech.com/entry/ent_software_humanoidverse_2024/
  accessed_at: '2026-07-16'
---
