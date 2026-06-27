---
$id: ent_paper_gao_real_time_service_subscription_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Real-Time Service Subscription and Adaptive Offloading Control in Vehicular
    Edge Computing
  zh: 车联网边缘计算中的实时服务订阅与自适应卸载控制
  ko: 차량 에지 컴퓨팅에서의 실시간 서비스 구독 및 적응형 오프로딩 제어
summary:
  en: This paper formulates the Deadline-Constrained Task Offloading and Resource
    Allocation Problem (DOAP) in Vehicular Edge Computing and proposes SARound, a
    1/4-approximation algorithm using LP rounding and local-ratio techniques, together
    with an online service-subscription and offloading-control framework evaluated
    in the OMNeT++/Simu5G-based VecSim simulator.
  zh: 本文针对车联网边缘计算提出了带截止时间约束的任务卸载与资源分配问题（DOAP），并设计了基于线性规划舍入和局部比率技术的 1/4 近似算法 SARound，以及在线服务订阅与卸载控制框架，并在基于
    OMNeT++/Simu5G 的 VecSim 仿真器中进行了验证。
  ko: 본 논문은 차량 에지 컴퓨팅에서 마감 시간 제약이 있는 작업 오프로딩 및 자원 할당 문제(DOAP)를 공식화하고, LP 라운딩과 국소 비율
    기법을 사용하는 1/4 근사 알고리즘 SARound와 온라인 서비스 구독 및 오프로딩 제어 프레임워크를 제안하며, OMNeT++/Simu5G
    기반 VecSim 시뮬레이터에서 평가한다.
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
- edge_computing
- vehicular_edge_computing
- task_offloading
- resource_allocation
- real_time_scheduling
- approximation_algorithm
- lp_rounding
- service_subscription
- 5g_networking
- humanoid_fleet_orchestration
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the supplied metadata/abstract. Full-text review is needed
    to confirm section-level citations and exact experimental claims.
sources:
- id: src_001
  type: paper
  title: Real-Time Service Subscription and Adaptive Offloading Control in Vehicular
    Edge Computing
  url: https://arxiv.org/abs/2512.14002
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

The paper addresses real-time computation offloading in Vehicular Edge Computing (VEC), where vehicles wirelessly offload compute-intensive tasks to Roadside Units (RSUs). It formulates the Deadline-Constrained Task Offloading and Resource Allocation Problem (DOAP) with bandwidth and computational-resource constraints, aiming to maximize total vehicle utility. To solve DOAP, the authors propose SARound, an approximation algorithm that combines Linear Program rounding with local-ratio techniques and improves the best-known approximation ratio from 1/6 to 1/4 while preserving runtime efficiency. Complementing the offline algorithm, the paper designs an online service-subscription and offloading-control framework that adapts to short task deadlines and rapidly changing wireless channel quality.

The proposed framework is implemented and evaluated in VecSim, a custom VEC simulator built on OMNeT++ and Simu5G. VecSim manages the full life-cycle of real-time vehicular tasks, integrating 5G networking, mobility, and compute-resource scheduling. Experiments use profiled object-detection workloads and the Shanghai Qiangsheng Taxi GPS trace, comparing SARound against Greedy, Iterative, Game, and IDAssign baselines. The results show that SARound consistently outperforms these baselines across varying network conditions while remaining computationally efficient.

## Key Contributions

- Formulates the Deadline-Constrained Task Offloading and Resource Allocation Problem (DOAP) in VEC with bandwidth and computational-resource constraints.
- Proposes SARound, an LP-rounding and local-ratio-based 1/4-approximation algorithm for DOAP, improving the prior best-known approximation ratio from 1/6 to 1/4.
- Designs an online service-subscription and offloading-control framework that handles short deadlines and dynamic wireless channel quality.
- Develops VecSim, a VEC simulator based on OMNeT++ and Simu5G, integrating 5G networking, mobility, and full task life-cycle management.
- Experimentally validates SARound using profiled object-detection applications and real-world Shanghai taxi GPS traces, outperforming Greedy, Iterative, Game, and IDAssign baselines.

## Relevance to Humanoid Robotics

Although the paper focuses on vehicular scenarios, it explicitly identifies robots and UAVs as energy-constrained mobile platforms that can benefit from deadline-aware edge offloading. The techniques for adaptive real-time service subscription, dynamic bandwidth and compute allocation, and online offloading control are directly transferable to orchestrating computation and communication in deployed humanoid robot fleets. In particular, humanoid robots operating in the field with limited onboard battery and compute can use similar VEC-style offloading to meet latency-sensitive perception and planning deadlines while balancing wireless link quality.
