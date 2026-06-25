---
$id: ent_robot_system_tesla_optimus
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: Tesla Optimus
  zh: Tesla Optimus
  ko: 테슬라 옵티머스
summary:
  en: Tesla's general-purpose humanoid robot program, with stated goals of factory deployment
    and high-volume manufacturing.
  zh: 特斯拉的通用人形机器人项目，目标是工厂部署和规模化制造。
  ko: 테슬라의 범용 휴인oid 로봇 프로그램으로, 공장 배치와 대량 생산을 목표로 합니다.
domains:
- 05_mass_production
- 06_design_engineering
- 11_applications_markets
layers:
- midstream
- validation_markets
functional_roles:
- system
- knowledge
tags:
- tesla
- optimus
- humanoid
- robot_system
- factory
- manufacturing
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-24'
  confidence: medium
  notes: Public demonstrations and company statements; detailed specifications and production
    plans are not independently verified.
sources:
- id: src_001
  type: website
  title: Tesla Optimus Official Page
  url: https://www.tesla.com/optimus
  date: '2026'
  accessed_at: '2026-06-24'
- id: src_002
  type: report
  title: Interact Analysis — Humanoid Robots and Lithium-Ion Batteries
  url: https://interactanalysis.com/insight/humanoid-robots-and-lithium-ion-batteries/
  date: '2026'
  accessed_at: '2026-06-24'
---

## Overview

Tesla Optimus is a humanoid robot program announced by Tesla with the aim of performing repetitive or dangerous tasks in manufacturing and logistics. The company has showcased several prototype generations, emphasizing affordability, mass production, and integration with Tesla's manufacturing and AI capabilities.

## Reported Specifications

- **Battery**: Reported 2.3 kWh pack on Optimus Gen-2, supporting roughly two hours of dynamic runtime.
- **Actuation**: Electric actuators designed in-house, with iterative improvements in torque density and weight.
- **Sensing**: Onboard cameras and sensors for navigation and manipulation.
- **Compute**: Leverages Tesla's automotive AI compute and software stack.

## Relevance to Humanoid Robotics

Optimus is notable for Tesla's explicit focus on scaling production and reducing unit cost. If successful at volume, it could influence supply-chain expectations and manufacturing workflows across the humanoid robotics industry. Many claims remain forward-looking and require independent verification.
