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
  zh: 这篇2018年的论文在基于ARMv7多核嵌入式设备的PREEMPT-RT Linux系统上，实证评估了UDP往返延迟。核心贡献在于证明通过适当的内核配置、流量优先级划分以及CPU/IRQ隔离，可以限定通信延迟，而未经隔离的并发流量会破坏确定性。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1808.10821v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
随着机器人系统日益分布式化，各模块间的通信对整体控制可靠性至关重要。本研究以多核嵌入式设备为测试平台，评估了Linux通信栈在实时机器人应用中的性能。实验证明，在适当配置下，Linux内核能显著增强UDP协议通信的确定性。同时，研究指出并发流量会破坏延迟边界，并提出通过将实时应用及其对应中断分离到不同CPU核心的解决方案。

## 核心内容
### 研究背景与目标
- 机器人系统分布式化趋势下，模块间通信可靠性成为关键。
- 针对PREEMPT-RT Linux系统，评估UDP通信的实时性能。

### 实验平台与方法
- 使用多核ARMv7嵌入式设备作为测试平台。
- 测量UDP往返延迟（round-trip latency），评估通信确定性。

### 关键发现
- **内核配置优化**：通过适当配置，Linux内核能显著提升UDP通信的确定性，实现有界延迟。
- **并发流量影响**：未隔离的并发流量会破坏延迟边界，导致确定性下降。
- **解决方案**：将实时应用及其对应中断（IRQ）分离到不同CPU核心，可有效隔离干扰。

### 结论
- 在PREEMPT-RT Linux上，通过内核配置、流量优先级划分及CPU/IRQ隔离，可满足实时机器人应用的通信延迟要求。
- 并发流量管理是保证确定性的关键挑战。

## Overview
As robotics systems become more distributed, the communications between different robot modules play a key role for the reliability of the overall robot control. In this paper, we present a study of the Linux communication stack meant for real-time robotic applications. We evaluate the real-time performance of UDP based communications in Linux on multi-core embedded devices as test platforms. We prove that, under an appropriate configuration, the Linux kernel greatly enhances the determinism of communications using the UDP protocol. Furthermore, we demonstrate that concurrent traffic disrupts the bounded latencies and propose a solution by separating the real-time application and the corresponding interrupt in a CPU.

## 개요
로봇 시스템이 점점 더 분산화됨에 따라, 다양한 로봇 모듈 간의 통신은 전체 로봇 제어의 신뢰성에 핵심적인 역할을 합니다. 본 논문에서는 실시간 로봇 애플리케이션을 위한 Linux 통신 스택에 대한 연구를 제시합니다. 멀티코어 임베디드 장치를 테스트 플랫폼으로 사용하여 Linux에서 UDP 기반 통신의 실시간 성능을 평가합니다. 적절한 구성 하에서 Linux 커널이 UDP 프로토콜을 사용하는 통신의 결정성을 크게 향상시킨다는 것을 입증합니다. 또한, 동시 트래픽이 제한된 지연 시간을 방해한다는 것을 보여주고, CPU에서 실시간 애플리케이션과 해당 인터럽트를 분리하는 솔루션을 제안합니다.

## 핵심 내용
로봇 시스템이 점점 더 분산화됨에 따라, 다양한 로봇 모듈 간의 통신은 전체 로봇 제어의 신뢰성에 핵심적인 역할을 합니다. 본 논문에서는 실시간 로봇 애플리케이션을 위한 Linux 통신 스택에 대한 연구를 제시합니다. 멀티코어 임베디드 장치를 테스트 플랫폼으로 사용하여 Linux에서 UDP 기반 통신의 실시간 성능을 평가합니다. 적절한 구성 하에서 Linux 커널이 UDP 프로토콜을 사용하는 통신의 결정성을 크게 향상시킨다는 것을 입증합니다. 또한, 동시 트래픽이 제한된 지연 시간을 방해한다는 것을 보여주고, CPU에서 실시간 애플리케이션과 해당 인터럽트를 분리하는 솔루션을 제안합니다.

## 参考
- http://arxiv.org/abs/1808.10821v1
