---
$id: ent_paper_lamon_a_unified_architecture_for_dyn_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Unified Architecture for Dynamic Role Allocation and Collaborative Task Planning in Mixed Human-Robot Teams
  zh: 混合人机团队中动态角色分配与协作任务规划的统一架构
  ko: 혼합 인간-로봇 팀에서의 동적 역할 할당 및 협업 작업 계획을 위한 통합 아키텍처
summary:
  en: This paper proposes a unified architecture that combines a centralized Behavior Tree planner for action scheduling with
    a Mixed-Integer Linear Program for dynamic role allocation in mixed human-robot teams, supported by an Augmented Reality
    interface for human-system negotiation.
  zh: The growing deployment of human-robot collaborative processes in several industrial applications, such as handling,
    welding, and assembly, unfolds the pursuit of systems which are able to manage large heterogeneous teams and, at the same
    time, monitor the execution of complex tasks. In this paper, we present a novel architecture for dynamic role allocation
    and collaborative task planning in a mixed human-robot team of arbitrary size. The architecture capitalizes on a centralized
    reactive and modular task-agnostic planning method based on Behavior Trees (BTs), in charge of actions scheduling, w
  ko: 본 논문은 동작 스케줄링을 위한 중앙 집중형 비헤이비어 트리 플래너와 혼합 인간-로봇 팀에서의 동적 역할 할당을 위한 혼합정수선형계획법을 결합하고, 증강 현실 인터페이스를 통해 인간-시스템 간 협상을 지원하는
    통합 아키텍처를 제안한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 03_manufacturing_processes
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- intelligence
- knowledge
- system
tags:
- behavior_tree
- mixed_integer_linear_programming
- human_robot_collaboration
- dynamic_role_allocation
- augmented_reality
- task_planning
- collaborative_manufacturing
- industrial_robotics
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2301.08038v2.
sources:
- id: src_001
  type: paper
  title: A Unified Architecture for Dynamic Role Allocation and Collaborative Task Planning in Mixed Human-Robot Teams
  url: https://arxiv.org/abs/2301.08038
  date: '2023'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
- system
---

## 概述
The growing deployment of human-robot collaborative processes in several industrial applications, such as handling, welding, and assembly, unfolds the pursuit of systems which are able to manage large heterogeneous teams and, at the same time, monitor the execution of complex tasks. In this paper, we present a novel architecture for dynamic role allocation and collaborative task planning in a mixed human-robot team of arbitrary size. The architecture capitalizes on a centralized reactive and modular task-agnostic planning method based on Behavior Trees (BTs), in charge of actions scheduling, while the allocation problem is formulated through a Mixed-Integer Linear Program (MILP), that assigns dynamically individual roles or collaborations to the agents of the team. Different metrics used as MILP cost allow the architecture to favor various aspects of the collaboration (e.g. makespan, ergonomics, human preferences). Human preference are identified through a negotiation phase, in which, an human agent can accept/refuse to execute the assigned task.In addition, bilateral communication between humans and the system is achieved through an Augmented Reality (AR) custom user interface that provides intuitive functionalities to assist and coordinate workers in different action phases. The computational complexity of the proposed methodology outperforms literature approaches in industrial sized jobs and teams (problems up to 50 actions and 20 agents in the team with collaborations are solved within 1 s). The different allocated roles, as the cost functions change, highlights the flexibility of the architecture to several production requirements. Finally, the subjective evaluation demonstrating the high usability level and the suitability for the targeted scenario.

