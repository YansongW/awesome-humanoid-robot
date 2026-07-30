---
$id: ent_paper_ye_latent_action_pretraining_from_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Latent Action Pretraining from Videos
  zh: LAPA
  ko: Latent Action Pretraining from Videos
summary:
  en: Latent Action Pretraining from Videos (LAPA), is a 2024 large vision-language-action model for robotic manipulation,
    introduced by KAIST, University of Washington, Microsoft Research, NVIDIA, Allen Institute for AI, and published at ICLR
    2024.
  zh: LAPA 是由 KAIST、华盛顿大学、微软研究院、NVIDIA 和 Allen Institute for AI 于 2024 年提出的无监督视觉-语言-动作模型预训练方法。其核心贡献在于无需真实机器人动作标签，仅从互联网视频中学习离散潜在动作，并在小规模机器人数据微调后显著超越现有方法，实现语言条件操控与语义泛化。
  ko: Latent Action Pretraining from Videos (LAPA), is a 2024 large vision-language-action model for robotic manipulation,
    introduced by KAIST, University of Washington, Microsoft Research, NVIDIA, Allen Institute for AI, and published at ICLR
    2024.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- lapa
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.11758v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: LAPA source
  url: https://openreview.net/forum?id=VYOe2eBQeh
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
LAPA 提出了一种无监督预训练框架，通过 VQ-VAE 目标从无标签视频中学习帧间的离散潜在动作，再预训练一个潜在 VLA 模型来根据观测和任务描述预测这些潜在动作。最后，该方法仅需少量机器人操控数据即可将潜在动作映射为真实机器人动作。实验表明，LAPA 在大规模视频训练中显著优于现有策略，并在需要语言条件、对未见物体泛化以及语义泛化到未见指令的真实世界任务中，超越了使用机器人动作标签训练的 SOTA VLA 模型。仅使用人类操控视频进行训练也展现出正向迁移能力，为利用网络规模数据构建机器人基础模型开辟了道路。

## 核心内容
### 方法架构
LAPA 包含三个关键阶段：
1. **潜在动作量化模型训练**：采用 VQ-VAE 目标，从无标签视频帧序列中学习离散潜在动作。该模型将连续图像帧间的变化编码为有限数量的离散码本向量。
2. **潜在 VLA 模型预训练**：基于观测图像和任务语言描述，预训练一个模型来预测上述离散潜在动作。此阶段完全无需真实机器人动作标签，可大规模利用互联网视频数据。
3. **微调映射**：在小规模机器人操控数据集上微调，将潜在动作空间映射到真实机器人动作空间，实现策略执行。

### 实验设置与关键数字
- **数据来源**：预训练使用大规模无标签互联网视频（包括人类操控视频），微调使用少量带动作标签的机器人操控数据。
- **对比基线**：与现有基于视频训练的策略方法以及使用机器人动作标签训练的 SOTA VLA 模型（如 RT-2）进行对比。
- **核心结果**：
  - LAPA 在语言条件操控任务上显著优于现有无标签视频训练方法。
  - 在需要泛化到未见物体和语义泛化到未见指令的真实世界任务中，LAPA 超越了使用机器人动作标签训练的 SOTA VLA 模型。
  - 仅使用人类操控视频训练时，LAPA 仍展现出正向迁移效果，表明其具备从网络规模数据中学习通用操控知识的潜力。

### 结论
LAPA 通过无监督潜在动作预训练，有效解决了 VLA 模型对人工标注动作标签的依赖问题，大幅扩展了可用的预训练数据源。其性能在多个真实世界操控任务上达到或超越有监督方法，为构建可泛化的机器人基础模型提供了新范式。

