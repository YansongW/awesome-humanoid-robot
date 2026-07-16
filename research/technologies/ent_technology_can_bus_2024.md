---
$id: ent_technology_can_bus_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: technology
names:
  en: CAN Bus
  zh: CAN 总线
  ko: CAN Bus
summary:
  en: Field bus connecting joint motor drives to the central controller in humanoid robots.
  zh: 连接人形机器人关节电机驱动与中央控制器的现场总线。
  ko: 휨로봇 관절 모터 드라이브와 중앙 제어기를 연결하는 필드 버스.
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
- bus
- can
- communication
- real_time
- technology
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
  title: CAN Bus
  url: https://en.wikipedia.org/wiki/CAN_bus
  date: '2024'
  accessed_at: '2026-07-02'
---

## 概述
连接人形机器人关节电机驱动与中央控制器的现场总线。

## 核心内容
### CAN 总线的定义与定位
CAN 总线属于 **技术** 类型。 所属领域包括：软件中间件, 设计工程。 价值链层级：智能层, midstream。 连接人形机器人关节电机驱动与中央控制器的现场总线。 英文名称为 *CAN Bus*。 韩文名称为 *CAN Bus*。

### CAN 总线的工作原理与技术架构
CAN 总线的核心机制决定了其在人形机器人系统中的性能边界。理解其内部结构、信号流与控制接口，有助于进行系统集成与优化。
在选型与集成过程中，需要关注其与控制器、通信总线、电源系统与机械结构的兼容性。

### 关键参数与选型要点
在工程实践中，选用CAN 总线需要综合考虑性能指标、可靠性、成本、供应链成熟度以及与整机系统的兼容性。
关键参数通常包括精度、带宽、扭矩、功耗、重量、接口协议与环境适应性等。
针对不同应用场景，可能需要在性能与成本之间进行权衡，并预留适当的冗余与安全裕量。

### 典型应用与发展趋势
CAN 总线已广泛应用于人形机器人的原型验证、学术研究与早期商业化产品中。
未来随着产业链成熟，其集成度、智能化水平与成本效益有望持续提升。

### 相关标签
- bus
- can
- communication
- real_time
- technology

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键技术之一，CAN 总线在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [CAN Bus](https://en.wikipedia.org/wiki/CAN_bus)

## Overview
A fieldbus connecting the joint motor drives of a humanoid robot to the central controller.

## Content
### Definition and Positioning of CAN Bus
CAN Bus belongs to the **technology** type. Its domains include: software middleware, design engineering. Value chain level: intelligent layer, midstream. It is a fieldbus connecting the joint motor drives of a humanoid robot to the central controller. The English name is *CAN Bus*. The Korean name is *CAN Bus*.

### Working Principle and Technical Architecture of CAN Bus
The core mechanism of CAN Bus determines its performance boundaries in humanoid robot systems. Understanding its internal structure, signal flow, and control interfaces aids in system integration and optimization.
During selection and integration, attention must be paid to its compatibility with controllers, communication buses, power systems, and mechanical structures.

### Key Parameters and Selection Points
In engineering practice, selecting CAN Bus requires comprehensive consideration of performance indicators, reliability, cost, supply chain maturity, and compatibility with the overall system.
Key parameters typically include precision, bandwidth, torque, power consumption, weight, interface protocols, and environmental adaptability.
For different application scenarios, trade-offs between performance and cost may be necessary, with appropriate redundancy and safety margins reserved.

### Typical Applications and Development Trends
CAN Bus has been widely used in prototype validation, academic research, and early commercial products of humanoid robots.
As the industry chain matures in the future, its integration level, intelligence, and cost-effectiveness are expected to continue improving.

### Related Tags
- bus
- can
- communication
- real_time
- technology

### Role in Humanoid Robot Systems
As one of the key technologies in the humanoid robot industry chain, CAN Bus plays an important role in system design, performance optimization, and industrial application. It couples with multiple subsystems such as perception, decision-making, actuation, energy, structure, and validation, collectively determining overall machine performance. Related research and applications are continuously advancing to further enhance its reliability, efficiency, and economy in practical scenarios.

## 개요
휴머노이드 로봇 관절 모터 드라이버와 중앙 제어기를 연결하는 필드버스.

## 핵심 내용
### CAN 버스의 정의와 위치
CAN 버스는 **기술** 유형에 속합니다. 관련 분야는 소프트웨어 미들웨어, 설계 공학입니다. 가치 사슬 계층: 지능 계층, 미드스트림. 휴머노이드 로봇 관절 모터 드라이버와 중앙 제어기를 연결하는 필드버스. 영문 명칭은 *CAN Bus*입니다. 한글 명칭은 *CAN Bus*입니다.

### CAN 버스의 작동 원리와 기술 아키텍처
CAN 버스의 핵심 메커니즘은 휴머노이드 로봇 시스템에서의 성능 한계를 결정합니다. 내부 구조, 신호 흐름 및 제어 인터페이스를 이해하면 시스템 통합 및 최적화에 도움이 됩니다.
선정 및 통합 과정에서는 컨트롤러, 통신 버스, 전원 시스템 및 기계 구조와의 호환성을 고려해야 합니다.

### 주요 매개변수 및 선정 포인트
공학 실무에서 CAN 버스를 선택할 때는 성능 지표, 신뢰성, 비용, 공급망 성숙도 및 전체 시스템과의 호환성을 종합적으로 고려해야 합니다.
주요 매개변수에는 일반적으로 정밀도, 대역폭, 토크, 전력 소비, 무게, 인터페이스 프로토콜 및 환경 적응성 등이 포함됩니다.
다양한 응용 시나리오에 따라 성능과 비용 간의 균형을 맞추고 적절한 여유와 안전 마진을 확보해야 할 수 있습니다.

### 대표적인 응용 및 발전 동향
CAN 버스는 휴머노이드 로봇의 프로토타입 검증, 학술 연구 및 초기 상용 제품에 널리 사용되고 있습니다.
향후 산업 체인이 성숙해짐에 따라 집적도, 지능화 수준 및 비용 효율성이 지속적으로 향상될 것으로 예상됩니다.

### 관련 태그
- bus
- can
- communication
- real_time
- technology

### 휴머노이드 로봇 시스템에서의 역할
휴머노이드 로봇 산업 체인의 핵심 기술 중 하나로서 CAN 버스는 시스템 설계, 성능 최적화 및 산업화 응용에서 중요한 역할을 합니다. 이는 인식, 의사 결정, 실행, 에너지, 구조 및 검증 등 여러 하위 시스템과 상호 결합되어 전체 기계 성능을 결정합니다. 관련 연구 및 응용은 실제 시나리오에서의 신뢰성, 효율성 및 경제성을 더욱 향상시키기 위해 지속적으로 추진되고 있습니다.
