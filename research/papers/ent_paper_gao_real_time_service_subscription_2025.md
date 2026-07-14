---
$id: ent_paper_gao_real_time_service_subscription_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Real-Time Service Subscription and Adaptive Offloading Control in Vehicular Edge Computing
  zh: 车联网边缘计算中的实时服务订阅与自适应卸载控制
  ko: 차량 에지 컴퓨팅에서의 실시간 서비스 구독 및 적응형 오프로딩 제어
summary:
  en: This paper formulates the Deadline-Constrained Task Offloading and Resource Allocation Problem (DOAP) in Vehicular Edge
    Computing and proposes SARound, a 1/4-approximation algorithm using LP rounding and local-ratio techniques, together with
    an online service-subscription and offloading-control framework evaluated in the OMNeT++/Simu5G-based VecSim simulator.
  zh: 本文针对车联网边缘计算提出了带截止时间约束的任务卸载与资源分配问题（DOAP），并设计了基于线性规划舍入和局部比率技术的 1/4 近似算法 SARound，以及在线服务订阅与卸载控制框架，并在基于 OMNeT++/Simu5G 的
    VecSim 仿真器中进行了验证。
  ko: 본 논문은 차량 에지 컴퓨팅에서 마감 시간 제약이 있는 작업 오프로딩 및 자원 할당 문제(DOAP)를 공식화하고, LP 라운딩과 국소 비율 기법을 사용하는 1/4 근사 알고리즘 SARound와 온라인 서비스
    구독 및 오프로딩 제어 프레임워크를 제안하며, OMNeT++/Simu5G 기반 VecSim 시뮬레이터에서 평가한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.14002v1.
sources:
- id: src_001
  type: paper
  title: Real-Time Service Subscription and Adaptive Offloading Control in Vehicular Edge Computing
  url: https://arxiv.org/abs/2512.14002
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
Vehicular Edge Computing (VEC) has emerged as a promising paradigm for enhancing the computational efficiency and service quality in intelligent transportation systems by enabling vehicles to wirelessly offload computation-intensive tasks to nearby Roadside Units. However, efficient task offloading and resource allocation for time-critical applications in VEC remain challenging due to constrained network bandwidth and computational resources, stringent task deadlines, and rapidly changing network conditions. To address these challenges, we formulate a Deadline-Constrained Task Offloading and Resource Allocation Problem (DOAP), denoted as $\mathbf{P}$, in VEC with both bandwidth and computational resource constraints, aiming to maximize the total vehicle utility. To solve $\mathbf{P}$, we propose $\mathtt{SARound}$, an approximation algorithm based on Linear Program rounding and local-ratio techniques, that improves the best-known approximation ratio for DOAP from $\frac{1}{6}$ to $\frac{1}{4}$. Additionally, we design an online service subscription and offloading control framework to address the challenges of short task deadlines and rapidly changing wireless network conditions. To validate our approach, we develop a comprehensive VEC simulator, VecSim, using the open-source simulation libraries OMNeT++ and Simu5G. VecSim integrates our designed framework to manage the full life-cycle of real-time vehicular tasks. Experimental results, based on profiled object detection applications and real-world taxi trace data, show that $\mathtt{SARound}$ consistently outperforms state-of-the-art baselines under varying network conditions while maintaining runtime efficiency.

## 核心内容
Vehicular Edge Computing (VEC) has emerged as a promising paradigm for enhancing the computational efficiency and service quality in intelligent transportation systems by enabling vehicles to wirelessly offload computation-intensive tasks to nearby Roadside Units. However, efficient task offloading and resource allocation for time-critical applications in VEC remain challenging due to constrained network bandwidth and computational resources, stringent task deadlines, and rapidly changing network conditions. To address these challenges, we formulate a Deadline-Constrained Task Offloading and Resource Allocation Problem (DOAP), denoted as $\mathbf{P}$, in VEC with both bandwidth and computational resource constraints, aiming to maximize the total vehicle utility. To solve $\mathbf{P}$, we propose $\mathtt{SARound}$, an approximation algorithm based on Linear Program rounding and local-ratio techniques, that improves the best-known approximation ratio for DOAP from $\frac{1}{6}$ to $\frac{1}{4}$. Additionally, we design an online service subscription and offloading control framework to address the challenges of short task deadlines and rapidly changing wireless network conditions. To validate our approach, we develop a comprehensive VEC simulator, VecSim, using the open-source simulation libraries OMNeT++ and Simu5G. VecSim integrates our designed framework to manage the full life-cycle of real-time vehicular tasks. Experimental results, based on profiled object detection applications and real-world taxi trace data, show that $\mathtt{SARound}$ consistently outperforms state-of-the-art baselines under varying network conditions while maintaining runtime efficiency.

## 参考
- http://arxiv.org/abs/2512.14002v1

