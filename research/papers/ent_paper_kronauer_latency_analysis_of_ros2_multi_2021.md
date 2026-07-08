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
  en: This paper characterizes end-to-end latency in ROS2 multi-node chains using
    default settings and profiles intra-layer delays across FastRTPS, CycloneDDS,
    and Connext on desktop and Raspberry Pi 4 hardware.
  zh: 本文在默认配置下对ROS2多节点链路的端到端延迟进行特征分析，并在台式机和树莓派4硬件上对FastRTPS、CycloneDDS与Connext进行层内延迟剖析。
  ko: 본 논문은 기본 설정을 사용하는 ROS2 다중 노드 체인의 종단 간 지연 시간을 특성화하고, 데스크톱 및 라즈베리 파이 4 하드웨어에서
    FastRTPS, CycloneDDS, Connext의 계층 내 지연을 프로파일링한다.
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
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: AI-extracted from the provided metadata and abstract; the full paper text
    was not independently inspected.
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

## Overview

This paper investigates the end-to-end latency of ROS2 in distributed multi-node systems using default settings. The authors instrument a Dockerized ROS2 Foxy build with intra-layer timestamps and measure the 95th-percentile end-to-end latency across node chains ranging from 3 to 23 nodes. Experiments are conducted on an Intel i7-8700 desktop PC and a Raspberry Pi 4 Model B Rev 1.1, varying the DDS middleware (FastRTPS 2.0.1, Eclipse Cyclone DDS 0.6.0, RTI Connext 6.0.1), publisher frequency (1–100 Hz), payload size (128 B–500 KB), and QoS reliability.

The findings indicate that end-to-end latency strongly depends on the chosen DDS middleware and that ROS2 can introduce approximately 50 % overhead compared to low-level DDS communication, especially for small messages. The profiling identifies DDS transport latency and rclcpp notification delay as the dominant contributors to overall latency.

The work provides practical rules of thumb for designing low-latency distributed ROS2 architectures and highlights where the ROS2 stack can be optimized to reduce overhead.

## Key Contributions

- End-to-end latency characterization of ROS2 multi-node chains up to 23 nodes with default settings.
- Intra-layer profiling that identifies DDS transport and rclcpp notification delay as dominant latency contributors.
- Quantification of up to ~50 % ROS2 overhead relative to low-level DDS communication for small messages.
- Practical rules of thumb for designing low-latency distributed ROS2 architectures.
- Comparative evaluation of FastRTPS, CycloneDDS, and Connext on desktop and embedded hardware.

## Relevance to Humanoid Robotics

Humanoid robots are typically distributed modular systems with many sensor, processing, and actuation nodes that must meet real-time constraints. Understanding and minimizing inter-node communication latency is therefore directly relevant to building predictable, scalable control pipelines for mass-produced humanoid platforms. The paper's comparison of DDS middlewares and its guidelines for low-latency ROS2 architectures can inform middleware selection and node-layout decisions in humanoid robot designs.
