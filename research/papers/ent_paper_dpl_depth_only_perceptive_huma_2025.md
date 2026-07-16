---
$id: ent_paper_dpl_depth_only_perceptive_huma_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DPL: Depth-only Perceptive Humanoid Locomotion via Realistic Depth Synthesis and Cross-Attention Terrain Reconstruction'
  zh: 'DPL: Depth-only Perceptive Humanoid Locomotion via Realistic Depth Synthesis and Cross-Attention Terrain Reconstruction'
  ko: 'DPL: Depth-only Perceptive Humanoid Locomotion via Realistic Depth Synthesis and Cross-Attention Terrain Reconstruction'
summary:
  en: 'DPL: Depth-only Perceptive Humanoid Locomotion via Realistic Depth Synthesis and Cross-Attention Terrain Reconstruction
    is a 2025 work on locomotion for humanoid robots.'
  zh: 'DPL: Depth-only Perceptive Humanoid Locomotion via Realistic Depth Synthesis and Cross-Attention Terrain Reconstruction
    is a 2025 work on locomotion for humanoid robots.'
  ko: 'DPL: Depth-only Perceptive Humanoid Locomotion via Realistic Depth Synthesis and Cross-Attention Terrain Reconstruction
    is a 2025 work on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dpl
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.07152v2.
sources:
- id: src_001
  type: paper
  title: 'DPL: Depth-only Perceptive Humanoid Locomotion via Realistic Depth Synthesis and Cross-Attention Terrain Reconstruction
    (arXiv)'
  url: https://arxiv.org/abs/2510.07152
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent advancements in legged robot perceptive locomotion have shown promising progress. However, terrain-aware humanoid locomotion remains largely constrained to two paradigms: depth image-based end-to-end learning and elevation map-based methods. The former suffers from limited training efficiency and a significant sim-to-real gap in depth perception, while the latter depends heavily on multiple vision sensors and localization systems, resulting in latency and reduced robustness. To overcome these challenges, we propose a novel framework that tightly integrates three key components: (1) Terrain-Aware Locomotion Policy with a Blind Backbone, which leverages pre-trained elevation map-based perception to guide reinforcement learning with minimal visual input; (2) Multi-Modality Cross-Attention Transformer, which reconstructs structured terrain representations from noisy depth images; (3) Realistic Depth Images Synthetic Method, which employs self-occlusion-aware ray casting and noise-aware modeling to synthesize realistic depth observations, achieving over 30\% reduction in terrain reconstruction error. This combination enables efficient policy training with limited data and hardware resources, while preserving critical terrain features essential for generalization. We validate our framework on a full-sized humanoid robot, demonstrating agile and adaptive locomotion across diverse and challenging terrains.

## 核心内容
Recent advancements in legged robot perceptive locomotion have shown promising progress. However, terrain-aware humanoid locomotion remains largely constrained to two paradigms: depth image-based end-to-end learning and elevation map-based methods. The former suffers from limited training efficiency and a significant sim-to-real gap in depth perception, while the latter depends heavily on multiple vision sensors and localization systems, resulting in latency and reduced robustness. To overcome these challenges, we propose a novel framework that tightly integrates three key components: (1) Terrain-Aware Locomotion Policy with a Blind Backbone, which leverages pre-trained elevation map-based perception to guide reinforcement learning with minimal visual input; (2) Multi-Modality Cross-Attention Transformer, which reconstructs structured terrain representations from noisy depth images; (3) Realistic Depth Images Synthetic Method, which employs self-occlusion-aware ray casting and noise-aware modeling to synthesize realistic depth observations, achieving over 30\% reduction in terrain reconstruction error. This combination enables efficient policy training with limited data and hardware resources, while preserving critical terrain features essential for generalization. We validate our framework on a full-sized humanoid robot, demonstrating agile and adaptive locomotion across diverse and challenging terrains.

## 参考
- http://arxiv.org/abs/2510.07152v2

## Overview
Recent advancements in legged robot perceptive locomotion have shown promising progress. However, terrain-aware humanoid locomotion remains largely constrained to two paradigms: depth image-based end-to-end learning and elevation map-based methods. The former suffers from limited training efficiency and a significant sim-to-real gap in depth perception, while the latter depends heavily on multiple vision sensors and localization systems, resulting in latency and reduced robustness. To overcome these challenges, we propose a novel framework that tightly integrates three key components: (1) Terrain-Aware Locomotion Policy with a Blind Backbone, which leverages pre-trained elevation map-based perception to guide reinforcement learning with minimal visual input; (2) Multi-Modality Cross-Attention Transformer, which reconstructs structured terrain representations from noisy depth images; (3) Realistic Depth Images Synthetic Method, which employs self-occlusion-aware ray casting and noise-aware modeling to synthesize realistic depth observations, achieving over 30% reduction in terrain reconstruction error. This combination enables efficient policy training with limited data and hardware resources, while preserving critical terrain features essential for generalization. We validate our framework on a full-sized humanoid robot, demonstrating agile and adaptive locomotion across diverse and challenging terrains.

