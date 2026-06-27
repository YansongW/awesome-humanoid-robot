---
$id: ent_paper_ejsing_near_optimal_task_graph_schedu_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Near Optimal Task Graph Scheduling with Priced Timed Automata and Priced Timed
    Markov Decision Processes
  zh: 基于 priced timed automata 与 priced timed Markov decision processes 的近优任务图调度
  ko: Priced Timed Automata 및 Priced Timed Markov Decision Processes를 이용한 근사 최적 작업
    그래프 스케줄링
summary:
  en: This paper reduces preemptive and non-preemptive task graph scheduling to fastest-path
    location reachability in Priced Timed Automata and Priced Timed Markov Decision
    Processes, implements the approach in Uppaal Cora and Uppaal Stratego, and evaluates
    it on the Kasahara-Narita standard task graph set.
  zh: 本文将抢占式与非抢占式任务图调度问题归约为 priced timed automata 与 priced timed Markov decision processes
    中的最快路径位置可达性问题，并在 Uppaal Cora 与 Uppaal Stratego 中实现，使用 Kasahara-Narita 标准任务图集进行评估。
  ko: 본 논문은 선점형 및 비선점형 작업 그래프 스케줄링을 Priced Timed Automata와 Priced Timed Markov Decision
    Processes에서의 최단 경로 위치 도달 문제로 환원한 후 Uppaal Cora와 Uppaal Stratego로 구현하고 Kasahara-Narita
    표준 작업 그래프 집합으로 평가한다.
domains:
- 05_mass_production
- 03_manufacturing_processes
- 07_ai_models_algorithms
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- task_graph_scheduling
- priced_timed_automata
- priced_timed_markov_decision_processes
- chain_decomposition
- manufacturing_orchestration
- production_line_optimization
- uppaal_cora
- uppaal_stratego
- near_optimal_scheduling
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the supplied metadata/abstract; full-text verification
    and human review are still required.
sources:
- id: src_001
  type: paper
  title: Near Optimal Task Graph Scheduling with Priced Timed Automata and Priced
    Timed Markov Decision Processes
  url: https://arxiv.org/abs/2002.10783
  date: '2020'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Task graph scheduling is an NP-complete combinatorial problem with applications in parallel computing and production workflow optimization. This paper introduces a methodology for computing near-optimal preemptive and non-preemptive schedulers by reducing the scheduling problem to fastest-path location reachability in Priced Timed Automata (PTA) and Priced Timed Markov Decision Processes (PTMDP). The models are implemented in Uppaal Cora and Uppaal Stratego, respectively.

To mitigate state-space explosion, the authors explore chain decomposition of task graphs. By grouping tasks into chains, the number of scheduling choices is reduced and computation time is lowered. The approach is evaluated exhaustively on the Kasahara-Narita standard task graph set, spanning graphs from 50 to 1000 tasks and multiprocessor configurations with 2, 4, 8, and 16 machines. The results show that many of the produced schedules are shorter than or equal to the previously best-known non-preemptive schedules.

The work is purely algorithmic and does not study humanoid hardware directly. Its relevance to humanoid robotics lies in its applicability to production-line scheduling, assembly sequencing, and resource allocation workflows that support scalable manufacturing.

## Key Contributions

- Reduction of preemptive and non-preemptive task graph scheduling to fastest-path location reachability in PTA and PTMDP.
- Use of chain decomposition to reduce scheduler choices and computation time.
- Implementation of the proposed models in Uppaal Cora and Uppaal Stratego.
- Experimental comparison against the Kasahara-Narita best-known schedules on task graphs of up to 1000 tasks.
- Demonstration that many produced schedules match or improve upon the best-known non-preemptive schedules.

## Relevance to Humanoid Robotics

Although the paper does not address humanoid robot hardware or control, its scheduling methodology can be applied to manufacturing process orchestration and production-line optimization, which are key enablers for humanoid robot mass production. Efficient task graph scheduling supports assembly sequencing, resource allocation, and workflow balancing in industrial settings. For this reason, the work is classified under mass production, manufacturing processes, and AI models/algorithms domains within the knowledge base.
