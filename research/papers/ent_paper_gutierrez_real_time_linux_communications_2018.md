---
$id: ent_paper_gutierrez_real_time_linux_communications_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Real-time Linux communications: an evaluation of the Linux communication stack for real-time robotic applications'
  zh: 实时 Linux 通信：面向实时机器人应用的 Linux 通信栈评估
  ko: '실시간 Linux 통신: 실시간 로봇 응용을 위한 Linux 통신 스택 평가'
summary:
  en: This 2018 paper empirically evaluates UDP round-trip latency on PREEMPT-RT Linux using multi-core ARMv7 embedded devices,
    showing that proper kernel configuration, traffic prioritization, and CPU/IRQ isolation can bound communication latency,
    while unshielded concurrent traffic disrupts determinism.
  zh: 该 2018 年论文在多核 ARMv7 嵌入式设备上对 PREEMPT-RT Linux 的 UDP 往返延迟进行了实证评估，表明适当的内核配置、流量优先级划分以及 CPU/IRQ 隔离可以约束通信延迟，而未隔离的并发流量会破坏确定性。
  ko: 이 2018년 논문은 다중 코어 ARMv7 임베디드 장치에서 PREEMPT-RT Linux의 UDP 왕복 지연을 실증적으로 평가하며, 적절한 커널 구성, 트래픽 우선순위 지정 및 CPU/IRQ 격리가 통신 지연을
    제한할 수 있으나, 격리되지 않은 동시 트래픽이 결정론성을 해친다고 보여준다.
domains:
- 08_software_middleware
- 02_components
layers:
- intelligence
- midstream
functional_roles:
- knowledge
tags:
- preempt_rt
- real_time_linux
- udp_communication
- robotic_middleware
- deterministic_networking
- low_latency
- armv7
- mqprio
- vlan_pcp
- cpu_isolation
- irq_affinity
- network_stack
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1808.10821v1.
sources:
- id: src_001
  type: paper
  title: 'Real-time Linux communications: an evaluation of the Linux communication stack for real-time robotic applications'
  url: https://arxiv.org/abs/1808.10821
  date: '2018'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---
## 概述
As robotics systems become more distributed, the communications between different robot modules play a key role for the reliability of the overall robot control. In this paper, we present a study of the Linux communication stack meant for real-time robotic applications. We evaluate the real-time performance of UDP based communications in Linux on multi-core embedded devices as test platforms. We prove that, under an appropriate configuration, the Linux kernel greatly enhances the determinism of communications using the UDP protocol. Furthermore, we demonstrate that concurrent traffic disrupts the bounded latencies and propose a solution by separating the real-time application and the corresponding interrupt in a CPU.

## 核心内容
As robotics systems become more distributed, the communications between different robot modules play a key role for the reliability of the overall robot control. In this paper, we present a study of the Linux communication stack meant for real-time robotic applications. We evaluate the real-time performance of UDP based communications in Linux on multi-core embedded devices as test platforms. We prove that, under an appropriate configuration, the Linux kernel greatly enhances the determinism of communications using the UDP protocol. Furthermore, we demonstrate that concurrent traffic disrupts the bounded latencies and propose a solution by separating the real-time application and the corresponding interrupt in a CPU.

## 参考
- http://arxiv.org/abs/1808.10821v1

