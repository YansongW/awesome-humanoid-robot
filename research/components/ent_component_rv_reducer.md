---
$id: ent_component_rv_reducer
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: RV Reducer
  zh: RV减速器
  ko: RV 감속기
summary:
  en: A high-rigidity, high-torque cycloidal reducer widely used in heavy-load robot joints, especially hips and waists, due
    to its excellent shock resistance and positioning accuracy.
  zh: 一种高刚性、高扭矩的摆线针轮减速器，抗冲击性与定位精度优异，常用于重载机器人臀、腰等关节。
  ko: 고강성·고토크 사이클로이드 감속기로, 충격 저항성과 위치 정밀도가 우수하여 중하량 로봇 관절에 널리 사용됨.
domains:
- 02_components
layers:
- midstream
functional_roles:
- knowledge
tags:
- component
- chapter_4
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-04.md#4.3.3 行星减速器与摆线减速器 by scripts/backfill_nonpaper_entries.py. Body backfilled from
    entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---

## 概述
一种高刚性、高扭矩的摆线针轮减速器，抗冲击性与定位精度优异，常用于重载机器人臀、腰等关节。

## 核心内容
### RV减速器的定义与定位
RV减速器属于 **零部件** 类型。 所属领域包括：零部件。 价值链层级：中游。 一种高刚性、高扭矩的摆线针轮减速器，抗冲击性与定位精度优异，常用于重载机器人臀、腰等关节。 英文名称为 *RV Reducer*。 韩文名称为 *RV 감속기*。

### RV减速器的工作原理与技术架构
RV减速器的核心机制决定了其在人形机器人系统中的性能边界。理解其内部结构、信号流与控制接口，有助于进行系统集成与优化。
在选型与集成过程中，需要关注其与控制器、通信总线、电源系统与机械结构的兼容性。

### 关键参数与选型要点
在工程实践中，选用RV减速器需要综合考虑性能指标、可靠性、成本、供应链成熟度以及与整机系统的兼容性。
关键参数通常包括精度、带宽、扭矩、功耗、重量、接口协议与环境适应性等。
针对不同应用场景，可能需要在性能与成本之间进行权衡，并预留适当的冗余与安全裕量。

### 典型应用与发展趋势
RV减速器已广泛应用于人形机器人的原型验证、学术研究与早期商业化产品中。
未来随着产业链成熟，其集成度、智能化水平与成本效益有望持续提升。

### 相关标签
- component
- chapter_4
- wiki_gap

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键零部件之一，RV减速器在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- Wiki extraction

## Overview
A high-rigidity, high-torque cycloidal pinwheel reducer with excellent impact resistance and positioning accuracy, commonly used in heavy-duty robot joints such as hips and waists.

## Content
### Definition and Positioning of RV Reducer
The RV reducer belongs to the **component** category. Its field includes: components. Value chain level: midstream. A high-rigidity, high-torque cycloidal pinwheel reducer with excellent impact resistance and positioning accuracy, commonly used in heavy-duty robot joints such as hips and waists. English name: *RV Reducer*. Korean name: *RV 감속기*.

### Working Principle and Technical Architecture of RV Reducer
The core mechanism of the RV reducer determines its performance boundaries in humanoid robot systems. Understanding its internal structure, signal flow, and control interfaces facilitates system integration and optimization.
During selection and integration, attention must be paid to its compatibility with controllers, communication buses, power systems, and mechanical structures.

### Key Parameters and Selection Considerations
In engineering practice, selecting an RV reducer requires comprehensive consideration of performance indicators, reliability, cost, supply chain maturity, and compatibility with the overall system.
Key parameters typically include precision, bandwidth, torque, power consumption, weight, interface protocols, and environmental adaptability.
For different application scenarios, trade-offs between performance and cost may be necessary, with appropriate redundancy and safety margins reserved.

### Typical Applications and Development Trends
RV reducers are widely used in prototype validation, academic research, and early commercial products of humanoid robots.
As the industry chain matures, their integration level, intelligence, and cost-effectiveness are expected to continue improving.

### Related Tags
- component
- chapter_4
- wiki_gap

### Role in Humanoid Robot Systems
As one of the key components in the humanoid robot industry chain, the RV reducer plays an important role in system design, performance optimization, and industrial application. It interacts with multiple subsystems such as perception, decision-making, actuation, energy, structure, and validation, collectively determining overall machine performance. Related research and applications are continuously advancing to further enhance its reliability, efficiency, and cost-effectiveness in practical scenarios.

## 개요
고강성, 고토크의 사이클로이드 감속기로 내충격성과 위치 정밀도가 우수하며, 중하중 로봇의 엉덩이, 허리 등 관절에 자주 사용됩니다.

## 핵심 내용
### RV 감속기의 정의와 위치
RV 감속기는 **부품** 유형에 속합니다. 소속 분야는 부품입니다. 가치 사슬 계층: 중류. 고강성, 고토크의 사이클로이드 감속기로 내충격성과 위치 정밀도가 우수하며, 중하중 로봇의 엉덩이, 허리 등 관절에 자주 사용됩니다. 영문 명칭은 *RV Reducer*입니다. 한글 명칭은 *RV 감속기*입니다.

### RV 감속기의 작동 원리와 기술 아키텍처
RV 감속기의 핵심 메커니즘은 인간형 로봇 시스템에서의 성능 경계를 결정합니다. 내부 구조, 신호 흐름 및 제어 인터페이스를 이해하면 시스템 통합 및 최적화에 도움이 됩니다.
선정 및 통합 과정에서는 컨트롤러, 통신 버스, 전원 시스템 및 기계 구조와의 호환성을 고려해야 합니다.

### 주요 파라미터와 선정 포인트
공학 실무에서 RV 감속기를 선택할 때는 성능 지표, 신뢰성, 비용, 공급망 성숙도 및 전체 시스템과의 호환성을 종합적으로 고려해야 합니다.
주요 파라미터에는 일반적으로 정밀도, 대역폭, 토크, 소비 전력, 무게, 인터페이스 프로토콜 및 환경 적응성 등이 포함됩니다.
다양한 응용 시나리오에 따라 성능과 비용 간의 균형을 맞추고 적절한 여유와 안전 마진을 확보해야 할 수 있습니다.

### 대표적인 응용과 발전 동향
RV 감속기는 이미 인간형 로봇의 프로토타입 검증, 학술 연구 및 초기 상용화 제품에 널리 사용되고 있습니다.
향후 산업 체인이 성숙해짐에 따라 집적도, 지능화 수준 및 비용 효율성이 지속적으로 향상될 것으로 기대됩니다.

### 관련 태그
- component
- chapter_4
- wiki_gap

### 인간형 로봇 시스템에서의 역할
인간형 로봇 산업 체인의 핵심 부품 중 하나로서 RV 감속기는 시스템 설계, 성능 최적화 및 산업화 응용에서 중요한 역할을 합니다. 이는 인식, 의사 결정, 실행, 에너지, 구조 및 검증 등 여러 하위 시스템과 상호 결합되어 전체 기계 성능을 결정합니다. 관련 연구와 응용은 실제 시나리오에서의 신뢰성, 효율성 및 경제성을 더욱 향상시키기 위해 지속적으로 추진되고 있습니다.
