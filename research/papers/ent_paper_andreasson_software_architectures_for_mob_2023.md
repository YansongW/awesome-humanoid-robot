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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2206.03233v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    en/ko body retranslated from zh deep-read (1425 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2206.03233v2

## Overview
This section first elaborates on the importance of software architecture as a blueprint for large-scale computing systems and notes that it has spawned numerous reference designs and implementations in the field of mobile robotics. The author outlines the requirements that the specific problem domain of mobile robots imposes on software frameworks, then discusses current mainstream design solutions, provides a historical perspective on common frameworks, and looks ahead to future development directions. The text highlights representative frameworks such as ROS, ROS2, YARP, Orocos, Player, CARMEN, MATLAB, and Microsoft Robotics Developer Studio, and systematically categorizes architectural patterns including component-based design, publish-subscribe, peer-to-peer, and service-oriented approaches.

## Content
### Content
- **Definition of Software Architecture**: Software architecture provides a blueprint for large-scale computing systems and is a critical part of the design and development process. In the field of mobile robotics, this task has been extensively explored, yielding numerous reference designs and implementations.
- **Domain Requirements**: Mobile robot systems impose specific requirements on software frameworks, including real-time performance, reliability, modularity, scalability, and support for heterogeneous hardware.
- **Historical Perspective**: The section provides a historical evolution of common frameworks, from early frameworks such as Player and CARMEN to the modern ROS/ROS2 ecosystem, reflecting a trend from tight coupling to loose coupling and from centralized to distributed systems.

### Major Frameworks
- **ROS (Robot Operating System)**: A distributed framework based on the publish-subscribe pattern, supporting asynchronous communication between nodes, widely used in research and prototyping.
- **ROS2**: Builds on ROS by introducing the DDS (Data Distribution Service) standard, enhancing real-time performance, security, and cross-platform support.
- **YARP (Yet Another Robot Platform)**: A peer-to-peer communication framework designed for humanoid robots, emphasizing modularity and cross-language support.
- **Orocos (Open Robot Control Software)**: Provides a library of real-time control components, supporting component-based design and hard real-time operations.
- **Player**: An early open-source framework employing a client-server model, suitable for mobile robots with multiple sensors.
- **CARMEN (Carnegie Mellon Robot Navigation Toolkit)**: A framework integrating navigation, localization, and perception modules, emphasizing loose coupling between modules.
- **MATLAB**: Offers simulation and rapid algorithm prototyping capabilities through Simulink and the Robotics System Toolbox.
- **Microsoft Robotics Developer Studio**: A .NET-based framework supporting visual programming and distributed service architectures.

### Architectural Patterns
- **Component-Based Design**: Decomposes the system into independent functional modules that interact through well-defined interfaces, enhancing reusability and maintainability.
- **Publish-Subscribe**: Decouples data producers from consumers, supporting asynchronous, many-to-many communication, as exemplified by the Topic mechanism in ROS.
- **Peer-to-Peer**: Direct communication between nodes reduces intermediate latency, suitable for real-time control scenarios, such as the Port connections in YARP.
- **Service-Oriented**: Encapsulates functionality as remotely invocable services, supporting synchronous request-response patterns, such as Service and Action in ROS.

### Future Directions
- Enhancing real-time performance and determinism to meet industrial-grade robot requirements.
- Improving cross-platform compatibility and cloud-edge-device collaboration capabilities.
- Introducing formal verification and security mechanisms to address complex dynamic environments.

## 개요
이 장에서는 먼저 소프트웨어 아키텍처가 대규모 컴퓨팅 시스템의 청사진으로서 지니는 중요성을 설명하고, 모바일 로봇 분야에서 이로 인해 수많은 참조 설계와 구현이 파생되었음을 지적합니다. 저자는 모바일 로봇이라는 특정 문제 영역이 소프트웨어 프레임워크에 요구하는 사항을 개괄한 뒤, 현재 주류 설계 솔루션을 논의하고, 일반적인 프레임워크에 대한 역사적 관점을 제공하며, 향후 발전 방향을 전망합니다. 본문에서는 ROS, ROS2, YARP, Orocos, Player, CARMEN, MATLAB 및 Microsoft Robotics Developer Studio와 같은 대표적인 프레임워크를 중점적으로 열거하고, 컴포넌트 기반 설계, 발행-구독, 점대점 및 서비스 지향과 같은 아키텍처 패턴을 체계적으로 분류합니다.

## 핵심 내용
### 핵심 내용
- **소프트웨어 아키텍처 정의**: 소프트웨어 아키텍처는 대규모 컴퓨팅 시스템에 청사진을 제공하며, 설계 및 개발 작업의 핵심 단계입니다. 모바일 로봇 분야에서 이 작업은 광범위하게 탐구되어 수많은 참조 설계와 구현을 낳았습니다.
- **도메인 요구 사항**: 모바일 로봇 시스템은 소프트웨어 프레임워크에 실시간성, 신뢰성, 모듈화, 확장성 및 이기종 하드웨어 지원 등을 포함한 특별한 요구 사항을 제기합니다.
- **역사적 관점**: 이 장은 초기 Player, CARMEN과 같은 프레임워크에서 현대 ROS/ROS2 생태계에 이르기까지 일반적인 프레임워크의 역사적 진화 흐름을 제공하며, 긴밀한 결합에서 느슨한 결합으로, 중앙 집중식에서 분산식으로의 발전 추세를 반영합니다.

### 주요 프레임워크
- **ROS (Robot Operating System)**: 발행-구독 패턴 기반의 분산 프레임워크로, 노드 간 비동기 통신을 지원하며 연구 및 프로토타입 개발에 널리 사용됩니다.
- **ROS2**: ROS를 기반으로 DDS (Data Distribution Service) 표준을 도입하여 실시간성, 보안성 및 크로스 플랫폼 지원을 강화합니다.
- **YARP (Yet Another Robot Platform)**: 휴머노이드 로봇 설계를 위한 점대점 통신 프레임워크로, 모듈성과 다국어 지원을 강조합니다.
- **Orocos (Open Robot Control Software)**: 실시간 제어 컴포넌트 라이브러리를 제공하며, 컴포넌트 기반 설계와 하드 실시간 운영을 지원합니다.
- **Player**: 초기 오픈소스 프레임워크로, 클라이언트-서버 모델을 채택하며 다중 센서 모바일 로봇에 적합합니다.
- **CARMEN (Carnegie Mellon Robot Navigation Toolkit)**: 내비게이션, 위치 추정 및 인식 모듈을 통합한 프레임워크로, 모듈 간 느슨한 결합을 강조합니다.
- **MATLAB**: Simulink와 Robotics System Toolbox를 통해 시뮬레이션 및 알고리즘 빠른 프로토타이핑 기능을 제공합니다.
- **Microsoft Robotics Developer Studio**: .NET 기반 프레임워크로, 시각적 프로그래밍과 분산 서비스 아키텍처를 지원합니다.

### 아키텍처 패턴
- **컴포넌트 기반 설계 (Component-Based Design)**: 시스템을 독립적인 기능 모듈로 분할하고, 명확하게 정의된 인터페이스를 통해 상호작용하여 재사용성과 유지보수성을 향상시킵니다.
- **발행-구독 (Publish-Subscribe)**: 데이터 생산자와 소비자를 분리하여 비동기, 다대다 통신을 지원하며, 대표적으로 ROS의 Topic 메커니즘이 있습니다.
- **점대점 (Peer-to-Peer)**: 노드 간 직접 통신으로 중간 단계의 지연을 줄이며, YARP의 Port 연결과 같은 실시간 제어 시나리오에 적합합니다.
- **서비스 지향 (Service-Oriented)**: 기능을 원격 호출 가능한 서비스로 캡슐화하여 동기식 요청-응답 패턴을 지원하며, ROS의 Service와 Action이 대표적입니다.

### 향후 방향
- 산업용 로봇 요구 사항을 충족하기 위해 실시간성과 결정론을 강화합니다.
- 크로스 플랫폼 호환성과 클라우드-엣지-디바이스 협업 능력을 향상시킵니다.
- 복잡한 동적 환경에 대응하기 위해 형식 검증과 보안 메커니즘을 도입합니다.
