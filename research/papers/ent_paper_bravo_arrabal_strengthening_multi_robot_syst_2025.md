---
$id: ent_paper_bravo_arrabal_strengthening_multi_robot_syst_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Strengthening Multi-Robot Systems for SAR: Co-Designing Robotics and Communication Towards 6G'
  zh: 面向搜救的强化多机器人系统：协同设计机器人与6G通信
  ko: 'SAR를 위한 다중 로봇 시스템 강화: 6G를 향한 로봇공학과 통신의 공동 설계'
summary:
  en: Presents field-tested Search and Rescue use cases that co-design mobile robots and 5G/6G edge-cloud communications,
    integrating hybrid wireless sensor networks, ROS-based smartphones, MEC-based SLAM, and networked UGV/UAV cooperation
    within the X-IoCA architecture.
  zh: 提出在X-IoCA架构中协同设计移动机器人与5G/6G边缘云通信的实地搜救用例，集成混合无线传感器网络、基于ROS的智能手机、MEC SLAM以及网络化UGV/UAV协作。
  ko: X-IoCA 아키텍처 내에서 혼합 무선 센서 네트워크, ROS 기반 스마트폰, MEC 기반 SLAM, 네트워크화된 UGV/UAV 협업을 통합하여 이동 로봇과 5G/6G 엣지-클라우드 통신을 공동 설계한 현장
    검증 구조 탐색 및 구조 사례를 제시한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.01940v1.
sources:
- id: src_001
  type: paper
  title: 'Strengthening Multi-Robot Systems for SAR: Co-Designing Robotics and Communication Towards 6G'
  url: https://arxiv.org/abs/2504.01940
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
This paper presents field-tested use cases from Search and Rescue (SAR) missions, highlighting the co-design of mobile robots and communication systems to support Edge-Cloud architectures based on 5G Standalone (SA). The main goal is to contribute to the effective cooperation of multiple robots and first responders. Our field experience includes the development of Hybrid Wireless Sensor Networks (H-WSNs) for risk and victim detection, smartphones integrated into the Robot Operating System (ROS) as Edge devices for mission requests and path planning, real-time Simultaneous Localization and Mapping (SLAM) via Multi-Access Edge Computing (MEC), and implementation of Uncrewed Ground Vehicles (UGVs) for victim evacuation in different navigation modes. These experiments, conducted in collaboration with actual first responders, underscore the need for intelligent network resource management, balancing low-latency and high-bandwidth demands. Network slicing is key to ensuring critical emergency services are performed despite challenging communication conditions. The paper identifies architectural needs, lessons learned, and challenges to be addressed by 6G technologies to enhance emergency response capabilities.

## 核心内容
This paper presents field-tested use cases from Search and Rescue (SAR) missions, highlighting the co-design of mobile robots and communication systems to support Edge-Cloud architectures based on 5G Standalone (SA). The main goal is to contribute to the effective cooperation of multiple robots and first responders. Our field experience includes the development of Hybrid Wireless Sensor Networks (H-WSNs) for risk and victim detection, smartphones integrated into the Robot Operating System (ROS) as Edge devices for mission requests and path planning, real-time Simultaneous Localization and Mapping (SLAM) via Multi-Access Edge Computing (MEC), and implementation of Uncrewed Ground Vehicles (UGVs) for victim evacuation in different navigation modes. These experiments, conducted in collaboration with actual first responders, underscore the need for intelligent network resource management, balancing low-latency and high-bandwidth demands. Network slicing is key to ensuring critical emergency services are performed despite challenging communication conditions. The paper identifies architectural needs, lessons learned, and challenges to be addressed by 6G technologies to enhance emergency response capabilities.

## 参考
- http://arxiv.org/abs/2504.01940v1

