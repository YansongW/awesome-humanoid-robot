---
$id: ent_paper_zhou_autovla_a_vision_language_acti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement
    Fine-Tuning'
  zh: AutoVLA
  ko: 'AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement
    Fine-Tuning'
summary:
  en: 'AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement
    Fine-Tuning (AutoVLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by University
    of California, Los Angeles, and published at NIPS25.'
  zh: 'AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement
    Fine-Tuning (AutoVLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by University
    of California, Los Angeles, and published at NIPS25.'
  ko: 'AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement
    Fine-Tuning (AutoVLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by University
    of California, Los Angeles, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- autovla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.13757v3.
sources:
- id: src_001
  type: paper
  title: 'AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement
    Fine-Tuning (arXiv)'
  url: https://arxiv.org/abs/2506.13757
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: AutoVLA source
  url: https://doi.org/10.48550/arXiv.2506.13757
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent advancements in Vision-Language-Action (VLA) models have shown promise for end-to-end autonomous driving by leveraging world knowledge and reasoning capabilities. However, current VLA models often struggle with physically infeasible action outputs, complex model structures, or unnecessarily long reasoning. In this paper, we propose AutoVLA, a novel VLA model that unifies reasoning and action generation within a single autoregressive generation model for end-to-end autonomous driving. AutoVLA performs semantic reasoning and trajectory planning directly from raw visual inputs and language instructions. We tokenize continuous trajectories into discrete, feasible actions, enabling direct integration into the language model. For training, we employ supervised fine-tuning to equip the model with dual thinking modes: fast thinking (trajectory-only) and slow thinking (enhanced with chain-of-thought reasoning). To further enhance planning performance and efficiency, we introduce a reinforcement fine-tuning method based on Group Relative Policy Optimization (GRPO), reducing unnecessary reasoning in straightforward scenarios. Extensive experiments across real-world and simulated datasets and benchmarks, including nuPlan, nuScenes, Waymo, and CARLA, demonstrate the competitive performance of AutoVLA in both open-loop and closed-loop settings. Qualitative results showcase the adaptive reasoning and accurate planning capabilities of AutoVLA in diverse scenarios.

## 核心内容
Recent advancements in Vision-Language-Action (VLA) models have shown promise for end-to-end autonomous driving by leveraging world knowledge and reasoning capabilities. However, current VLA models often struggle with physically infeasible action outputs, complex model structures, or unnecessarily long reasoning. In this paper, we propose AutoVLA, a novel VLA model that unifies reasoning and action generation within a single autoregressive generation model for end-to-end autonomous driving. AutoVLA performs semantic reasoning and trajectory planning directly from raw visual inputs and language instructions. We tokenize continuous trajectories into discrete, feasible actions, enabling direct integration into the language model. For training, we employ supervised fine-tuning to equip the model with dual thinking modes: fast thinking (trajectory-only) and slow thinking (enhanced with chain-of-thought reasoning). To further enhance planning performance and efficiency, we introduce a reinforcement fine-tuning method based on Group Relative Policy Optimization (GRPO), reducing unnecessary reasoning in straightforward scenarios. Extensive experiments across real-world and simulated datasets and benchmarks, including nuPlan, nuScenes, Waymo, and CARLA, demonstrate the competitive performance of AutoVLA in both open-loop and closed-loop settings. Qualitative results showcase the adaptive reasoning and accurate planning capabilities of AutoVLA in diverse scenarios.

## 参考
- http://arxiv.org/abs/2506.13757v3

## Overview
Recent advancements in Vision-Language-Action (VLA) models have shown promise for end-to-end autonomous driving by leveraging world knowledge and reasoning capabilities. However, current VLA models often struggle with physically infeasible action outputs, complex model structures, or unnecessarily long reasoning. In this paper, we propose AutoVLA, a novel VLA model that unifies reasoning and action generation within a single autoregressive generation model for end-to-end autonomous driving. AutoVLA performs semantic reasoning and trajectory planning directly from raw visual inputs and language instructions. We tokenize continuous trajectories into discrete, feasible actions, enabling direct integration into the language model. For training, we employ supervised fine-tuning to equip the model with dual thinking modes: fast thinking (trajectory-only) and slow thinking (enhanced with chain-of-thought reasoning). To further enhance planning performance and efficiency, we introduce a reinforcement fine-tuning method based on Group Relative Policy Optimization (GRPO), reducing unnecessary reasoning in straightforward scenarios. Extensive experiments across real-world and simulated datasets and benchmarks, including nuPlan, nuScenes, Waymo, and CARLA, demonstrate the competitive performance of AutoVLA in both open-loop and closed-loop settings. Qualitative results showcase the adaptive reasoning and accurate planning capabilities of AutoVLA in diverse scenarios.

## Content
Recent advancements in Vision-Language-Action (VLA) models have shown promise for end-to-end autonomous driving by leveraging world knowledge and reasoning capabilities. However, current VLA models often struggle with physically infeasible action outputs, complex model structures, or unnecessarily long reasoning. In this paper, we propose AutoVLA, a novel VLA model that unifies reasoning and action generation within a single autoregressive generation model for end-to-end autonomous driving. AutoVLA performs semantic reasoning and trajectory planning directly from raw visual inputs and language instructions. We tokenize continuous trajectories into discrete, feasible actions, enabling direct integration into the language model. For training, we employ supervised fine-tuning to equip the model with dual thinking modes: fast thinking (trajectory-only) and slow thinking (enhanced with chain-of-thought reasoning). To further enhance planning performance and efficiency, we introduce a reinforcement fine-tuning method based on Group Relative Policy Optimization (GRPO), reducing unnecessary reasoning in straightforward scenarios. Extensive experiments across real-world and simulated datasets and benchmarks, including nuPlan, nuScenes, Waymo, and CARLA, demonstrate the competitive performance of AutoVLA in both open-loop and closed-loop settings. Qualitative results showcase the adaptive reasoning and accurate planning capabilities of AutoVLA in diverse scenarios.

## 개요
최근 Vision-Language-Action(VLA) 모델의 발전은 세계 지식과 추론 능력을 활용하여 엔드투엔드 자율 주행에 가능성을 보여주고 있습니다. 그러나 현재의 VLA 모델은 물리적으로 실행 불가능한 행동 출력, 복잡한 모델 구조, 또는 불필요하게 긴 추론으로 인해 어려움을 겪는 경우가 많습니다. 본 논문에서는 엔드투엔드 자율 주행을 위해 단일 자기회귀 생성 모델 내에서 추론과 행동 생성을 통합하는 새로운 VLA 모델인 AutoVLA를 제안합니다. AutoVLA는 원시 시각 입력과 언어 명령으로부터 직접 의미 추론과 궤적 계획을 수행합니다. 연속적인 궤적을 이산적이고 실행 가능한 행동으로 토큰화하여 언어 모델에 직접 통합할 수 있도록 합니다. 훈련을 위해, 우리는 지도 미세 조정을 사용하여 모델에 이중 사고 모드, 즉 빠른 사고(궤적 전용)와 느린 사고(사고 사슬 추론 강화)를 부여합니다. 계획 성능과 효율성을 더욱 향상시키기 위해, 우리는 그룹 상대 정책 최적화(GRPO)에 기반한 강화 미세 조정 방법을 도입하여 간단한 시나리오에서 불필요한 추론을 줄입니다. nuPlan, nuScenes, Waymo 및 CARLA를 포함한 실제 및 시뮬레이션 데이터셋과 벤치마크에 걸친 광범위한 실험은 오픈 루프 및 폐쇄 루프 설정 모두에서 AutoVLA의 경쟁력 있는 성능을 입증합니다. 정성적 결과는 다양한 시나리오에서 AutoVLA의 적응형 추론과 정확한 계획 능력을 보여줍니다.

## 핵심 내용
최근 Vision-Language-Action(VLA) 모델의 발전은 세계 지식과 추론 능력을 활용하여 엔드투엔드 자율 주행에 가능성을 보여주고 있습니다. 그러나 현재의 VLA 모델은 물리적으로 실행 불가능한 행동 출력, 복잡한 모델 구조, 또는 불필요하게 긴 추론으로 인해 어려움을 겪는 경우가 많습니다. 본 논문에서는 엔드투엔드 자율 주행을 위해 단일 자기회귀 생성 모델 내에서 추론과 행동 생성을 통합하는 새로운 VLA 모델인 AutoVLA를 제안합니다. AutoVLA는 원시 시각 입력과 언어 명령으로부터 직접 의미 추론과 궤적 계획을 수행합니다. 연속적인 궤적을 이산적이고 실행 가능한 행동으로 토큰화하여 언어 모델에 직접 통합할 수 있도록 합니다. 훈련을 위해, 우리는 지도 미세 조정을 사용하여 모델에 이중 사고 모드, 즉 빠른 사고(궤적 전용)와 느린 사고(사고 사슬 추론 강화)를 부여합니다. 계획 성능과 효율성을 더욱 향상시키기 위해, 우리는 그룹 상대 정책 최적화(GRPO)에 기반한 강화 미세 조정 방법을 도입하여 간단한 시나리오에서 불필요한 추론을 줄입니다. nuPlan, nuScenes, Waymo 및 CARLA를 포함한 실제 및 시뮬레이션 데이터셋과 벤치마크에 걸친 광범위한 실험은 오픈 루프 및 폐쇄 루프 설정 모두에서 AutoVLA의 경쟁력 있는 성능을 입증합니다. 정성적 결과는 다양한 시나리오에서 AutoVLA의 적응형 추론과 정확한 계획 능력을 보여줍니다.
