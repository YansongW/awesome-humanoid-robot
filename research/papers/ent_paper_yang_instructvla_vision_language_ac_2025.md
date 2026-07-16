---
$id: ent_paper_yang_instructvla_vision_language_ac_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation'
  zh: InstructVLA
  ko: 'InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation'
summary:
  en: 'InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation (InstructVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by University of Science and Technology of China,
    Zhejiang University, Shanghai Artificial Intelligence Laboratory.'
  zh: 'InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation (InstructVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by University of Science and Technology of China,
    Zhejiang University, Shanghai Artificial Intelligence Laboratory.'
  ko: 'InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation (InstructVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by University of Science and Technology of China,
    Zhejiang University, Shanghai Artificial Intelligence Laboratory.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- instructvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.17520v2.
sources:
- id: src_001
  type: paper
  title: 'InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation (arXiv)'
  url: https://arxiv.org/abs/2507.17520
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: InstructVLA source
  url: https://doi.org/10.48550/arXiv.2507.17520
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
To operate effectively in the real world, robots should integrate multimodal reasoning with precise action generation. However, existing vision-language-action (VLA) models often sacrifice one for the other, narrow their abilities to task-specific manipulation data, and suffer catastrophic forgetting of pre-trained vision-language capabilities. To bridge this gap, we introduce InstructVLA, an end-to-end VLA model that preserves the flexible reasoning of large vision-language models (VLMs) while delivering leading manipulation performance with the help of embodied reasoning. InstructVLA introduces a novel training paradigm, Vision-Language-Action Instruction Tuning (VLA-IT), which employs multimodal training with mixture-of-experts adaptation to jointly optimize embodied reasoning and action generation on both standard VLM corpora and a curated 650K-sample VLA-IT dataset. On in-domain SimplerEnv tasks, InstructVLA achieves 33% improvement over SpatialVLA. To evaluate generalization, we introduce SimplerEnv-Instruct, an 80-task benchmark requiring closed-loop control and high-level instruction understanding, where it outperforms a fine-tuned OpenVLA by 96% and an action expert aided by GPT-4o by 29%. Additionally, InstructVLA surpasses baseline VLMs on multimodal tasks and exhibits inference-time scaling by leveraging textual reasoning to boost manipulation performance in both simulated and real-world settings. These results demonstrate InstructVLA's potential for bridging intuitive and steerable human-robot interaction with efficient policy learning.

## 核心内容
To operate effectively in the real world, robots should integrate multimodal reasoning with precise action generation. However, existing vision-language-action (VLA) models often sacrifice one for the other, narrow their abilities to task-specific manipulation data, and suffer catastrophic forgetting of pre-trained vision-language capabilities. To bridge this gap, we introduce InstructVLA, an end-to-end VLA model that preserves the flexible reasoning of large vision-language models (VLMs) while delivering leading manipulation performance with the help of embodied reasoning. InstructVLA introduces a novel training paradigm, Vision-Language-Action Instruction Tuning (VLA-IT), which employs multimodal training with mixture-of-experts adaptation to jointly optimize embodied reasoning and action generation on both standard VLM corpora and a curated 650K-sample VLA-IT dataset. On in-domain SimplerEnv tasks, InstructVLA achieves 33% improvement over SpatialVLA. To evaluate generalization, we introduce SimplerEnv-Instruct, an 80-task benchmark requiring closed-loop control and high-level instruction understanding, where it outperforms a fine-tuned OpenVLA by 96% and an action expert aided by GPT-4o by 29%. Additionally, InstructVLA surpasses baseline VLMs on multimodal tasks and exhibits inference-time scaling by leveraging textual reasoning to boost manipulation performance in both simulated and real-world settings. These results demonstrate InstructVLA's potential for bridging intuitive and steerable human-robot interaction with efficient policy learning.

## 参考
- http://arxiv.org/abs/2507.17520v2

## Overview
To operate effectively in the real world, robots should integrate multimodal reasoning with precise action generation. However, existing vision-language-action (VLA) models often sacrifice one for the other, narrow their abilities to task-specific manipulation data, and suffer catastrophic forgetting of pre-trained vision-language capabilities. To bridge this gap, we introduce InstructVLA, an end-to-end VLA model that preserves the flexible reasoning of large vision-language models (VLMs) while delivering leading manipulation performance with the help of embodied reasoning. InstructVLA introduces a novel training paradigm, Vision-Language-Action Instruction Tuning (VLA-IT), which employs multimodal training with mixture-of-experts adaptation to jointly optimize embodied reasoning and action generation on both standard VLM corpora and a curated 650K-sample VLA-IT dataset. On in-domain SimplerEnv tasks, InstructVLA achieves 33% improvement over SpatialVLA. To evaluate generalization, we introduce SimplerEnv-Instruct, an 80-task benchmark requiring closed-loop control and high-level instruction understanding, where it outperforms a fine-tuned OpenVLA by 96% and an action expert aided by GPT-4o by 29%. Additionally, InstructVLA surpasses baseline VLMs on multimodal tasks and exhibits inference-time scaling by leveraging textual reasoning to boost manipulation performance in both simulated and real-world settings. These results demonstrate InstructVLA's potential for bridging intuitive and steerable human-robot interaction with efficient policy learning.

