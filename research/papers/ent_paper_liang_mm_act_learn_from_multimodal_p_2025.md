---
$id: ent_paper_liang_mm_act_learn_from_multimodal_p_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MM-ACT: Learn from Multimodal Parallel Generation to Act'
  zh: MM-ACT
  ko: 'MM-ACT: Learn from Multimodal Parallel Generation to Act'
summary:
  en: 'MM-ACT: Learn from Multimodal Parallel Generation to Act (MM-ACT), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Shanghai AI Laboratory, Shanghai Jiao Tong University, The University of Hong Kong,
    University of Science and Technology of China, Fudan University, Zhejiang University.'
  zh: 'MM-ACT: Learn from Multimodal Parallel Generation to Act (MM-ACT), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Shanghai AI Laboratory, Shanghai Jiao Tong University, The University of Hong Kong,
    University of Science and Technology of China, Fudan University, Zhejiang University.'
  ko: 'MM-ACT: Learn from Multimodal Parallel Generation to Act (MM-ACT), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Shanghai AI Laboratory, Shanghai Jiao Tong University, The University of Hong Kong,
    University of Science and Technology of China, Fudan University, Zhejiang University.'
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
- mm_act
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.00975v2.
sources:
- id: src_001
  type: paper
  title: 'MM-ACT: Learn from Multimodal Parallel Generation to Act (arXiv)'
  url: https://arxiv.org/abs/2512.00975
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MM-ACT source
  url: https://doi.org/10.48550/arXiv.2512.00975
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
A generalist robotic policy needs both semantic understanding for task planning and the ability to interact with the environment through predictive capabilities. To tackle this, we present MM-ACT, a unified Vision-Language-Action (VLA) model that integrates text, image, and action in shared token space and performs generation across all three modalities. MM-ACT adopts a re-mask parallel decoding strategy for text and image generation, and employs a one-step parallel decoding strategy for action generation to improve efficiency. We introduce Context-Shared Multimodal Learning, a unified training paradigm that supervises generation in all three modalities from a shared context, enhancing action generation through cross-modal learning. Experiments were conducted on the LIBERO simulation and Franka real-robot setups as well as RoboTwin2.0 to assess in-domain and out-of-domain performances respectively. Our approach achieves a success rate of 96.3% on LIBERO, 72.0% across three tasks of real Franka, and 52.38% across eight bimanual tasks of RoboTwin2.0 with an additional gain of 9.25% from cross-modal learning. We release our codes, models and data at https://github.com/HHYHRHY/MM-ACT.

## 核心内容
A generalist robotic policy needs both semantic understanding for task planning and the ability to interact with the environment through predictive capabilities. To tackle this, we present MM-ACT, a unified Vision-Language-Action (VLA) model that integrates text, image, and action in shared token space and performs generation across all three modalities. MM-ACT adopts a re-mask parallel decoding strategy for text and image generation, and employs a one-step parallel decoding strategy for action generation to improve efficiency. We introduce Context-Shared Multimodal Learning, a unified training paradigm that supervises generation in all three modalities from a shared context, enhancing action generation through cross-modal learning. Experiments were conducted on the LIBERO simulation and Franka real-robot setups as well as RoboTwin2.0 to assess in-domain and out-of-domain performances respectively. Our approach achieves a success rate of 96.3% on LIBERO, 72.0% across three tasks of real Franka, and 52.38% across eight bimanual tasks of RoboTwin2.0 with an additional gain of 9.25% from cross-modal learning. We release our codes, models and data at https://github.com/HHYHRHY/MM-ACT.

## 参考
- http://arxiv.org/abs/2512.00975v2

## Overview
A generalist robotic policy needs both semantic understanding for task planning and the ability to interact with the environment through predictive capabilities. To tackle this, we present MM-ACT, a unified Vision-Language-Action (VLA) model that integrates text, image, and action in shared token space and performs generation across all three modalities. MM-ACT adopts a re-mask parallel decoding strategy for text and image generation, and employs a one-step parallel decoding strategy for action generation to improve efficiency. We introduce Context-Shared Multimodal Learning, a unified training paradigm that supervises generation in all three modalities from a shared context, enhancing action generation through cross-modal learning. Experiments were conducted on the LIBERO simulation and Franka real-robot setups as well as RoboTwin2.0 to assess in-domain and out-of-domain performances respectively. Our approach achieves a success rate of 96.3% on LIBERO, 72.0% across three tasks of real Franka, and 52.38% across eight bimanual tasks of RoboTwin2.0 with an additional gain of 9.25% from cross-modal learning. We release our codes, models and data at https://github.com/HHYHRHY/MM-ACT.

