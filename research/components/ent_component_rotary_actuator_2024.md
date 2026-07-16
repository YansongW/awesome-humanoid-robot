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


