---
$id: ent_equation_thevenin_terminal_voltage
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: equation
names:
  en: Thevenin Terminal Voltage Equation
  zh: Thevenin 端电压方程
  ko: 테베닌 단자 전압 방정식
summary:
  en: The equation that gives the terminal voltage of a Thevenin equivalent circuit
    as the open-circuit voltage minus the voltage drop across the equivalent resistance.
  zh: 给出 Thevenin 等效电路端电压等于开路电压减去等效电阻上压降的方程。
  ko: 테베닌 등가 회로의 단자 전압을 개방 전압에서 등가 저항의 전압 강하를 뺀 값으로 나타내는 방정식이다.
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
- terminal_voltage
- equivalent_circuit
- battery_model
- voltage_divider
- humanoid_robot
theoretical_depth:
- formalism
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Direct consequence of Kirchhoff's voltage law applied to the Thevenin equivalent circuit.
sources:
- id: src_dorf_svoboda_2017
  type: paper
  title: 'Dorf & Svoboda, Introduction to Electric Circuits, 9th ed.'
  url: https://www.wiley.com/en-us/Introduction+to+Electric+Circuits%2C+9th+Edition-p-9781118931897
  date: '2017-01-01'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_operator_voltage_divider
  relationship: uses
  description:
    en: The terminal voltage equation applies the voltage-divider concept to the series Thevenin resistance and load.
    zh: 端电压方程将分压概念应用于串联的 Thevenin 电阻和负载。
    ko: 단자 전압 방정식은 직렬 테베닌 저항과 부하에 분압 개념을 적용한다.
- id: ent_principle_conservation_of_charge
  relationship: derived_from
  description:
    en: Kirchhoff's current law, rooted in charge conservation, underlies the current-balance used to derive terminal voltage.
    zh: 源于电荷守恒的基尔霍夫电流定律支撑着推导端电压所用的电流平衡。
    ko: 전하 보존에 뿌리를 둔 키르히호프 전류 법칙은 단자 전압을 유도하는 데 사용되는 전류 평형의 기초가 된다.
---

## 抽象

> **生活实例**：想象一根水管，水龙头全开时水压最高；接上一个细喷头后，水流受阻力，喷头处的水压就会下降。电池端电压也是这样：没有电流时等于“开路电压”，一有电流，内部电阻就会“吃掉”一部分电压。
>
> **自然语言逻辑**：把电池抽象成理想电压源 $V_{oc}$ 和内部电阻 $R_{th}$ 的串联。接上负载电流 $I$ 后，根据欧姆定律，内阻上的压降是 $I R_{th}$，所以外部能测到的端电压就是 $V_t = V_{oc} - I R_{th}$。

## Overview

For a battery modeled by a Thevenin equivalent circuit, the terminal voltage $V_t$ under load current $I$ is given by the open-circuit voltage minus the ohmic drop across the equivalent series resistance. With one RC polarization branch, the equation extends to include a transient polarization voltage $V_{RC}$.

## Formal Definition

For the first-order Thevenin equivalent circuit with a single RC pair:

$$
V_t(t) = V_{oc}\bigl(SoC(t)\bigr) - I(t) R_0 - V_{RC}(t)
$$

where the polarization voltage evolves as

$$
\frac{d V_{RC}}{dt} = -\frac{V_{RC}}{R_1 C_1} + \frac{I}{C_1}.
$$

In steady state or for a purely resistive Thevenin model ($R_1 C_1 \to 0$), this reduces to

$$
V_t = V_{oc} - I R_{th}.
$$

| Symbol | Name | Intuition |
|--------|------|-----------|
| $V_t$ | Terminal voltage | The voltage you can actually measure at the battery terminals |
| $V_{oc}$ | Open-circuit voltage | The battery's "ideal" voltage when no current flows |
| $R_0$ / $R_{th}$ | Ohmic / Thevenin resistance | The internal "friction" that causes instant voltage sag |
| $V_{RC}$ | Polarization voltage | The slower voltage drift caused by diffusion and charge-transfer dynamics |
| $R_1, C_1$ | Polarization resistance and capacitance | The "memory" branch that captures transient behavior |
| $I$ | Load current | Positive for discharge, negative for charge |
| $SoC$ | State of charge | Remaining charge as a fraction of total capacity |

## Relevance to Humanoid Robotics

Humanoid actuators draw large, rapidly changing currents. The Thevenin terminal-voltage equation lets the BMS and motion controller predict how much voltage will be available at the motor drives during peak power demands. Keeping $V_t$ above the minimum operating voltage of the servo drives is essential for preventing control faults or unexpected joint lockouts.
