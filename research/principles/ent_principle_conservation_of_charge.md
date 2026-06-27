---
$id: ent_principle_conservation_of_charge
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: principle
names:
  en: Conservation of Charge
  zh: 电荷守恒
  ko: 전하 보존
summary:
  en: A fundamental principle stating that electric charge cannot be created or destroyed,
    only redistributed; it underlies Kirchhoff's current law and charge-balance equations
    in electrochemical systems.
  zh: 电荷既不能被创造也不能被消灭、只能重新分布的基本原理；它是基尔霍夫电流定律和电化学系统电荷平衡方程的基础。
  ko: 전하는 생성되거나 소멸될 수 없고 재분배될 뿐이라는 기본 원리이며, 키르히호프 전류 법칙과 전기화학 시스템의 전하 평형 방정식의 기초가 된다.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
tags:
- conservation_of_charge
- kirchhoff_current_law
- electrochemistry
- battery_model
- humanoid_robot
theoretical_depth:
- principle
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Fundamental conservation law; standard in physics and electrochemistry.
sources:
- id: src_halliday_resnick_2014
  type: paper
  title: 'Halliday, Resnick & Walker, Fundamentals of Physics, 10th ed.'
  url: https://www.wiley.com/en-us/Fundamentals+of+Physics%2C+10th+Edition-p-9781118230730
  date: '2014-01-01'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_foundation_electrochemistry
  relationship: has_prerequisite
  description:
    en: Conservation of charge is formalized within electrochemical theory through ionic and electronic transport balances.
    zh: 电荷守恒在电化学理论中通过离子和电子传输平衡被形式化。
    ko: 전하 보존은 이온 및 전자 전송 평형을 통해 전기화학 이론 내에서 형식화된다.
---

## 抽象

> **生活实例**：想象一个封闭房间里有固定数量的人。他们可以从一边走到另一边，也可以挤在一起，但总人数不会变。电荷守恒就是说，电荷就像这些人——只能移动，不能凭空出现或消失。
>
> **自然语言逻辑**：在任何孤立系统或电路节点中，总电荷量保持不变。流入节点的电流之和等于流出节点的电流之和，这就是基尔霍夫电流定律；在电池中，它保证锂离子在正负极之间迁移时，电荷始终平衡。

## Overview

The principle of conservation of charge is a cornerstone of electromagnetism and electrochemistry. It states that for any closed system, the total electric charge is constant over time. In circuit theory, this principle is embodied by Kirchhoff's current law: the algebraic sum of currents entering any node is zero. In battery modeling, charge conservation links the current flowing through the external circuit to the rate of change of stored charge and to the flux of lithium ions between electrodes.

## Key Characteristics

- Charge is a conserved scalar quantity in classical electromagnetism.
- Kirchhoff's current law is the lumped-circuit expression of charge conservation.
- In electrochemical systems, charge conservation couples electronic current in conductors to ionic current in electrolytes.
- The state-of-charge of a battery is computed by integrating current while respecting charge balance.

## Relevance to Humanoid Robotics

For humanoid robots, charge conservation is the reason why state-of-charge estimation via current integration (coulomb counting) works. It also constrains how quickly current can be drawn without violating electrochemical balances that accelerate degradation. Understanding this principle helps engineers design BMS algorithms that keep the battery within safe charge-throughput limits during highly dynamic motions.
