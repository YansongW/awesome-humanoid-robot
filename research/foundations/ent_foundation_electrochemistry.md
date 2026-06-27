---
$id: ent_foundation_electrochemistry
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: foundation
names:
  en: Electrochemistry
  zh: 电化学
  ko: 전기화학
summary:
  en: The foundational science of electron and ion transport across interfaces, governing
    reactions, potentials, and mass transfer in batteries, fuel cells, and corrosion.
  zh: 研究界面间电子与离子传输的基础科学，支配电池、燃料电池和腐蚀中的反应、电势与传质过程。
  ko: 전지, 연료 전지 및 부식에서 반응, 전위 및 물질 이동을 지배하는 계면을 통한 전자와 이온 전송의 기초 과학이다.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
tags:
- electrochemistry
- ion_transport
- electrode_kinetics
- battery
- humanoid_robot
theoretical_depth:
- foundation
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Broad foundational discipline; underpins lithium-ion battery operation.
sources:
- id: src_bard_faulkner_2001
  type: other
  title: 'A. J. Bard and L. R. Faulkner, Electrochemical Methods: Fundamentals and Applications, 2nd ed.'
  url: https://www.wiley.com/en-us/Electrochemical+Methods%3A+Fundamentals+and+Applications%2C+2nd+Edition-p-9780471043720
  date: '2001-01-01'
  accessed_at: '2026-06-26'
---

## 抽象

> **生活实例**：把电池想象成一个繁忙的跨国收费站。电子走一条车道，锂离子走另一条车道，两边必须协调好流量，否则就会堵车。电化学就是研究这两条“车道”如何互相配合、如何收费（交换能量）的科学。
>
> **自然语言逻辑**：电化学研究带电粒子在电极-电解质界面上的行为，包括电荷转移反应、离子扩散、浓差极化等。它解释了电池为什么能存储和释放电能，也决定了电池的能量密度、功率密度、寿命和安全性。

## Overview

Electrochemistry is the foundational discipline that describes how chemical reactions and electrical energy interconvert at interfaces. Core concepts include electrode potentials, redox reactions, charge-transfer kinetics, mass transport by diffusion and migration, and the structure of the electrical double layer. These phenomena collectively determine the voltage, capacity, rate capability, and degradation of lithium-ion batteries.

## Key Characteristics

- **Redox reactions**: Reduction and oxidation half-reactions occur at the negative and positive electrodes.
- **Charge-transfer kinetics**: Described by the Butler-Volmer equation and related activation models.
- **Mass transport**: Diffusion and migration of ions in electrolytes and electrodes limit rate capability.
- **Thermodynamics**: Equilibrium potentials are governed by the Nernst equation and Gibbs free energy.
- **Interfacial stability**: Solid-electrolyte interphase (SEI) layers critically affect cycle life and safety.

## Relevance to Humanoid Robotics

Humanoid robots demand batteries with high energy density, high power density, and long cycle life. Electrochemistry sets the fundamental limits of what battery chemistry can achieve and explains trade-offs such as energy versus power, capacity versus stability, and fast charging versus degradation. A solid grasp of electrochemistry is therefore essential for selecting cell chemistry, designing thermal management, and predicting battery lifetime in humanoid applications.
