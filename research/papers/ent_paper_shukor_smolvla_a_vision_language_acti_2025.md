---
$id: ent_paper_shukor_smolvla_a_vision_language_acti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics'
  zh: SmolVLA
  ko: 'SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics'
summary:
  en: 'SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (SmolVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Hugging Face, Sorbonne University, valeo.ai, École Normale Supérieure Paris-Saclay.'
  zh: 'SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (SmolVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Hugging Face, Sorbonne University, valeo.ai, École Normale Supérieure Paris-Saclay.'
  ko: 'SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (SmolVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Hugging Face, Sorbonne University, valeo.ai, École Normale Supérieure Paris-Saclay.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- smolvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.01844v1.
sources:
- id: src_001
  type: paper
  title: 'SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (arXiv)'
  url: https://arxiv.org/abs/2506.01844
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SmolVLA source
  url: https://doi.org/10.48550/arXiv.2506.01844
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language models (VLMs) pretrained on large-scale multimodal datasets encode rich visual and linguistic knowledge, making them a strong foundation for robotics. Rather than training robotic policies from scratch, recent approaches adapt VLMs into vision-language-action (VLA) models that enable natural language-driven perception and control. However, existing VLAs are typically massive--often with billions of parameters--leading to high training costs and limited real-world deployability. Moreover, they rely on academic and industrial datasets, overlooking the growing availability of community-collected data from affordable robotic platforms. In this work, we present SmolVLA, a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance. SmolVLA is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs. To further improve responsiveness, we introduce an asynchronous inference stack decoupling perception and action prediction from action execution, allowing higher control rates with chunked action generation. Despite its compact size, SmolVLA achieves performance comparable to VLAs that are 10x larger. We evaluate SmolVLA on a range of both simulated as well as real-world robotic benchmarks and release all code, pretrained models, and training data.

## 核心内容
Vision-language models (VLMs) pretrained on large-scale multimodal datasets encode rich visual and linguistic knowledge, making them a strong foundation for robotics. Rather than training robotic policies from scratch, recent approaches adapt VLMs into vision-language-action (VLA) models that enable natural language-driven perception and control. However, existing VLAs are typically massive--often with billions of parameters--leading to high training costs and limited real-world deployability. Moreover, they rely on academic and industrial datasets, overlooking the growing availability of community-collected data from affordable robotic platforms. In this work, we present SmolVLA, a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance. SmolVLA is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs. To further improve responsiveness, we introduce an asynchronous inference stack decoupling perception and action prediction from action execution, allowing higher control rates with chunked action generation. Despite its compact size, SmolVLA achieves performance comparable to VLAs that are 10x larger. We evaluate SmolVLA on a range of both simulated as well as real-world robotic benchmarks and release all code, pretrained models, and training data.

## 参考
- http://arxiv.org/abs/2506.01844v1

## Overview
Vision-language models (VLMs) pretrained on large-scale multimodal datasets encode rich visual and linguistic knowledge, making them a strong foundation for robotics. Rather than training robotic policies from scratch, recent approaches adapt VLMs into vision-language-action (VLA) models that enable natural language-driven perception and control. However, existing VLAs are typically massive—often with billions of parameters—leading to high training costs and limited real-world deployability. Moreover, they rely on academic and industrial datasets, overlooking the growing availability of community-collected data from affordable robotic platforms. In this work, we present SmolVLA, a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance. SmolVLA is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs. To further improve responsiveness, we introduce an asynchronous inference stack decoupling perception and action prediction from action execution, allowing higher control rates with chunked action generation. Despite its compact size, SmolVLA achieves performance comparable to VLAs that are 10x larger. We evaluate SmolVLA on a range of both simulated as well as real-world robotic benchmarks and release all code, pretrained models, and training data.

