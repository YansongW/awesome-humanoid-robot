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
  zh: Latent Action Pretraining from Videos (LAPA), is a 2024 large vision-language-action model for robotic manipulation,
    introduced by KAIST, University of Washington, Microsoft Research, NVIDIA, Allen Institute for AI, and published at ICLR
    2024.
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.11758v2.
sources:
- id: src_001
  type: paper
  title: LAPA source
  url: https://openreview.net/forum?id=VYOe2eBQeh
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
We introduce Latent Action Pretraining for general Action models (LAPA), an unsupervised method for pretraining Vision-Language-Action (VLA) models without ground-truth robot action labels. Existing Vision-Language-Action models require action labels typically collected by human teleoperators during pretraining, which significantly limits possible data sources and scale. In this work, we propose a method to learn from internet-scale videos that do not have robot action labels. We first train an action quantization model leveraging VQ-VAE-based objective to learn discrete latent actions between image frames, then pretrain a latent VLA model to predict these latent actions from observations and task descriptions, and finally finetune the VLA on small-scale robot manipulation data to map from latent to robot actions. Experimental results demonstrate that our method significantly outperforms existing techniques that train robot manipulation policies from large-scale videos. Furthermore, it outperforms the state-of-the-art VLA model trained with robotic action labels on real-world manipulation tasks that require language conditioning, generalization to unseen objects, and semantic generalization to unseen instructions. Training only on human manipulation videos also shows positive transfer, opening up the potential for leveraging web-scale data for robotics foundation model.

## 核心内容
We introduce Latent Action Pretraining for general Action models (LAPA), an unsupervised method for pretraining Vision-Language-Action (VLA) models without ground-truth robot action labels. Existing Vision-Language-Action models require action labels typically collected by human teleoperators during pretraining, which significantly limits possible data sources and scale. In this work, we propose a method to learn from internet-scale videos that do not have robot action labels. We first train an action quantization model leveraging VQ-VAE-based objective to learn discrete latent actions between image frames, then pretrain a latent VLA model to predict these latent actions from observations and task descriptions, and finally finetune the VLA on small-scale robot manipulation data to map from latent to robot actions. Experimental results demonstrate that our method significantly outperforms existing techniques that train robot manipulation policies from large-scale videos. Furthermore, it outperforms the state-of-the-art VLA model trained with robotic action labels on real-world manipulation tasks that require language conditioning, generalization to unseen objects, and semantic generalization to unseen instructions. Training only on human manipulation videos also shows positive transfer, opening up the potential for leveraging web-scale data for robotics foundation model.

## 参考
- http://arxiv.org/abs/2410.11758v2

## Overview
We introduce Latent Action Pretraining for general Action models (LAPA), an unsupervised method for pretraining Vision-Language-Action (VLA) models without ground-truth robot action labels. Existing Vision-Language-Action models require action labels typically collected by human teleoperators during pretraining, which significantly limits possible data sources and scale. In this work, we propose a method to learn from internet-scale videos that do not have robot action labels. We first train an action quantization model leveraging VQ-VAE-based objective to learn discrete latent actions between image frames, then pretrain a latent VLA model to predict these latent actions from observations and task descriptions, and finally finetune the VLA on small-scale robot manipulation data to map from latent to robot actions. Experimental results demonstrate that our method significantly outperforms existing techniques that train robot manipulation policies from large-scale videos. Furthermore, it outperforms the state-of-the-art VLA model trained with robotic action labels on real-world manipulation tasks that require language conditioning, generalization to unseen objects, and semantic generalization to unseen instructions. Training only on human manipulation videos also shows positive transfer, opening up the potential for leveraging web-scale data for robotics foundation model.

