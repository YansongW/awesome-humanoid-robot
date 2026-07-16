---
$id: ent_paper_yang_lohovla_a_unified_vision_langu_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LoHoVLA: A Unified Vision-Language-Action Model for Long-Horizon Embodied Tasks'
  zh: LoHoVLA
  ko: 'LoHoVLA: A Unified Vision-Language-Action Model for Long-Horizon Embodied Tasks'
summary:
  en: 'LoHoVLA: A Unified Vision-Language-Action Model for Long-Horizon Embodied Tasks (LoHoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Fudan University, ShanghaiTech University, Shanghai Jiao Tong University.'
  zh: 'LoHoVLA: A Unified Vision-Language-Action Model for Long-Horizon Embodied Tasks (LoHoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Fudan University, ShanghaiTech University, Shanghai Jiao Tong University.'
  ko: 'LoHoVLA: A Unified Vision-Language-Action Model for Long-Horizon Embodied Tasks (LoHoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Fudan University, ShanghaiTech University, Shanghai Jiao Tong University.'
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
- lohovla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.00411v1.
sources:
- id: src_001
  type: paper
  title: 'LoHoVLA: A Unified Vision-Language-Action Model for Long-Horizon Embodied Tasks (arXiv)'
  url: https://arxiv.org/abs/2506.00411
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: LoHoVLA source
  url: https://doi.org/10.48550/arXiv.2506.00411
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Real-world embodied agents face long-horizon tasks, characterized by high-level goals demanding multi-step solutions beyond single actions. Successfully navigating these requires both high-level task planning (i.e., decomposing goals into sub-tasks) and low-level motion control (i.e., generating precise robot actions). While existing vision language action (VLA) models and hierarchical architectures offer potential in embodied tasks, the former often falter in planning, and the latter can suffer from coordination issues, both hampering performance. We introduce a new unified VLA framework for long-horizon tasks, dubbed LoHoVLA, to overcome these limitations. LoHoVLA leverages a large pretrained vision language model (VLM) as the backbone to jointly generate language and action tokens for sub-task generation and robot action prediction, respectively. This shared representation promotes better generalization across tasks. Additionally, LoHoVLA embraces a hierarchical closed-loop control mechanism to mitigate errors originating from both high-level planning and low-level control. To train LoHoVLA, we introduce LoHoSet, a dataset built on the Ravens simulator, containing 20 long-horizon tasks, each with 1,000 expert demonstrations composed of visual observations, linguistic goals, sub-tasks, and robot actions. Experimental results show that LoHoVLA significantly surpasses both hierarchical and standard VLA approaches on long-horizon embodied tasks in the Ravens simulator. These findings underscore the promise of unified architectures for advancing generalizable embodied intelligence.

## 核心内容
Real-world embodied agents face long-horizon tasks, characterized by high-level goals demanding multi-step solutions beyond single actions. Successfully navigating these requires both high-level task planning (i.e., decomposing goals into sub-tasks) and low-level motion control (i.e., generating precise robot actions). While existing vision language action (VLA) models and hierarchical architectures offer potential in embodied tasks, the former often falter in planning, and the latter can suffer from coordination issues, both hampering performance. We introduce a new unified VLA framework for long-horizon tasks, dubbed LoHoVLA, to overcome these limitations. LoHoVLA leverages a large pretrained vision language model (VLM) as the backbone to jointly generate language and action tokens for sub-task generation and robot action prediction, respectively. This shared representation promotes better generalization across tasks. Additionally, LoHoVLA embraces a hierarchical closed-loop control mechanism to mitigate errors originating from both high-level planning and low-level control. To train LoHoVLA, we introduce LoHoSet, a dataset built on the Ravens simulator, containing 20 long-horizon tasks, each with 1,000 expert demonstrations composed of visual observations, linguistic goals, sub-tasks, and robot actions. Experimental results show that LoHoVLA significantly surpasses both hierarchical and standard VLA approaches on long-horizon embodied tasks in the Ravens simulator. These findings underscore the promise of unified architectures for advancing generalizable embodied intelligence.

## 参考
- http://arxiv.org/abs/2506.00411v1

## Overview
Real-world embodied agents face long-horizon tasks, characterized by high-level goals demanding multi-step solutions beyond single actions. Successfully navigating these requires both high-level task planning (i.e., decomposing goals into sub-tasks) and low-level motion control (i.e., generating precise robot actions). While existing vision language action (VLA) models and hierarchical architectures offer potential in embodied tasks, the former often falter in planning, and the latter can suffer from coordination issues, both hampering performance. We introduce a new unified VLA framework for long-horizon tasks, dubbed LoHoVLA, to overcome these limitations. LoHoVLA leverages a large pretrained vision language model (VLM) as the backbone to jointly generate language and action tokens for sub-task generation and robot action prediction, respectively. This shared representation promotes better generalization across tasks. Additionally, LoHoVLA embraces a hierarchical closed-loop control mechanism to mitigate errors originating from both high-level planning and low-level control. To train LoHoVLA, we introduce LoHoSet, a dataset built on the Ravens simulator, containing 20 long-horizon tasks, each with 1,000 expert demonstrations composed of visual observations, linguistic goals, sub-tasks, and robot actions. Experimental results show that LoHoVLA significantly surpasses both hierarchical and standard VLA approaches on long-horizon embodied tasks in the Ravens simulator. These findings underscore the promise of unified architectures for advancing generalizable embodied intelligence.

