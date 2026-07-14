---
$id: ent_paper_ejsing_near_optimal_task_graph_schedu_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Near Optimal Task Graph Scheduling with Priced Timed Automata and Priced Timed Markov Decision Processes
  zh: 基于 priced timed automata 与 priced timed Markov decision processes 的近优任务图调度
  ko: Priced Timed Automata 및 Priced Timed Markov Decision Processes를 이용한 근사 최적 작업 그래프 스케줄링
summary:
  en: This paper reduces preemptive and non-preemptive task graph scheduling to fastest-path location reachability in Priced
    Timed Automata and Priced Timed Markov Decision Processes, implements the approach in Uppaal Cora and Uppaal Stratego,
    and evaluates it on the Kasahara-Narita standard task graph set.
  zh: 本文将抢占式与非抢占式任务图调度问题归约为 priced timed automata 与 priced timed Markov decision processes 中的最快路径位置可达性问题，并在 Uppaal Cora 与
    Uppaal Stratego 中实现，使用 Kasahara-Narita 标准任务图集进行评估。
  ko: 본 논문은 선점형 및 비선점형 작업 그래프 스케줄링을 Priced Timed Automata와 Priced Timed Markov Decision Processes에서의 최단 경로 위치 도달 문제로 환원한 후
    Uppaal Cora와 Uppaal Stratego로 구현하고 Kasahara-Narita 표준 작업 그래프 집합으로 평가한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2002.10783v1.
sources:
- id: src_001
  type: paper
  title: Near Optimal Task Graph Scheduling with Priced Timed Automata and Priced Timed Markov Decision Processes
  url: https://arxiv.org/abs/2002.10783
  date: '2020'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Task graph scheduling is a relevant problem in computer science with application to diverse real world domains. Task graph scheduling suffers from a combinatorial explosion and thus finding optimal schedulers is a difficult task.   In this paper we present a methodology for computing near-optimal preemptive and non-preemptive schedulers for task graphs. The task graph scheduling problem is reduced to location reachability via the fastest path in Priced Timed Automata (PTA) and Priced Timed Markov Decision Processes (PTMDP). Additionally, we explore the effect of using chains to reduce the computation time for finding schedules.   We have implemented our models in UPPAAL CORA and UPPAAL STRATEGO. We conduct an exhaustive experimental evaluation where we compare our resulting schedules with the best-known schedules of a state of the art tool. A significant number of our resulting schedules are shown to be shorter than or equal to the best-known schedules.

## 核心内容
Task graph scheduling is a relevant problem in computer science with application to diverse real world domains. Task graph scheduling suffers from a combinatorial explosion and thus finding optimal schedulers is a difficult task.   In this paper we present a methodology for computing near-optimal preemptive and non-preemptive schedulers for task graphs. The task graph scheduling problem is reduced to location reachability via the fastest path in Priced Timed Automata (PTA) and Priced Timed Markov Decision Processes (PTMDP). Additionally, we explore the effect of using chains to reduce the computation time for finding schedules.   We have implemented our models in UPPAAL CORA and UPPAAL STRATEGO. We conduct an exhaustive experimental evaluation where we compare our resulting schedules with the best-known schedules of a state of the art tool. A significant number of our resulting schedules are shown to be shorter than or equal to the best-known schedules.

## 参考
- http://arxiv.org/abs/2002.10783v1

