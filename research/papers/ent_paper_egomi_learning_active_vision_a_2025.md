---
$id: ent_paper_egomi_learning_active_vision_a_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoMI: Learning Active Vision and Whole-Body Manipulation from Egocentric Human Demonstrations'
  zh: 'EgoMI: Learning Active Vision and Whole-Body Manipulation from Egocentric Human Demonstrations'
  ko: 'EgoMI: Learning Active Vision and Whole-Body Manipulation from Egocentric Human Demonstrations'
summary:
  en: 'EgoMI: Learning Active Vision and Whole-Body Manipulation from Egocentric Human Demonstrations is a 2025 work on manipulation
    for humanoid robots.'
  zh: 'EgoMI: Learning Active Vision and Whole-Body Manipulation from Egocentric Human Demonstrations is a 2025 work on manipulation
    for humanoid robots.'
  ko: 'EgoMI: Learning Active Vision and Whole-Body Manipulation from Egocentric Human Demonstrations is a 2025 work on manipulation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- egomi
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.00153v2.
sources:
- id: src_001
  type: paper
  title: 'EgoMI: Learning Active Vision and Whole-Body Manipulation from Egocentric Human Demonstrations (arXiv)'
  url: https://arxiv.org/abs/2511.00153
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Imitation learning from human demonstrations offers a promising approach for robot skill acquisition, but egocentric human data introduces fundamental challenges due to the embodiment gap. During manipulation, humans actively coordinate head and hand movements, continuously reposition their viewpoint and use pre-action visual fixation search strategies to locate relevant objects. These behaviors create dynamic, task-driven head motions that static robot sensing systems cannot replicate, leading to a significant distribution shift that degrades policy performance. We present EgoMI (Egocentric Manipulation Interface), a framework that captures synchronized end-effector and active head trajectories during manipulation tasks, resulting in data that can be retargeted to compatible semi-humanoid robot embodiments. To handle rapid and wide-spanning head viewpoint changes, we introduce a memory-augmented policy that selectively incorporates historical observations. We evaluate our approach on a bimanual robot equipped with an actuated camera head and find that policies with explicit head-motion modeling consistently outperform baseline methods. Results suggest that coordinated hand-eye learning with EgoMI effectively bridges the human-robot embodiment gap for robust imitation learning on semi-humanoid embodiments. Project page: https://egocentric-manipulation-interface.github.io

## 核心内容
Imitation learning from human demonstrations offers a promising approach for robot skill acquisition, but egocentric human data introduces fundamental challenges due to the embodiment gap. During manipulation, humans actively coordinate head and hand movements, continuously reposition their viewpoint and use pre-action visual fixation search strategies to locate relevant objects. These behaviors create dynamic, task-driven head motions that static robot sensing systems cannot replicate, leading to a significant distribution shift that degrades policy performance. We present EgoMI (Egocentric Manipulation Interface), a framework that captures synchronized end-effector and active head trajectories during manipulation tasks, resulting in data that can be retargeted to compatible semi-humanoid robot embodiments. To handle rapid and wide-spanning head viewpoint changes, we introduce a memory-augmented policy that selectively incorporates historical observations. We evaluate our approach on a bimanual robot equipped with an actuated camera head and find that policies with explicit head-motion modeling consistently outperform baseline methods. Results suggest that coordinated hand-eye learning with EgoMI effectively bridges the human-robot embodiment gap for robust imitation learning on semi-humanoid embodiments. Project page: https://egocentric-manipulation-interface.github.io

## 参考
- http://arxiv.org/abs/2511.00153v2

## Overview
Imitation learning from human demonstrations offers a promising approach for robot skill acquisition, but egocentric human data introduces fundamental challenges due to the embodiment gap. During manipulation, humans actively coordinate head and hand movements, continuously reposition their viewpoint and use pre-action visual fixation search strategies to locate relevant objects. These behaviors create dynamic, task-driven head motions that static robot sensing systems cannot replicate, leading to a significant distribution shift that degrades policy performance. We present EgoMI (Egocentric Manipulation Interface), a framework that captures synchronized end-effector and active head trajectories during manipulation tasks, resulting in data that can be retargeted to compatible semi-humanoid robot embodiments. To handle rapid and wide-spanning head viewpoint changes, we introduce a memory-augmented policy that selectively incorporates historical observations. We evaluate our approach on a bimanual robot equipped with an actuated camera head and find that policies with explicit head-motion modeling consistently outperform baseline methods. Results suggest that coordinated hand-eye learning with EgoMI effectively bridges the human-robot embodiment gap for robust imitation learning on semi-humanoid embodiments. Project page: https://egocentric-manipulation-interface.github.io

