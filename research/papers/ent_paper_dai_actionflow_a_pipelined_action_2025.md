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
  zh: 'ActionFlow: A Pipelined Action Acceleration for Vision Language Models on Edge (ActionFlow), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by School of Computer Science and Technology, University of Science and Technology
    of China, Suzhou Institute for Advanced Research, University of Science and Technology of China, IEIT SYSTEMS Co., Ltd..'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.20276v1.
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
Vision-Language-Action (VLA) models have emerged as a unified paradigm for robotic perception and control, enabling emergent generalization and long-horizon task execution. However, their deployment in dynamic, real-world environments is severely hin dered by high inference latency. While smooth robotic interaction requires control frequencies of 20 to 30 Hz, current VLA models typi cally operate at only 3-5 Hz on edge devices due to the memory bound nature of autoregressive decoding. Existing optimizations often require extensive retraining or compromise model accuracy. To bridge this gap, we introduce ActionFlow, a system-level inference framework tailored for resource-constrained edge plat forms. At the core of ActionFlow is a Cross-Request Pipelin ing strategy, a novel scheduler that redefines VLA inference as a macro-pipeline of micro-requests. The strategy intelligently batches memory-bound Decode phases with compute-bound Prefill phases across continuous time steps to maximize hardware utilization. Furthermore, to support this scheduling, we propose a Cross Request State Packed Forward operator and a Unified KV Ring Buffer, which fuse fragmented memory operations into efficient dense computations. Experimental results demonstrate that ActionFlow achieves a 2.55x improvement in FPS on the OpenVLA-7B model without retraining, enabling real-time dy namic manipulation on edge hardware. Our work is available at https://anonymous.4open.science/r/ActionFlow-1D47.

## 核心内容
Vision-Language-Action (VLA) models have emerged as a unified paradigm for robotic perception and control, enabling emergent generalization and long-horizon task execution. However, their deployment in dynamic, real-world environments is severely hin dered by high inference latency. While smooth robotic interaction requires control frequencies of 20 to 30 Hz, current VLA models typi cally operate at only 3-5 Hz on edge devices due to the memory bound nature of autoregressive decoding. Existing optimizations often require extensive retraining or compromise model accuracy. To bridge this gap, we introduce ActionFlow, a system-level inference framework tailored for resource-constrained edge plat forms. At the core of ActionFlow is a Cross-Request Pipelin ing strategy, a novel scheduler that redefines VLA inference as a macro-pipeline of micro-requests. The strategy intelligently batches memory-bound Decode phases with compute-bound Prefill phases across continuous time steps to maximize hardware utilization. Furthermore, to support this scheduling, we propose a Cross Request State Packed Forward operator and a Unified KV Ring Buffer, which fuse fragmented memory operations into efficient dense computations. Experimental results demonstrate that ActionFlow achieves a 2.55x improvement in FPS on the OpenVLA-7B model without retraining, enabling real-time dy namic manipulation on edge hardware. Our work is available at https://anonymous.4open.science/r/ActionFlow-1D47.

## 参考
- http://arxiv.org/abs/2512.20276v1

## Overview
Vision-Language-Action (VLA) models have emerged as a unified paradigm for robotic perception and control, enabling emergent generalization and long-horizon task execution. However, their deployment in dynamic, real-world environments is severely hindered by high inference latency. While smooth robotic interaction requires control frequencies of 20 to 30 Hz, current VLA models typically operate at only 3-5 Hz on edge devices due to the memory-bound nature of autoregressive decoding. Existing optimizations often require extensive retraining or compromise model accuracy. To bridge this gap, we introduce ActionFlow, a system-level inference framework tailored for resource-constrained edge platforms. At the core of ActionFlow is a Cross-Request Pipelining strategy, a novel scheduler that redefines VLA inference as a macro-pipeline of micro-requests. The strategy intelligently batches memory-bound Decode phases with compute-bound Prefill phases across continuous time steps to maximize hardware utilization. Furthermore, to support this scheduling, we propose a Cross-Request State Packed Forward operator and a Unified KV Ring Buffer, which fuse fragmented memory operations into efficient dense computations. Experimental results demonstrate that ActionFlow achieves a 2.55x improvement in FPS on the OpenVLA-7B model without retraining, enabling real-time dynamic manipulation on edge hardware. Our work is available at https://anonymous.4open.science/r/ActionFlow-1D47.

