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
  en: A linear circuit operator that partitions a total voltage across a series of
    resistances in proportion to their resistance values.
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
  notes: Direct consequence of Ohm's law and series current equality.
sources:
- id: src_dorf_svoboda_2017
  type: paper
  title: 'Dorf & Svoboda, Introduction to Electric Circuits, 9th ed.'
  url: https://www.wiley.com/en-us/Introduction+to+Electric+Circuits%2C+9th+Edition-p-9781118931897
  date: '2017-01-01'
  accessed_at: '2026-06-26'
---

## 抽象

> **生活实例**：想象一块蛋糕要分给几个按体重比例排队的人，体重越大分到的越多。分压器就是这样：串联电阻越大，它“分走”的电压就越多。
>
> **自然语言逻辑**：在串联电路中，流过每个电阻的电流相同。根据欧姆定律 $V = IR$，电阻越大，电压降越大；总电压按各电阻占总电阻的比例分配。

## Overview

The voltage-divider operator expresses how a voltage is distributed across series-connected resistive elements. For two resistors $R_1$ and $R_2$ in series across a voltage source $V_s$, the voltage across $R_2$ is

$$
V_{R_2} = V_s \frac{R_2}{R_1 + R_2}.
$$

More generally, for $N$ series resistors, the voltage across resistor $R_i$ is

$$
V_{R_i} = V_s \frac{R_i}{\sum_{j=1}^{N} R_j}.
$$

## Key Characteristics

- Applies to linear, series-connected resistive networks.
- The output voltage is a fraction of the input voltage determined by the resistance ratio.
- Loading effects must be considered when the divider drives a finite impedance.
- Generalizes to impedances in the frequency domain for AC analysis.

## Relevance to Humanoid Robotics

In battery-powered humanoids, the voltage-divider principle explains how the available terminal voltage is split between the battery's internal resistance and the external load. A sudden increase in motor current raises the voltage drop across the internal resistance, leaving less voltage for the motor drives—a critical constraint for real-time power management and low-voltage ride-through design.
