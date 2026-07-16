---
$id: ent_paper_zhang_up_vla_a_unified_understanding_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent'
  zh: UP-VLA
  ko: 'UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent'
summary:
  en: 'UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent (UP-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Shanghai Qi Zhi Institute, and published at ICML 2025.'
  zh: 'UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent (UP-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Shanghai Qi Zhi Institute, and published at ICML 2025.'
  ko: 'UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent (UP-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Shanghai Qi Zhi Institute, and published at ICML 2025.'
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
- up_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2501.18867v3.
sources:
- id: src_001
  type: paper
  title: UP-VLA source
  url: https://openreview.net/forum?id=V7JPraxi5j
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent advancements in Vision-Language-Action (VLA) models have leveraged pre-trained Vision-Language Models (VLMs) to improve the generalization capabilities. VLMs, typically pre-trained on vision-language understanding tasks, provide rich semantic knowledge and reasoning abilities. However, prior research has shown that VLMs often focus on high-level semantic content and neglect low-level features, limiting their ability to capture detailed spatial information and understand physical dynamics. These aspects, which are crucial for embodied control tasks, remain underexplored in existing pre-training paradigms. In this paper, we investigate the training paradigm for VLAs, and introduce \textbf{UP-VLA}, a \textbf{U}nified VLA model training with both multi-modal \textbf{U}nderstanding and future \textbf{P}rediction objectives, enhancing both high-level semantic comprehension and low-level spatial understanding. Experimental results show that UP-VLA achieves a 33% improvement on the Calvin ABC-D benchmark compared to the previous state-of-the-art method. Additionally, UP-VLA demonstrates improved success rates in real-world manipulation tasks, particularly those requiring precise spatial information.

## 核心内容
Recent advancements in Vision-Language-Action (VLA) models have leveraged pre-trained Vision-Language Models (VLMs) to improve the generalization capabilities. VLMs, typically pre-trained on vision-language understanding tasks, provide rich semantic knowledge and reasoning abilities. However, prior research has shown that VLMs often focus on high-level semantic content and neglect low-level features, limiting their ability to capture detailed spatial information and understand physical dynamics. These aspects, which are crucial for embodied control tasks, remain underexplored in existing pre-training paradigms. In this paper, we investigate the training paradigm for VLAs, and introduce \textbf{UP-VLA}, a \textbf{U}nified VLA model training with both multi-modal \textbf{U}nderstanding and future \textbf{P}rediction objectives, enhancing both high-level semantic comprehension and low-level spatial understanding. Experimental results show that UP-VLA achieves a 33% improvement on the Calvin ABC-D benchmark compared to the previous state-of-the-art method. Additionally, UP-VLA demonstrates improved success rates in real-world manipulation tasks, particularly those requiring precise spatial information.

## 参考
- http://arxiv.org/abs/2501.18867v3

## Overview
Recent advancements in Vision-Language-Action (VLA) models have leveraged pre-trained Vision-Language Models (VLMs) to improve the generalization capabilities. VLMs, typically pre-trained on vision-language understanding tasks, provide rich semantic knowledge and reasoning abilities. However, prior research has shown that VLMs often focus on high-level semantic content and neglect low-level features, limiting their ability to capture detailed spatial information and understand physical dynamics. These aspects, which are crucial for embodied control tasks, remain underexplored in existing pre-training paradigms. In this paper, we investigate the training paradigm for VLAs, and introduce \textbf{UP-VLA}, a \textbf{U}nified VLA model training with both multi-modal \textbf{U}nderstanding and future \textbf{P}rediction objectives, enhancing both high-level semantic comprehension and low-level spatial understanding. Experimental results show that UP-VLA achieves a 33% improvement on the Calvin ABC-D benchmark compared to the previous state-of-the-art method. Additionally, UP-VLA demonstrates improved success rates in real-world manipulation tasks, particularly those requiring precise spatial information.

## Content
Recent advancements in Vision-Language-Action (VLA) models have leveraged pre-trained Vision-Language Models (VLMs) to improve the generalization capabilities. VLMs, typically pre-trained on vision-language understanding tasks, provide rich semantic knowledge and reasoning abilities. However, prior research has shown that VLMs often focus on high-level semantic content and neglect low-level features, limiting their ability to capture detailed spatial information and understand physical dynamics. These aspects, which are crucial for embodied control tasks, remain underexplored in existing pre-training paradigms. In this paper, we investigate the training paradigm for VLAs, and introduce \textbf{UP-VLA}, a \textbf{U}nified VLA model training with both multi-modal \textbf{U}nderstanding and future \textbf{P}rediction objectives, enhancing both high-level semantic comprehension and low-level spatial understanding. Experimental results show that UP-VLA achieves a 33% improvement on the Calvin ABC-D benchmark compared to the previous state-of-the-art method. Additionally, UP-VLA demonstrates improved success rates in real-world manipulation tasks, particularly those requiring precise spatial information.

## 개요
최근 Vision-Language-Action(VLA) 모델의 발전은 사전 학습된 Vision-Language Model(VLM)을 활용하여 일반화 능력을 향상시켰습니다. 일반적으로 시각-언어 이해 작업에 사전 학습된 VLM은 풍부한 의미론적 지식과 추론 능력을 제공합니다. 그러나 기존 연구에 따르면 VLM은 종종 고수준 의미론적 콘텐츠에 집중하고 저수준 특징을 무시하여 세부적인 공간 정보를 포착하고 물리적 역학을 이해하는 능력이 제한됩니다. 구현 제어 작업에 중요한 이러한 측면은 기존 사전 학습 패러다임에서 충분히 탐구되지 않았습니다. 본 논문에서는 VLA의 학습 패러다임을 조사하고, 다중 모달 이해와 미래 예측 목표를 모두 포함하는 통합 VLA 모델 학습인 \textbf{UP-VLA}를 소개합니다. 이는 고수준 의미론적 이해와 저수준 공간 이해를 모두 향상시킵니다. 실험 결과, UP-VLA는 Calvin ABC-D 벤치마크에서 이전 최첨단 방법보다 33% 향상된 성능을 달성했습니다. 또한 UP-VLA는 실제 조작 작업, 특히 정밀한 공간 정보가 필요한 작업에서 향상된 성공률을 보여줍니다.

## 핵심 내용
최근 Vision-Language-Action(VLA) 모델의 발전은 사전 학습된 Vision-Language Model(VLM)을 활용하여 일반화 능력을 향상시켰습니다. 일반적으로 시각-언어 이해 작업에 사전 학습된 VLM은 풍부한 의미론적 지식과 추론 능력을 제공합니다. 그러나 기존 연구에 따르면 VLM은 종종 고수준 의미론적 콘텐츠에 집중하고 저수준 특징을 무시하여 세부적인 공간 정보를 포착하고 물리적 역학을 이해하는 능력이 제한됩니다. 구현 제어 작업에 중요한 이러한 측면은 기존 사전 학습 패러다임에서 충분히 탐구되지 않았습니다. 본 논문에서는 VLA의 학습 패러다임을 조사하고, 다중 모달 이해와 미래 예측 목표를 모두 포함하는 통합 VLA 모델 학습인 \textbf{UP-VLA}를 소개합니다. 이는 고수준 의미론적 이해와 저수준 공간 이해를 모두 향상시킵니다. 실험 결과, UP-VLA는 Calvin ABC-D 벤치마크에서 이전 최첨단 방법보다 33% 향상된 성능을 달성했습니다. 또한 UP-VLA는 실제 조작 작업, 특히 정밀한 공간 정보가 필요한 작업에서 향상된 성공률을 보여줍니다.
