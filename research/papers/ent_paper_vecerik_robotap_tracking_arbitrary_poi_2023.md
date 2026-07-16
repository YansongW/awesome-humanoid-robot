---
$id: ent_paper_vecerik_robotap_tracking_arbitrary_poi_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboTAP: Tracking Arbitrary Points for Few-Shot Visual Imitation'
  zh: RoboTAP
  ko: 'RoboTAP: Tracking Arbitrary Points for Few-Shot Visual Imitation'
summary:
  en: 'RoboTAP: Tracking Arbitrary Points for Few-Shot Visual Imitation (RoboTAP), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, Department of Computer Science at University College London,
    and published at ICRA 2023.'
  zh: 'RoboTAP: Tracking Arbitrary Points for Few-Shot Visual Imitation (RoboTAP), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, Department of Computer Science at University College London,
    and published at ICRA 2023.'
  ko: 'RoboTAP: Tracking Arbitrary Points for Few-Shot Visual Imitation (RoboTAP), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, Department of Computer Science at University College London,
    and published at ICRA 2023.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- robotap
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2308.15975v2.
sources:
- id: src_001
  type: website
  title: RoboTAP source
  url: https://doi.org/10.1109/ICRA57147.2024.10611409
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
For robots to be useful outside labs and specialized factories we need a way to teach them new useful behaviors quickly. Current approaches lack either the generality to onboard new tasks without task-specific engineering, or else lack the data-efficiency to do so in an amount of time that enables practical use. In this work we explore dense tracking as a representational vehicle to allow faster and more general learning from demonstration. Our approach utilizes Track-Any-Point (TAP) models to isolate the relevant motion in a demonstration, and parameterize a low-level controller to reproduce this motion across changes in the scene configuration. We show this results in robust robot policies that can solve complex object-arrangement tasks such as shape-matching, stacking, and even full path-following tasks such as applying glue and sticking objects together, all from demonstrations that can be collected in minutes.

## 核心内容
For robots to be useful outside labs and specialized factories we need a way to teach them new useful behaviors quickly. Current approaches lack either the generality to onboard new tasks without task-specific engineering, or else lack the data-efficiency to do so in an amount of time that enables practical use. In this work we explore dense tracking as a representational vehicle to allow faster and more general learning from demonstration. Our approach utilizes Track-Any-Point (TAP) models to isolate the relevant motion in a demonstration, and parameterize a low-level controller to reproduce this motion across changes in the scene configuration. We show this results in robust robot policies that can solve complex object-arrangement tasks such as shape-matching, stacking, and even full path-following tasks such as applying glue and sticking objects together, all from demonstrations that can be collected in minutes.

## 参考
- http://arxiv.org/abs/2308.15975v2

## Overview
For robots to be useful outside labs and specialized factories we need a way to teach them new useful behaviors quickly. Current approaches lack either the generality to onboard new tasks without task-specific engineering, or else lack the data-efficiency to do so in an amount of time that enables practical use. In this work we explore dense tracking as a representational vehicle to allow faster and more general learning from demonstration. Our approach utilizes Track-Any-Point (TAP) models to isolate the relevant motion in a demonstration, and parameterize a low-level controller to reproduce this motion across changes in the scene configuration. We show this results in robust robot policies that can solve complex object-arrangement tasks such as shape-matching, stacking, and even full path-following tasks such as applying glue and sticking objects together, all from demonstrations that can be collected in minutes.

## Content
For robots to be useful outside labs and specialized factories we need a way to teach them new useful behaviors quickly. Current approaches lack either the generality to onboard new tasks without task-specific engineering, or else lack the data-efficiency to do so in an amount of time that enables practical use. In this work we explore dense tracking as a representational vehicle to allow faster and more general learning from demonstration. Our approach utilizes Track-Any-Point (TAP) models to isolate the relevant motion in a demonstration, and parameterize a low-level controller to reproduce this motion across changes in the scene configuration. We show this results in robust robot policies that can solve complex object-arrangement tasks such as shape-matching, stacking, and even full path-following tasks such as applying glue and sticking objects together, all from demonstrations that can be collected in minutes.

## 개요
로봇이 실험실과 특수 공장 외부에서 유용하게 사용되기 위해서는 새로운 유용한 행동을 빠르게 가르칠 수 있는 방법이 필요합니다. 현재의 접근 방식은 특정 작업에 맞춘 엔지니어링 없이 새로운 작업을 도입할 수 있는 일반성이 부족하거나, 실용적인 사용이 가능한 시간 내에 이를 수행할 수 있는 데이터 효율성이 부족합니다. 본 연구에서는 밀집 추적(dense tracking)을 표현 수단으로 활용하여 시연으로부터 더 빠르고 일반적인 학습을 가능하게 하는 방법을 탐구합니다. 우리의 접근 방식은 Track-Any-Point (TAP) 모델을 사용하여 시연에서 관련 동작을 분리하고, 장면 구성의 변화에 걸쳐 이 동작을 재현할 수 있는 저수준 제어기를 매개변수화합니다. 이를 통해 모양 맞추기, 쌓기, 심지어 접착제 바르기 및 물체 붙이기와 같은 전체 경로 추적 작업까지 포함하는 복잡한 물체 배치 작업을 해결할 수 있는 강력한 로봇 정책을 얻을 수 있으며, 이러한 모든 작업은 몇 분 안에 수집할 수 있는 시연을 기반으로 합니다.

## 핵심 내용
로봇이 실험실과 특수 공장 외부에서 유용하게 사용되기 위해서는 새로운 유용한 행동을 빠르게 가르칠 수 있는 방법이 필요합니다. 현재의 접근 방식은 특정 작업에 맞춘 엔지니어링 없이 새로운 작업을 도입할 수 있는 일반성이 부족하거나, 실용적인 사용이 가능한 시간 내에 이를 수행할 수 있는 데이터 효율성이 부족합니다. 본 연구에서는 밀집 추적(dense tracking)을 표현 수단으로 활용하여 시연으로부터 더 빠르고 일반적인 학습을 가능하게 하는 방법을 탐구합니다. 우리의 접근 방식은 Track-Any-Point (TAP) 모델을 사용하여 시연에서 관련 동작을 분리하고, 장면 구성의 변화에 걸쳐 이 동작을 재현할 수 있는 저수준 제어기를 매개변수화합니다. 이를 통해 모양 맞추기, 쌓기, 심지어 접착제 바르기 및 물체 붙이기와 같은 전체 경로 추적 작업까지 포함하는 복잡한 물체 배치 작업을 해결할 수 있는 강력한 로봇 정책을 얻을 수 있으며, 이러한 모든 작업은 몇 분 안에 수집할 수 있는 시연을 기반으로 합니다.
