---
$id: ent_paper_fang_automated_task_updates_of_temp_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Automated Task Updates of Temporal Logic Specifications for Heterogeneous Robots
  zh: 异构机器人时序逻辑规范的自动任务更新
  ko: 이종 로봇을 위한 선형시제논리 명세의 자동 작업 갱신
summary:
  en: This paper defines the task update problem for heterogeneous robots executing
    existing Linear Temporal Logic (LTL) tasks, and proposes a framework that synthesizes
    updated individual behaviors by intersecting the remaining current-task Büchi
    automaton with new-task Büchi automata, followed by a heuristic token-based conflict-resolution
    allocation algorithm.
  zh: 本文针对执行现有线性时序逻辑（LTL）任务的异构机器人定义了任务更新问题，并提出了一种框架：通过将剩余当前任务 Büchi 自动机与新任务 Büchi
    自动机求交来合成更新的个体行为，随后采用启发式基于令牌的冲突消解分配算法。
  ko: 본 논문은 기존 선형시제논리(LTL) 작업을 수행하는 이종 로봇 군을 위한 작업 갱신 문제를 정의하고, 남아 있는 현재 작업 Büchi
    오토마톤과 새 작업 Büchi 오토마톤의 교차를 통해 갱신된 개별 행위를 합성한 뒤 휴리스틱 토큰 기반 충돌 해소 할당 알고리즘을 적용하는
    프레임워크를 제안한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- intelligence
- knowledge
tags:
- linear_temporal_logic
- task_allocation
- multi_robot
- heterogeneous_robots
- buchi_automata
- temporal_logic_planning
- dynamic_task_update
- token_based_algorithm
- behavior_synthesis
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: AI-extracted from the arXiv full text; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: Automated Task Updates of Temporal Logic Specifications for Heterogeneous
    Robots
  url: https://arxiv.org/abs/2204.05423
  date: '2022'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---

## Overview

The paper addresses the problem of automatically updating robot behaviors when a new task is introduced to a heterogeneous group of robots that are already executing tasks specified in Linear Temporal Logic (LTL). The authors formalize this as the new task distribution problem: given robots with current tasks, capabilities, and progress states, find an assignment of new sub-tasks that minimizes the total cost of updated behaviors while preserving feasibility of the ongoing tasks. The framework first determines how much of each current task has already been completed, then intersects the remaining current-task Büchi automaton with Büchi automata representing the new sub-tasks to synthesize combined behaviors.

For behavior synthesis, each robot translates its LTL formulas into Büchi automata using Spot, computes the reachable portion of the current-task automaton from the robot's current state, and intersects it with the new-task automata. A minimum-cost accepting path through the product of the robot model and the intersected automaton is found using Dijkstra's shortest path algorithm. Because costs are non-additive across sub-tasks, each robot evaluates all feasible combinations of sub-tasks it can perform. A heuristic token-based conflict-resolution algorithm then allocates sub-tasks among robots by passing an assignment token locally and resolving conflicts pairwise, yielding near-optimal assignments with lower computational cost than an exhaustive optimal search.

The authors validate the framework on a multi-robot simulation with three robots and five rooms, showing that robots interleave current and new tasks rather than executing them sequentially. They also compare the token-based allocation algorithm against the optimal assignment for varying team and task sizes, demonstrating near-optimal results with substantially reduced computation time.

## Key Contributions

- Mathematical formulation of the new task distribution problem for heterogeneous robots that already have ongoing LTL tasks.
- A framework that automatically updates individual robot behaviors by combining the remaining current-task Büchi automaton with new-task Büchi automata, accounting for task progress.
- A heuristic token-based conflict-resolution task allocation algorithm that finds near-optimal assignments without requiring token history, with complexity O(2mn) compared to O(mn) for the optimal exhaustive algorithm.
- Simulation-based scalability evaluation showing near-optimal allocation performance with much lower computation time than the optimal algorithm.

## Relevance to Humanoid Robotics

Although the paper uses abstract mobile robots with manipulator, scanner, and camera capabilities in its examples, the underlying framework is directly applicable to coordinated fleets of humanoid robots operating in dynamic automation environments such as factories or warehouses. Humanoid workcells often receive new instructions while already executing prior tasks, and the ability to re-synthesize behavior from temporal-logic specifications while respecting each robot's capabilities and current progress supports flexible, autonomous task management. The token-based allocation approach also maintains a flat hierarchy, which can simplify coordination among multiple humanoid agents without a centralized mediator.
