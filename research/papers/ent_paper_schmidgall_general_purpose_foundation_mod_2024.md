---
$id: ent_paper_schmidgall_general_purpose_foundation_mod_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: General-purpose foundation models for increased autonomy in robot-assisted surgery
  zh: RT-RAS
  ko: General-purpose foundation models for increased autonomy in robot-assisted surgery
summary:
  en: General-purpose foundation models for increased autonomy in robot-assisted surgery (RT-RAS), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Johns Hopkins University, University of Utah, and published at Nat. Mac.
    Intell. 2024.
  zh: General-purpose foundation models for increased autonomy in robot-assisted surgery (RT-RAS), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Johns Hopkins University, University of Utah, and published at Nat. Mac.
    Intell. 2024.
  ko: General-purpose foundation models for increased autonomy in robot-assisted surgery (RT-RAS), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Johns Hopkins University, University of Utah, and published at Nat. Mac.
    Intell. 2024.
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
- rt_ras
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2401.00678v1.
sources:
- id: src_001
  type: website
  title: RT-RAS source
  url: https://doi.org/10.1038/s42256-024-00917-4
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
The dominant paradigm for end-to-end robot learning focuses on optimizing task-specific objectives that solve a single robotic problem such as picking up an object or reaching a target position. However, recent work on high-capacity models in robotics has shown promise toward being trained on large collections of diverse and task-agnostic datasets of video demonstrations. These models have shown impressive levels of generalization to unseen circumstances, especially as the amount of data and the model complexity scale. Surgical robot systems that learn from data have struggled to advance as quickly as other fields of robot learning for a few reasons: (1) there is a lack of existing large-scale open-source data to train models, (2) it is challenging to model the soft-body deformations that these robots work with during surgery because simulation cannot match the physical and visual complexity of biological tissue, and (3) surgical robots risk harming patients when tested in clinical trials and require more extensive safety measures. This perspective article aims to provide a path toward increasing robot autonomy in robot-assisted surgery through the development of a multi-modal, multi-task, vision-language-action model for surgical robots. Ultimately, we argue that surgical robots are uniquely positioned to benefit from general-purpose models and provide three guiding actions toward increased autonomy in robot-assisted surgery.

## 核心内容
The dominant paradigm for end-to-end robot learning focuses on optimizing task-specific objectives that solve a single robotic problem such as picking up an object or reaching a target position. However, recent work on high-capacity models in robotics has shown promise toward being trained on large collections of diverse and task-agnostic datasets of video demonstrations. These models have shown impressive levels of generalization to unseen circumstances, especially as the amount of data and the model complexity scale. Surgical robot systems that learn from data have struggled to advance as quickly as other fields of robot learning for a few reasons: (1) there is a lack of existing large-scale open-source data to train models, (2) it is challenging to model the soft-body deformations that these robots work with during surgery because simulation cannot match the physical and visual complexity of biological tissue, and (3) surgical robots risk harming patients when tested in clinical trials and require more extensive safety measures. This perspective article aims to provide a path toward increasing robot autonomy in robot-assisted surgery through the development of a multi-modal, multi-task, vision-language-action model for surgical robots. Ultimately, we argue that surgical robots are uniquely positioned to benefit from general-purpose models and provide three guiding actions toward increased autonomy in robot-assisted surgery.

## 参考
- http://arxiv.org/abs/2401.00678v1

## Overview
The dominant paradigm for end-to-end robot learning focuses on optimizing task-specific objectives that solve a single robotic problem such as picking up an object or reaching a target position. However, recent work on high-capacity models in robotics has shown promise toward being trained on large collections of diverse and task-agnostic datasets of video demonstrations. These models have shown impressive levels of generalization to unseen circumstances, especially as the amount of data and the model complexity scale. Surgical robot systems that learn from data have struggled to advance as quickly as other fields of robot learning for a few reasons: (1) there is a lack of existing large-scale open-source data to train models, (2) it is challenging to model the soft-body deformations that these robots work with during surgery because simulation cannot match the physical and visual complexity of biological tissue, and (3) surgical robots risk harming patients when tested in clinical trials and require more extensive safety measures. This perspective article aims to provide a path toward increasing robot autonomy in robot-assisted surgery through the development of a multi-modal, multi-task, vision-language-action model for surgical robots. Ultimately, we argue that surgical robots are uniquely positioned to benefit from general-purpose models and provide three guiding actions toward increased autonomy in robot-assisted surgery.

