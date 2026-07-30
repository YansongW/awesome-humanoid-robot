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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2101.02074v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
Robot Operating System 2 (ROS2)는 분산 실시간 시스템을 대상으로 하며 로봇 공학 커뮤니티에서 널리 사용됩니다. 특히 이러한 시스템에서는 데이터 처리 및 통신의 지연 시간이 불안정성을 초래할 수 있습니다. 지연 시간 측면에서 매우 구성 가능함에도 불구하고, ROS2는 종종 기본 설정으로 사용됩니다. 본 논문에서는 기본 설정과 다양한 DDS(Data Distribution Service) 미들웨어를 사용하는 분산 시스템에서 ROS2의 종단 간 지연 시간을 조사합니다. 또한 ROS2 스택을 프로파일링하고 지연 시간 병목 현상을 지적합니다. 연구 결과에 따르면 종단 간 지연 시간은 사용된 DDS 미들웨어에 크게 의존합니다. 더 나아가, ROS2는 저수준 DDS 통신을 사용하는 것에 비해 50%의 지연 시간 오버헤드를 초래할 수 있음을 보여줍니다. 이러한 결과는 분산 ROS2 아키텍처 설계를 위한 지침을 제시하며 ROS2 오버헤드 감소 가능성을 시사합니다.

## 핵심 내용
Robot Operating System 2 (ROS2)는 분산 실시간 시스템을 대상으로 하며 로봇 공학 커뮤니티에서 널리 사용됩니다. 특히 이러한 시스템에서는 데이터 처리 및 통신의 지연 시간이 불안정성을 초래할 수 있습니다. 지연 시간 측면에서 매우 구성 가능함에도 불구하고, ROS2는 종종 기본 설정으로 사용됩니다. 본 논문에서는 기본 설정과 다양한 DDS(Data Distribution Service) 미들웨어를 사용하는 분산 시스템에서 ROS2의 종단 간 지연 시간을 조사합니다. 또한 ROS2 스택을 프로파일링하고 지연 시간 병목 현상을 지적합니다. 연구 결과에 따르면 종단 간 지연 시간은 사용된 DDS 미들웨어에 크게 의존합니다. 더 나아가, ROS2는 저수준 DDS 통신을 사용하는 것에 비해 50%의 지연 시간 오버헤드를 초래할 수 있음을 보여줍니다. 이러한 결과는 분산 ROS2 아키텍처 설계를 위한 지침을 제시하며 ROS2 오버헤드 감소 가능성을 시사합니다.

## 参考
- http://arxiv.org/abs/2101.02074v3
