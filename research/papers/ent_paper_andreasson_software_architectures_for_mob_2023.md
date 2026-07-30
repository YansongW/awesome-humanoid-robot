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
  zh: 本文是一篇综述章节，系统回顾了移动机器人领域的软件架构与中间件框架，包括ROS、ROS2、YARP、Orocos、Player、CARMEN、MATLAB及Microsoft Robotics Developer Studio。核心贡献在于梳理了组件化设计、发布-订阅、点对点和服务导向等常见架构模式，并分析了移动机器人系统对软件框架的特殊需求。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2206.03233v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
该章节首先阐述了软件架构作为大型计算系统蓝图的重要性，并指出其在移动机器人领域已催生大量参考设计与实现。作者概述了移动机器人这一特定问题域对软件框架提出的要求，随后讨论了当前主流设计解决方案，提供了常见框架的历史视角，并展望了未来发展方向。文中重点列举了ROS、ROS2、YARP、Orocos、Player、CARMEN、MATLAB及Microsoft Robotics Developer Studio等代表性框架，并系统分类了组件化设计、发布-订阅、点对点和服务导向等架构模式。

## 核心内容
### 核心内容
- **软件架构定义**：软件架构为大型计算系统提供蓝图，是设计与开发工作的关键环节。在移动机器人领域，这一任务已被广泛探索，产生了大量参考设计与实现。
- **领域需求**：移动机器人系统对软件框架有特殊要求，包括实时性、可靠性、模块化、可扩展性及异构硬件支持等。
- **历史视角**：章节提供了常见框架的历史演进脉络，从早期Player、CARMEN等框架到现代ROS/ROS2生态，反映了从紧耦合到松耦合、从集中式到分布式的发展趋势。

### 主要框架
- **ROS (Robot Operating System)**：基于发布-订阅模式的分布式框架，支持节点间异步通信，广泛用于研究与原型开发。
- **ROS2**：在ROS基础上引入DDS (Data Distribution Service) 标准，增强实时性、安全性与跨平台支持。
- **YARP (Yet Another Robot Platform)**：面向人形机器人设计的点对点通信框架，强调模块化与跨语言支持。
- **Orocos (Open Robot Control Software)**：提供实时控制组件库，支持组件化设计与硬实时操作。
- **Player**：早期开源框架，采用客户端-服务器模型，适用于多传感器移动机器人。
- **CARMEN (Carnegie Mellon Robot Navigation Toolkit)**：集成导航、定位与感知模块的框架，强调模块间松耦合。
- **MATLAB**：通过Simulink与Robotics System Toolbox提供仿真与算法快速原型能力。
- **Microsoft Robotics Developer Studio**：基于.NET的框架，支持可视化编程与分布式服务架构。

### 架构模式
- **组件化设计 (Component-Based Design)**：将系统拆分为独立功能模块，通过明确定义的接口交互，提升复用性与可维护性。
- **发布-订阅 (Publish-Subscribe)**：解耦数据生产者与消费者，支持异步、多对多通信，典型如ROS中的Topic机制。
- **点对点 (Peer-to-Peer)**：节点间直接通信，减少中间环节延迟，适用于实时控制场景，如YARP的Port连接。
- **服务导向 (Service-Oriented)**：将功能封装为可远程调用的服务，支持同步请求-响应模式，如ROS中的Service与Action。

### 未来方向
- 增强实时性与确定性，满足工业级机器人需求。
- 提升跨平台兼容性与云-边-端协同能力。
- 引入形式化验证与安全机制，应对复杂动态环境。

## Overview
A software architecture defines the blueprints of a large computational system, and is thus a crucial part of the design and development effort. This task has been explored extensively in the context of mobile robots, resulting in a plethora of reference designs and implementations. As the software architecture defines the framework in which all components are implemented, it is naturally a very important aspect of a mobile robot system. In this chapter, we overview the requirements that the particular problem domain (a mobile robot system) imposes on the software framework. We discuss some of the current design solutions, provide a historical perspective on common frameworks, and outline directions for future development.

## 개요
소프트웨어 아키텍처는 대규모 컴퓨팅 시스템의 청사진을 정의하므로 설계 및 개발 노력의 중요한 부분입니다. 이 작업은 모바일 로봇의 맥락에서 광범위하게 탐구되어 수많은 참조 설계와 구현을 낳았습니다. 소프트웨어 아키텍처는 모든 구성 요소가 구현되는 프레임워크를 정의하므로, 당연히 모바일 로봇 시스템의 매우 중요한 측면입니다. 이 장에서는 특정 문제 영역(모바일 로봇 시스템)이 소프트웨어 프레임워크에 부과하는 요구 사항을 개괄적으로 살펴봅니다. 현재의 몇 가지 설계 솔루션을 논의하고, 일반적인 프레임워크에 대한 역사적 관점을 제공하며, 향후 개발 방향을 제시합니다.

## 핵심 내용
소프트웨어 아키텍처는 대규모 컴퓨팅 시스템의 청사진을 정의하므로 설계 및 개발 노력의 중요한 부분입니다. 이 작업은 모바일 로봇의 맥락에서 광범위하게 탐구되어 수많은 참조 설계와 구현을 낳았습니다. 소프트웨어 아키텍처는 모든 구성 요소가 구현되는 프레임워크를 정의하므로, 당연히 모바일 로봇 시스템의 매우 중요한 측면입니다. 이 장에서는 특정 문제 영역(모바일 로봇 시스템)이 소프트웨어 프레임워크에 부과하는 요구 사항을 개괄적으로 살펴봅니다. 현재의 몇 가지 설계 솔루션을 논의하고, 일반적인 프레임워크에 대한 역사적 관점을 제공하며, 향후 개발 방향을 제시합니다.

## 参考
- http://arxiv.org/abs/2206.03233v2
