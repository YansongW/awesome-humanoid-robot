---
$id: ent_component_rotary_actuator_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Rotary Actuator
  zh: 旋转执行器
  ko: Rotary Actuator
summary:
  en: Actuator producing rotational motion, typically composed of frameless torque motor, harmonic reducer, encoder and torque
    sensor.
  zh: 产生旋转运动的执行器，通常由无框力矩电机、谐波减速器、编码器和力矩传感器组成。
  ko: 회전 운 동을 생성하는 액추에이터, 일반적으로 프레임리스 토크 모터, 하모닉 감속기, 인코더 및 토크 센서로 구성.
domains:
- 02_components
layers:
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- component
- harmonic_reducer
- joint
- rotary_actuator
- torque_motor
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: Imported via ingestion framework from source_type=website. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_001
  type: website
  title: Rotary Actuator
  url: https://en.wikipedia.org/wiki/Actuator
  date: '2024'
  accessed_at: '2026-07-01'
---

## 概述
产生旋转运动的执行器，通常由无框力矩电机、谐波减速器、编码器和力矩传感器组成。

## 核心内容
### 旋转执行器的定义与定位
旋转执行器属于 **零部件** 类型。 所属领域包括：零部件。 价值链层级：上游。 产生旋转运动的执行器，通常由无框力矩电机、谐波减速器、编码器和力矩传感器组成。 英文名称为 *Rotary Actuator*。 韩文名称为 *Rotary Actuator*。

### 旋转执行器的工作原理与技术架构
旋转执行器的核心机制决定了其在人形机器人系统中的性能边界。理解其内部结构、信号流与控制接口，有助于进行系统集成与优化。
在选型与集成过程中，需要关注其与控制器、通信总线、电源系统与机械结构的兼容性。

### 关键参数与选型要点
在工程实践中，选用旋转执行器需要综合考虑性能指标、可靠性、成本、供应链成熟度以及与整机系统的兼容性。
关键参数通常包括精度、带宽、扭矩、功耗、重量、接口协议与环境适应性等。
针对不同应用场景，可能需要在性能与成本之间进行权衡，并预留适当的冗余与安全裕量。

### 典型应用与发展趋势
旋转执行器已广泛应用于人形机器人的原型验证、学术研究与早期商业化产品中。
未来随着产业链成熟，其集成度、智能化水平与成本效益有望持续提升。

### 相关标签
- component
- harmonic_reducer
- joint
- rotary_actuator
- torque_motor

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键零部件之一，旋转执行器在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Rotary Actuator](https://en.wikipedia.org/wiki/Actuator)

## Overview
An actuator that generates rotary motion, typically composed of a frameless torque motor, harmonic reducer, encoder, and torque sensor.

## Content
### Definition and Positioning of Rotary Actuators
Rotary actuators fall under the **component** category. Their domain includes: components. Value chain level: upstream. An actuator that generates rotary motion, typically composed of a frameless torque motor, harmonic reducer, encoder, and torque sensor. The English name is *Rotary Actuator*. The Korean name is *Rotary Actuator*.

### Working Principle and Technical Architecture of Rotary Actuators
The core mechanism of a rotary actuator determines the performance boundaries within a humanoid robot system. Understanding its internal structure, signal flow, and control interface facilitates system integration and optimization.
During selection and integration, attention must be paid to compatibility with the controller, communication bus, power system, and mechanical structure.

### Key Parameters and Selection Considerations
In engineering practice, selecting a rotary actuator requires comprehensive consideration of performance indicators, reliability, cost, supply chain maturity, and compatibility with the overall system.
Key parameters typically include precision, bandwidth, torque, power consumption, weight, interface protocol, and environmental adaptability.
For different application scenarios, trade-offs between performance and cost may be necessary, with appropriate redundancy and safety margins reserved.

### Typical Applications and Development Trends
Rotary actuators have been widely used in prototype validation, academic research, and early commercial products of humanoid robots.
In the future, as the industry chain matures, their integration level, intelligence, and cost-effectiveness are expected to continue improving.

### Related Tags
- component
- harmonic_reducer
- joint
- rotary_actuator
- torque_motor

### Role in Humanoid Robot Systems
As one of the key components in the humanoid robot industry chain, rotary actuators play an important role in system design, performance optimization, and industrial application. They interact with multiple subsystems such as perception, decision-making, actuation, energy, structure, and validation, collectively determining overall machine performance. Related research and applications are ongoing to further enhance their reliability, efficiency, and cost-effectiveness in real-world scenarios.

## 개요
회전 운동을 생성하는 액추에이터는 일반적으로 프레임리스 토크 모터, 하모닉 감속기, 엔코더 및 토크 센서로 구성됩니다.

## 핵심 내용
### 회전 액추에이터의 정의와 위치
회전 액추에이터는 **부품** 유형에 속합니다. 소속 분야는 부품입니다. 가치 사슬 계층: 상류. 회전 운동을 생성하는 액추에이터는 일반적으로 프레임리스 토크 모터, 하모닉 감속기, 엔코더 및 토크 센서로 구성됩니다. 영어 명칭은 *Rotary Actuator*입니다. 한국어 명칭은 *Rotary Actuator*입니다.

### 회전 액추에이터의 작동 원리와 기술 아키텍처
회전 액추에이터의 핵심 메커니즘은 휴머노이드 로봇 시스템에서의 성능 경계를 결정합니다. 내부 구조, 신호 흐름 및 제어 인터페이스를 이해하면 시스템 통합 및 최적화에 도움이 됩니다.
선정 및 통합 과정에서는 컨트롤러, 통신 버스, 전원 시스템 및 기계 구조와의 호환성을 고려해야 합니다.

### 주요 파라미터와 선정 포인트
공학 실무에서 회전 액추에이터를 선택할 때는 성능 지표, 신뢰성, 비용, 공급망 성숙도 및 전체 시스템과의 호환성을 종합적으로 고려해야 합니다.
주요 파라미터에는 일반적으로 정밀도, 대역폭, 토크, 전력 소비, 무게, 인터페이스 프로토콜 및 환경 적응성 등이 포함됩니다.
다양한 응용 시나리오에 따라 성능과 비용 사이에서 균형을 맞추고 적절한 여유와 안전 마진을 확보해야 할 수 있습니다.

### 대표적인 응용과 발전 추세
회전 액추에이터는 이미 휴머노이드 로봇의 프로토타입 검증, 학술 연구 및 초기 상용 제품에 널리 사용되고 있습니다.
향후 산업 체인이 성숙해짐에 따라 집적도, 지능화 수준 및 비용 효율성이 지속적으로 향상될 것으로 예상됩니다.

### 관련 태그
- component
- harmonic_reducer
- joint
- rotary_actuator
- torque_motor

### 휴머노이드 로봇 시스템에서의 역할
휴머노이드 로봇 산업 체인의 핵심 부품 중 하나로서, 회전 액추에이터는 시스템 설계, 성능 최적화 및 산업화 응용에서 중요한 역할을 합니다. 이는 인식, 의사 결정, 실행, 에너지, 구조 및 검증 등 여러 하위 시스템과 상호 결합되어 전체 기계의 성능을 결정합니다. 관련 연구와 응용은 실제 시나리오에서의 신뢰성, 효율성 및 경제성을 더욱 향상시키기 위해 지속적으로 추진되고 있습니다.