## Content
Vision-language models (VLMs) pretrained on large-scale multimodal datasets encode rich visual and linguistic knowledge, making them a strong foundation for robotics. Rather than training robotic policies from scratch, recent approaches adapt VLMs into vision-language-action (VLA) models that enable natural language-driven perception and control. However, existing VLAs are typically massive—often with billions of parameters—leading to high training costs and limited real-world deployability. Moreover, they rely on academic and industrial datasets, overlooking the growing availability of community-collected data from affordable robotic platforms. In this work, we present SmolVLA, a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance. SmolVLA is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs. To further improve responsiveness, we introduce an asynchronous inference stack decoupling perception and action prediction from action execution, allowing higher control rates with chunked action generation. Despite its compact size, SmolVLA achieves performance comparable to VLAs that are 10x larger. We evaluate SmolVLA on a range of both simulated as well as real-world robotic benchmarks and release all code, pretrained models, and training data.

## 개요
대규모 멀티모달 데이터셋으로 사전 학습된 비전-언어 모델(VLM)은 풍부한 시각 및 언어 지식을 인코딩하여 로봇 공학의 강력한 기반이 됩니다. 최근 접근법은 로봇 정책을 처음부터 학습하는 대신 VLM을 비전-언어-행동(VLA) 모델로 변환하여 자연어 기반의 인식 및 제어를 가능하게 합니다. 그러나 기존 VLA는 일반적으로 수십억 개의 매개변수를 가진 거대한 모델로, 높은 학습 비용과 제한된 실제 배포 가능성을 초래합니다. 또한 학술 및 산업 데이터셋에 의존하며, 저렴한 로봇 플랫폼에서 수집된 커뮤니티 데이터의 증가하는 가용성을 간과합니다. 본 연구에서는 경쟁력 있는 성능을 유지하면서 학습 및 추론 비용을 획기적으로 줄인 소형, 효율적, 커뮤니티 기반 VLA인 SmolVLA를 제시합니다. SmolVLA는 단일 GPU에서 학습되고 소비자용 GPU 또는 CPU에서 배포되도록 설계되었습니다. 응답성을 더욱 개선하기 위해 인식 및 행동 예측을 행동 실행에서 분리하는 비동기 추론 스택을 도입하여 청크 단위 행동 생성으로 더 높은 제어 속도를 가능하게 합니다. 작은 크기에도 불구하고 SmolVLA는 10배 더 큰 VLA와 비교할 수 있는 성능을 달성합니다. 우리는 시뮬레이션 및 실제 로봇 벤치마크에서 SmolVLA를 평가하고 모든 코드, 사전 학습된 모델 및 학습 데이터를 공개합니다.

## 핵심 내용
대규모 멀티모달 데이터셋으로 사전 학습된 비전-언어 모델(VLM)은 풍부한 시각 및 언어 지식을 인코딩하여 로봇 공학의 강력한 기반이 됩니다. 최근 접근법은 로봇 정책을 처음부터 학습하는 대신 VLM을 비전-언어-행동(VLA) 모델로 변환하여 자연어 기반의 인식 및 제어를 가능하게 합니다. 그러나 기존 VLA는 일반적으로 수십억 개의 매개변수를 가진 거대한 모델로, 높은 학습 비용과 제한된 실제 배포 가능성을 초래합니다. 또한 학술 및 산업 데이터셋에 의존하며, 저렴한 로봇 플랫폼에서 수집된 커뮤니티 데이터의 증가하는 가용성을 간과합니다. 본 연구에서는 경쟁력 있는 성능을 유지하면서 학습 및 추론 비용을 획기적으로 줄인 소형, 효율적, 커뮤니티 기반 VLA인 SmolVLA를 제시합니다. SmolVLA는 단일 GPU에서 학습되고 소비자용 GPU 또는 CPU에서 배포되도록 설계되었습니다. 응답성을 더욱 개선하기 위해 인식 및 행동 예측을 행동 실행에서 분리하는 비동기 추론 스택을 도입하여 청크 단위 행동 생성으로 더 높은 제어 속도를 가능하게 합니다. 작은 크기에도 불구하고 SmolVLA는 10배 더 큰 VLA와 비교할 수 있는 성능을 달성합니다. 우리는 시뮬레이션 및 실제 로봇 벤치마크에서 SmolVLA를 평가하고 모든 코드, 사전 학습된 모델 및 학습 데이터를 공개합니다.