## 核心内容
The growing deployment of human-robot collaborative processes in several industrial applications, such as handling, welding, and assembly, unfolds the pursuit of systems which are able to manage large heterogeneous teams and, at the same time, monitor the execution of complex tasks. In this paper, we present a novel architecture for dynamic role allocation and collaborative task planning in a mixed human-robot team of arbitrary size. The architecture capitalizes on a centralized reactive and modular task-agnostic planning method based on Behavior Trees (BTs), in charge of actions scheduling, while the allocation problem is formulated through a Mixed-Integer Linear Program (MILP), that assigns dynamically individual roles or collaborations to the agents of the team. Different metrics used as MILP cost allow the architecture to favor various aspects of the collaboration (e.g. makespan, ergonomics, human preferences). Human preference are identified through a negotiation phase, in which, an human agent can accept/refuse to execute the assigned task.In addition, bilateral communication between humans and the system is achieved through an Augmented Reality (AR) custom user interface that provides intuitive functionalities to assist and coordinate workers in different action phases. The computational complexity of the proposed methodology outperforms literature approaches in industrial sized jobs and teams (problems up to 50 actions and 20 agents in the team with collaborations are solved within 1 s). The different allocated roles, as the cost functions change, highlights the flexibility of the architecture to several production requirements. Finally, the subjective evaluation demonstrating the high usability level and the suitability for the targeted scenario.

## 参考
- http://arxiv.org/abs/2301.08038v2

## Overview
The growing deployment of human-robot collaborative processes in several industrial applications, such as handling, welding, and assembly, unfolds the pursuit of systems which are able to manage large heterogeneous teams and, at the same time, monitor the execution of complex tasks. In this paper, we present a novel architecture for dynamic role allocation and collaborative task planning in a mixed human-robot team of arbitrary size. The architecture capitalizes on a centralized reactive and modular task-agnostic planning method based on Behavior Trees (BTs), in charge of actions scheduling, while the allocation problem is formulated through a Mixed-Integer Linear Program (MILP), that assigns dynamically individual roles or collaborations to the agents of the team. Different metrics used as MILP cost allow the architecture to favor various aspects of the collaboration (e.g. makespan, ergonomics, human preferences). Human preference are identified through a negotiation phase, in which, an human agent can accept/refuse to execute the assigned task.In addition, bilateral communication between humans and the system is achieved through an Augmented Reality (AR) custom user interface that provides intuitive functionalities to assist and coordinate workers in different action phases. The computational complexity of the proposed methodology outperforms literature approaches in industrial sized jobs and teams (problems up to 50 actions and 20 agents in the team with collaborations are solved within 1 s). The different allocated roles, as the cost functions change, highlights the flexibility of the architecture to several production requirements. Finally, the subjective evaluation demonstrating the high usability level and the suitability for the targeted scenario.

## Content
The growing deployment of human-robot collaborative processes in several industrial applications, such as handling, welding, and assembly, unfolds the pursuit of systems which are able to manage large heterogeneous teams and, at the same time, monitor the execution of complex tasks. In this paper, we present a novel architecture for dynamic role allocation and collaborative task planning in a mixed human-robot team of arbitrary size. The architecture capitalizes on a centralized reactive and modular task-agnostic planning method based on Behavior Trees (BTs), in charge of actions scheduling, while the allocation problem is formulated through a Mixed-Integer Linear Program (MILP), that assigns dynamically individual roles or collaborations to the agents of the team. Different metrics used as MILP cost allow the architecture to favor various aspects of the collaboration (e.g. makespan, ergonomics, human preferences). Human preference are identified through a negotiation phase, in which, an human agent can accept/refuse to execute the assigned task.In addition, bilateral communication between humans and the system is achieved through an Augmented Reality (AR) custom user interface that provides intuitive functionalities to assist and coordinate workers in different action phases. The computational complexity of the proposed methodology outperforms literature approaches in industrial sized jobs and teams (problems up to 50 actions and 20 agents in the team with collaborations are solved within 1 s). The different allocated roles, as the cost functions change, highlights the flexibility of the architecture to several production requirements. Finally, the subjective evaluation demonstrating the high usability level and the suitability for the targeted scenario.

