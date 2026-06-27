---
$id: ent_report_bofa_humanoid_robots_101_2025
$schema: ../../../../../data/schema/v1/entry_schema.json
$version: 1
type: report
names:
  en: Bank of America Institute — Humanoid Robots 101
  zh: 美国银行研究所——人形机器人入门
  ko: 뱅크오브아메리카 인스티튜트 — 휴이노이드 로봇 101
summary:
  en: An April 2025 primer from Bank of America Institute that breaks down humanoid
    robot architecture, key components, BOM cost trajectory, and adoption stages through
    2060.
  zh: 美国银行研究所 2025 年 4 月发布的人形机器人入门报告，解析了人形机器人架构、核心零部件、物料成本轨迹及到 2060 年的应用阶段。
  ko: 2025년 4월 Bank of America Institute가 발표한 휴이노이드 로봇 입문서로, 휴이노이드 로봇 아키텍처, 핵심 부품,
    BOM 비용 궤적 및 2060년까지의 도입 단계를 분석함.
domains:
- 05_mass_production
- 11_applications_markets
layers:
- midstream
- validation_markets
functional_roles:
- knowledge
- market
tags:
- bofa
- market_report
- bom_cost
- mass_production
- adoption_forecast
- supply_chain
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: AI-extracted from the published Bank of America Institute PDF; quantitative
    forecasts are analyst estimates and should be treated as projections, not facts.
sources:
- id: src_report_bofa_humanoid_robots_101_2025
  type: report
  title: Humanoid Robots 101
  url: https://institute.bankofamerica.com/content/dam/transformation/humanoid-robots.pdf
  date: '2025-04-29'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_component_harmonic_drive_reducer
  relationship: cites
  description:
    en: The report identifies harmonic reducers as a mainstream transmission choice
      for rotary actuators in humanoid robots.
    zh: 该报告指出谐波减速器是人形机器人旋转执行器的主流传动选择之一。
    ko: 해당 보고서는 하모닉 감속기가 휴이노이드 로봇의 회전 액추에이터에 사용되는 주류 전동 장치 중 하나임을 언급함.
theoretical_depth:
- system
---

# Bank of America Institute — Humanoid Robots 101

## 抽象

> **生活实例**：它就像给投资者写的《人形机器人入门手册》——拆解了机器人由哪些“器官”组成、每台成本大概多少、未来几十年可能怎么普及。

> **自然语言逻辑**：这份 2025 年 4 月发布的美国银行研究所报告系统介绍了人形机器人架构、核心零部件、物料成本轨迹以及到 2060 年的应用阶段；它为理解人形机器人市场预测、供应链机会和规模化路径提供了投资者视角的宏观参考。

## Overview

Published on 29 April 2025 by the Bank of America Institute, *Humanoid Robots 101* is a strategic primer aimed at investors and business audiences. It frames humanoid robots as service robots that operate in unstructured environments, contrasting them with traditional industrial robots. The report argues that advances in AI (especially LLMs and VLMs), 3D perception, control algorithms, and falling component costs are poised to move humanoids from proof-of-concept to multi-industry adoption by the end of the decade.

## Key Findings

- **Architecture**: A typical humanoid robot is divided into an AI system ("brain"), a motion-control system ("little brain"), and a body containing vision, sensing, actuators, dexterous hands, energy, and structural components.
- **Actuation**: Electric actuators are the mainstream route. A rotary actuator typically combines a frameless torque motor, a harmonic or planetary reducer, encoders, and torque/force sensors; linear actuators often use planetary roller screws.
- **BOM cost**: BofA Global Research estimated a typical humanoid robot BOM at roughly **$35,000 per unit** by end-2025, assuming 16 rotary actuators, 14 linear actuators, harmonic reducers, planetary roller screws, a 6-DoF dexterous hand, one depth camera, one LiDAR, and predominantly Chinese-made components.
- **Cost trajectory**: BOM is projected to fall to **$13,000–$17,000 per unit by 2030–2035**, driven by economies of scale and component-design improvements—an implied ~14% CAGR of decline.
- **Adoption stages**:
  1. Development (2025–2027): small-batch industrial/logistics pilots.
  2. Mass commercial adoption (2028–2034): business services and less-structured environments.
  3. Mass consumer adoption (2035+): household and elderly care.
- **Long-term forecast**: Under BofA assumptions, global humanoid-robot units-in-ownership could reach **3 billion by 2060**.

## Supply-Chain Relevance

The report highlights several near-term bottlenecks: availability of high-performance processor chips, high-end machine tools for precision parts (e.g., planetary roller screws and harmonic reducers), and the design choices that will determine whether harmonic or planetary reducers, roller screws or ball screws, and cameras or LiDAR dominate. These uncertainties imply a 24-month supplier-entry window before architectures consolidate.

## Uncertainties

The BOM and shipment figures are analyst estimates, not audited financials. The report itself notes that humanoid robots are not yet standard-spec products, so cost predictions are inherently uncertain.
