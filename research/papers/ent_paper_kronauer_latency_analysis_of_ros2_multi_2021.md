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
  zh: 本文在默认配置下对ROS2多节点链路的端到端延迟进行特征分析，并在台式机和树莓派4硬件上对FastRTPS、CycloneDDS与Connext进行层内延迟剖析。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2101.02074v3.
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
The Robot Operating System 2 (ROS2) targets distributed real-time systems and is widely used in the robotics community. Especially in these systems, latency in data processing and communication can lead to instabilities. Though being highly configurable with respect to latency, ROS2 is often used with its default settings.   In this paper, we investigate the end-to-end latency of ROS2 for distributed systems with default settings and different Data Distribution Service (DDS) middlewares. In addition, we profile the ROS2 stack and point out latency bottlenecks. Our findings indicate that end-to-end latency strongly depends on the used DDS middleware. Moreover, we show that ROS2 can lead to 50% latency overhead compared to using low-level DDS communications. Our results imply guidelines for designing distributed ROS2 architectures and indicate possibilities for reducing the ROS2 overhead.

## 核心内容
The Robot Operating System 2 (ROS2) targets distributed real-time systems and is widely used in the robotics community. Especially in these systems, latency in data processing and communication can lead to instabilities. Though being highly configurable with respect to latency, ROS2 is often used with its default settings.   In this paper, we investigate the end-to-end latency of ROS2 for distributed systems with default settings and different Data Distribution Service (DDS) middlewares. In addition, we profile the ROS2 stack and point out latency bottlenecks. Our findings indicate that end-to-end latency strongly depends on the used DDS middleware. Moreover, we show that ROS2 can lead to 50% latency overhead compared to using low-level DDS communications. Our results imply guidelines for designing distributed ROS2 architectures and indicate possibilities for reducing the ROS2 overhead.

## 参考
- http://arxiv.org/abs/2101.02074v3

## Overview
The Robot Operating System 2 (ROS2) targets distributed real-time systems and is widely used in the robotics community. Especially in these systems, latency in data processing and communication can lead to instabilities. Though being highly configurable with respect to latency, ROS2 is often used with its default settings. In this paper, we investigate the end-to-end latency of ROS2 for distributed systems with default settings and different Data Distribution Service (DDS) middlewares. In addition, we profile the ROS2 stack and point out latency bottlenecks. Our findings indicate that end-to-end latency strongly depends on the used DDS middleware. Moreover, we show that ROS2 can lead to 50% latency overhead compared to using low-level DDS communications. Our results imply guidelines for designing distributed ROS2 architectures and indicate possibilities for reducing the ROS2 overhead.

## Content
The Robot Operating System 2 (ROS2) targets distributed real-time systems and is widely used in the robotics community. Especially in these systems, latency in data processing and communication can lead to instabilities. Though being highly configurable with respect to latency, ROS2 is often used with its default settings. In this paper, we investigate the end-to-end latency of ROS2 for distributed systems with default settings and different Data Distribution Service (DDS) middlewares. In addition, we profile the ROS2 stack and point out latency bottlenecks. Our findings indicate that end-to-end latency strongly depends on the used DDS middleware. Moreover, we show that ROS2 can lead to 50% latency overhead compared to using low-level DDS communications. Our results imply guidelines for designing distributed ROS2 architectures and indicate possibilities for reducing the ROS2 overhead.

## 개요
Robot Operating System 2 (ROS2)는 분산 실시간 시스템을 대상으로 하며 로봇 공학 커뮤니티에서 널리 사용됩니다. 특히 이러한 시스템에서는 데이터 처리 및 통신의 지연 시간이 불안정성을 초래할 수 있습니다. 지연 시간 측면에서 매우 구성 가능함에도 불구하고, ROS2는 종종 기본 설정으로 사용됩니다. 본 논문에서는 기본 설정과 다양한 DDS(Data Distribution Service) 미들웨어를 사용하는 분산 시스템에서 ROS2의 종단 간 지연 시간을 조사합니다. 또한 ROS2 스택을 프로파일링하고 지연 시간 병목 현상을 지적합니다. 연구 결과에 따르면 종단 간 지연 시간은 사용된 DDS 미들웨어에 크게 의존합니다. 더 나아가, ROS2는 저수준 DDS 통신을 사용하는 것에 비해 50%의 지연 시간 오버헤드를 초래할 수 있음을 보여줍니다. 이러한 결과는 분산 ROS2 아키텍처 설계를 위한 지침을 제시하며 ROS2 오버헤드 감소 가능성을 시사합니다.

## 핵심 내용
Robot Operating System 2 (ROS2)는 분산 실시간 시스템을 대상으로 하며 로봇 공학 커뮤니티에서 널리 사용됩니다. 특히 이러한 시스템에서는 데이터 처리 및 통신의 지연 시간이 불안정성을 초래할 수 있습니다. 지연 시간 측면에서 매우 구성 가능함에도 불구하고, ROS2는 종종 기본 설정으로 사용됩니다. 본 논문에서는 기본 설정과 다양한 DDS(Data Distribution Service) 미들웨어를 사용하는 분산 시스템에서 ROS2의 종단 간 지연 시간을 조사합니다. 또한 ROS2 스택을 프로파일링하고 지연 시간 병목 현상을 지적합니다. 연구 결과에 따르면 종단 간 지연 시간은 사용된 DDS 미들웨어에 크게 의존합니다. 더 나아가, ROS2는 저수준 DDS 통신을 사용하는 것에 비해 50%의 지연 시간 오버헤드를 초래할 수 있음을 보여줍니다. 이러한 결과는 분산 ROS2 아키텍처 설계를 위한 지침을 제시하며 ROS2 오버헤드 감소 가능성을 시사합니다.
