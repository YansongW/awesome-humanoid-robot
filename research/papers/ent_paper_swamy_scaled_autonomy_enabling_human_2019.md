---
$id: ent_paper_swamy_scaled_autonomy_enabling_human_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Scaled Autonomy: Enabling Human Operators to Control Robot Fleets'
  zh: 可扩展自主：使人类操作员能够控制机器人群
  ko: '확장된 자율성: 인간 운영자가 로봇 함대를 제어할 수 있도록'
summary:
  en: This paper formalizes operator attention allocation as learning an internal scoring function under the Luce choice model,
    and uses the learned model to automatically select which robot in a large fleet most needs teleoperated intervention.
  zh: 'Autonomous robots often encounter challenging situations where their control policies fail and an expert human operator
    must briefly intervene, e.g., through teleoperation. In settings where multiple robots act in separate environments, a
    single human operator can manage a fleet of robots by identifying and teleoperating one robot at any given time. The key
    challenge is that users have limited attention: as the number of robots increases, users lose the ability to decide which
    robot requires teleoperation the most. Our goal is to automate this decision, thereby enabling users to supervise more'
  ko: 본 논문은 운영자의 주의력 배분을 Luce 선택 모델 하에서 내부 점수 함수를 학습하는 문제로 형식화하고, 학습된 모델을 사용하여 대규모 로봇 함대에서 가장 원격 조작 개입이 필요한 로봇을 자동으로 선택한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
- 05_mass_production
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- fleet_supervision
- human_robot_interaction
- teleoperation
- preference_learning
- attention_allocation
- luce_choice_model
- shared_autonomy
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1910.02910v2.
sources:
- id: src_001
  type: paper
  title: 'Scaled Autonomy: Enabling Human Operators to Control Robot Fleets'
  url: https://arxiv.org/abs/1910.02910
  date: '2019'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## 概述
Autonomous robots often encounter challenging situations where their control policies fail and an expert human operator must briefly intervene, e.g., through teleoperation. In settings where multiple robots act in separate environments, a single human operator can manage a fleet of robots by identifying and teleoperating one robot at any given time. The key challenge is that users have limited attention: as the number of robots increases, users lose the ability to decide which robot requires teleoperation the most. Our goal is to automate this decision, thereby enabling users to supervise more robots than their attention would normally allow for. Our insight is that we can model the user's choice of which robot to control as an approximately optimal decision that maximizes the user's utility function. We learn a model of the user's preferences from observations of the user's choices in easy settings with a few robots, and use it in challenging settings with more robots to automatically identify which robot the user would most likely choose to control, if they were able to evaluate the states of all robots at all times. We run simulation experiments and a user study with twelve participants that show our method can be used to assist users in performing a simulated navigation task. We also run a hardware demonstration that illustrates how our method can be applied to a real-world mobile robot navigation task.

## 核心内容
Autonomous robots often encounter challenging situations where their control policies fail and an expert human operator must briefly intervene, e.g., through teleoperation. In settings where multiple robots act in separate environments, a single human operator can manage a fleet of robots by identifying and teleoperating one robot at any given time. The key challenge is that users have limited attention: as the number of robots increases, users lose the ability to decide which robot requires teleoperation the most. Our goal is to automate this decision, thereby enabling users to supervise more robots than their attention would normally allow for. Our insight is that we can model the user's choice of which robot to control as an approximately optimal decision that maximizes the user's utility function. We learn a model of the user's preferences from observations of the user's choices in easy settings with a few robots, and use it in challenging settings with more robots to automatically identify which robot the user would most likely choose to control, if they were able to evaluate the states of all robots at all times. We run simulation experiments and a user study with twelve participants that show our method can be used to assist users in performing a simulated navigation task. We also run a hardware demonstration that illustrates how our method can be applied to a real-world mobile robot navigation task.

## 参考
- http://arxiv.org/abs/1910.02910v2

## Overview
Autonomous robots often encounter challenging situations where their control policies fail and an expert human operator must briefly intervene, e.g., through teleoperation. In settings where multiple robots act in separate environments, a single human operator can manage a fleet of robots by identifying and teleoperating one robot at any given time. The key challenge is that users have limited attention: as the number of robots increases, users lose the ability to decide which robot requires teleoperation the most. Our goal is to automate this decision, thereby enabling users to supervise more robots than their attention would normally allow for. Our insight is that we can model the user's choice of which robot to control as an approximately optimal decision that maximizes the user's utility function. We learn a model of the user's preferences from observations of the user's choices in easy settings with a few robots, and use it in challenging settings with more robots to automatically identify which robot the user would most likely choose to control, if they were able to evaluate the states of all robots at all times. We run simulation experiments and a user study with twelve participants that show our method can be used to assist users in performing a simulated navigation task. We also run a hardware demonstration that illustrates how our method can be applied to a real-world mobile robot navigation task.

