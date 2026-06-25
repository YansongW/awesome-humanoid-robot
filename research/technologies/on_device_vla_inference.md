---
$id: "ent_tech_on_device_vla_inference"
$schema: "../../../../../data/schema/v1/entry_schema.json"
$version: 1

type: "technology"

names:
  en: "On-Device VLA Inference"
  zh: "端侧 VLA 推理"
  ko: "온디바이스 VLA 추론"

summary:
  en: "The practice of running Vision-Language-Action models directly on robot-embedded edge compute rather than offloading to edge or cloud servers, driven by latency, connectivity, and privacy constraints."
  zh: "将视觉-语言-动作模型直接部署在机器人内置边缘计算设备上，而非卸载到边缘或云端服务器，以满足延迟、连接性和隐私约束。"
  ko: "지연 시간, 연결성 및 프라이버시 제약을 해결하기 위해 VLA 모델을 엣지 또는 클라우드 서버가 아닌 로봇 임베디드 엣지 컴퓨팅에서 직접 실행하는 기술 방식."

domains:
  - "07_ai_models_algorithms"
  - "08_software_middleware"
  - "02_components"

layers:
  - "intelligence"

functional_roles:
  - "intelligence"
  - "tool_equipment"

tags:
  - "vla"
  - "on_device_inference"
  - "edge_compute"
  - "latency"
  - "real_time_control"
  - "humanoid"

verification:
  status: "partially_verified"
  reviewed_by: "ai"
  reviewed_at: "2026-06-25"
  confidence: "medium"
  notes: "AI-extracted from VLA-Perf paper and NVIDIA deployment blog; specific latency claims depend on model and quantization configuration."

sources:
  - id: "src_vla_perf_paper"
    type: "paper"
    title: "How Fast Can I Run My VLA? Demystifying VLA Inference Performance with VLA-Perf"
    url: "https://arxiv.org/abs/2602.18397"
    date: "2026-02-20"
    accessed_at: "2026-06-25"
  - id: "src_nvidia_gr00t_n16_blog"
    type: "website"
    title: "Building Generalist Humanoid Capabilities with NVIDIA Isaac GR00T N1.6 Using a Sim-to-Real Workflow"
    url: "https://developer.nvidia.com/blog/building-generalist-humanoid-capabilities-with-nvidia-isaac-gr00t-n1-6-using-a-sim-to-real-workflow/"
    date: "2026-01-08"
    accessed_at: "2026-06-25"
---

# On-Device VLA Inference

## Overview

On-device VLA inference refers to executing Vision-Language-Action models entirely on the robot's embedded compute, avoiding round-trips to edge or cloud servers. This deployment mode is motivated by the tight latency budgets of high-frequency control loops (e.g., balance recovery, dexterous manipulation) and by operational constraints such as network availability and data privacy.

## Key Trade-offs

- **Latency**: on-device execution removes network latency, but edge GPUs such as Jetson Thor still achieve lower inference frequency than datacenter GPUs.
- **Power and thermal**: robot-embedded compute must fit within onboard power budgets and cooling limits.
- **Model size**: quantization (FP8, FP4, INT8/INT4) and distillation are commonly used to fit large VLAs on edge hardware.
- **Reliability**: local inference is preferable when network conditions are poor, while server-side inference can deliver higher throughput when connectivity is reliable.

## Relevance to Humanoid Robotics

Humanoid robots must close sensorimotor loops quickly enough to maintain balance and manipulate safely. On-device VLA inference is therefore a key systems question for production humanoids, balancing model capability against hardware cost, power, and real-time performance.