## Content
We introduce Latent Action Pretraining for general Action models (LAPA), an unsupervised method for pretraining Vision-Language-Action (VLA) models without ground-truth robot action labels. Existing Vision-Language-Action models require action labels typically collected by human teleoperators during pretraining, which significantly limits possible data sources and scale. In this work, we propose a method to learn from internet-scale videos that do not have robot action labels. We first train an action quantization model leveraging VQ-VAE-based objective to learn discrete latent actions between image frames, then pretrain a latent VLA model to predict these latent actions from observations and task descriptions, and finally finetune the VLA on small-scale robot manipulation data to map from latent to robot actions. Experimental results demonstrate that our method significantly outperforms existing techniques that train robot manipulation policies from large-scale videos. Furthermore, it outperforms the state-of-the-art VLA model trained with robotic action labels on real-world manipulation tasks that require language conditioning, generalization to unseen objects, and semantic generalization to unseen instructions. Training only on human manipulation videos also shows positive transfer, opening up the potential for leveraging web-scale data for robotics foundation model.

## 개요
우리는 Latent Action Pretraining for general Action models (LAPA)를 소개합니다. 이는 실제 로봇 동작 레이블 없이 Vision-Language-Action (VLA) 모델을 사전 학습하는 비지도 방법입니다. 기존의 Vision-Language-Action 모델은 사전 학습 중 일반적으로 인간 원격 조작자가 수집한 동작 레이블을 필요로 하며, 이는 가능한 데이터 소스와 규모를 크게 제한합니다. 본 연구에서는 로봇 동작 레이블이 없는 인터넷 규모의 비디오로부터 학습하는 방법을 제안합니다. 먼저 VQ-VAE 기반 목적 함수를 활용한 동작 양자화 모델을 훈련하여 이미지 프레임 간의 이산적인 잠재 동작을 학습하고, 그런 다음 관찰 및 작업 설명으로부터 이러한 잠재 동작을 예측하도록 잠재 VLA 모델을 사전 학습하며, 마지막으로 소규모 로봇 조작 데이터로 VLA를 미세 조정하여 잠재 동작을 로봇 동작으로 매핑합니다. 실험 결과는 우리의 방법이 대규모 비디오로부터 로봇 조작 정책을 훈련하는 기존 기술보다 현저히 우수함을 보여줍니다. 또한, 언어 조건화, 보이지 않는 객체에 대한 일반화, 보이지 않는 명령에 대한 의미적 일반화가 필요한 실제 조작 작업에서 로봇 동작 레이블로 훈련된 최첨단 VLA 모델보다 성능이 뛰어납니다. 인간 조작 비디오만으로 훈련해도 긍정적인 전이가 나타나며, 이는 웹 규모 데이터를 로봇 기반 모델에 활용할 가능성을 열어줍니다.

## 핵심 내용
우리는 Latent Action Pretraining for general Action models (LAPA)를 소개합니다. 이는 실제 로봇 동작 레이블 없이 Vision-Language-Action (VLA) 모델을 사전 학습하는 비지도 방법입니다. 기존의 Vision-Language-Action 모델은 사전 학습 중 일반적으로 인간 원격 조작자가 수집한 동작 레이블을 필요로 하며, 이는 가능한 데이터 소스와 규모를 크게 제한합니다. 본 연구에서는 로봇 동작 레이블이 없는 인터넷 규모의 비디오로부터 학습하는 방법을 제안합니다. 먼저 VQ-VAE 기반 목적 함수를 활용한 동작 양자화 모델을 훈련하여 이미지 프레임 간의 이산적인 잠재 동작을 학습하고, 그런 다음 관찰 및 작업 설명으로부터 이러한 잠재 동작을 예측하도록 잠재 VLA 모델을 사전 학습하며, 마지막으로 소규모 로봇 조작 데이터로 VLA를 미세 조정하여 잠재 동작을 로봇 동작으로 매핑합니다. 실험 결과는 우리의 방법이 대규모 비디오로부터 로봇 조작 정책을 훈련하는 기존 기술보다 현저히 우수함을 보여줍니다. 또한, 언어 조건화, 보이지 않는 객체에 대한 일반화, 보이지 않는 명령에 대한 의미적 일반화가 필요한 실제 조작 작업에서 로봇 동작 레이블로 훈련된 최첨단 VLA 모델보다 성능이 뛰어납니다. 인간 조작 비디오만으로 훈련해도 긍정적인 전이가 나타나며, 이는 웹 규모 데이터를 로봇 기반 모델에 활용할 가능성을 열어줍니다.
