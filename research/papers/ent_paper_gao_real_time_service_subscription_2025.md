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

## Overview
Vehicular Edge Computing (VEC) has emerged as a promising paradigm for enhancing the computational efficiency and service quality in intelligent transportation systems by enabling vehicles to wirelessly offload computation-intensive tasks to nearby Roadside Units. However, efficient task offloading and resource allocation for time-critical applications in VEC remain challenging due to constrained network bandwidth and computational resources, stringent task deadlines, and rapidly changing network conditions. To address these challenges, we formulate a Deadline-Constrained Task Offloading and Resource Allocation Problem (DOAP), denoted as $\mathbf{P}$, in VEC with both bandwidth and computational resource constraints, aiming to maximize the total vehicle utility. To solve $\mathbf{P}$, we propose $\mathtt{SARound}$, an approximation algorithm based on Linear Program rounding and local-ratio techniques, that improves the best-known approximation ratio for DOAP from $\frac{1}{6}$ to $\frac{1}{4}$. Additionally, we design an online service subscription and offloading control framework to address the challenges of short task deadlines and rapidly changing wireless network conditions. To validate our approach, we develop a comprehensive VEC simulator, VecSim, using the open-source simulation libraries OMNeT++ and Simu5G. VecSim integrates our designed framework to manage the full life-cycle of real-time vehicular tasks. Experimental results, based on profiled object detection applications and real-world taxi trace data, show that $\mathtt{SARound}$ consistently outperforms state-of-the-art baselines under varying network conditions while maintaining runtime efficiency.

## Content
Vehicular Edge Computing (VEC) has emerged as a promising paradigm for enhancing the computational efficiency and service quality in intelligent transportation systems by enabling vehicles to wirelessly offload computation-intensive tasks to nearby Roadside Units. However, efficient task offloading and resource allocation for time-critical applications in VEC remain challenging due to constrained network bandwidth and computational resources, stringent task deadlines, and rapidly changing network conditions. To address these challenges, we formulate a Deadline-Constrained Task Offloading and Resource Allocation Problem (DOAP), denoted as $\mathbf{P}$, in VEC with both bandwidth and computational resource constraints, aiming to maximize the total vehicle utility. To solve $\mathbf{P}$, we propose $\mathtt{SARound}$, an approximation algorithm based on Linear Program rounding and local-ratio techniques, that improves the best-known approximation ratio for DOAP from $\frac{1}{6}$ to $\frac{1}{4}$. Additionally, we design an online service subscription and offloading control framework to address the challenges of short task deadlines and rapidly changing wireless network conditions. To validate our approach, we develop a comprehensive VEC simulator, VecSim, using the open-source simulation libraries OMNeT++ and Simu5G. VecSim integrates our designed framework to manage the full life-cycle of real-time vehicular tasks. Experimental results, based on profiled object detection applications and real-world taxi trace data, show that $\mathtt{SARound}$ consistently outperforms state-of-the-art baselines under varying network conditions while maintaining runtime efficiency.

## 개요
Vehicular Edge Computing(VEC)은 차량이 무선으로 계산 집약적 작업을 인근 도로변 유닛(Roadside Units)에 오프로드할 수 있게 함으로써 지능형 교통 시스템의 계산 효율성과 서비스 품질을 향상시키는 유망한 패러다임으로 부상했습니다. 그러나 VEC에서 시간에 민감한 애플리케이션을 위한 효율적인 작업 오프로드 및 자원 할당은 제한된 네트워크 대역폭과 계산 자원, 엄격한 작업 마감 시간, 그리고 빠르게 변화하는 네트워크 조건으로 인해 여전히 어려운 과제로 남아 있습니다. 이러한 문제를 해결하기 위해, 우리는 대역폭과 계산 자원 제약이 있는 VEC에서 총 차량 효용을 최대화하는 것을 목표로 하는 마감 시간 제약 작업 오프로드 및 자원 할당 문제(DOAP)를 $\mathbf{P}$로 표기하여 정식화합니다. $\mathbf{P}$를 해결하기 위해, 우리는 선형 계획법 라운딩(Linear Program rounding)과 국소 비율(local-ratio) 기법에 기반한 근사 알고리즘인 $\mathtt{SARound}$를 제안하며, 이는 DOAP에 대한 기존 최고 근사 비율을 $\frac{1}{6}$에서 $\frac{1}{4}$로 개선합니다. 또한, 짧은 작업 마감 시간과 빠르게 변화하는 무선 네트워크 조건의 문제를 해결하기 위해 온라인 서비스 구독 및 오프로드 제어 프레임워크를 설계합니다. 접근 방식을 검증하기 위해, 우리는 오픈소스 시뮬레이션 라이브러리인 OMNeT++와 Simu5G를 사용하여 포괄적인 VEC 시뮬레이터인 VecSim을 개발합니다. VecSim은 실시간 차량 작업의 전체 수명 주기를 관리하기 위해 설계된 프레임워크를 통합합니다. 프로파일링된 객체 탐지 애플리케이션과 실제 택시 궤적 데이터를 기반으로 한 실험 결과는 $\mathtt{SARound}$가 다양한 네트워크 조건에서 최신 기준선을 일관되게 능가하면서도 런타임 효율성을 유지함을 보여줍니다.

## 핵심 내용
Vehicular Edge Computing(VEC)은 차량이 무선으로 계산 집약적 작업을 인근 도로변 유닛(Roadside Units)에 오프로드할 수 있게 함으로써 지능형 교통 시스템의 계산 효율성과 서비스 품질을 향상시키는 유망한 패러다임으로 부상했습니다. 그러나 VEC에서 시간에 민감한 애플리케이션을 위한 효율적인 작업 오프로드 및 자원 할당은 제한된 네트워크 대역폭과 계산 자원, 엄격한 작업 마감 시간, 그리고 빠르게 변화하는 네트워크 조건으로 인해 여전히 어려운 과제로 남아 있습니다. 이러한 문제를 해결하기 위해, 우리는 대역폭과 계산 자원 제약이 있는 VEC에서 총 차량 효용을 최대화하는 것을 목표로 하는 마감 시간 제약 작업 오프로드 및 자원 할당 문제(DOAP)를 $\mathbf{P}$로 표기하여 정식화합니다. $\mathbf{P}$를 해결하기 위해, 우리는 선형 계획법 라운딩(Linear Program rounding)과 국소 비율(local-ratio) 기법에 기반한 근사 알고리즘인 $\mathtt{SARound}$를 제안하며, 이는 DOAP에 대한 기존 최고 근사 비율을 $\frac{1}{6}$에서 $\frac{1}{4}$로 개선합니다. 또한, 짧은 작업 마감 시간과 빠르게 변화하는 무선 네트워크 조건의 문제를 해결하기 위해 온라인 서비스 구독 및 오프로드 제어 프레임워크를 설계합니다. 접근 방식을 검증하기 위해, 우리는 오픈소스 시뮬레이션 라이브러리인 OMNeT++와 Simu5G를 사용하여 포괄적인 VEC 시뮬레이터인 VecSim을 개발합니다. VecSim은 실시간 차량 작업의 전체 수명 주기를 관리하기 위해 설계된 프레임워크를 통합합니다. 프로파일링된 객체 탐지 애플리케이션과 실제 택시 궤적 데이터를 기반으로 한 실험 결과는 $\mathtt{SARound}$가 다양한 네트워크 조건에서 최신 기준선을 일관되게 능가하면서도 런타임 효율성을 유지함을 보여줍니다.