## Content
Real-world embodied agents face long-horizon tasks, characterized by high-level goals demanding multi-step solutions beyond single actions. Successfully navigating these requires both high-level task planning (i.e., decomposing goals into sub-tasks) and low-level motion control (i.e., generating precise robot actions). While existing vision language action (VLA) models and hierarchical architectures offer potential in embodied tasks, the former often falter in planning, and the latter can suffer from coordination issues, both hampering performance. We introduce a new unified VLA framework for long-horizon tasks, dubbed LoHoVLA, to overcome these limitations. LoHoVLA leverages a large pretrained vision language model (VLM) as the backbone to jointly generate language and action tokens for sub-task generation and robot action prediction, respectively. This shared representation promotes better generalization across tasks. Additionally, LoHoVLA embraces a hierarchical closed-loop control mechanism to mitigate errors originating from both high-level planning and low-level control. To train LoHoVLA, we introduce LoHoSet, a dataset built on the Ravens simulator, containing 20 long-horizon tasks, each with 1,000 expert demonstrations composed of visual observations, linguistic goals, sub-tasks, and robot actions. Experimental results show that LoHoVLA significantly surpasses both hierarchical and standard VLA approaches on long-horizon embodied tasks in the Ravens simulator. These findings underscore the promise of unified architectures for advancing generalizable embodied intelligence.

## 개요
실제 세계의 임베디드 에이전트는 단일 행동을 넘어 다단계 해결책을 요구하는 높은 수준의 목표로 특징지어지는 장기적 과제에 직면합니다. 이러한 과제를 성공적으로 수행하려면 높은 수준의 작업 계획(즉, 목표를 하위 작업으로 분해)과 낮은 수준의 동작 제어(즉, 정밀한 로봇 행동 생성)가 모두 필요합니다. 기존의 시각-언어-행동(VLA) 모델과 계층적 아키텍처는 임베디드 작업에서 잠재력을 보여주지만, 전자는 계획에서 자주 실패하고 후자는 조정 문제로 어려움을 겪어 성능을 저하시킵니다. 우리는 이러한 한계를 극복하기 위해 LoHoVLA라는 장기적 과제를 위한 새로운 통합 VLA 프레임워크를 소개합니다. LoHoVLA는 대규모 사전 훈련된 시각-언어 모델(VLM)을 백본으로 활용하여 하위 작업 생성과 로봇 행동 예측을 위한 언어 및 행동 토큰을 각각 공동으로 생성합니다. 이 공유 표현은 작업 간 더 나은 일반화를 촉진합니다. 또한 LoHoVLA는 높은 수준의 계획과 낮은 수준의 제어에서 발생하는 오류를 완화하기 위해 계층적 폐쇄 루프 제어 메커니즘을 채택합니다. LoHoVLA를 훈련하기 위해 Ravens 시뮬레이터를 기반으로 구축된 LoHoSet 데이터셋을 소개합니다. 이 데이터셋은 시각적 관찰, 언어적 목표, 하위 작업 및 로봇 행동으로 구성된 1,000개의 전문가 시연을 포함하는 20개의 장기적 과제로 이루어져 있습니다. 실험 결과는 LoHoVLA가 Ravens 시뮬레이터에서 장기적 임베디드 작업에서 계층적 및 표준 VLA 접근 방식을 모두 크게 능가함을 보여줍니다. 이러한 발견은 일반화 가능한 임베디드 지능을 발전시키기 위한 통합 아키텍처의 가능성을 강조합니다.

## 핵심 내용
실제 세계의 임베디드 에이전트는 단일 행동을 넘어 다단계 해결책을 요구하는 높은 수준의 목표로 특징지어지는 장기적 과제에 직면합니다. 이러한 과제를 성공적으로 수행하려면 높은 수준의 작업 계획(즉, 목표를 하위 작업으로 분해)과 낮은 수준의 동작 제어(즉, 정밀한 로봇 행동 생성)가 모두 필요합니다. 기존의 시각-언어-행동(VLA) 모델과 계층적 아키텍처는 임베디드 작업에서 잠재력을 보여주지만, 전자는 계획에서 자주 실패하고 후자는 조정 문제로 어려움을 겪어 성능을 저하시킵니다. 우리는 이러한 한계를 극복하기 위해 LoHoVLA라는 장기적 과제를 위한 새로운 통합 VLA 프레임워크를 소개합니다. LoHoVLA는 대규모 사전 훈련된 시각-언어 모델(VLM)을 백본으로 활용하여 하위 작업 생성과 로봇 행동 예측을 위한 언어 및 행동 토큰을 각각 공동으로 생성합니다. 이 공유 표현은 작업 간 더 나은 일반화를 촉진합니다. 또한 LoHoVLA는 높은 수준의 계획과 낮은 수준의 제어에서 발생하는 오류를 완화하기 위해 계층적 폐쇄 루프 제어 메커니즘을 채택합니다. LoHoVLA를 훈련하기 위해 Ravens 시뮬레이터를 기반으로 구축된 LoHoSet 데이터셋을 소개합니다. 이 데이터셋은 시각적 관찰, 언어적 목표, 하위 작업 및 로봇 행동으로 구성된 1,000개의 전문가 시연을 포함하는 20개의 장기적 과제로 이루어져 있습니다. 실험 결과는 LoHoVLA가 Ravens 시뮬레이터에서 장기적 임베디드 작업에서 계층적 및 표준 VLA 접근 방식을 모두 크게 능가함을 보여줍니다. 이러한 발견은 일반화 가능한 임베디드 지능을 발전시키기 위한 통합 아키텍처의 가능성을 강조합니다.
