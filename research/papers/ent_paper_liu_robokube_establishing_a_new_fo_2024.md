---
$id: ent_paper_liu_robokube_establishing_a_new_fo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboKube: Establishing a New Foundation for the Cloud Native Evolution in Robotics'
  zh: RoboKube：为机器人云原生演进建立新基础
  ko: 'RoboKube: 로보틱스의 클라우드 네이티브 진화를 위한 새로운 기반 구축'
summary:
  en: This paper proposes RoboKube, a Kubernetes-based framework for deploying containerized ROS 2 applications across the
    device-edge-cloud continuum, and demonstrates its feasibility through a teleoperation testbed using a UR5 manipulator.
  zh: 本文提出 RoboKube，一种基于 Kubernetes 的框架，用于在设备-边缘-云端连续体上部署容器化的 ROS 2 应用，并通过使用 UR5 机械臂的遥操作测试平台验证其可行性。
  ko: 본 논문은 디바이스-엣지-클라우드 연속체에서 컨테이너화된 ROS 2 애플리케이션을 배포하기 위한 Kubernetes 기반 프레임워크인 RoboKube를 제안하고, UR5 매니퓰레이터를 사용한 원격조작 테스트베드를
    통해 그 타당성을 입증한다.
domains:
- 08_software_middleware
- 05_mass_production
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- system
tags:
- cloud_native
- kubernetes
- ros_2
- containerization
- orchestration
- device_edge_cloud
- teleoperation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.04440v1.
sources:
- id: src_001
  type: paper
  title: 'RoboKube: Establishing a New Foundation for the Cloud Native Evolution in Robotics'
  url: https://arxiv.org/abs/2403.04440
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Cloud native technologies have been observed to expand into the realm of Internet of Things (IoT) and Cyber-physical Systems, of which an important application domain is robotics. In this paper, we review the cloudification practice in the robotics domain from both literature and industrial perspectives. We propose RoboKube, an adaptive framework that is based on the Kubernetes (K8s) ecosystem to set up a common platform across the device-cloud continuum for the deployment of cloudified Robotic Operating System (ROS) powered applications, to facilitate the cloud native evolution in robotics. We examine the process of modernizing ROS applications using cloud-native technologies, focusing on both the platform and application perspectives. In addition, we address the challenges of networking setups for heterogeneous environments. This paper intends to serves as a guide for developers and researchers, offering insights into containerization strategies, ROS node distribution and clustering, and deployment options. To demonstrate the feasibility of our approach, we present a case study involving the cloudification of a teleoperation testbed.

## 核心内容
Cloud native technologies have been observed to expand into the realm of Internet of Things (IoT) and Cyber-physical Systems, of which an important application domain is robotics. In this paper, we review the cloudification practice in the robotics domain from both literature and industrial perspectives. We propose RoboKube, an adaptive framework that is based on the Kubernetes (K8s) ecosystem to set up a common platform across the device-cloud continuum for the deployment of cloudified Robotic Operating System (ROS) powered applications, to facilitate the cloud native evolution in robotics. We examine the process of modernizing ROS applications using cloud-native technologies, focusing on both the platform and application perspectives. In addition, we address the challenges of networking setups for heterogeneous environments. This paper intends to serves as a guide for developers and researchers, offering insights into containerization strategies, ROS node distribution and clustering, and deployment options. To demonstrate the feasibility of our approach, we present a case study involving the cloudification of a teleoperation testbed.

## 参考
- http://arxiv.org/abs/2403.04440v1

## Overview
Cloud native technologies have been observed to expand into the realm of Internet of Things (IoT) and Cyber-physical Systems, of which an important application domain is robotics. In this paper, we review the cloudification practice in the robotics domain from both literature and industrial perspectives. We propose RoboKube, an adaptive framework that is based on the Kubernetes (K8s) ecosystem to set up a common platform across the device-cloud continuum for the deployment of cloudified Robotic Operating System (ROS) powered applications, to facilitate the cloud native evolution in robotics. We examine the process of modernizing ROS applications using cloud-native technologies, focusing on both the platform and application perspectives. In addition, we address the challenges of networking setups for heterogeneous environments. This paper intends to serve as a guide for developers and researchers, offering insights into containerization strategies, ROS node distribution and clustering, and deployment options. To demonstrate the feasibility of our approach, we present a case study involving the cloudification of a teleoperation testbed.

