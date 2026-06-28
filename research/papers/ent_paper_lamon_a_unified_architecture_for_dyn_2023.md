---
$id: ent_paper_lamon_a_unified_architecture_for_dyn_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Unified Architecture for Dynamic Role Allocation and Collaborative Task Planning
    in Mixed Human-Robot Teams
  zh: 混合人机团队中动态角色分配与协作任务规划的统一架构
  ko: 혼합 인간-로봇 팀에서의 동적 역할 할당 및 협업 작업 계획을 위한 통합 아키텍처
summary:
  en: This paper proposes a unified architecture that combines a centralized Behavior
    Tree planner for action scheduling with a Mixed-Integer Linear Program for dynamic
    role allocation in mixed human-robot teams, supported by an Augmented Reality
    interface for human-system negotiation.
  zh: 本文提出了一种统一架构，将用于动作调度的集中式行为树规划器与用于混合人机团队中动态角色分配的混合整数线性规划相结合，并通过增强现实界面实现人机协商。
  ko: 본 논문은 동작 스케줄링을 위한 중앙 집중형 비헤이비어 트리 플래너와 혼합 인간-로봇 팀에서의 동적 역할 할당을 위한 혼합정수선형계획법을
    결합하고, 증강 현실 인터페이스를 통해 인간-시스템 간 협상을 지원하는 통합 아키텍처를 제안한다.
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
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from metadata and abstract; full-text verification needed before
    promotion to verified status.; approved by autonomous review workflow.
sources:
- id: src_001
  type: paper
  title: A Unified Architecture for Dynamic Role Allocation and Collaborative Task
    Planning in Mixed Human-Robot Teams
  url: https://arxiv.org/abs/2301.08038
  date: '2023'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
- system
---

## Overview

The paper addresses the problem of coordinating mixed human-robot teams in industrial collaborative processes such as handling, welding, and assembly. It proposes a unified architecture in which a centralized, reactive, modular, and task-agnostic planner based on Behavior Trees (BTs) handles action scheduling, while a Mixed-Integer Linear Program (MILP) dynamically assigns individual roles or collaborations to agents. The system supports human preferences through a negotiation phase and uses an Augmented Reality (AR) interface to enable bilateral communication between workers and the planning system.

The MILP formulation is a core technical contribution: it encodes role allocation over individual agents and agent pairs (human-robot, robot-robot, human-human), allowing the optimizer to select collaborations when they are beneficial. Different cost functions (e.g., makespan, ergonomics, human preferences) can be plugged in to favor different production requirements. The authors report that industrial-scale problems with up to 50 actions and 20 agents are solved within one second.

Validation includes both large-scale simulations and a real-world table-assembly experiment involving a Franka Emika Panda robot, a Robotiq 2F-85 gripper, a Microsoft HoloLens 2 AR headset, and human participants. Subjective usability evaluation indicates high suitability for the targeted industrial scenario.

## Key Contributions

- A unified architecture integrating Behavior Trees for task-agnostic planning with MILP-based dynamic role allocation.
- Extension of role allocation to collaborative roles (human-robot, robot-robot, human-human pairs) within a single MILP formulation.
- An AR-based user interface enabling bilateral human-system communication and negotiation of task assignments.
- A scalability evaluation showing industrial-sized problems (up to 50 actions and 20 agents) are solved within 1 second.
- Validation through simulations and a real-world table assembly task with a Franka Emika Panda robot and human subjects.

## Relevance to Humanoid Robotics

Although the real-world demonstration uses a fixed manipulator, the architecture is designed to be task-agnostic and scalable to teams of arbitrary size. Its combination of reactive BT planning, MILP-based dynamic role allocation, and AR-mediated human-robot negotiation is directly transferable to humanoid robot deployment in collaborative manufacturing cells. Humanoids can be treated as agents within the same MILP allocation framework, receiving roles or collaborations alongside human workers, while the AR interface can guide and coordinate workers during mixed human-humanoid operations.
