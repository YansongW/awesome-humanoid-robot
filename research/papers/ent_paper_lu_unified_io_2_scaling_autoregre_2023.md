---
$id: ent_paper_lu_unified_io_2_scaling_autoregre_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Unified-IO 2: Scaling Autoregressive Multimodal Models with Vision, Language, Audio, and Action'
  zh: Unified-IO 2
  ko: 'Unified-IO 2: Scaling Autoregressive Multimodal Models with Vision, Language, Audio, and Action'
summary:
  en: 'Unified-IO 2: Scaling Autoregressive Multimodal Models with Vision, Language, Audio, and Action (Unified-IO 2), is
    a 2023 large vision-language-action model for robotic manipulation, introduced by Allen Institute for AI, University of
    Illinois Urbana-Champaign, University of Washington, and published at CVPR 2023.'
  zh: 'Unified-IO 2: Scaling Autoregressive Multimodal Models with Vision, Language, Audio, and Action (Unified-IO 2), is
    a 2023 large vision-language-action model for robotic manipulation, introduced by Allen Institute for AI, University of
    Illinois Urbana-Champaign, University of Washington, and published at CVPR 2023.'
  ko: 'Unified-IO 2: Scaling Autoregressive Multimodal Models with Vision, Language, Audio, and Action (Unified-IO 2), is
    a 2023 large vision-language-action model for robotic manipulation, introduced by Allen Institute for AI, University of
    Illinois Urbana-Champaign, University of Washington, and published at CVPR 2023.'
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
- unified_io_2
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2312.17172v1.
sources:
- id: src_001
  type: website
  title: Unified-IO 2 source
  url: https://doi.org/10.1109/CVPR52733.2024.02497
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
We present Unified-IO 2, the first autoregressive multimodal model that is capable of understanding and generating image, text, audio, and action. To unify different modalities, we tokenize inputs and outputs -- images, text, audio, action, bounding boxes, etc., into a shared semantic space and then process them with a single encoder-decoder transformer model. Since training with such diverse modalities is challenging, we propose various architectural improvements to stabilize model training. We train our model from scratch on a large multimodal pre-training corpus from diverse sources with a multimodal mixture of denoisers objective. To learn an expansive set of skills, such as following multimodal instructions, we construct and finetune on an ensemble of 120 datasets with prompts and augmentations. With a single unified model, Unified-IO 2 achieves state-of-the-art performance on the GRIT benchmark and strong results in more than 35 benchmarks, including image generation and understanding, natural language understanding, video and audio understanding, and robotic manipulation. We release all our models to the research community.

## 核心内容
We present Unified-IO 2, the first autoregressive multimodal model that is capable of understanding and generating image, text, audio, and action. To unify different modalities, we tokenize inputs and outputs -- images, text, audio, action, bounding boxes, etc., into a shared semantic space and then process them with a single encoder-decoder transformer model. Since training with such diverse modalities is challenging, we propose various architectural improvements to stabilize model training. We train our model from scratch on a large multimodal pre-training corpus from diverse sources with a multimodal mixture of denoisers objective. To learn an expansive set of skills, such as following multimodal instructions, we construct and finetune on an ensemble of 120 datasets with prompts and augmentations. With a single unified model, Unified-IO 2 achieves state-of-the-art performance on the GRIT benchmark and strong results in more than 35 benchmarks, including image generation and understanding, natural language understanding, video and audio understanding, and robotic manipulation. We release all our models to the research community.

## 参考
- http://arxiv.org/abs/2312.17172v1

## Overview
We present Unified-IO 2, the first autoregressive multimodal model that is capable of understanding and generating image, text, audio, and action. To unify different modalities, we tokenize inputs and outputs -- images, text, audio, action, bounding boxes, etc., into a shared semantic space and then process them with a single encoder-decoder transformer model. Since training with such diverse modalities is challenging, we propose various architectural improvements to stabilize model training. We train our model from scratch on a large multimodal pre-training corpus from diverse sources with a multimodal mixture of denoisers objective. To learn an expansive set of skills, such as following multimodal instructions, we construct and finetune on an ensemble of 120 datasets with prompts and augmentations. With a single unified model, Unified-IO 2 achieves state-of-the-art performance on the GRIT benchmark and strong results in more than 35 benchmarks, including image generation and understanding, natural language understanding, video and audio understanding, and robotic manipulation. We release all our models to the research community.