## Overview
We introduce Latent Action Pretraining for general Action models (LAPA), an unsupervised method for pretraining Vision-Language-Action (VLA) models without ground-truth robot action labels. Existing Vision-Language-Action models require action labels typically collected by human teleoperators during pretraining, which significantly limits possible data sources and scale. In this work, we propose a method to learn from internet-scale videos that do not have robot action labels. We first train an action quantization model leveraging VQ-VAE-based objective to learn discrete latent actions between image frames, then pretrain a latent VLA model to predict these latent actions from observations and task descriptions, and finally finetune the VLA on small-scale robot manipulation data to map from latent to robot actions. Experimental results demonstrate that our method significantly outperforms existing techniques that train robot manipulation policies from large-scale videos. Furthermore, it outperforms the state-of-the-art VLA model trained with robotic action labels on real-world manipulation tasks that require language conditioning, generalization to unseen objects, and semantic generalization to unseen instructions. Training only on human manipulation videos also shows positive transfer, opening up the potential for leveraging web-scale data for robotics foundation model.

## 개요
우리는 Latent Action Pretraining for general Action models (LAPA)를 소개합니다. 이는 실제 로봇 동작 레이블 없이 Vision-Language-Action (VLA) 모델을 사전 학습하는 비지도 방법입니다. 기존의 Vision-Language-Action 모델은 사전 학습 중 일반적으로 인간 원격 조작자가 수집한 동작 레이블을 필요로 하며, 이는 가능한 데이터 소스와 규모를 크게 제한합니다. 본 연구에서는 로봇 동작 레이블이 없는 인터넷 규모의 비디오로부터 학습하는 방법을 제안합니다. 먼저 VQ-VAE 기반 목적 함수를 활용한 동작 양자화 모델을 훈련하여 이미지 프레임 간의 이산적인 잠재 동작을 학습하고, 그런 다음 관찰 및 작업 설명으로부터 이러한 잠재 동작을 예측하도록 잠재 VLA 모델을 사전 학습하며, 마지막으로 소규모 로봇 조작 데이터로 VLA를 미세 조정하여 잠재 동작을 로봇 동작으로 매핑합니다. 실험 결과는 우리의 방법이 대규모 비디오로부터 로봇 조작 정책을 훈련하는 기존 기술보다 현저히 우수함을 보여줍니다. 또한, 언어 조건화, 보이지 않는 객체에 대한 일반화, 보이지 않는 명령에 대한 의미적 일반화가 필요한 실제 조작 작업에서 로봇 동작 레이블로 훈련된 최첨단 VLA 모델보다 성능이 뛰어납니다. 인간 조작 비디오만으로 훈련해도 긍정적인 전이가 나타나며, 이는 웹 규모 데이터를 로봇 기반 모델에 활용할 가능성을 열어줍니다.

## 핵심 내용
우리는 Latent Action Pretraining for general Action models (LAPA)를 소개합니다. 이는 실제 로봇 동작 레이블 없이 Vision-Language-Action (VLA) 모델을 사전 학습하는 비지도 방법입니다. 기존의 Vision-Language-Action 모델은 사전 학습 중 일반적으로 인간 원격 조작자가 수집한 동작 레이블을 필요로 하며, 이는 가능한 데이터 소스와 규모를 크게 제한합니다. 본 연구에서는 로봇 동작 레이블이 없는 인터넷 규모의 비디오로부터 학습하는 방법을 제안합니다. 먼저 VQ-VAE 기반 목적 함수를 활용한 동작 양자화 모델을 훈련하여 이미지 프레임 간의 이산적인 잠재 동작을 학습하고, 그런 다음 관찰 및 작업 설명으로부터 이러한 잠재 동작을 예측하도록 잠재 VLA 모델을 사전 학습하며, 마지막으로 소규모 로봇 조작 데이터로 VLA를 미세 조정하여 잠재 동작을 로봇 동작으로 매핑합니다. 실험 결과는 우리의 방법이 대규모 비디오로부터 로봇 조작 정책을 훈련하는 기존 기술보다 현저히 우수함을 보여줍니다. 또한, 언어 조건화, 보이지 않는 객체에 대한 일반화, 보이지 않는 명령에 대한 의미적 일반화가 필요한 실제 조작 작업에서 로봇 동작 레이블로 훈련된 최첨단 VLA 모델보다 성능이 뛰어납니다. 인간 조작 비디오만으로 훈련해도 긍정적인 전이가 나타나며, 이는 웹 규모 데이터를 로봇 기반 모델에 활용할 가능성을 열어줍니다.

## 参考
- http://arxiv.org/abs/2410.11758v2
