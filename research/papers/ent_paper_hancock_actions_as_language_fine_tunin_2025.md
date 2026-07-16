---
$id: ent_paper_hancock_actions_as_language_fine_tunin_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting'
  zh: VLM2VLA
  ko: 'Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting'
summary:
  en: 'Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting (VLM2VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Princeton University.'
  zh: 'Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting (VLM2VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Princeton University.'
  ko: 'Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting (VLM2VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Princeton University.'
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
- vision_language_action
- vla
- vlm2vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.22195v1.
sources:
- id: src_001
  type: paper
  title: 'Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting (arXiv)'
  url: https://arxiv.org/abs/2509.22195
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLM2VLA source
  url: https://doi.org/10.48550/arXiv.2509.22195
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Fine-tuning vision-language models (VLMs) on robot teleoperation data to create vision-language-action (VLA) models is a promising paradigm for training generalist policies, but it suffers from a fundamental tradeoff: learning to produce actions often diminishes the VLM's foundational reasoning and multimodal understanding, hindering generalization to novel scenarios, instruction following, and semantic understanding. We argue that this catastrophic forgetting is due to a distribution mismatch between the VLM's internet-scale pretraining corpus and the robotics fine-tuning data. Inspired by this observation, we introduce VLM2VLA: a VLA training paradigm that first resolves this mismatch at the data level by representing low-level actions with natural language. This alignment makes it possible to train VLAs solely with Low-Rank Adaptation (LoRA), thereby minimally modifying the VLM backbone and averting catastrophic forgetting. As a result, the VLM can be fine-tuned on robot teleoperation data without fundamentally altering the underlying architecture and without expensive co-training on internet-scale VLM datasets. Through extensive Visual Question Answering (VQA) studies and over 800 real-world robotics experiments, we demonstrate that VLM2VLA preserves the VLM's core capabilities, enabling zero-shot generalization to novel tasks that require open-world semantic reasoning and multilingual instruction following.

## 核心内容
Fine-tuning vision-language models (VLMs) on robot teleoperation data to create vision-language-action (VLA) models is a promising paradigm for training generalist policies, but it suffers from a fundamental tradeoff: learning to produce actions often diminishes the VLM's foundational reasoning and multimodal understanding, hindering generalization to novel scenarios, instruction following, and semantic understanding. We argue that this catastrophic forgetting is due to a distribution mismatch between the VLM's internet-scale pretraining corpus and the robotics fine-tuning data. Inspired by this observation, we introduce VLM2VLA: a VLA training paradigm that first resolves this mismatch at the data level by representing low-level actions with natural language. This alignment makes it possible to train VLAs solely with Low-Rank Adaptation (LoRA), thereby minimally modifying the VLM backbone and averting catastrophic forgetting. As a result, the VLM can be fine-tuned on robot teleoperation data without fundamentally altering the underlying architecture and without expensive co-training on internet-scale VLM datasets. Through extensive Visual Question Answering (VQA) studies and over 800 real-world robotics experiments, we demonstrate that VLM2VLA preserves the VLM's core capabilities, enabling zero-shot generalization to novel tasks that require open-world semantic reasoning and multilingual instruction following.

## 参考
- http://arxiv.org/abs/2509.22195v1

## Overview
Fine-tuning vision-language models (VLMs) on robot teleoperation data to create vision-language-action (VLA) models is a promising paradigm for training generalist policies, but it suffers from a fundamental tradeoff: learning to produce actions often diminishes the VLM's foundational reasoning and multimodal understanding, hindering generalization to novel scenarios, instruction following, and semantic understanding. We argue that this catastrophic forgetting is due to a distribution mismatch between the VLM's internet-scale pretraining corpus and the robotics fine-tuning data. Inspired by this observation, we introduce VLM2VLA: a VLA training paradigm that first resolves this mismatch at the data level by representing low-level actions with natural language. This alignment makes it possible to train VLAs solely with Low-Rank Adaptation (LoRA), thereby minimally modifying the VLM backbone and averting catastrophic forgetting. As a result, the VLM can be fine-tuned on robot teleoperation data without fundamentally altering the underlying architecture and without expensive co-training on internet-scale VLM datasets. Through extensive Visual Question Answering (VQA) studies and over 800 real-world robotics experiments, we demonstrate that VLM2VLA preserves the VLM's core capabilities, enabling zero-shot generalization to novel tasks that require open-world semantic reasoning and multilingual instruction following.

