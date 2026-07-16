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

## Overview
A robotic network is a system with multiple robots connected by a communication network. Certain tasks that cannot be accomplished with available robotic resources are candidates for the use of cloud robotics, which overcomes the limitations of the robot network by adding to the network, either local or remote servers or cloud infrastructure, to aid in computational demanding tasks or storage. Previous studies have mainly focused on minimizing the cost of the robots in retrieving resources by knowing the resource allocation in advance. We develop a method for a robotic network cloud system that includes robots, fog and cloud nodes, to determine where each algorithm should be allocated so that the system achieves optimal performance, regardless of which robot initiates the request. We can find the minimum required memory for the robots and the optimal way to allocate the algorithms with the shortest time to complete each task. We experimentally compare our method with a state-of-the-art method, using real-world data, showing the improvements that can be obtained.

## Content
A robotic network is a system with multiple robots connected by a communication network. Certain tasks that cannot be accomplished with available robotic resources are candidates for the use of cloud robotics, which overcomes the limitations of the robot network by adding to the network, either local or remote servers or cloud infrastructure, to aid in computational demanding tasks or storage. Previous studies have mainly focused on minimizing the cost of the robots in retrieving resources by knowing the resource allocation in advance. We develop a method for a robotic network cloud system that includes robots, fog and cloud nodes, to determine where each algorithm should be allocated so that the system achieves optimal performance, regardless of which robot initiates the request. We can find the minimum required memory for the robots and the optimal way to allocate the algorithms with the shortest time to complete each task. We experimentally compare our method with a state-of-the-art method, using real-world data, showing the improvements that can be obtained.

## 개요
로봇 네트워크는 통신 네트워크로 연결된 여러 로봇으로 구성된 시스템입니다. 가용 로봇 자원만으로는 수행할 수 없는 특정 작업은 클라우드 로보틱스의 활용 대상이 되며, 이는 로컬 또는 원격 서버나 클라우드 인프라를 네트워크에 추가하여 계산 집약적 작업이나 저장을 지원함으로써 로봇 네트워크의 한계를 극복합니다. 기존 연구는 주로 자원 할당을 사전에 파악하여 로봇이 자원을 검색하는 비용을 최소화하는 데 초점을 맞추었습니다. 우리는 로봇, 포그(fog) 및 클라우드 노드를 포함하는 로봇 네트워크 클라우드 시스템을 위한 방법을 개발하여, 어떤 로봇이 요청을 시작하든 시스템이 최적의 성능을 달성할 수 있도록 각 알고리즘을 할당할 위치를 결정합니다. 로봇에 필요한 최소 메모리와 각 작업을 완료하는 최단 시간으로 알고리즘을 할당하는 최적의 방법을 찾을 수 있습니다. 실제 데이터를 사용하여 최신 방법과 실험적으로 비교함으로써 얻을 수 있는 개선 사항을 보여줍니다.

## 핵심 내용
로봇 네트워크는 통신 네트워크로 연결된 여러 로봇으로 구성된 시스템입니다. 가용 로봇 자원만으로는 수행할 수 없는 특정 작업은 클라우드 로보틱스의 활용 대상이 되며, 이는 로컬 또는 원격 서버나 클라우드 인프라를 네트워크에 추가하여 계산 집약적 작업이나 저장을 지원함으로써 로봇 네트워크의 한계를 극복합니다. 기존 연구는 주로 자원 할당을 사전에 파악하여 로봇이 자원을 검색하는 비용을 최소화하는 데 초점을 맞추었습니다. 우리는 로봇, 포그(fog) 및 클라우드 노드를 포함하는 로봇 네트워크 클라우드 시스템을 위한 방법을 개발하여, 어떤 로봇이 요청을 시작하든 시스템이 최적의 성능을 달성할 수 있도록 각 알고리즘을 할당할 위치를 결정합니다. 로봇에 필요한 최소 메모리와 각 작업을 완료하는 최단 시간으로 알고리즘을 할당하는 최적의 방법을 찾을 수 있습니다. 실제 데이터를 사용하여 최신 방법과 실험적으로 비교함으로써 얻을 수 있는 개선 사항을 보여줍니다.
