---
$id: ent_paper_unified_video_action_model_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Unified Video Action Model
  zh: Unified Video Action Model
  ko: Unified Video Action Model
summary:
  en: Unified Video Action Model is a 2025 work on manipulation for humanoid robots.
  zh: A unified video and action model holds significant promise for robotics, where videos provide rich scene information
    for action prediction, and actions provide dynamics information for video prediction. However, effectively combining video
    generation and action prediction remains challenging, and current video generation-based methods struggle to match the
    performance of direct policy learning in action accuracy and inference speed. To bridge this gap, we introduce the Unified
    Video Action model (UVA), which jointly optimizes video and action predictions to achieve both high accuracy and effic
  ko: Unified Video Action Model is a 2025 work on manipulation for humanoid robots.
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
- manipulation
- unified_video_action_model
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.00200v3.
sources:
- id: src_001
  type: paper
  title: Unified Video Action Model (arXiv)
  url: https://arxiv.org/abs/2503.00200
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Unified Video Action Model project page
  url: https://unified-video-action-model.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---

## 概述
A unified video and action model holds significant promise for robotics, where videos provide rich scene information for action prediction, and actions provide dynamics information for video prediction. However, effectively combining video generation and action prediction remains challenging, and current video generation-based methods struggle to match the performance of direct policy learning in action accuracy and inference speed. To bridge this gap, we introduce the Unified Video Action model (UVA), which jointly optimizes video and action predictions to achieve both high accuracy and efficient action inference. The key lies in learning a joint video-action latent representation and decoupling video-action decoding. The joint latent representation bridges the visual and action domains, effectively modeling the relationship between video and action sequences. Meanwhile, the decoupled decoding, powered by two lightweight diffusion heads, enables high-speed action inference by bypassing video generation during inference. Such a unified framework further enables versatile functionality through masked input training. By selectively masking actions or videos, a single model can tackle diverse tasks beyond policy learning, such as forward and inverse dynamics modeling and video generation. Via an extensive set of experiments, we demonstrate that UVA can serve as a general-purpose solution for a wide range of robotics tasks, such as policy learning, forward/inverse dynamics and video observation prediction, without compromising performance compared to methods tailored for specific applications. Results are best viewed on https://unified-video-action-model.github.io/.

## 核心内容
A unified video and action model holds significant promise for robotics, where videos provide rich scene information for action prediction, and actions provide dynamics information for video prediction. However, effectively combining video generation and action prediction remains challenging, and current video generation-based methods struggle to match the performance of direct policy learning in action accuracy and inference speed. To bridge this gap, we introduce the Unified Video Action model (UVA), which jointly optimizes video and action predictions to achieve both high accuracy and efficient action inference. The key lies in learning a joint video-action latent representation and decoupling video-action decoding. The joint latent representation bridges the visual and action domains, effectively modeling the relationship between video and action sequences. Meanwhile, the decoupled decoding, powered by two lightweight diffusion heads, enables high-speed action inference by bypassing video generation during inference. Such a unified framework further enables versatile functionality through masked input training. By selectively masking actions or videos, a single model can tackle diverse tasks beyond policy learning, such as forward and inverse dynamics modeling and video generation. Via an extensive set of experiments, we demonstrate that UVA can serve as a general-purpose solution for a wide range of robotics tasks, such as policy learning, forward/inverse dynamics and video observation prediction, without compromising performance compared to methods tailored for specific applications. Results are best viewed on https://unified-video-action-model.github.io/.

## 参考
- http://arxiv.org/abs/2503.00200v3

## Overview
A unified video and action model holds significant promise for robotics, where videos provide rich scene information for action prediction, and actions provide dynamics information for video prediction. However, effectively combining video generation and action prediction remains challenging, and current video generation-based methods struggle to match the performance of direct policy learning in action accuracy and inference speed. To bridge this gap, we introduce the Unified Video Action model (UVA), which jointly optimizes video and action predictions to achieve both high accuracy and efficient action inference. The key lies in learning a joint video-action latent representation and decoupling video-action decoding. The joint latent representation bridges the visual and action domains, effectively modeling the relationship between video and action sequences. Meanwhile, the decoupled decoding, powered by two lightweight diffusion heads, enables high-speed action inference by bypassing video generation during inference. Such a unified framework further enables versatile functionality through masked input training. By selectively masking actions or videos, a single model can tackle diverse tasks beyond policy learning, such as forward and inverse dynamics modeling and video generation. Via an extensive set of experiments, we demonstrate that UVA can serve as a general-purpose solution for a wide range of robotics tasks, such as policy learning, forward/inverse dynamics and video observation prediction, without compromising performance compared to methods tailored for specific applications. Results are best viewed on https://unified-video-action-model.github.io/.

