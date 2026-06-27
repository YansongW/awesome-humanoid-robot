---
$id: ent_method_equivalent_circuit_battery_model
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Equivalent-Circuit Battery Model
  zh: 等效电路电池模型
  ko: 등가 회로 배터리 모델
summary:
  en: A method that represents a lithium-ion cell or pack as an electrical circuit
    of a voltage source and lumped resistive-capacitive elements to predict terminal
    voltage, current response, and state-of-charge dynamics.
  zh: 一种将锂离子电芯或电池包表示为由电压源与集总阻容元件组成的电路的方法，用于预测端电压、电流响应和荷电状态动态。
  ko: 전압원과 집중된 저항-커패시터 소자로 구성된 회로로 리튬 이온 셀 또는 팩을 표현하여 단자 전압, 전류 응답, 충전 상태 동역학을 예측하는 방법이다.
domains:
- 02_components
- 06_design_engineering
- 00_foundations
layers:
- upstream
- midstream
- foundations
functional_roles:
- knowledge
- component
tags:
- battery_model
- equivalent_circuit
- thevenin_model
- lithium_ion_battery
- state_of_charge
- humanoid_robot
theoretical_depth:
- method
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Standard method in battery engineering and BMS state estimation.
sources:
- id: src_hu_2012_ecm_soh
  type: paper
  title: 'A comparative study of equivalent circuit models for Li-ion batteries'
  url: https://doi.org/10.1016/j.jpowsour.2012.02.064
  date: '2012-07-15'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_formalism_thevenin_equivalent_circuit
  relationship: formalizes
  description:
    en: The equivalent-circuit battery method instantiates the Thevenin equivalent-circuit formalism.
    zh: 等效电路电池方法实例化了 Thevenin 等效电路形式化。
    ko: 등가 회로 배터리 방법은 테베닌 등가 회로 공식화를 구현한다.
- id: ent_butler_volmer_equation
  relationship: uses
  description:
    en: High-fidelity variants of the model use Butler-Volmer kinetics to parameterize polarization resistance.
    zh: 该模型的高保真变体使用 Butler-Volmer 动力学来参数化极化电阻。
    ko: 모델의 고충실도 변형은 Butler-Volmer 동역학을 사용하여 분극 저항을 매개변수화한다.
- id: ent_foundation_electrochemistry
  relationship: has_prerequisite
  description:
    en: Electrochemical kinetics and transport theory underpin the parameterization of equivalent-circuit elements.
    zh: 电化学动力学与传输理论支撑着等效电路元件的参数化。
    ko: 전기화학 동역학 및 전송 이론은 등가 회로 소자의 매개변수화를 뒷받침한다.
---

## 抽象

> **生活实例**：把电池想象成一支正在慢慢挤出水的牙膏。电压源是“牙膏还剩多少”，电阻是“牙膏口的粗细”，电容则是“管壁还能临时储一点牙膏”。等效电路模型就是把这支牙膏筒画成一个简单电路，让我们能快速估算还能挤出多少、挤多快。
>
> **自然语言逻辑**：锂离子电池内部的电化学过程非常复杂，但工程上常用一个由理想电压源、串联电阻和若干 RC 并联支路组成的电路来近似。通过测量电流，模型可以预测端电压下降、暂态响应以及剩余电量，为 BMS 和能耗管理提供实时依据。

## Overview

Equivalent-circuit battery models (ECMs) are widely used for real-time battery state estimation and control design. They trade physical detail for computational efficiency, representing a cell by an open-circuit voltage (OCV) source in series with ohmic resistance and one or more resistor-capacitor (RC) pairs. The model predicts how terminal voltage evolves under load, enabling state-of-charge (SoC) estimation, state-of-health (SoH) tracking, and power-limit calculation in battery management systems.

## Key Characteristics

- **First-order or higher-order RC structures**: A first-order ECM uses one RC pair; higher-order variants add pairs for improved transient accuracy.
- **Parameter identification**: OCV, ohmic resistance, and RC time constants are identified from pulse-discharge tests or online adaptive methods.
- **Coupled SoC dynamics**: The OCV source is a nonlinear function of SoC, so the electrical and charge-balance equations are coupled.
- **Computational efficiency**: ECMs are far lighter than physics-based pseudo-two-dimensional (P2D) models, making them suitable for embedded BMS.

## Relevance to Humanoid Robotics

Humanoid robots rely on compact, high-power-density battery packs whose voltage sags sharply during dynamic motions such as jumping or lifting. An equivalent-circuit model lets the BMS and motion planner predict available power, enforce safe current limits, and estimate remaining runtime. In power-aware whole-body control, the predicted voltage trajectory can be used to avoid actuation commands that would drive the pack outside its safe operating area.
