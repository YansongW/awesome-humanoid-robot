---
$id: ent_paper_alirezazadeh_optimal_algorithm_allocation_f_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Optimal Algorithm Allocation for Robotic Network Cloud Systems
  zh: 机器人网络云系统的最优算法分配
  ko: 로봇 네트워크 클라우드 시스템을 위한 최적 알고리즘 할당
summary:
  en: Proposes a discrete optimization method for allocating algorithms across robots, fog nodes, and cloud nodes to minimize
    both total task completion time and robot memory usage, using a semi-lattice dependency graph and branch-and-bound search.
  zh: A robotic network is a system with multiple robots connected by a communication network. Certain tasks that cannot be
    accomplished with available robotic resources are candidates for the use of cloud robotics, which overcomes the limitations
    of the robot network by adding to the network, either local or remote servers or cloud infrastructure, to aid in computational
    demanding tasks or storage. Previous studies have mainly focused on minimizing the cost of the robots in retrieving resources
    by knowing the resource allocation in advance. We develop a method for a robotic network cloud system tha
  ko: 로봇, 안개 노드, 클라우드 노드 간 알고리즘 할당을 위해 반격자 의존성 그래프와 분기한계 탐색을 사용하여 작업 총 완료 시간과 로봇 메모리 사용량을 동시에 최소화하는 이산 최적화 방법을 제안한다.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- cloud_robotics
- fog_computing
- edge_computing
- algorithm_allocation
- resource_optimization
- latency_minimization
- memory_optimization
- multi_robot_systems
- branch_and_bound
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2104.12710v5.
sources:
- id: src_001
  type: paper
  title: Optimal Algorithm Allocation for Robotic Network Cloud Systems
  url: https://arxiv.org/abs/2104.12710
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## 概述
A robotic network is a system with multiple robots connected by a communication network. Certain tasks that cannot be accomplished with available robotic resources are candidates for the use of cloud robotics, which overcomes the limitations of the robot network by adding to the network, either local or remote servers or cloud infrastructure, to aid in computational demanding tasks or storage. Previous studies have mainly focused on minimizing the cost of the robots in retrieving resources by knowing the resource allocation in advance. We develop a method for a robotic network cloud system that includes robots, fog and cloud nodes, to determine where each algorithm should be allocated so that the system achieves optimal performance, regardless of which robot initiates the request. We can find the minimum required memory for the robots and the optimal way to allocate the algorithms with the shortest time to complete each task. We experimentally compare our method with a state-of-the-art method, using real-world data, showing the improvements that can be obtained.

## 核心内容
A robotic network is a system with multiple robots connected by a communication network. Certain tasks that cannot be accomplished with available robotic resources are candidates for the use of cloud robotics, which overcomes the limitations of the robot network by adding to the network, either local or remote servers or cloud infrastructure, to aid in computational demanding tasks or storage. Previous studies have mainly focused on minimizing the cost of the robots in retrieving resources by knowing the resource allocation in advance. We develop a method for a robotic network cloud system that includes robots, fog and cloud nodes, to determine where each algorithm should be allocated so that the system achieves optimal performance, regardless of which robot initiates the request. We can find the minimum required memory for the robots and the optimal way to allocate the algorithms with the shortest time to complete each task. We experimentally compare our method with a state-of-the-art method, using real-world data, showing the improvements that can be obtained.

## 参考
- http://arxiv.org/abs/2104.12710v5


