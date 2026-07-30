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
  zh: 这是一篇2014年ICALP会议论文，研究了将无向图划分为相同大小的星形子图的计算复杂性。作者在完美图的子类上进行了系统分类，对区间图、二分置换图等类别给出了多项式时间算法，对网格图、弦图等类别证明了NP完全性。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1402.2589v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
该论文聚焦于将无向图划分为相同大小的星形子图这一经典算法问题，该问题即使对于三顶点星形也已知是NP完全的。作者在完美图的多个子类上进行了全面的计算复杂性分析，识别出若干多项式时间可解的情况，例如区间图和二分置换图，同时也发现了NP完全的情况，例如网格图和弦图。这项工作与匹配理论有紧密联系，为图划分问题的复杂性边界提供了重要见解。

## 核心内容
### 问题定义
- 研究将无向图划分为相同大小的星形子图（star），每个星形由一个中心顶点和若干叶子顶点组成。
- 该问题与匹配理论密切相关，是图划分领域的核心算法问题之一。

### 主要结果
- **多项式时间可解类**：
  - 区间图（interval graphs）
  - 二分置换图（bipartite permutation graphs）
  - 其他完美图子类
- **NP完全类**：
  - 网格图（grid graphs）
  - 弦图（chordal graphs）
  - 三顶点星形情况已知为NP完全

### 方法
- 针对多项式时间可解类，设计了基于动态规划和图结构特性的算法。
- 对于NP完全类，通过从已知NP完全问题（如3-SAT或图着色问题）进行归约来证明。

### 实验与结论
- 论文未提供实验数据，主要贡献是理论复杂性分类。
- 结论：在完美图子类中，该问题的复杂性边界清晰，某些结构特性（如区间性、置换性）导致多项式可解，而网格和弦结构则导致NP完全性。

## Overview
The partition of graphs into "nice" subgraphs is a central algorithmic problem with strong ties to matching theory. We study the partitioning of undirected graphs into same-size stars, a problem known to be NP-complete even for the case of stars on three vertices. We perform a thorough computational complexity study of the problem on subclasses of perfect graphs and identify several polynomial-time solvable cases, for example, on interval graphs and bipartite permutation graphs, and also NP-complete cases, for example, on grid graphs and chordal graphs.

## 개요
그래프를 "좋은" 부분 그래프로 분할하는 것은 매칭 이론과 강한 연관성을 가진 중심적인 알고리즘 문제입니다. 우리는 무방향 그래프를 동일한 크기의 별 모양으로 분할하는 문제를 연구하며, 이 문제는 세 개의 꼭짓점을 가진 별의 경우에도 NP-완전인 것으로 알려져 있습니다. 우리는 완전 그래프의 부분 클래스에 대해 이 문제의 계산 복잡성을 철저히 연구하고, 예를 들어 구간 그래프와 이분 순열 그래프에서 다항 시간에 해결 가능한 여러 경우와, 예를 들어 격자 그래프와 현 그래프에서 NP-완전인 경우를 식별합니다.

## 핵심 내용
그래프를 "좋은" 부분 그래프로 분할하는 것은 매칭 이론과 강한 연관성을 가진 중심적인 알고리즘 문제입니다. 우리는 무방향 그래프를 동일한 크기의 별 모양으로 분할하는 문제를 연구하며, 이 문제는 세 개의 꼭짓점을 가진 별의 경우에도 NP-완전인 것으로 알려져 있습니다. 우리는 완전 그래프의 부분 클래스에 대해 이 문제의 계산 복잡성을 철저히 연구하고, 예를 들어 구간 그래프와 이분 순열 그래프에서 다항 시간에 해결 가능한 여러 경우와, 예를 들어 격자 그래프와 현 그래프에서 NP-완전인 경우를 식별합니다.

## 参考
- http://arxiv.org/abs/1402.2589v3
