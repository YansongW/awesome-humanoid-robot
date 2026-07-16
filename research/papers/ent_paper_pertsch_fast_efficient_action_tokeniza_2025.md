---
$id: ent_paper_pertsch_fast_efficient_action_tokeniza_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FAST: Efficient Action Tokenization for Vision-Language-Action Models'
  zh: FAST
  ko: 'FAST: Efficient Action Tokenization for Vision-Language-Action Models'
summary:
  en: 'FAST: Efficient Action Tokenization for Vision-Language-Action Models (FAST), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Physical Intelligence, UC Berkeley, Stanford, and published at RSS25.'
  zh: 'FAST: Efficient Action Tokenization for Vision-Language-Action Models (FAST), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Physical Intelligence, UC Berkeley, Stanford, and published at RSS25.'
  ko: 'FAST: Efficient Action Tokenization for Vision-Language-Action Models (FAST), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Physical Intelligence, UC Berkeley, Stanford, and published at RSS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- fast
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2501.09747v1.
sources:
- id: src_001
  type: paper
  title: 'FAST: Efficient Action Tokenization for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2501.09747
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: FAST source
  url: https://doi.org/10.48550/arXiv.2501.09747
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Autoregressive sequence models, such as Transformer-based vision-language action (VLA) policies, can be tremendously effective for capturing complex and generalizable robotic behaviors. However, such models require us to choose a tokenization of our continuous action signals, which determines how the discrete symbols predicted by the model map to continuous robot actions. We find that current approaches for robot action tokenization, based on simple per-dimension, per-timestep binning schemes, typically perform poorly when learning dexterous skills from high-frequency robot data. To address this challenge, we propose a new compression-based tokenization scheme for robot actions, based on the discrete cosine transform. Our tokenization approach, Frequency-space Action Sequence Tokenization (FAST), enables us to train autoregressive VLAs for highly dexterous and high-frequency tasks where standard discretization methods fail completely. Based on FAST, we release FAST+, a universal robot action tokenizer, trained on 1M real robot action trajectories. It can be used as a black-box tokenizer for a wide range of robot action sequences, with diverse action spaces and control frequencies. Finally, we show that, when combined with the pi0 VLA, our method can scale to training on 10k hours of robot data and match the performance of diffusion VLAs, while reducing training time by up to 5x.

## 核心内容
Autoregressive sequence models, such as Transformer-based vision-language action (VLA) policies, can be tremendously effective for capturing complex and generalizable robotic behaviors. However, such models require us to choose a tokenization of our continuous action signals, which determines how the discrete symbols predicted by the model map to continuous robot actions. We find that current approaches for robot action tokenization, based on simple per-dimension, per-timestep binning schemes, typically perform poorly when learning dexterous skills from high-frequency robot data. To address this challenge, we propose a new compression-based tokenization scheme for robot actions, based on the discrete cosine transform. Our tokenization approach, Frequency-space Action Sequence Tokenization (FAST), enables us to train autoregressive VLAs for highly dexterous and high-frequency tasks where standard discretization methods fail completely. Based on FAST, we release FAST+, a universal robot action tokenizer, trained on 1M real robot action trajectories. It can be used as a black-box tokenizer for a wide range of robot action sequences, with diverse action spaces and control frequencies. Finally, we show that, when combined with the pi0 VLA, our method can scale to training on 10k hours of robot data and match the performance of diffusion VLAs, while reducing training time by up to 5x.

## 参考
- http://arxiv.org/abs/2501.09747v1

## Overview
Autoregressive sequence models, such as Transformer-based vision-language action (VLA) policies, can be tremendously effective for capturing complex and generalizable robotic behaviors. However, such models require us to choose a tokenization of our continuous action signals, which determines how the discrete symbols predicted by the model map to continuous robot actions. We find that current approaches for robot action tokenization, based on simple per-dimension, per-timestep binning schemes, typically perform poorly when learning dexterous skills from high-frequency robot data. To address this challenge, we propose a new compression-based tokenization scheme for robot actions, based on the discrete cosine transform. Our tokenization approach, Frequency-space Action Sequence Tokenization (FAST), enables us to train autoregressive VLAs for highly dexterous and high-frequency tasks where standard discretization methods fail completely. Based on FAST, we release FAST+, a universal robot action tokenizer, trained on 1M real robot action trajectories. It can be used as a black-box tokenizer for a wide range of robot action sequences, with diverse action spaces and control frequencies. Finally, we show that, when combined with the pi0 VLA, our method can scale to training on 10k hours of robot data and match the performance of diffusion VLAs, while reducing training time by up to 5x.