## Content
Recent advancements in legged robot perceptive locomotion have shown promising progress. However, terrain-aware humanoid locomotion remains largely constrained to two paradigms: depth image-based end-to-end learning and elevation map-based methods. The former suffers from limited training efficiency and a significant sim-to-real gap in depth perception, while the latter depends heavily on multiple vision sensors and localization systems, resulting in latency and reduced robustness. To overcome these challenges, we propose a novel framework that tightly integrates three key components: (1) Terrain-Aware Locomotion Policy with a Blind Backbone, which leverages pre-trained elevation map-based perception to guide reinforcement learning with minimal visual input; (2) Multi-Modality Cross-Attention Transformer, which reconstructs structured terrain representations from noisy depth images; (3) Realistic Depth Images Synthetic Method, which employs self-occlusion-aware ray casting and noise-aware modeling to synthesize realistic depth observations, achieving over 30% reduction in terrain reconstruction error. This combination enables efficient policy training with limited data and hardware resources, while preserving critical terrain features essential for generalization. We validate our framework on a full-sized humanoid robot, demonstrating agile and adaptive locomotion across diverse and challenging terrains.

## 개요
최근 다리 로봇의 지각적 보행(perceptive locomotion) 분야에서 진전이 있었습니다. 그러나 지형 인식 휴머노이드 보행은 여전히 두 가지 패러다임, 즉 깊이 이미지 기반 종단간 학습과 고도 지도 기반 방법에 크게 제한되어 있습니다. 전자는 훈련 효율성이 낮고 깊이 인식에서 시뮬레이션-실제 간 차이가 크며, 후자는 여러 시각 센서와 위치 추정 시스템에 크게 의존하여 지연 시간과 견고성 저하를 초래합니다. 이러한 문제를 해결하기 위해, 우리는 세 가지 핵심 구성 요소를 긴밀하게 통합한 새로운 프레임워크를 제안합니다: (1) 블라인드 백본을 갖춘 지형 인식 보행 정책(Terrain-Aware Locomotion Policy with a Blind Backbone)으로, 사전 훈련된 고도 지도 기반 인식을 활용하여 최소한의 시각 입력으로 강화 학습을 안내합니다; (2) 다중 모달리티 교차 주의 변환기(Multi-Modality Cross-Attention Transformer)로, 잡음이 있는 깊이 이미지에서 구조화된 지형 표현을 재구성합니다; (3) 현실적인 깊이 이미지 합성 방법(Realistic Depth Images Synthetic Method)으로, 자기 폐색 인식 레이 캐스팅과 잡음 인식 모델링을 사용하여 현실적인 깊이 관측을 합성하며, 지형 재구성 오류를 30% 이상 줄입니다. 이 조합은 제한된 데이터와 하드웨어 자원으로 효율적인 정책 훈련을 가능하게 하면서, 일반화에 필수적인 중요한 지형 특징을 보존합니다. 우리는 이 프레임워크를 실제 크기의 휴머노이드 로봇에서 검증하여, 다양하고 도전적인 지형에서 민첩하고 적응적인 보행을 입증했습니다.

## 핵심 내용
최근 다리 로봇의 지각적 보행(perceptive locomotion) 분야에서 진전이 있었습니다. 그러나 지형 인식 휴머노이드 보행은 여전히 두 가지 패러다임, 즉 깊이 이미지 기반 종단간 학습과 고도 지도 기반 방법에 크게 제한되어 있습니다. 전자는 훈련 효율성이 낮고 깊이 인식에서 시뮬레이션-실제 간 차이가 크며, 후자는 여러 시각 센서와 위치 추정 시스템에 크게 의존하여 지연 시간과 견고성 저하를 초래합니다. 이러한 문제를 해결하기 위해, 우리는 세 가지 핵심 구성 요소를 긴밀하게 통합한 새로운 프레임워크를 제안합니다: (1) 블라인드 백본을 갖춘 지형 인식 보행 정책(Terrain-Aware Locomotion Policy with a Blind Backbone)으로, 사전 훈련된 고도 지도 기반 인식을 활용하여 최소한의 시각 입력으로 강화 학습을 안내합니다; (2) 다중 모달리티 교차 주의 변환기(Multi-Modality Cross-Attention Transformer)로, 잡음이 있는 깊이 이미지에서 구조화된 지형 표현을 재구성합니다; (3) 현실적인 깊이 이미지 합성 방법(Realistic Depth Images Synthetic Method)으로, 자기 폐색 인식 레이 캐스팅과 잡음 인식 모델링을 사용하여 현실적인 깊이 관측을 합성하며, 지형 재구성 오류를 30% 이상 줄입니다. 이 조합은 제한된 데이터와 하드웨어 자원으로 효율적인 정책 훈련을 가능하게 하면서, 일반화에 필수적인 중요한 지형 특징을 보존합니다. 우리는 이 프레임워크를 실제 크기의 휴머노이드 로봇에서 검증하여, 다양하고 도전적인 지형에서 민첩하고 적응적인 보행을 입증했습니다.
