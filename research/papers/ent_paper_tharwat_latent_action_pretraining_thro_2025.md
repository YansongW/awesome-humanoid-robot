---
$id: ent_paper_tharwat_latent_action_pretraining_thro_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Latent Action Pretraining Through World Modeling
  zh: LAWM
  ko: Latent Action Pretraining Through World Modeling
summary:
  en: Latent Action Pretraining Through World Modeling (LAWM), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Mohamed bin Zayed University of Artificial Intelligence, Alexandria University.
  zh: Latent Action Pretraining Through World Modeling (LAWM), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Mohamed bin Zayed University of Artificial Intelligence, Alexandria University.
  ko: Latent Action Pretraining Through World Modeling (LAWM), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Mohamed bin Zayed University of Artificial Intelligence, Alexandria University.
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
- lawm
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.18428v2.
sources:
- id: src_001
  type: paper
  title: Latent Action Pretraining Through World Modeling (arXiv)
  url: https://arxiv.org/abs/2509.18428
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: LAWM source
  url: https://doi.org/10.48550/arXiv.2509.18428
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have gained popularity for learning robotic manipulation tasks that follow language instructions. State-of-the-art VLAs, such as OpenVLA and $π_{0}$, were trained on large-scale, manually labeled action datasets collected through teleoperation. More recent approaches, including LAPA and villa-X, introduce latent action representations that enable unsupervised pretraining on unlabeled datasets by modeling abstract visual changes between frames. Although these methods have shown strong results, their large model sizes make deployment in real-world settings challenging. In this work, we propose LAWM, a model-agnostic framework to pretrain imitation learning models in a self-supervised way, by learning latent action representations from unlabeled video data through world modeling. These videos can be sourced from robot recordings or videos of humans performing actions with everyday objects. Our framework is able to transfer learned knowledge across tasks, environments, and embodiments. It outperforms models pretrained with ground-truth robot actions and other similar pretraining methods on the LIBERO benchmark and real-world setup, while being efficient and practical for real-world settings.

## 核心内容
Vision-Language-Action (VLA) models have gained popularity for learning robotic manipulation tasks that follow language instructions. State-of-the-art VLAs, such as OpenVLA and $π_{0}$, were trained on large-scale, manually labeled action datasets collected through teleoperation. More recent approaches, including LAPA and villa-X, introduce latent action representations that enable unsupervised pretraining on unlabeled datasets by modeling abstract visual changes between frames. Although these methods have shown strong results, their large model sizes make deployment in real-world settings challenging. In this work, we propose LAWM, a model-agnostic framework to pretrain imitation learning models in a self-supervised way, by learning latent action representations from unlabeled video data through world modeling. These videos can be sourced from robot recordings or videos of humans performing actions with everyday objects. Our framework is able to transfer learned knowledge across tasks, environments, and embodiments. It outperforms models pretrained with ground-truth robot actions and other similar pretraining methods on the LIBERO benchmark and real-world setup, while being efficient and practical for real-world settings.

## 参考
- http://arxiv.org/abs/2509.18428v2

## Overview
Vision-Language-Action (VLA) models have gained popularity for learning robotic manipulation tasks that follow language instructions. State-of-the-art VLAs, such as OpenVLA and $π_{0}$, were trained on large-scale, manually labeled action datasets collected through teleoperation. More recent approaches, including LAPA and villa-X, introduce latent action representations that enable unsupervised pretraining on unlabeled datasets by modeling abstract visual changes between frames. Although these methods have shown strong results, their large model sizes make deployment in real-world settings challenging. In this work, we propose LAWM, a model-agnostic framework to pretrain imitation learning models in a self-supervised way, by learning latent action representations from unlabeled video data through world modeling. These videos can be sourced from robot recordings or videos of humans performing actions with everyday objects. Our framework is able to transfer learned knowledge across tasks, environments, and embodiments. It outperforms models pretrained with ground-truth robot actions and other similar pretraining methods on the LIBERO benchmark and real-world setup, while being efficient and practical for real-world settings.

