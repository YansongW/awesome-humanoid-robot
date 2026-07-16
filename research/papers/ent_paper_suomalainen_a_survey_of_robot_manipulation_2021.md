---
$id: ent_paper_suomalainen_a_survey_of_robot_manipulation_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Survey of Robot Manipulation in Contact
  zh: 接触式机器人操作综述
  ko: 접촉 상태에서의 로봇 조작에 대한 서베이
summary:
  en: This survey reviews robot manipulation tasks that require sustained or controlled contact with the environment, categorizing
    in-contact tasks, low-level control strategies, skill representations, and planning or learning approaches, and identifies
    open challenges in deformable objects, exception handling, and sim-to-real transfer.
  zh: 本综述回顾了需要与环境保持持续或受控接触的机器人操作任务，对接触式任务、底层控制策略、技能表示以及规划或学习方法进行了分类，并指出了可变形物体、异常处理和仿真到现实迁移中的开放挑战。
  ko: 본 서베이는 환경과의 지속적이거나 제어된 접촉을 필요로 하는 로봇 조작 작업을 검토하고, 접촉 작업, 저수준 제어 전략, 스킬 표현, 계획 및 학습 방법을 분류하며, 변형 가능한 물체, 예외 처리, 시뮬레이션에서
    실제로의 전이에서의 미해결 과제를 제시한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- contact_rich_manipulation
- force_control
- impedance_control
- admittance_control
- manipulation_survey
- peg_in_hole
- assembly
- reinforcement_learning
- imitation_learning
- sim_to_real
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2112.01942v3.
sources:
- id: src_001
  type: paper
  title: A Survey of Robot Manipulation in Contact
  url: https://arxiv.org/abs/2112.01942
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
In this survey, we present the current status on robots performing manipulation tasks that require varying contact with the environment, such that the robot must either implicitly or explicitly control the contact force with the environment to complete the task. Robots can perform more and more manipulation tasks that are still done by humans, and there is a growing number of publications on the topics of 1) performing tasks that always require contact and 2) mitigating uncertainty by leveraging the environment in tasks that, under perfect information, could be performed without contact. The recent trends have seen robots perform tasks earlier left for humans, such as massage, and in the classical tasks, such as peg-in-hole, there is a more efficient generalization to other similar tasks, better error tolerance, and faster planning or learning of the tasks. Thus, in this survey we cover the current stage of robots performing such tasks, starting from surveying all the different in-contact tasks robots can perform, observing how these tasks are controlled and represented, and finally presenting the learning and planning of the skills required to complete these tasks.

## 核心内容
In this survey, we present the current status on robots performing manipulation tasks that require varying contact with the environment, such that the robot must either implicitly or explicitly control the contact force with the environment to complete the task. Robots can perform more and more manipulation tasks that are still done by humans, and there is a growing number of publications on the topics of 1) performing tasks that always require contact and 2) mitigating uncertainty by leveraging the environment in tasks that, under perfect information, could be performed without contact. The recent trends have seen robots perform tasks earlier left for humans, such as massage, and in the classical tasks, such as peg-in-hole, there is a more efficient generalization to other similar tasks, better error tolerance, and faster planning or learning of the tasks. Thus, in this survey we cover the current stage of robots performing such tasks, starting from surveying all the different in-contact tasks robots can perform, observing how these tasks are controlled and represented, and finally presenting the learning and planning of the skills required to complete these tasks.

## 参考
- http://arxiv.org/abs/2112.01942v3

## Overview
In this survey, we present the current status on robots performing manipulation tasks that require varying contact with the environment, such that the robot must either implicitly or explicitly control the contact force with the environment to complete the task. Robots can perform more and more manipulation tasks that are still done by humans, and there is a growing number of publications on the topics of 1) performing tasks that always require contact and 2) mitigating uncertainty by leveraging the environment in tasks that, under perfect information, could be performed without contact. The recent trends have seen robots perform tasks earlier left for humans, such as massage, and in the classical tasks, such as peg-in-hole, there is a more efficient generalization to other similar tasks, better error tolerance, and faster planning or learning of the tasks. Thus, in this survey we cover the current stage of robots performing such tasks, starting from surveying all the different in-contact tasks robots can perform, observing how these tasks are controlled and represented, and finally presenting the learning and planning of the skills required to complete these tasks.