## Content
Fine-tuning vision-language models (VLMs) on robot teleoperation data to create vision-language-action (VLA) models is a promising paradigm for training generalist policies, but it suffers from a fundamental tradeoff: learning to produce actions often diminishes the VLM's foundational reasoning and multimodal understanding, hindering generalization to novel scenarios, instruction following, and semantic understanding. We argue that this catastrophic forgetting is due to a distribution mismatch between the VLM's internet-scale pretraining corpus and the robotics fine-tuning data. Inspired by this observation, we introduce VLM2VLA: a VLA training paradigm that first resolves this mismatch at the data level by representing low-level actions with natural language. This alignment makes it possible to train VLAs solely with Low-Rank Adaptation (LoRA), thereby minimally modifying the VLM backbone and averting catastrophic forgetting. As a result, the VLM can be fine-tuned on robot teleoperation data without fundamentally altering the underlying architecture and without expensive co-training on internet-scale VLM datasets. Through extensive Visual Question Answering (VQA) studies and over 800 real-world robotics experiments, we demonstrate that VLM2VLA preserves the VLM's core capabilities, enabling zero-shot generalization to novel tasks that require open-world semantic reasoning and multilingual instruction following.

## 개요
로봇 원격 조작 데이터를 기반으로 비전-언어 모델(VLM)을 미세 조정하여 비전-언어-행동(VLA) 모델을 구축하는 것은 범용 정책을 훈련하기 위한 유망한 패러다임이지만, 근본적인 트레이드오프가 존재합니다. 즉, 행동을 생성하는 방법을 학습하면 VLM의 기초 추론 능력과 다중 모달 이해력이 저하되어 새로운 시나리오에 대한 일반화, 명령 수행 및 의미 이해가 방해받습니다. 우리는 이러한 파괴적 망각이 VLM의 인터넷 규모 사전 학습 코퍼스와 로봇 미세 조정 데이터 간의 분포 불일치로 인해 발생한다고 주장합니다. 이 관찰에 영감을 받아, 우리는 VLM2VLA를 소개합니다. 이는 저수준 행동을 자연어로 표현하여 데이터 수준에서 이러한 불일치를 먼저 해결하는 VLA 훈련 패러다임입니다. 이러한 정렬 덕분에 Low-Rank Adaptation(LoRA)만으로 VLA를 훈련할 수 있어 VLM 백본을 최소한으로 수정하고 파괴적 망각을 방지할 수 있습니다. 결과적으로 VLM은 기본 아키텍처를 근본적으로 변경하지 않고, 인터넷 규모 VLM 데이터셋에 대한 값비싼 공동 훈련 없이 로봇 원격 조작 데이터로 미세 조정될 수 있습니다. 광범위한 Visual Question Answering(VQA) 연구와 800회 이상의 실제 로봇 실험을 통해 VLM2VLA가 VLM의 핵심 능력을 보존하여, 개방형 세계 의미 추론 및 다국어 명령 수행이 필요한 새로운 작업에 대한 제로샷 일반화를 가능하게 함을 입증합니다.

## 핵심 내용
로봇 원격 조작 데이터를 기반으로 비전-언어 모델(VLM)을 미세 조정하여 비전-언어-행동(VLA) 모델을 구축하는 것은 범용 정책을 훈련하기 위한 유망한 패러다임이지만, 근본적인 트레이드오프가 존재합니다. 즉, 행동을 생성하는 방법을 학습하면 VLM의 기초 추론 능력과 다중 모달 이해력이 저하되어 새로운 시나리오에 대한 일반화, 명령 수행 및 의미 이해가 방해받습니다. 우리는 이러한 파괴적 망각이 VLM의 인터넷 규모 사전 학습 코퍼스와 로봇 미세 조정 데이터 간의 분포 불일치로 인해 발생한다고 주장합니다. 이 관찰에 영감을 받아, 우리는 VLM2VLA를 소개합니다. 이는 저수준 행동을 자연어로 표현하여 데이터 수준에서 이러한 불일치를 먼저 해결하는 VLA 훈련 패러다임입니다. 이러한 정렬 덕분에 Low-Rank Adaptation(LoRA)만으로 VLA를 훈련할 수 있어 VLM 백본을 최소한으로 수정하고 파괴적 망각을 방지할 수 있습니다. 결과적으로 VLM은 기본 아키텍처를 근본적으로 변경하지 않고, 인터넷 규모 VLM 데이터셋에 대한 값비싼 공동 훈련 없이 로봇 원격 조작 데이터로 미세 조정될 수 있습니다. 광범위한 Visual Question Answering(VQA) 연구와 800회 이상의 실제 로봇 실험을 통해 VLM2VLA가 VLM의 핵심 능력을 보존하여, 개방형 세계 의미 추론 및 다국어 명령 수행이 필요한 새로운 작업에 대한 제로샷 일반화를 가능하게 함을 입증합니다.
