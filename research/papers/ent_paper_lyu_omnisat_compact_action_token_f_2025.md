---
$id: ent_paper_lyu_omnisat_compact_action_token_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniSAT: Compact Action Token, Faster Auto Regression'
  zh: OmniSAT
  ko: 'OmniSAT: Compact Action Token, Faster Auto Regression'
summary:
  en: 'OmniSAT: Compact Action Token, Faster Auto Regression (OmniSAT), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by University of Science and Technology of China.'
  zh: 'OmniSAT: Compact Action Token, Faster Auto Regression (OmniSAT), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by University of Science and Technology of China.'
  ko: 'OmniSAT: Compact Action Token, Faster Auto Regression (OmniSAT), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by University of Science and Technology of China.'
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
- omnisat
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.09667v1.
sources:
- id: src_001
  type: paper
  title: 'OmniSAT: Compact Action Token, Faster Auto Regression (arXiv)'
  url: https://arxiv.org/abs/2510.09667
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OmniSAT source
  url: https://doi.org/10.48550/arXiv.2510.09667
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Existing Vision-Language-Action (VLA) models can be broadly categorized into diffusion-based and auto-regressive (AR) approaches: diffusion models capture continuous action distributions but rely on computationally heavy iterative denoising. In contrast, AR models enable efficient optimization and flexible sequence construction, making them better suited for large-scale pretraining. To further improve AR efficiency, particularly when action chunks induce extended and high-dimensional sequences, prior work applies entropy-guided and token-frequency techniques to shorten the sequence length. However, such compression struggled with \textit{poor reconstruction or inefficient compression}. Motivated by this, we introduce an Omni Swift Action Tokenizer, which learns a compact, transferable action representation. Specifically, we first normalize value ranges and temporal horizons to obtain a consistent representation with B-Spline encoding. Then, we apply multi-stage residual quantization to the position, rotation, and gripper subspaces, producing compressed discrete tokens with coarse-to-fine granularity for each part. After pre-training on the large-scale dataset Droid, the resulting discrete tokenization shortens the training sequence by 6.8$\times$, and lowers the target entropy. To further explore the potential of OmniSAT, we develop a cross-embodiment learning strategy that builds on the unified action-pattern space and jointly leverages robot and human demonstrations. It enables scalable auxiliary supervision from heterogeneous egocentric videos. Across diverse real-robot and simulation experiments, OmniSAT encompasses higher compression while preserving reconstruction quality, enabling faster AR training convergence and model performance.

## 核心内容
Existing Vision-Language-Action (VLA) models can be broadly categorized into diffusion-based and auto-regressive (AR) approaches: diffusion models capture continuous action distributions but rely on computationally heavy iterative denoising. In contrast, AR models enable efficient optimization and flexible sequence construction, making them better suited for large-scale pretraining. To further improve AR efficiency, particularly when action chunks induce extended and high-dimensional sequences, prior work applies entropy-guided and token-frequency techniques to shorten the sequence length. However, such compression struggled with \textit{poor reconstruction or inefficient compression}. Motivated by this, we introduce an Omni Swift Action Tokenizer, which learns a compact, transferable action representation. Specifically, we first normalize value ranges and temporal horizons to obtain a consistent representation with B-Spline encoding. Then, we apply multi-stage residual quantization to the position, rotation, and gripper subspaces, producing compressed discrete tokens with coarse-to-fine granularity for each part. After pre-training on the large-scale dataset Droid, the resulting discrete tokenization shortens the training sequence by 6.8$\times$, and lowers the target entropy. To further explore the potential of OmniSAT, we develop a cross-embodiment learning strategy that builds on the unified action-pattern space and jointly leverages robot and human demonstrations. It enables scalable auxiliary supervision from heterogeneous egocentric videos. Across diverse real-robot and simulation experiments, OmniSAT encompasses higher compression while preserving reconstruction quality, enabling faster AR training convergence and model performance.

## 参考
- http://arxiv.org/abs/2510.09667v1

## Overview
Existing Vision-Language-Action (VLA) models can be broadly categorized into diffusion-based and auto-regressive (AR) approaches: diffusion models capture continuous action distributions but rely on computationally heavy iterative denoising. In contrast, AR models enable efficient optimization and flexible sequence construction, making them better suited for large-scale pretraining. To further improve AR efficiency, particularly when action chunks induce extended and high-dimensional sequences, prior work applies entropy-guided and token-frequency techniques to shorten the sequence length. However, such compression struggled with \textit{poor reconstruction or inefficient compression}. Motivated by this, we introduce an Omni Swift Action Tokenizer, which learns a compact, transferable action representation. Specifically, we first normalize value ranges and temporal horizons to obtain a consistent representation with B-Spline encoding. Then, we apply multi-stage residual quantization to the position, rotation, and gripper subspaces, producing compressed discrete tokens with coarse-to-fine granularity for each part. After pre-training on the large-scale dataset Droid, the resulting discrete tokenization shortens the training sequence by 6.8$\times$, and lowers the target entropy. To further explore the potential of OmniSAT, we develop a cross-embodiment learning strategy that builds on the unified action-pattern space and jointly leverages robot and human demonstrations. It enables scalable auxiliary supervision from heterogeneous egocentric videos. Across diverse real-robot and simulation experiments, OmniSAT encompasses higher compression while preserving reconstruction quality, enabling faster AR training convergence and model performance.

