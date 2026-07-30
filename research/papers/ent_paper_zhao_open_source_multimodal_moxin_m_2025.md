---
$id: ent_paper_zhao_open_source_multimodal_moxin_m_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Open-Source Multimodal Moxin Models with Moxin-VLM and Moxin-VLA
  zh: Moxin-VLA
  ko: Open-Source Multimodal Moxin Models with Moxin-VLM and Moxin-VLA
summary:
  en: Open-Source Multimodal Moxin Models with Moxin-VLM and Moxin-VLA (Moxin-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Harvard University.
  zh: Moxin 7B 是由哈佛大学于 2025 年提出的完全开源大语言模型，严格遵循 Model Openness Framework，不仅公开权重，更透明地共享训练、数据集与实现细节。基于该模型衍生出三个变体：Moxin-VLM（视觉语言）、Moxin-VLA（视觉语言动作）和
    Moxin-Chinese（中文能力），其中 Moxin-VLA 专为机器人操作任务设计。实验表明，这些模型在多项评估中均取得优异性能。
  ko: Open-Source Multimodal Moxin Models with Moxin-VLM and Moxin-VLA (Moxin-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Harvard University.
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
- moxin_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.22208v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Open-Source Multimodal Moxin Models with Moxin-VLM and Moxin-VLA (arXiv)
  url: https://arxiv.org/abs/2512.22208
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Moxin-VLA source
  url: https://doi.org/10.48550/arXiv.2512.22208
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Moxin 7B 是一个完全开源的大语言模型，由哈佛大学开发，其核心创新在于遵循 Model Openness Framework，实现了从模型权重到训练数据、实现细节的全面透明化，旨在促进更包容、协作的研究环境。基于 Moxin 7B，团队进一步开发了三个变体：Moxin-VLM 专注于视觉语言任务，Moxin-VLA 面向机器人操作的视觉语言动作任务，Moxin-Chinese 则强化中文能力。所有模型均采用开源框架和公开数据进行训练，并已公开发布模型、可用数据及代码。

## 核心内容
### 背景与动机
近年来，大语言模型（LLMs）经历了显著变革，其流行度和能力迅速提升。专有模型如 GPT-4 和 GPT-o1 凭借卓越性能吸引了广泛关注，而开源模型如 LLaMA 和 Mistral 则因易于定制和部署，推动了 LLMs 的普及。然而，许多开源模型仅共享权重，缺乏训练和数据的透明度。

### Moxin 7B 核心设计
Moxin 7B 是一个完全开源的大语言模型，严格遵循 Model Openness Framework。该框架超越了简单的权重共享，要求完整公开训练过程、数据集和实现细节，从而营造更包容、协作的研究环境，支撑健康的开源生态系统。

### 三个变体
基于 Moxin 7B，团队开发了三个变体：
- **Moxin-VLM**：针对视觉语言任务（vision-language）。
- **Moxin-VLA**：针对视觉语言动作任务（vision-language-action），专用于机器人操作。
- **Moxin-Chinese**：强化中文能力。

### 实验与结果
实验表明，所有模型在多项评估中均取得 superior performance。训练采用开源框架和公开数据，确保可复现性。团队已公开发布模型、可用数据及代码，以推动开源社区发展。

## Overview
Recently, Large Language Models (LLMs) have undergone a significant transformation, marked by a rapid rise in both their popularity and capabilities. Leading this evolution are proprietary LLMs like GPT-4 and GPT-o1, which have captured widespread attention in the AI community due to their remarkable performance and versatility. Simultaneously, open-source LLMs, such as LLaMA and Mistral, have made great contributions to the ever-increasing popularity of LLMs due to the ease to customize and deploy the models across diverse applications. Moxin 7B is introduced as a fully open-source LLM developed in accordance with the Model Openness Framework, which moves beyond the simple sharing of model weights to embrace complete transparency in training, datasets, and implementation detail, thus fostering a more inclusive and collaborative research environment that can sustain a healthy open-source ecosystem. To further equip Moxin with various capabilities in different tasks, we develop three variants based on Moxin, including Moxin-VLM, Moxin-VLA, and Moxin-Chinese, which target the vision-language, vision-language-action, and Chinese capabilities, respectively. Experiments show that our models achieve superior performance in various evaluations. We adopt open-source framework and open data for the training. We release our models, along with the available data and code to derive these models.

## 개요
최근 대규모 언어 모델(LLM)은 인기와 성능 모두에서 급격한 상승을 보이며 중요한 변화를 겪고 있습니다. 이러한 진화를 선도하는 것은 GPT-4 및 GPT-o1과 같은 독점 LLM으로, 이들은 뛰어난 성능과 다재다능함으로 AI 커뮤니티에서 광범위한 주목을 받고 있습니다. 동시에 LLaMA 및 Mistral과 같은 오픈소스 LLM은 다양한 애플리케이션에 걸쳐 모델을 쉽게 맞춤화하고 배포할 수 있어 LLM의 지속적인 인기 상승에 크게 기여했습니다. Moxin 7B는 모델 개방성 프레임워크(Model Openness Framework)에 따라 개발된 완전 오픈소스 LLM으로 소개됩니다. 이는 단순한 모델 가중치 공유를 넘어 훈련, 데이터셋 및 구현 세부 사항에 대한 완전한 투명성을 수용하여 건강한 오픈소스 생태계를 유지할 수 있는 보다 포용적이고 협력적인 연구 환경을 조성합니다. Moxin에 다양한 작업에서의 여러 능력을 추가로 부여하기 위해, 우리는 Moxin을 기반으로 Moxin-VLM, Moxin-VLA, Moxin-Chinese의 세 가지 변형을 개발했습니다. 이들은 각각 시각-언어, 시각-언어-행동 및 중국어 능력을 목표로 합니다. 실험 결과, 우리 모델은 다양한 평가에서 우수한 성능을 달성했습니다. 우리는 훈련을 위해 오픈소스 프레임워크와 공개 데이터를 채택했습니다. 또한 모델과 함께 이러한 모델을 도출하는 데 사용된 데이터 및 코드를 공개합니다.

## 핵심 내용
최근 대규모 언어 모델(LLM)은 인기와 성능 모두에서 급격한 상승을 보이며 중요한 변화를 겪고 있습니다. 이러한 진화를 선도하는 것은 GPT-4 및 GPT-o1과 같은 독점 LLM으로, 이들은 뛰어난 성능과 다재다능함으로 AI 커뮤니티에서 광범위한 주목을 받고 있습니다. 동시에 LLaMA 및 Mistral과 같은 오픈소스 LLM은 다양한 애플리케이션에 걸쳐 모델을 쉽게 맞춤화하고 배포할 수 있어 LLM의 지속적인 인기 상승에 크게 기여했습니다. Moxin 7B는 모델 개방성 프레임워크(Model Openness Framework)에 따라 개발된 완전 오픈소스 LLM으로 소개됩니다. 이는 단순한 모델 가중치 공유를 넘어 훈련, 데이터셋 및 구현 세부 사항에 대한 완전한 투명성을 수용하여 건강한 오픈소스 생태계를 유지할 수 있는 보다 포용적이고 협력적인 연구 환경을 조성합니다. Moxin에 다양한 작업에서의 여러 능력을 추가로 부여하기 위해, 우리는 Moxin을 기반으로 Moxin-VLM, Moxin-VLA, Moxin-Chinese의 세 가지 변형을 개발했습니다. 이들은 각각 시각-언어, 시각-언어-행동 및 중국어 능력을 목표로 합니다. 실험 결과, 우리 모델은 다양한 평가에서 우수한 성능을 달성했습니다. 우리는 훈련을 위해 오픈소스 프레임워크와 공개 데이터를 채택했습니다. 또한 모델과 함께 이러한 모델을 도출하는 데 사용된 데이터 및 코드를 공개합니다.

## 参考
- http://arxiv.org/abs/2512.22208v2
