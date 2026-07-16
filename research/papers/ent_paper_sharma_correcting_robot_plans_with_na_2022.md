---
$id: ent_paper_sharma_correcting_robot_plans_with_na_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Correcting Robot Plans with Natural Language Feedback
  zh: Language costs
  ko: Correcting Robot Plans with Natural Language Feedback
summary:
  en: Correcting Robot Plans with Natural Language Feedback (Language costs), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by NVIDIA, MIT, University of Utah, University of Washington, and published
    at Robotics - Science and Systems 2022.
  zh: Correcting Robot Plans with Natural Language Feedback (Language costs), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by NVIDIA, MIT, University of Utah, University of Washington, and published
    at Robotics - Science and Systems 2022.
  ko: Correcting Robot Plans with Natural Language Feedback (Language costs), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by NVIDIA, MIT, University of Utah, University of Washington, and published
    at Robotics - Science and Systems 2022.
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
- language_costs
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2204.05186v1.
sources:
- id: src_001
  type: website
  title: Language costs source
  url: https://doi.org/10.15607/RSS.2022.XVIII.065
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
When humans design cost or goal specifications for robots, they often produce specifications that are ambiguous, underspecified, or beyond planners' ability to solve. In these cases, corrections provide a valuable tool for human-in-the-loop robot control. Corrections might take the form of new goal specifications, new constraints (e.g. to avoid specific objects), or hints for planning algorithms (e.g. to visit specific waypoints). Existing correction methods (e.g. using a joystick or direct manipulation of an end effector) require full teleoperation or real-time interaction. In this paper, we explore natural language as an expressive and flexible tool for robot correction. We describe how to map from natural language sentences to transformations of cost functions. We show that these transformations enable users to correct goals, update robot motions to accommodate additional user preferences, and recover from planning errors. These corrections can be leveraged to get 81% and 93% success rates on tasks where the original planner failed, with either one or two language corrections. Our method makes it possible to compose multiple constraints and generalizes to unseen scenes, objects, and sentences in simulated environments and real-world environments.

## 核心内容
When humans design cost or goal specifications for robots, they often produce specifications that are ambiguous, underspecified, or beyond planners' ability to solve. In these cases, corrections provide a valuable tool for human-in-the-loop robot control. Corrections might take the form of new goal specifications, new constraints (e.g. to avoid specific objects), or hints for planning algorithms (e.g. to visit specific waypoints). Existing correction methods (e.g. using a joystick or direct manipulation of an end effector) require full teleoperation or real-time interaction. In this paper, we explore natural language as an expressive and flexible tool for robot correction. We describe how to map from natural language sentences to transformations of cost functions. We show that these transformations enable users to correct goals, update robot motions to accommodate additional user preferences, and recover from planning errors. These corrections can be leveraged to get 81% and 93% success rates on tasks where the original planner failed, with either one or two language corrections. Our method makes it possible to compose multiple constraints and generalizes to unseen scenes, objects, and sentences in simulated environments and real-world environments.

## 参考
- http://arxiv.org/abs/2204.05186v1

## Overview
When humans design cost or goal specifications for robots, they often produce specifications that are ambiguous, underspecified, or beyond planners' ability to solve. In these cases, corrections provide a valuable tool for human-in-the-loop robot control. Corrections might take the form of new goal specifications, new constraints (e.g. to avoid specific objects), or hints for planning algorithms (e.g. to visit specific waypoints). Existing correction methods (e.g. using a joystick or direct manipulation of an end effector) require full teleoperation or real-time interaction. In this paper, we explore natural language as an expressive and flexible tool for robot correction. We describe how to map from natural language sentences to transformations of cost functions. We show that these transformations enable users to correct goals, update robot motions to accommodate additional user preferences, and recover from planning errors. These corrections can be leveraged to get 81% and 93% success rates on tasks where the original planner failed, with either one or two language corrections. Our method makes it possible to compose multiple constraints and generalizes to unseen scenes, objects, and sentences in simulated environments and real-world environments.

