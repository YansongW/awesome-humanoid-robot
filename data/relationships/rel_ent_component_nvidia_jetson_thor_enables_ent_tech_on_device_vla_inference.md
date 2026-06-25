---
$id: "rel_ent_component_nvidia_jetson_thor_enables_ent_tech_on_device_vla_inference"
$schema: "../../../../../data/schema/v1/relationship_schema.json"
$version: 1

type: "enables"

source:
  id: "ent_component_nvidia_jetson_thor"
  name:
    en: "NVIDIA Jetson Thor"
    zh: "NVIDIA Jetson Thor"
    ko: "NVIDIA Jetson Thor"

target:
  id: "ent_tech_on_device_vla_inference"
  name:
    en: "On-Device VLA Inference"
    zh: "端侧 VLA 推理"
    ko: "온디바이스 VLA 추론"

domains:
  source_domain: "02_components"
  target_domain: "07_ai_models_algorithms"

description:
  en: "Jetson Thor's on-robot AI compute enables real-time VLA inference without relying on external servers."
  zh: "Jetson Thor 的机载 AI 算力支持不依赖外部服务器的实时 VLA 推理。"
  ko: "Jetson Thor의 온로봇 AI 컴퓨팅은 외부 서버에 의존하지 않는 실시간 VLA 추론을 가능하게 합니다."

verification:
  status: "partially_verified"
  reviewed_by: "ai"
  reviewed_at: "2026-06-25"
  confidence: "medium"
  notes: "Supported by VLA-Perf benchmarks and NVIDIA deployment blog; actual throughput depends on model size and quantization."

sources:
  - id: "src_vla_perf_paper"
    type: "paper"
    title: "How Fast Can I Run My VLA? Demystifying VLA Inference Performance with VLA-Perf"
    url: "https://arxiv.org/abs/2602.18397"
    date: "2026-02-20"
    accessed_at: "2026-06-25"
---
