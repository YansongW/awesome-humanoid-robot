---
$id: ent_paper_huang_robot_inner_attention_modeling_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robot Inner Attention Modeling for Task-Adaptive Teaming of Heterogeneous Multi Robots
  zh: 面向任务自适应异构多机器人协作的机器人内部注意力建模
  ko: 이종 다중 로봇의 작업 적응형 팀 구성을 위한 로봇 내부 주의 모델링
summary:
  en: Proposes innerATT, an attention-based multi-agent actor-critic method that dynamically forms heterogeneous robot teams
    to satisfy changing task requirements while limiting resource cost, evaluated in the Multi-Agent Particle Environment.
  zh: 提出了innerATT，一种基于注意力机制的多智能体actor-critic方法，用于动态组建异构机器人团队以满足变化的任务需求并限制资源消耗，并在Multi-Agent Particle Environment中进行了验证。
  ko: 변화하는 작업 요구를 충족하고 자원 비용을 제한하면서 이종 로봇 팀을 동적으로 구성하기 위한 주의 메커니즘 기반 다중 에이전트 actor-critic 방법인 innerATT를 제안하고 Multi-Agent Particle
    Environment에서 검증한다.
domains:
- 07_ai_models_algorithms
- 05_mass_production
- 11_applications_markets
layers:
- intelligence
- midstream
- validation_markets
functional_roles:
- knowledge
tags:
- inner_attention
- multi_agent_reinforcement_learning
- heterogeneous_multi_robot_systems
- task_allocation
- robot_teaming
- attention_mechanism
- multi_agent_particle_environment
- fault_tolerance
- disaster_rescue
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2006.15482v2.
sources:
- id: src_001
  type: paper
  title: Robot Inner Attention Modeling for Task-Adaptive Teaming of Heterogeneous Multi Robots
  url: https://arxiv.org/abs/2006.15482
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Attracted by team scale and function diversity, a heterogeneous multi-robot system (HMRS), where multiple robots with different functions and numbers are coordinated to perform tasks, has been widely used for complex and large-scale scenarios, including disaster search and rescue, site surveillance, and social security. However, due to the variety of the task requirements, it is challenging to accurately compose a robot team with appropriate sizes and functions to dynamically satisfy task needs while limiting the robot resource cost to a low level. To solve this problem, in this paper, a novel adaptive cooperation method, inner attention (innerATT), is developed to flexibly team heterogeneous robots to execute tasks as task types and environment change. innerATT is designed by integrating a novel attention mechanism into a multi-agent actor-critic reinforcement learning architecture. With an attention mechanism, robot capability will be analyzed to flexibly form teams to meet task requirements. Scenarios with different task variety ("Single Task", "Double Task", and "Mixed Task") were designed. The effectiveness of the innerATT was validated by its accuracy in flexible cooperation.

## 核心内容
Attracted by team scale and function diversity, a heterogeneous multi-robot system (HMRS), where multiple robots with different functions and numbers are coordinated to perform tasks, has been widely used for complex and large-scale scenarios, including disaster search and rescue, site surveillance, and social security. However, due to the variety of the task requirements, it is challenging to accurately compose a robot team with appropriate sizes and functions to dynamically satisfy task needs while limiting the robot resource cost to a low level. To solve this problem, in this paper, a novel adaptive cooperation method, inner attention (innerATT), is developed to flexibly team heterogeneous robots to execute tasks as task types and environment change. innerATT is designed by integrating a novel attention mechanism into a multi-agent actor-critic reinforcement learning architecture. With an attention mechanism, robot capability will be analyzed to flexibly form teams to meet task requirements. Scenarios with different task variety ("Single Task", "Double Task", and "Mixed Task") were designed. The effectiveness of the innerATT was validated by its accuracy in flexible cooperation.

## 参考
- http://arxiv.org/abs/2006.15482v2

## Overview
Attracted by team scale and function diversity, a heterogeneous multi-robot system (HMRS), where multiple robots with different functions and numbers are coordinated to perform tasks, has been widely used for complex and large-scale scenarios, including disaster search and rescue, site surveillance, and social security. However, due to the variety of the task requirements, it is challenging to accurately compose a robot team with appropriate sizes and functions to dynamically satisfy task needs while limiting the robot resource cost to a low level. To solve this problem, in this paper, a novel adaptive cooperation method, inner attention (innerATT), is developed to flexibly team heterogeneous robots to execute tasks as task types and environment change. innerATT is designed by integrating a novel attention mechanism into a multi-agent actor-critic reinforcement learning architecture. With an attention mechanism, robot capability will be analyzed to flexibly form teams to meet task requirements. Scenarios with different task variety ("Single Task", "Double Task", and "Mixed Task") were designed. The effectiveness of the innerATT was validated by its accuracy in flexible cooperation.