## 개요
핸들링, 용접, 조립 등 여러 산업 응용 분야에서 인간-로봇 협업 프로세스의 배치가 증가함에 따라, 대규모 이종 팀을 관리하면서 동시에 복잡한 작업의 실행을 모니터링할 수 있는 시스템에 대한 추구가 확대되고 있습니다. 본 논문에서는 임의 크기의 인간-로봇 혼합 팀에서 동적 역할 할당 및 협업 작업 계획을 위한 새로운 아키텍처를 제시합니다. 이 아키텍처는 행동 스케줄링을 담당하는 Behavior Trees(BTs) 기반의 중앙 집중식 반응형 및 모듈식 작업 무관 계획 방법을 활용하며, 할당 문제는 Mixed-Integer Linear Program(MILP)을 통해 공식화되어 팀 에이전트에게 개별 역할 또는 협업을 동적으로 할당합니다. MILP 비용으로 사용되는 다양한 지표를 통해 아키텍처는 협업의 여러 측면(예: makespan, 인간공학, 인간 선호도)을 우선시할 수 있습니다. 인간 선호도는 협상 단계를 통해 식별되며, 이 단계에서 인간 에이전트는 할당된 작업의 실행을 수락하거나 거부할 수 있습니다. 또한, 인간과 시스템 간의 양방향 통신은 다양한 행동 단계에서 작업자를 지원하고 조정하는 직관적인 기능을 제공하는 맞춤형 Augmented Reality(AR) 사용자 인터페이스를 통해 구현됩니다. 제안된 방법론의 계산 복잡성은 산업 규모의 작업 및 팀(협업이 포함된 최대 50개 행동 및 20개 에이전트 문제를 1초 이내에 해결)에서 기존 문헌 접근법을 능가합니다. 비용 함수가 변경됨에 따라 할당된 역할이 달라지는 점은 다양한 생산 요구 사항에 대한 아키텍처의 유연성을 강조합니다. 마지막으로, 주관적 평가는 높은 사용성 수준과 대상 시나리오에 대한 적합성을 입증합니다.

## 핵심 내용
핸들링, 용접, 조립 등 여러 산업 응용 분야에서 인간-로봇 협업 프로세스의 배치가 증가함에 따라, 대규모 이종 팀을 관리하면서 동시에 복잡한 작업의 실행을 모니터링할 수 있는 시스템에 대한 추구가 확대되고 있습니다. 본 논문에서는 임의 크기의 인간-로봇 혼합 팀에서 동적 역할 할당 및 협업 작업 계획을 위한 새로운 아키텍처를 제시합니다. 이 아키텍처는 행동 스케줄링을 담당하는 Behavior Trees(BTs) 기반의 중앙 집중식 반응형 및 모듈식 작업 무관 계획 방법을 활용하며, 할당 문제는 Mixed-Integer Linear Program(MILP)을 통해 공식화되어 팀 에이전트에게 개별 역할 또는 협업을 동적으로 할당합니다. MILP 비용으로 사용되는 다양한 지표를 통해 아키텍처는 협업의 여러 측면(예: makespan, 인간공학, 인간 선호도)을 우선시할 수 있습니다. 인간 선호도는 협상 단계를 통해 식별되며, 이 단계에서 인간 에이전트는 할당된 작업의 실행을 수락하거나 거부할 수 있습니다. 또한, 인간과 시스템 간의 양방향 통신은 다양한 행동 단계에서 작업자를 지원하고 조정하는 직관적인 기능을 제공하는 맞춤형 Augmented Reality(AR) 사용자 인터페이스를 통해 구현됩니다. 제안된 방법론의 계산 복잡성은 산업 규모의 작업 및 팀(협업이 포함된 최대 50개 행동 및 20개 에이전트 문제를 1초 이내에 해결)에서 기존 문헌 접근법을 능가합니다. 비용 함수가 변경됨에 따라 할당된 역할이 달라지는 점은 다양한 생산 요구 사항에 대한 아키텍처의 유연성을 강조합니다. 마지막으로, 주관적 평가는 높은 사용성 수준과 대상 시나리오에 대한 적합성을 입증합니다.
