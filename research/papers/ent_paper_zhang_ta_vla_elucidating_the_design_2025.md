---
$id: ent_paper_zhang_ta_vla_elucidating_the_design_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models'
  zh: TA-VLA
  ko: 'TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models'
summary:
  en: 'TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models (TA-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing Academy of Artificial Intelligence, BAAI, Institute for AI Industry
    Research (AIR), Tsinghua Univeristy, Nanyang Technological University, and published at CoRL25.'
  zh: 'TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models (TA-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing Academy of Artificial Intelligence, BAAI, Institute for AI Industry
    Research (AIR), Tsinghua Univeristy, Nanyang Technological University, and published at CoRL25.'
  ko: 'TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models (TA-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing Academy of Artificial Intelligence, BAAI, Institute for AI Industry
    Research (AIR), Tsinghua Univeristy, Nanyang Technological University, and published at CoRL25.'
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
- ta_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.07962v1.
sources:
- id: src_001
  type: paper
  title: 'TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2509.07962
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: TA-VLA source
  url: https://doi.org/10.48550/arXiv.2509.07962
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Many robotic manipulation tasks require sensing and responding to force signals such as torque to assess whether the task has been successfully completed and to enable closed-loop control. However, current Vision-Language-Action (VLA) models lack the ability to integrate such subtle physical feedback. In this work, we explore Torque-aware VLA models, aiming to bridge this gap by systematically studying the design space for incorporating torque signals into existing VLA architectures. We identify and evaluate several strategies, leading to three key findings. First, introducing torque adapters into the decoder consistently outperforms inserting them into the encoder.Third, inspired by joint prediction and planning paradigms in autonomous driving, we propose predicting torque as an auxiliary output, which further improves performance. This strategy encourages the model to build a physically grounded internal representation of interaction dynamics. Extensive quantitative and qualitative experiments across contact-rich manipulation benchmarks validate our findings.

## 核心内容
Many robotic manipulation tasks require sensing and responding to force signals such as torque to assess whether the task has been successfully completed and to enable closed-loop control. However, current Vision-Language-Action (VLA) models lack the ability to integrate such subtle physical feedback. In this work, we explore Torque-aware VLA models, aiming to bridge this gap by systematically studying the design space for incorporating torque signals into existing VLA architectures. We identify and evaluate several strategies, leading to three key findings. First, introducing torque adapters into the decoder consistently outperforms inserting them into the encoder.Third, inspired by joint prediction and planning paradigms in autonomous driving, we propose predicting torque as an auxiliary output, which further improves performance. This strategy encourages the model to build a physically grounded internal representation of interaction dynamics. Extensive quantitative and qualitative experiments across contact-rich manipulation benchmarks validate our findings.

## 参考
- http://arxiv.org/abs/2509.07962v1

## Overview
Many robotic manipulation tasks require sensing and responding to force signals such as torque to assess whether the task has been successfully completed and to enable closed-loop control. However, current Vision-Language-Action (VLA) models lack the ability to integrate such subtle physical feedback. In this work, we explore Torque-aware VLA models, aiming to bridge this gap by systematically studying the design space for incorporating torque signals into existing VLA architectures. We identify and evaluate several strategies, leading to three key findings. First, introducing torque adapters into the decoder consistently outperforms inserting them into the encoder. Third, inspired by joint prediction and planning paradigms in autonomous driving, we propose predicting torque as an auxiliary output, which further improves performance. This strategy encourages the model to build a physically grounded internal representation of interaction dynamics. Extensive quantitative and qualitative experiments across contact-rich manipulation benchmarks validate our findings.

## Content
Many robotic manipulation tasks require sensing and responding to force signals such as torque to assess whether the task has been successfully completed and to enable closed-loop control. However, current Vision-Language-Action (VLA) models lack the ability to integrate such subtle physical feedback. In this work, we explore Torque-aware VLA models, aiming to bridge this gap by systematically studying the design space for incorporating torque signals into existing VLA architectures. We identify and evaluate several strategies, leading to three key findings. First, introducing torque adapters into the decoder consistently outperforms inserting them into the encoder. Third, inspired by joint prediction and planning paradigms in autonomous driving, we propose predicting torque as an auxiliary output, which further improves performance. This strategy encourages the model to build a physically grounded internal representation of interaction dynamics. Extensive quantitative and qualitative experiments across contact-rich manipulation benchmarks validate our findings.

## 개요
많은 로봇 조작 작업은 작업이 성공적으로 완료되었는지 평가하고 폐쇄 루프 제어를 가능하게 하기 위해 토크와 같은 힘 신호를 감지하고 반응해야 합니다. 그러나 현재의 Vision-Language-Action(VLA) 모델은 이러한 미묘한 물리적 피드백을 통합하는 능력이 부족합니다. 본 연구에서는 Torque-aware VLA 모델을 탐구하며, 기존 VLA 아키텍처에 토크 신호를 통합하기 위한 설계 공간을 체계적으로 연구하여 이러한 격차를 해소하고자 합니다. 우리는 여러 전략을 식별하고 평가하여 세 가지 주요 발견을 도출했습니다. 첫째, 디코더에 토크 어댑터를 도입하는 것이 인코더에 삽입하는 것보다 일관되게 더 나은 성능을 보였습니다. 셋째, 자율 주행에서의 공동 예측 및 계획 패러다임에서 영감을 받아, 우리는 보조 출력으로 토크를 예측하는 것을 제안하며, 이는 성능을 더욱 향상시킵니다. 이 전략은 모델이 상호작용 역학에 대한 물리적으로 기반한 내부 표현을 구축하도록 장려합니다. 접촉이 많은 조작 벤치마크에 걸친 광범위한 정량적 및 정성적 실험을 통해 우리의 발견을 검증했습니다.

## 핵심 내용
많은 로봇 조작 작업은 작업이 성공적으로 완료되었는지 평가하고 폐쇄 루프 제어를 가능하게 하기 위해 토크와 같은 힘 신호를 감지하고 반응해야 합니다. 그러나 현재의 Vision-Language-Action(VLA) 모델은 이러한 미묘한 물리적 피드백을 통합하는 능력이 부족합니다. 본 연구에서는 Torque-aware VLA 모델을 탐구하며, 기존 VLA 아키텍처에 토크 신호를 통합하기 위한 설계 공간을 체계적으로 연구하여 이러한 격차를 해소하고자 합니다. 우리는 여러 전략을 식별하고 평가하여 세 가지 주요 발견을 도출했습니다. 첫째, 디코더에 토크 어댑터를 도입하는 것이 인코더에 삽입하는 것보다 일관되게 더 나은 성능을 보였습니다. 셋째, 자율 주행에서의 공동 예측 및 계획 패러다임에서 영감을 받아, 우리는 보조 출력으로 토크를 예측하는 것을 제안하며, 이는 성능을 더욱 향상시킵니다. 이 전략은 모델이 상호작용 역학에 대한 물리적으로 기반한 내부 표현을 구축하도록 장려합니다. 접촉이 많은 조작 벤치마크에 걸친 광범위한 정량적 및 정성적 실험을 통해 우리의 발견을 검증했습니다.
