---
$id: ent_paper_bendikas_focusing_on_what_matters_objec_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models'
  zh: Oat-VLA
  ko: 'Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models'
summary:
  en: 'Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models (Oat-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Centre for Artificial Intelligence, UCL, Qualcomm
    AI Research, and published at CoRL25.'
  zh: 'Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models (Oat-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Centre for Artificial Intelligence, UCL, Qualcomm
    AI Research, and published at CoRL25.'
  ko: 'Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models (Oat-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Centre for Artificial Intelligence, UCL, Qualcomm
    AI Research, and published at CoRL25.'
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
- oat_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.23655v1.
sources:
- id: src_001
  type: paper
  title: 'Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models (arXiv)'
  url: https://arxiv.org/abs/2509.23655
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Oat-VLA source
  url: https://doi.org/10.48550/arXiv.2509.23655
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models offer a pivotal approach to learning robotic manipulation at scale by repurposing large pre-trained Vision-Language-Models (VLM) to output robotic actions. However, adapting VLMs for robotic domains comes with an unnecessarily high computational cost, which we attribute to the tokenization scheme of visual inputs. In this work, we aim to enable efficient VLA training by proposing Oat-VLA, an Object-Agent-centric Tokenization for VLAs. Building on the insights of object-centric representation learning, our method introduces an inductive bias towards scene objects and the agent's own visual information. As a result, we find that Oat-VLA can drastically reduce the number of visual tokens to just a few tokens without sacrificing performance. We reveal that Oat-VLA converges at least twice as fast as OpenVLA on the LIBERO suite, as well as outperform OpenVLA in diverse real-world pick and place tasks.

## 核心内容
Vision-Language-Action (VLA) models offer a pivotal approach to learning robotic manipulation at scale by repurposing large pre-trained Vision-Language-Models (VLM) to output robotic actions. However, adapting VLMs for robotic domains comes with an unnecessarily high computational cost, which we attribute to the tokenization scheme of visual inputs. In this work, we aim to enable efficient VLA training by proposing Oat-VLA, an Object-Agent-centric Tokenization for VLAs. Building on the insights of object-centric representation learning, our method introduces an inductive bias towards scene objects and the agent's own visual information. As a result, we find that Oat-VLA can drastically reduce the number of visual tokens to just a few tokens without sacrificing performance. We reveal that Oat-VLA converges at least twice as fast as OpenVLA on the LIBERO suite, as well as outperform OpenVLA in diverse real-world pick and place tasks.

## 参考
- http://arxiv.org/abs/2509.23655v1

## Overview
Vision-Language-Action (VLA) models offer a pivotal approach to learning robotic manipulation at scale by repurposing large pre-trained Vision-Language-Models (VLM) to output robotic actions. However, adapting VLMs for robotic domains comes with an unnecessarily high computational cost, which we attribute to the tokenization scheme of visual inputs. In this work, we aim to enable efficient VLA training by proposing Oat-VLA, an Object-Agent-centric Tokenization for VLAs. Building on the insights of object-centric representation learning, our method introduces an inductive bias towards scene objects and the agent's own visual information. As a result, we find that Oat-VLA can drastically reduce the number of visual tokens to just a few tokens without sacrificing performance. We reveal that Oat-VLA converges at least twice as fast as OpenVLA on the LIBERO suite, as well as outperform OpenVLA in diverse real-world pick and place tasks.

## Content
Vision-Language-Action (VLA) models offer a pivotal approach to learning robotic manipulation at scale by repurposing large pre-trained Vision-Language-Models (VLM) to output robotic actions. However, adapting VLMs for robotic domains comes with an unnecessarily high computational cost, which we attribute to the tokenization scheme of visual inputs. In this work, we aim to enable efficient VLA training by proposing Oat-VLA, an Object-Agent-centric Tokenization for VLAs. Building on the insights of object-centric representation learning, our method introduces an inductive bias towards scene objects and the agent's own visual information. As a result, we find that Oat-VLA can drastically reduce the number of visual tokens to just a few tokens without sacrificing performance. We reveal that Oat-VLA converges at least twice as fast as OpenVLA on the LIBERO suite, as well as outperform OpenVLA in diverse real-world pick and place tasks.

## 개요
Vision-Language-Action (VLA) 모델은 대규모 사전 훈련된 Vision-Language-Model (VLM)을 로봇 동작 출력에 재활용함으로써 로봇 조작을 대규모로 학습하는 핵심 접근 방식을 제공합니다. 그러나 VLM을 로봇 도메인에 적용하는 과정에서 불필요하게 높은 계산 비용이 발생하며, 이는 시각 입력의 토큰화 방식에 기인한다고 판단합니다. 본 연구에서는 VLA를 위한 효율적인 훈련을 가능하게 하기 위해 Oat-VLA, 즉 객체-에이전트 중심 토큰화(Object-Agent-centric Tokenization)를 제안합니다. 객체 중심 표현 학습의 통찰을 바탕으로, 우리의 방법은 장면 객체와 에이전트 자체의 시각 정보에 대한 귀납적 편향을 도입합니다. 그 결과, Oat-VLA는 성능 저하 없이 시각 토큰 수를 단 몇 개로 대폭 줄일 수 있음을 발견했습니다. 또한 Oat-VLA가 LIBERO 스위트에서 OpenVLA보다 최소 두 배 빠르게 수렴하며, 다양한 실제 세계의 집기 및 배치 작업에서 OpenVLA를 능가한다는 것을 입증했습니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 대규모 사전 훈련된 Vision-Language-Model (VLM)을 로봇 동작 출력에 재활용함으로써 로봇 조작을 대규모로 학습하는 핵심 접근 방식을 제공합니다. 그러나 VLM을 로봇 도메인에 적용하는 과정에서 불필요하게 높은 계산 비용이 발생하며, 이는 시각 입력의 토큰화 방식에 기인한다고 판단합니다. 본 연구에서는 VLA를 위한 효율적인 훈련을 가능하게 하기 위해 Oat-VLA, 즉 객체-에이전트 중심 토큰화(Object-Agent-centric Tokenization)를 제안합니다. 객체 중심 표현 학습의 통찰을 바탕으로, 우리의 방법은 장면 객체와 에이전트 자체의 시각 정보에 대한 귀납적 편향을 도입합니다. 그 결과, Oat-VLA는 성능 저하 없이 시각 토큰 수를 단 몇 개로 대폭 줄일 수 있음을 발견했습니다. 또한 Oat-VLA가 LIBERO 스위트에서 OpenVLA보다 최소 두 배 빠르게 수렴하며, 다양한 실제 세계의 집기 및 배치 작업에서 OpenVLA를 능가한다는 것을 입증했습니다.
