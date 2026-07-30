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
  zh: Embodied$.$cpp 是一个面向具身AI模型的便携式C++推理运行时，由研究团队提出。其核心贡献在于通过五层架构设计，解决了异构机器人上VLA模型与WAM模型部署碎片化的问题，实现了多速率闭环执行与延迟优先推理。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02501v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots (arXiv)'
  url: https://arxiv.org/abs/2607.02501
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
现有推理运行时主要面向请求-响应服务，无法满足具身部署的实时闭环控制需求。Embodied$.$cpp 通过分析代表性VLA模型与WAM模型，提取共享执行路径并组织为输入适配器、序列构建器、骨干执行、头部插件和部署适配器五层架构。该运行时提供模块化多速率执行、延迟优先融合推理以及可扩展算子与I/O支持，通过单一后端抽象实现跨异构设备、机器人与仿真器的部署。

## 核心内容
### 方法架构
- **五层设计**：输入适配器处理多模态输入，序列构建器组织token序列，骨干执行层运行核心模型，头部插件支持任务特定输出，部署适配器对接不同硬件后端。
- **核心特性**：模块化多速率执行支持闭环控制中不同频率的模型调用；延迟优先融合推理针对batch-1场景优化；可扩展算子与I/O支持超越固定token接口的具身交互。

### 实验设置
- **VLA模型评估**：在HY-VLA与pi0.5两个模型上测试闭环执行，任务成功率分别达到100.0%与91.0%。
- **WAM基准测试**：使用LingBot-VA Transformer块进行初步评估，将块内存占用从312.2 MiB降至88.1 MiB。

### 关键结论
- Embodied$.$cpp 在保持高精度的同时显著提升部署效率，支持异构设备、机器人与仿真器的统一推理。
- 内存优化效果突出，WAM基准测试中内存减少超过70%，验证了架构设计的有效性。

## Overview
Embodied AI models now span vision-language-action (VLA) models and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend assumptions, and robot-side glue code, especially on heterogeneous edge devices. Existing inference runtimes are designed mainly for request-response serving and therefore do not satisfy the runtime contract of embodied deployment: multi-rate execution inside closed-loop control, latency-first batch-1 inference on heterogeneous hardware, and extensible embodied interfaces beyond fixed token I/O. We present Embodied$.$cpp, a portable C++ inference runtime for embodied models. Based on an architectural analysis of representative VLA models and WAMs, Embodied$.$cpp captures a shared execution path and organizes it into five layers: input adapters, sequence builders, backbone execution, head plugins, and deployment adapters. The runtime provides modular multi-rate execution, latency-first fused inference, and extensible operator and I/O support, enabling deployment across heterogeneous devices, robots, and simulators through one backend abstraction. We evaluate Embodied$.$cpp on two VLA models, HY-VLA and pi0.5, and on a preliminary WAM benchmark using a LingBot-VA Transformer block. The VLA deployments achieve successful closed-loop execution with 100.0% and 91.0% task success rates, respectively. The WAM benchmark reduces block memory from 312.2 MiB to 88.1 MiB. These results show that Embodied$.$cpp improves deployment efficiency while preserving high accuracy across diverse embodied model architectures.

## 개요
임베디드 AI 모델은 현재 시각-언어-행동(VLA) 모델과 세계-행동 모델(WAM)을 포괄하지만, 실제 배포는 모델별 Python 스택, 백엔드 가정, 로봇 측 글루 코드로 인해 특히 이기종 엣지 디바이스에서 파편화된 상태로 남아 있습니다. 기존 추론 런타임은 주로 요청-응답 서빙을 위해 설계되어 폐쇄 루프 제어 내 다중 속도 실행, 이기종 하드웨어에서의 지연 시간 우선 배치-1 추론, 고정 토큰 I/O를 넘어서는 확장 가능한 임베디드 인터페이스 등 임베디드 배포의 런타임 계약을 충족하지 못합니다. 우리는 임베디드 모델을 위한 이식 가능한 C++ 추론 런타임인 Embodied$.$cpp를 제시합니다. 대표적인 VLA 모델과 WAM의 아키텍처 분석을 바탕으로 Embodied$.$cpp는 공유 실행 경로를 포착하여 입력 어댑터, 시퀀스 빌더, 백본 실행, 헤드 플러그인, 배포 어댑터의 다섯 계층으로 구성합니다. 이 런타임은 모듈식 다중 속도 실행, 지연 시간 우선 융합 추론, 확장 가능한 연산자 및 I/O 지원을 제공하여 하나의 백엔드 추상화를 통해 이기종 디바이스, 로봇, 시뮬레이터에 걸친 배포를 가능하게 합니다. 우리는 Embodied$.$cpp를 두 개의 VLA 모델(HY-VLA 및 pi0.5)과 LingBot-VA Transformer 블록을 사용한 예비 WAM 벤치마크에서 평가합니다. VLA 배포는 각각 100.0% 및 91.0%의 작업 성공률로 성공적인 폐쇄 루프 실행을 달성합니다. WAM 벤치마크는 블록 메모리를 312.2 MiB에서 88.1 MiB로 줄입니다. 이러한 결과는 Embodied$.$cpp가 다양한 임베디드 모델 아키텍처에서 높은 정확도를 유지하면서 배포 효율성을 향상시킴을 보여줍니다.

## 핵심 내용
임베디드 AI 모델은 현재 시각-언어-행동(VLA) 모델과 세계-행동 모델(WAM)을 포괄하지만, 실제 배포는 모델별 Python 스택, 백엔드 가정, 로봇 측 글루 코드로 인해 특히 이기종 엣지 디바이스에서 파편화된 상태로 남아 있습니다. 기존 추론 런타임은 주로 요청-응답 서빙을 위해 설계되어 폐쇄 루프 제어 내 다중 속도 실행, 이기종 하드웨어에서의 지연 시간 우선 배치-1 추론, 고정 토큰 I/O를 넘어서는 확장 가능한 임베디드 인터페이스 등 임베디드 배포의 런타임 계약을 충족하지 못합니다. 우리는 임베디드 모델을 위한 이식 가능한 C++ 추론 런타임인 Embodied$.$cpp를 제시합니다. 대표적인 VLA 모델과 WAM의 아키텍처 분석을 바탕으로 Embodied$.$cpp는 공유 실행 경로를 포착하여 입력 어댑터, 시퀀스 빌더, 백본 실행, 헤드 플러그인, 배포 어댑터의 다섯 계층으로 구성합니다. 이 런타임은 모듈식 다중 속도 실행, 지연 시간 우선 융합 추론, 확장 가능한 연산자 및 I/O 지원을 제공하여 하나의 백엔드 추상화를 통해 이기종 디바이스, 로봇, 시뮬레이터에 걸친 배포를 가능하게 합니다. 우리는 Embodied$.$cpp를 두 개의 VLA 모델(HY-VLA 및 pi0.5)과 LingBot-VA Transformer 블록을 사용한 예비 WAM 벤치마크에서 평가합니다. VLA 배포는 각각 100.0% 및 91.0%의 작업 성공률로 성공적인 폐쇄 루프 실행을 달성합니다. WAM 벤치마크는 블록 메모리를 312.2 MiB에서 88.1 MiB로 줄입니다. 이러한 결과는 Embodied$.$cpp가 다양한 임베디드 모델 아키텍처에서 높은 정확도를 유지하면서 배포 효율성을 향상시킴을 보여줍니다.

## 参考
- http://arxiv.org/abs/2607.02501v2
