---
$id: ent_paper_bravo_arrabal_strengthening_multi_robot_syst_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Strengthening Multi-Robot Systems for SAR: Co-Designing Robotics and Communication
    Towards 6G'
  zh: 面向搜救的强化多机器人系统：协同设计机器人与6G通信
  ko: 'SAR를 위한 다중 로봇 시스템 강화: 6G를 향한 로봇공학과 통신의 공동 설계'
summary:
  en: Presents field-tested Search and Rescue use cases that co-design mobile robots
    and 5G/6G edge-cloud communications, integrating hybrid wireless sensor networks,
    ROS-based smartphones, MEC-based SLAM, and networked UGV/UAV cooperation within
    the X-IoCA architecture.
  zh: 提出在X-IoCA架构中协同设计移动机器人与5G/6G边缘云通信的实地搜救用例，集成混合无线传感器网络、基于ROS的智能手机、MEC SLAM以及网络化UGV/UAV协作。
  ko: X-IoCA 아키텍처 내에서 혼합 무선 센서 네트워크, ROS 기반 스마트폰, MEC 기반 SLAM, 네트워크화된 UGV/UAV 협업을
    통합하여 이동 로봇과 5G/6G 엣지-클라우드 통신을 공동 설계한 현장 검증 구조 탐색 및 구조 사례를 제시한다.
domains:
- 08_software_middleware
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- system
- intelligence
tags:
- search_and_rescue
- multi_robot_coordination
- edge_cloud
- 5g
- 6g
- network_slicing
- ros
- mec_slam
- hybrid_wireless_sensor_network
- ugv
- uav
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full paper not independently
    consulted. Requires human review before full verification.
sources:
- id: src_001
  type: paper
  title: 'Strengthening Multi-Robot Systems for SAR: Co-Designing Robotics and Communication
    Towards 6G'
  url: https://arxiv.org/abs/2504.01940
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper reports field-tested Search and Rescue (SAR) use cases developed with first-responder organizations, emphasizing the co-design of mobile robots and communication systems for 5G Standalone edge-cloud architectures. The work covers Hybrid Wireless Sensor Networks for risk and victim detection, smartphones integrated into ROS as Edge devices, real-time SLAM offloaded to Multi-Access Edge Computing, and UGV-based casualty extraction in multiple navigation modes. These experiments are positioned within the X-IoCA architecture, which coordinates heterogeneous robots, sensor networks, edge infrastructure, and human responders. The authors stress that intelligent network resource management—particularly network slicing—is needed to balance low-latency and high-bandwidth demands in emergency scenarios.

## Key Contributions

- Field-tested SAR use cases demonstrating co-design of robotics and 5G edge-cloud communications.
- Integration of H-WSNs, ROS smartphones as Edge devices, MEC-based SLAM, and UGV casualty extraction.
- X-IoCA architecture enabling cooperation among heterogeneous robots, sensor networks, MEC, and human responders.
- Analysis of lessons learned and 6G challenges including reliability, sensing, human-robot interaction, and integrated sensing and communication.

## Relevance to Humanoid Robotics

Although the reported experiments use UGVs and UAVs rather than humanoids, the communication, edge-cloud, network-slicing, and ROS-based multi-agent coordination infrastructure is directly applicable to scaling humanoid robots in emergency and industrial field operations. Humanoid deployment in unstructured SAR environments would face the same latency, bandwidth, reliability, and human-robot interaction requirements analyzed here.
