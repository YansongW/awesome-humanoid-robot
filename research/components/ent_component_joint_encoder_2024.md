---
$id: ent_component_joint_encoder_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Joint Encoder
  zh: 关节编码器
  ko: 관절 엔코더
summary:
  en: Position or velocity sensor mounted on a robot joint to provide high-resolution feedback for motor control.
  zh: 安装于机器人关节的位置或速度传感器，为电机控制提供高分辨率反馈。
  ko: 모터 제어를 위해 고해상도 피드백을 제공하기 위해 로봇 관절에 장착된 위치 또는 속도 센서.
domains:
- 02_components
layers:
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- component
- sensor
- encoder
- joint
- motor_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-13'
  confidence: medium
  notes: Stub entity created during wiki-chapter-mapping repair; body under construction. Body backfilled from entity metadata
    by scripts/backfill_critical_entities.py.
sources:
- id: src_001
  type: website
  title: Rotary Encoder
  url: https://en.wikipedia.org/wiki/Rotary_encoder
  date: '2024'
  accessed_at: '2026-07-13'
---

## 概述
安装于机器人关节的位置或速度传感器，为电机控制提供高分辨率反馈。

## 核心内容
### 关节编码器的定义与定位
关节编码器属于 **零部件** 类型。 所属领域包括：零部件。 价值链层级：上游。 安装于机器人关节的位置或速度传感器，为电机控制提供高分辨率反馈。 英文名称为 *Joint Encoder*。 韩文名称为 *관절 엔코더*。

### 关节编码器的工作原理与技术架构
关节编码器的核心机制决定了其在人形机器人系统中的性能边界。理解其内部结构、信号流与控制接口，有助于进行系统集成与优化。
在选型与集成过程中，需要关注其与控制器、通信总线、电源系统与机械结构的兼容性。

### 关键参数与选型要点
在工程实践中，选用关节编码器需要综合考虑性能指标、可靠性、成本、供应链成熟度以及与整机系统的兼容性。
关键参数通常包括精度、带宽、扭矩、功耗、重量、接口协议与环境适应性等。
针对不同应用场景，可能需要在性能与成本之间进行权衡，并预留适当的冗余与安全裕量。

### 典型应用与发展趋势
关节编码器已广泛应用于人形机器人的原型验证、学术研究与早期商业化产品中。
未来随着产业链成熟，其集成度、智能化水平与成本效益有望持续提升。

### 相关标签
- component
- sensor
- encoder
- joint
- motor_control

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键零部件之一，关节编码器在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Rotary Encoder](https://en.wikipedia.org/wiki/Rotary_encoder)

## Overview
Position or velocity sensors installed in robot joints provide high-resolution feedback for motor control.

## Content
### Definition and Positioning of Joint Encoders
Joint encoders belong to the **component** category. Their domain includes components. Value chain level: upstream. Position or velocity sensors installed in robot joints provide high-resolution feedback for motor control. The English term is *Joint Encoder*. The Korean term is *관절 엔코더*.

### Working Principle and Technical Architecture of Joint Encoders
The core mechanism of joint encoders determines the performance boundaries within a humanoid robot system. Understanding their internal structure, signal flow, and control interfaces facilitates system integration and optimization.
During selection and integration, attention must be paid to compatibility with controllers, communication buses, power systems, and mechanical structures.

### Key Parameters and Selection Criteria
In engineering practice, selecting joint encoders requires comprehensive consideration of performance indicators, reliability, cost, supply chain maturity, and compatibility with the overall system.
Key parameters typically include accuracy, bandwidth, torque, power consumption, weight, interface protocols, and environmental adaptability.
For different application scenarios, trade-offs between performance and cost may be necessary, with appropriate redundancy and safety margins reserved.

### Typical Applications and Development Trends
Joint encoders have been widely used in prototype validation, academic research, and early commercial products of humanoid robots.
In the future, as the industry chain matures, their integration level, intelligence, and cost-effectiveness are expected to continue improving.

### Related Tags
- component
- sensor
- encoder
- joint
- motor_control

### Role in Humanoid Robot Systems
As one of the key components in the humanoid robot industry chain, joint encoders play an important role in system design, performance optimization, and industrial application. They interact with multiple subsystems such as perception, decision-making, actuation, energy, structure, and validation, collectively determining overall machine performance. Related research and applications are ongoing to further enhance their reliability, efficiency, and cost-effectiveness in real-world scenarios.

## 개요
로봇 관절에 장착된 위치 또는 속도 센서로, 모터 제어에 고해상도 피드백을 제공합니다.

## 핵심 내용
### 관절 엔코더의 정의와 위치
관절 엔코더는 **부품** 유형에 속합니다. 소속 분야는 부품입니다. 가치 사슬 계층: 상류. 로봇 관절에 장착된 위치 또는 속도 센서로, 모터 제어에 고해상도 피드백을 제공합니다. 영문 명칭은 *Joint Encoder*입니다. 한글 명칭은 *관절 엔코더*입니다.

### 관절 엔코더의 작동 원리와 기술 아키텍처
관절 엔코더의 핵심 메커니즘은 휴머노이드 로봇 시스템에서의 성능 경계를 결정합니다. 내부 구조, 신호 흐름 및 제어 인터페이스를 이해하면 시스템 통합 및 최적화에 도움이 됩니다.
선정 및 통합 과정에서는 컨트롤러, 통신 버스, 전원 시스템 및 기계 구조와의 호환성을 고려해야 합니다.

### 주요 파라미터와 선정 포인트
공학 실무에서 관절 엔코더를 선정할 때는 성능 지표, 신뢰성, 비용, 공급망 성숙도 및 전체 시스템과의 호환성을 종합적으로 고려해야 합니다.
주요 파라미터에는 일반적으로 정밀도, 대역폭, 토크, 소비 전력, 무게, 인터페이스 프로토콜 및 환경 적응성 등이 포함됩니다.
다양한 응용 시나리오에 따라 성능과 비용 사이에서 균형을 맞추고 적절한 여유와 안전 마진을 확보해야 할 수 있습니다.

### 대표적인 응용과 발전 동향
관절 엔코더는 휴머노이드 로봇의 프로토타입 검증, 학술 연구 및 초기 상용화 제품에 널리 사용되고 있습니다.
향후 공급망이 성숙해짐에 따라 집적도, 지능화 수준 및 비용 효율성이 지속적으로 향상될 것으로 기대됩니다.

### 관련 태그
- component
- sensor
- encoder
- joint
- motor_control

### 휴머노이드 로봇 시스템에서의 역할
휴머노이드 로봇 공급망의 핵심 부품 중 하나로서 관절 엔코더는 시스템 설계, 성능 최적화 및 산업화 응용에서 중요한 역할을 합니다. 이는 인식, 의사 결정, 실행, 에너지, 구조 및 검증 등 여러 하위 시스템과 상호 결합되어 전체 기계의 성능을 결정합니다. 관련 연구와 응용은 실제 시나리오에서의 신뢰성, 효율성 및 경제성을 더욱 향상시키기 위해 지속적으로 추진되고 있습니다.
