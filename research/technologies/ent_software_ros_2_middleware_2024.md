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
  zh: '核心内容 ### ROS 2 中间件的定义与定位 ROS 2 中间件属于 **software_platform** 类型。 所属领域包括：08_software_middleware, 06_design_engineering。
    价值链层级：intelligence, midstream。 基于DDS的发布/订阅和实时支持的事实标准机器人中间件。 英文名称为 *ROS 2 Middleware*。 韩文名称为 *ROS 2 미들웨어*。'
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
ROS 2 中间件属于 **software_platform** 类型。 所属领域包括：08_software_middleware, 06_design_engineering。 价值链层级：intelligence, midstream。 基于DDS的发布/订阅和实时支持的事实标准机器人中间件。 英文名称为 *ROS 2 Middleware*。 韩文名称为 *ROS 2 미들웨어*。

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
作为人形机器人产业链中的关键software_platform之一，ROS 2 中间件在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [ROS 2 Middleware](https://www.ros.org/)