## Content
When humans design cost or goal specifications for robots, they often produce specifications that are ambiguous, underspecified, or beyond planners' ability to solve. In these cases, corrections provide a valuable tool for human-in-the-loop robot control. Corrections might take the form of new goal specifications, new constraints (e.g. to avoid specific objects), or hints for planning algorithms (e.g. to visit specific waypoints). Existing correction methods (e.g. using a joystick or direct manipulation of an end effector) require full teleoperation or real-time interaction. In this paper, we explore natural language as an expressive and flexible tool for robot correction. We describe how to map from natural language sentences to transformations of cost functions. We show that these transformations enable users to correct goals, update robot motions to accommodate additional user preferences, and recover from planning errors. These corrections can be leveraged to get 81% and 93% success rates on tasks where the original planner failed, with either one or two language corrections. Our method makes it possible to compose multiple constraints and generalizes to unseen scenes, objects, and sentences in simulated environments and real-world environments.

## 개요
인간이 로봇을 위한 비용 또는 목표 명세를 설계할 때, 종종 모호하거나 불완전하게 명시되거나 계획자가 해결할 수 없는 범위를 벗어난 명세를 생성합니다. 이러한 경우, 수정(corrections)은 인간이 개입하는 로봇 제어(Human-in-the-loop robot control)를 위한 귀중한 도구를 제공합니다. 수정은 새로운 목표 명세, 새로운 제약 조건(예: 특정 물체 회피), 또는 계획 알고리즘을 위한 힌트(예: 특정 경유지 방문)의 형태를 취할 수 있습니다. 기존의 수정 방법(예: 조이스틱 사용 또는 엔드 이펙터 직접 조작)은 완전한 원격 조작 또는 실시간 상호작용을 필요로 합니다. 본 논문에서는 자연어를 로봇 수정을 위한 표현력 있고 유연한 도구로 탐구합니다. 자연어 문장을 비용 함수의 변환으로 매핑하는 방법을 설명하고, 이러한 변환을 통해 사용자가 목표를 수정하고, 추가 사용자 선호도를 수용하도록 로봇 동작을 업데이트하며, 계획 오류로부터 복구할 수 있음을 보여줍니다. 이러한 수정을 활용하여 원래 계획자가 실패한 작업에서 한 번 또는 두 번의 언어 수정으로 81%와 93%의 성공률을 달성했습니다. 우리의 방법은 여러 제약 조건을 구성할 수 있게 하며, 시뮬레이션 환경과 실제 환경에서 보지 못한 장면, 물체, 문장에 일반화됩니다.

## 핵심 내용
인간이 로봇을 위한 비용 또는 목표 명세를 설계할 때, 종종 모호하거나 불완전하게 명시되거나 계획자가 해결할 수 없는 범위를 벗어난 명세를 생성합니다. 이러한 경우, 수정(corrections)은 인간이 개입하는 로봇 제어를 위한 귀중한 도구를 제공합니다. 수정은 새로운 목표 명세, 새로운 제약 조건(예: 특정 물체 회피), 또는 계획 알고리즘을 위한 힌트(예: 특정 경유지 방문)의 형태를 취할 수 있습니다. 기존의 수정 방법(예: 조이스틱 사용 또는 엔드 이펙터 직접 조작)은 완전한 원격 조작 또는 실시간 상호작용을 필요로 합니다. 본 논문에서는 자연어를 로봇 수정을 위한 표현력 있고 유연한 도구로 탐구합니다. 자연어 문장을 비용 함수의 변환으로 매핑하는 방법을 설명하고, 이러한 변환을 통해 사용자가 목표를 수정하고, 추가 사용자 선호도를 수용하도록 로봇 동작을 업데이트하며, 계획 오류로부터 복구할 수 있음을 보여줍니다. 이러한 수정을 활용하여 원래 계획자가 실패한 작업에서 한 번 또는 두 번의 언어 수정으로 81%와 93%의 성공률을 달성했습니다. 우리의 방법은 여러 제약 조건을 구성할 수 있게 하며, 시뮬레이션 환경과 실제 환경에서 보지 못한 장면, 물체, 문장에 일반화됩니다.
