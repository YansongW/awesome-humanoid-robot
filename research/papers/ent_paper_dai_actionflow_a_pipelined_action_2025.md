---
$id: ent_paper_dai_actionflow_a_pipelined_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ActionFlow: A Pipelined Action Acceleration for Vision Language Models on Edge'
  zh: ActionFlow
  ko: 'ActionFlow: A Pipelined Action Acceleration for Vision Language Models on Edge'
summary:
  en: 'ActionFlow: A Pipelined Action Acceleration for Vision Language Models on Edge (ActionFlow), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by School of Computer Science and Technology, University of Science and Technology
    of China, Suzhou Institute for Advanced Research, University of Science and Technology of China, IEIT SYSTEMS Co., Ltd..'
  zh: ActionFlow 是中国科学技术大学与浪潮信息联合提出的系统级推理加速框架，针对边缘设备上视觉-语言-动作（VLA）模型推理延迟高的问题，通过跨请求流水线调度策略实现 2.55 倍 FPS 提升，无需重新训练即可在边缘硬件上达到实时动态操控所需的
    20-30 Hz 控制频率。
  ko: 'ActionFlow: A Pipelined Action Acceleration for Vision Language Models on Edge (ActionFlow), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by School of Computer Science and Technology, University of Science and Technology
    of China, Suzhou Institute for Advanced Research, University of Science and Technology of China, IEIT SYSTEMS Co., Ltd..'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- actionflow
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.20276v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (768 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'ActionFlow: A Pipelined Action Acceleration for Vision Language Models on Edge (arXiv)'
  url: https://arxiv.org/abs/2512.20276
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ActionFlow source
  url: https://doi.org/10.48550/arXiv.2512.20276
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
当前 VLA 模型在边缘设备上因自回归解码的内存瓶颈，推理速度仅 3-5 Hz，远低于机器人实时操控所需的 20-30 Hz。ActionFlow 提出跨请求流水线策略，将 VLA 推理重构为微请求组成的宏流水线，智能地将内存密集的解码阶段与计算密集的预填充阶段跨连续时间步进行批处理。为支撑该调度，框架设计了跨请求状态打包前向算子与统一 KV 环缓冲区，将碎片化内存操作融合为高效密集计算。实验表明，在 OpenVLA-7B 模型上无需重新训练即可实现 2.55 倍 FPS 提升。

## 核心内容
### 核心挑战
- 边缘设备上 VLA 模型因自回归解码的内存瓶颈，推理速度仅 3-5 Hz，远低于机器人实时操控所需的 20-30 Hz
- 现有优化方案需大量重新训练或牺牲模型精度

### ActionFlow 框架设计
#### 跨请求流水线策略
- 将 VLA 推理重构为宏流水线，包含多个微请求
- 智能调度：将内存密集的 Decode 阶段与计算密集的 Prefill 阶段跨连续时间步进行批处理，最大化硬件利用率

#### 关键算子与数据结构
- **跨请求状态打包前向算子**：融合碎片化内存操作
- **统一 KV 环缓冲区**：将分散的键值缓存组织为连续内存块，减少内存访问开销

### 实验设置与结果
- **模型**：OpenVLA-7B
- **硬件**：边缘设备（未指定具体型号）
- **性能提升**：FPS 提升 2.55 倍，无需重新训练
- **实时性**：达到实时动态操控所需的 20-30 Hz 控制频率

### 结论
ActionFlow 通过系统级优化，在不牺牲模型精度的前提下，显著提升边缘设备上 VLA 模型的推理速度，为机器人实时操控提供可行方案。代码已开源。

## Overview
Vision-Language-Action (VLA) models have emerged as a unified paradigm for robotic perception and control, enabling emergent generalization and long-horizon task execution. However, their deployment in dynamic, real-world environments is severely hin dered by high inference latency. While smooth robotic interaction requires control frequencies of 20 to 30 Hz, current VLA models typi cally operate at only 3-5 Hz on edge devices due to the memory bound nature of autoregressive decoding. Existing optimizations often require extensive retraining or compromise model accuracy. To bridge this gap, we introduce ActionFlow, a system-level inference framework tailored for resource-constrained edge plat forms. At the core of ActionFlow is a Cross-Request Pipelin ing strategy, a novel scheduler that redefines VLA inference as a macro-pipeline of micro-requests. The strategy intelligently batches memory-bound Decode phases with compute-bound Prefill phases across continuous time steps to maximize hardware utilization. Furthermore, to support this scheduling, we propose a Cross Request State Packed Forward operator and a Unified KV Ring Buffer, which fuse fragmented memory operations into efficient dense computations. Experimental results demonstrate that ActionFlow achieves a 2.55x improvement in FPS on the OpenVLA-7B model without retraining, enabling real-time dy namic manipulation on edge hardware. Our work is available at https://anonymous.4open.science/r/ActionFlow-1D47.

## Overview
Vision-Language-Action (VLA) models have emerged as a unified paradigm for robotic perception and control, enabling emergent generalization and long-horizon task execution. However, their deployment in dynamic, real-world environments is severely hindered by high inference latency. While smooth robotic interaction requires control frequencies of 20 to 30 Hz, current VLA models typically operate at only 3-5 Hz on edge devices due to the memory-bound nature of autoregressive decoding. Existing optimizations often require extensive retraining or compromise model accuracy. To bridge this gap, we introduce ActionFlow, a system-level inference framework tailored for resource-constrained edge platforms. At the core of ActionFlow is a Cross-Request Pipelining strategy, a novel scheduler that redefines VLA inference as a macro-pipeline of micro-requests. The strategy intelligently batches memory-bound Decode phases with compute-bound Prefill phases across continuous time steps to maximize hardware utilization. Furthermore, to support this scheduling, we propose a Cross-Request State Packed Forward operator and a Unified KV Ring Buffer, which fuse fragmented memory operations into efficient dense computations. Experimental results demonstrate that ActionFlow achieves a 2.55x improvement in FPS on the OpenVLA-7B model without retraining, enabling real-time dynamic manipulation on edge hardware. Our work is available at https://anonymous.4open.science/r/ActionFlow-1D47.

## Content
Vision-Language-Action (VLA) models have emerged as a unified paradigm for robotic perception and control, enabling emergent generalization and long-horizon task execution. However, their deployment in dynamic, real-world environments is severely hindered by high inference latency. While smooth robotic interaction requires control frequencies of 20 to 30 Hz, current VLA models typically operate at only 3-5 Hz on edge devices due to the memory-bound nature of autoregressive decoding. Existing optimizations often require extensive retraining or compromise model accuracy. To bridge this gap, we introduce ActionFlow, a system-level inference framework tailored for resource-constrained edge platforms. At the core of ActionFlow is a Cross-Request Pipelining strategy, a novel scheduler that redefines VLA inference as a macro-pipeline of micro-requests. The strategy intelligently batches memory-bound Decode phases with compute-bound Prefill phases across continuous time steps to maximize hardware utilization. Furthermore, to support this scheduling, we propose a Cross-Request State Packed Forward operator and a Unified KV Ring Buffer, which fuse fragmented memory operations into efficient dense computations. Experimental results demonstrate that ActionFlow achieves a 2.55x improvement in FPS on the OpenVLA-7B model without retraining, enabling real-time dynamic manipulation on edge hardware. Our work is available at https://anonymous.4open.science/r/ActionFlow-1D47.

## 参考
- http://arxiv.org/abs/2512.20276v1

## 개요
현재 VLA 모델은 엣지 디바이스에서 자기회귀 디코딩의 메모리 병목으로 인해 추론 속도가 3-5Hz에 불과하며, 이는 로봇 실시간 제어에 필요한 20-30Hz보다 훨씬 낮습니다. ActionFlow는 교차 요청 파이프라인 전략을 제안하여 VLA 추론을 마이크로 요청으로 구성된 매크로 파이프라인으로 재구성하고, 메모리 집약적인 디코딩 단계와 계산 집약적인 프리필 단계를 연속적인 시간 단계에 걸쳐 지능적으로 배치합니다. 이 스케줄링을 지원하기 위해 프레임워크는 교차 요청 상태 패킹 순방향 연산자와 통합 KV 링 버퍼를 설계하여 단편화된 메모리 연산을 효율적인 밀집 계산으로 융합합니다. 실험 결과, OpenVLA-7B 모델에서 재훈련 없이 2.55배의 FPS 향상을 달성했습니다.

## 핵심 내용
### 핵심 과제
- 엣지 디바이스에서 VLA 모델은 자기회귀 디코딩의 메모리 병목으로 인해 추론 속도가 3-5Hz에 불과하며, 이는 로봇 실시간 제어에 필요한 20-30Hz보다 훨씬 낮음
- 기존 최적화 방법은 대규모 재훈련이 필요하거나 모델 정확도를 희생함

### ActionFlow 프레임워크 설계
#### 교차 요청 파이프라인 전략
- VLA 추론을 여러 마이크로 요청으로 구성된 매크로 파이프라인으로 재구성
- 지능적 스케줄링: 메모리 집약적인 디코딩 단계와 계산 집약적인 프리필 단계를 연속적인 시간 단계에 걸쳐 배치하여 하드웨어 활용도를 극대화

#### 핵심 연산자 및 데이터 구조
- **교차 요청 상태 패킹 순방향 연산자**: 단편화된 메모리 연산 융합
- **통합 KV 링 버퍼**: 분산된 키-값 캐시를 연속 메모리 블록으로 구성하여 메모리 접근 오버헤드 감소

### 실험 설정 및 결과
- **모델**: OpenVLA-7B
- **하드웨어**: 엣지 디바이스 (구체적 모델 미지정)
- **성능 향상**: FPS 2.55배 향상, 재훈련 불필요
- **실시간성**: 실시간 동적 제어에 필요한 20-30Hz 제어 주파수 달성

### 결론
ActionFlow는 시스템 수준 최적화를 통해 모델 정확도를 희생하지 않으면서 엣지 디바이스에서 VLA 모델의 추론 속도를 크게 향상시켜 로봇 실시간 제어를 위한 실현 가능한 솔루션을 제공합니다. 코드는 오픈소스로 공개되었습니다.
