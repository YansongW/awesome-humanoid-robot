---
$id: ent_component_manufacturer_nidec_drive_technology
$schema: "../../../../../data/schema/v1/entry_schema.json"
$version: 1

type: component_manufacturer

names:
  en: "Nidec Drive Technology"
  zh: "尼得科传动技术"
  ko: "니덱 드라이브 테크놀로지"

summary:
  en: "Japanese precision drive subsidiary of Nidec Corporation, manufacturer of FLEXWAVE strain-wave gear reducers and motion products targeted at humanoid robots."
  zh: "日本电产株式会社旗下精密传动子公司，生产面向人形机器人的 FLEXWAVE 应变波齿轮减速器及运动控制产品。"
  ko: "Nidec Corporation의 일본 정밀 드라이브 자회사로, 휴이노이드 로봇용 FLEXWAVE 스트레인 웨이브 기어 감속기 및 모션 제품을 생산함."

domains:
  - "02_components"

layers:
  - "upstream"

functional_roles:
  - "organization"
  - "component"

tags:
  - "nidec"
  - "flexwave"
  - "harmonic_reducer"
  - "strain_wave_gear"
  - "component_manufacturer"
  - "japan"

verification:
  status: "partially_verified"
  reviewed_by: "ai"
  reviewed_at: "2026-06-25"
  confidence: "medium"
  notes: "AI-extracted from Nidec's official humanoid-robot product page and industry market reports; specific customer names and design-win status are not confirmed."

sources:
  - id: "src_001_nidec_official"
    type: "website"
    title: "Nidec — Highly Developed Humanoid Robots"
    url: "https://www.nidec-dtc.com/humanoid-robots/"
    date: "2026"
    accessed_at: "2026-06-25"
  - id: "src_002_nidec_market_report"
    type: "report"
    title: "Humanoid Robot Market Key Player Ecosystem — Actuators & Actuator Parts"
    url: "https://www.maximizemarketresearch.com/market-report/global-humanoid-robot-market/10567/"
    date: "2026-05-07"
    accessed_at: "2026-06-25"

related_entities:
  - id: "ent_component_harmonic_drive_reducer"
    relationship: "produces"
    description:
      en: "Nidec Drive Technology produces FLEXWAVE strain-wave gear reducers, a form of harmonic reducer used in humanoid robot joints."
      zh: "尼得科传动技术生产 FLEXWAVE 应变波齿轮减速器，这是一种用于人形机器人关节的谐波减速器。"
      ko: "니덱 드라이브 테크놀로지는 휴이노이드 로봇 관절에 사용되는 하모닉 감속기의 일종인 FLEXWAVE 스트레인 웨이브 기어 감속기를 생산함."
  - id: "ent_component_bldc_motor"
    relationship: "produces"
    description:
      en: "Nidec's broader motor portfolio includes brushless DC and precision servo motors used in robotic actuators."
      zh: "尼得科更广泛的电机产品组合包括用于机器人执行器的无刷直流电机和精密伺服电机。"
      ko: "니덱의 폭넓은 모터 포트폴리오에는 로봇 액추에이터에 사용되는 브러시리스 DC 모터 및 정밀 서보 모터가 포함됨."
---

# Nidec Drive Technology

## 生活实例 + 自然语言阐述逻辑

> **生活实例**：它就像一家精密手表齿轮厂开始为机器人生产“微型强力变速器”——用极小的体积把电机的高速旋转变成关节所需的慢速大扭矩。

> **自然语言逻辑**：尼得科传动技术是日本电产旗下的精密传动子公司，生产面向人形机器人的 FLEXWAVE 应变波减速器、电机和编码器；它为机器人关节提供高减速比、低背隙的精密传动方案，是人形机器人上游减速器和电机供应链的重要参与者。

## Overview

Nidec Drive Technology (Nidec-DTC) is a subsidiary of Nidec Corporation focused on precision drive systems. It markets the **FLEXWAVE** family of strain-wave gear reducers—also known as harmonic-drive-style reducers—specifically for humanoid robots and other precision robotics applications. Nidec is also a major global producer of small precision motors, including brushless DC and servo motors.

## FLEXWAVE Product Line

The FLEXWAVE series is advertised on Nidec's humanoid-robot page as offering:

- High positional accuracy and zero backlash
- Low vibration and compact form factor
- High torque capacity relative to size
- Component sub-assembly and complete-unit configurations
- Frame sizes from 35 mm to 80 mm outer diameter, with reduction ratios from 50:1 to 160:1
- Peak output torque ranging from ~12 N·m (flat-profile WPC-CD 35) to ~484 N·m (WPC-CR 80)

These specifications place FLEXWAVE in direct competition with traditional harmonic-drive suppliers such as Harmonic Drive Systems (Japan) and LeaderDrive (China).

## Role in the Humanoid Supply Chain

Industry market reports list Nidec as a key supplier of **motors + encoders** and precision reducers for commercial and industrial robots. While Nidec's exact customer list for humanoid robots is not publicly confirmed, its product positioning and the existence of a dedicated humanoid-robot landing page indicate that the company is targeting the sector as a component supplier.

## Relevance to Humanoid Robotics

Nidec represents the established Japanese precision-motion supplier segment competing to supply reducers and motors for next-generation humanoids. Its entry into humanoid-specific reducer marketing illustrates how industrial automation suppliers are adapting existing technologies for the humanoid robot form factor.

## Uncertainties

- Specific humanoid OEM customers and design wins have not been publicly disclosed by Nidec.
- Market-share claims in third-party reports are estimates and should be treated as indicative.
- The extent to which FLEXWAVE is already in production volumes for humanoids versus being sampled/evaluated is unclear.
