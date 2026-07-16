---
$id: ent_paper_greedy_heuristics_for_sampling_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Greedy Heuristics for Sampling-Based Motion Planning in High-Dimensional State Spaces
  zh: Greedy Heuristics for Sampling-Based Motion Planning in High-Dimensional State Spaces
  ko: Greedy Heuristics for Sampling-Based Motion Planning in High-Dimensional State Spaces
summary:
  en: 'arXiv:2405.03411v4 Announce Type: replace Abstract: Informed sampling techniques accelerate the convergence of sampling-based
    motion planners by biasing sampling toward regions of the state space that are most likely to yield better solutions.
    However, when the current solution path contains redundant or tortuous segments, the resulting informed subset may remain
    unnecessarily large, slowing convergence. Our prior work addressed this issue by introducing the greedy informed set,
    which reduces the sampling region based on the maximum heuristic cost along the current solution path. In this article,
    we formally characterize the behavior of the greedy informed set within Rapidly-exploring Random Tree (RRT*)-like planners
    and analyze how greedy sampling affects exploration and asymptotic optimality. We then present Greedy RRT* (G-RRT*), a
    bi-directional anytime variant of RRT* that leverages the greedy informed set to focus sampling in the most promising
    regions of the search space. Experiments on abstract planning benchmarks, manipulation tasks from the MotionBenchMaker
    dataset, and a dual-arm Barrett WAM problem demonstrate that G-RRT* rapidly finds initial solutions and converges asymptotically
    to optimal paths, outperforming state-of-the-art sampling-based planners.'
  zh: 'arXiv:2405.03411v4 Announce Type: replace Abstract: Informed sampling techniques accelerate the convergence of sampling-based
    motion planners by biasing sampling toward regions of the state space that are most likely to yield better solutions.
    However, when the current solution path contains redundant or tortuous segments, the resulting informed subset may remain
    unnecessarily large, slowing convergence. Our prior work addressed this issue by introducing the greedy informed set,
    which reduces the sampling region based on the maximum heuristic cost along the current solution path. In this article,
    we formally characterize the behavior of the greedy informed set within Rapidly-exploring Random Tree (RRT*)-like planners
    and analyze how greedy sampling affects exploration and asymptotic optimality. We then present Greedy RRT* (G-RRT*), a
    bi-directional anytime variant of RRT* that leverages the greedy informed set to focus sampling in the most promising
    regions of the search space. Experiments on abstract planning benchmarks, manipulation tasks from the MotionBenchMaker
    dataset, and a dual-arm Barrett WAM problem demonstrate that G-RRT* rapidly finds initial solutions and converges asymptotically
    to optimal paths, outperforming state-of-the-art sampling-based planners.'
  ko: 'arXiv:2405.03411v4 Announce Type: replace Abstract: Informed sampling techniques accelerate the convergence of sampling-based
    motion planners by biasing sampling toward regions of the state space that are most likely to yield better solutions.
    However, when the current solution path contains redundant or tortuous segments, the resulting informed subset may remain
    unnecessarily large, slowing convergence. Our prior work addressed this issue by introducing the greedy informed set,
    which reduces the sampling region based on the maximum heuristic cost along the current solution path. In this article,
    we formally characterize the behavior of the greedy informed set within Rapidly-exploring Random Tree (RRT*)-like planners
    and analyze how greedy sampling affects exploration and asymptotic optimality. We then present Greedy RRT* (G-RRT*), a
    bi-directional anytime variant of RRT* that leverages the greedy informed set to focus sampling in the most promising
    regions of the search space. Experiments on abstract planning benchmarks, manipulation tasks from the MotionBenchMaker
    dataset, and a dual-arm Barrett WAM problem demonstrate that G-RRT* rapidly finds initial solutions and converges asymptotically
    to optimal paths, outperforming state-of-the-art sampling-based planners.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- greedy_heuristics_for_sampling
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2405.03411v4.
sources:
- id: src_001
  type: paper
  title: Greedy Heuristics for Sampling-Based Motion Planning in High-Dimensional State Spaces (arXiv)
  url: https://arxiv.org/abs/2405.03411
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
Informed sampling techniques accelerate the convergence of sampling-based motion planners by biasing sampling toward regions of the state space that are most likely to yield better solutions. However, when the current solution path contains redundant or tortuous segments, the resulting informed subset may remain unnecessarily large, slowing convergence. Our prior work addressed this issue by introducing the greedy informed set, which reduces the sampling region based on the maximum heuristic cost along the current solution path. In this article, we formally characterize the behavior of the greedy informed set within Rapidly-exploring Random Tree (RRT*)-like planners and analyze how greedy sampling affects exploration and asymptotic optimality. We then present Greedy RRT* (G-RRT*), a bi-directional anytime variant of RRT* that leverages the greedy informed set to focus sampling in the most promising regions of the search space. Experiments on abstract planning benchmarks, manipulation tasks from the MotionBenchMaker dataset, and a dual-arm Barrett WAM problem demonstrate that G-RRT* rapidly finds initial solutions and converges asymptotically to optimal paths, outperforming state-of-the-art sampling-based planners.

## 核心内容
Informed sampling techniques accelerate the convergence of sampling-based motion planners by biasing sampling toward regions of the state space that are most likely to yield better solutions. However, when the current solution path contains redundant or tortuous segments, the resulting informed subset may remain unnecessarily large, slowing convergence. Our prior work addressed this issue by introducing the greedy informed set, which reduces the sampling region based on the maximum heuristic cost along the current solution path. In this article, we formally characterize the behavior of the greedy informed set within Rapidly-exploring Random Tree (RRT*)-like planners and analyze how greedy sampling affects exploration and asymptotic optimality. We then present Greedy RRT* (G-RRT*), a bi-directional anytime variant of RRT* that leverages the greedy informed set to focus sampling in the most promising regions of the search space. Experiments on abstract planning benchmarks, manipulation tasks from the MotionBenchMaker dataset, and a dual-arm Barrett WAM problem demonstrate that G-RRT* rapidly finds initial solutions and converges asymptotically to optimal paths, outperforming state-of-the-art sampling-based planners.

