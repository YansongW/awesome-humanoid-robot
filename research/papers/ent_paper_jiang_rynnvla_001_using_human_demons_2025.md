---
$id: ent_paper_jiang_rynnvla_001_using_human_demons_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RynnVLA-001: Using Human Demonstrations to Improve Robot Manipulation'
  zh: RynnVLA-001
  ko: 'RynnVLA-001: Using Human Demonstrations to Improve Robot Manipulation'
summary:
  en: 'RynnVLA-001: Using Human Demonstrations to Improve Robot Manipulation (RynnVLA-001), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University.'
  zh: 'RynnVLA-001: Using Human Demonstrations to Improve Robot Manipulation (RynnVLA-001), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University.'
  ko: 'RynnVLA-001: Using Human Demonstrations to Improve Robot Manipulation (RynnVLA-001), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University.'
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
- rynnvla_001
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.15212v1.
sources:
- id: src_001
  type: paper
  title: 'RynnVLA-001: Using Human Demonstrations to Improve Robot Manipulation (arXiv)'
  url: https://arxiv.org/abs/2509.15212
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RynnVLA-001 source
  url: https://doi.org/10.48550/arXiv.2509.15212
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This paper presents RynnVLA-001, a vision-language-action(VLA) model built upon large-scale video generative pretraining from human demonstrations. We propose a novel two-stage pretraining methodology. The first stage, Ego-Centric Video Generative Pretraining, trains an Image-to-Video model on 12M ego-centric manipulation videos to predict future frames conditioned on an initial frame and a language instruction. The second stage, Human-Centric Trajectory-Aware Modeling, extends this by jointly predicting future keypoint trajectories, thereby effectively bridging visual frame prediction with action prediction. Furthermore, to enhance action representation, we propose ActionVAE, a variational autoencoder that compresses sequences of actions into compact latent embeddings, reducing the complexity of the VLA output space. When finetuned on the same downstream robotics datasets, RynnVLA-001 achieves superior performance over state-of-the-art baselines, demonstrating that the proposed pretraining strategy provides a more effective initialization for VLA models.

## 核心内容
This paper presents RynnVLA-001, a vision-language-action(VLA) model built upon large-scale video generative pretraining from human demonstrations. We propose a novel two-stage pretraining methodology. The first stage, Ego-Centric Video Generative Pretraining, trains an Image-to-Video model on 12M ego-centric manipulation videos to predict future frames conditioned on an initial frame and a language instruction. The second stage, Human-Centric Trajectory-Aware Modeling, extends this by jointly predicting future keypoint trajectories, thereby effectively bridging visual frame prediction with action prediction. Furthermore, to enhance action representation, we propose ActionVAE, a variational autoencoder that compresses sequences of actions into compact latent embeddings, reducing the complexity of the VLA output space. When finetuned on the same downstream robotics datasets, RynnVLA-001 achieves superior performance over state-of-the-art baselines, demonstrating that the proposed pretraining strategy provides a more effective initialization for VLA models.

## 参考
- http://arxiv.org/abs/2509.15212v1

## Overview
This paper presents RynnVLA-001, a vision-language-action (VLA) model built upon large-scale video generative pretraining from human demonstrations. We propose a novel two-stage pretraining methodology. The first stage, Ego-Centric Video Generative Pretraining, trains an Image-to-Video model on 12M ego-centric manipulation videos to predict future frames conditioned on an initial frame and a language instruction. The second stage, Human-Centric Trajectory-Aware Modeling, extends this by jointly predicting future keypoint trajectories, thereby effectively bridging visual frame prediction with action prediction. Furthermore, to enhance action representation, we propose ActionVAE, a variational autoencoder that compresses sequences of actions into compact latent embeddings, reducing the complexity of the VLA output space. When finetuned on the same downstream robotics datasets, RynnVLA-001 achieves superior performance over state-of-the-art baselines, demonstrating that the proposed pretraining strategy provides a more effective initialization for VLA models.