## Content
Cloud native technologies have been observed to expand into the realm of Internet of Things (IoT) and Cyber-physical Systems, of which an important application domain is robotics. In this paper, we review the cloudification practice in the robotics domain from both literature and industrial perspectives. We propose RoboKube, an adaptive framework that is based on the Kubernetes (K8s) ecosystem to set up a common platform across the device-cloud continuum for the deployment of cloudified Robotic Operating System (ROS) powered applications, to facilitate the cloud native evolution in robotics. We examine the process of modernizing ROS applications using cloud-native technologies, focusing on both the platform and application perspectives. In addition, we address the challenges of networking setups for heterogeneous environments. This paper intends to serve as a guide for developers and researchers, offering insights into containerization strategies, ROS node distribution and clustering, and deployment options. To demonstrate the feasibility of our approach, we present a case study involving the cloudification of a teleoperation testbed.

## 개요
클라우드 네이티브 기술은 사물인터넷(IoT) 및 사이버-물리 시스템 영역으로 확장되고 있으며, 그중 중요한 응용 분야 중 하나가 로봇공학입니다. 본 논문에서는 문헌 및 산업 관점에서 로봇공학 분야의 클라우드화 실무를 검토합니다. 우리는 Kubernetes(K8s) 생태계를 기반으로 한 적응형 프레임워크인 RoboKube를 제안하여, 디바이스-클라우드 연속체 전반에 걸친 공통 플랫폼을 구축하고 클라우드화된 로봇 운영 체제(ROS) 기반 애플리케이션을 배포함으로써 로봇공학에서의 클라우드 네이티브 발전을 촉진합니다. 또한, 플랫폼 및 애플리케이션 관점에 초점을 맞춰 클라우드 네이티브 기술을 사용한 ROS 애플리케이션 현대화 과정을 검토합니다. 추가로, 이기종 환경에서의 네트워킹 설정 과제를 다룹니다. 본 논문은 컨테이너화 전략, ROS 노드 분배 및 클러스터링, 배포 옵션에 대한 통찰력을 제공하여 개발자와 연구자에게 가이드 역할을 하고자 합니다. 접근 방식의 실현 가능성을 입증하기 위해, 원격 조작 테스트베드의 클라우드화를 포함한 사례 연구를 제시합니다.

## 핵심 내용
클라우드 네이티브 기술은 사물인터넷(IoT) 및 사이버-물리 시스템 영역으로 확장되고 있으며, 그중 중요한 응용 분야 중 하나가 로봇공학입니다. 본 논문에서는 문헌 및 산업 관점에서 로봇공학 분야의 클라우드화 실무를 검토합니다. 우리는 Kubernetes(K8s) 생태계를 기반으로 한 적응형 프레임워크인 RoboKube를 제안하여, 디바이스-클라우드 연속체 전반에 걸친 공통 플랫폼을 구축하고 클라우드화된 로봇 운영 체제(ROS) 기반 애플리케이션을 배포함으로써 로봇공학에서의 클라우드 네이티브 발전을 촉진합니다. 또한, 플랫폼 및 애플리케이션 관점에 초점을 맞춰 클라우드 네이티브 기술을 사용한 ROS 애플리케이션 현대화 과정을 검토합니다. 추가로, 이기종 환경에서의 네트워킹 설정 과제를 다룹니다. 본 논문은 컨테이너화 전략, ROS 노드 분배 및 클러스터링, 배포 옵션에 대한 통찰력을 제공하여 개발자와 연구자에게 가이드 역할을 하고자 합니다. 접근 방식의 실현 가능성을 입증하기 위해, 원격 조작 테스트베드의 클라우드화를 포함한 사례 연구를 제시합니다.
