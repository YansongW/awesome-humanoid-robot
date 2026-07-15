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
  zh: '核心内容 ### 关节编码器的定义与定位 关节编码器属于 **component** 类型。 所属领域包括：02_components。 价值链层级：upstream。 安装于机器人关节的位置或速度传感器，为电机控制提供高分辨率反馈。
    英文名称为 *Joint Encoder*。 韩文名称为 *관절 엔코더*。'
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
关节编码器属于 **component** 类型。 所属领域包括：02_components。 价值链层级：upstream。 安装于机器人关节的位置或速度传感器，为电机控制提供高分辨率反馈。 英文名称为 *Joint Encoder*。 韩文名称为 *관절 엔코더*。

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
作为人形机器人产业链中的关键component之一，关节编码器在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Rotary Encoder](https://en.wikipedia.org/wiki/Rotary_encoder)


