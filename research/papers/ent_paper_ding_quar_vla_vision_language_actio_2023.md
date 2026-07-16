---
$id: ent_paper_ding_quar_vla_vision_language_actio_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'QUAR-VLA: Vision-Language-Action Model for Quadruped Robots'
  zh: QUAR-VLA
  ko: 'QUAR-VLA: Vision-Language-Action Model for Quadruped Robots'
summary:
  en: 'QUAR-VLA: Vision-Language-Action Model for Quadruped Robots (QUAR-VLA), is a 2023 large vision-language-action model
    for robotic manipulation, introduced by Westlake University, Zhejiang University, and published at ECCV24.'
  zh: 'QUAR-VLA: Vision-Language-Action Model for Quadruped Robots (QUAR-VLA), is a 2023 large vision-language-action model
    for robotic manipulation, introduced by Westlake University, Zhejiang University, and published at ECCV24.'
  ko: 'QUAR-VLA: Vision-Language-Action Model for Quadruped Robots (QUAR-VLA), is a 2023 large vision-language-action model
    for robotic manipulation, introduced by Westlake University, Zhejiang University, and published at ECCV24.'
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
- quar_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2312.14457v6.
sources:
- id: src_001
  type: website
  title: QUAR-VLA source
  url: https://doi.org/10.1007/978-3-031-72652-1_21
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
The important manifestation of robot intelligence is the ability to naturally interact and autonomously make decisions. Traditional approaches to robot control often compartmentalize perception, planning, and decision-making, simplifying system design but limiting the synergy between different information streams. This compartmentalization poses challenges in achieving seamless autonomous reasoning, decision-making, and action execution. To address these limitations, a novel paradigm, named Vision-Language-Action tasks for QUAdruped Robots (QUAR-VLA), has been introduced in this paper. This approach tightly integrates visual information and instructions to generate executable actions, effectively merging perception, planning, and decision-making. The central idea is to elevate the overall intelligence of the robot. Within this framework, a notable challenge lies in aligning fine-grained instructions with visual perception information. This emphasizes the complexity involved in ensuring that the robot accurately interprets and acts upon detailed instructions in harmony with its visual observations. Consequently, we propose QUAdruped Robotic Transformer (QUART), a family of VLA models to integrate visual information and instructions from diverse modalities as input and generates executable actions for real-world robots and present QUAdruped Robot Dataset (QUARD), a large-scale multi-task dataset including navigation, complex terrain locomotion, and whole-body manipulation tasks for training QUART models. Our extensive evaluation (4000 evaluation trials) shows that our approach leads to performant robotic policies and enables QUART to obtain a range of emergent capabilities.

## 核心内容
The important manifestation of robot intelligence is the ability to naturally interact and autonomously make decisions. Traditional approaches to robot control often compartmentalize perception, planning, and decision-making, simplifying system design but limiting the synergy between different information streams. This compartmentalization poses challenges in achieving seamless autonomous reasoning, decision-making, and action execution. To address these limitations, a novel paradigm, named Vision-Language-Action tasks for QUAdruped Robots (QUAR-VLA), has been introduced in this paper. This approach tightly integrates visual information and instructions to generate executable actions, effectively merging perception, planning, and decision-making. The central idea is to elevate the overall intelligence of the robot. Within this framework, a notable challenge lies in aligning fine-grained instructions with visual perception information. This emphasizes the complexity involved in ensuring that the robot accurately interprets and acts upon detailed instructions in harmony with its visual observations. Consequently, we propose QUAdruped Robotic Transformer (QUART), a family of VLA models to integrate visual information and instructions from diverse modalities as input and generates executable actions for real-world robots and present QUAdruped Robot Dataset (QUARD), a large-scale multi-task dataset including navigation, complex terrain locomotion, and whole-body manipulation tasks for training QUART models. Our extensive evaluation (4000 evaluation trials) shows that our approach leads to performant robotic policies and enables QUART to obtain a range of emergent capabilities.

## 参考
- http://arxiv.org/abs/2312.14457v6

## Overview
The important manifestation of robot intelligence is the ability to naturally interact and autonomously make decisions. Traditional approaches to robot control often compartmentalize perception, planning, and decision-making, simplifying system design but limiting the synergy between different information streams. This compartmentalization poses challenges in achieving seamless autonomous reasoning, decision-making, and action execution. To address these limitations, a novel paradigm, named Vision-Language-Action tasks for QUAdruped Robots (QUAR-VLA), has been introduced in this paper. This approach tightly integrates visual information and instructions to generate executable actions, effectively merging perception, planning, and decision-making. The central idea is to elevate the overall intelligence of the robot. Within this framework, a notable challenge lies in aligning fine-grained instructions with visual perception information. This emphasizes the complexity involved in ensuring that the robot accurately interprets and acts upon detailed instructions in harmony with its visual observations. Consequently, we propose QUAdruped Robotic Transformer (QUART), a family of VLA models to integrate visual information and instructions from diverse modalities as input and generates executable actions for real-world robots and present QUAdruped Robot Dataset (QUARD), a large-scale multi-task dataset including navigation, complex terrain locomotion, and whole-body manipulation tasks for training QUART models. Our extensive evaluation (4000 evaluation trials) shows that our approach leads to performant robotic policies and enables QUART to obtain a range of emergent capabilities.

