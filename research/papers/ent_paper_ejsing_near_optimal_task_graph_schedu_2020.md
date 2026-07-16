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

## Overview
Task graph scheduling is a relevant problem in computer science with application to diverse real world domains. Task graph scheduling suffers from a combinatorial explosion and thus finding optimal schedulers is a difficult task. In this paper we present a methodology for computing near-optimal preemptive and non-preemptive schedulers for task graphs. The task graph scheduling problem is reduced to location reachability via the fastest path in Priced Timed Automata (PTA) and Priced Timed Markov Decision Processes (PTMDP). Additionally, we explore the effect of using chains to reduce the computation time for finding schedules. We have implemented our models in UPPAAL CORA and UPPAAL STRATEGO. We conduct an exhaustive experimental evaluation where we compare our resulting schedules with the best-known schedules of a state of the art tool. A significant number of our resulting schedules are shown to be shorter than or equal to the best-known schedules.

## Content
Task graph scheduling is a relevant problem in computer science with application to diverse real world domains. Task graph scheduling suffers from a combinatorial explosion and thus finding optimal schedulers is a difficult task. In this paper we present a methodology for computing near-optimal preemptive and non-preemptive schedulers for task graphs. The task graph scheduling problem is reduced to location reachability via the fastest path in Priced Timed Automata (PTA) and Priced Timed Markov Decision Processes (PTMDP). Additionally, we explore the effect of using chains to reduce the computation time for finding schedules. We have implemented our models in UPPAAL CORA and UPPAAL STRATEGO. We conduct an exhaustive experimental evaluation where we compare our resulting schedules with the best-known schedules of a state of the art tool. A significant number of our resulting schedules are shown to be shorter than or equal to the best-known schedules.

## 개요
태스크 그래프 스케줄링은 컴퓨터 과학에서 중요한 문제로, 다양한 실제 도메인에 응용됩니다. 태스크 그래프 스케줄링은 조합적 폭발(combinatorial explosion) 문제를 겪기 때문에 최적의 스케줄러를 찾는 것은 어려운 작업입니다. 본 논문에서는 태스크 그래프에 대한 준최적의 선점형 및 비선점형 스케줄러를 계산하는 방법론을 제시합니다. 태스크 그래프 스케줄링 문제는 가격 시간 오토마타(PTA)와 가격 시간 마르코프 결정 과정(PTMDP)에서 최단 경로를 통한 위치 도달성 문제로 축소됩니다. 또한, 체인을 사용하여 스케줄 탐색 시간을 줄이는 효과를 탐구합니다. 우리는 UPPAAL CORA와 UPPAAL STRATEGO에서 모델을 구현했습니다. 최첨단 도구의 알려진 최고 스케줄과 결과 스케줄을 비교하는 철저한 실험적 평가를 수행했습니다. 상당수의 결과 스케줄이 알려진 최고 스케줄보다 짧거나 같음을 보여줍니다.

## 핵심 내용
태스크 그래프 스케줄링은 컴퓨터 과학에서 중요한 문제로, 다양한 실제 도메인에 응용됩니다. 태스크 그래프 스케줄링은 조합적 폭발(combinatorial explosion) 문제를 겪기 때문에 최적의 스케줄러를 찾는 것은 어려운 작업입니다. 본 논문에서는 태스크 그래프에 대한 준최적의 선점형 및 비선점형 스케줄러를 계산하는 방법론을 제시합니다. 태스크 그래프 스케줄링 문제는 가격 시간 오토마타(PTA)와 가격 시간 마르코프 결정 과정(PTMDP)에서 최단 경로를 통한 위치 도달성 문제로 축소됩니다. 또한, 체인을 사용하여 스케줄 탐색 시간을 줄이는 효과를 탐구합니다. 우리는 UPPAAL CORA와 UPPAAL STRATEGO에서 모델을 구현했습니다. 최첨단 도구의 알려진 최고 스케줄과 결과 스케줄을 비교하는 철저한 실험적 평가를 수행했습니다. 상당수의 결과 스케줄이 알려진 최고 스케줄보다 짧거나 같음을 보여줍니다.
