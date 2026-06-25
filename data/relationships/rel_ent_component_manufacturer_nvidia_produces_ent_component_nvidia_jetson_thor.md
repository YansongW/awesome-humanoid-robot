---
$id: "rel_ent_component_manufacturer_nvidia_produces_ent_component_nvidia_jetson_thor"
$schema: "../../../../../data/schema/v1/relationship_schema.json"
$version: 1

type: "produces"

source:
  id: "ent_component_manufacturer_nvidia"
  name:
    en: "NVIDIA"
    zh: "英伟达"
    ko: "엔비디아"

target:
  id: "ent_component_nvidia_jetson_thor"
  name:
    en: "NVIDIA Jetson Thor"
    zh: "NVIDIA Jetson Thor"
    ko: "NVIDIA Jetson Thor"

domains:
  source_domain: "02_components"
  target_domain: "02_components"

description:
  en: "NVIDIA designs and manufactures the Jetson Thor edge AI compute module."
  zh: "NVIDIA 设计并制造 Jetson Thor 边缘 AI 计算模块。"
  ko: "NVIDIA는 Jetson Thor 엣지 AI 컴퓨팅 모듈을 설계하고 제조합니다."

verification:
  status: "partially_verified"
  reviewed_by: "ai"
  reviewed_at: "2026-06-25"
  confidence: "medium"
  notes: "AI-extracted from NVIDIA official product blog; supply-chain details require human review."

sources:
  - id: "src_nvidia_jetson_thor_blog"
    type: "website"
    title: "Introducing NVIDIA Jetson Thor, the Ultimate Platform for Physical AI"
    url: "https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai/"
    date: "2025-08-25"
    accessed_at: "2026-06-25"
---
