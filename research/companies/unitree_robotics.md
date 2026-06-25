---
$id: ent_oem_unitree_robotics
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: oem
names:
  en: Unitree Robotics
  zh: 宇树科技
  ko: 유닛리 로보틱스
summary:
  en: Chinese robotics company developing quadruped and humanoid robots, including the Unitree
    H1 and G1 platforms, with a focus on high-torque actuators and cost-conscious design.
  zh: 中国机器人公司，开发四足和人形机器人，包括 Unitree H1 和 G1 平台，专注于高扭矩执行器和成本导向设计。
  ko: 중국 로봇 기업으로, 고토크 액추에이터와 비용 중심 설계에 초점을 맞춘 Unitree H1 및 G1
    휴인oid 플랫폼을 개발하고 있습니다.
domains:
- 02_components
- 06_design_engineering
- 11_applications_markets
layers:
- upstream
- midstream
- validation_markets
functional_roles:
- organization
- system
tags:
- unitree
- humanoid
- oem
- quadruped
- actuator
- h1
- g1
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-24'
  confidence: medium
  notes: Product specifications and company background sourced from official product pages
    and industry reports; financial and operational details are limited.
sources:
- id: src_001
  type: website
  title: Unitree H1 Humanoid Robot — Product Specifications
  url: https://unitreerobotics.us/products/unitree-h1-humanoid-robot
  date: '2025'
  accessed_at: '2026-06-24'
- id: src_002
  type: report
  title: IDTechEx Humanoid Robots 2025-2035
  url: https://www.idtechex.com/en/research-report/humanoid-robots/1093
  date: '2025'
  accessed_at: '2026-06-24'
---

# Unitree Robotics

## 抽象

> **生活实例**：它就像一家因机器狗闻名的公司，转而推出价格更亲民的“机器人体”——让更多实验室能买得起、用得上真实的人形硬件。

> **自然语言逻辑**：宇树科技是中国机器人公司，以四足机器人和 Unitree H1/G1 人形平台著称；它注重自研高扭矩执行器和成本控制，使人形机器人硬件对研究者和早期工业用户更加可及，成为讨论人形机器人 BOM 和规模化时的重要参照。

## Overview

Unitree Robotics is a Hangzhou-based robotics company founded in 2016. It first became known for consumer and industrial quadruped robots, then expanded into humanoids with the Unitree H1 (launched 2023) and the smaller, lower-cost Unitree G1 (launched 2024). The company emphasizes in-house actuator development, high torque density, and aggressive pricing relative to comparable humanoid platforms.

## Key Products

- **Unitree H1**: Full-size humanoid with 3D LiDAR, depth camera, Intel Core i5/i7 compute with optional NVIDIA Jetson Orin NX, and reported knee-joint peak torque of ~360 N·m.
- **Unitree G1**: Compact humanoid targeting research and education, with a lower price point and reduced degrees of freedom compared to H1.
- **Quadruped line**: Go1, Go2, B2, and similar legged platforms used for research, inspection, and logistics.

## Relevance to Humanoid Robotics

Unitree is one of the few OEMs shipping humanoid hardware in volume to research labs and early industrial pilots. Its focus on actuator performance and cost makes it a frequently cited reference point for discussions about humanoid BOM cost and scalability.
