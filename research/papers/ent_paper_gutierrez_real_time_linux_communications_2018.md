---
$id: ent_paper_gutierrez_real_time_linux_communications_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Real-time Linux communications: an evaluation of the Linux communication stack
    for real-time robotic applications'
  zh: 实时 Linux 通信：面向实时机器人应用的 Linux 通信栈评估
  ko: '실시간 Linux 통신: 실시간 로봇 응용을 위한 Linux 통신 스택 평가'
summary:
  en: This 2018 paper empirically evaluates UDP round-trip latency on PREEMPT-RT Linux
    using multi-core ARMv7 embedded devices, showing that proper kernel configuration,
    traffic prioritization, and CPU/IRQ isolation can bound communication latency,
    while unshielded concurrent traffic disrupts determinism.
  zh: 该 2018 年论文在多核 ARMv7 嵌入式设备上对 PREEMPT-RT Linux 的 UDP 往返延迟进行了实证评估，表明适当的内核配置、流量优先级划分以及
    CPU/IRQ 隔离可以约束通信延迟，而未隔离的并发流量会破坏确定性。
  ko: 이 2018년 논문은 다중 코어 ARMv7 임베디드 장치에서 PREEMPT-RT Linux의 UDP 왕복 지연을 실증적으로 평가하며, 적절한
    커널 구성, 트래픽 우선순위 지정 및 CPU/IRQ 격리가 통신 지연을 제한할 수 있으나, 격리되지 않은 동시 트래픽이 결정론성을 해친다고
    보여준다.
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
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: AI-extracted from arXiv abstract and full PDF; factual claims match the paper
    text, but human review is required before marking verified.
sources:
- id: src_001
  type: paper
  title: 'Real-time Linux communications: an evaluation of the Linux communication
    stack for real-time robotic applications'
  url: https://arxiv.org/abs/1808.10821
  date: '2018'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---

## Overview

This paper presents an empirical study of UDP-based real-time communication over the standard Linux network stack on multi-core embedded ARMv7 hardware. The authors configure Linux kernel 4.9.30 with the PREEMPT-RT rt21 patch and apply real-time priorities, memory locking, CPU affinity, and interrupt isolation to evaluate whether bounded latencies can be achieved without a custom network stack. They measure round-trip time with a modified cyclictest client/server pair under idle, stress, and concurrent-traffic conditions.

The core finding is that, under appropriate configuration, PREEMPT-RT Linux can deliver bounded UDP round-trip latencies. However, simply using a real-time kernel is insufficient when concurrent background traffic is present. The authors show that separating the real-time application and its associated network interrupt onto a dedicated CPU substantially reduces latency spikes and missed deadlines. They also configure Linux Traffic Control using the MQPRIO qdisc and VLAN Priority Code Point (PCP) marking to map real-time traffic onto dedicated hardware transmit queues.

## Key Contributions

- Demonstrates that PREEMPT-RT Linux can achieve bounded UDP round-trip latencies on ARMv7 embedded hardware when properly configured.
- Shows that concurrent traffic disrupts bounded latencies unless the real-time application and its network interrupt are isolated on a dedicated CPU.
- Evaluates Linux Traffic Control (MQPRIO qdisc) combined with VLAN PCP marking to prioritize real-time traffic over background traffic on multi-queue NICs.
- Provides a reproducible experimental setup and latency benchmarks using cyclictest, stress, and iperf under idle, stress, and concurrent-traffic loads.

## Relevance to Humanoid Robotics

Humanoid robots rely on tightly coordinated, low-latency communication between distributed controllers, sensors, and actuators. This work is relevant because it validates that a cost-effective, standard Linux networking stack with PREEMPT-RT can meet real-time constraints when properly tuned, providing a practical middleware foundation for humanoid control systems. The CPU/IRQ isolation and traffic-prioritization techniques it evaluates are directly applicable to reducing communication jitter in humanoid platforms that use Ethernet-based middleware such as DDS/RTPS or ROS 2.
