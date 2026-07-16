---
$id: ent_component_planetary_roller_screw
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Planetary Roller Screw
  zh: 行星滚柱丝杠
  ko: 행성 롤러 스크류
summary:
  en: A high-load, high-precision linear motion mechanism that converts rotary motion to linear motion via threaded rollers,
    often used in humanoid linear actuators.
  zh: '- Tesla Optimus：据 Tesla AI Day 2022 与后续公开信息，Optimus 躯干采用 28 个执行器（14 个旋转 + 14 个线性），旋转关节使用无框力矩电机 + 谐波减速器，线性关节使用无框力矩电机
    + 行星滚柱丝杠；灵巧手从 Gen 2 的 11 DoF 升级到 Gen 3 的 22 DoF，采用腱驱动与微型执行器[14]。 - Boston Dynamics Atlas：早期 Atlas 采用液压执行器以获得极大爆发力；2024
    年发布的全电动 Atlas 改用电动执行器，强调力量、敏捷与平衡恢复能力[15]。 - Agility Robotics Digit：Digit 腿部采用串联弹性执行器（SEA），强调行走能效与人机安全；上肢自由度较少，面向物流搬运场景[16]。
    - Figure AI Figure 02：采用全电动执行器，目标是人形机器人在仓储与制造中的通用操作，公开信息强调端到端 AI 与灵巧手集成[17]。'
  ko: 스레드 롤러를 통해 회전욕동을 직선욕동으로 변환하는 고하중·고정밀 직선 기구로 휴로봇 선형 액추에이터에 사용됨.
domains:
- 02_components
layers:
- midstream
functional_roles:
- knowledge
tags:
- component
- chapter_4
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body restructured into standard sections by scripts/restructure_entry_bodies.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---

## 概述
### 4.6.4 案例：Optimus、Atlas、Digit、Figure

## 核心内容
- **Tesla Optimus**：据 Tesla AI Day 2022 与后续公开信息，Optimus 躯干采用 28 个执行器（14 个旋转 + 14 个线性），旋转关节使用无框力矩电机 + 谐波减速器，线性关节使用无框力矩电机 + 行星滚柱丝杠；灵巧手从 Gen 2 的 11 DoF 升级到 Gen 3 的 22 DoF，采用腱驱动与微型执行器[14]。
- **Boston Dynamics Atlas**：早期 Atlas 采用液压执行器以获得极大爆发力；2024 年发布的全电动 Atlas 改用电动执行器，强调力量、敏捷与平衡恢复能力[15]。
- **Agility Robotics Digit**：Digit 腿部采用串联弹性执行器（SEA），强调行走能效与人机安全；上肢自由度较少，面向物流搬运场景[16]。
- **Figure AI Figure 02**：采用全电动执行器，目标是人形机器人在仓储与制造中的通用操作，公开信息强调端到端 AI 与灵巧手集成[17]。

!!! note "术语解释：行星滚柱丝杠、液压执行器、灵巧手、腱驱动手、人形机器人平台"
    - **行星滚柱丝杠（planetary roller screw）**：由丝杠、滚柱和螺母组成的高效精密直线传动机构，承载力与寿命远高于滚珠丝杠。
    - **液压执行器（hydraulic actuator）**：利用高压油液推动活塞产生力的执行器，功率密度极高但系统复杂。
    - **灵巧手（dexterous hand）**：具有多自由度、多触点的仿人手，可执行抓握与精细操作。
    - **腱驱动手（tendon-driven hand）**：电机布置在前臂或手掌，通过腱绳驱动手指关节，降低手指惯量。
    - **人形机器人平台（humanoid robot platform）**：面向研究与商业应用的完整机器人系统，如 Atlas、Digit、Optimus、Figure 等。

---

## 参考
- Wiki extraction

## Overview
### 4.6.4 Case Studies: Optimus, Atlas, Digit, Figure

