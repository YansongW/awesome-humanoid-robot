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