## Content
Attracted by team scale and function diversity, a heterogeneous multi-robot system (HMRS), where multiple robots with different functions and numbers are coordinated to perform tasks, has been widely used for complex and large-scale scenarios, including disaster search and rescue, site surveillance, and social security. However, due to the variety of the task requirements, it is challenging to accurately compose a robot team with appropriate sizes and functions to dynamically satisfy task needs while limiting the robot resource cost to a low level. To solve this problem, in this paper, a novel adaptive cooperation method, inner attention (innerATT), is developed to flexibly team heterogeneous robots to execute tasks as task types and environment change. innerATT is designed by integrating a novel attention mechanism into a multi-agent actor-critic reinforcement learning architecture. With an attention mechanism, robot capability will be analyzed to flexibly form teams to meet task requirements. Scenarios with different task variety ("Single Task", "Double Task", and "Mixed Task") were designed. The effectiveness of the innerATT was validated by its accuracy in flexible cooperation.

## 개요
팀 규모와 기능 다양성에 매료되어, 서로 다른 기능과 수를 가진 여러 로봇이 협력하여 작업을 수행하는 이종 다중 로봇 시스템(HMRS)은 재난 수색 및 구조, 현장 감시, 사회 안전 등 복잡하고 대규모인 시나리오에서 널리 사용되고 있다. 그러나 작업 요구 사항의 다양성으로 인해, 로봇 자원 비용을 낮은 수준으로 제한하면서 동적으로 작업 요구를 충족시키기 위해 적절한 규모와 기능을 가진 로봇 팀을 정확하게 구성하는 것은 어려운 과제이다. 이 문제를 해결하기 위해, 본 논문에서는 작업 유형과 환경 변화에 따라 이종 로봇을 유연하게 팀으로 구성하여 작업을 수행할 수 있는 새로운 적응형 협력 방법인 inner attention (innerATT)을 개발하였다. innerATT는 새로운 주의 메커니즘을 다중 에이전트 행위자-비평가 강화 학습 아키텍처에 통합하여 설계되었다. 주의 메커니즘을 통해 로봇의 능력을 분석하여 작업 요구를 충족시키기 위해 유연하게 팀을 구성할 수 있다. 다양한 작업 다양성("단일 작업", "이중 작업", "혼합 작업")을 가진 시나리오가 설계되었다. innerATT의 효과성은 유연한 협력에서의 정확성을 통해 검증되었다.

## 핵심 내용
팀 규모와 기능 다양성에 매료되어, 서로 다른 기능과 수를 가진 여러 로봇이 협력하여 작업을 수행하는 이종 다중 로봇 시스템(HMRS)은 재난 수색 및 구조, 현장 감시, 사회 안전 등 복잡하고 대규모인 시나리오에서 널리 사용되고 있다. 그러나 작업 요구 사항의 다양성으로 인해, 로봇 자원 비용을 낮은 수준으로 제한하면서 동적으로 작업 요구를 충족시키기 위해 적절한 규모와 기능을 가진 로봇 팀을 정확하게 구성하는 것은 어려운 과제이다. 이 문제를 해결하기 위해, 본 논문에서는 작업 유형과 환경 변화에 따라 이종 로봇을 유연하게 팀으로 구성하여 작업을 수행할 수 있는 새로운 적응형 협력 방법인 inner attention (innerATT)을 개발하였다. innerATT는 새로운 주의 메커니즘을 다중 에이전트 행위자-비평가 강화 학습 아키텍처에 통합하여 설계되었다. 주의 메커니즘을 통해 로봇의 능력을 분석하여 작업 요구를 충족시키기 위해 유연하게 팀을 구성할 수 있다. 다양한 작업 다양성("단일 작업", "이중 작업", "혼합 작업")을 가진 시나리오가 설계되었다. innerATT의 효과성은 유연한 협력에서의 정확성을 통해 검증되었다.
