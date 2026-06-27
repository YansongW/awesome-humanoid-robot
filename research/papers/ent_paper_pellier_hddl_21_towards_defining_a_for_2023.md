---
$id: ent_paper_pellier_hddl_21_towards_defining_a_for_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HDDL 2.1: Towards Defining a Formalism and a Semantics for Temporal HTN Planning'
  zh: HDDL 2.1：面向时序HTN规划的形式化与语义定义
  ko: 'HDDL 2.1: 시간적 HTN 계획을 위한 형식화 및 의미 정의를 향하여'
summary:
  en: Proposes a lifted temporal HTN planning formalism and execution semantics that
    extends HDDL with durative actions, temporal task networks, and decomposition
    constraints inspired by PDDL 2.1 and ANML.
  zh: 提出一种 lifted 时序 HTN 规划形式化及执行语义，通过借鉴 PDDL 2.1 与 ANML，将 HDDL 扩展为支持持续动作、时序任务网络与分解约束。
  ko: PDDL 2.1과 ANML에서 영감을 받아 HDDL을 지속적 동작, 시간적 작업 네트워크 및 분해 제약으로 확장하는 lifted temporal
    HTN 계획 형식화 및 실행 의미를 제안한다.
domains:
- 07_ai_models_algorithms
- 04_assembly_integration_testing
- 05_mass_production
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- temporal_htn_planning
- hierarchical_task_network
- durative_actions
- task_decomposition
- pddl
- pddl_2_1
- anml
- automated_planning
- robotics_planning
- planning_formalism
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from metadata and abstract; requires human review against the
    full paper before verification.
sources:
- id: src_001
  type: paper
  title: 'HDDL 2.1: Towards Defining a Formalism and a Semantics for Temporal HTN
    Planning'
  url: https://arxiv.org/abs/2306.07353
  date: '2023'
  accessed_at: '2026-06-27'
theoretical_depth:
- formalism
- method
---

## Overview

The paper addresses the gap between Hierarchical Task Network (HTN) planning formalisms and the practical needs of robotics and industrial applications, where concurrent and durative action execution is essential. It proposes a lifted temporal HTN planning formalism referred to as HDDL 2.1, extending HDDL with temporal and numerical constructs drawn from PDDL 2.1 and ANML. The authors define durative actions and snap actions, temporal task networks with qualitative ordering and variable binding constraints, and an execution semantics for primitive temporal task sequences and decomposition-based refinement.

The contribution is presented as a foundation for discussion rather than a finalized standard: the authors provide formal definitions, identify open issues such as point-algebra delays and continuous effects, and release an open-source parser and benchmark suite in the PDDL4J library to support reproducible research.

## Key Contributions

- Formal definition of durative actions and snap actions within a lifted temporal HTN framework.
- Definition of temporal task networks with qualitative ordering, variable binding, duration, and temporal decomposition constraints.
- Execution semantics for primitive temporal task sequences and decomposition-based refinement.
- Open-source parser and benchmark suite released as part of the PDDL4J library.

## Relevance to Humanoid Robotics

Temporal HTN planning is directly relevant to humanoid robot mass production and deployment because humanoid assembly and manipulation tasks require coordinated, concurrent, and durative action scheduling. The ability to model task hierarchies with temporal and numerical constraints supports production-line coordination, tool-use sequencing, and multi-robot collaboration. By extending HDDL toward PDDL 2.1 expressivity, this work provides a formal substrate for planners that must reason about action durations, resource usage, and temporal deadlines in realistic humanoid workcells.