## Content
This paper presents RynnVLA-001, a vision-language-action (VLA) model built upon large-scale video generative pretraining from human demonstrations. We propose a novel two-stage pretraining methodology. The first stage, Ego-Centric Video Generative Pretraining, trains an Image-to-Video model on 12M ego-centric manipulation videos to predict future frames conditioned on an initial frame and a language instruction. The second stage, Human-Centric Trajectory-Aware Modeling, extends this by jointly predicting future keypoint trajectories, thereby effectively bridging visual frame prediction with action prediction. Furthermore, to enhance action representation, we propose ActionVAE, a variational autoencoder that compresses sequences of actions into compact latent embeddings, reducing the complexity of the VLA output space. When finetuned on the same downstream robotics datasets, RynnVLA-001 achieves superior performance over state-of-the-art baselines, demonstrating that the proposed pretraining strategy provides a more effective initialization for VLA models.

## 개요
본 논문은 인간 시연 데이터를 기반으로 한 대규모 비디오 생성 사전 학습을 통해 구축된 비전-언어-행동(VLA) 모델인 RynnVLA-001을 제시합니다. 우리는 새로운 두 단계 사전 학습 방법론을 제안합니다. 첫 번째 단계인 자아 중심 비디오 생성 사전 학습(Ego-Centric Video Generative Pretraining)은 1,200만 개의 자아 중심 조작 비디오를 사용하여 초기 프레임과 언어 명령을 조건으로 미래 프레임을 예측하는 이미지-투-비디오(Image-to-Video) 모델을 학습합니다. 두 번째 단계인 인간 중심 궤적 인식 모델링(Human-Centric Trajectory-Aware Modeling)은 미래 키포인트 궤적을 공동으로 예측하여 시각적 프레임 예측과 행동 예측을 효과적으로 연결합니다. 또한, 행동 표현을 강화하기 위해 ActionVAE를 제안합니다. 이는 변분 오토인코더로, 행동 시퀀스를 압축된 잠재 임베딩으로 압축하여 VLA 출력 공간의 복잡성을 줄입니다. 동일한 다운스트림 로봇공학 데이터셋에서 미세 조정되었을 때, RynnVLA-001은 최첨단 기준 모델보다 우수한 성능을 달성하며, 제안된 사전 학습 전략이 VLA 모델에 더 효과적인 초기화를 제공함을 입증합니다.

## 핵심 내용
본 논문은 인간 시연 데이터를 기반으로 한 대규모 비디오 생성 사전 학습을 통해 구축된 비전-언어-행동(VLA) 모델인 RynnVLA-001을 제시합니다. 우리는 새로운 두 단계 사전 학습 방법론을 제안합니다. 첫 번째 단계인 자아 중심 비디오 생성 사전 학습(Ego-Centric Video Generative Pretraining)은 1,200만 개의 자아 중심 조작 비디오를 사용하여 초기 프레임과 언어 명령을 조건으로 미래 프레임을 예측하는 이미지-투-비디오(Image-to-Video) 모델을 학습합니다. 두 번째 단계인 인간 중심 궤적 인식 모델링(Human-Centric Trajectory-Aware Modeling)은 미래 키포인트 궤적을 공동으로 예측하여 시각적 프레임 예측과 행동 예측을 효과적으로 연결합니다. 또한, 행동 표현을 강화하기 위해 ActionVAE를 제안합니다. 이는 변분 오토인코더로, 행동 시퀀스를 압축된 잠재 임베딩으로 압축하여 VLA 출력 공간의 복잡성을 줄입니다. 동일한 다운스트림 로봇공학 데이터셋에서 미세 조정되었을 때, RynnVLA-001은 최첨단 기준 모델보다 우수한 성능을 달성하며, 제안된 사전 학습 전략이 VLA 모델에 더 효과적인 초기화를 제공함을 입증합니다.
