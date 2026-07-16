---
$id: ent_paper_andreasson_software_architectures_for_mob_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Software Architectures for Mobile Robots
  zh: 移动机器人软件架构
  ko: 모바일 로봇을 위한 소프트웨어 아키텍처
summary:
  en: A survey chapter that reviews software architectures and middleware frameworks for mobile robots, including ROS, ROS2,
    YARP, Orocos, Player, CARMEN, MATLAB, and Microsoft Robotics Developer Studio, and catalogs common architectural patterns
    such as component-based design, publish-subscribe, peer-to-peer, and service-oriented approaches.
  zh: 一篇综述章节，回顾了移动机器人的软件架构和中间件框架，包括 ROS、ROS2、YARP、Orocos、Player、CARMEN、MATLAB 和 Microsoft Robotics Developer Studio，并梳理了基于组件设计、发布-订阅、点对点、面向服务等常见架构模式。
  ko: ROS, ROS2, YARP, Orocos, Player, CARMEN, MATLAB, Microsoft Robotics Developer Studio 등 모바일 로봇용 소프트웨어 아키텍처와 미들웨어 프레임워크를
    검토하고, 컴포넌트 기반 설계, 발행-구독, 피어 투 피어, 서비스 지향 등의 일반적인 아키텍처 패턴을 정리한 서베이 장이다.
domains:
- 08_software_middleware
- 06_design_engineering
- 05_mass_production
layers:
- intelligence
- midstream
functional_roles:
- knowledge
tags:
- software_architecture
- robotic_middleware
- ros
- ros2
- yarp
- orocos
- component_based_design
- publish_subscribe
- peer_to_peer
- humanoid_software
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2206.03233v2.
sources:
- id: src_001
  type: paper
  title: Software Architectures for Mobile Robots
  url: https://arxiv.org/abs/2206.03233
  date: '2023'
  accessed_at: '2026-06-27'
  doi: 10.1007/978-3-642-41610-1_160-1
theoretical_depth:
- method
---
## 概述
A software architecture defines the blueprints of a large computational system, and is thus a crucial part of the design and development effort. This task has been explored extensively in the context of mobile robots, resulting in a plethora of reference designs and implementations. As the software architecture defines the framework in which all components are implemented, it is naturally a very important aspect of a mobile robot system. In this chapter, we overview the requirements that the particular problem domain (a mobile robot system) imposes on the software framework. We discuss some of the current design solutions, provide a historical perspective on common frameworks, and outline directions for future development.

## 核心内容
A software architecture defines the blueprints of a large computational system, and is thus a crucial part of the design and development effort. This task has been explored extensively in the context of mobile robots, resulting in a plethora of reference designs and implementations. As the software architecture defines the framework in which all components are implemented, it is naturally a very important aspect of a mobile robot system. In this chapter, we overview the requirements that the particular problem domain (a mobile robot system) imposes on the software framework. We discuss some of the current design solutions, provide a historical perspective on common frameworks, and outline directions for future development.

## 参考
- http://arxiv.org/abs/2206.03233v2

## Overview
A software architecture defines the blueprints of a large computational system, and is thus a crucial part of the design and development effort. This task has been explored extensively in the context of mobile robots, resulting in a plethora of reference designs and implementations. As the software architecture defines the framework in which all components are implemented, it is naturally a very important aspect of a mobile robot system. In this chapter, we overview the requirements that the particular problem domain (a mobile robot system) imposes on the software framework. We discuss some of the current design solutions, provide a historical perspective on common frameworks, and outline directions for future development.

## Content
A software architecture defines the blueprints of a large computational system, and is thus a crucial part of the design and development effort. This task has been explored extensively in the context of mobile robots, resulting in a plethora of reference designs and implementations. As the software architecture defines the framework in which all components are implemented, it is naturally a very important aspect of a mobile robot system. In this chapter, we overview the requirements that the particular problem domain (a mobile robot system) imposes on the software framework. We discuss some of the current design solutions, provide a historical perspective on common frameworks, and outline directions for future development.

## 개요
소프트웨어 아키텍처는 대규모 컴퓨팅 시스템의 청사진을 정의하므로 설계 및 개발 노력의 중요한 부분입니다. 이 작업은 모바일 로봇의 맥락에서 광범위하게 탐구되어 수많은 참조 설계와 구현을 낳았습니다. 소프트웨어 아키텍처는 모든 구성 요소가 구현되는 프레임워크를 정의하므로, 당연히 모바일 로봇 시스템의 매우 중요한 측면입니다. 이 장에서는 특정 문제 영역(모바일 로봇 시스템)이 소프트웨어 프레임워크에 부과하는 요구 사항을 개괄적으로 살펴봅니다. 현재의 몇 가지 설계 솔루션을 논의하고, 일반적인 프레임워크에 대한 역사적 관점을 제공하며, 향후 개발 방향을 제시합니다.

## 핵심 내용
소프트웨어 아키텍처는 대규모 컴퓨팅 시스템의 청사진을 정의하므로 설계 및 개발 노력의 중요한 부분입니다. 이 작업은 모바일 로봇의 맥락에서 광범위하게 탐구되어 수많은 참조 설계와 구현을 낳았습니다. 소프트웨어 아키텍처는 모든 구성 요소가 구현되는 프레임워크를 정의하므로, 당연히 모바일 로봇 시스템의 매우 중요한 측면입니다. 이 장에서는 특정 문제 영역(모바일 로봇 시스템)이 소프트웨어 프레임워크에 부과하는 요구 사항을 개괄적으로 살펴봅니다. 현재의 몇 가지 설계 솔루션을 논의하고, 일반적인 프레임워크에 대한 역사적 관점을 제공하며, 향후 개발 방향을 제시합니다.
