---
$id: ent_paper_embracing_bulky_objects_with_h_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning'
  zh: 'Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning'
  ko: 'Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning'
summary:
  en: 'Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.'
  zh: 'Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.'
  ko: 'Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- embracing_bulky_objects_with_h
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.13534v1.
sources:
- id: src_001
  type: paper
  title: 'Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning (arXiv)'
  url: https://arxiv.org/abs/2509.13534
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Whole-body manipulation (WBM) for humanoid robots presents a promising approach for executing embracing tasks involving bulky objects, where traditional grasping relying on end-effectors only remains limited in such scenarios due to inherent stability and payload constraints. This paper introduces a reinforcement learning framework that integrates a pre-trained human motion prior with a neural signed distance field (NSDF) representation to achieve robust whole-body embracing. Our method leverages a teacher-student architecture to distill large-scale human motion data, generating kinematically natural and physically feasible whole-body motion patterns. This facilitates coordinated control across the arms and torso, enabling stable multi-contact interactions that enhance the robustness in manipulation and also the load capacity. The embedded NSDF further provides accurate and continuous geometric perception, improving contact awareness throughout long-horizon tasks. We thoroughly evaluate the approach through comprehensive simulations and real-world experiments. The results demonstrate improved adaptability to diverse shapes and sizes of objects and also successful sim-to-real transfer. These indicate that the proposed framework offers an effective and practical solution for multi-contact and long-horizon WBM tasks of humanoid robots.

## 核心内容
Whole-body manipulation (WBM) for humanoid robots presents a promising approach for executing embracing tasks involving bulky objects, where traditional grasping relying on end-effectors only remains limited in such scenarios due to inherent stability and payload constraints. This paper introduces a reinforcement learning framework that integrates a pre-trained human motion prior with a neural signed distance field (NSDF) representation to achieve robust whole-body embracing. Our method leverages a teacher-student architecture to distill large-scale human motion data, generating kinematically natural and physically feasible whole-body motion patterns. This facilitates coordinated control across the arms and torso, enabling stable multi-contact interactions that enhance the robustness in manipulation and also the load capacity. The embedded NSDF further provides accurate and continuous geometric perception, improving contact awareness throughout long-horizon tasks. We thoroughly evaluate the approach through comprehensive simulations and real-world experiments. The results demonstrate improved adaptability to diverse shapes and sizes of objects and also successful sim-to-real transfer. These indicate that the proposed framework offers an effective and practical solution for multi-contact and long-horizon WBM tasks of humanoid robots.

## 参考
- http://arxiv.org/abs/2509.13534v1

## Overview
Whole-body manipulation (WBM) for humanoid robots presents a promising approach for executing embracing tasks involving bulky objects, where traditional grasping relying on end-effectors only remains limited in such scenarios due to inherent stability and payload constraints. This paper introduces a reinforcement learning framework that integrates a pre-trained human motion prior with a neural signed distance field (NSDF) representation to achieve robust whole-body embracing. Our method leverages a teacher-student architecture to distill large-scale human motion data, generating kinematically natural and physically feasible whole-body motion patterns. This facilitates coordinated control across the arms and torso, enabling stable multi-contact interactions that enhance the robustness in manipulation and also the load capacity. The embedded NSDF further provides accurate and continuous geometric perception, improving contact awareness throughout long-horizon tasks. We thoroughly evaluate the approach through comprehensive simulations and real-world experiments. The results demonstrate improved adaptability to diverse shapes and sizes of objects and also successful sim-to-real transfer. These indicate that the proposed framework offers an effective and practical solution for multi-contact and long-horizon WBM tasks of humanoid robots.

