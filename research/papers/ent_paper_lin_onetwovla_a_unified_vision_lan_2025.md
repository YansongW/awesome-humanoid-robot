---
$id: ent_paper_lin_onetwovla_a_unified_vision_lan_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning'
  zh: OneTwoVLA
  ko: 'OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning'
summary:
  en: 'OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning (OneTwoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Shanghai Qi Zhi Institute, Shanghai Artificial Intelligence
    Laboratory, Fudan University, Spirit AI.'
  zh: 'OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning (OneTwoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Shanghai Qi Zhi Institute, Shanghai Artificial Intelligence
    Laboratory, Fudan University, Spirit AI.'
  ko: 'OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning (OneTwoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Shanghai Qi Zhi Institute, Shanghai Artificial Intelligence
    Laboratory, Fudan University, Spirit AI.'
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
- onetwovla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.11917v2.
sources:
- id: src_001
  type: paper
  title: 'OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning (arXiv)'
  url: https://arxiv.org/abs/2505.11917
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OneTwoVLA source
  url: https://doi.org/10.48550/arXiv.2505.11917
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
General-purpose robots capable of performing diverse tasks require synergistic reasoning and acting capabilities. However, recent dual-system approaches, which separate high-level reasoning from low-level acting, often suffer from challenges such as limited mutual understanding of capabilities between systems and latency issues. This paper introduces OneTwoVLA, a single unified vision-language-action model that can perform both acting (System One) and reasoning (System Two). Crucially, OneTwoVLA adaptively switches between two modes: explicitly reasoning at critical moments during task execution, and generating actions based on the most recent reasoning at other times. To further unlock OneTwoVLA's reasoning and generalization capabilities, we design a scalable pipeline for synthesizing embodied reasoning-centric vision-language data, used for co-training with robot data. We validate OneTwoVLA's effectiveness through extensive experiments, highlighting its superior performance across four key capabilities: long-horizon task planning, error detection and recovery, natural human-robot interaction, and generalizable visual grounding, enabling the model to perform long-horizon, highly dexterous manipulation tasks such as making hotpot or mixing cocktails.

## 核心内容
General-purpose robots capable of performing diverse tasks require synergistic reasoning and acting capabilities. However, recent dual-system approaches, which separate high-level reasoning from low-level acting, often suffer from challenges such as limited mutual understanding of capabilities between systems and latency issues. This paper introduces OneTwoVLA, a single unified vision-language-action model that can perform both acting (System One) and reasoning (System Two). Crucially, OneTwoVLA adaptively switches between two modes: explicitly reasoning at critical moments during task execution, and generating actions based on the most recent reasoning at other times. To further unlock OneTwoVLA's reasoning and generalization capabilities, we design a scalable pipeline for synthesizing embodied reasoning-centric vision-language data, used for co-training with robot data. We validate OneTwoVLA's effectiveness through extensive experiments, highlighting its superior performance across four key capabilities: long-horizon task planning, error detection and recovery, natural human-robot interaction, and generalizable visual grounding, enabling the model to perform long-horizon, highly dexterous manipulation tasks such as making hotpot or mixing cocktails.

## 参考
- http://arxiv.org/abs/2505.11917v2

## Overview
General-purpose robots capable of performing diverse tasks require synergistic reasoning and acting capabilities. However, recent dual-system approaches, which separate high-level reasoning from low-level acting, often suffer from challenges such as limited mutual understanding of capabilities between systems and latency issues. This paper introduces OneTwoVLA, a single unified vision-language-action model that can perform both acting (System One) and reasoning (System Two). Crucially, OneTwoVLA adaptively switches between two modes: explicitly reasoning at critical moments during task execution, and generating actions based on the most recent reasoning at other times. To further unlock OneTwoVLA's reasoning and generalization capabilities, we design a scalable pipeline for synthesizing embodied reasoning-centric vision-language data, used for co-training with robot data. We validate OneTwoVLA's effectiveness through extensive experiments, highlighting its superior performance across four key capabilities: long-horizon task planning, error detection and recovery, natural human-robot interaction, and generalizable visual grounding, enabling the model to perform long-horizon, highly dexterous manipulation tasks such as making hotpot or mixing cocktails.

