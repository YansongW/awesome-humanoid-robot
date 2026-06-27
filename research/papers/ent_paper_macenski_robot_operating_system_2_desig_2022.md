---
$id: ent_paper_macenski_robot_operating_system_2_desig_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Robot Operating System 2: Design, Architecture, and Uses In The Wild'
  zh: 机器人操作系统2：设计、架构与真实场景应用
  ko: '로봇 운영 체제 2: 설계, 아키텍처 및 실제 활용'
summary:
  en: A 2022 review paper that presents the ground-up architectural redesign of ROS
    2 around DDS middleware and documents its real-world adoption through case studies
    across land, sea, air, space, and fleet robotics.
  zh: 一篇2022年的综述论文，介绍了ROS 2围绕DDS中间件进行的自下而上架构重构，并通过陆地、海洋、空中、太空及集群机器人等案例研究记录其实际应用。
  ko: 2022년 리뷰 논문으로, DDS 미들웨어 중심의 ROS 2 전면 아키텍처 재설계를 제시하고 육상·해상·공중·우주·fleet 로보틱스 사례
    연구를 통해 실제 도입 상황을 기록함.
domains:
- 08_software_middleware
- 02_components
- 04_assembly_integration_testing
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- system
tags:
- ros2
- dds_middleware
- robot_middleware
- lifecycle_nodes
- component_nodes
- micro_ros
- sros2
- production_robotics
- fleet_robotics
- simulation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text verification
    needed for exact citations, section numbers, and quantitative claims.
sources:
- id: src_001
  type: paper
  title: 'Robot Operating System 2: Design, Architecture, and Uses In The Wild'
  url: https://arxiv.org/abs/2211.07752
  date: '2022'
  accessed_at: '2026-06-27'
  doi: 10.1126/scirobotics.abm6074
theoretical_depth:
- method
- system
---

## Overview

This 2022 paper provides a comprehensive review of the Robot Operating System 2 (ROS 2), explaining why ROS 1 was insufficient for production-grade robotics and how ROS 2 was rebuilt from the ground up to address those gaps. The authors describe a modular, distributed, asynchronous architecture centered on the Data Distribution Service (DDS) standard, with layered abstractions such as rcl, rmw, and rosidl separating application code from middleware details. They also discuss production-oriented capabilities including DDS-Security/SROS2, real-time APIs, lifecycle nodes, component-node composition, and micro-ROS for embedded devices.

The paper grounds these architectural claims in empirical benchmarking and case-study evidence. Benchmarks cover latency, throughput, CPU utilization, and resilience to packet loss under varying quality-of-service configurations. Case studies span land, sea, air, space, and large-scale fleet robotics, illustrating how ROS 2 has been adopted for reliable deployment outside research laboratories.

Overall, the work is positioned as both a technical survey and a status report on the ROS 2 ecosystem, synthesizing design philosophy, implementation choices, performance characterization, and field adoption.

## Key Contributions

- Architectural redesign of ROS 2 around DDS middleware with abstraction layers (rcl, rmw, rosidl).
- Built-in support for security via DDS-Security/SROS2, real-time computing, embedded systems via micro-ROS, and configurable quality-of-service policies.
- Introduction of lifecycle nodes and component-node composition to support flexible deployment and resource management.
- Empirical benchmarking of ROS 2 latency, throughput, CPU utilization, and resilience under packet loss.
- Case-study evidence of ROS 2 accelerating deployment across land, sea, air, space, and large-scale fleet robotics.

## Relevance to Humanoid Robotics

Humanoid robots require integration of multiple subsystems—perception, planning, control, simulation, and hardware interfaces—often developed by different teams and reused across platforms. ROS 2 provides the production-grade, modular middleware and developer tooling stack that supports this integration, enabling scalable development and reliable deployment beyond the lab. Its DDS-based networking, quality-of-service controls, and real-time support are directly applicable to the tight timing and safety requirements of humanoid locomotion and manipulation.

In addition, capabilities such as lifecycle nodes, component-node composition, and micro-ROS allow humanoid systems to manage computational resources across onboard computers and embedded motor controllers. Tools like Gazebo, rviz2, TF2, URDF, and rosbag2 support simulation, visualization, calibration, and data logging workflows that are essential for iterative humanoid-robot development and validation.
