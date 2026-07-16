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

## Overview
This paper presents field-tested use cases from Search and Rescue (SAR) missions, highlighting the co-design of mobile robots and communication systems to support Edge-Cloud architectures based on 5G Standalone (SA). The main goal is to contribute to the effective cooperation of multiple robots and first responders. Our field experience includes the development of Hybrid Wireless Sensor Networks (H-WSNs) for risk and victim detection, smartphones integrated into the Robot Operating System (ROS) as Edge devices for mission requests and path planning, real-time Simultaneous Localization and Mapping (SLAM) via Multi-Access Edge Computing (MEC), and implementation of Uncrewed Ground Vehicles (UGVs) for victim evacuation in different navigation modes. These experiments, conducted in collaboration with actual first responders, underscore the need for intelligent network resource management, balancing low-latency and high-bandwidth demands. Network slicing is key to ensuring critical emergency services are performed despite challenging communication conditions. The paper identifies architectural needs, lessons learned, and challenges to be addressed by 6G technologies to enhance emergency response capabilities.

## Content
This paper presents field-tested use cases from Search and Rescue (SAR) missions, highlighting the co-design of mobile robots and communication systems to support Edge-Cloud architectures based on 5G Standalone (SA). The main goal is to contribute to the effective cooperation of multiple robots and first responders. Our field experience includes the development of Hybrid Wireless Sensor Networks (H-WSNs) for risk and victim detection, smartphones integrated into the Robot Operating System (ROS) as Edge devices for mission requests and path planning, real-time Simultaneous Localization and Mapping (SLAM) via Multi-Access Edge Computing (MEC), and implementation of Uncrewed Ground Vehicles (UGVs) for victim evacuation in different navigation modes. These experiments, conducted in collaboration with actual first responders, underscore the need for intelligent network resource management, balancing low-latency and high-bandwidth demands. Network slicing is key to ensuring critical emergency services are performed despite challenging communication conditions. The paper identifies architectural needs, lessons learned, and challenges to be addressed by 6G technologies to enhance emergency response capabilities.

## 개요
본 논문은 수색 및 구조(SAR) 임무에서 현장 검증된 사용 사례를 제시하며, 5G 독립형(SA) 기반 엣지-클라우드 아키텍처를 지원하기 위한 모바일 로봇과 통신 시스템의 공동 설계를 강조합니다. 주요 목표는 다중 로봇과 최초 대응자 간의 효과적인 협력에 기여하는 것입니다. 현장 경험에는 위험 및 피해자 탐지를 위한 하이브리드 무선 센서 네트워크(H-WSN) 개발, 임무 요청 및 경로 계획을 위한 엣지 장치로서 로봇 운영 체제(ROS)에 통합된 스마트폰, 다중 접속 엣지 컴퓨팅(MEC)을 통한 실시간 동시 위치 추정 및 지도 작성(SLAM), 다양한 주행 모드에서 피해자 대피를 위한 무인 지상 차량(UGV) 구현이 포함됩니다. 실제 최초 대응자와 협력하여 수행된 이러한 실험은 지능형 네트워크 자원 관리의 필요성과 저지연 및 고대역폭 요구 간의 균형을 강조합니다. 네트워크 슬라이싱은 까다로운 통신 조건에서도 중요한 긴급 서비스가 수행되도록 보장하는 핵심 요소입니다. 본 논문은 6G 기술이 긴급 대응 능력을 향상시키기 위해 해결해야 할 아키텍처 요구 사항, 교훈 및 과제를 식별합니다.

## 핵심 내용
본 논문은 수색 및 구조(SAR) 임무에서 현장 검증된 사용 사례를 제시하며, 5G 독립형(SA) 기반 엣지-클라우드 아키텍처를 지원하기 위한 모바일 로봇과 통신 시스템의 공동 설계를 강조합니다. 주요 목표는 다중 로봇과 최초 대응자 간의 효과적인 협력에 기여하는 것입니다. 현장 경험에는 위험 및 피해자 탐지를 위한 하이브리드 무선 센서 네트워크(H-WSN) 개발, 임무 요청 및 경로 계획을 위한 엣지 장치로서 로봇 운영 체제(ROS)에 통합된 스마트폰, 다중 접속 엣지 컴퓨팅(MEC)을 통한 실시간 동시 위치 추정 및 지도 작성(SLAM), 다양한 주행 모드에서 피해자 대피를 위한 무인 지상 차량(UGV) 구현이 포함됩니다. 실제 최초 대응자와 협력하여 수행된 이러한 실험은 지능형 네트워크 자원 관리의 필요성과 저지연 및 고대역폭 요구 간의 균형을 강조합니다. 네트워크 슬라이싱은 까다로운 통신 조건에서도 중요한 긴급 서비스가 수행되도록 보장하는 핵심 요소입니다. 본 논문은 6G 기술이 긴급 대응 능력을 향상시키기 위해 해결해야 할 아키텍처 요구 사항, 교훈 및 과제를 식별합니다.
