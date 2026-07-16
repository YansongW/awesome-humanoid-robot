---
$id: ent_paper_embodiedcpp_a_portable_inferen_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots'
  zh: 'Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots'
  ko: 'Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots'
summary:
  en: 'arXiv:2607.02501v2 Announce Type: replace Abstract: Embodied AI models now span vision-language-action (VLA) models
    and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend
    assumptions, and robot-side glue code, especially on heterogeneous edge devices. Existing inference runtimes are designed
    mainly for request-response serving and therefore do not satisfy the runtime contract of embodied deployment: multi-rate
    execution inside closed-loop control, latency-first batch-1 inference on heterogeneous hardware, and extensible embodied
    interfaces beyond fixed token I/O. We present Embodied$.$cpp, a portable C++ inference runtime for embodied models. Based
    on an architectural analysis of representative VLA models and WAMs, Embodied$.$cpp captures a shared execution path and
    organizes it into five layers: input adapters, sequence builders, backbone execution, head plugins, and deployment adapters.
    The runtime provides modular multi-rate execution, latency-first fused inference, and extensible operator and I/O support,
    enabling deployment across heterogeneous devices, robots, and simulators through one backend abstraction. We evaluate
    Embodied$.$cpp on two VLA models, HY-VLA and pi0.5, and on a preliminary WAM benchmark using a LingBot-VA Transformer
    block. The VLA deployments achieve successful closed-loop execution with 100.0% and 91.0% task success rates, respectively.
    The WAM benchmark reduces block memory from 312.2 MiB to 88.1 MiB. These results show that Embodied$.$cpp improves deployment
    efficiency while preserving high accuracy across diverse embodied model architectures.'
  zh: 'arXiv:2607.02501v2 Announce Type: replace Abstract: Embodied AI models now span vision-language-action (VLA) models
    and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend
    assumptions, and robot-side glue code, especially on heterogeneous edge devices. Existing inference runtimes are designed
    mainly for request-response serving and therefore do not satisfy the runtime contract of embodied deployment: multi-rate
    execution inside closed-loop control, latency-first batch-1 inference on heterogeneous hardware, and extensible embodied
    interfaces beyond fixed token I/O. We present Embodied$.$cpp, a portable C++ inference runtime for embodied models. Based
    on an architectural analysis of representative VLA models and WAMs, Embodied$.$cpp captures a shared execution path and
    organizes it into five layers: input adapters, sequence builders, backbone execution, head plugins, and deployment adapters.
    The runtime provides modular multi-rate execution, latency-first fused inference, and extensible operator and I/O support,
    enabling deployment across heterogeneous devices, robots, and simulators through one backend abstraction. We evaluate
    Embodied$.$cpp on two VLA models, HY-VLA and pi0.5, and on a preliminary WAM benchmark using a LingBot-VA Transformer
    block. The VLA deployments achieve successful closed-loop execution with 100.0% and 91.0% task success rates, respectively.
    The WAM benchmark reduces block memory from 312.2 MiB to 88.1 MiB. These results show that Embodied$.$cpp improves deployment
    efficiency while preserving high accuracy across diverse embodied model architectures.'
  ko: 'arXiv:2607.02501v2 Announce Type: replace Abstract: Embodied AI models now span vision-language-action (VLA) models
    and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend
    assumptions, and robot-side glue code, especially on heterogeneous edge devices. Existing inference runtimes are designed
    mainly for request-response serving and therefore do not satisfy the runtime contract of embodied deployment: multi-rate
    execution inside closed-loop control, latency-first batch-1 inference on heterogeneous hardware, and extensible embodied
    interfaces beyond fixed token I/O. We present Embodied$.$cpp, a portable C++ inference runtime for embodied models. Based
    on an architectural analysis of representative VLA models and WAMs, Embodied$.$cpp captures a shared execution path and
    organizes it into five layers: input adapters, sequence builders, backbone execution, head plugins, and deployment adapters.
    The runtime provides modular multi-rate execution, latency-first fused inference, and extensible operator and I/O support,
    enabling deployment across heterogeneous devices, robots, and simulators through one backend abstraction. We evaluate
    Embodied$.$cpp on two VLA models, HY-VLA and pi0.5, and on a preliminary WAM benchmark using a LingBot-VA Transformer
    block. The VLA deployments achieve successful closed-loop execution with 100.0% and 91.0% task success rates, respectively.
    The WAM benchmark reduces block memory from 312.2 MiB to 88.1 MiB. These results show that Embodied$.$cpp improves deployment
    efficiency while preserving high accuracy across diverse embodied model architectures.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- embodiedcpp
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02501v2.
sources:
- id: src_001
  type: paper
  title: 'Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots (arXiv)'
  url: https://arxiv.org/abs/2607.02501
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Embodied AI models now span vision-language-action (VLA) models and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend assumptions, and robot-side glue code, especially on heterogeneous edge devices. Existing inference runtimes are designed mainly for request-response serving and therefore do not satisfy the runtime contract of embodied deployment: multi-rate execution inside closed-loop control, latency-first batch-1 inference on heterogeneous hardware, and extensible embodied interfaces beyond fixed token I/O. We present Embodied$.$cpp, a portable C++ inference runtime for embodied models. Based on an architectural analysis of representative VLA models and WAMs, Embodied$.$cpp captures a shared execution path and organizes it into five layers: input adapters, sequence builders, backbone execution, head plugins, and deployment adapters. The runtime provides modular multi-rate execution, latency-first fused inference, and extensible operator and I/O support, enabling deployment across heterogeneous devices, robots, and simulators through one backend abstraction. We evaluate Embodied$.$cpp on two VLA models, HY-VLA and pi0.5, and on a preliminary WAM benchmark using a LingBot-VA Transformer block. The VLA deployments achieve successful closed-loop execution with 100.0% and 91.0% task success rates, respectively. The WAM benchmark reduces block memory from 312.2 MiB to 88.1 MiB. These results show that Embodied$.$cpp improves deployment efficiency while preserving high accuracy across diverse embodied model architectures.

