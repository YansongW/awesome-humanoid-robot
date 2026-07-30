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
  zh: Unified-IO 2 是 Allen Institute for AI、伊利诺伊大学厄巴纳-香槟分校和华盛顿大学于 2023 年提出的首个自回归多模态模型，能够同时理解和生成图像、文本、音频与动作。其核心贡献在于通过统一的 token
    化空间和单编码器-解码器 Transformer 架构，在超过 35 个基准上取得领先性能，包括 GRIT 基准和机器人操作任务。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2312.17172v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: Unified-IO 2 source
  url: https://doi.org/10.1109/CVPR52733.2024.02497
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Unified-IO 2 将图像、文本、音频、动作、边界框等多种模态的输入输出 token 化到共享语义空间，由单一编码器-解码器 Transformer 模型处理。为应对多模态训练的挑战，研究团队提出了多项架构改进以稳定训练过程，并采用多模态去噪目标从零开始在大规模预训练语料上训练。随后，模型在 120 个数据集的集成上通过提示和增强进行微调，学习遵循多模态指令等广泛技能。最终，Unified-IO 2 在 GRIT 基准上达到最先进水平，并在图像生成与理解、自然语言理解、视频与音频理解以及机器人操作等 35 多个基准上取得强劲结果。

## 核心内容
### 方法
- Unified-IO 2 采用自回归架构，将图像、文本、音频、动作、边界框等所有模态的输入和输出 token 化到共享语义空间。
- 模型基于单一编码器-解码器 Transformer 架构，处理统一后的 token 序列。

### 架构改进
- 为应对多模态训练的稳定性挑战，研究团队提出了多种架构改进，具体细节未在摘要中展开，但旨在稳定训练过程。

### 训练设置
- 模型从零开始训练，使用大规模多模态预训练语料，数据来源多样。
- 训练目标采用多模态去噪混合（multimodal mixture of denoisers objective）。
- 为学习广泛技能（如遵循多模态指令），模型在 120 个数据集的集成上进行微调，并应用提示和增强。

### 关键数字与结果
- Unified-IO 2 在 GRIT 基准上达到最先进性能。
- 在超过 35 个基准上取得强劲结果，涵盖：
  - 图像生成与理解
  - 自然语言理解
  - 视频与音频理解
  - 机器人操作

### 结论
- 单一统一模型即可在多个模态和任务上实现领先性能，展示了多模态自回归建模的潜力。
- 所有模型已向研究社区开源。

## Overview
We present Unified-IO 2, the first autoregressive multimodal model that is capable of understanding and generating image, text, audio, and action. To unify different modalities, we tokenize inputs and outputs -- images, text, audio, action, bounding boxes, etc., into a shared semantic space and then process them with a single encoder-decoder transformer model. Since training with such diverse modalities is challenging, we propose various architectural improvements to stabilize model training. We train our model from scratch on a large multimodal pre-training corpus from diverse sources with a multimodal mixture of denoisers objective. To learn an expansive set of skills, such as following multimodal instructions, we construct and finetune on an ensemble of 120 datasets with prompts and augmentations. With a single unified model, Unified-IO 2 achieves state-of-the-art performance on the GRIT benchmark and strong results in more than 35 benchmarks, including image generation and understanding, natural language understanding, video and audio understanding, and robotic manipulation. We release all our models to the research community.

## 개요
본 논문에서는 이미지, 텍스트, 오디오 및 행동을 이해하고 생성할 수 있는 최초의 자기회귀 멀티모달 모델인 Unified-IO 2를 제시합니다. 다양한 모달리티를 통합하기 위해 이미지, 텍스트, 오디오, 행동, 바운딩 박스 등의 입력과 출력을 공유 의미 공간으로 토큰화한 후 단일 인코더-디코더 트랜스포머 모델로 처리합니다. 이러한 다양한 모달리티로 학습하는 것은 까다롭기 때문에, 모델 학습을 안정화하기 위한 다양한 아키텍처 개선 사항을 제안합니다. 다양한 소스의 대규모 멀티모달 사전 학습 코퍼스에서 멀티모달 잡음 제거기 목적 함수를 혼합하여 모델을 처음부터 학습시킵니다. 멀티모달 지시사항 따르기와 같은 광범위한 기술 세트를 학습하기 위해 프롬프트와 증강을 포함한 120개 데이터셋 앙상블을 구축하고 미세 조정합니다. 단일 통합 모델로 Unified-IO 2는 GRIT 벤치마크에서 최첨단 성능을 달성하고, 이미지 생성 및 이해, 자연어 이해, 비디오 및 오디오 이해, 로봇 조작을 포함한 35개 이상의 벤치마크에서 강력한 결과를 보여줍니다. 모든 모델을 연구 커뮤니티에 공개합니다.

## 핵심 내용
본 논문에서는 이미지, 텍스트, 오디오 및 행동을 이해하고 생성할 수 있는 최초의 자기회귀 멀티모달 모델인 Unified-IO 2를 제시합니다. 다양한 모달리티를 통합하기 위해 이미지, 텍스트, 오디오, 행동, 바운딩 박스 등의 입력과 출력을 공유 의미 공간으로 토큰화한 후 단일 인코더-디코더 트랜스포머 모델로 처리합니다. 이러한 다양한 모달리티로 학습하는 것은 까다롭기 때문에, 모델 학습을 안정화하기 위한 다양한 아키텍처 개선 사항을 제안합니다. 다양한 소스의 대규모 멀티모달 사전 학습 코퍼스에서 멀티모달 잡음 제거기 목적 함수를 혼합하여 모델을 처음부터 학습시킵니다. 멀티모달 지시사항 따르기와 같은 광범위한 기술 세트를 학습하기 위해 프롬프트와 증강을 포함한 120개 데이터셋 앙상블을 구축하고 미세 조정합니다. 단일 통합 모델로 Unified-IO 2는 GRIT 벤치마크에서 최첨단 성능을 달성하고, 이미지 생성 및 이해, 자연어 이해, 비디오 및 오디오 이해, 로봇 조작을 포함한 35개 이상의 벤치마크에서 강력한 결과를 보여줍니다. 모든 모델을 연구 커뮤니티에 공개합니다.

## 参考
- http://arxiv.org/abs/2312.17172v1
