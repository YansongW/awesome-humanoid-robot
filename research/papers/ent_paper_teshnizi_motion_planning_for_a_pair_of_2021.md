---
$id: ent_paper_teshnizi_motion_planning_for_a_pair_of_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Motion Planning for a Pair of Tethered Robots
  zh: 一对系留机器人的运动规划
  ko: 테더링된 두 로봇의 동작 계획
summary:
  en: Proposes a reduced-visibility-graph A* planning algorithm for two planar point
    robots connected by a finite-length cable, proving that an optimal solution can
    always be found on the reduced visibility graph and reducing trajectory existence
    to path search.
  zh: 针对由有限长度电缆连接的两个平面点机器人，提出了一种基于精简可视图的 A* 规划算法，并证明了最优解总能在精简可视图上找到，将轨迹存在性问题简化为路径搜索。
  ko: 유한 길이 케이블로 연결된 두 평면 점 로봇을 위해 축소 가시성 그래프 기반 A* 계획 알고리즘을 제안하고, 최적 해가 항상 축소 가시성
    그래프 상에서 찾아질 수 있음을 증명하여 궤적 존재 문제를 경로 탐색으로 환원한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- tethered_robots
- motion_planning
- multi_robot_coordination
- visibility_graph
- a_star
- cable_constrained_planning
- homotopy
- trajectory_planning
- extreme_terrain_robotics
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from arXiv full text; factual claims were checked against the
    PDF, but the paper is an arXiv preprint and human review is required before full
    verification.
sources:
- id: src_001
  type: paper
  title: Motion Planning for a Pair of Tethered Robots
  url: https://arxiv.org/abs/2102.13212
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper studies the tethered robot pair motion planning problem (trpmpp): given a planar workspace with polygonal obstacles and two point robots connected by a cable of bounded length, find paths from given initial positions to goal positions such that the cable length constraint is never violated. The authors show that the reduced visibility graph (RVG) is sufficient as a discrete representation: any feasible solution can be replaced by a pair of shortest paths in their respective homotopy classes that lie on RVG edges. They formalize this through a tightening operator, a concatenation operator that joins robot paths with a cable configuration, and a quantity C* that measures the minimum cable length needed to execute two paths under a fixed homotopy class. With these tools, Theorem 2 proves that if a solution exists, an RVG-based solution also exists, allowing the planner to search over paths rather than full trajectories.

The planning algorithm is an A* search over a tree of cable configurations. Each node stores a taut cable as a deque of RVG vertices, the distances traveled by each robot, and a parent pointer. Transitions correspond to both robots moving along visibility edges, which modifies the cable deque by pushing or popping vertices at the appropriate ends. Because Lemma 2 establishes that cable consumption is a convex function when shortest paths are traversed with a common curve parameter, feasibility only needs to be checked at the endpoints of a path pair. Theorems 3 and 4 establish soundness and completeness of this algorithm. Finally, the paper prescribes a time-optimal execution: both robots move at maximum speed for a duration equal to the longer of their two travel times, and the trajectories constructed in this way are guaranteed to respect the cable bound.

## Key Contributions

- Theorem 2: a feasible trpmpp solution can always be found within the reduced visibility graph, reducing trajectory existence to path finding.
- A tree-of-cable-configurations representation using a deque of RVG vertices, searched with A* to find distance-optimal solutions.
- Lemma 2 and its convexity proof: shortest-path motions yield convex cable consumption, so cable-length checks are needed only at path endpoints.
- A time-optimal execution prescription (Equations (y) and (z)) that converts RVG paths into feasible, maximum-speed trajectories.
- Experimental comparison showing the A* formulation expands fewer nodes and runs faster than a prior dynamic-programming approach on a shared test scenario.

## Relevance to Humanoid Robotics

Although the paper uses planar point robots, its core concern—coordinated motion under a shared finite-length tether—is directly relevant to humanoid deployment in constrained or hazardous environments. Tethers are commonly used with humanoid and legged systems for power delivery, communication, fall protection, or emergency retrieval in industrial inspection, search-and-rescue, and extreme-terrain operations. The homotopy-aware cable representation and the convexity-based feasibility check provide algorithmic building blocks that can be adapted to higher-dimensional planners for tethered humanoid teams, particularly where line-of-sight and cable management dominate safety and feasibility.
