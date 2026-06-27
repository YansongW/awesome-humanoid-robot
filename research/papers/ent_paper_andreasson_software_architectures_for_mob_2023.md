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
  en: A survey chapter that reviews software architectures and middleware frameworks
    for mobile robots, including ROS, ROS2, YARP, Orocos, Player, CARMEN, MATLAB,
    and Microsoft Robotics Developer Studio, and catalogs common architectural patterns
    such as component-based design, publish-subscribe, peer-to-peer, and service-oriented
    approaches.
  zh: 一篇综述章节，回顾了移动机器人的软件架构和中间件框架，包括 ROS、ROS2、YARP、Orocos、Player、CARMEN、MATLAB 和 Microsoft
    Robotics Developer Studio，并梳理了基于组件设计、发布-订阅、点对点、面向服务等常见架构模式。
  ko: ROS, ROS2, YARP, Orocos, Player, CARMEN, MATLAB, Microsoft Robotics Developer
    Studio 등 모바일 로봇용 소프트웨어 아키텍처와 미들웨어 프레임워크를 검토하고, 컴포넌트 기반 설계, 발행-구독, 피어 투 피어, 서비스
    지향 등의 일반적인 아키텍처 패턴을 정리한 서베이 장이다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full-text review required
    before verification.
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

## Overview

This Encyclopedia of Robotics chapter provides a broad survey of software architectures and middleware frameworks developed for mobile robots. The authors review historically influential and currently prominent frameworks, including ROS, ROS2, YARP, Orocos, Player, CARMEN, MATLAB, and Microsoft Robotics Developer Studio, and identify common functional and non-functional requirements that such systems must satisfy. These requirements include support for asynchronous communication, real-time behavior, distributed processing, hardware heterogeneity, modularity, fault tolerance, and reuse. The chapter maps each framework to the architectural patterns it embodies, offering a conceptual basis for comparing and selecting middleware for specific robotic platforms.

The chapter organizes architectural patterns into categories such as component-based design, publish-subscribe, peer-to-peer, client-server, event-driven, service-oriented, plug-in, blackboard, and database-centric approaches. For each pattern, the authors discuss how it addresses communication, coordination, scalability, and dynamic reconfiguration. The discussion also covers supporting infrastructure such as hardware abstraction layers, simulation tools (e.g., Gazebo, Stage, RViz), and communication buses (e.g., CAN bus, Ethernet, serial bus). The chapter concludes by outlining convergence trends and future research directions toward more distributed, efficient, and dynamically reconfigurable component-based systems.

Overall, the work is positioned as a methodological survey rather than an empirical benchmark study. It synthesizes existing knowledge about robot software architectures and provides a taxonomy that can guide practitioners in choosing or designing middleware for mobile robots, including complex humanoid platforms.

## Key Contributions

- Comparative survey of widely used mobile-robotic frameworks and their core communication designs.
- Enumeration of common functional and non-functional requirements for mobile-robot middleware, including real-time capabilities, asynchronous communication, and distributed processing.
- Taxonomy of architectural patterns used in mobile robotics, including peer-to-peer, publish-subscribe, component-based, and service-oriented designs.
- Discussion of convergence trends and future research directions toward distributed component-based systems.

## Relevance to Humanoid Robotics

Humanoid robots are complex mobile robotic platforms that integrate diverse sensors, actuators, perception modules, planners, and controllers into a single system. The middleware and architectural patterns surveyed in this chapter are directly relevant to humanoid robotics because they provide the communication, modularity, and real-time coordination infrastructure required to integrate these subsystems. Frameworks such as ROS2 and YARP, in particular, are widely used in humanoid research and development.

For mass production and deployment of humanoids, selecting scalable, maintainable, and dynamically reconfigurable software architectures is critical. This chapter's taxonomy of component-based, publish-subscribe, and service-oriented patterns offers a knowledge foundation for making such architectural decisions in humanoid-robot engineering and production pipelines.