## Content
Autonomous robots often encounter challenging situations where their control policies fail and an expert human operator must briefly intervene, e.g., through teleoperation. In settings where multiple robots act in separate environments, a single human operator can manage a fleet of robots by identifying and teleoperating one robot at any given time. The key challenge is that users have limited attention: as the number of robots increases, users lose the ability to decide which robot requires teleoperation the most. Our goal is to automate this decision, thereby enabling users to supervise more robots than their attention would normally allow for. Our insight is that we can model the user's choice of which robot to control as an approximately optimal decision that maximizes the user's utility function. We learn a model of the user's preferences from observations of the user's choices in easy settings with a few robots, and use it in challenging settings with more robots to automatically identify which robot the user would most likely choose to control, if they were able to evaluate the states of all robots at all times. We run simulation experiments and a user study with twelve participants that show our method can be used to assist users in performing a simulated navigation task. We also run a hardware demonstration that illustrates how our method can be applied to a real-world mobile robot navigation task.

## 개요
자율 로봇은 종종 제어 정책이 실패하는 어려운 상황에 직면하며, 이때 전문 인간 운영자가 원격 조작 등을 통해 잠시 개입해야 합니다. 여러 로봇이 각기 다른 환경에서 작동하는 상황에서, 단일 인간 운영자는 특정 시점에 하나의 로봇을 식별하고 원격 조작함으로써 로봇 군집을 관리할 수 있습니다. 주요 과제는 사용자의 주의력이 제한적이라는 점입니다. 로봇의 수가 증가함에 따라 사용자는 어떤 로봇이 가장 원격 조작을 필요로 하는지 결정하는 능력을 상실합니다. 우리의 목표는 이 결정을 자동화하여, 사용자가 평소 주의력으로 허용되는 것보다 더 많은 로봇을 감독할 수 있도록 하는 것입니다. 우리의 통찰은 사용자가 어떤 로봇을 제어할지 선택하는 것을 사용자의 효용 함수를 최대화하는 대략 최적의 결정으로 모델링할 수 있다는 점입니다. 우리는 소수의 로봇이 있는 쉬운 환경에서 사용자의 선택 관찰을 통해 사용자 선호도 모델을 학습하고, 더 많은 로봇이 있는 어려운 환경에서 이를 사용하여 사용자가 모든 로봇의 상태를 항상 평가할 수 있다면 가장 제어하고 싶어할 로봇을 자동으로 식별합니다. 우리는 시뮬레이션 실험과 12명의 참가자를 대상으로 한 사용자 연구를 수행하여, 우리 방법이 시뮬레이션된 내비게이션 작업을 수행하는 사용자를 지원하는 데 사용될 수 있음을 보여줍니다. 또한, 우리 방법이 실제 모바일 로봇 내비게이션 작업에 어떻게 적용될 수 있는지 보여주는 하드웨어 데모도 실행합니다.

## 핵심 내용
자율 로봇은 종종 제어 정책이 실패하는 어려운 상황에 직면하며, 이때 전문 인간 운영자가 원격 조작 등을 통해 잠시 개입해야 합니다. 여러 로봇이 각기 다른 환경에서 작동하는 상황에서, 단일 인간 운영자는 특정 시점에 하나의 로봇을 식별하고 원격 조작함으로써 로봇 군집을 관리할 수 있습니다. 주요 과제는 사용자의 주의력이 제한적이라는 점입니다. 로봇의 수가 증가함에 따라 사용자는 어떤 로봇이 가장 원격 조작을 필요로 하는지 결정하는 능력을 상실합니다. 우리의 목표는 이 결정을 자동화하여, 사용자가 평소 주의력으로 허용되는 것보다 더 많은 로봇을 감독할 수 있도록 하는 것입니다. 우리의 통찰은 사용자가 어떤 로봇을 제어할지 선택하는 것을 사용자의 효용 함수를 최대화하는 대략 최적의 결정으로 모델링할 수 있다는 점입니다. 우리는 소수의 로봇이 있는 쉬운 환경에서 사용자의 선택 관찰을 통해 사용자 선호도 모델을 학습하고, 더 많은 로봇이 있는 어려운 환경에서 이를 사용하여 사용자가 모든 로봇의 상태를 항상 평가할 수 있다면 가장 제어하고 싶어할 로봇을 자동으로 식별합니다. 우리는 시뮬레이션 실험과 12명의 참가자를 대상으로 한 사용자 연구를 수행하여, 우리 방법이 시뮬레이션된 내비게이션 작업을 수행하는 사용자를 지원하는 데 사용될 수 있음을 보여줍니다. 또한, 우리 방법이 실제 모바일 로봇 내비게이션 작업에 어떻게 적용될 수 있는지 보여주는 하드웨어 데모도 실행합니다.
