---
$id: rel_ent_robot_system_toddlerbot_uses_ent_component_nvidia_jetson_agx_orin_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_robot_system_toddlerbot
  name:
    en: ToddlerBot
    zh: ToddlerBot 幼儿机器人
target:
  id: ent_component_nvidia_jetson_agx_orin_2024
  name:
    en: NVIDIA Jetson AGX Orin
    zh: NVIDIA Jetson AGX Orin
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: ToddlerBot uses an NVIDIA Jetson Orin NX 16GB as its onboard computer for real-time inference (about
    100 ms latency for a 300M-parameter diffusion policy).
  zh: ToddlerBot 采用 NVIDIA Jetson Orin NX 16GB 作为机载主控进行实时推理（300M 参数扩散策略约 100 ms 延迟）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 来源档案 data/roadmap/research/toddlerbot.md 确认主控为 Jetson Orin NX 16GB；目标实体为知识图谱中 Jetson Orin 系列代表条目（AGX
    Orin），与 Orin NX 同属 Jetson Orin 家族但非同一型号。
sources:
- id: src_001
  type: website
  title: ToddlerBot paper arXiv:2502.00893
  url: https://arxiv.org/html/2502.00893v2
  accessed_at: '2026-07-01'
---
