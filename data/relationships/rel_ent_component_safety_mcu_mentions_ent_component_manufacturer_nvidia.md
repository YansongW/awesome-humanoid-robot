---
$id: rel_ent_component_safety_mcu_mentions_ent_component_manufacturer_nvidia
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_component_safety_mcu
  name:
    en: Safety Microcontroller Unit (Safety MCU)
    zh: 安全MCU
target:
  id: ent_component_manufacturer_nvidia
  name:
    en: NVIDIA
    zh: 英伟达
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Safety Microcontroller Unit (Safety MCU) mentions NVIDIA.
  zh: 安全MCU提及英伟达。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: 面向 Transformer、扩散模型和机器人策略的专用加速器（如 NVIDIA Blackwell、Qualcomm
    Hexagon NPU、Apple Neural Engine）持续提高能效。'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_safety_mcu
  url: https://kg.rounds-tech.com/entry/ent_component_safety_mcu/
  accessed_at: '2026-07-16'
---
