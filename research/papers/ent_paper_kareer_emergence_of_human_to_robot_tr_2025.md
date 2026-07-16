---
$id: ent_paper_kareer_emergence_of_human_to_robot_tr_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Emergence of Human to Robot Transfer in Vision-Language-Action Models
  zh: Emergence of Human to Robot Transfer in Vision-Language-Action Models
  ko: Emergence of Human to Robot Transfer in Vision-Language-Action Models
summary:
  en: Emergence of Human to Robot Transfer in Vision-Language-Action Models (Emergence of Human to Robot Transfer in Vision-Language-Action
    Models), is a 2025 large vision-language-action model for robotic manipulation, introduced by Physical Intelligence, Georgia
    Institute of Technology.
  zh: Emergence of Human to Robot Transfer in Vision-Language-Action Models (Emergence of Human to Robot Transfer in Vision-Language-Action
    Models), is a 2025 large vision-language-action model for robotic manipulation, introduced by Physical Intelligence, Georgia
    Institute of Technology.
  ko: Emergence of Human to Robot Transfer in Vision-Language-Action Models (Emergence of Human to Robot Transfer in Vision-Language-Action
    Models), is a 2025 large vision-language-action model for robotic manipulation, introduced by Physical Intelligence, Georgia
    Institute of Technology.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- emergence_of_human_to_robot_tr
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.22414v1.
sources:
- id: src_001
  type: paper
  title: Emergence of Human to Robot Transfer in Vision-Language-Action Models (arXiv)
  url: https://arxiv.org/abs/2512.22414
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Emergence of Human to Robot Transfer in Vision-Language-Action Models source
  url: https://doi.org/10.48550/arXiv.2512.22414
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models can enable broad open world generalization, but require large and diverse datasets. It is appealing to consider whether some of this data can come from human videos, which cover diverse real-world situations and are easy to obtain. However, it is difficult to train VLAs with human videos alone, and establishing a mapping between humans and robots requires manual engineering and presents a major research challenge. Drawing inspiration from advances in large language models, where the ability to learn from diverse supervision emerges with scale, we ask whether a similar phenomenon holds for VLAs that incorporate human video data. We introduce a simple co-training recipe, and find that human-to-robot transfer emerges once the VLA is pre-trained on sufficient scenes, tasks, and embodiments. Our analysis suggests that this emergent capability arises because diverse pretraining produces embodiment-agnostic representations for human and robot data. We validate these findings through a series of experiments probing human to robot skill transfer and find that with sufficiently diverse robot pre-training our method can nearly double the performance on generalization settings seen only in human data.

## 核心内容
Vision-language-action (VLA) models can enable broad open world generalization, but require large and diverse datasets. It is appealing to consider whether some of this data can come from human videos, which cover diverse real-world situations and are easy to obtain. However, it is difficult to train VLAs with human videos alone, and establishing a mapping between humans and robots requires manual engineering and presents a major research challenge. Drawing inspiration from advances in large language models, where the ability to learn from diverse supervision emerges with scale, we ask whether a similar phenomenon holds for VLAs that incorporate human video data. We introduce a simple co-training recipe, and find that human-to-robot transfer emerges once the VLA is pre-trained on sufficient scenes, tasks, and embodiments. Our analysis suggests that this emergent capability arises because diverse pretraining produces embodiment-agnostic representations for human and robot data. We validate these findings through a series of experiments probing human to robot skill transfer and find that with sufficiently diverse robot pre-training our method can nearly double the performance on generalization settings seen only in human data.

## 参考
- http://arxiv.org/abs/2512.22414v1

## Overview
Vision-language-action (VLA) models can enable broad open world generalization, but require large and diverse datasets. It is appealing to consider whether some of this data can come from human videos, which cover diverse real-world situations and are easy to obtain. However, it is difficult to train VLAs with human videos alone, and establishing a mapping between humans and robots requires manual engineering and presents a major research challenge. Drawing inspiration from advances in large language models, where the ability to learn from diverse supervision emerges with scale, we ask whether a similar phenomenon holds for VLAs that incorporate human video data. We introduce a simple co-training recipe, and find that human-to-robot transfer emerges once the VLA is pre-trained on sufficient scenes, tasks, and embodiments. Our analysis suggests that this emergent capability arises because diverse pretraining produces embodiment-agnostic representations for human and robot data. We validate these findings through a series of experiments probing human to robot skill transfer and find that with sufficiently diverse robot pre-training our method can nearly double the performance on generalization settings seen only in human data.