## Content
To operate effectively in the real world, robots should integrate multimodal reasoning with precise action generation. However, existing vision-language-action (VLA) models often sacrifice one for the other, narrow their abilities to task-specific manipulation data, and suffer catastrophic forgetting of pre-trained vision-language capabilities. To bridge this gap, we introduce InstructVLA, an end-to-end VLA model that preserves the flexible reasoning of large vision-language models (VLMs) while delivering leading manipulation performance with the help of embodied reasoning. InstructVLA introduces a novel training paradigm, Vision-Language-Action Instruction Tuning (VLA-IT), which employs multimodal training with mixture-of-experts adaptation to jointly optimize embodied reasoning and action generation on both standard VLM corpora and a curated 650K-sample VLA-IT dataset. On in-domain SimplerEnv tasks, InstructVLA achieves 33% improvement over SpatialVLA. To evaluate generalization, we introduce SimplerEnv-Instruct, an 80-task benchmark requiring closed-loop control and high-level instruction understanding, where it outperforms a fine-tuned OpenVLA by 96% and an action expert aided by GPT-4o by 29%. Additionally, InstructVLA surpasses baseline VLMs on multimodal tasks and exhibits inference-time scaling by leveraging textual reasoning to boost manipulation performance in both simulated and real-world settings. These results demonstrate InstructVLA's potential for bridging intuitive and steerable human-robot interaction with efficient policy learning.

## 개요
실제 세계에서 효과적으로 작동하기 위해 로봇은 다중 모드 추론과 정밀한 동작 생성을 통합해야 합니다. 그러나 기존의 시각-언어-동작(VLA) 모델은 종종 한쪽을 희생하고, 작업별 조작 데이터에 능력을 제한하며, 사전 훈련된 시각-언어 능력의 치명적 망각을 겪습니다. 이러한 격차를 해소하기 위해 우리는 InstructVLA를 소개합니다. 이는 대규모 시각-언어 모델(VLM)의 유연한 추론을 유지하면서도 체화된 추론의 도움으로 최고 수준의 조작 성능을 제공하는 종단간 VLA 모델입니다. InstructVLA는 새로운 훈련 패러다임인 시각-언어-동작 명령 튜닝(VLA-IT)을 도입하며, 이는 혼합 전문가 적응을 통한 다중 모드 훈련을 활용하여 표준 VLM 코퍼스와 선별된 65만 샘플 VLA-IT 데이터셋에서 체화된 추론과 동작 생성을 공동으로 최적화합니다. 도메인 내 SimplerEnv 작업에서 InstructVLA는 SpatialVLA 대비 33% 향상된 성능을 달성합니다. 일반화를 평가하기 위해 폐루프 제어와 고수준 명령 이해가 필요한 80개 작업 벤치마크인 SimplerEnv-Instruct를 도입했으며, 여기서 미세 조정된 OpenVLA보다 96%, GPT-4o의 지원을 받는 동작 전문가보다 29% 더 우수한 성능을 보입니다. 또한 InstructVLA는 다중 모드 작업에서 기준 VLM을 능가하며, 텍스트 추론을 활용하여 시뮬레이션 및 실제 환경 모두에서 조작 성능을 향상시키는 추론 시간 스케일링을 보여줍니다. 이러한 결과는 InstructVLA가 직관적이고 제어 가능한 인간-로봇 상호작용과 효율적인 정책 학습을 연결할 잠재력을 입증합니다.

## 핵심 내용
실제 세계에서 효과적으로 작동하기 위해 로봇은 다중 모드 추론과 정밀한 동작 생성을 통합해야 합니다. 그러나 기존의 시각-언어-동작(VLA) 모델은 종종 한쪽을 희생하고, 작업별 조작 데이터에 능력을 제한하며, 사전 훈련된 시각-언어 능력의 치명적 망각을 겪습니다. 이러한 격차를 해소하기 위해 우리는 InstructVLA를 소개합니다. 이는 대규모 시각-언어 모델(VLM)의 유연한 추론을 유지하면서도 체화된 추론의 도움으로 최고 수준의 조작 성능을 제공하는 종단간 VLA 모델입니다. InstructVLA는 새로운 훈련 패러다임인 시각-언어-동작 명령 튜닝(VLA-IT)을 도입하며, 이는 혼합 전문가 적응을 통한 다중 모드 훈련을 활용하여 표준 VLM 코퍼스와 선별된 65만 샘플 VLA-IT 데이터셋에서 체화된 추론과 동작 생성을 공동으로 최적화합니다. 도메인 내 SimplerEnv 작업에서 InstructVLA는 SpatialVLA 대비 33% 향상된 성능을 달성합니다. 일반화를 평가하기 위해 폐루프 제어와 고수준 명령 이해가 필요한 80개 작업 벤치마크인 SimplerEnv-Instruct를 도입했으며, 여기서 미세 조정된 OpenVLA보다 96%, GPT-4o의 지원을 받는 동작 전문가보다 29% 더 우수한 성능을 보입니다. 또한 InstructVLA는 다중 모드 작업에서 기준 VLM을 능가하며, 텍스트 추론을 활용하여 시뮬레이션 및 실제 환경 모두에서 조작 성능을 향상시키는 추론 시간 스케일링을 보여줍니다. 이러한 결과는 InstructVLA가 직관적이고 제어 가능한 인간-로봇 상호작용과 효율적인 정책 학습을 연결할 잠재력을 입증합니다.