## Content
The dominant paradigm for end-to-end robot learning focuses on optimizing task-specific objectives that solve a single robotic problem such as picking up an object or reaching a target position. However, recent work on high-capacity models in robotics has shown promise toward being trained on large collections of diverse and task-agnostic datasets of video demonstrations. These models have shown impressive levels of generalization to unseen circumstances, especially as the amount of data and the model complexity scale. Surgical robot systems that learn from data have struggled to advance as quickly as other fields of robot learning for a few reasons: (1) there is a lack of existing large-scale open-source data to train models, (2) it is challenging to model the soft-body deformations that these robots work with during surgery because simulation cannot match the physical and visual complexity of biological tissue, and (3) surgical robots risk harming patients when tested in clinical trials and require more extensive safety measures. This perspective article aims to provide a path toward increasing robot autonomy in robot-assisted surgery through the development of a multi-modal, multi-task, vision-language-action model for surgical robots. Ultimately, we argue that surgical robots are uniquely positioned to benefit from general-purpose models and provide three guiding actions toward increased autonomy in robot-assisted surgery.

## 개요
엔드투엔드 로봇 학습의 지배적인 패러다임은 물체 집기나 목표 위치 도달과 같은 단일 로봇 문제를 해결하는 작업별 목표를 최적화하는 데 초점을 맞추고 있습니다. 그러나 로봇 분야의 고용량 모델에 대한 최근 연구는 다양한 작업에 구애받지 않는 대규모 비디오 시연 데이터셋을 학습하는 데 가능성을 보여주고 있습니다. 이러한 모델은 특히 데이터 양과 모델 복잡성이 증가함에 따라 보지 못한 상황에 대해 인상적인 일반화 수준을 보여주었습니다. 데이터로부터 학습하는 수술 로봇 시스템은 몇 가지 이유로 다른 로봇 학습 분야만큼 빠르게 발전하지 못했습니다: (1) 모델을 학습시킬 기존의 대규모 오픈소스 데이터가 부족하고, (2) 시뮬레이션이 생물학적 조직의 물리적 및 시각적 복잡성을 따라잡을 수 없기 때문에 수술 중 이러한 로봇이 다루는 연체 변형을 모델링하기 어렵고, (3) 수술 로봇은 임상 시험에서 환자에게 해를 끼칠 위험이 있어 더 광범위한 안전 조치가 필요합니다. 이 관점 논문은 수술 로봇을 위한 다중 모달, 다중 작업, 시각-언어-행동 모델을 개발함으로써 로봇 지원 수술에서 로봇 자율성을 높이는 방향을 제시하는 것을 목표로 합니다. 궁극적으로, 우리는 수술 로봇이 범용 모델의 이점을 얻을 수 있는 독특한 위치에 있다고 주장하며, 로봇 지원 수술에서 자율성을 높이기 위한 세 가지 지침 행동을 제시합니다.

## 핵심 내용
엔드투엔드 로봇 학습의 지배적인 패러다임은 물체 집기나 목표 위치 도달과 같은 단일 로봇 문제를 해결하는 작업별 목표를 최적화하는 데 초점을 맞추고 있습니다. 그러나 로봇 분야의 고용량 모델에 대한 최근 연구는 다양한 작업에 구애받지 않는 대규모 비디오 시연 데이터셋을 학습하는 데 가능성을 보여주고 있습니다. 이러한 모델은 특히 데이터 양과 모델 복잡성이 증가함에 따라 보지 못한 상황에 대해 인상적인 일반화 수준을 보여주었습니다. 데이터로부터 학습하는 수술 로봇 시스템은 몇 가지 이유로 다른 로봇 학습 분야만큼 빠르게 발전하지 못했습니다: (1) 모델을 학습시킬 기존의 대규모 오픈소스 데이터가 부족하고, (2) 시뮬레이션이 생물학적 조직의 물리적 및 시각적 복잡성을 따라잡을 수 없기 때문에 수술 중 이러한 로봇이 다루는 연체 변형을 모델링하기 어렵고, (3) 수술 로봇은 임상 시험에서 환자에게 해를 끼칠 위험이 있어 더 광범위한 안전 조치가 필요합니다. 이 관점 논문은 수술 로봇을 위한 다중 모달, 다중 작업, 시각-언어-행동 모델을 개발함으로써 로봇 지원 수술에서 로봇 자율성을 높이는 방향을 제시하는 것을 목표로 합니다. 궁극적으로, 우리는 수술 로봇이 범용 모델의 이점을 얻을 수 있는 독특한 위치에 있다고 주장하며, 로봇 지원 수술에서 자율성을 높이기 위한 세 가지 지침 행동을 제시합니다.
