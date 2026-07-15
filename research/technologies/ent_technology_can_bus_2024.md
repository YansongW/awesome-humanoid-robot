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
CAN 总线属于 **technology** 类型。 所属领域包括：08_software_middleware, 06_design_engineering。 价值链层级：intelligence, midstream。 连接人形机器人关节电机驱动与中央控制器的现场总线。 英文名称为 *CAN Bus*。 韩文名称为 *CAN Bus*。

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
作为人形机器人产业链中的关键technology之一，CAN 总线在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [CAN Bus](https://en.wikipedia.org/wiki/CAN_bus)

