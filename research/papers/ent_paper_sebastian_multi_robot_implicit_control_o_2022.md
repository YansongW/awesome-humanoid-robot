---
$id: ent_paper_sebastian_multi_robot_implicit_control_o_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Multi-robot Implicit Control of Massive Herds
  zh: 大规模集群的多机器人隐式控制
  ko: 대규모 군집의 다중 로봇 암묵적 제어
summary:
  en: This paper proposes a multi-robot herding method that combines Implicit Control with a dynamic assignment strategy based
    on convex-hull clustering to steer large numbers of evaders toward a desired reference using only a few herders.
  zh: 本文提出了一种多机器人放牧方法，将隐式控制与基于凸包聚类的动态分配策略相结合，利用少量放牧机器人将大量逃逸者驱赶至期望轨迹。
  ko: 본 논문은 음영 제어와 볼록 껍질 군집에 기반한 동적 할당 전략을 결합하여 소수의 로봇으로 대량의 도망자를 원하는 궤적으로 유도하는 다중 로봇 군집 제어 방법을 제시한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- multi_robot_herding
- implicit_control
- dynamic_assignment
- convex_hull_clustering
- evader_herding
- voronoi_tessellation
- k_means_clustering
- multi_agent_coordination
- input_nonaffine_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2209.09705v1.
sources:
- id: src_001
  type: paper
  title: Multi-robot Implicit Control of Massive Herds
  url: https://arxiv.org/abs/2209.09705
  date: '2022'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
This paper solves the problem of herding countless evaders by means of a few robots. The objective is to steer all the evaders towards a desired tracking reference while avoiding escapes. The problem is very challenging due to the highly complex repulsive evaders' dynamics and the underdetermined states to control. We propose a solution that is based on Implicit Control and a novel dynamic assignment strategy to select the evaders to be directly controlled. The former is a general technique that explicitly computes control inputs even in highly complex input-nonaffine dynamics. The latter is built upon a convex-hull dynamic clustering inspired by the Voronoi tessellation problem. The combination of both allows to choose the best evaders to directly control, while the others are indirectly controlled by exploiting the repulsive interactions among them. Simulations show that massive herds can be herd throughout complex patterns by means of a few herders.

## 核心内容
This paper solves the problem of herding countless evaders by means of a few robots. The objective is to steer all the evaders towards a desired tracking reference while avoiding escapes. The problem is very challenging due to the highly complex repulsive evaders' dynamics and the underdetermined states to control. We propose a solution that is based on Implicit Control and a novel dynamic assignment strategy to select the evaders to be directly controlled. The former is a general technique that explicitly computes control inputs even in highly complex input-nonaffine dynamics. The latter is built upon a convex-hull dynamic clustering inspired by the Voronoi tessellation problem. The combination of both allows to choose the best evaders to directly control, while the others are indirectly controlled by exploiting the repulsive interactions among them. Simulations show that massive herds can be herd throughout complex patterns by means of a few herders.

## 参考
- http://arxiv.org/abs/2209.09705v1

