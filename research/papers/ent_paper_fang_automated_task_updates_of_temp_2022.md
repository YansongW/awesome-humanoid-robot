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
  en: This paper defines the task update problem for heterogeneous robots executing existing Linear Temporal Logic (LTL) tasks,
    and proposes a framework that synthesizes updated individual behaviors by intersecting the remaining current-task Büchi
    automaton with new-task Büchi automata, followed by a heuristic token-based conflict-resolution allocation algorithm.
  zh: 本文针对执行现有线性时序逻辑（LTL）任务的异构机器人定义了任务更新问题，并提出了一种框架：通过将剩余当前任务 Büchi 自动机与新任务 Büchi 自动机求交来合成更新的个体行为，随后采用启发式基于令牌的冲突消解分配算法。
  ko: 본 논문은 기존 선형시제논리(LTL) 작업을 수행하는 이종 로봇 군을 위한 작업 갱신 문제를 정의하고, 남아 있는 현재 작업 Büchi 오토마톤과 새 작업 Büchi 오토마톤의 교차를 통해 갱신된 개별 행위를
    합성한 뒤 휴리스틱 토큰 기반 충돌 해소 할당 알고리즘을 적용하는 프레임워크를 제안한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2204.05423v3.
sources:
- id: src_001
  type: paper
  title: Automated Task Updates of Temporal Logic Specifications for Heterogeneous Robots
  url: https://arxiv.org/abs/2204.05423
  date: '2022'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---
## 概述
Given a heterogeneous group of robots executing a complex task represented in Linear Temporal Logic, and a new set of tasks for the group, we define the task update problem and propose a framework for automatically updating individual robot tasks given their respective existing tasks and capabilities. Our heuristic, token-based, conflict resolution task allocation algorithm generates a near-optimal assignment for the new task. We demonstrate the scalability of our approach through simulations of multi-robot tasks.

## 核心内容
Given a heterogeneous group of robots executing a complex task represented in Linear Temporal Logic, and a new set of tasks for the group, we define the task update problem and propose a framework for automatically updating individual robot tasks given their respective existing tasks and capabilities. Our heuristic, token-based, conflict resolution task allocation algorithm generates a near-optimal assignment for the new task. We demonstrate the scalability of our approach through simulations of multi-robot tasks.

## 参考
- http://arxiv.org/abs/2204.05423v3

