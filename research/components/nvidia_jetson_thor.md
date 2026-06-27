---
$id: ent_component_nvidia_jetson_thor
$schema: ../../../../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: NVIDIA Jetson Thor
  zh: NVIDIA Jetson Thor
  ko: NVIDIA Jetson Thor
summary:
  en: NVIDIA's flagship edge AI compute module for humanoid and physical AI robots,
    built on Blackwell architecture and designed to run multimodal generative AI,
    VLMs, and VLA policies on-device.
  zh: NVIDIA 面向人形机器人和物理 AI 机器人的旗舰边缘 AI 计算模块，基于 Blackwell 架构，支持在设备端运行多模态生成式 AI、视觉语言模型和
    VLA 策略。
  ko: NVIDIA의 휴인oid 및 물리 AI 로봇용 플래그십 엣지 AI 컴퓨팅 모듈로, Blackwell 아키텍처 기반이며 온디바이스에서 멀티모달
    생성 AI, VLM 및 VLA 정책 실행을 위해 설계됨.
domains:
- 02_components
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- upstream
- intelligence
functional_roles:
- component
- intelligence
- tool_equipment
tags:
- nvidia
- jetson
- edge_compute
- vla
- on_device_inference
- blackwell
- humanoid
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: AI-extracted from NVIDIA official blog and VLA-Perf paper; detailed datasheet
    review pending.
sources:
- id: src_nvidia_jetson_thor_blog
  type: website
  title: Introducing NVIDIA Jetson Thor, the Ultimate Platform for Physical AI
  url: https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai/
  date: '2025-08-25'
  accessed_at: '2026-06-25'
- id: src_vla_perf_paper
  type: paper
  title: How Fast Can I Run My VLA? Demystifying VLA Inference Performance with VLA-Perf
  url: https://arxiv.org/abs/2602.18397
  date: '2026-02-20'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
---

# NVIDIA Jetson Thor

## 抽象

> **生活实例**：它就像战斗机座舱里的独立飞行电脑——不需要时时请示地面塔台，自己就能在极短时间内完成感知、判断并下达动作指令。

> **自然语言逻辑**：NVIDIA Jetson Thor 是人形机器人的“ onboard AI 大脑”，负责在机器人本地上运行视觉-语言-动作（VLA）等大模型；它决定了机器人能跑多复杂的 AI、反应有多快、功耗有多大，是让机器人摆脱对远程服务器依赖的关键计算模块。

## Overview

Jetson Thor is NVIDIA's next-generation system-on-module (SOM) targeted at humanoid and other physical AI robots. It is based on the Blackwell GPU architecture and is positioned as an on-robot "AI super brain" capable of running large multimodal models including vision-language-action (VLA) policies locally.

## Key Characteristics

- **Architecture**: Blackwell-based GPU with native FP4 support and transformer engine.
- **Memory**: up to 128 GB unified memory (per partner/product briefs).
- **Performance**: NVIDIA claims up to ~5× generative-AI speedup over Jetson AGX Orin for LLMs, VLMs, and VLAs such as GR00T N1.
- **Power**: configurable envelopes, commonly cited around 40–130 W.
- **Software**: supported by NVIDIA JetPack, Isaac GR00T, Isaac Lab, and TensorRT / ModelOpt quantization workflows.

## Relevance to Humanoid Robotics

Jetson Thor exemplifies the hardware-software co-design required for deployable humanoid VLAs: it must provide enough tensor throughput for multimodal inference while fitting within a robot's power, thermal, and latency budget. Its availability influences whether OEMs can run policies on-device or must rely on tethered edge/cloud servers.
