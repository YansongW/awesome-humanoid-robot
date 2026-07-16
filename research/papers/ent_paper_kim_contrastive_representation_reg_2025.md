---
$id: ent_paper_kim_contrastive_representation_reg_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Contrastive Representation Regularization for Vision-Language-Action Models
  zh: RS-CL
  ko: Contrastive Representation Regularization for Vision-Language-Action Models
summary:
  en: Contrastive Representation Regularization for Vision-Language-Action Models (RS-CL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by KAIST, UC Berkeley, RLWRLD.
  zh: Contrastive Representation Regularization for Vision-Language-Action Models (RS-CL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by KAIST, UC Berkeley, RLWRLD.
  ko: Contrastive Representation Regularization for Vision-Language-Action Models (RS-CL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by KAIST, UC Berkeley, RLWRLD.
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
- rs_cl
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.01711v4.
sources:
- id: src_001
  type: paper
  title: Contrastive Representation Regularization for Vision-Language-Action Models (arXiv)
  url: https://arxiv.org/abs/2510.01711
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RS-CL source
  url: https://doi.org/10.48550/arXiv.2510.01711
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have shown strong capabilities in robot manipulation by leveraging rich representations from pre-trained Vision-Language Models (VLMs). However, their representations arguably remain suboptimal, lacking sensitivity to robotic signals such as control actions and proprioceptive information. To address the issue, we introduce Robot State-aware Contrastive Loss (RS-CL), a simple and effective representation regularization for VLA models, designed to bridge the gap between VLM representations and robotic signals. In particular, RS-CL aligns the representations more closely with the robot's proprioceptive states by using relative distances between the states as soft supervision. Complementing the original action prediction objective, RS-CL enhances control-relevant representation learning, while being lightweight and fully compatible with standard VLA training pipelines. Our empirical results demonstrate that RS-CL substantially improves the performance of state-of-the-art VLA models; it pushes the prior art to 69.7% achieving the state-of-the-art performance on the RoboCasa-Kitchen benchmark, and boosts success rates from 45.0% to 58.3% on challenging real-robot manipulation tasks.

## 核心内容
Vision-Language-Action (VLA) models have shown strong capabilities in robot manipulation by leveraging rich representations from pre-trained Vision-Language Models (VLMs). However, their representations arguably remain suboptimal, lacking sensitivity to robotic signals such as control actions and proprioceptive information. To address the issue, we introduce Robot State-aware Contrastive Loss (RS-CL), a simple and effective representation regularization for VLA models, designed to bridge the gap between VLM representations and robotic signals. In particular, RS-CL aligns the representations more closely with the robot's proprioceptive states by using relative distances between the states as soft supervision. Complementing the original action prediction objective, RS-CL enhances control-relevant representation learning, while being lightweight and fully compatible with standard VLA training pipelines. Our empirical results demonstrate that RS-CL substantially improves the performance of state-of-the-art VLA models; it pushes the prior art to 69.7% achieving the state-of-the-art performance on the RoboCasa-Kitchen benchmark, and boosts success rates from 45.0% to 58.3% on challenging real-robot manipulation tasks.

## 参考
- http://arxiv.org/abs/2510.01711v4

## Overview
Vision-Language-Action (VLA) models have shown strong capabilities in robot manipulation by leveraging rich representations from pre-trained Vision-Language Models (VLMs). However, their representations arguably remain suboptimal, lacking sensitivity to robotic signals such as control actions and proprioceptive information. To address the issue, we introduce Robot State-aware Contrastive Loss (RS-CL), a simple and effective representation regularization for VLA models, designed to bridge the gap between VLM representations and robotic signals. In particular, RS-CL aligns the representations more closely with the robot's proprioceptive states by using relative distances between the states as soft supervision. Complementing the original action prediction objective, RS-CL enhances control-relevant representation learning, while being lightweight and fully compatible with standard VLA training pipelines. Our empirical results demonstrate that RS-CL substantially improves the performance of state-of-the-art VLA models; it pushes the prior art to 69.7% achieving the state-of-the-art performance on the RoboCasa-Kitchen benchmark, and boosts success rates from 45.0% to 58.3% on challenging real-robot manipulation tasks.

## Content
Vision-Language-Action (VLA) models have shown strong capabilities in robot manipulation by leveraging rich representations from pre-trained Vision-Language Models (VLMs). However, their representations arguably remain suboptimal, lacking sensitivity to robotic signals such as control actions and proprioceptive information. To address the issue, we introduce Robot State-aware Contrastive Loss (RS-CL), a simple and effective representation regularization for VLA models, designed to bridge the gap between VLM representations and robotic signals. In particular, RS-CL aligns the representations more closely with the robot's proprioceptive states by using relative distances between the states as soft supervision. Complementing the original action prediction objective, RS-CL enhances control-relevant representation learning, while being lightweight and fully compatible with standard VLA training pipelines. Our empirical results demonstrate that RS-CL substantially improves the performance of state-of-the-art VLA models; it pushes the prior art to 69.7% achieving the state-of-the-art performance on the RoboCasa-Kitchen benchmark, and boosts success rates from 45.0% to 58.3% on challenging real-robot manipulation tasks.

## 개요
Vision-Language-Action (VLA) 모델은 사전 훈련된 Vision-Language Models (VLM)의 풍부한 표현을 활용하여 로봇 조작에서 강력한 성능을 보여주었습니다. 그러나 이러한 표현은 제어 동작 및 고유 수용 정보와 같은 로봇 신호에 대한 민감성이 부족하여 여전히 최적이 아니라고 할 수 있습니다. 이 문제를 해결하기 위해, 우리는 VLM 표현과 로봇 신호 간의 격차를 해소하도록 설계된 VLA 모델을 위한 간단하면서도 효과적인 표현 정규화 기법인 Robot State-aware Contrastive Loss (RS-CL)를 소개합니다. 특히, RS-CL은 상태 간 상대적 거리를 소프트 감독으로 사용하여 표현을 로봇의 고유 수용 상태와 더 밀접하게 정렬합니다. 원래의 행동 예측 목표를 보완하는 RS-CL은 제어 관련 표현 학습을 향상시키면서도 가볍고 표준 VLA 훈련 파이프라인과 완전히 호환됩니다. 우리의 실험 결과는 RS-CL이 최첨단 VLA 모델의 성능을 크게 향상시킴을 보여줍니다. 이는 RoboCasa-Kitchen 벤치마크에서 이전 기술을 69.7%로 끌어올려 최첨단 성능을 달성하고, 까다로운 실제 로봇 조작 작업에서 성공률을 45.0%에서 58.3%로 향상시킵니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 사전 훈련된 Vision-Language Models (VLM)의 풍부한 표현을 활용하여 로봇 조작에서 강력한 성능을 보여주었습니다. 그러나 이러한 표현은 제어 동작 및 고유 수용 정보와 같은 로봇 신호에 대한 민감성이 부족하여 여전히 최적이 아니라고 할 수 있습니다. 이 문제를 해결하기 위해, 우리는 VLM 표현과 로봇 신호 간의 격차를 해소하도록 설계된 VLA 모델을 위한 간단하면서도 효과적인 표현 정규화 기법인 Robot State-aware Contrastive Loss (RS-CL)를 소개합니다. 특히, RS-CL은 상태 간 상대적 거리를 소프트 감독으로 사용하여 표현을 로봇의 고유 수용 상태와 더 밀접하게 정렬합니다. 원래의 행동 예측 목표를 보완하는 RS-CL은 제어 관련 표현 학습을 향상시키면서도 가볍고 표준 VLA 훈련 파이프라인과 완전히 호환됩니다. 우리의 실험 결과는 RS-CL이 최첨단 VLA 모델의 성능을 크게 향상시킴을 보여줍니다. 이는 RoboCasa-Kitchen 벤치마크에서 이전 기술을 69.7%로 끌어올려 최첨단 성능을 달성하고, 까다로운 실제 로봇 조작 작업에서 성공률을 45.0%에서 58.3%로 향상시킵니다.
