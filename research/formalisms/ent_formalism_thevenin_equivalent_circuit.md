---
$id: ent_formalism_thevenin_equivalent_circuit
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: formalism
names:
  en: Thevenin Equivalent Circuit
  zh: Thevenin 等效电路
  ko: 테베닌 등가 회로
summary:
  en: A formalism that replaces any linear electrical network, viewed from two terminals,
    by an equivalent ideal voltage source in series with an equivalent resistance.
  zh: 一种形式化方法，将任意线性电网络从两个端子看进去替换为一个等效理想电压源串联一个等效电阻。
  ko: 두 단자에서 바라본 임의의 선형 전기 네트워크를 등가 이상 전압원과 등가 저항의 직렬 연결로 대체하는 형식화이다.
domains:
- 00_foundations
- 06_design_engineering
layers:
- foundations
- midstream
functional_roles:
- knowledge
tags:
- thevenin
- equivalent_circuit
- linear_network
- battery_model
- humanoid_robot
theoretical_depth:
- formalism
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Standard circuit-theory formalism; widely applied to battery modeling.
sources:
- id: src_dorf_svoboda_2017
  type: paper
  title: 'Dorf & Svoboda, Introduction to Electric Circuits, 9th ed.'
  url: https://www.wiley.com/en-us/Introduction+to+Electric+Circuits%2C+9th+Edition-p-9781118931897
  date: '2017-01-01'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_equation_thevenin_terminal_voltage
  relationship: includes
  description:
    en: The formalism includes the terminal-voltage equation derived from the equivalent circuit.
    zh: 该形式化包含由等效电路推导出的端电压方程。
    ko: 형식화는 등가 회로에서 유도된 단자 전압 방정식을 포함한다.
---

## 抽象

> **生活实例**：你家里有一个装满各种电器的配电箱，但你只关心墙上的插座能不能带动空调。Thevenin 等效电路告诉你：不管配电箱里多复杂，从插座看进去，它都可以被简化为“一个电源加一个内阻”。
>
> **自然语言逻辑**：对于线性电阻网络，外部负载只关心端口电压-电流关系。Thevenin 定理证明，任何这样的网络都可以等效为一个电压源与电阻的串联；开路电压等于等效电压源，短路电流与开路电压之比等于等效电阻。

## Overview

The Thevenin equivalent-circuit formalism states that any linear electrical network containing only voltage sources, current sources, and resistances, viewed from a pair of terminals, can be replaced by an equivalent circuit consisting of an independent voltage source $V_{\text{th}}$ in series with a resistance $R_{\text{th}}$. The equivalent voltage is the open-circuit voltage at the terminals, and the equivalent resistance is the resistance seen from the terminals when all independent sources are turned off.

## Key Characteristics

- Applies to linear, time-invariant networks.
- Preserves the terminal voltage-current relationship of the original network.
- Thevenin voltage equals the open-circuit terminal voltage.
- Thevenin resistance equals the equivalent resistance looking into the terminals with independent sources deactivated.
- Forms the basis for first-order and higher-order equivalent-circuit battery models.

## Relevance to Humanoid Robotics

In humanoid robots, the battery pack is a complex network of cells, interconnects, and protection circuits. The Thevenin formalism lets engineers reduce this network to a simple source-resistance model for controller design and BMS estimation, enabling real-time prediction of voltage sag and available power without simulating every cell.
