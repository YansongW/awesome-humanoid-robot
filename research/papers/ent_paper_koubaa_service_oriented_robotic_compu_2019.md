---
$id: ent_paper_koubaa_service_oriented_robotic_compu_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Service-Oriented Robotic Computing for Cloud Robotics
  zh: 面向云机器人技术的服务导向机器人计算
  ko: 클라우드 로보틱스를 위한 서비스 지향 로봇 컴퓨팅
summary:
  en: A survey of service-oriented architecture and Web services for cloud robotics,
    distinguishing the virtualization of robotic systems from computation offloading
    to cloud-based services.
  zh: 本文综述了面向服务的架构与Web服务在云机器人中的应用，区分了机器人系统虚拟化和向云端服务卸载计算两类方法。
  ko: 본 논문은 서비스 지향 아키텍처와 웹 서비스를 활용한 클라우드 로보틱스를 개괄하며, 로봇 시스템 가상화와 클라우드 기반 서비스로의 계산
    오프로딩을 구분한다.
domains:
- 08_software_middleware
- 05_mass_production
- 02_components
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
tags:
- cloud_robotics
- service_oriented_architecture
- web_services
- computation_offloading
- robot_virtualization
- ros
- middleware
- rest
- soap
- websockets
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the arXiv full text (v2); requires human review before
    verification.
sources:
- id: src_001
  type: paper
  title: Service-Oriented Robotic Computing for Cloud Robotics
  url: https://arxiv.org/abs/1901.08173
  date: '2019'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This article surveys the use of service-oriented architecture (SOA) and Web services in robotics applications integrated with the Internet and the Cloud. The author traces the emergence of this trend from the broader concept of cloud robotics, which leverages cloud infrastructures for robotics following a service-oriented approach.

The survey organizes the literature into two main categories: (i) the virtualization of robotic systems through Web services, and (ii) the offloading of computation from robots to cloud-based services. For each category, the paper reviews representative technologies and systems, compares SOAP, REST, and Websocket communication paradigms, and discusses their implications for building scalable, Internet-accessible robotic software.

## Key Contributions

- Defines core concepts including SOA, Web services, REST, cloud robotics, virtualization, and computation offloading.
- Compares SOAP, REST, and Websocket technologies as communication mechanisms for robot virtualization.
- Reviews robotic virtualization contributions such as rosbridge, ROS Web services, Dronemap Planner, and ROSLink.
- Reviews cloud computation offloading contributions including DaVinci, Rapyuta, OpenEASE, and AWS RoboMaker.

## Relevance to Humanoid Robotics

Service-oriented cloud robotics can reduce onboard hardware requirements for humanoid robots by offloading computation-intensive tasks such as perception, planning, and machine learning to cloud services. This supports cost-effective mass production and deployment because less powerful onboard computers can be used while still achieving complex behaviors.

However, the paper also notes that the performance of cloud-dependent robotics systems is heavily affected by network quality-of-service, which is a critical concern for real-time humanoid control. In addition, several reviewed prototypes rely on simulators or lack extensive real-world validation, so their direct transfer to humanoid platforms requires further verification.