## Content
Imitation learning from human demonstrations offers a promising approach for robot skill acquisition, but egocentric human data introduces fundamental challenges due to the embodiment gap. During manipulation, humans actively coordinate head and hand movements, continuously reposition their viewpoint and use pre-action visual fixation search strategies to locate relevant objects. These behaviors create dynamic, task-driven head motions that static robot sensing systems cannot replicate, leading to a significant distribution shift that degrades policy performance. We present EgoMI (Egocentric Manipulation Interface), a framework that captures synchronized end-effector and active head trajectories during manipulation tasks, resulting in data that can be retargeted to compatible semi-humanoid robot embodiments. To handle rapid and wide-spanning head viewpoint changes, we introduce a memory-augmented policy that selectively incorporates historical observations. We evaluate our approach on a bimanual robot equipped with an actuated camera head and find that policies with explicit head-motion modeling consistently outperform baseline methods. Results suggest that coordinated hand-eye learning with EgoMI effectively bridges the human-robot embodiment gap for robust imitation learning on semi-humanoid embodiments. Project page: https://egocentric-manipulation-interface.github.io

## 개요
인간 시연으로부터의 모방 학습은 로봇 기술 습득에 유망한 접근 방식을 제공하지만, 자아 중심적 인간 데이터는 구현 격차(embodiment gap)로 인해 근본적인 도전 과제를 야기합니다. 조작 과정에서 인간은 머리와 손의 움직임을 능동적으로 조정하고, 시점을 지속적으로 재배치하며, 사전 동작 시각적 고정 탐색 전략을 사용하여 관련 물체를 찾습니다. 이러한 행동은 동적이고 작업 중심적인 머리 움직임을 생성하지만, 정적 로봇 감지 시스템은 이를 재현할 수 없어 정책 성능을 저하시키는 심각한 분포 변화를 초래합니다. 우리는 조작 작업 중 동기화된 엔드 이펙터와 능동적 머리 궤적을 포착하여 호환 가능한 반인간형 로봇 구현체에 재타겟팅할 수 있는 데이터를 생성하는 프레임워크인 EgoMI(Egocentric Manipulation Interface)를 제시합니다. 빠르고 광범위한 머리 시점 변화를 처리하기 위해, 우리는 역사적 관찰을 선택적으로 통합하는 메모리 증강 정책을 도입합니다. 우리는 구동식 카메라 헤드를 장착한 양팔 로봇에서 접근 방식을 평가한 결과, 명시적 머리 움직임 모델링을 사용한 정책이 기준 방법보다 일관되게 우수한 성능을 보임을 발견했습니다. 결과는 EgoMI를 통한 조정된 손-눈 학습이 반인간형 구현체에서 강건한 모방 학습을 위해 인간-로봇 구현 격차를 효과적으로 해소함을 시사합니다. 프로젝트 페이지: https://egocentric-manipulation-interface.github.io

## 핵심 내용
인간 시연으로부터의 모방 학습은 로봇 기술 습득에 유망한 접근 방식을 제공하지만, 자아 중심적 인간 데이터는 구현 격차(embodiment gap)로 인해 근본적인 도전 과제를 야기합니다. 조작 과정에서 인간은 머리와 손의 움직임을 능동적으로 조정하고, 시점을 지속적으로 재배치하며, 사전 동작 시각적 고정 탐색 전략을 사용하여 관련 물체를 찾습니다. 이러한 행동은 동적이고 작업 중심적인 머리 움직임을 생성하지만, 정적 로봇 감지 시스템은 이를 재현할 수 없어 정책 성능을 저하시키는 심각한 분포 변화를 초래합니다. 우리는 조작 작업 중 동기화된 엔드 이펙터와 능동적 머리 궤적을 포착하여 호환 가능한 반인간형 로봇 구현체에 재타겟팅할 수 있는 데이터를 생성하는 프레임워크인 EgoMI(Egocentric Manipulation Interface)를 제시합니다. 빠르고 광범위한 머리 시점 변화를 처리하기 위해, 우리는 역사적 관찰을 선택적으로 통합하는 메모리 증강 정책을 도입합니다. 우리는 구동식 카메라 헤드를 장착한 양팔 로봇에서 접근 방식을 평가한 결과, 명시적 머리 움직임 모델링을 사용한 정책이 기준 방법보다 일관되게 우수한 성능을 보임을 발견했습니다. 결과는 EgoMI를 통한 조정된 손-눈 학습이 반인간형 구현체에서 강건한 모방 학습을 위해 인간-로봇 구현 격차를 효과적으로 해소함을 시사합니다. 프로젝트 페이지: https://egocentric-manipulation-interface.github.io