## 核心内容
Embodied AI models now span vision-language-action (VLA) models and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend assumptions, and robot-side glue code, especially on heterogeneous edge devices. Existing inference runtimes are designed mainly for request-response serving and therefore do not satisfy the runtime contract of embodied deployment: multi-rate execution inside closed-loop control, latency-first batch-1 inference on heterogeneous hardware, and extensible embodied interfaces beyond fixed token I/O. We present Embodied$.$cpp, a portable C++ inference runtime for embodied models. Based on an architectural analysis of representative VLA models and WAMs, Embodied$.$cpp captures a shared execution path and organizes it into five layers: input adapters, sequence builders, backbone execution, head plugins, and deployment adapters. The runtime provides modular multi-rate execution, latency-first fused inference, and extensible operator and I/O support, enabling deployment across heterogeneous devices, robots, and simulators through one backend abstraction. We evaluate Embodied$.$cpp on two VLA models, HY-VLA and pi0.5, and on a preliminary WAM benchmark using a LingBot-VA Transformer block. The VLA deployments achieve successful closed-loop execution with 100.0% and 91.0% task success rates, respectively. The WAM benchmark reduces block memory from 312.2 MiB to 88.1 MiB. These results show that Embodied$.$cpp improves deployment efficiency while preserving high accuracy across diverse embodied model architectures.

## 参考
- http://arxiv.org/abs/2607.02501v2

## Overview
Embodied AI models now span vision-language-action (VLA) models and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend assumptions, and robot-side glue code, especially on heterogeneous edge devices. Existing inference runtimes are designed mainly for request-response serving and therefore do not satisfy the runtime contract of embodied deployment: multi-rate execution inside closed-loop control, latency-first batch-1 inference on heterogeneous hardware, and extensible embodied interfaces beyond fixed token I/O. We present Embodied$.$cpp, a portable C++ inference runtime for embodied models. Based on an architectural analysis of representative VLA models and WAMs, Embodied$.$cpp captures a shared execution path and organizes it into five layers: input adapters, sequence builders, backbone execution, head plugins, and deployment adapters. The runtime provides modular multi-rate execution, latency-first fused inference, and extensible operator and I/O support, enabling deployment across heterogeneous devices, robots, and simulators through one backend abstraction. We evaluate Embodied$.$cpp on two VLA models, HY-VLA and pi0.5, and on a preliminary WAM benchmark using a LingBot-VA Transformer block. The VLA deployments achieve successful closed-loop execution with 100.0% and 91.0% task success rates, respectively. The WAM benchmark reduces block memory from 312.2 MiB to 88.1 MiB. These results show that Embodied$.$cpp improves deployment efficiency while preserving high accuracy across diverse embodied model architectures.

## Content
Embodied AI models now span vision-language-action (VLA) models and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend assumptions, and robot-side glue code, especially on heterogeneous edge devices. Existing inference runtimes are designed mainly for request-response serving and therefore do not satisfy the runtime contract of embodied deployment: multi-rate execution inside closed-loop control, latency-first batch-1 inference on heterogeneous hardware, and extensible embodied interfaces beyond fixed token I/O. We present Embodied$.$cpp, a portable C++ inference runtime for embodied models. Based on an architectural analysis of representative VLA models and WAMs, Embodied$.$cpp captures a shared execution path and organizes it into five layers: input adapters, sequence builders, backbone execution, head plugins, and deployment adapters. The runtime provides modular multi-rate execution, latency-first fused inference, and extensible operator and I/O support, enabling deployment across heterogeneous devices, robots, and simulators through one backend abstraction. We evaluate Embodied$.$cpp on two VLA models, HY-VLA and pi0.5, and on a preliminary WAM benchmark using a LingBot-VA Transformer block. The VLA deployments achieve successful closed-loop execution with 100.0% and 91.0% task success rates, respectively. The WAM benchmark reduces block memory from 312.2 MiB to 88.1 MiB. These results show that Embodied$.$cpp improves deployment efficiency while preserving high accuracy across diverse embodied model architectures.

