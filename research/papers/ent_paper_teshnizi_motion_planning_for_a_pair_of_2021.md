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
  en: Proposes a reduced-visibility-graph A* planning algorithm for two planar point robots connected by a finite-length cable,
    proving that an optimal solution can always be found on the reduced visibility graph and reducing trajectory existence
    to path search.
  zh: 针对由有限长度电缆连接的两个平面点机器人，提出了一种基于精简可视图的 A* 规划算法，并证明了最优解总能在精简可视图上找到，将轨迹存在性问题简化为路径搜索。
  ko: 유한 길이 케이블로 연결된 두 평면 점 로봇을 위해 축소 가시성 그래프 기반 A* 계획 알고리즘을 제안하고, 최적 해가 항상 축소 가시성 그래프 상에서 찾아질 수 있음을 증명하여 궤적 존재 문제를 경로 탐색으로
    환원한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2102.13212v1.
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
## 概述
Considering an environment containing polygonal obstacles, we address the problem of planning motions for a pair of planar robots connected to one another via a cable of limited length. Much like prior problems with a single robot connected via a cable to a fixed base, straight line-of-sight visibility plays an important role. The present paper shows how the reduced visibility graph provides a natural discretization and captures the essential topological considerations very effectively for the two robot case as well. Unlike the single robot case, however, the bounded cable length introduces considerations around coordination (or equivalently, when viewed from the point of view of a centralized planner, relative timing) that complicates the matter. Indeed, the paper has to introduce a rather more involved formalization than prior single-robot work in order to establish the core theoretical result -- a theorem permitting the problem to be cast as one of finding paths rather than trajectories. Once affirmed, the planning problem reduces to a straightforward graph search with an elegant representation of the connecting cable, demanding only a few extra ancillary checks that ensure sufficiency of cable to guarantee feasibility of the solution. We describe our implementation of A${}^\star$ search, and report experimental results. Lastly, we prescribe an optimal execution for the solutions provided by the algorithm.

## 核心内容
Considering an environment containing polygonal obstacles, we address the problem of planning motions for a pair of planar robots connected to one another via a cable of limited length. Much like prior problems with a single robot connected via a cable to a fixed base, straight line-of-sight visibility plays an important role. The present paper shows how the reduced visibility graph provides a natural discretization and captures the essential topological considerations very effectively for the two robot case as well. Unlike the single robot case, however, the bounded cable length introduces considerations around coordination (or equivalently, when viewed from the point of view of a centralized planner, relative timing) that complicates the matter. Indeed, the paper has to introduce a rather more involved formalization than prior single-robot work in order to establish the core theoretical result -- a theorem permitting the problem to be cast as one of finding paths rather than trajectories. Once affirmed, the planning problem reduces to a straightforward graph search with an elegant representation of the connecting cable, demanding only a few extra ancillary checks that ensure sufficiency of cable to guarantee feasibility of the solution. We describe our implementation of A${}^\star$ search, and report experimental results. Lastly, we prescribe an optimal execution for the solutions provided by the algorithm.

## 参考
- http://arxiv.org/abs/2102.13212v1

