---
$id: ent_operator_voltage_divider
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: operator
names:
  en: Voltage Divider
  zh: 分压器
  ko: 전압 분배기
summary:
  en: A linear circuit operator that partitions a total voltage across a series of resistances in proportion to their resistance
    values.
  zh: 一种线性电路算子，按电阻值比例将总电压分配到串联电阻上。
  ko: 저항값에 비례하여 직렬 저항에 총 전압을 분배하는 선형 회로 연산자이다.
domains:
- 00_foundations
- 06_design_engineering
layers:
- foundations
- midstream
functional_roles:
- knowledge
tags:
- voltage_divider
- ohm_law
- circuit_theory
- battery_model
- humanoid_robot
theoretical_depth:
- formalism
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Direct consequence of Ohm's law and series current equality. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_dorf_svoboda_2017
  type: paper
  title: Dorf & Svoboda, Introduction to Electric Circuits, 9th ed.
  url: https://www.wiley.com/en-us/Introduction+to+Electric+Circuits%2C+9th+Edition-p-9781118931897
  date: '2017-01-01'
  accessed_at: '2026-06-26'
---

## 概述
一种线性电路算子，按电阻值比例将总电压分配到串联电阻上。

## 核心内容
### 分压器的定义与定位
分压器属于 **运营商** 类型。 所属领域包括：基础学科, 设计工程。 价值链层级：基础层, midstream。 一种线性电路算子，按电阻值比例将总电压分配到串联电阻上。 英文名称为 *Voltage Divider*。 韩文名称为 *전압 분배기*。

### 分压器的关键维度
理解分压器需要从定义、边界条件、相关实体以及典型应用场景等多个维度展开，以形成系统性的认知。
该实体在人形机器人知识图谱中起到连接基础理论与工程实践的桥梁作用。

### 实践意义
在人形机器人产业化的背景下，分压器对于技术研究、产品开发、投资决策与生态建设均具有参考价值。
准确把握其内涵与外延，有助于避免概念混淆并推动跨学科协作。

### 研究与发展方向
随着人形机器人技术不断演进，分压器的相关理论与实践也将持续更新，需要保持跟踪与审校。

### 相关标签
- voltage_divider
- ohm_law
- circuit_theory
- battery_model
- humanoid_robot

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键运营商之一，分压器在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Dorf & Svoboda, Introduction to Electric Circuits, 9th ed.](https://www.wiley.com/en-us/Introduction+to+Electric+Circuits%2C+9th+Edition-p-9781118931897)