## Content
Vision-language-action (VLA) models can enable broad open world generalization, but require large and diverse datasets. It is appealing to consider whether some of this data can come from human videos, which cover diverse real-world situations and are easy to obtain. However, it is difficult to train VLAs with human videos alone, and establishing a mapping between humans and robots requires manual engineering and presents a major research challenge. Drawing inspiration from advances in large language models, where the ability to learn from diverse supervision emerges with scale, we ask whether a similar phenomenon holds for VLAs that incorporate human video data. We introduce a simple co-training recipe, and find that human-to-robot transfer emerges once the VLA is pre-trained on sufficient scenes, tasks, and embodiments. Our analysis suggests that this emergent capability arises because diverse pretraining produces embodiment-agnostic representations for human and robot data. We validate these findings through a series of experiments probing human to robot skill transfer and find that with sufficiently diverse robot pre-training our method can nearly double the performance on generalization settings seen only in human data.

## 개요
Vision-language-action (VLA) 모델은 광범위한 개방형 세계 일반화를 가능하게 하지만, 크고 다양한 데이터셋이 필요합니다. 이러한 데이터 중 일부가 다양한 실제 상황을 포괄하고 쉽게 얻을 수 있는 인간 비디오에서 나올 수 있는지 고려하는 것은 매력적입니다. 그러나 인간 비디오만으로 VLA를 훈련하는 것은 어렵고, 인간과 로봇 간의 매핑을 구축하려면 수동 엔지니어링이 필요하며 이는 주요 연구 과제로 남아 있습니다. 다양한 감독(supervision)으로부터 학습하는 능력이 규모에 따라 나타나는 대규모 언어 모델의 발전에서 영감을 얻어, 인간 비디오 데이터를 통합한 VLA에서도 유사한 현상이 발생하는지 질문합니다. 우리는 간단한 공동 훈련(co-training) 방법을 도입하고, VLA가 충분한 장면, 작업 및 구현체(embodiment)에 대해 사전 훈련되면 인간-로봇 전이가 나타난다는 것을 발견했습니다. 우리의 분석은 이러한 창발적 능력이 다양한 사전 훈련이 인간 및 로봇 데이터에 대해 구현체에 구애받지 않는 표현(embodiment-agnostic representations)을 생성하기 때문에 발생한다고 제안합니다. 우리는 인간에서 로봇으로의 기술 전이를 조사하는 일련의 실험을 통해 이러한 발견을 검증하고, 충분히 다양한 로봇 사전 훈련을 통해 우리의 방법이 인간 데이터에서만 관찰된 일반화 설정에서 성능을 거의 두 배로 향상시킬 수 있음을 발견했습니다.

## 핵심 내용
Vision-language-action (VLA) 모델은 광범위한 개방형 세계 일반화를 가능하게 하지만, 크고 다양한 데이터셋이 필요합니다. 이러한 데이터 중 일부가 다양한 실제 상황을 포괄하고 쉽게 얻을 수 있는 인간 비디오에서 나올 수 있는지 고려하는 것은 매력적입니다. 그러나 인간 비디오만으로 VLA를 훈련하는 것은 어렵고, 인간과 로봇 간의 매핑을 구축하려면 수동 엔지니어링이 필요하며 이는 주요 연구 과제로 남아 있습니다. 다양한 감독(supervision)으로부터 학습하는 능력이 규모에 따라 나타나는 대규모 언어 모델의 발전에서 영감을 얻어, 인간 비디오 데이터를 통합한 VLA에서도 유사한 현상이 발생하는지 질문합니다. 우리는 간단한 공동 훈련(co-training) 방법을 도입하고, VLA가 충분한 장면, 작업 및 구현체(embodiment)에 대해 사전 훈련되면 인간-로봇 전이가 나타난다는 것을 발견했습니다. 우리의 분석은 이러한 창발적 능력이 다양한 사전 훈련이 인간 및 로봇 데이터에 대해 구현체에 구애받지 않는 표현(embodiment-agnostic representations)을 생성하기 때문에 발생한다고 제안합니다. 우리는 인간에서 로봇으로의 기술 전이를 조사하는 일련의 실험을 통해 이러한 발견을 검증하고, 충분히 다양한 로봇 사전 훈련을 통해 우리의 방법이 인간 데이터에서만 관찰된 일반화 설정에서 성능을 거의 두 배로 향상시킬 수 있음을 발견했습니다.
