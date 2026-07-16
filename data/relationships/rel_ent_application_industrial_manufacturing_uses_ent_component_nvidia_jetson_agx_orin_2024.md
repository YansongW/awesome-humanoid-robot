---
$id: rel_ent_application_industrial_manufacturing_uses_ent_component_nvidia_jetson_agx_orin_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_application_industrial_manufacturing
  name:
    en: Industrial Manufacturing
    zh: 工业制造
target:
  id: ent_component_nvidia_jetson_agx_orin_2024
  name:
    en: NVIDIA Jetson AGX Orin
    zh: NVIDIA Jetson AGX Orin
domains:
  source_domain: 11_applications_markets
  target_domain: 02_components
description:
  en: Industrial Manufacturing uses NVIDIA Jetson AGX Orin.
  zh: 工业制造使用NVIDIA Jetson AGX Orin。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 工业制造应用场景使用了NVIDIA Jetson AGX Orin组件。 | 证据: -
    **优必选 Walker / 智元远征 A2 / 傅利叶 GR-1**：多采用 NVIDIA Jetson AGX Orin / Xavier 或国产替代平台作为上位机，结合 ARM MCU/FPGA 做关节实时控制。'
sources:
- id: src_001
  type: other
  title: KG body of ent_application_industrial_manufacturing
  url: https://kg.rounds-tech.com/entry/ent_application_industrial_manufacturing/
  accessed_at: '2026-07-16'
---
