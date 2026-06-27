---
$id: ent_paper_bevern_partitioning_perfect_graphs_in_2014
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Partitioning Perfect Graphs into Stars
  zh: 将完美图划分为星图
  ko: 완벽 그래프를 별로 분할하기
summary:
  en: A 2014 ICALP paper that classifies the computational complexity of partitioning
    undirected graphs into same-size stars on subclasses of perfect graphs, presenting
    polynomial-time algorithms for several graph classes and NP-hardness results for
    others.
  zh: 一篇2014年ICALP论文，对完美图子类上无向图划分为同尺寸星图问题的计算复杂性进行分类，给出了多个图类上的多项式时间算法及其他图类上的NP难结果。
  ko: 2014년 ICALP 논문으로, 완벽 그래프의 하위 클래스에서 무방향 그래프를 동일한 크기의 별로 분할하는 문제의 계산 복잡도를 분류하고,
    여러 그래프 클래스에 대해 다항 시간 알고리즘과 다른 클래스에 대한 NP-hardness 결과를 제시한다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- graph_partitioning
- star_partition
- combinatorial_optimization
- task_allocation
- multi_agent_coordination
- perfect_graphs
- interval_graphs
- computational_complexity
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from metadata and abstract; full-text verification not performed.
    Human review required before production use.
sources:
- id: src_001
  type: paper
  title: Partitioning Perfect Graphs into Stars
  url: https://arxiv.org/abs/1402.2589
  date: '2014'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Partitioning Perfect Graphs into Stars (van Bevern et al., ICALP 2014) investigates the Star Partition problem, which asks whether an undirected graph can be partitioned into same-size stars. The authors perform a computational complexity classification across subclasses of perfect graphs. They identify polynomial-time solvable cases including unit interval graphs, trivially perfect graphs, cographs, and bipartite permutation graphs, and establish NP-hardness for cases such as grid graphs and chordal graphs. A notable dichotomy is shown for split graphs: polynomial-time solvable for stars of size two (P3-Partition) but NP-hard for stars of size three or greater.

The technical approach combines greedy algorithms and dynamic programming for tractable graph classes with NP-hardness reductions for intractable ones. The study is purely theoretical and does not include empirical benchmarks or implementations.

## Key Contributions

- Linear-time algorithms for Star Partition on unit interval graphs and trivially perfect graphs.
- A quasilinear-time algorithm for P3-Partition on interval graphs.
- Polynomial-time algorithms for Star Partition on cographs and bipartite permutation graphs.
- NP-hardness results for P3-Partition on grid graphs and chordal graphs.
- Dichotomy on split graphs: polynomial-time solvable for s=2 but NP-hard for s≥3.

## Relevance to Humanoid Robotics

The paper is not directly about humanoid robotics; it is a theoretical graph-algorithms contribution. Its team-formation interpretation on interval graphs—partitioning agents into same-size teams each with a designated hub member—could loosely inform task-allocation or coordination models for fleets of humanoid robots. However, the relevance is indirect, and no robotic application, embodiment, or empirical validation is provided.