## Content
Autoregressive sequence models, such as Transformer-based vision-language action (VLA) policies, can be tremendously effective for capturing complex and generalizable robotic behaviors. However, such models require us to choose a tokenization of our continuous action signals, which determines how the discrete symbols predicted by the model map to continuous robot actions. We find that current approaches for robot action tokenization, based on simple per-dimension, per-timestep binning schemes, typically perform poorly when learning dexterous skills from high-frequency robot data. To address this challenge, we propose a new compression-based tokenization scheme for robot actions, based on the discrete cosine transform. Our tokenization approach, Frequency-space Action Sequence Tokenization (FAST), enables us to train autoregressive VLAs for highly dexterous and high-frequency tasks where standard discretization methods fail completely. Based on FAST, we release FAST+, a universal robot action tokenizer, trained on 1M real robot action trajectories. It can be used as a black-box tokenizer for a wide range of robot action sequences, with diverse action spaces and control frequencies. Finally, we show that, when combined with the pi0 VLA, our method can scale to training on 10k hours of robot data and match the performance of diffusion VLAs, while reducing training time by up to 5x.

## 개요
Transformer 기반의 시각-언어-행동(VLA) 정책과 같은 자기회귀 시퀀스 모델은 복잡하고 일반화 가능한 로봇 동작을 포착하는 데 매우 효과적일 수 있습니다. 그러나 이러한 모델은 연속적인 행동 신호를 토큰화해야 하며, 이는 모델이 예측한 이산 기호가 연속적인 로봇 행동에 어떻게 매핑되는지를 결정합니다. 우리는 단순한 차원별, 시간 단계별 구간화 방식에 기반한 현재의 로봇 행동 토큰화 접근 방식이 고주파 로봇 데이터로부터 정밀한 기술을 학습할 때 일반적으로 성능이 낮다는 것을 발견했습니다. 이 문제를 해결하기 위해, 우리는 이산 코사인 변환에 기반한 새로운 압축 기반 로봇 행동 토큰화 방식을 제안합니다. 우리의 토큰화 접근 방식인 주파수 공간 행동 시퀀스 토큰화(FAST)는 표준 이산화 방법이 완전히 실패하는 고정밀 및 고주파 작업에 대해 자기회귀 VLA를 훈련할 수 있게 해줍니다. FAST를 기반으로, 우리는 100만 개의 실제 로봇 행동 궤적으로 훈련된 범용 로봇 행동 토크나이저인 FAST+를 공개합니다. 이는 다양한 행동 공간과 제어 주파수를 가진 광범위한 로봇 행동 시퀀스에 대해 블랙박스 토크나이저로 사용될 수 있습니다. 마지막으로, 우리의 방법이 pi0 VLA와 결합될 때 10,000시간의 로봇 데이터로 훈련을 확장하고 확산 VLA의 성능과 일치하면서 훈련 시간을 최대 5배까지 줄일 수 있음을 보여줍니다.

## 핵심 내용
Transformer 기반의 시각-언어-행동(VLA) 정책과 같은 자기회귀 시퀀스 모델은 복잡하고 일반화 가능한 로봇 동작을 포착하는 데 매우 효과적일 수 있습니다. 그러나 이러한 모델은 연속적인 행동 신호를 토큰화해야 하며, 이는 모델이 예측한 이산 기호가 연속적인 로봇 행동에 어떻게 매핑되는지를 결정합니다. 우리는 단순한 차원별, 시간 단계별 구간화 방식에 기반한 현재의 로봇 행동 토큰화 접근 방식이 고주파 로봇 데이터로부터 정밀한 기술을 학습할 때 일반적으로 성능이 낮다는 것을 발견했습니다. 이 문제를 해결하기 위해, 우리는 이산 코사인 변환에 기반한 새로운 압축 기반 로봇 행동 토큰화 방식을 제안합니다. 우리의 토큰화 접근 방식인 주파수 공간 행동 시퀀스 토큰화(FAST)는 표준 이산화 방법이 완전히 실패하는 고정밀 및 고주파 작업에 대해 자기회귀 VLA를 훈련할 수 있게 해줍니다. FAST를 기반으로, 우리는 100만 개의 실제 로봇 행동 궤적으로 훈련된 범용 로봇 행동 토크나이저인 FAST+를 공개합니다. 이는 다양한 행동 공간과 제어 주파수를 가진 광범위한 로봇 행동 시퀀스에 대해 블랙박스 토크나이저로 사용될 수 있습니다. 마지막으로, 우리의 방법이 pi0 VLA와 결합될 때 10,000시간의 로봇 데이터로 훈련을 확장하고 확산 VLA의 성능과 일치하면서 훈련 시간을 최대 5배까지 줄일 수 있음을 보여줍니다.