## Content
General-purpose robots capable of performing diverse tasks require synergistic reasoning and acting capabilities. However, recent dual-system approaches, which separate high-level reasoning from low-level acting, often suffer from challenges such as limited mutual understanding of capabilities between systems and latency issues. This paper introduces OneTwoVLA, a single unified vision-language-action model that can perform both acting (System One) and reasoning (System Two). Crucially, OneTwoVLA adaptively switches between two modes: explicitly reasoning at critical moments during task execution, and generating actions based on the most recent reasoning at other times. To further unlock OneTwoVLA's reasoning and generalization capabilities, we design a scalable pipeline for synthesizing embodied reasoning-centric vision-language data, used for co-training with robot data. We validate OneTwoVLA's effectiveness through extensive experiments, highlighting its superior performance across four key capabilities: long-horizon task planning, error detection and recovery, natural human-robot interaction, and generalizable visual grounding, enabling the model to perform long-horizon, highly dexterous manipulation tasks such as making hotpot or mixing cocktails.

## 개요
다양한 작업을 수행할 수 있는 범용 로봇은 시너지 효과를 내는 추론 및 행동 능력을 필요로 합니다. 그러나 최근의 이중 시스템 접근 방식은 고수준 추론과 저수준 행동을 분리하여, 시스템 간 능력에 대한 상호 이해 부족 및 지연 문제와 같은 어려움을 겪는 경우가 많습니다. 본 논문은 행동(시스템 1)과 추론(시스템 2)을 모두 수행할 수 있는 단일 통합 비전-언어-행동 모델인 OneTwoVLA를 소개합니다. 핵심적으로, OneTwoVLA는 작업 실행 중 중요한 순간에 명시적으로 추론하고, 그 외 시간에는 가장 최근 추론을 기반으로 행동을 생성하는 두 가지 모드 간에 적응적으로 전환합니다. OneTwoVLA의 추론 및 일반화 능력을 더욱 향상시키기 위해, 로봇 데이터와 공동 학습에 사용되는 구현 추론 중심의 비전-언어 데이터를 합성하기 위한 확장 가능한 파이프라인을 설계합니다. 광범위한 실험을 통해 OneTwoVLA의 효과성을 검증하며, 장기 작업 계획, 오류 감지 및 복구, 자연스러운 인간-로봇 상호작용, 일반화 가능한 시각적 근거라는 네 가지 핵심 능력에서 뛰어난 성능을 강조합니다. 이를 통해 모델이 핫팟 만들기나 칵테일 혼합과 같은 장기적이고 고도의 정밀 조작 작업을 수행할 수 있게 합니다.

## 핵심 내용
다양한 작업을 수행할 수 있는 범용 로봇은 시너지 효과를 내는 추론 및 행동 능력을 필요로 합니다. 그러나 최근의 이중 시스템 접근 방식은 고수준 추론과 저수준 행동을 분리하여, 시스템 간 능력에 대한 상호 이해 부족 및 지연 문제와 같은 어려움을 겪는 경우가 많습니다. 본 논문은 행동(시스템 1)과 추론(시스템 2)을 모두 수행할 수 있는 단일 통합 비전-언어-행동 모델인 OneTwoVLA를 소개합니다. 핵심적으로, OneTwoVLA는 작업 실행 중 중요한 순간에 명시적으로 추론하고, 그 외 시간에는 가장 최근 추론을 기반으로 행동을 생성하는 두 가지 모드 간에 적응적으로 전환합니다. OneTwoVLA의 추론 및 일반화 능력을 더욱 향상시키기 위해, 로봇 데이터와 공동 학습에 사용되는 구현 추론 중심의 비전-언어 데이터를 합성하기 위한 확장 가능한 파이프라인을 설계합니다. 광범위한 실험을 통해 OneTwoVLA의 효과성을 검증하며, 장기 작업 계획, 오류 감지 및 복구, 자연스러운 인간-로봇 상호작용, 일반화 가능한 시각적 근거라는 네 가지 핵심 능력에서 뛰어난 성능을 강조합니다. 이를 통해 모델이 핫팟 만들기나 칵테일 혼합과 같은 장기적이고 고도의 정밀 조작 작업을 수행할 수 있게 합니다.
