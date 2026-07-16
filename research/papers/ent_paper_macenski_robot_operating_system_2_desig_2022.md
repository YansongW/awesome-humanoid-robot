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
  en: A 2022 review paper that presents the ground-up architectural redesign of ROS 2 around DDS middleware and documents
    its real-world adoption through case studies across land, sea, air, space, and fleet robotics.
  zh: The next chapter of the robotics revolution is well underway with the deployment of robots for a broad range of commercial
    use-cases. Even in a myriad of applications and environments, there exists a common vocabulary of components that robots
    share - the need for a modular, scalable, and reliable architecture; sensing; planning; mobility; and autonomy. The Robot
    Operating System (ROS) was an integral part of the last chapter, demonstrably expediting robotics research with freely-available
    components and a modular framework. However, ROS 1 was not designed with many necessary production-grade
  ko: 2022년 리뷰 논문으로, DDS 미들웨어 중심의 ROS 2 전면 아키텍처 재설계를 제시하고 육상·해상·공중·우주·fleet 로보틱스 사례 연구를 통해 실제 도입 상황을 기록함.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2211.07752v1.
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

## 概述
The next chapter of the robotics revolution is well underway with the deployment of robots for a broad range of commercial use-cases. Even in a myriad of applications and environments, there exists a common vocabulary of components that robots share - the need for a modular, scalable, and reliable architecture; sensing; planning; mobility; and autonomy. The Robot Operating System (ROS) was an integral part of the last chapter, demonstrably expediting robotics research with freely-available components and a modular framework. However, ROS 1 was not designed with many necessary production-grade features and algorithms. ROS 2 and its related projects have been redesigned from the ground up to meet the challenges set forth by modern robotic systems in new and exploratory domains at all scales. In this review, we highlight the philosophical and architectural changes of ROS 2 powering this new chapter in the robotics revolution. We also show through case studies the influence ROS 2 and its adoption has had on accelerating real robot systems to reliable deployment in an assortment of challenging environments.

## 核心内容
The next chapter of the robotics revolution is well underway with the deployment of robots for a broad range of commercial use-cases. Even in a myriad of applications and environments, there exists a common vocabulary of components that robots share - the need for a modular, scalable, and reliable architecture; sensing; planning; mobility; and autonomy. The Robot Operating System (ROS) was an integral part of the last chapter, demonstrably expediting robotics research with freely-available components and a modular framework. However, ROS 1 was not designed with many necessary production-grade features and algorithms. ROS 2 and its related projects have been redesigned from the ground up to meet the challenges set forth by modern robotic systems in new and exploratory domains at all scales. In this review, we highlight the philosophical and architectural changes of ROS 2 powering this new chapter in the robotics revolution. We also show through case studies the influence ROS 2 and its adoption has had on accelerating real robot systems to reliable deployment in an assortment of challenging environments.

## 参考
- http://arxiv.org/abs/2211.07752v1

## Overview
The next chapter of the robotics revolution is well underway with the deployment of robots for a broad range of commercial use-cases. Even in a myriad of applications and environments, there exists a common vocabulary of components that robots share - the need for a modular, scalable, and reliable architecture; sensing; planning; mobility; and autonomy. The Robot Operating System (ROS) was an integral part of the last chapter, demonstrably expediting robotics research with freely-available components and a modular framework. However, ROS 1 was not designed with many necessary production-grade features and algorithms. ROS 2 and its related projects have been redesigned from the ground up to meet the challenges set forth by modern robotic systems in new and exploratory domains at all scales. In this review, we highlight the philosophical and architectural changes of ROS 2 powering this new chapter in the robotics revolution. We also show through case studies the influence ROS 2 and its adoption has had on accelerating real robot systems to reliable deployment in an assortment of challenging environments.

## Content
The next chapter of the robotics revolution is well underway with the deployment of robots for a broad range of commercial use-cases. Even in a myriad of applications and environments, there exists a common vocabulary of components that robots share - the need for a modular, scalable, and reliable architecture; sensing; planning; mobility; and autonomy. The Robot Operating System (ROS) was an integral part of the last chapter, demonstrably expediting robotics research with freely-available components and a modular framework. However, ROS 1 was not designed with many necessary production-grade features and algorithms. ROS 2 and its related projects have been redesigned from the ground up to meet the challenges set forth by modern robotic systems in new and exploratory domains at all scales. In this review, we highlight the philosophical and architectural changes of ROS 2 powering this new chapter in the robotics revolution. We also show through case studies the influence ROS 2 and its adoption has had on accelerating real robot systems to reliable deployment in an assortment of challenging environments.

## 개요
로봇 혁명의 다음 장은 다양한 상업적 사용 사례를 위한 로봇 배치와 함께 본격적으로 진행되고 있습니다. 수많은 응용 분야와 환경에서도 로봇이 공유하는 공통 구성 요소 어휘가 존재합니다. 즉, 모듈식, 확장 가능, 신뢰할 수 있는 아키텍처, 센싱, 계획, 이동성, 자율성에 대한 필요성입니다. 로봇 운영 체제(ROS)는 이전 장의 핵심적인 부분이었으며, 무료로 제공되는 구성 요소와 모듈식 프레임워크를 통해 로봇 연구를 획기적으로 가속화했습니다. 그러나 ROS 1은 많은 필수 생산 등급 기능과 알고리즘을 염두에 두고 설계되지 않았습니다. ROS 2와 관련 프로젝트는 모든 규모의 새롭고 탐구적인 영역에서 현대 로봇 시스템이 제시하는 과제를 해결하기 위해 처음부터 재설계되었습니다. 이 리뷰에서 우리는 로봇 혁명의 이 새로운 장을 추진하는 ROS 2의 철학적 및 아키텍처적 변화를 강조합니다. 또한 사례 연구를 통해 ROS 2와 그 채택이 다양한 도전적인 환경에서 실제 로봇 시스템의 신뢰할 수 있는 배치를 가속화하는 데 미친 영향을 보여줍니다.

## 핵심 내용
로봇 혁명의 다음 장은 다양한 상업적 사용 사례를 위한 로봇 배치와 함께 본격적으로 진행되고 있습니다. 수많은 응용 분야와 환경에서도 로봇이 공유하는 공통 구성 요소 어휘가 존재합니다. 즉, 모듈식, 확장 가능, 신뢰할 수 있는 아키텍처, 센싱, 계획, 이동성, 자율성에 대한 필요성입니다. 로봇 운영 체제(ROS)는 이전 장의 핵심적인 부분이었으며, 무료로 제공되는 구성 요소와 모듈식 프레임워크를 통해 로봇 연구를 획기적으로 가속화했습니다. 그러나 ROS 1은 많은 필수 생산 등급 기능과 알고리즘을 염두에 두고 설계되지 않았습니다. ROS 2와 관련 프로젝트는 모든 규모의 새롭고 탐구적인 영역에서 현대 로봇 시스템이 제시하는 과제를 해결하기 위해 처음부터 재설계되었습니다. 이 리뷰에서 우리는 로봇 혁명의 이 새로운 장을 추진하는 ROS 2의 철학적 및 아키텍처적 변화를 강조합니다. 또한 사례 연구를 통해 ROS 2와 그 채택이 다양한 도전적인 환경에서 실제 로봇 시스템의 신뢰할 수 있는 배치를 가속화하는 데 미친 영향을 보여줍니다.
