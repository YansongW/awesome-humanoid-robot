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
  zh: 本文提出了一种统一架构，将用于动作调度的集中式行为树规划器与用于混合人机团队中动态角色分配的混合整数线性规划相结合，并通过增强现实界面实现人机协商。
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

