---
$id: ent_paper_generative_world_modelling_for_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Generative World Modelling for Humanoids: 1X World Model Challenge Technical Report'
  zh: 'Generative World Modelling for Humanoids: 1X World Model Challenge Technical Report'
  ko: 'Generative World Modelling for Humanoids: 1X World Model Challenge Technical Report'
summary:
  en: 'Generative World Modelling for Humanoids: 1X World Model Challenge Technical Report is a 2025 work on simulation benchmark
    for humanoid robots.'
  zh: 'Generative World Modelling for Humanoids: 1X World Model Challenge Technical Report is a 2025 work on simulation benchmark
    for humanoid robots.'
  ko: 'Generative World Modelling for Humanoids: 1X World Model Challenge Technical Report is a 2025 work on simulation benchmark
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmark
- generative_world_modelling_for
- humanoid
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.07092v1.
sources:
- id: src_001
  type: paper
  title: 'Generative World Modelling for Humanoids: 1X World Model Challenge Technical Report (arXiv)'
  url: https://arxiv.org/abs/2510.07092
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
World models are a powerful paradigm in AI and robotics, enabling agents to reason about the future by predicting visual observations or compact latent states. The 1X World Model Challenge introduces an open-source benchmark of real-world humanoid interaction, with two complementary tracks: sampling, focused on forecasting future image frames, and compression, focused on predicting future discrete latent codes. For the sampling track, we adapt the video generation foundation model Wan-2.2 TI2V-5B to video-state-conditioned future frame prediction. We condition the video generation on robot states using AdaLN-Zero, and further post-train the model using LoRA. For the compression track, we train a Spatio-Temporal Transformer model from scratch. Our models achieve 23.0 dB PSNR in the sampling task and a Top-500 CE of 6.6386 in the compression task, securing 1st place in both challenges.

## 核心内容
World models are a powerful paradigm in AI and robotics, enabling agents to reason about the future by predicting visual observations or compact latent states. The 1X World Model Challenge introduces an open-source benchmark of real-world humanoid interaction, with two complementary tracks: sampling, focused on forecasting future image frames, and compression, focused on predicting future discrete latent codes. For the sampling track, we adapt the video generation foundation model Wan-2.2 TI2V-5B to video-state-conditioned future frame prediction. We condition the video generation on robot states using AdaLN-Zero, and further post-train the model using LoRA. For the compression track, we train a Spatio-Temporal Transformer model from scratch. Our models achieve 23.0 dB PSNR in the sampling task and a Top-500 CE of 6.6386 in the compression task, securing 1st place in both challenges.

## 参考
- http://arxiv.org/abs/2510.07092v1

## Overview
World models are a powerful paradigm in AI and robotics, enabling agents to reason about the future by predicting visual observations or compact latent states. The 1X World Model Challenge introduces an open-source benchmark of real-world humanoid interaction, with two complementary tracks: sampling, focused on forecasting future image frames, and compression, focused on predicting future discrete latent codes. For the sampling track, we adapt the video generation foundation model Wan-2.2 TI2V-5B to video-state-conditioned future frame prediction. We condition the video generation on robot states using AdaLN-Zero, and further post-train the model using LoRA. For the compression track, we train a Spatio-Temporal Transformer model from scratch. Our models achieve 23.0 dB PSNR in the sampling task and a Top-500 CE of 6.6386 in the compression task, securing 1st place in both challenges.

## Content
World models are a powerful paradigm in AI and robotics, enabling agents to reason about the future by predicting visual observations or compact latent states. The 1X World Model Challenge introduces an open-source benchmark of real-world humanoid interaction, with two complementary tracks: sampling, focused on forecasting future image frames, and compression, focused on predicting future discrete latent codes. For the sampling track, we adapt the video generation foundation model Wan-2.2 TI2V-5B to video-state-conditioned future frame prediction. We condition the video generation on robot states using AdaLN-Zero, and further post-train the model using LoRA. For the compression track, we train a Spatio-Temporal Transformer model from scratch. Our models achieve 23.0 dB PSNR in the sampling task and a Top-500 CE of 6.6386 in the compression task, securing 1st place in both challenges.

## 개요
World models는 AI와 로보틱스에서 강력한 패러다임으로, 에이전트가 시각적 관측이나 압축된 잠재 상태를 예측하여 미래에 대해 추론할 수 있게 합니다. 1X World Model Challenge는 실제 인간형 상호작용에 대한 오픈소스 벤치마크를 도입하며, 두 가지 상호 보완적인 트랙을 제공합니다: 미래 이미지 프레임 예측에 초점을 맞춘 샘플링 트랙과 미래 이산 잠재 코드 예측에 초점을 맞춘 압축 트랙입니다. 샘플링 트랙의 경우, 비디오 생성 기반 모델 Wan-2.2 TI2V-5B를 비디오-상태 조건부 미래 프레임 예측에 적용했습니다. AdaLN-Zero를 사용하여 로봇 상태에 비디오 생성을 조건화하고, LoRA를 사용하여 모델을 추가로 사후 학습했습니다. 압축 트랙의 경우, Spatio-Temporal Transformer 모델을 처음부터 학습했습니다. 우리 모델은 샘플링 작업에서 23.0 dB PSNR을, 압축 작업에서 Top-500 CE 6.6386을 달성하여 두 챌린지 모두에서 1위를 차지했습니다.

## 핵심 내용
World models는 AI와 로보틱스에서 강력한 패러다임으로, 에이전트가 시각적 관측이나 압축된 잠재 상태를 예측하여 미래에 대해 추론할 수 있게 합니다. 1X World Model Challenge는 실제 인간형 상호작용에 대한 오픈소스 벤치마크를 도입하며, 두 가지 상호 보완적인 트랙을 제공합니다: 미래 이미지 프레임 예측에 초점을 맞춘 샘플링 트랙과 미래 이산 잠재 코드 예측에 초점을 맞춘 압축 트랙입니다. 샘플링 트랙의 경우, 비디오 생성 기반 모델 Wan-2.2 TI2V-5B를 비디오-상태 조건부 미래 프레임 예측에 적용했습니다. AdaLN-Zero를 사용하여 로봇 상태에 비디오 생성을 조건화하고, LoRA를 사용하여 모델을 추가로 사후 학습했습니다. 압축 트랙의 경우, Spatio-Temporal Transformer 모델을 처음부터 학습했습니다. 우리 모델은 샘플링 작업에서 23.0 dB PSNR을, 압축 작업에서 Top-500 CE 6.6386을 달성하여 두 챌린지 모두에서 1위를 차지했습니다.
