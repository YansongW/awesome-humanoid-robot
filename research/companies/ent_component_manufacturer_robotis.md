---
$id: ent_component_manufacturer_robotis
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component_manufacturer
names:
  en: Robotis
  zh: Robotis
  ko: 로보티즈
summary:
  en: South Korean company known for Dynamixel smart actuators, widely used in research
    robots, educational platforms, and humanoid hands.
  zh: 韩国公司，以 Dynamixel 智能执行器闻名，广泛应用于研究机器人、教育平台和人形手。
  ko: 다이나믹셀 스마트 액추에이터로 잘 알려진 한국 기업으로, 연구용 로봇, 교육용 플랫폼 및 휴인oid 손에 널리 사용됩니다.
domains:
- 02_components
- 06_design_engineering
layers:
- upstream
- midstream
functional_roles:
- organization
- component
tags:
- robotis
- dynamixel
- actuator
- servo
- research
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-24'
  confidence: high
  notes: Product specifications and company history are documented on the official
    Robotis website and in academic papers citing Dynamixel hardware.
sources:
- id: src_001
  type: website
  title: Robotis Official Website
  url: https://www.robotis.com/
  date: '2026'
  accessed_at: '2026-06-24'
- id: src_002
  type: paper
  title: 'RUKA: Rethinking the Design of Humanoid Hands with Learning'
  url: https://arxiv.org/abs/2504.13165
  date: '2025'
  accessed_at: '2026-06-24'
theoretical_depth:
- system
---

# Robotis

## 抽象

> **生活实例**：它就像机器人界的“乐高舵机供应商”——把电机、减速器、控制器和通信接口装进一个模块里，研究者可以像搭积木一样拼接出机器手或机器臂。

> **自然语言逻辑**：Robotis 是韩国机器人公司，以 Dynamixel 系列智能执行器闻名；这些模块化的舵机集成了电机、减速齿轮、驱动器和反馈传感器，通过串行总线级联，广泛用于研究型机器人、教育平台和人形灵巧手。

## Overview

Robotis is a South Korean robotics company founded in 1999. It is best known for the Dynamixel line of smart actuators, which integrate a motor, reducer, driver, and communication bus in a single package. Dynamixel servos are common in research robots, manipulators, and dexterous hands because of their modularity, feedback capabilities, and broad software support.

## Key Products

- **Dynamixel X series**: Modular smart actuators with position, velocity, current, and temperature feedback.
- **Dynamixel XL330-M288-T**: Low-cost, compact servo used in smaller robotic mechanisms.
- **Dynamixel XM430-W210-T**: Mid-size servo used in research manipulators and hands.
- **TurtleBot**: Popular open-source mobile robot platform co-developed for education and research.

## Relevance to Humanoid Robotics

Robotis actuators are frequently used in research-grade humanoid hands and arms, including prototypes evaluated in papers such as RUKA. Their availability and documentation make them a practical option for early-stage humanoid hardware development.