## Content
The important manifestation of robot intelligence is the ability to naturally interact and autonomously make decisions. Traditional approaches to robot control often compartmentalize perception, planning, and decision-making, simplifying system design but limiting the synergy between different information streams. This compartmentalization poses challenges in achieving seamless autonomous reasoning, decision-making, and action execution. To address these limitations, a novel paradigm, named Vision-Language-Action tasks for QUAdruped Robots (QUAR-VLA), has been introduced in this paper. This approach tightly integrates visual information and instructions to generate executable actions, effectively merging perception, planning, and decision-making. The central idea is to elevate the overall intelligence of the robot. Within this framework, a notable challenge lies in aligning fine-grained instructions with visual perception information. This emphasizes the complexity involved in ensuring that the robot accurately interprets and acts upon detailed instructions in harmony with its visual observations. Consequently, we propose QUAdruped Robotic Transformer (QUART), a family of VLA models to integrate visual information and instructions from diverse modalities as input and generates executable actions for real-world robots and present QUAdruped Robot Dataset (QUARD), a large-scale multi-task dataset including navigation, complex terrain locomotion, and whole-body manipulation tasks for training QUART models. Our extensive evaluation (4000 evaluation trials) shows that our approach leads to performant robotic policies and enables QUART to obtain a range of emergent capabilities.

## 개요
로봇 지능의 중요한 표현은 자연스러운 상호작용과 자율적 의사 결정 능력입니다. 전통적인 로봇 제어 접근 방식은 종종 인식, 계획 및 의사 결정을 분리하여 시스템 설계를 단순화하지만, 다양한 정보 흐름 간의 시너지를 제한합니다. 이러한 분리는 원활한 자율 추론, 의사 결정 및 행동 실행을 달성하는 데 어려움을 초래합니다. 이러한 한계를 해결하기 위해, 본 논문에서는 QUAR-VLA(Quadruped Robots를 위한 Vision-Language-Action 작업)라는 새로운 패러다임을 소개합니다. 이 접근 방식은 시각 정보와 명령을 긴밀하게 통합하여 실행 가능한 행동을 생성하며, 인식, 계획 및 의사 결정을 효과적으로 병합합니다. 핵심 아이디어는 로봇의 전반적인 지능을 향상시키는 것입니다. 이 프레임워크 내에서 주목할 만한 과제는 세분화된 명령을 시각적 인식 정보와 정렬하는 데 있습니다. 이는 로봇이 시각적 관찰과 조화를 이루며 세부 명령을 정확히 해석하고 실행하도록 보장하는 복잡성을 강조합니다. 이에 따라, 우리는 다양한 양식의 시각 정보와 명령을 입력으로 통합하고 실제 로봇을 위한 실행 가능한 행동을 생성하는 VLA 모델군인 QUART(Quadruped Robotic Transformer)를 제안하며, QUART 모델 훈련을 위한 내비게이션, 복잡한 지형 이동 및 전신 조작 작업을 포함한 대규모 멀티태스크 데이터셋인 QUARD(Quadruped Robot Dataset)를 제시합니다. 광범위한 평가(4000회 평가 시험)를 통해 우리의 접근 방식이 성능이 뛰어난 로봇 정책을 이끌어내고 QUART가 다양한 창발적 능력을 획득할 수 있게 함을 보여줍니다.

## 핵심 내용
로봇 지능의 중요한 표현은 자연스러운 상호작용과 자율적 의사 결정 능력입니다. 전통적인 로봇 제어 접근 방식은 종종 인식, 계획 및 의사 결정을 분리하여 시스템 설계를 단순화하지만, 다양한 정보 흐름 간의 시너지를 제한합니다. 이러한 분리는 원활한 자율 추론, 의사 결정 및 행동 실행을 달성하는 데 어려움을 초래합니다. 이러한 한계를 해결하기 위해, 본 논문에서는 QUAR-VLA(Quadruped Robots를 위한 Vision-Language-Action 작업)라는 새로운 패러다임을 소개합니다. 이 접근 방식은 시각 정보와 명령을 긴밀하게 통합하여 실행 가능한 행동을 생성하며, 인식, 계획 및 의사 결정을 효과적으로 병합합니다. 핵심 아이디어는 로봇의 전반적인 지능을 향상시키는 것입니다. 이 프레임워크 내에서 주목할 만한 과제는 세분화된 명령을 시각적 인식 정보와 정렬하는 데 있습니다. 이는 로봇이 시각적 관찰과 조화를 이루며 세부 명령을 정확히 해석하고 실행하도록 보장하는 복잡성을 강조합니다. 이에 따라, 우리는 다양한 양식의 시각 정보와 명령을 입력으로 통합하고 실제 로봇을 위한 실행 가능한 행동을 생성하는 VLA 모델군인 QUART(Quadruped Robotic Transformer)를 제안하며, QUART 모델 훈련을 위한 내비게이션, 복잡한 지형 이동 및 전신 조작 작업을 포함한 대규모 멀티태스크 데이터셋인 QUARD(Quadruped Robot Dataset)를 제시합니다. 광범위한 평가(4000회 평가 시험)를 통해 우리의 접근 방식이 성능이 뛰어난 로봇 정책을 이끌어내고 QUART가 다양한 창발적 능력을 획득할 수 있게 함을 보여줍니다.
