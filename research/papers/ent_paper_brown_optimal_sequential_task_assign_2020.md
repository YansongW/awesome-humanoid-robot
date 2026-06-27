---
$id: ent_paper_brown_optimal_sequential_task_assign_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Optimal Sequential Task Assignment and Path Finding for Multi-Agent Robotic
    Assembly Planning
  zh: 多机器人装配规划中的最优顺序任务分配与路径规划
  ko: 다중 에이전트 로봇 조립 계획을 위한 최적 순차 작업 할당 및 경로 탐색
summary:
  en: Proposes a hierarchical optimal solver for precedence-constrained multi-agent
    task assignment and path finding (PC-TAPF), integrating MILP-based assignment,
    conflict-based search, incremental slack-prioritized search, and slack-aware A*
    to minimize makespan in robotic assembly.
  zh: 针对带先后次序约束的多智能体任务分配与路径规划（PC-TAPF）问题，提出了一种分层最优求解器，整合基于混合整数线性规划（MILP）的任务分配、冲突搜索、增量松弛优先搜索和松弛感知
    A*，以最小化机器人装配的完工时间。
  ko: 선행 제약 조건이 있는 다중 에이전트 작업 할당 및 경로 탐색(PC-TAPF) 문제를 해결하기 위해 MILP 기반 할당, 충돌 기반 탐색,
    증분형 여유 우선 탐색, 여유 인지 A*를 통합한 계층적 최적 솔버를 제안한다.
domains:
- 04_assembly_integration_testing
- 07_ai_models_algorithms
- 03_manufacturing_processes
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- multi_agent_planning
- task_assignment
- path_planning
- precedence_constraints
- collision_free_routing
- makespan_optimization
- robotic_assembly
- conflict_based_search
- differential_drive_robots
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from abstract and metadata; full-text review required before
    final verification.
sources:
- id: src_001
  type: paper
  title: Optimal Sequential Task Assignment and Path Finding for Multi-Agent Robotic
    Assembly Planning
  url: https://arxiv.org/abs/2006.08845
  date: '2020'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper studies the problem of sequential task assignment and collision-free routing for large teams of robots subject to inter-task precedence constraints, termed Precedence-Constrained Task Assignment and Path Finding (PC-TAPF). Applications include robotic manufacturing, where sub-assemblies must be finished before they can be combined into the final product. The authors formulate the problem as a makespan-minimization task and propose a four-level hierarchical optimal solver.

The solver consists of Sequential Next-Best Assignment Search (NBS), which solves a relaxed MILP assignment problem; Conflict-Based Search (CBS), which resolves collisions between robot paths; Incremental Slack-Prioritized Search (ISPS), which builds routes using schedule slack; and a slack-and-collision-aware A* (A*_SC), which plans individual path segments. The authors evaluate the algorithm on randomly generated factory grid-world instances and demonstrate, in high-fidelity Webots simulation, that the planner can generate collision-free trajectories for non-holonomic differential-drive robots.

## Key Contributions

- Introduces the PC-TAPF problem formulation that combines sequential task assignment, precedence constraints, and collision-free routing.
- Proposes a hierarchical optimal solver integrating MILP-based next-best assignment, CBS, ISPS, and slack-aware A*.
- Demonstrates that instances with up to 40 robots and 60 tasks can be solved to optimality quickly in most cases.
- Shows the planner can generate collision-free trajectories for non-holonomic differential-drive robots in high-fidelity Webots simulation.

## Relevance to Humanoid Robotics

Although the paper focuses on factory mobile robot fleets rather than humanoid robots directly, its methods for precedence-constrained task assignment and collision-free multi-agent routing are foundational for coordinating robots during humanoid sub-assembly and manufacturing workflows. Humanoid production lines can reuse similar planners to schedule component transport, sub-assembly sequencing, and final integration steps while avoiding collisions among multiple mobile manipulators or transport robots.