## 개요
임베디드 AI 모델은 현재 시각-언어-행동(VLA) 모델과 세계-행동 모델(WAM)을 포괄하지만, 실제 배포는 모델별 Python 스택, 백엔드 가정, 로봇 측 글루 코드로 인해 특히 이기종 엣지 디바이스에서 파편화된 상태로 남아 있습니다. 기존 추론 런타임은 주로 요청-응답 서빙을 위해 설계되어 폐쇄 루프 제어 내 다중 속도 실행, 이기종 하드웨어에서의 지연 시간 우선 배치-1 추론, 고정 토큰 I/O를 넘어서는 확장 가능한 임베디드 인터페이스 등 임베디드 배포의 런타임 계약을 충족하지 못합니다. 우리는 임베디드 모델을 위한 이식 가능한 C++ 추론 런타임인 Embodied$.$cpp를 제시합니다. 대표적인 VLA 모델과 WAM의 아키텍처 분석을 바탕으로 Embodied$.$cpp는 공유 실행 경로를 포착하여 입력 어댑터, 시퀀스 빌더, 백본 실행, 헤드 플러그인, 배포 어댑터의 다섯 계층으로 구성합니다. 이 런타임은 모듈식 다중 속도 실행, 지연 시간 우선 융합 추론, 확장 가능한 연산자 및 I/O 지원을 제공하여 하나의 백엔드 추상화를 통해 이기종 디바이스, 로봇, 시뮬레이터에 걸친 배포를 가능하게 합니다. 우리는 Embodied$.$cpp를 두 개의 VLA 모델(HY-VLA 및 pi0.5)과 LingBot-VA Transformer 블록을 사용한 예비 WAM 벤치마크에서 평가합니다. VLA 배포는 각각 100.0% 및 91.0%의 작업 성공률로 성공적인 폐쇄 루프 실행을 달성합니다. WAM 벤치마크는 블록 메모리를 312.2 MiB에서 88.1 MiB로 줄입니다. 이러한 결과는 Embodied$.$cpp가 다양한 임베디드 모델 아키텍처에서 높은 정확도를 유지하면서 배포 효율성을 향상시킴을 보여줍니다.

## 핵심 내용
임베디드 AI 모델은 현재 시각-언어-행동(VLA) 모델과 세계-행동 모델(WAM)을 포괄하지만, 실제 배포는 모델별 Python 스택, 백엔드 가정, 로봇 측 글루 코드로 인해 특히 이기종 엣지 디바이스에서 파편화된 상태로 남아 있습니다. 기존 추론 런타임은 주로 요청-응답 서빙을 위해 설계되어 폐쇄 루프 제어 내 다중 속도 실행, 이기종 하드웨어에서의 지연 시간 우선 배치-1 추론, 고정 토큰 I/O를 넘어서는 확장 가능한 임베디드 인터페이스 등 임베디드 배포의 런타임 계약을 충족하지 못합니다. 우리는 임베디드 모델을 위한 이식 가능한 C++ 추론 런타임인 Embodied$.$cpp를 제시합니다. 대표적인 VLA 모델과 WAM의 아키텍처 분석을 바탕으로 Embodied$.$cpp는 공유 실행 경로를 포착하여 입력 어댑터, 시퀀스 빌더, 백본 실행, 헤드 플러그인, 배포 어댑터의 다섯 계층으로 구성합니다. 이 런타임은 모듈식 다중 속도 실행, 지연 시간 우선 융합 추론, 확장 가능한 연산자 및 I/O 지원을 제공하여 하나의 백엔드 추상화를 통해 이기종 디바이스, 로봇, 시뮬레이터에 걸친 배포를 가능하게 합니다. 우리는 Embodied$.$cpp를 두 개의 VLA 모델(HY-VLA 및 pi0.5)과 LingBot-VA Transformer 블록을 사용한 예비 WAM 벤치마크에서 평가합니다. VLA 배포는 각각 100.0% 및 91.0%의 작업 성공률로 성공적인 폐쇄 루프 실행을 달성합니다. WAM 벤치마크는 블록 메모리를 312.2 MiB에서 88.1 MiB로 줄입니다. 이러한 결과는 Embodied$.$cpp가 다양한 임베디드 모델 아키텍처에서 높은 정확도를 유지하면서 배포 효율성을 향상시킴을 보여줍니다.