## 参考
- http://arxiv.org/abs/2405.03411v4

## Overview
Informed sampling techniques accelerate the convergence of sampling-based motion planners by biasing sampling toward regions of the state space that are most likely to yield better solutions. However, when the current solution path contains redundant or tortuous segments, the resulting informed subset may remain unnecessarily large, slowing convergence. Our prior work addressed this issue by introducing the greedy informed set, which reduces the sampling region based on the maximum heuristic cost along the current solution path. In this article, we formally characterize the behavior of the greedy informed set within Rapidly-exploring Random Tree (RRT*)-like planners and analyze how greedy sampling affects exploration and asymptotic optimality. We then present Greedy RRT* (G-RRT*), a bi-directional anytime variant of RRT* that leverages the greedy informed set to focus sampling in the most promising regions of the search space. Experiments on abstract planning benchmarks, manipulation tasks from the MotionBenchMaker dataset, and a dual-arm Barrett WAM problem demonstrate that G-RRT* rapidly finds initial solutions and converges asymptotically to optimal paths, outperforming state-of-the-art sampling-based planners.

## Content
Informed sampling techniques accelerate the convergence of sampling-based motion planners by biasing sampling toward regions of the state space that are most likely to yield better solutions. However, when the current solution path contains redundant or tortuous segments, the resulting informed subset may remain unnecessarily large, slowing convergence. Our prior work addressed this issue by introducing the greedy informed set, which reduces the sampling region based on the maximum heuristic cost along the current solution path. In this article, we formally characterize the behavior of the greedy informed set within Rapidly-exploring Random Tree (RRT*)-like planners and analyze how greedy sampling affects exploration and asymptotic optimality. We then present Greedy RRT* (G-RRT*), a bi-directional anytime variant of RRT* that leverages the greedy informed set to focus sampling in the most promising regions of the search space. Experiments on abstract planning benchmarks, manipulation tasks from the MotionBenchMaker dataset, and a dual-arm Barrett WAM problem demonstrate that G-RRT* rapidly finds initial solutions and converges asymptotically to optimal paths, outperforming state-of-the-art sampling-based planners.

## 개요
Informed 샘플링 기법은 상태 공간에서 더 나은 해를 도출할 가능성이 높은 영역으로 샘플링을 편향시켜 샘플 기반 모션 플래너의 수렴을 가속화합니다. 그러나 현재 해 경로에 중복되거나 구불구불한 구간이 포함된 경우, 결과적으로 생성되는 informed 부분 집합이 불필요하게 커져 수렴 속도가 느려질 수 있습니다. 이전 연구에서는 현재 해 경로를 따라 최대 휴리스틱 비용을 기준으로 샘플링 영역을 축소하는 greedy informed 집합을 도입하여 이 문제를 해결했습니다. 본 논문에서는 Rapidly-exploring Random Tree (RRT*)-유사 플래너 내에서 greedy informed 집합의 동작을 공식적으로 특성화하고, greedy 샘플링이 탐색과 점근적 최적성에 미치는 영향을 분석합니다. 그런 다음 검색 공간에서 가장 유망한 영역에 샘플링을 집중시키기 위해 greedy informed 집합을 활용하는 RRT*의 양방향 anytime 변형인 Greedy RRT* (G-RRT*)를 제시합니다. 추상적인 계획 벤치마크, MotionBenchMaker 데이터셋의 조작 작업, 그리고 이중 암 Barrett WAM 문제에 대한 실험을 통해 G-RRT*가 초기 해를 빠르게 찾고 점근적으로 최적 경로로 수렴하여 최신 샘플 기반 플래너보다 우수한 성능을 보임을 입증합니다.

## 핵심 내용
Informed 샘플링 기법은 상태 공간에서 더 나은 해를 도출할 가능성이 높은 영역으로 샘플링을 편향시켜 샘플 기반 모션 플래너의 수렴을 가속화합니다. 그러나 현재 해 경로에 중복되거나 구불구불한 구간이 포함된 경우, 결과적으로 생성되는 informed 부분 집합이 불필요하게 커져 수렴 속도가 느려질 수 있습니다. 이전 연구에서는 현재 해 경로를 따라 최대 휴리스틱 비용을 기준으로 샘플링 영역을 축소하는 greedy informed 집합을 도입하여 이 문제를 해결했습니다. 본 논문에서는 Rapidly-exploring Random Tree (RRT*)-유사 플래너 내에서 greedy informed 집합의 동작을 공식적으로 특성화하고, greedy 샘플링이 탐색과 점근적 최적성에 미치는 영향을 분석합니다. 그런 다음 검색 공간에서 가장 유망한 영역에 샘플링을 집중시키기 위해 greedy informed 집합을 활용하는 RRT*의 양방향 anytime 변형인 Greedy RRT* (G-RRT*)를 제시합니다. 추상적인 계획 벤치마크, MotionBenchMaker 데이터셋의 조작 작업, 그리고 이중 암 Barrett WAM 문제에 대한 실험을 통해 G-RRT*가 초기 해를 빠르게 찾고 점근적으로 최적 경로로 수렴하여 최신 샘플 기반 플래너보다 우수한 성능을 보임을 입증합니다.
