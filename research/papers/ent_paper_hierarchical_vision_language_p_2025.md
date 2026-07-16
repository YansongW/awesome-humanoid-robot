---
$id: ent_paper_hierarchical_vision_language_p_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation
  zh: Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation
  ko: Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation
summary:
  en: Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation is a 2025 work on manipulation for humanoid
    robots.
  zh: Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation is a 2025 work on manipulation for humanoid
    robots.
  ko: Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation is a 2025 work on manipulation for humanoid
    robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hierarchical_vision_language_p
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.22827v3.
sources:
- id: src_001
  type: paper
  title: Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation (arXiv)
  url: https://arxiv.org/abs/2506.22827
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Enabling humanoid robots to reliably execute complex multi-step manipulation tasks is crucial for their effective deployment in industrial and household environments. This paper presents a hierarchical planning and control framework designed to achieve reliable multi-step humanoid manipulation. The proposed system comprises three layers: (1) a low-level RL-based controller responsible for tracking whole-body motion targets; (2) a mid-level set of skill policies trained via imitation learning that produce motion targets for different steps of a task; and (3) a high-level vision-language planning module that determines which skills should be executed and also monitors their completion in real-time using pretrained vision-language models (VLMs). Experimental validation is performed on a Unitree G1 humanoid robot executing a non-prehensile pick-and-place task. Over 40 real-world trials, the hierarchical system achieved a 73% success rate in completing the full manipulation sequence. These experiments confirm the feasibility of the proposed hierarchical system, highlighting the benefits of VLM-based skill planning and monitoring for multi-step manipulation scenarios. See https://vlp-humanoid.github.io/ for video demonstrations of the policy rollout.

## 核心内容
Enabling humanoid robots to reliably execute complex multi-step manipulation tasks is crucial for their effective deployment in industrial and household environments. This paper presents a hierarchical planning and control framework designed to achieve reliable multi-step humanoid manipulation. The proposed system comprises three layers: (1) a low-level RL-based controller responsible for tracking whole-body motion targets; (2) a mid-level set of skill policies trained via imitation learning that produce motion targets for different steps of a task; and (3) a high-level vision-language planning module that determines which skills should be executed and also monitors their completion in real-time using pretrained vision-language models (VLMs). Experimental validation is performed on a Unitree G1 humanoid robot executing a non-prehensile pick-and-place task. Over 40 real-world trials, the hierarchical system achieved a 73% success rate in completing the full manipulation sequence. These experiments confirm the feasibility of the proposed hierarchical system, highlighting the benefits of VLM-based skill planning and monitoring for multi-step manipulation scenarios. See https://vlp-humanoid.github.io/ for video demonstrations of the policy rollout.

## 参考
- http://arxiv.org/abs/2506.22827v3

## Overview
Enabling humanoid robots to reliably execute complex multi-step manipulation tasks is crucial for their effective deployment in industrial and household environments. This paper presents a hierarchical planning and control framework designed to achieve reliable multi-step humanoid manipulation. The proposed system comprises three layers: (1) a low-level RL-based controller responsible for tracking whole-body motion targets; (2) a mid-level set of skill policies trained via imitation learning that produce motion targets for different steps of a task; and (3) a high-level vision-language planning module that determines which skills should be executed and also monitors their completion in real-time using pretrained vision-language models (VLMs). Experimental validation is performed on a Unitree G1 humanoid robot executing a non-prehensile pick-and-place task. Over 40 real-world trials, the hierarchical system achieved a 73% success rate in completing the full manipulation sequence. These experiments confirm the feasibility of the proposed hierarchical system, highlighting the benefits of VLM-based skill planning and monitoring for multi-step manipulation scenarios. See https://vlp-humanoid.github.io/ for video demonstrations of the policy rollout.