## Content
Vision-Language-Action (VLA) models have gained popularity for learning robotic manipulation tasks that follow language instructions. State-of-the-art VLAs, such as OpenVLA and $π_{0}$, were trained on large-scale, manually labeled action datasets collected through teleoperation. More recent approaches, including LAPA and villa-X, introduce latent action representations that enable unsupervised pretraining on unlabeled datasets by modeling abstract visual changes between frames. Although these methods have shown strong results, their large model sizes make deployment in real-world settings challenging. In this work, we propose LAWM, a model-agnostic framework to pretrain imitation learning models in a self-supervised way, by learning latent action representations from unlabeled video data through world modeling. These videos can be sourced from robot recordings or videos of humans performing actions with everyday objects. Our framework is able to transfer learned knowledge across tasks, environments, and embodiments. It outperforms models pretrained with ground-truth robot actions and other similar pretraining methods on the LIBERO benchmark and real-world setup, while being efficient and practical for real-world settings.

## 개요
Vision-Language-Action (VLA) 모델은 언어 명령을 따르는 로봇 조작 작업을 학습하는 데 널리 사용되고 있습니다. OpenVLA 및 $π_{0}$와 같은 최첨단 VLA 모델은 원격 조작을 통해 수집된 대규모의 수동 레이블링된 행동 데이터셋으로 학습되었습니다. LAPA 및 villa-X를 포함한 최근 접근 방식은 프레임 간의 추상적인 시각적 변화를 모델링하여 레이블이 없는 데이터셋에서 비지도 사전 학습을 가능하게 하는 잠재 행동 표현을 도입합니다. 이러한 방법들은 강력한 결과를 보여주었지만, 큰 모델 크기로 인해 실제 환경에서의 배포가 어렵습니다. 본 연구에서는 세계 모델링을 통해 레이블이 없는 비디오 데이터에서 잠재 행동 표현을 학습함으로써, 모방 학습 모델을 자기 지도 방식으로 사전 학습하는 모델에 구애받지 않는 프레임워크인 LAWM을 제안합니다. 이러한 비디오는 로봇 녹화물이나 일상적인 물체로 행동을 수행하는 인간의 비디오에서 얻을 수 있습니다. 우리의 프레임워크는 작업, 환경 및 구현체 간에 학습된 지식을 전이할 수 있습니다. 이는 LIBERO 벤치마크 및 실제 환경 설정에서 실제 로봇 행동으로 사전 학습된 모델 및 기타 유사한 사전 학습 방법보다 뛰어난 성능을 보이면서도 실제 환경에 효율적이고 실용적입니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 언어 명령을 따르는 로봇 조작 작업을 학습하는 데 널리 사용되고 있습니다. OpenVLA 및 $π_{0}$와 같은 최첨단 VLA 모델은 원격 조작을 통해 수집된 대규모의 수동 레이블링된 행동 데이터셋으로 학습되었습니다. LAPA 및 villa-X를 포함한 최근 접근 방식은 프레임 간의 추상적인 시각적 변화를 모델링하여 레이블이 없는 데이터셋에서 비지도 사전 학습을 가능하게 하는 잠재 행동 표현을 도입합니다. 이러한 방법들은 강력한 결과를 보여주었지만, 큰 모델 크기로 인해 실제 환경에서의 배포가 어렵습니다. 본 연구에서는 세계 모델링을 통해 레이블이 없는 비디오 데이터에서 잠재 행동 표현을 학습함으로써, 모방 학습 모델을 자기 지도 방식으로 사전 학습하는 모델에 구애받지 않는 프레임워크인 LAWM을 제안합니다. 이러한 비디오는 로봇 녹화물이나 일상적인 물체로 행동을 수행하는 인간의 비디오에서 얻을 수 있습니다. 우리의 프레임워크는 작업, 환경 및 구현체 간에 학습된 지식을 전이할 수 있습니다. 이는 LIBERO 벤치마크 및 실제 환경 설정에서 실제 로봇 행동으로 사전 학습된 모델 및 기타 유사한 사전 학습 방법보다 뛰어난 성능을 보이면서도 실제 환경에 효율적이고 실용적입니다.
