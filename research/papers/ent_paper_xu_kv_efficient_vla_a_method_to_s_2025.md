---
$id: ent_paper_xu_kv_efficient_vla_a_method_to_s_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'KV-Efficient VLA: A Method to Speed up Vision Language Models with RNN-Gated Chunked KV Cache'
  zh: KV-Efficient VLA
  ko: 'KV-Efficient VLA: A Method to Speed up Vision Language Models with RNN-Gated Chunked KV Cache'
summary:
  en: 'KV-Efficient VLA: A Method to Speed up Vision Language Models with RNN-Gated Chunked KV Cache (KV-Efficient VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by University of Toronto, Tsinghua University.'
  zh: 'KV-Efficient VLA: A Method to Speed up Vision Language Models with RNN-Gated Chunked KV Cache (KV-Efficient VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by University of Toronto, Tsinghua University.'
  ko: 'KV-Efficient VLA: A Method to Speed up Vision Language Models with RNN-Gated Chunked KV Cache (KV-Efficient VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by University of Toronto, Tsinghua University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- kv_efficient_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.21354v2.
sources:
- id: src_001
  type: paper
  title: 'KV-Efficient VLA: A Method to Speed up Vision Language Models with RNN-Gated Chunked KV Cache (arXiv)'
  url: https://arxiv.org/abs/2509.21354
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models offer a unified framework for robotic perception and control, but their ability to scale to real-world, long-horizon tasks is limited by the high computational cost of attention and the large memory required for storing key-value (KV) pairs during inference, particularly when retaining historical image tokens as context. Recent methods have focused on scaling backbone architectures to improve generalization, with less emphasis on addressing inference inefficiencies essential for real-time use. In this work, we present KV-Efficient VLA, a model-agnostic memory compression approach designed to address these limitations by introducing a lightweight mechanism to selectively retain high-utility context. Our method partitions the KV cache into fixed-size chunks and employs a recurrent gating module to summarize and filter the historical context according to learned utility scores. This design aims to preserve recent fine-grained detail while aggressively pruning stale, low-relevance memory. Based on experiments, our approach can yield an average of 24.6% FLOPs savings, 1.34x inference speedup, and 1.87x reduction in KV memory. Our method integrates seamlessly into recent VLA stacks, enabling scalable inference without modifying downstream control logic.

## 核心内容
Vision-Language-Action (VLA) models offer a unified framework for robotic perception and control, but their ability to scale to real-world, long-horizon tasks is limited by the high computational cost of attention and the large memory required for storing key-value (KV) pairs during inference, particularly when retaining historical image tokens as context. Recent methods have focused on scaling backbone architectures to improve generalization, with less emphasis on addressing inference inefficiencies essential for real-time use. In this work, we present KV-Efficient VLA, a model-agnostic memory compression approach designed to address these limitations by introducing a lightweight mechanism to selectively retain high-utility context. Our method partitions the KV cache into fixed-size chunks and employs a recurrent gating module to summarize and filter the historical context according to learned utility scores. This design aims to preserve recent fine-grained detail while aggressively pruning stale, low-relevance memory. Based on experiments, our approach can yield an average of 24.6% FLOPs savings, 1.34x inference speedup, and 1.87x reduction in KV memory. Our method integrates seamlessly into recent VLA stacks, enabling scalable inference without modifying downstream control logic.

## 参考
- http://arxiv.org/abs/2509.21354v2

## Overview
Vision-Language-Action (VLA) models offer a unified framework for robotic perception and control, but their ability to scale to real-world, long-horizon tasks is limited by the high computational cost of attention and the large memory required for storing key-value (KV) pairs during inference, particularly when retaining historical image tokens as context. Recent methods have focused on scaling backbone architectures to improve generalization, with less emphasis on addressing inference inefficiencies essential for real-time use. In this work, we present KV-Efficient VLA, a model-agnostic memory compression approach designed to address these limitations by introducing a lightweight mechanism to selectively retain high-utility context. Our method partitions the KV cache into fixed-size chunks and employs a recurrent gating module to summarize and filter the historical context according to learned utility scores. This design aims to preserve recent fine-grained detail while aggressively pruning stale, low-relevance memory. Based on experiments, our approach can yield an average of 24.6% FLOPs savings, 1.34x inference speedup, and 1.87x reduction in KV memory. Our method integrates seamlessly into recent VLA stacks, enabling scalable inference without modifying downstream control logic.

