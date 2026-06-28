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
  en: This paper proposes RoboKube, a Kubernetes-based framework for deploying containerized
    ROS 2 applications across the device-edge-cloud continuum, and demonstrates its
    feasibility through a teleoperation testbed using a UR5 manipulator.
  zh: 本文提出 RoboKube，一种基于 Kubernetes 的框架，用于在设备-边缘-云端连续体上部署容器化的 ROS 2 应用，并通过使用 UR5 机械臂的遥操作测试平台验证其可行性。
  ko: 본 논문은 디바이스-엣지-클라우드 연속체에서 컨테이너화된 ROS 2 애플리케이션을 배포하기 위한 Kubernetes 기반 프레임워크인 RoboKube를
    제안하고, UR5 매니퓰레이터를 사용한 원격조작 테스트베드를 통해 그 타당성을 입증한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review against
    the full arXiv text before final verification.
sources:
- id: src_001
  type: paper
  title: 'RoboKube: Establishing a New Foundation for the Cloud Native Evolution in
    Robotics'
  url: https://arxiv.org/abs/2403.04440
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Cloud native technologies are increasingly being adopted beyond data centers into the Internet of Things and cyber-physical systems, including robotics. This paper reviews existing academic and industrial efforts to cloudify robotics, identifies their limitations, and proposes RoboKube—an adaptive, Kubernetes-based framework for deploying cloudified ROS applications across the device-edge-cloud continuum. The authors examine modernization from both platform and application perspectives, address networking challenges for heterogeneous environments, and present a teleoperation testbed to demonstrate the approach.

RoboKube leverages the Kubernetes ecosystem, including lightweight distributions such as K3s, to orchestrate containerized ROS 2 nodes. The framework uses overlay networking solutions with multicast-capable CNI backends such as Kube-ovn to support ROS 2 DDS/RTPS traffic across clusters. Application packaging and deployment follow container best practices and are distributed using Helm charts. The authors also discuss container image minimization techniques such as DockerSlim, although they note that dependency extraction still requires manual effort.

## Key Contributions

- Proposes RoboKube, a Kubernetes-based orchestration framework for cloudified ROS applications.
- Provides guidance on networking setup across the device-edge-cloud continuum for ROS 2 DDS/RTPS traffic.
- Defines containerization, deployment, and distribution best practices for ROS 2 nodes.
- Demonstrates the approach with a cloudified teleoperation testbed using a UR5 arm and a USB joystick.
- Surveys existing academic and industrial cloud-robotics efforts and identifies their limitations.

## Relevance to Humanoid Robotics

Although the paper's case study uses a UR5 manipulator rather than a humanoid robot, the problem of cloud-native deployment and orchestration of ROS-based robot systems is directly relevant to scaling and managing fleets of humanoid robots in heterogeneous production environments. Humanoid robots typically run many ROS 2 nodes for perception, planning, and control, and require reliable coordination across device, edge, and cloud resources. RoboKube's Kubernetes-based orchestration, overlay networking for DDS/RTPS, and containerization practices address core middleware challenges that humanoid deployments face at scale.
