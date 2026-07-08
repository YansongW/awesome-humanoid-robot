---
$id: ent_paper_paul_performance_evaluation_of_ros2_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Performance Evaluation of ROS2-DDS middleware implementations facilitating Cooperative
    Driving in Autonomous Vehicle
  zh: 促进自动驾驶协同驾驶的ROS2-DDS中间件实现性能评估
  ko: 자율주행 차량의 협력 주행을 위한 ROS2-DDS 미들웨어 구현체의 성능 평가
summary:
  en: This paper empirically evaluates same-domain and cross-domain ROS2-DDS communication
    latency across Eclipse Cyclone DDS, eProsima Fast-DDS, and RTI Connext DDS using
    heterogeneous physical devices and multiple data types.
  zh: 本文使用异构物理设备和多种数据类型，对Eclipse Cyclone DDS、eProsima Fast-DDS和RTI Connext DDS的域内和跨域ROS2-DDS通信延迟进行了实证评估。
  ko: 본 논문은 이종 물리적 장치와 다양한 데이터 유형을 사용하여 Eclipse Cyclone DDS, eProsima Fast-DDS, RTI
    Connext DDS의 동일 도메인 및 교차 도메인 ROS2-DDS 통신 지연 시간을 실증적으로 평가한다.
domains:
- 08_software_middleware
- 10_evaluation_benchmarks
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- system
tags:
- ros2
- dds
- middleware
- autonomous_vehicles
- cooperative_perception
- multi_domain_communication
- cross_domain_latency
- latency_evaluation
- cyclone_dds
- fast_dds
- connext_dds
- real_time_communication
- heterogeneous_devices
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full-text review needed
    before verification.
sources:
- id: src_001
  type: paper
  title: Performance Evaluation of ROS2-DDS middleware implementations facilitating
    Cooperative Driving in Autonomous Vehicle
  url: https://arxiv.org/abs/2412.07485
  date: '2024'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---

## Overview

The study addresses the challenge of DDS domain participant limits in large-scale ROS2 deployments for cooperative autonomous driving. It evaluates how different vendor-specific DDS implementations perform when ROS2 nodes communicate across DDS domains. The experiments use ROS2 Humble on Raspberry Pi 3, Raspberry Pi 4, Jetson Nano, and laptops, connected via wired and wireless links. Three DDS implementations—Eclipse Cyclone DDS, eProsima Fast-DDS, and RTI Connext DDS—are tested, along with bridging solutions including Zenoh-plugin-DDS, Integration Service, and Routing Service.

The methodology measures round-trip latency for binary, string, and IMU message types with varying payload sizes and publisher frequencies. Results compare same-domain versus different-domain communication and assess the overhead introduced by cross-domain bridges. The authors provide practical guidance for selecting DDS implementations, data types, and connectivity media in multi-domain ROS2 systems.

## Key Contributions

- First performance comparison of same-domain versus different-domain ROS2 communication across multiple vendor-specific DDS implementations.
- Benchmarking on ROS2 Humble using real physical devices including Raspberry Pi 3, Raspberry Pi 4, Jetson Nano, and laptops.
- Latency characterization across binary, string, and IMU data types with variable sizes and publisher frequencies.
- Practical guidance for selecting DDS implementation, data type/size, and connectivity medium for multi-domain ROS2 systems.

## Relevance to Humanoid Robotics

Although framed around autonomous vehicles, the findings directly apply to scalable humanoid-robot deployments that rely on ROS2 and DDS for distributed multi-node communication. Humanoid robots often require cooperative perception and sensor data sharing across multiple compute units and domains, making cross-domain DDS latency and bridge overhead critical design considerations.
