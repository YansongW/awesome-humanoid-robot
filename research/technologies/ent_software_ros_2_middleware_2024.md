---
$id: ent_software_ros_2_middleware_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: software_platform
names:
  en: ROS 2 Middleware
  zh: ROS 2 中间件
  ko: ROS 2 미들웨어
summary:
  en: De facto robot middleware with DDS-based pub/sub and real-time support.
  zh: 基于DDS的发布/订阅和实时支持的事实标准机器人中间件。
  ko: DDS 기반 pub/sub 및 실시간 지원을 갖춘 사실상의 로봇 미들웨어.
domains:
- 08_software_middleware
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- dds
- middleware
- real_time
- ros2
- software_platform
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-02'
  confidence: medium
  notes: Imported via ingestion framework from source_type=website. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_001
  type: website
  title: ROS 2 Middleware
  url: https://www.ros.org/
  date: '2024'
  accessed_at: '2026-07-02'
---

## 概述
基于DDS的发布/订阅和实时支持的事实标准机器人中间件。

## 核心内容
### ROS 2 中间件的定义与定位
ROS 2 中间件属于 **软件平台** 类型。 所属领域包括：软件中间件, 设计工程。 价值链层级：智能层, midstream。 基于DDS的发布/订阅和实时支持的事实标准机器人中间件。 英文名称为 *ROS 2 Middleware*。 韩文名称为 *ROS 2 미들웨어*。

### ROS 2 中间件的工作原理与技术架构
ROS 2 中间件的核心机制决定了其在人形机器人系统中的性能边界。理解其内部结构、信号流与控制接口，有助于进行系统集成与优化。
在选型与集成过程中，需要关注其与控制器、通信总线、电源系统与机械结构的兼容性。

### 关键参数与选型要点
在工程实践中，选用ROS 2 中间件需要综合考虑性能指标、可靠性、成本、供应链成熟度以及与整机系统的兼容性。
关键参数通常包括精度、带宽、扭矩、功耗、重量、接口协议与环境适应性等。
针对不同应用场景，可能需要在性能与成本之间进行权衡，并预留适当的冗余与安全裕量。

### 典型应用与发展趋势
ROS 2 中间件已广泛应用于人形机器人的原型验证、学术研究与早期商业化产品中。
未来随着产业链成熟，其集成度、智能化水平与成本效益有望持续提升。

### 相关标签
- dds
- middleware
- real_time
- ros2
- software_platform

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键软件平台之一，ROS 2 中间件在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [ROS 2 Middleware](https://www.ros.org/)

## Overview
A de facto standard robot middleware based on DDS publish/subscribe and real-time support.

## Content
### Definition and Positioning of ROS 2 Middleware
ROS 2 Middleware belongs to the **software platform** type. Its domains include: software middleware, design engineering. Value chain level: intelligence layer, midstream. It is a de facto standard robot middleware based on DDS publish/subscribe and real-time support. Its English name is *ROS 2 Middleware*. Its Korean name is *ROS 2 미들웨어*.

### Working Principle and Technical Architecture of ROS 2 Middleware
The core mechanism of ROS 2 Middleware determines its performance boundaries in humanoid robot systems. Understanding its internal structure, signal flow, and control interfaces facilitates system integration and optimization.
During the selection and integration process, attention must be paid to its compatibility with controllers, communication buses, power systems, and mechanical structures.

### Key Parameters and Selection Criteria
In engineering practice, selecting ROS 2 Middleware requires comprehensive consideration of performance indicators, reliability, cost, supply chain maturity, and compatibility with the overall system.
Key parameters typically include precision, bandwidth, torque, power consumption, weight, interface protocols, and environmental adaptability.
For different application scenarios, trade-offs between performance and cost may be necessary, with appropriate redundancy and safety margins reserved.

### Typical Applications and Development Trends
ROS 2 Middleware has been widely used in prototype validation, academic research, and early commercial products of humanoid robots.
As the industry chain matures in the future, its integration level, intelligence, and cost-effectiveness are expected to continue improving.

### Related Tags
- dds
- middleware
- real_time
- ros2
- software_platform

### Role in Humanoid Robot Systems
As one of the key software platforms in the humanoid robot industry chain, ROS 2 Middleware plays an important role in system design, performance optimization, and industrial application. It interacts with multiple subsystems such as perception, decision-making, actuation, energy, structure, and validation, collectively determining overall system performance. Related research and applications are continuously advancing to further enhance its reliability, efficiency, and cost-effectiveness in real-world scenarios.

## 개요
DDS 기반의 발행/구독 및 실시간 지원을 제공하는 사실상 표준 로봇 미들웨어입니다.

## 핵심 내용
### ROS 2 미들웨어의 정의와 위치
ROS 2 미들웨어는 **소프트웨어 플랫폼** 유형에 속합니다. 관련 분야는 소프트웨어 미들웨어, 설계 공학입니다. 가치 사슬 계층은 지능 계층, 미드스트림입니다. DDS 기반의 발행/구독 및 실시간 지원을 제공하는 사실상 표준 로봇 미들웨어입니다. 영문 명칭은 *ROS 2 Middleware*입니다. 한글 명칭은 *ROS 2 미들웨어*입니다.

### ROS 2 미들웨어의 작동 원리와 기술 아키텍처
ROS 2 미들웨어의 핵심 메커니즘은 휴머노이드 로봇 시스템에서의 성능 경계를 결정합니다. 내부 구조, 신호 흐름 및 제어 인터페이스를 이해하면 시스템 통합 및 최적화에 도움이 됩니다.
선정 및 통합 과정에서는 컨트롤러, 통신 버스, 전원 시스템 및 기계 구조와의 호환성을 고려해야 합니다.

### 주요 파라미터 및 선정 포인트
공학 실무에서 ROS 2 미들웨어를 선택할 때는 성능 지표, 신뢰성, 비용, 공급망 성숙도 및 전체 시스템과의 호환성을 종합적으로 고려해야 합니다.
주요 파라미터에는 일반적으로 정밀도, 대역폭, 토크, 소비 전력, 무게, 인터페이스 프로토콜 및 환경 적응성 등이 포함됩니다.
다양한 응용 시나리오에 따라 성능과 비용 간의 균형을 맞추고 적절한 여유와 안전 마진을 확보해야 할 수 있습니다.

### 대표적인 응용 및 발전 동향
ROS 2 미들웨어는 휴머노이드 로봇의 프로토타입 검증, 학술 연구 및 초기 상용 제품에 널리 사용되고 있습니다.
향후 산업 체인이 성숙해짐에 따라 통합도, 지능화 수준 및 비용 효율성이 지속적으로 향상될 것으로 예상됩니다.

### 관련 태그
- dds
- middleware
- real_time
- ros2
- software_platform

### 휴머노이드 로봇 시스템에서의 역할
휴머노이드 로봇 산업 체인의 핵심 소프트웨어 플랫폼 중 하나로서, ROS 2 미들웨어는 시스템 설계, 성능 최적화 및 산업화 응용에서 중요한 역할을 합니다. 이는 인식, 의사 결정, 실행, 에너지, 구조 및 검증 등 여러 하위 시스템과 상호 결합되어 전체 기계의 성능을 결정합니다. 관련 연구와 응용은 실제 시나리오에서의 신뢰성, 효율성 및 경제성을 더욱 향상시키기 위해 지속적으로 추진되고 있습니다.
