---
$id: ent_paper_humanoid_locomotion_as_next_to_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Humanoid Locomotion as Next Token Prediction
  zh: Humanoid Locomotion as Next Token Prediction
  ko: Humanoid Locomotion as Next Token Prediction
summary:
  en: Humanoid Locomotion as Next Token Prediction is a 2024 work on locomotion for humanoid robots.
  zh: Humanoid Locomotion as Next Token Prediction is a 2024 work on locomotion for humanoid robots.
  ko: Humanoid Locomotion as Next Token Prediction is a 2024 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- humanoid_locomotion_as_next_to
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2402.19469v1.
sources:
- id: src_001
  type: paper
  title: Humanoid Locomotion as Next Token Prediction (arXiv)
  url: https://arxiv.org/abs/2402.19469
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Humanoid Locomotion as Next Token Prediction project page
  url: https://humanoid-next-token-prediction.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
We cast real-world humanoid control as a next token prediction problem, akin to predicting the next word in language. Our model is a causal transformer trained via autoregressive prediction of sensorimotor trajectories. To account for the multi-modal nature of the data, we perform prediction in a modality-aligned way, and for each input token predict the next token from the same modality. This general formulation enables us to leverage data with missing modalities, like video trajectories without actions. We train our model on a collection of simulated trajectories coming from prior neural network policies, model-based controllers, motion capture data, and YouTube videos of humans. We show that our model enables a full-sized humanoid to walk in San Francisco zero-shot. Our model can transfer to the real world even when trained on only 27 hours of walking data, and can generalize to commands not seen during training like walking backward. These findings suggest a promising path toward learning challenging real-world control tasks by generative modeling of sensorimotor trajectories.

## 核心内容
We cast real-world humanoid control as a next token prediction problem, akin to predicting the next word in language. Our model is a causal transformer trained via autoregressive prediction of sensorimotor trajectories. To account for the multi-modal nature of the data, we perform prediction in a modality-aligned way, and for each input token predict the next token from the same modality. This general formulation enables us to leverage data with missing modalities, like video trajectories without actions. We train our model on a collection of simulated trajectories coming from prior neural network policies, model-based controllers, motion capture data, and YouTube videos of humans. We show that our model enables a full-sized humanoid to walk in San Francisco zero-shot. Our model can transfer to the real world even when trained on only 27 hours of walking data, and can generalize to commands not seen during training like walking backward. These findings suggest a promising path toward learning challenging real-world control tasks by generative modeling of sensorimotor trajectories.

## 参考
- http://arxiv.org/abs/2402.19469v1

## Overview
We cast real-world humanoid control as a next token prediction problem, akin to predicting the next word in language. Our model is a causal transformer trained via autoregressive prediction of sensorimotor trajectories. To account for the multi-modal nature of the data, we perform prediction in a modality-aligned way, and for each input token predict the next token from the same modality. This general formulation enables us to leverage data with missing modalities, like video trajectories without actions. We train our model on a collection of simulated trajectories coming from prior neural network policies, model-based controllers, motion capture data, and YouTube videos of humans. We show that our model enables a full-sized humanoid to walk in San Francisco zero-shot. Our model can transfer to the real world even when trained on only 27 hours of walking data, and can generalize to commands not seen during training like walking backward. These findings suggest a promising path toward learning challenging real-world control tasks by generative modeling of sensorimotor trajectories.

## Content
We cast real-world humanoid control as a next token prediction problem, akin to predicting the next word in language. Our model is a causal transformer trained via autoregressive prediction of sensorimotor trajectories. To account for the multi-modal nature of the data, we perform prediction in a modality-aligned way, and for each input token predict the next token from the same modality. This general formulation enables us to leverage data with missing modalities, like video trajectories without actions. We train our model on a collection of simulated trajectories coming from prior neural network policies, model-based controllers, motion capture data, and YouTube videos of humans. We show that our model enables a full-sized humanoid to walk in San Francisco zero-shot. Our model can transfer to the real world even when trained on only 27 hours of walking data, and can generalize to commands not seen during training like walking backward. These findings suggest a promising path toward learning challenging real-world control tasks by generative modeling of sensorimotor trajectories.

## 개요
우리는 실제 세계의 휴머노이드 제어를 언어에서 다음 단어를 예측하는 것과 유사한 다음 토큰 예측 문제로 간주합니다. 우리의 모델은 감각운동 궤적의 자기회귀 예측을 통해 훈련된 인과적 트랜스포머입니다. 데이터의 다중 모달 특성을 고려하기 위해, 우리는 모달리티 정렬 방식으로 예측을 수행하며, 각 입력 토큰에 대해 동일한 모달리티의 다음 토큰을 예측합니다. 이 일반적인 공식화는 행동이 없는 비디오 궤적과 같이 누락된 모달리티가 있는 데이터를 활용할 수 있게 해줍니다. 우리는 이전 신경망 정책, 모델 기반 제어기, 모션 캡처 데이터, 그리고 유튜브 인간 비디오에서 얻은 시뮬레이션 궤적 모음으로 모델을 훈련합니다. 우리의 모델이 샌프란시스코에서 제로샷으로 전신 휴머노이드가 걷는 것을 가능하게 함을 보여줍니다. 이 모델은 단 27시간의 걷기 데이터로 훈련되어도 실제 세계로 전이할 수 있으며, 훈련 중 보지 못한 뒤로 걷기와 같은 명령에도 일반화할 수 있습니다. 이러한 발견은 감각운동 궤적의 생성 모델링을 통해 도전적인 실제 세계 제어 작업을 학습하는 유망한 경로를 제시합니다.

## 핵심 내용
우리는 실제 세계의 휴머노이드 제어를 언어에서 다음 단어를 예측하는 것과 유사한 다음 토큰 예측 문제로 간주합니다. 우리의 모델은 감각운동 궤적의 자기회귀 예측을 통해 훈련된 인과적 트랜스포머입니다. 데이터의 다중 모달 특성을 고려하기 위해, 우리는 모달리티 정렬 방식으로 예측을 수행하며, 각 입력 토큰에 대해 동일한 모달리티의 다음 토큰을 예측합니다. 이 일반적인 공식화는 행동이 없는 비디오 궤적과 같이 누락된 모달리티가 있는 데이터를 활용할 수 있게 해줍니다. 우리는 이전 신경망 정책, 모델 기반 제어기, 모션 캡처 데이터, 그리고 유튜브 인간 비디오에서 얻은 시뮬레이션 궤적 모음으로 모델을 훈련합니다. 우리의 모델이 샌프란시스코에서 제로샷으로 전신 휴머노이드가 걷는 것을 가능하게 함을 보여줍니다. 이 모델은 단 27시간의 걷기 데이터로 훈련되어도 실제 세계로 전이할 수 있으며, 훈련 중 보지 못한 뒤로 걷기와 같은 명령에도 일반화할 수 있습니다. 이러한 발견은 감각운동 궤적의 생성 모델링을 통해 도전적인 실제 세계 제어 작업을 학습하는 유망한 경로를 제시합니다.
