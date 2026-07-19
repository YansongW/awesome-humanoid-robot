---
$id: rel_ent_component_nvidia_jetson_thor_has_prerequisite_ent_component_nvidia_jetson_agx_orin_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_component_nvidia_jetson_thor
  name:
    en: NVIDIA Jetson Thor
    zh: NVIDIA Jetson Thor
target:
  id: ent_component_nvidia_jetson_agx_orin_2024
  name:
    en: NVIDIA Jetson AGX Orin
    zh: NVIDIA Jetson AGX Orin
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: NVIDIA Jetson Thor has prerequisite NVIDIA Jetson AGX Orin.
  zh: NVIDIA Jetson Thor前置依赖NVIDIA Jetson AGX Orin。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: Jetson Thor是更先进的型号，理解前代Orin的架构有助于学习Thor的新特性。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