## Content
A generalist robotic policy needs both semantic understanding for task planning and the ability to interact with the environment through predictive capabilities. To tackle this, we present MM-ACT, a unified Vision-Language-Action (VLA) model that integrates text, image, and action in shared token space and performs generation across all three modalities. MM-ACT adopts a re-mask parallel decoding strategy for text and image generation, and employs a one-step parallel decoding strategy for action generation to improve efficiency. We introduce Context-Shared Multimodal Learning, a unified training paradigm that supervises generation in all three modalities from a shared context, enhancing action generation through cross-modal learning. Experiments were conducted on the LIBERO simulation and Franka real-robot setups as well as RoboTwin2.0 to assess in-domain and out-of-domain performances respectively. Our approach achieves a success rate of 96.3% on LIBERO, 72.0% across three tasks of real Franka, and 52.38% across eight bimanual tasks of RoboTwin2.0 with an additional gain of 9.25% from cross-modal learning. We release our codes, models and data at https://github.com/HHYHRHY/MM-ACT.

## 개요
범용 로봇 정책은 작업 계획을 위한 의미적 이해와 예측 능력을 통한 환경 상호작용 능력을 모두 필요로 합니다. 이를 해결하기 위해, 우리는 텍스트, 이미지, 행동을 공유 토큰 공간에 통합하고 세 가지 모달리티 모두에서 생성을 수행하는 통합 비전-언어-행동(VLA) 모델인 MM-ACT를 제시합니다. MM-ACT는 텍스트 및 이미지 생성을 위해 재마스크 병렬 디코딩 전략을 채택하고, 행동 생성을 위해 단일 단계 병렬 디코딩 전략을 사용하여 효율성을 향상시킵니다. 또한, 공유 컨텍스트에서 세 가지 모달리티 모두의 생성을 감독하는 통합 훈련 패러다임인 컨텍스트 공유 멀티모달 학습(Context-Shared Multimodal Learning)을 도입하여 교차 모달 학습을 통해 행동 생성을 강화합니다. 실험은 LIBERO 시뮬레이션 및 Franka 실제 로봇 환경, 그리고 RoboTwin2.0에서 각각 도메인 내 및 도메인 외 성능을 평가하기 위해 수행되었습니다. 우리의 접근 방식은 LIBERO에서 96.3%, 실제 Franka의 세 가지 작업에서 72.0%, RoboTwin2.0의 여덟 가지 양손 작업에서 52.38%의 성공률을 달성했으며, 교차 모달 학습을 통해 추가로 9.25%의 성능 향상을 얻었습니다. 코드, 모델 및 데이터는 https://github.com/HHYHRHY/MM-ACT에서 공개합니다.

## 핵심 내용
범용 로봇 정책은 작업 계획을 위한 의미적 이해와 예측 능력을 통한 환경 상호작용 능력을 모두 필요로 합니다. 이를 해결하기 위해, 우리는 텍스트, 이미지, 행동을 공유 토큰 공간에 통합하고 세 가지 모달리티 모두에서 생성을 수행하는 통합 비전-언어-행동(VLA) 모델인 MM-ACT를 제시합니다. MM-ACT는 텍스트 및 이미지 생성을 위해 재마스크 병렬 디코딩 전략을 채택하고, 행동 생성을 위해 단일 단계 병렬 디코딩 전략을 사용하여 효율성을 향상시킵니다. 또한, 공유 컨텍스트에서 세 가지 모달리티 모두의 생성을 감독하는 통합 훈련 패러다임인 컨텍스트 공유 멀티모달 학습(Context-Shared Multimodal Learning)을 도입하여 교차 모달 학습을 통해 행동 생성을 강화합니다. 실험은 LIBERO 시뮬레이션 및 Franka 실제 로봇 환경, 그리고 RoboTwin2.0에서 각각 도메인 내 및 도메인 외 성능을 평가하기 위해 수행되었습니다. 우리의 접근 방식은 LIBERO에서 96.3%, 실제 Franka의 세 가지 작업에서 72.0%, RoboTwin2.0의 여덟 가지 양손 작업에서 52.38%의 성공률을 달성했으며, 교차 모달 학습을 통해 추가로 9.25%의 성능 향상을 얻었습니다. 코드, 모델 및 데이터는 https://github.com/HHYHRHY/MM-ACT에서 공개합니다.
