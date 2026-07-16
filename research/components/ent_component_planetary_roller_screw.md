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


