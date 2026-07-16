---
$id: ent_mat_neodymium_magnet
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: material
names:
  en: Neodymium-Iron-Boron Magnet
  zh: 钕铁硼磁体
  ko: 네오디뮴 철 붕자석
summary:
  en: A high-performance rare-earth permanent magnet widely used in servo motors, electric vehicle motors, and high-precision
    actuators.
  zh: 一种高性能稀土永磁体，广泛用于伺服电机、电动汽车电机和高精度执行器。
  ko: 서보 모터, 전기차 모터 및 고정밀 액추에이터에 널리 사용되는 고성능 희토류 영구자석입니다.
domains:
- 01_raw_materials
layers:
- upstream
functional_roles:
- material
tags:
- rare_earth
- magnet
- motor
- actuator
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-16'
  confidence: high
  notes: Widely documented in motor teardown reports, supplier catalogs, and materials science literature. Body backfilled
    from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_mat_001
  type: report
  title: Rare Earth Magnets in Robotics and EV Motors
  url: https://example.com/rare-earth-robotics-report
  date: '2025-08-10'
  accessed_at: '2026-06-16'
related_entities:
- id: ent_comp_servo_motor
  relationship: supplies
  description:
    en: NdFeB magnets are supplied to high-performance servo motors.
    zh: 钕铁硼磁体供应给高性能伺服电机。
    ko: NdFeB 자석은 고성능 서보 모터에 공급됩니다.
theoretical_depth:
- system
---

## 概述
一种高性能稀土永磁体，广泛用于伺服电机、电动汽车电机和高精度执行器。

## 核心内容
### 钕铁硼磁体的定义与定位
钕铁硼磁体属于 **材料** 类型。 所属领域包括：原材料。 价值链层级：上游。 一种高性能稀土永磁体，广泛用于伺服电机、电动汽车电机和高精度执行器。 英文名称为 *Neodymium-Iron-Boron Magnet*。 韩文名称为 *네오디뮴 철 붕자석*。

### 钕铁硼磁体的关键维度
理解钕铁硼磁体需要从定义、边界条件、相关实体以及典型应用场景等多个维度展开，以形成系统性的认知。
该实体在人形机器人知识图谱中起到连接基础理论与工程实践的桥梁作用。

### 实践意义
在人形机器人产业化的背景下，钕铁硼磁体对于技术研究、产品开发、投资决策与生态建设均具有参考价值。
准确把握其内涵与外延，有助于避免概念混淆并推动跨学科协作。

### 研究与发展方向
随着人形机器人技术不断演进，钕铁硼磁体的相关理论与实践也将持续更新，需要保持跟踪与审校。

### 相关标签
- rare_earth
- magnet
- motor
- actuator

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键材料之一，钕铁硼磁体在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Rare Earth Magnets in Robotics and EV Motors](https://example.com/rare-earth-robotics-report)


