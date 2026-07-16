---
$id: ent_paper_guo_glad_geometric_latent_distilla_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GLaD: Geometric Latent Distillation for Vision-Language-Action Models'
  zh: GLaD
  ko: 'GLaD: Geometric Latent Distillation for Vision-Language-Action Models'
summary:
  en: 'GLaD: Geometric Latent Distillation for Vision-Language-Action Models (GLaD), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by MBZUAI, University of Illinois Chicago.'
  zh: 'GLaD: Geometric Latent Distillation for Vision-Language-Action Models (GLaD), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by MBZUAI, University of Illinois Chicago.'
  ko: 'GLaD: Geometric Latent Distillation for Vision-Language-Action Models (GLaD), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by MBZUAI, University of Illinois Chicago.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- glad
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.09619v1.
sources:
- id: src_001
  type: paper
  title: 'GLaD: Geometric Latent Distillation for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2512.09619
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: GLaD source
  url: https://doi.org/10.48550/arXiv.2512.09619
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Most existing Vision-Language-Action (VLA) models rely primarily on RGB information, while ignoring geometric cues crucial for spatial reasoning and manipulation. In this work, we introduce GLaD, a geometry-aware VLA framework that incorporates 3D geometric priors during pretraining through knowledge distillation. Rather than distilling geometric features solely into the vision encoder, we align the LLM's hidden states corresponding to visual tokens with features from a frozen geometry-aware vision transformer (VGGT), ensuring that geometric understanding is deeply integrated into the multimodal representations that drive action prediction. Pretrained on the Bridge dataset with this geometry distillation mechanism, GLaD achieves 94.1% average success rate across four LIBERO task suites, outperforming UniVLA (92.5%) which uses identical pretraining data. These results validate that geometry-aware pretraining enhances spatial reasoning and policy generalization without requiring explicit depth sensors or 3D annotations.

## 核心内容
Most existing Vision-Language-Action (VLA) models rely primarily on RGB information, while ignoring geometric cues crucial for spatial reasoning and manipulation. In this work, we introduce GLaD, a geometry-aware VLA framework that incorporates 3D geometric priors during pretraining through knowledge distillation. Rather than distilling geometric features solely into the vision encoder, we align the LLM's hidden states corresponding to visual tokens with features from a frozen geometry-aware vision transformer (VGGT), ensuring that geometric understanding is deeply integrated into the multimodal representations that drive action prediction. Pretrained on the Bridge dataset with this geometry distillation mechanism, GLaD achieves 94.1% average success rate across four LIBERO task suites, outperforming UniVLA (92.5%) which uses identical pretraining data. These results validate that geometry-aware pretraining enhances spatial reasoning and policy generalization without requiring explicit depth sensors or 3D annotations.

## 参考
- http://arxiv.org/abs/2512.09619v1

## Overview
Most existing Vision-Language-Action (VLA) models rely primarily on RGB information, while ignoring geometric cues crucial for spatial reasoning and manipulation. In this work, we introduce GLaD, a geometry-aware VLA framework that incorporates 3D geometric priors during pretraining through knowledge distillation. Rather than distilling geometric features solely into the vision encoder, we align the LLM's hidden states corresponding to visual tokens with features from a frozen geometry-aware vision transformer (VGGT), ensuring that geometric understanding is deeply integrated into the multimodal representations that drive action prediction. Pretrained on the Bridge dataset with this geometry distillation mechanism, GLaD achieves 94.1% average success rate across four LIBERO task suites, outperforming UniVLA (92.5%) which uses identical pretraining data. These results validate that geometry-aware pretraining enhances spatial reasoning and policy generalization without requiring explicit depth sensors or 3D annotations.

## Content
Most existing Vision-Language-Action (VLA) models rely primarily on RGB information, while ignoring geometric cues crucial for spatial reasoning and manipulation. In this work, we introduce GLaD, a geometry-aware VLA framework that incorporates 3D geometric priors during pretraining through knowledge distillation. Rather than distilling geometric features solely into the vision encoder, we align the LLM's hidden states corresponding to visual tokens with features from a frozen geometry-aware vision transformer (VGGT), ensuring that geometric understanding is deeply integrated into the multimodal representations that drive action prediction. Pretrained on the Bridge dataset with this geometry distillation mechanism, GLaD achieves 94.1% average success rate across four LIBERO task suites, outperforming UniVLA (92.5%) which uses identical pretraining data. These results validate that geometry-aware pretraining enhances spatial reasoning and policy generalization without requiring explicit depth sensors or 3D annotations.

## 개요
대부분의 기존 Vision-Language-Action (VLA) 모델은 주로 RGB 정보에 의존하며, 공간 추론 및 조작에 중요한 기하학적 단서를 무시합니다. 본 연구에서는 지식 증류를 통해 사전 학습 중 3D 기하학적 사전 지식을 통합하는 기하학 인식 VLA 프레임워크인 GLaD를 소개합니다. 기하학적 특징을 시각 인코더에만 증류하는 대신, 시각 토큰에 해당하는 LLM의 은닉 상태를 고정된 기하학 인식 비전 트랜스포머(VGGT)의 특징과 정렬하여, 행동 예측을 구동하는 다중 모달 표현에 기하학적 이해가 깊이 통합되도록 합니다. 이 기하학 증류 메커니즘으로 Bridge 데이터셋에서 사전 학습된 GLaD는 네 가지 LIBERO 작업 제품군에서 평균 94.1%의 성공률을 달성하여, 동일한 사전 학습 데이터를 사용하는 UniVLA(92.5%)를 능가합니다. 이러한 결과는 기하학 인식 사전 학습이 명시적인 깊이 센서나 3D 주석 없이도 공간 추론 및 정책 일반화를 향상시킴을 입증합니다.

## 핵심 내용
대부분의 기존 Vision-Language-Action (VLA) 모델은 주로 RGB 정보에 의존하며, 공간 추론 및 조작에 중요한 기하학적 단서를 무시합니다. 본 연구에서는 지식 증류를 통해 사전 학습 중 3D 기하학적 사전 지식을 통합하는 기하학 인식 VLA 프레임워크인 GLaD를 소개합니다. 기하학적 특징을 시각 인코더에만 증류하는 대신, 시각 토큰에 해당하는 LLM의 은닉 상태를 고정된 기하학 인식 비전 트랜스포머(VGGT)의 특징과 정렬하여, 행동 예측을 구동하는 다중 모달 표현에 기하학적 이해가 깊이 통합되도록 합니다. 이 기하학 증류 메커니즘으로 Bridge 데이터셋에서 사전 학습된 GLaD는 네 가지 LIBERO 작업 제품군에서 평균 94.1%의 성공률을 달성하여, 동일한 사전 학습 데이터를 사용하는 UniVLA(92.5%)를 능가합니다. 이러한 결과는 기하학 인식 사전 학습이 명시적인 깊이 센서나 3D 주석 없이도 공간 추론 및 정책 일반화를 향상시킴을 입증합니다.
