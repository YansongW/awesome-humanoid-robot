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
  en: A 2014 ICALP paper that classifies the computational complexity of partitioning undirected graphs into same-size stars
    on subclasses of perfect graphs, presenting polynomial-time algorithms for several graph classes and NP-hardness results
    for others.
  zh: 一篇2014年ICALP论文，对完美图子类上无向图划分为同尺寸星图问题的计算复杂性进行分类，给出了多个图类上的多项式时间算法及其他图类上的NP难结果。
  ko: 2014년 ICALP 논문으로, 완벽 그래프의 하위 클래스에서 무방향 그래프를 동일한 크기의 별로 분할하는 문제의 계산 복잡도를 분류하고, 여러 그래프 클래스에 대해 다항 시간 알고리즘과 다른 클래스에 대한
    NP-hardness 결과를 제시한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1402.2589v3.
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
## 概述
The partition of graphs into "nice" subgraphs is a central algorithmic problem with strong ties to matching theory. We study the partitioning of undirected graphs into same-size stars, a problem known to be NP-complete even for the case of stars on three vertices. We perform a thorough computational complexity study of the problem on subclasses of perfect graphs and identify several polynomial-time solvable cases, for example, on interval graphs and bipartite permutation graphs, and also NP-complete cases, for example, on grid graphs and chordal graphs.

## 核心内容
The partition of graphs into "nice" subgraphs is a central algorithmic problem with strong ties to matching theory. We study the partitioning of undirected graphs into same-size stars, a problem known to be NP-complete even for the case of stars on three vertices. We perform a thorough computational complexity study of the problem on subclasses of perfect graphs and identify several polynomial-time solvable cases, for example, on interval graphs and bipartite permutation graphs, and also NP-complete cases, for example, on grid graphs and chordal graphs.

## 参考
- http://arxiv.org/abs/1402.2589v3