## Content
- **Tesla Optimus**: According to Tesla AI Day 2022 and subsequent public information, Optimus uses 28 actuators in its torso (14 rotary + 14 linear). The rotary joints employ frameless torque motors + harmonic reducers, while the linear joints use frameless torque motors + planetary roller screws. The dexterous hand has been upgraded from 11 DoF in Gen 2 to 22 DoF in Gen 3, utilizing tendon-driven actuation and micro actuators[14].
- **Boston Dynamics Atlas**: Early Atlas used hydraulic actuators to achieve extreme explosive power. The fully electric Atlas released in 2024 switched to electric actuators, emphasizing strength, agility, and balance recovery capabilities[15].
- **Agility Robotics Digit**: Digit's legs use series elastic actuators (SEA), emphasizing walking energy efficiency and human safety. Its upper body has fewer degrees of freedom, targeting logistics and material handling scenarios[16].
- **Figure AI Figure 02**: Adopts fully electric actuators, aiming for general-purpose humanoid robot operations in warehousing and manufacturing. Public information highlights end-to-end AI integration with dexterous hands[17].

!!! note "Terminology Explanation: Planetary Roller Screw, Hydraulic Actuator, Dexterous Hand, Tendon-Driven Hand, Humanoid Robot Platform"
    - **Planetary roller screw**: A high-efficiency precision linear transmission mechanism composed of a screw, rollers, and a nut, offering significantly higher load capacity and lifespan than ball screws.
    - **Hydraulic actuator**: An actuator that uses high-pressure oil to push a piston to generate force, offering extremely high power density but with complex system requirements.
    - **Dexterous hand**: A multi-degree-of-freedom, multi-contact anthropomorphic hand capable of grasping and fine manipulation.
    - **Tendon-driven hand**: A hand where motors are placed in the forearm or palm, driving finger joints via tendons to reduce finger inertia.
    - **Humanoid robot platform**: A complete robotic system for research and commercial applications, such as Atlas, Digit, Optimus, Figure, etc.

---

## 개요
### 4.6.4 사례: Optimus, Atlas, Digit, Figure

## 핵심 내용
- **Tesla Optimus**: Tesla AI Day 2022 및 이후 공개 정보에 따르면, Optimus의 동체는 28개의 액추에이터(14개 회전 + 14개 선형)를 사용하며, 회전 관절은 프레임리스 토크 모터 + 고조파 감속기를, 선형 관절은 프레임리스 토크 모터 + 행성 롤러 스크류를 사용합니다. 다섯 손가락 로봇 핸드는 Gen 2의 11 DoF에서 Gen 3의 22 DoF로 업그레이드되었으며, 텐던 구동과 마이크로 액추에이터를 채택했습니다[14].
- **Boston Dynamics Atlas**: 초기 Atlas는 유압 액추에이터를 사용하여 뛰어난 폭발력을 얻었습니다. 2024년에 발표된 완전 전기식 Atlas는 전동 액추에이터로 전환하여 힘, 민첩성 및 균형 회복 능력을 강조합니다[15].
- **Agility Robotics Digit**: Digit의 다리는 직렬 탄성 액추에이터(SEA)를 사용하여 보행 에너지 효율과 인간-로봇 안전을 강조합니다. 상체 자유도는 상대적으로 적으며, 물류 운반 시나리오를 대상으로 합니다[16].
- **Figure AI Figure 02**: 완전 전동 액추에이터를 채택하며, 목표는 창고 및 제조 분야에서 인간형 로봇의 범용 작업입니다. 공개 정보는 엔드투엔드 AI와 다섯 손가락 로봇 핸드 통합을 강조합니다[17].

!!! note "용어 설명: 행성 롤러 스크류, 유압 액추에이터, 다섯 손가락 로봇 핸드, 텐던 구동 핸드, 인간형 로봇 플랫폼"
    - **행성 롤러 스크류(planetary roller screw)**: 스크류, 롤러 및 너트로 구성된 고효율 정밀 직선 운동 기구로, 볼 스크류보다 훨씬 높은 하중 지지력과 수명을 제공합니다.
    - **유압 액추에이터(hydraulic actuator)**: 고압 오일을 사용하여 피스톤에 힘을 생성하는 액추에이터로, 출력 밀도가 매우 높지만 시스템이 복잡합니다.
    - **다섯 손가락 로봇 핸드(dexterous hand)**: 다중 자유도와 다중 접점을 가진 인간형 손으로, 파지 및 정밀 조작을 수행할 수 있습니다.
    - **텐던 구동 핸드(tendon-driven hand)**: 모터가 팔뚝이나 손바닥에 배치되고, 텐던을 통해 손가락 관절을 구동하여 손가락 관성을 줄입니다.
    - **인간형 로봇 플랫폼(humanoid robot platform)**: 연구 및 상업 응용을 위한 완전한 로봇 시스템으로, Atlas, Digit, Optimus, Figure 등이 있습니다.

---
