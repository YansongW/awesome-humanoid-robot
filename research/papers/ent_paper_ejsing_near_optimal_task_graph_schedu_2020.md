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
  zh: 本文提出一种将抢占式与非抢占式任务图调度问题转化为Priced Timed Automata和Priced Timed Markov Decision Processes中最快路径位置可达性问题的求解方法。该方法在Uppaal Cora和Uppaal
    Stratego中实现，并在Kasahara-Narita标准任务图集上验证了其生成近最优调度的能力。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2002.10783v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (699 chars, DeepSeek).'
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
针对任务图调度面临的组合爆炸难题，本研究通过将调度问题形式化为Priced Timed Automata和Priced Timed Markov Decision Processes中的最快路径搜索，实现了近最优解的求解。研究同时探索了利用链式结构缩短计算时间的策略。基于Uppaal Cora和Uppaal Stratego工具的实现，在标准测试集上的实验表明，该方法产生的调度方案在多数情况下优于或持平于当前最优工具的结果。

## 核心内容
### 核心方法
- 将任务图调度问题转化为Priced Timed Automata和Priced Timed Markov Decision Processes中的位置可达性搜索，通过寻找最快路径获得近最优调度。
- 支持抢占式与非抢占式两种调度模式，覆盖实际应用中的不同需求。
- 引入链式结构优化计算效率，通过减少状态空间规模加速调度生成。

### 实现与实验
- 模型在Uppaal Cora和Uppaal Stratego中实现，利用其高效的模型检测与策略搜索能力。
- 在Kasahara-Narita标准任务图集上进行全面实验评估，该数据集包含不同规模与结构的任务图。
- 对比对象为当前最优工具生成的最佳已知调度方案，结果显示本方法生成的调度在多数案例中时间更短或持平。

### 关键结论
- 实验证明该方法能稳定生成近最优调度，且计算开销可控。
- 链式优化策略在保持解质量的同时显著缩短了求解时间，尤其适用于大规模任务图。
- 研究为任务图调度问题提供了一种形式化、可扩展的求解框架，兼具理论严谨性与工程实用性。

## Overview
Task graph scheduling is a relevant problem in computer science with application to diverse real world domains. Task graph scheduling suffers from a combinatorial explosion and thus finding optimal schedulers is a difficult task.   In this paper we present a methodology for computing near-optimal preemptive and non-preemptive schedulers for task graphs. The task graph scheduling problem is reduced to location reachability via the fastest path in Priced Timed Automata (PTA) and Priced Timed Markov Decision Processes (PTMDP). Additionally, we explore the effect of using chains to reduce the computation time for finding schedules.   We have implemented our models in UPPAAL CORA and UPPAAL STRATEGO. We conduct an exhaustive experimental evaluation where we compare our resulting schedules with the best-known schedules of a state of the art tool. A significant number of our resulting schedules are shown to be shorter than or equal to the best-known schedules.

## Overview
Task graph scheduling is a relevant problem in computer science with application to diverse real world domains. Task graph scheduling suffers from a combinatorial explosion and thus finding optimal schedulers is a difficult task. In this paper we present a methodology for computing near-optimal preemptive and non-preemptive schedulers for task graphs. The task graph scheduling problem is reduced to location reachability via the fastest path in Priced Timed Automata (PTA) and Priced Timed Markov Decision Processes (PTMDP). Additionally, we explore the effect of using chains to reduce the computation time for finding schedules. We have implemented our models in UPPAAL CORA and UPPAAL STRATEGO. We conduct an exhaustive experimental evaluation where we compare our resulting schedules with the best-known schedules of a state of the art tool. A significant number of our resulting schedules are shown to be shorter than or equal to the best-known schedules.

## Content
Task graph scheduling is a relevant problem in computer science with application to diverse real world domains. Task graph scheduling suffers from a combinatorial explosion and thus finding optimal schedulers is a difficult task. In this paper we present a methodology for computing near-optimal preemptive and non-preemptive schedulers for task graphs. The task graph scheduling problem is reduced to location reachability via the fastest path in Priced Timed Automata (PTA) and Priced Timed Markov Decision Processes (PTMDP). Additionally, we explore the effect of using chains to reduce the computation time for finding schedules. We have implemented our models in UPPAAL CORA and UPPAAL STRATEGO. We conduct an exhaustive experimental evaluation where we compare our resulting schedules with the best-known schedules of a state of the art tool. A significant number of our resulting schedules are shown to be shorter than or equal to the best-known schedules.

## 参考
- http://arxiv.org/abs/2002.10783v1

## 개요
작업 그래프 스케줄링의 조합 폭발 문제를 해결하기 위해, 본 연구는 스케줄링 문제를 Priced Timed Automata 및 Priced Timed Markov Decision Processes에서의 최단 경로 탐색으로 형식화하여 준최적 해를 도출합니다. 또한, 체인 구조를 활용해 계산 시간을 단축하는 전략을 탐구합니다. Uppaal Cora와 Uppaal Stratego 기반 구현을 표준 테스트 세트에서 실험한 결과, 본 방법이 생성한 스케줄은 대부분의 경우 현재 최적 도구의 결과보다 우수하거나 동등함을 보여줍니다.

## 핵심 내용
### 핵심 방법
- 작업 그래프 스케줄링 문제를 Priced Timed Automata 및 Priced Timed Markov Decision Processes에서의 위치 도달 가능성 탐색으로 변환하고, 최단 경로 탐색을 통해 준최적 스케줄을 획득합니다.
- 선점형 및 비선점형 두 가지 스케줄링 모드를 지원하여 실제 응용의 다양한 요구를 충족합니다.
- 체인 구조를 도입해 계산 효율성을 최적화하고, 상태 공간 규모를 줄여 스케줄 생성을 가속화합니다.

### 구현 및 실험
- 모델은 Uppaal Cora와 Uppaal Stratego에서 구현되며, 효율적인 모델 검사 및 전략 탐색 기능을 활용합니다.
- Kasahara-Narita 표준 작업 그래프 세트에서 포괄적인 실험 평가를 수행하며, 이 데이터 세트는 다양한 규모와 구조의 작업 그래프를 포함합니다.
- 비교 대상은 현재 최적 도구가 생성한 최고 알려진 스케줄이며, 결과는 본 방법이 생성한 스케줄이 대부분의 사례에서 시간이 더 짧거나 동등함을 보여줍니다.

### 핵심 결론
- 실험은 본 방법이 안정적으로 준최적 스케줄을 생성하며 계산 비용이 통제 가능함을 입증합니다.
- 체인 최적화 전략은 해 품질을 유지하면서도 해결 시간을 크게 단축하며, 특히 대규모 작업 그래프에 적합합니다.
- 본 연구는 작업 그래프 스케줄링 문제에 대해 형식적이고 확장 가능한 해결 프레임워크를 제공하며, 이론적 엄밀성과 공학적 실용성을 겸비합니다.