## Content
Enabling humanoid robots to reliably execute complex multi-step manipulation tasks is crucial for their effective deployment in industrial and household environments. This paper presents a hierarchical planning and control framework designed to achieve reliable multi-step humanoid manipulation. The proposed system comprises three layers: (1) a low-level RL-based controller responsible for tracking whole-body motion targets; (2) a mid-level set of skill policies trained via imitation learning that produce motion targets for different steps of a task; and (3) a high-level vision-language planning module that determines which skills should be executed and also monitors their completion in real-time using pretrained vision-language models (VLMs). Experimental validation is performed on a Unitree G1 humanoid robot executing a non-prehensile pick-and-place task. Over 40 real-world trials, the hierarchical system achieved a 73% success rate in completing the full manipulation sequence. These experiments confirm the feasibility of the proposed hierarchical system, highlighting the benefits of VLM-based skill planning and monitoring for multi-step manipulation scenarios. See https://vlp-humanoid.github.io/ for video demonstrations of the policy rollout.

## 개요
휴머노이드 로봇이 복잡한 다단계 조작 작업을 안정적으로 수행할 수 있도록 하는 것은 산업 및 가정 환경에서의 효과적인 배치에 필수적입니다. 본 논문은 신뢰할 수 있는 다단계 휴머노이드 조작을 달성하기 위해 설계된 계층적 계획 및 제어 프레임워크를 제시합니다. 제안된 시스템은 세 가지 계층으로 구성됩니다: (1) 전신 동작 목표를 추적하는 저수준 RL 기반 제어기; (2) 작업의 각 단계에 대한 동작 목표를 생성하는 모방 학습을 통해 훈련된 중간 수준의 스킬 정책 세트; (3) 어떤 스킬을 실행해야 하는지 결정하고 사전 훈련된 비전-언어 모델(VLM)을 사용하여 실시간으로 완료 여부를 모니터링하는 고수준 비전-언어 계획 모듈. 실험 검증은 비파지적 집기 및 배치 작업을 수행하는 Unitree G1 휴머노이드 로봇에서 수행되었습니다. 40회 이상의 실제 환경 시험에서 계층적 시스템은 전체 조작 시퀀스를 완료하는 데 73%의 성공률을 달성했습니다. 이러한 실험은 제안된 계층적 시스템의 실현 가능성을 확인하며, 다단계 조작 시나리오에서 VLM 기반 스킬 계획 및 모니터링의 이점을 강조합니다. 정책 롤아웃의 비디오 데모는 https://vlp-humanoid.github.io/ 에서 확인할 수 있습니다.

## 핵심 내용
휴머노이드 로봇이 복잡한 다단계 조작 작업을 안정적으로 수행할 수 있도록 하는 것은 산업 및 가정 환경에서의 효과적인 배치에 필수적입니다. 본 논문은 신뢰할 수 있는 다단계 휴머노이드 조작을 달성하기 위해 설계된 계층적 계획 및 제어 프레임워크를 제시합니다. 제안된 시스템은 세 가지 계층으로 구성됩니다: (1) 전신 동작 목표를 추적하는 저수준 RL 기반 제어기; (2) 작업의 각 단계에 대한 동작 목표를 생성하는 모방 학습을 통해 훈련된 중간 수준의 스킬 정책 세트; (3) 어떤 스킬을 실행해야 하는지 결정하고 사전 훈련된 비전-언어 모델(VLM)을 사용하여 실시간으로 완료 여부를 모니터링하는 고수준 비전-언어 계획 모듈. 실험 검증은 비파지적 집기 및 배치 작업을 수행하는 Unitree G1 휴머노이드 로봇에서 수행되었습니다. 40회 이상의 실제 환경 시험에서 계층적 시스템은 전체 조작 시퀀스를 완료하는 데 73%의 성공률을 달성했습니다. 이러한 실험은 제안된 계층적 시스템의 실현 가능성을 확인하며, 다단계 조작 시나리오에서 VLM 기반 스킬 계획 및 모니터링의 이점을 강조합니다. 정책 롤아웃의 비디오 데모는 https://vlp-humanoid.github.io/ 에서 확인할 수 있습니다.
