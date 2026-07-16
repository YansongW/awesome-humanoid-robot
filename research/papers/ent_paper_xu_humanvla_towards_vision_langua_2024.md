---
$id: ent_paper_xu_humanvla_towards_vision_langua_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumanVLA: Towards Vision-Language Directed Object Rearrangement by Physical Humanoid'
  zh: HumanVLA
  ko: 'HumanVLA: Towards Vision-Language Directed Object Rearrangement by Physical Humanoid'
summary:
  en: 'HumanVLA: Towards Vision-Language Directed Object Rearrangement by Physical Humanoid (HumanVLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University, Tencent Robotics X, and published at NIPS
    2024.'
  zh: 'HumanVLA: Towards Vision-Language Directed Object Rearrangement by Physical Humanoid (HumanVLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University, Tencent Robotics X, and published at NIPS
    2024.'
  ko: 'HumanVLA: Towards Vision-Language Directed Object Rearrangement by Physical Humanoid (HumanVLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University, Tencent Robotics X, and published at NIPS
    2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.19972v2.
sources:
- id: src_001
  type: website
  title: HumanVLA source
  url: http://papers.nips.cc/paper_files/paper/2024/hash/215aeb07b5996c969c0123c3c6ee8f54-Abstract-Conference.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Physical Human-Scene Interaction (HSI) plays a crucial role in numerous applications.   However, existing HSI techniques are limited to specific object dynamics and privileged information, which prevents the development of more comprehensive applications.   To address this limitation, we introduce HumanVLA for general object rearrangement directed by practical vision and language.   A teacher-student framework is utilized to develop HumanVLA.   A state-based teacher policy is trained first using goal-conditioned reinforcement learning and adversarial motion prior.   Then, it is distilled into a vision-language-action model via behavior cloning.   We propose several key insights to facilitate the large-scale learning process.   To support general object rearrangement by physical humanoid, we introduce a novel Human-in-the-Room dataset encompassing various rearrangement tasks.   Through extensive experiments and analysis, we demonstrate the effectiveness of the proposed approach.

## 核心内容
Physical Human-Scene Interaction (HSI) plays a crucial role in numerous applications.   However, existing HSI techniques are limited to specific object dynamics and privileged information, which prevents the development of more comprehensive applications.   To address this limitation, we introduce HumanVLA for general object rearrangement directed by practical vision and language.   A teacher-student framework is utilized to develop HumanVLA.   A state-based teacher policy is trained first using goal-conditioned reinforcement learning and adversarial motion prior.   Then, it is distilled into a vision-language-action model via behavior cloning.   We propose several key insights to facilitate the large-scale learning process.   To support general object rearrangement by physical humanoid, we introduce a novel Human-in-the-Room dataset encompassing various rearrangement tasks.   Through extensive experiments and analysis, we demonstrate the effectiveness of the proposed approach.

## 参考
- http://arxiv.org/abs/2406.19972v2

## Overview
Physical Human-Scene Interaction (HSI) plays a crucial role in numerous applications. However, existing HSI techniques are limited to specific object dynamics and privileged information, which prevents the development of more comprehensive applications. To address this limitation, we introduce HumanVLA for general object rearrangement directed by practical vision and language. A teacher-student framework is utilized to develop HumanVLA. A state-based teacher policy is trained first using goal-conditioned reinforcement learning and adversarial motion prior. Then, it is distilled into a vision-language-action model via behavior cloning. We propose several key insights to facilitate the large-scale learning process. To support general object rearrangement by physical humanoid, we introduce a novel Human-in-the-Room dataset encompassing various rearrangement tasks. Through extensive experiments and analysis, we demonstrate the effectiveness of the proposed approach.

## Content
Physical Human-Scene Interaction (HSI) plays a crucial role in numerous applications. However, existing HSI techniques are limited to specific object dynamics and privileged information, which prevents the development of more comprehensive applications. To address this limitation, we introduce HumanVLA for general object rearrangement directed by practical vision and language. A teacher-student framework is utilized to develop HumanVLA. A state-based teacher policy is trained first using goal-conditioned reinforcement learning and adversarial motion prior. Then, it is distilled into a vision-language-action model via behavior cloning. We propose several key insights to facilitate the large-scale learning process. To support general object rearrangement by physical humanoid, we introduce a novel Human-in-the-Room dataset encompassing various rearrangement tasks. Through extensive experiments and analysis, we demonstrate the effectiveness of the proposed approach.

## 개요
물리적 인간-환경 상호작용(HSI)은 다양한 응용 분야에서 중요한 역할을 한다. 그러나 기존 HSI 기술은 특정 객체 동역학과 특권 정보에 국한되어 있어, 보다 포괄적인 응용 개발을 저해한다. 이러한 한계를 해결하기 위해, 우리는 실용적인 시각 및 언어 명령에 기반한 일반 객체 재배치를 위한 HumanVLA를 소개한다. HumanVLA 개발에는 교사-학생 프레임워크가 활용된다. 먼저 목표 조건화 강화 학습과 적대적 운동 사전을 사용하여 상태 기반 교사 정책을 훈련한다. 그런 다음 행동 복제를 통해 이를 시각-언어-행동 모델로 증류한다. 대규모 학습 과정을 촉진하기 위해 몇 가지 핵심 통찰을 제안한다. 물리적 휴머노이드에 의한 일반 객체 재배치를 지원하기 위해, 다양한 재배치 작업을 포함하는 새로운 Human-in-the-Room 데이터셋을 도입한다. 광범위한 실험과 분석을 통해 제안된 접근 방식의 효과를 입증한다.

## 핵심 내용
물리적 인간-환경 상호작용(HSI)은 다양한 응용 분야에서 중요한 역할을 한다. 그러나 기존 HSI 기술은 특정 객체 동역학과 특권 정보에 국한되어 있어, 보다 포괄적인 응용 개발을 저해한다. 이러한 한계를 해결하기 위해, 우리는 실용적인 시각 및 언어 명령에 기반한 일반 객체 재배치를 위한 HumanVLA를 소개한다. HumanVLA 개발에는 교사-학생 프레임워크가 활용된다. 먼저 목표 조건화 강화 학습과 적대적 운동 사전을 사용하여 상태 기반 교사 정책을 훈련한다. 그런 다음 행동 복제를 통해 이를 시각-언어-행동 모델로 증류한다. 대규모 학습 과정을 촉진하기 위해 몇 가지 핵심 통찰을 제안한다. 물리적 휴머노이드에 의한 일반 객체 재배치를 지원하기 위해, 다양한 재배치 작업을 포함하는 새로운 Human-in-the-Room 데이터셋을 도입한다. 광범위한 실험과 분석을 통해 제안된 접근 방식의 효과를 입증한다.