## Content
A unified video and action model holds significant promise for robotics, where videos provide rich scene information for action prediction, and actions provide dynamics information for video prediction. However, effectively combining video generation and action prediction remains challenging, and current video generation-based methods struggle to match the performance of direct policy learning in action accuracy and inference speed. To bridge this gap, we introduce the Unified Video Action model (UVA), which jointly optimizes video and action predictions to achieve both high accuracy and efficient action inference. The key lies in learning a joint video-action latent representation and decoupling video-action decoding. The joint latent representation bridges the visual and action domains, effectively modeling the relationship between video and action sequences. Meanwhile, the decoupled decoding, powered by two lightweight diffusion heads, enables high-speed action inference by bypassing video generation during inference. Such a unified framework further enables versatile functionality through masked input training. By selectively masking actions or videos, a single model can tackle diverse tasks beyond policy learning, such as forward and inverse dynamics modeling and video generation. Via an extensive set of experiments, we demonstrate that UVA can serve as a general-purpose solution for a wide range of robotics tasks, such as policy learning, forward/inverse dynamics and video observation prediction, without compromising performance compared to methods tailored for specific applications. Results are best viewed on https://unified-video-action-model.github.io/.

## 개요
통합 비디오 및 행동 모델은 로보틱스에서 큰 가능성을 지니고 있습니다. 비디오는 행동 예측을 위한 풍부한 장면 정보를 제공하고, 행동은 비디오 예측을 위한 동역학 정보를 제공합니다. 그러나 비디오 생성과 행동 예측을 효과적으로 결합하는 것은 여전히 어려운 과제이며, 현재 비디오 생성 기반 방법은 행동 정확도와 추론 속도에서 직접 정책 학습의 성능을 따라잡기 어렵습니다. 이러한 격차를 해소하기 위해, 우리는 비디오와 행동 예측을 공동으로 최적화하여 높은 정확도와 효율적인 행동 추론을 동시에 달성하는 통합 비디오 행동 모델(UVA)을 소개합니다. 핵심은 공동 비디오-행동 잠재 표현을 학습하고 비디오-행동 디코딩을 분리하는 데 있습니다. 공동 잠재 표현은 시각 및 행동 도메인을 연결하여 비디오와 행동 시퀀스 간의 관계를 효과적으로 모델링합니다. 동시에, 두 개의 경량 확산 헤드로 구동되는 분리된 디코딩은 추론 중 비디오 생성을 우회하여 고속 행동 추론을 가능하게 합니다. 이러한 통합 프레임워크는 마스크 입력 학습을 통해 다기능성을 더욱 향상시킵니다. 행동이나 비디오를 선택적으로 마스킹함으로써, 단일 모델이 정책 학습 외에도 순방향 및 역방향 동역학 모델링, 비디오 생성과 같은 다양한 작업을 처리할 수 있습니다. 광범위한 실험을 통해, UVA가 특정 애플리케이션에 맞춤화된 방법과 비교하여 성능 저하 없이 정책 학습, 순방향/역방향 동역학, 비디오 관측 예측 등 다양한 로보틱스 작업을 위한 범용 솔루션으로 사용될 수 있음을 입증합니다. 결과는 https://unified-video-action-model.github.io/에서 가장 잘 확인할 수 있습니다.

## 핵심 내용
통합 비디오 및 행동 모델은 로보틱스에서 큰 가능성을 지니고 있습니다. 비디오는 행동 예측을 위한 풍부한 장면 정보를 제공하고, 행동은 비디오 예측을 위한 동역학 정보를 제공합니다. 그러나 비디오 생성과 행동 예측을 효과적으로 결합하는 것은 여전히 어려운 과제이며, 현재 비디오 생성 기반 방법은 행동 정확도와 추론 속도에서 직접 정책 학습의 성능을 따라잡기 어렵습니다. 이러한 격차를 해소하기 위해, 우리는 비디오와 행동 예측을 공동으로 최적화하여 높은 정확도와 효율적인 행동 추론을 동시에 달성하는 통합 비디오 행동 모델(UVA)을 소개합니다. 핵심은 공동 비디오-행동 잠재 표현을 학습하고 비디오-행동 디코딩을 분리하는 데 있습니다. 공동 잠재 표현은 시각 및 행동 도메인을 연결하여 비디오와 행동 시퀀스 간의 관계를 효과적으로 모델링합니다. 동시에, 두 개의 경량 확산 헤드로 구동되는 분리된 디코딩은 추론 중 비디오 생성을 우회하여 고속 행동 추론을 가능하게 합니다. 이러한 통합 프레임워크는 마스크 입력 학습을 통해 다기능성을 더욱 향상시킵니다. 행동이나 비디오를 선택적으로 마스킹함으로써, 단일 모델이 정책 학습 외에도 순방향 및 역방향 동역학 모델링, 비디오 생성과 같은 다양한 작업을 처리할 수 있습니다. 광범위한 실험을 통해, UVA가 특정 애플리케이션에 맞춤화된 방법과 비교하여 성능 저하 없이 정책 학습, 순방향/역방향 동역학, 비디오 관측 예측 등 다양한 로보틱스 작업을 위한 범용 솔루션으로 사용될 수 있음을 입증합니다. 결과는 https://unified-video-action-model.github.io/에서 가장 잘 확인할 수 있습니다.