## Content
Existing Vision-Language-Action (VLA) models can be broadly categorized into diffusion-based and auto-regressive (AR) approaches: diffusion models capture continuous action distributions but rely on computationally heavy iterative denoising. In contrast, AR models enable efficient optimization and flexible sequence construction, making them better suited for large-scale pretraining. To further improve AR efficiency, particularly when action chunks induce extended and high-dimensional sequences, prior work applies entropy-guided and token-frequency techniques to shorten the sequence length. However, such compression struggled with \textit{poor reconstruction or inefficient compression}. Motivated by this, we introduce an Omni Swift Action Tokenizer, which learns a compact, transferable action representation. Specifically, we first normalize value ranges and temporal horizons to obtain a consistent representation with B-Spline encoding. Then, we apply multi-stage residual quantization to the position, rotation, and gripper subspaces, producing compressed discrete tokens with coarse-to-fine granularity for each part. After pre-training on the large-scale dataset Droid, the resulting discrete tokenization shortens the training sequence by 6.8$\times$, and lowers the target entropy. To further explore the potential of OmniSAT, we develop a cross-embodiment learning strategy that builds on the unified action-pattern space and jointly leverages robot and human demonstrations. It enables scalable auxiliary supervision from heterogeneous egocentric videos. Across diverse real-robot and simulation experiments, OmniSAT encompasses higher compression while preserving reconstruction quality, enabling faster AR training convergence and model performance.

## 개요
기존의 Vision-Language-Action (VLA) 모델은 크게 확산 기반(diffusion-based)과 자기회귀(auto-regressive, AR) 접근법으로 분류할 수 있습니다. 확산 모델은 연속적인 행동 분포를 포착하지만 계산량이 많은 반복적 잡음 제거에 의존합니다. 반면, AR 모델은 효율적인 최적화와 유연한 시퀀스 구성을 가능하게 하여 대규모 사전 학습에 더 적합합니다. 특히 행동 청크(action chunk)가 길고 고차원적인 시퀀스를 유발할 때 AR 효율성을 더욱 개선하기 위해, 기존 연구는 엔트로피 기반 및 토큰 빈도 기법을 적용하여 시퀀스 길이를 단축했습니다. 그러나 이러한 압축은 \textit{재구성 성능 저하 또는 비효율적인 압축}이라는 문제를 겪었습니다. 이에 착안하여, 우리는 Omni Swift Action Tokenizer를 소개합니다. 이는 간결하고 전이 가능한 행동 표현을 학습합니다. 구체적으로, 먼저 값 범위와 시간적 지평을 정규화하여 B-Spline 인코딩으로 일관된 표현을 얻습니다. 그런 다음, 위치, 회전, 그리퍼 하위 공간에 다단계 잔차 양자화(multi-stage residual quantization)를 적용하여 각 부분에 대해 거친 수준에서 세밀한 수준까지의 압축된 이산 토큰을 생성합니다. 대규모 데이터셋 Droid에서 사전 학습한 결과, 생성된 이산 토큰화는 학습 시퀀스를 6.8배 단축하고 목표 엔트로피를 낮춥니다. OmniSAT의 잠재력을 더 탐구하기 위해, 통합된 행동 패턴 공간을 기반으로 하고 로봇 및 인간 시연을 공동으로 활용하는 교차 체현 학습 전략(cross-embodiment learning strategy)을 개발합니다. 이를 통해 이질적인 자기중심적 비디오(heterogeneous egocentric videos)로부터 확장 가능한 보조 감독을 가능하게 합니다. 다양한 실제 로봇 및 시뮬레이션 실험에서 OmniSAT은 재구성 품질을 유지하면서 더 높은 압축률을 제공하여, 더 빠른 AR 학습 수렴과 모델 성능을 가능하게 합니다.

## 핵심 내용
기존의 Vision-Language-Action (VLA) 모델은 크게 확산 기반(diffusion-based)과 자기회귀(auto-regressive, AR) 접근법으로 분류할 수 있습니다. 확산 모델은 연속적인 행동 분포를 포착하지만 계산량이 많은 반복적 잡음 제거에 의존합니다. 반면, AR 모델은 효율적인 최적화와 유연한 시퀀스 구성을 가능하게 하여 대규모 사전 학습에 더 적합합니다. 특히 행동 청크(action chunk)가 길고 고차원적인 시퀀스를 유발할 때 AR 효율성을 더욱 개선하기 위해, 기존 연구는 엔트로피 기반 및 토큰 빈도 기법을 적용하여 시퀀스 길이를 단축했습니다. 그러나 이러한 압축은 \textit{재구성 성능 저하 또는 비효율적인 압축}이라는 문제를 겪었습니다. 이에 착안하여, 우리는 Omni Swift Action Tokenizer를 소개합니다. 이는 간결하고 전이 가능한 행동 표현을 학습합니다. 구체적으로, 먼저 값 범위와 시간적 지평을 정규화하여 B-Spline 인코딩으로 일관된 표현을 얻습니다. 그런 다음, 위치, 회전, 그리퍼 하위 공간에 다단계 잔차 양자화(multi-stage residual quantization)를 적용하여 각 부분에 대해 거친 수준에서 세밀한 수준까지의 압축된 이산 토큰을 생성합니다. 대규모 데이터셋 Droid에서 사전 학습한 결과, 생성된 이산 토큰화는 학습 시퀀스를 6.8배 단축하고 목표 엔트로피를 낮춥니다. OmniSAT의 잠재력을 더 탐구하기 위해, 통합된 행동 패턴 공간을 기반으로 하고 로봇 및 인간 시연을 공동으로 활용하는 교차 체현 학습 전략(cross-embodiment learning strategy)을 개발합니다. 이를 통해 이질적인 자기중심적 비디오(heterogeneous egocentric videos)로부터 확장 가능한 보조 감독을 가능하게 합니다. 다양한 실제 로봇 및 시뮬레이션 실험에서 OmniSAT은 재구성 품질을 유지하면서 더 높은 압축률을 제공하여, 더 빠른 AR 학습 수렴과 모델 성능을 가능하게 합니다.