## Content
Whole-body manipulation (WBM) for humanoid robots presents a promising approach for executing embracing tasks involving bulky objects, where traditional grasping relying on end-effectors only remains limited in such scenarios due to inherent stability and payload constraints. This paper introduces a reinforcement learning framework that integrates a pre-trained human motion prior with a neural signed distance field (NSDF) representation to achieve robust whole-body embracing. Our method leverages a teacher-student architecture to distill large-scale human motion data, generating kinematically natural and physically feasible whole-body motion patterns. This facilitates coordinated control across the arms and torso, enabling stable multi-contact interactions that enhance the robustness in manipulation and also the load capacity. The embedded NSDF further provides accurate and continuous geometric perception, improving contact awareness throughout long-horizon tasks. We thoroughly evaluate the approach through comprehensive simulations and real-world experiments. The results demonstrate improved adaptability to diverse shapes and sizes of objects and also successful sim-to-real transfer. These indicate that the proposed framework offers an effective and practical solution for multi-contact and long-horizon WBM tasks of humanoid robots.

## 개요
휴머노이드 로봇의 전신 조작(WBM)은 대형 물체를 포함한 포옹 작업을 실행하는 유망한 접근 방식을 제시합니다. 기존의 엔드 이펙터에만 의존하는 파지 방식은 안정성과 페이로드 제약으로 인해 이러한 시나리오에서 여전히 한계가 있습니다. 본 논문은 사전 훈련된 인간 동작 사전과 신경 부호 거리장(NSDF) 표현을 통합한 강화 학습 프레임워크를 소개하여 강건한 전신 포옹을 달성합니다. 우리의 방법은 교사-학생 아키텍처를 활용하여 대규모 인간 동작 데이터를 증류하고, 운동학적으로 자연스럽고 물리적으로 실현 가능한 전신 동작 패턴을 생성합니다. 이는 팔과 몸통 간의 협조 제어를 촉진하여 안정적인 다중 접촉 상호작용을 가능하게 하고, 조작의 강건성과 하중 용량을 향상시킵니다. 내장된 NSDF는 추가로 정확하고 연속적인 기하학적 인식을 제공하여 장기 작업에서 접촉 인식을 개선합니다. 우리는 포괄적인 시뮬레이션과 실제 실험을 통해 접근 방식을 철저히 평가합니다. 결과는 다양한 모양과 크기의 물체에 대한 적응성 향상과 성공적인 시뮬레이션-실제 전환을 보여줍니다. 이는 제안된 프레임워크가 휴머노이드 로봇의 다중 접촉 및 장기 WBM 작업에 효과적이고 실용적인 솔루션을 제공함을 나타냅니다.

## 핵심 내용
휴머노이드 로봇의 전신 조작(WBM)은 대형 물체를 포함한 포옹 작업을 실행하는 유망한 접근 방식을 제시합니다. 기존의 엔드 이펙터에만 의존하는 파지 방식은 안정성과 페이로드 제약으로 인해 이러한 시나리오에서 여전히 한계가 있습니다. 본 논문은 사전 훈련된 인간 동작 사전과 신경 부호 거리장(NSDF) 표현을 통합한 강화 학습 프레임워크를 소개하여 강건한 전신 포옹을 달성합니다. 우리의 방법은 교사-학생 아키텍처를 활용하여 대규모 인간 동작 데이터를 증류하고, 운동학적으로 자연스럽고 물리적으로 실현 가능한 전신 동작 패턴을 생성합니다. 이는 팔과 몸통 간의 협조 제어를 촉진하여 안정적인 다중 접촉 상호작용을 가능하게 하고, 조작의 강건성과 하중 용량을 향상시킵니다. 내장된 NSDF는 추가로 정확하고 연속적인 기하학적 인식을 제공하여 장기 작업에서 접촉 인식을 개선합니다. 우리는 포괄적인 시뮬레이션과 실제 실험을 통해 접근 방식을 철저히 평가합니다. 결과는 다양한 모양과 크기의 물체에 대한 적응성 향상과 성공적인 시뮬레이션-실제 전환을 보여줍니다. 이는 제안된 프레임워크가 휴머노이드 로봇의 다중 접촉 및 장기 WBM 작업에 효과적이고 실용적인 솔루션을 제공함을 나타냅니다.