## Content
We present Unified-IO 2, the first autoregressive multimodal model that is capable of understanding and generating image, text, audio, and action. To unify different modalities, we tokenize inputs and outputs -- images, text, audio, action, bounding boxes, etc., into a shared semantic space and then process them with a single encoder-decoder transformer model. Since training with such diverse modalities is challenging, we propose various architectural improvements to stabilize model training. We train our model from scratch on a large multimodal pre-training corpus from diverse sources with a multimodal mixture of denoisers objective. To learn an expansive set of skills, such as following multimodal instructions, we construct and finetune on an ensemble of 120 datasets with prompts and augmentations. With a single unified model, Unified-IO 2 achieves state-of-the-art performance on the GRIT benchmark and strong results in more than 35 benchmarks, including image generation and understanding, natural language understanding, video and audio understanding, and robotic manipulation. We release all our models to the research community.

## 개요
본 논문에서는 이미지, 텍스트, 오디오 및 행동을 이해하고 생성할 수 있는 최초의 자기회귀 멀티모달 모델인 Unified-IO 2를 제시합니다. 다양한 모달리티를 통합하기 위해 이미지, 텍스트, 오디오, 행동, 바운딩 박스 등의 입력과 출력을 공유 의미 공간으로 토큰화한 후 단일 인코더-디코더 트랜스포머 모델로 처리합니다. 이러한 다양한 모달리티로 학습하는 것은 까다롭기 때문에, 모델 학습을 안정화하기 위한 다양한 아키텍처 개선 사항을 제안합니다. 다양한 소스의 대규모 멀티모달 사전 학습 코퍼스에서 멀티모달 잡음 제거기 목적 함수를 혼합하여 모델을 처음부터 학습시킵니다. 멀티모달 지시사항 따르기와 같은 광범위한 기술 세트를 학습하기 위해 프롬프트와 증강을 포함한 120개 데이터셋 앙상블을 구축하고 미세 조정합니다. 단일 통합 모델로 Unified-IO 2는 GRIT 벤치마크에서 최첨단 성능을 달성하고, 이미지 생성 및 이해, 자연어 이해, 비디오 및 오디오 이해, 로봇 조작을 포함한 35개 이상의 벤치마크에서 강력한 결과를 보여줍니다. 모든 모델을 연구 커뮤니티에 공개합니다.

## 핵심 내용
본 논문에서는 이미지, 텍스트, 오디오 및 행동을 이해하고 생성할 수 있는 최초의 자기회귀 멀티모달 모델인 Unified-IO 2를 제시합니다. 다양한 모달리티를 통합하기 위해 이미지, 텍스트, 오디오, 행동, 바운딩 박스 등의 입력과 출력을 공유 의미 공간으로 토큰화한 후 단일 인코더-디코더 트랜스포머 모델로 처리합니다. 이러한 다양한 모달리티로 학습하는 것은 까다롭기 때문에, 모델 학습을 안정화하기 위한 다양한 아키텍처 개선 사항을 제안합니다. 다양한 소스의 대규모 멀티모달 사전 학습 코퍼스에서 멀티모달 잡음 제거기 목적 함수를 혼합하여 모델을 처음부터 학습시킵니다. 멀티모달 지시사항 따르기와 같은 광범위한 기술 세트를 학습하기 위해 프롬프트와 증강을 포함한 120개 데이터셋 앙상블을 구축하고 미세 조정합니다. 단일 통합 모델로 Unified-IO 2는 GRIT 벤치마크에서 최첨단 성능을 달성하고, 이미지 생성 및 이해, 자연어 이해, 비디오 및 오디오 이해, 로봇 조작을 포함한 35개 이상의 벤치마크에서 강력한 결과를 보여줍니다. 모든 모델을 연구 커뮤니티에 공개합니다.
