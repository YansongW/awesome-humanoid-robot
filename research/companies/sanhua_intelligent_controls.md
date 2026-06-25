---
$id: ent_tier1_supplier_sanhua_intelligent_controls
$schema: "../../../../../data/schema/v1/entry_schema.json"
$version: 1

type: tier1_supplier

names:
  en: "Sanhua Intelligent Controls"
  zh: "三花智控"
  ko: "산화 인텔리전트 컨트롤스"

summary:
  en: "Chinese Tier-1 supplier of thermal management and electromechanical actuators, reportedly a key actuator assembly partner for Tesla Optimus."
  zh: "中国一级供应商，主营热管理和机电执行器，据报道是特斯拉 Optimus 执行器总成的核心合作伙伴。"
  ko: "중국의 Tier-1 열관리 및 전기기계 액추에이터 공급업체로, 테슬라 옵티머스의 액추에이터 어셈블리 핵심 파트너로 알려짐."

domains:
  - "02_components"
  - "05_mass_production"

layers:
  - "upstream"
  - "midstream"

functional_roles:
  - "organization"

tags:
  - "sanhua"
  - "tier1_supplier"
  - "actuator"
  - "thermal_management"
  - "tesla"
  - "optimus"
  - "china"

verification:
  status: "partially_verified"
  reviewed_by: "ai"
  reviewed_at: "2026-06-25"
  confidence: "medium"
  notes: "AI-extracted from industry reports and supply-chain analysis; the exact dollar value of the Tesla order and Sanhua's exclusive supplier status are based on unconfirmed media reports that Sanhua has publicly denied."

sources:
  - id: "src_001_sanhua_36kr"
    type: "report"
    title: "Elon Musk Places $685M Order with Sanhua"
    url: "https://eu.36kr.com/en/p/3510288514980998"
    date: "2025-10-15"
    accessed_at: "2026-06-25"
  - id: "src_002_sanhua_optimusk"
    type: "report"
    title: "Tesla Optimus Supply Chain: Who Makes the Parts?"
    url: "https://optimusk.blog/blog/tesla-optimus-suppliers/"
    date: "2026-06-01"
    accessed_at: "2026-06-25"

related_entities:
  - id: "ent_robot_system_tesla_optimus"
    relationship: "supplies"
    description:
      en: "Sanhua is reported to supply linear and rotary actuator assemblies for Tesla Optimus."
      zh: "据报道，三花智控为特斯拉 Optimus 供应线性与旋转执行器总成。"
      ko: "산화는 테슬라 옵티머스용 선형 및 회전 액추에이터 어셈블리를 공급하는 것으로 볏도됨."
  - id: "ent_component_harmonic_drive_reducer"
    relationship: "integrates"
    description:
      en: "Sanhua's actuator assemblies are understood to integrate precision reducers such as harmonic drives sourced from specialized reducer suppliers."
      zh: "三花的执行器总成据信集成了来自专业减速器供应商的谐波减速器等精密减速装置。"
      ko: "산화의 액추에이터 어셈블리는 전문 감속기 공급업체로부터 조달한 하모닉 드라이브 등의 정밀 감속기를 통합하는 것으로 파악됨."
---

# Sanhua Intelligent Controls

## 生活实例 + 自然语言阐述逻辑

> **生活实例**：它就像一家原本给汽车做空调阀和散热管的零部件厂，突然被要求为新一代“机器人工人”批量生产关节总成——靠的是精密加工和大规模供货能力。

> **自然语言逻辑**：三花智控是中国热管理和机电执行器的一级供应商，据报道是特斯拉 Optimus 执行器总成的核心合作伙伴；它把人形机器人关节当成新的规模化产品，利用在汽车供应链中积累的精密制造和量产经验，进入人形机器人上游供应链。

## Overview

Sanhua Intelligent Controls Co., Ltd. (SZSE: 002050) is a Chinese Tier-1 supplier best known for thermal-management components for automotive and HVAC industries. In the humanoid-robot supply chain, it is frequently cited as a leading supplier of **linear and rotary actuator assemblies** for Tesla Optimus, leveraging a roughly decade-long relationship as a Tesla vehicle supplier.

## Reported Role in Optimus Supply Chain

- **Actuator assemblies**: Chinese supply-chain analyses name Sanhua as the exclusive or primary Tier-1 supplier of linear/rotary actuator assemblies for Optimus, with a reported Ningbo base capacity of **500,000 actuator sets per year**.
- **$685 million order**: An October 2025 36kr report claimed Tesla placed a ~$685 million (5 billion RMB) order with Sanhua for linear actuators, with deliveries beginning Q1 2026. **Sanhua publicly denied the specific figure**, but its robot-related revenue grew **320% year-on-year in H1 2025**, suggesting significant real orders even if the exact value is unconfirmed.
- **Thermal management**: Beyond actuators, Sanhua supplies thermal-management systems that help regulate actuator temperatures.

## Corporate Context

Sanhua's robotics pivot mirrors the broader migration of Chinese automotive suppliers into humanoid-robot components. Its strengths—precision machining, high-volume production, and existing Tesla quality-system certification—are cited as reasons it was able to win humanoid actuator business. The company is also reported to be expanding production in Thailand, near Tesla's Gigafactory Texas supply chain.

## Relevance to Humanoid Robotics

Sanhua is one of the most frequently referenced examples of a traditional automotive/HVAC supplier crossing over into humanoid-robot actuators. Its reported orders and revenue growth are used by analysts as a proxy for Tesla Optimus production ramp and for the broader commercial viability of Chinese component suppliers in the humanoid robot value chain.

## Uncertainties

- The exact value and exclusivity of the Tesla order are disputed; Sanhua denied the $685 million figure.
- The precise mix of components Sanhua manufactures in-house versus sources from sub-suppliers is not publicly detailed.
- Geographic concentration risk: Sanhua's facilities are primarily in China, with Thailand expansion reported but not independently verified.
