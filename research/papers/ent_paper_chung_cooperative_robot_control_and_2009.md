---
$id: ent_paper_chung_cooperative_robot_control_and_2009
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Cooperative Robot Control and Concurrent Synchronization of Lagrangian Systems
  zh: 拉格朗日系统的协同机器人控制与并发同步
  ko: 라그랑주 시스템의 협동 로봇 제어 및 병행 동기화
summary:
  en: Chung and Slotine (2009) derive a decentralized tracking control law that globally exponentially synchronizes networks
    of Lagrangian robots using diffusive local couplings, and extend it to adaptive synchronization, partial-state coupling,
    and time-delayed communication.
  zh: Chung与Slotine（2009）提出了一种分散式跟踪控制律，利用扩散式局部耦合实现拉格朗日机器人网络的全局指数同步，并将其扩展到自适应同步、部分状态耦合和时延通信。
  ko: Chung과 Slotine(2009)은 확산적 국부 결합을 사용하여 라그랑주 로봇 네트워크의 전역 지수 동기화를 달성하는 분산 추적 제어법을 도출하고, 이를 적응 동기화, 부분 상태 결합 및 지연 통신으로 확장한다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- concurrent_synchronization
- decentralized_control
- lagrangian_systems
- contraction_analysis
- cooperative_robot_control
- multi_robot_synchronization
- diffusive_coupling
- tracking_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/0711.1709v4.
sources:
- id: src_001
  type: paper
  title: Cooperative Robot Control and Concurrent Synchronization of Lagrangian Systems
  url: https://arxiv.org/abs/0711.1709
  date: '2009'
  accessed_at: '2026-06-28'
  doi: 10.1109/TRO.2009.2014125
theoretical_depth:
- method
---
## 概述
Concurrent synchronization is a regime where diverse groups of fully synchronized dynamic systems stably coexist. We study global exponential synchronization and concurrent synchronization in the context of Lagrangian systems control. In a network constructed by adding diffusive couplings to robot manipulators or mobile robots, a decentralized tracking control law globally exponentially synchronizes an arbitrary number of robots, and represents a generalization of the average consensus problem. Exact nonlinear stability guarantees and synchronization conditions are derived by contraction analysis. The proposed decentralized strategy is further extended to adaptive synchronization and partial-state coupling.

## 核心内容
Concurrent synchronization is a regime where diverse groups of fully synchronized dynamic systems stably coexist. We study global exponential synchronization and concurrent synchronization in the context of Lagrangian systems control. In a network constructed by adding diffusive couplings to robot manipulators or mobile robots, a decentralized tracking control law globally exponentially synchronizes an arbitrary number of robots, and represents a generalization of the average consensus problem. Exact nonlinear stability guarantees and synchronization conditions are derived by contraction analysis. The proposed decentralized strategy is further extended to adaptive synchronization and partial-state coupling.

## 参考
- http://arxiv.org/abs/0711.1709v4