## Content
Vision-Language-Action (VLA) models have emerged as a unified paradigm for robotic perception and control, enabling emergent generalization and long-horizon task execution. However, their deployment in dynamic, real-world environments is severely hindered by high inference latency. While smooth robotic interaction requires control frequencies of 20 to 30 Hz, current VLA models typically operate at only 3-5 Hz on edge devices due to the memory-bound nature of autoregressive decoding. Existing optimizations often require extensive retraining or compromise model accuracy. To bridge this gap, we introduce ActionFlow, a system-level inference framework tailored for resource-constrained edge platforms. At the core of ActionFlow is a Cross-Request Pipelining strategy, a novel scheduler that redefines VLA inference as a macro-pipeline of micro-requests. The strategy intelligently batches memory-bound Decode phases with compute-bound Prefill phases across continuous time steps to maximize hardware utilization. Furthermore, to support this scheduling, we propose a Cross-Request State Packed Forward operator and a Unified KV Ring Buffer, which fuse fragmented memory operations into efficient dense computations. Experimental results demonstrate that ActionFlow achieves a 2.55x improvement in FPS on the OpenVLA-7B model without retraining, enabling real-time dynamic manipulation on edge hardware. Our work is available at https://anonymous.4open.science/r/ActionFlow-1D47.

## 개요
Vision-Language-Action (VLA) 모델은 로봇 인식 및 제어를 위한 통합 패러다임으로 등장하여, 창발적 일반화와 장기 작업 실행을 가능하게 합니다. 그러나 동적이고 실제 환경에서의 배포는 높은 추론 지연 시간으로 인해 심각하게 제한됩니다. 원활한 로봇 상호작용을 위해서는 20~30Hz의 제어 주파수가 필요한 반면, 현재 VLA 모델은 자동회귀 디코딩의 메모리 바운드 특성으로 인해 엣지 디바이스에서 일반적으로 3~5Hz로만 작동합니다. 기존 최적화는 종종 광범위한 재학습이 필요하거나 모델 정확도를 저하시킵니다. 이러한 격차를 해소하기 위해, 우리는 자원이 제한된 엣지 플랫폼에 특화된 시스템 수준 추론 프레임워크인 ActionFlow를 소개합니다. ActionFlow의 핵심은 Cross-Request Pipelining 전략으로, VLA 추론을 마이크로 요청의 매크로 파이프라인으로 재정의하는 새로운 스케줄러입니다. 이 전략은 연속적인 시간 단계에서 메모리 바운드인 Decode 단계와 계산 바운드인 Prefill 단계를 지능적으로 배치하여 하드웨어 활용도를 극대화합니다. 또한, 이 스케줄링을 지원하기 위해 Cross Request State Packed Forward 연산자와 Unified KV Ring Buffer를 제안하여, 단편화된 메모리 연산을 효율적인 밀집 계산으로 통합합니다. 실험 결과, ActionFlow는 재학습 없이 OpenVLA-7B 모델에서 FPS를 2.55배 향상시켜 엣지 하드웨어에서 실시간 동적 조작을 가능하게 합니다. 본 연구는 https://anonymous.4open.science/r/ActionFlow-1D47에서 확인할 수 있습니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 로봇 인식 및 제어를 위한 통합 패러다임으로 등장하여, 창발적 일반화와 장기 작업 실행을 가능하게 합니다. 그러나 동적이고 실제 환경에서의 배포는 높은 추론 지연 시간으로 인해 심각하게 제한됩니다. 원활한 로봇 상호작용을 위해서는 20~30Hz의 제어 주파수가 필요한 반면, 현재 VLA 모델은 자동회귀 디코딩의 메모리 바운드 특성으로 인해 엣지 디바이스에서 일반적으로 3~5Hz로만 작동합니다. 기존 최적화는 종종 광범위한 재학습이 필요하거나 모델 정확도를 저하시킵니다. 이러한 격차를 해소하기 위해, 우리는 자원이 제한된 엣지 플랫폼에 특화된 시스템 수준 추론 프레임워크인 ActionFlow를 소개합니다. ActionFlow의 핵심은 Cross-Request Pipelining 전략으로, VLA 추론을 마이크로 요청의 매크로 파이프라인으로 재정의하는 새로운 스케줄러입니다. 이 전략은 연속적인 시간 단계에서 메모리 바운드인 Decode 단계와 계산 바운드인 Prefill 단계를 지능적으로 배치하여 하드웨어 활용도를 극대화합니다. 또한, 이 스케줄링을 지원하기 위해 Cross Request State Packed Forward 연산자와 Unified KV Ring Buffer를 제안하여, 단편화된 메모리 연산을 효율적인 밀집 계산으로 통합합니다. 실험 결과, ActionFlow는 재학습 없이 OpenVLA-7B 모델에서 FPS를 2.55배 향상시켜 엣지 하드웨어에서 실시간 동적 조작을 가능하게 합니다. 본 연구는 https://anonymous.4open.science/r/ActionFlow-1D47에서 확인할 수 있습니다.
