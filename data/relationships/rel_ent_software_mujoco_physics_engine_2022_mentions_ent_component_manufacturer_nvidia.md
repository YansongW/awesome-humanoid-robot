---
$id: rel_ent_software_mujoco_physics_engine_2022_mentions_ent_component_manufacturer_nvidia
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_software_mujoco_physics_engine_2022
  name:
    en: MuJoCo Physics Engine
    zh: MuJoCo 物理引擎
target:
  id: ent_component_manufacturer_nvidia
  name:
    en: NVIDIA
    zh: 英伟达
domains:
  source_domain: 08_software_middleware
  target_domain: 02_components
description:
  en: MuJoCo Physics Engine mentions NVIDIA.
  zh: MuJoCo 物理引擎提及英伟达。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: 原版 MuJoCo 以 CPU 为主；大规模并行由两个后端承接——**MJX**（基于 JAX）与
    **MuJoCo Warp**（基于 NVIDIA Warp），二者消费同一 MJCF 模型（来源：官方文档 overview）。'
sources:
- id: src_001
  type: other
  title: KG body of ent_software_mujoco_physics_engine_2022
  url: https://kg.rounds-tech.com/entry/ent_software_mujoco_physics_engine_2022/
  accessed_at: '2026-08-06'
---