## Content
In this survey, we present the current status on robots performing manipulation tasks that require varying contact with the environment, such that the robot must either implicitly or explicitly control the contact force with the environment to complete the task. Robots can perform more and more manipulation tasks that are still done by humans, and there is a growing number of publications on the topics of 1) performing tasks that always require contact and 2) mitigating uncertainty by leveraging the environment in tasks that, under perfect information, could be performed without contact. The recent trends have seen robots perform tasks earlier left for humans, such as massage, and in the classical tasks, such as peg-in-hole, there is a more efficient generalization to other similar tasks, better error tolerance, and faster planning or learning of the tasks. Thus, in this survey we cover the current stage of robots performing such tasks, starting from surveying all the different in-contact tasks robots can perform, observing how these tasks are controlled and represented, and finally presenting the learning and planning of the skills required to complete these tasks.

## 개요
본 조사에서는 로봇이 환경과의 다양한 접촉을 요구하는 조작 작업을 수행하는 현재 상황을 제시합니다. 이러한 작업에서 로봇은 작업을 완료하기 위해 환경과의 접촉력을 암시적 또는 명시적으로 제어해야 합니다. 로봇은 여전히 인간이 수행하는 점점 더 많은 조작 작업을 수행할 수 있으며, 1) 항상 접촉이 필요한 작업 수행과 2) 완벽한 정보 하에서는 접촉 없이 수행될 수 있는 작업에서 환경을 활용하여 불확실성을 완화하는 주제에 대한 출판물이 증가하고 있습니다. 최근 추세에 따르면 로봇은 마사지와 같이 이전에는 인간에게 맡겨졌던 작업을 수행하고 있으며, 핀-인-홀(peg-in-hole)과 같은 고전적인 작업에서는 다른 유사한 작업으로의 더 효율적인 일반화, 더 나은 오류 허용성, 그리고 더 빠른 작업 계획 또는 학습이 이루어지고 있습니다. 따라서 본 조사에서는 로봇이 수행할 수 있는 다양한 접촉 작업을 조사하고, 이러한 작업이 어떻게 제어되고 표현되는지 관찰하며, 마지막으로 이러한 작업을 완료하는 데 필요한 기술의 학습 및 계획을 제시함으로써 로봇이 이러한 작업을 수행하는 현재 단계를 다룹니다.

## 핵심 내용
본 조사에서는 로봇이 환경과의 다양한 접촉을 요구하는 조작 작업을 수행하는 현재 상황을 제시합니다. 이러한 작업에서 로봇은 작업을 완료하기 위해 환경과의 접촉력을 암시적 또는 명시적으로 제어해야 합니다. 로봇은 여전히 인간이 수행하는 점점 더 많은 조작 작업을 수행할 수 있으며, 1) 항상 접촉이 필요한 작업 수행과 2) 완벽한 정보 하에서는 접촉 없이 수행될 수 있는 작업에서 환경을 활용하여 불확실성을 완화하는 주제에 대한 출판물이 증가하고 있습니다. 최근 추세에 따르면 로봇은 마사지와 같이 이전에는 인간에게 맡겨졌던 작업을 수행하고 있으며, 핀-인-홀(peg-in-hole)과 같은 고전적인 작업에서는 다른 유사한 작업으로의 더 효율적인 일반화, 더 나은 오류 허용성, 그리고 더 빠른 작업 계획 또는 학습이 이루어지고 있습니다. 따라서 본 조사에서는 로봇이 수행할 수 있는 다양한 접촉 작업을 조사하고, 이러한 작업이 어떻게 제어되고 표현되는지 관찰하며, 마지막으로 이러한 작업을 완료하는 데 필요한 기술의 학습 및 계획을 제시함으로써 로봇이 이러한 작업을 수행하는 현재 단계를 다룹니다.
