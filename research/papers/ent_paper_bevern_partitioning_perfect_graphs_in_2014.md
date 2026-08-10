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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1402.2589v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10: en/ko
    body retranslated from zh deep-read (637 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/1402.2589v3

## Overview
This paper focuses on the classical algorithmic problem of partitioning an undirected graph into equal-sized star subgraphs, which is known to be NP-complete even for three-vertex stars. The authors conduct a comprehensive computational complexity analysis across multiple subclasses of perfect graphs, identifying several polynomial-time solvable cases, such as interval graphs and bipartite permutation graphs, while also uncovering NP-complete cases, such as grid graphs and chordal graphs. This work is closely related to matching theory and provides important insights into the complexity boundaries of graph partitioning problems.

## Content
### Problem Definition
- Studies the partitioning of an undirected graph into equal-sized star subgraphs, where each star consists of a central vertex and several leaf vertices.
- This problem is closely related to matching theory and is one of the core algorithmic problems in the field of graph partitioning.

### Main Results
- **Polynomial-time solvable classes**:
  - Interval graphs
  - Bipartite permutation graphs
  - Other subclasses of perfect graphs
- **NP-complete classes**:
  - Grid graphs
  - Chordal graphs
  - The three-vertex star case is known to be NP-complete

### Methods
- For polynomial-time solvable classes, algorithms based on dynamic programming and graph structural properties are designed.
- For NP-complete classes, NP-completeness is proven via reductions from known NP-complete problems, such as 3-SAT or graph coloring problems.

### Experiments and Conclusions
- The paper does not provide experimental data; its main contribution is a theoretical complexity classification.
- Conclusion: Within subclasses of perfect graphs, the complexity boundaries of this problem are clear; certain structural properties (such as interval and permutation properties) lead to polynomial solvability, while grid and chordal structures result in NP-completeness.

## 개요
이 논문은 무방향 그래프를 동일한 크기의 스타(star) 부분 그래프로 분할하는 고전적인 알고리즘 문제에 초점을 맞추며, 이 문제는 세 개의 정점으로 이루어진 스타의 경우에도 NP-완전인 것으로 알려져 있습니다. 저자는 완전 그래프(perfect graph)의 여러 하위 클래스에 대해 포괄적인 계산 복잡성 분석을 수행하여, 구간 그래프(interval graphs)와 이분 순열 그래프(bipartite permutation graphs)와 같은 여러 다항 시간 해결 가능 사례를 식별하는 동시에, 격자 그래프(grid graphs)와 현 그래프(chordal graphs)와 같은 NP-완전 사례도 발견했습니다. 이 연구는 매칭 이론과 밀접한 연관을 가지며, 그래프 분할 문제의 복잡성 경계에 대한 중요한 통찰을 제공합니다.

## 핵심 내용
### 문제 정의
- 무방향 그래프를 동일한 크기의 스타 부분 그래프로 분할하는 것을 연구하며, 각 스타는 하나의 중심 정점과 여러 개의 잎 정점으로 구성됩니다.
- 이 문제는 매칭 이론과 밀접하게 관련되어 있으며, 그래프 분할 분야의 핵심 알고리즘 문제 중 하나입니다.

### 주요 결과
- **다항 시간 해결 가능 클래스**:
  - 구간 그래프(interval graphs)
  - 이분 순열 그래프(bipartite permutation graphs)
  - 기타 완전 그래프 하위 클래스
- **NP-완전 클래스**:
  - 격자 그래프(grid graphs)
  - 현 그래프(chordal graphs)
  - 세 개의 정점으로 이루어진 스타의 경우는 NP-완전으로 알려져 있음

### 방법
- 다항 시간 해결 가능 클래스에 대해서는 동적 프로그래밍과 그래프 구조적 특성을 기반으로 한 알고리즘을 설계했습니다.
- NP-완전 클래스에 대해서는 알려진 NP-완전 문제(예: 3-SAT 또는 그래프 색칠 문제)로부터의 환원을 통해 증명했습니다.

### 실험 및 결론
- 논문은 실험 데이터를 제공하지 않으며, 주요 기여는 이론적 복잡성 분류입니다.
- 결론: 완전 그래프 하위 클래스에서 이 문제의 복잡성 경계는 명확하며, 구간성(interval property)이나 순열성(permutation property)과 같은 특정 구조적 특성은 다항 시간 해결 가능성을 유도하는 반면, 격자 및 현 구조는 NP-완전성을 유도합니다.