## Content
Vision-Language-Action (VLA) models offer a unified framework for robotic perception and control, but their ability to scale to real-world, long-horizon tasks is limited by the high computational cost of attention and the large memory required for storing key-value (KV) pairs during inference, particularly when retaining historical image tokens as context. Recent methods have focused on scaling backbone architectures to improve generalization, with less emphasis on addressing inference inefficiencies essential for real-time use. In this work, we present KV-Efficient VLA, a model-agnostic memory compression approach designed to address these limitations by introducing a lightweight mechanism to selectively retain high-utility context. Our method partitions the KV cache into fixed-size chunks and employs a recurrent gating module to summarize and filter the historical context according to learned utility scores. This design aims to preserve recent fine-grained detail while aggressively pruning stale, low-relevance memory. Based on experiments, our approach can yield an average of 24.6% FLOPs savings, 1.34x inference speedup, and 1.87x reduction in KV memory. Our method integrates seamlessly into recent VLA stacks, enabling scalable inference without modifying downstream control logic.

## 개요
Vision-Language-Action (VLA) 모델은 로봇 인식 및 제어를 위한 통합 프레임워크를 제공하지만, 실제 세계의 장기적 과제로 확장하는 능력은 어텐션의 높은 계산 비용과 추론 중 키-값(KV) 쌍 저장에 필요한 대용량 메모리, 특히 과거 이미지 토큰을 컨텍스트로 유지할 때 제한됩니다. 최근 방법들은 일반화를 개선하기 위해 백본 아키텍처 확장에 초점을 맞추었으며, 실시간 사용에 필수적인 추론 비효율성 해결에는 덜 중점을 두었습니다. 본 연구에서는 KV-Efficient VLA를 제시합니다. 이는 모델에 구애받지 않는 메모리 압축 접근 방식으로, 학습된 유틸리티 점수에 따라 고효용 컨텍스트를 선택적으로 유지하는 경량 메커니즘을 도입하여 이러한 한계를 해결합니다. 우리의 방법은 KV 캐시를 고정 크기 청크로 분할하고, 순환 게이팅 모듈을 사용하여 학습된 유틸리티 점수에 따라 과거 컨텍스트를 요약 및 필터링합니다. 이 설계는 최근의 세부 정보를 보존하면서 오래되고 관련성이 낮은 메모리를 적극적으로 제거하는 것을 목표로 합니다. 실험에 따르면, 우리의 접근 방식은 평균 24.6%의 FLOPs 절감, 1.34배의 추론 속도 향상, 1.87배의 KV 메모리 감소를 달성할 수 있습니다. 우리의 방법은 최근 VLA 스택에 원활하게 통합되어 하위 제어 로직을 수정하지 않고도 확장 가능한 추론을 가능하게 합니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 로봇 인식 및 제어를 위한 통합 프레임워크를 제공하지만, 실제 세계의 장기적 과제로 확장하는 능력은 어텐션의 높은 계산 비용과 추론 중 키-값(KV) 쌍 저장에 필요한 대용량 메모리, 특히 과거 이미지 토큰을 컨텍스트로 유지할 때 제한됩니다. 최근 방법들은 일반화를 개선하기 위해 백본 아키텍처 확장에 초점을 맞추었으며, 실시간 사용에 필수적인 추론 비효율성 해결에는 덜 중점을 두었습니다. 본 연구에서는 KV-Efficient VLA를 제시합니다. 이는 모델에 구애받지 않는 메모리 압축 접근 방식으로, 학습된 유틸리티 점수에 따라 고효용 컨텍스트를 선택적으로 유지하는 경량 메커니즘을 도입하여 이러한 한계를 해결합니다. 우리의 방법은 KV 캐시를 고정 크기 청크로 분할하고, 순환 게이팅 모듈을 사용하여 학습된 유틸리티 점수에 따라 과거 컨텍스트를 요약 및 필터링합니다. 이 설계는 최근의 세부 정보를 보존하면서 오래되고 관련성이 낮은 메모리를 적극적으로 제거하는 것을 목표로 합니다. 실험에 따르면, 우리의 접근 방식은 평균 24.6%의 FLOPs 절감, 1.34배의 추론 속도 향상, 1.87배의 KV 메모리 감소를 달성할 수 있습니다. 우리의 방법은 최근 VLA 스택에 원활하게 통합되어 하위 제어 로직을 수정하지 않고도 확장 가능한 추론을 가능하게 합니다.
