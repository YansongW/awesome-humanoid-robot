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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1808.10821v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    en/ko body retranslated from zh deep-read (572 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/1808.10821v1

## Overview
As robotic systems become increasingly distributed, communication between modules is crucial for overall control reliability. This study evaluates the performance of the Linux communication stack in real-time robotic applications using a multi-core embedded device as the test platform. Experiments demonstrate that, with appropriate configuration, the Linux kernel can significantly enhance the determinism of UDP protocol communication. Additionally, the research highlights that concurrent traffic can disrupt latency bounds and proposes a solution by isolating real-time applications and their corresponding interrupts to different CPU cores.

## Content
### Research Background and Objectives
- Under the trend of distributed robotic systems, the reliability of inter-module communication has become critical.
- Evaluate the real-time performance of UDP communication on PREEMPT-RT Linux systems.

### Experimental Platform and Methodology
- Use a multi-core ARMv7 embedded device as the test platform.
- Measure UDP round-trip latency to assess communication determinism.

### Key Findings
- **Kernel Configuration Optimization**: With appropriate configuration, the Linux kernel can significantly improve the determinism of UDP communication, achieving bounded latency.
- **Impact of Concurrent Traffic**: Unisolated concurrent traffic can disrupt latency bounds, leading to reduced determinism.
- **Solution**: Isolating real-time applications and their corresponding interrupts (IRQ) to different CPU cores can effectively mitigate interference.

### Conclusion
- On PREEMPT-RT Linux, communication latency requirements for real-time robotic applications can be met through kernel configuration, traffic prioritization, and CPU/IRQ isolation.
- Managing concurrent traffic is a key challenge in ensuring determinism.

## 개요
로봇 시스템이 점점 분산화됨에 따라, 모듈 간 통신은 전체 제어 신뢰성에 있어 중요합니다. 본 연구는 멀티코어 임베디드 장치를 테스트 플랫폼으로 사용하여, 실시간 로봇 애플리케이션에서 Linux 통신 스택의 성능을 평가합니다. 실험을 통해 적절한 구성 하에서 Linux 커널이 UDP 프로토콜 통신의 결정성을 크게 향상시킬 수 있음을 입증했습니다. 동시에, 연구는 동시 트래픽이 지연 경계를 파괴할 수 있음을 지적하며, 실시간 애플리케이션과 해당 인터럽트를 서로 다른 CPU 코어에 분리하는 솔루션을 제안합니다.

## 핵심 내용
### 연구 배경 및 목표
- 로봇 시스템의 분산화 추세 속에서 모듈 간 통신 신뢰성이 핵심이 됩니다.
- PREEMPT-RT Linux 시스템에서 UDP 통신의 실시간 성능을 평가합니다.

### 실험 플랫폼 및 방법
- 멀티코어 ARMv7 임베디드 장치를 테스트 플랫폼으로 사용합니다.
- UDP 왕복 지연(round-trip latency)을 측정하여 통신 결정성을 평가합니다.

### 주요 발견
- **커널 구성 최적화**: 적절한 구성을 통해 Linux 커널이 UDP 통신의 결정성을 크게 향상시켜 유계 지연을 구현할 수 있습니다.
- **동시 트래픽 영향**: 격리되지 않은 동시 트래픽은 지연 경계를 파괴하여 결정성을 저하시킵니다.
- **솔루션**: 실시간 애플리케이션과 해당 인터럽트(IRQ)를 서로 다른 CPU 코어에 분리하면 간섭을 효과적으로 격리할 수 있습니다.

### 결론
- PREEMPT-RT Linux에서 커널 구성, 트래픽 우선순위 지정 및 CPU/IRQ 격리를 통해 실시간 로봇 애플리케이션의 통신 지연 요구 사항을 충족할 수 있습니다.
- 동시 트래픽 관리는 결정성을 보장하는 핵심 과제입니다.
