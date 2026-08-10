---
$id: ent_paper_kronauer_latency_analysis_of_ros2_multi_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Latency Analysis of ROS2 Multi-Node Systems
  zh: ROS2多节点系统的延迟分析
  ko: ROS2 다중 노드 시스템의 지연 시간 분석
summary:
  en: This paper characterizes end-to-end latency in ROS2 multi-node chains using default settings and profiles intra-layer
    delays across FastRTPS, CycloneDDS, and Connext on desktop and Raspberry Pi 4 hardware.
  zh: 本文针对ROS2多节点链路的端到端延迟进行表征，使用默认配置在桌面平台和Raspberry Pi 4上分析了FastRTPS、CycloneDDS与Connext三种中间件的层内延迟分布。研究发现端到端延迟高度依赖所选DDS中间件，且ROS2相比底层DDS通信会引入高达50%的延迟开销。
  ko: 본 논문은 기본 설정을 사용하는 ROS2 다중 노드 체인의 종단 간 지연 시간을 특성화하고, 데스크톱 및 라즈베리 파이 4 하드웨어에서 FastRTPS, CycloneDDS, Connext의 계층 내 지연을
    프로파일링한다.
domains:
- 08_software_middleware
- 05_mass_production
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- knowledge
tags:
- ros2
- dds_middleware
- end_to_end_latency
- multi_node_systems
- distributed_real_time
- latency_bottleneck
- middleware_overhead
- humanoid_control_pipeline
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2101.02074v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (734 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Latency Analysis of ROS2 Multi-Node Systems
  url: https://arxiv.org/abs/2101.02074
  date: '2021'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---
## 概述
本研究聚焦于ROS2在分布式实时系统中的默认配置延迟特性。作者在桌面计算机和Raspberry Pi 4硬件上，对FastRTPS、CycloneDDS和Connext三种DDS中间件进行了多节点链路的端到端延迟测量，并深入剖析了ROS2协议栈各层的延迟瓶颈。实验结果表明，不同DDS中间件对延迟影响显著，同时ROS2自身的封装层会带来额外延迟开销，最高可达底层DDS通信的50%。这些发现为设计低延迟的分布式ROS2架构提供了指导原则，并指出了降低ROS2开销的潜在优化方向。

## 核心内容
### 研究背景与目标
- ROS2面向分布式实时系统，在机器人领域广泛应用，其数据处理与通信延迟可能导致系统不稳定。
- 尽管ROS2在延迟方面具有高度可配置性，实际使用中常采用默认设置。
- 本文旨在评估默认配置下ROS2多节点系统的端到端延迟，并对比不同DDS中间件的性能差异。

### 实验方法
- **硬件平台**：桌面计算机与Raspberry Pi 4。
- **中间件**：FastRTPS、CycloneDDS、Connext。
- **测量内容**：多节点链路的端到端延迟，以及ROS2协议栈各层（intra-layer）的延迟分布。

### 关键发现
- 端到端延迟对所选DDS中间件高度敏感，不同中间件间延迟差异显著。
- ROS2封装层引入额外延迟开销，相比直接使用底层DDS通信，延迟最高增加50%。
- 通过剖析ROS2栈，识别出延迟瓶颈所在层。

### 结论与指导意义
- 研究结果为设计分布式ROS2架构提供延迟优化指南。
- 指出通过减少ROS2封装层开销可有效降低系统延迟，例如优化节点间通信路径或调整中间件配置。

## Overview
The Robot Operating System 2 (ROS2) targets distributed real-time systems and is widely used in the robotics community. Especially in these systems, latency in data processing and communication can lead to instabilities. Though being highly configurable with respect to latency, ROS2 is often used with its default settings.   In this paper, we investigate the end-to-end latency of ROS2 for distributed systems with default settings and different Data Distribution Service (DDS) middlewares. In addition, we profile the ROS2 stack and point out latency bottlenecks. Our findings indicate that end-to-end latency strongly depends on the used DDS middleware. Moreover, we show that ROS2 can lead to 50% latency overhead compared to using low-level DDS communications. Our results imply guidelines for designing distributed ROS2 architectures and indicate possibilities for reducing the ROS2 overhead.

## Overview
The Robot Operating System 2 (ROS2) targets distributed real-time systems and is widely used in the robotics community. Especially in these systems, latency in data processing and communication can lead to instabilities. Though being highly configurable with respect to latency, ROS2 is often used with its default settings. In this paper, we investigate the end-to-end latency of ROS2 for distributed systems with default settings and different Data Distribution Service (DDS) middlewares. In addition, we profile the ROS2 stack and point out latency bottlenecks. Our findings indicate that end-to-end latency strongly depends on the used DDS middleware. Moreover, we show that ROS2 can lead to 50% latency overhead compared to using low-level DDS communications. Our results imply guidelines for designing distributed ROS2 architectures and indicate possibilities for reducing the ROS2 overhead.

## Content
The Robot Operating System 2 (ROS2) targets distributed real-time systems and is widely used in the robotics community. Especially in these systems, latency in data processing and communication can lead to instabilities. Though being highly configurable with respect to latency, ROS2 is often used with its default settings. In this paper, we investigate the end-to-end latency of ROS2 for distributed systems with default settings and different Data Distribution Service (DDS) middlewares. In addition, we profile the ROS2 stack and point out latency bottlenecks. Our findings indicate that end-to-end latency strongly depends on the used DDS middleware. Moreover, we show that ROS2 can lead to 50% latency overhead compared to using low-level DDS communications. Our results imply guidelines for designing distributed ROS2 architectures and indicate possibilities for reducing the ROS2 overhead.

## 参考
- http://arxiv.org/abs/2101.02074v3

## 개요
본 연구는 ROS2가 분산 실시간 시스템에서 기본 설정으로 사용될 때의 지연 특성에 초점을 맞춘다. 저자는 데스크톱 컴퓨터와 Raspberry Pi 4 하드웨어에서 FastRTPS, CycloneDDS, Connext 세 가지 DDS 미들웨어를 대상으로 다중 노드 링크의 종단 간 지연을 측정하고, ROS2 프로토콜 스택의 각 계층에서 발생하는 지연 병목 현상을 심층 분석하였다. 실험 결과, DDS 미들웨어에 따라 지연에 미치는 영향이 크게 달랐으며, ROS2 자체의 캡슐화 계층이 추가적인 지연 오버헤드를 유발하여 최대 기본 DDS 통신의 50%에 달하는 지연이 발생할 수 있음을 확인하였다. 이러한 발견은 저지연 분산 ROS2 아키텍처 설계를 위한 지침을 제공하며, ROS2 오버헤드를 줄일 수 있는 잠재적 최적화 방향을 제시한다.

## 핵심 내용
### 연구 배경 및 목표
- ROS2는 분산 실시간 시스템을 대상으로 하며 로봇 분야에서 널리 활용되는데, 데이터 처리 및 통신 지연이 시스템 불안정을 초래할 수 있다.
- ROS2는 지연 측면에서 높은 구성 유연성을 제공하지만, 실제 사용에서는 기본 설정이 자주 사용된다.
- 본 논문은 기본 설정 하에서 ROS2 다중 노드 시스템의 종단 간 지연을 평가하고, 서로 다른 DDS 미들웨어 간 성능 차이를 비교하는 것을 목표로 한다.

### 실험 방법
- **하드웨어 플랫폼**: 데스크톱 컴퓨터 및 Raspberry Pi 4.
- **미들웨어**: FastRTPS, CycloneDDS, Connext.
- **측정 내용**: 다중 노드 링크의 종단 간 지연 및 ROS2 프로토콜 스택 각 계층(intra-layer)의 지연 분포.

### 주요 발견
- 종단 간 지연은 선택된 DDS 미들웨어에 매우 민감하며, 미들웨어 간 지연 차이가 크게 나타난다.
- ROS2 캡슐화 계층은 추가적인 지연 오버헤드를 유발하며, 기본 DDS 통신을 직접 사용할 때보다 지연이 최대 50% 증가할 수 있다.
- ROS2 스택 분석을 통해 지연 병목이 발생하는 계층을 식별하였다.

### 결론 및 지침 의미
- 연구 결과는 분산 ROS2 아키텍처 설계를 위한 지연 최적화 지침을 제공한다.
- ROS2 캡슐화 계층의 오버헤드를 줄이면 시스템 지연을 효과적으로 낮출 수 있음을 지적하며, 예를 들어 노드 간 통신 경로 최적화나 미들웨어 구성 조정을 통해 이를 달성할 수 있다.
