---
$id: ent_component_manufacturer_wonik_robotics
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component_manufacturer
names:
  en: Wonik Robotics
  zh: Wonik Robotics
  ko: 원익로보틱스
summary:
  en: South Korean robotics company manufacturing the Allegro Hand, a widely used
    research-grade multi-fingered robot hand.
  zh: 韩国机器人公司，生产 Allegro Hand，一种广泛使用的研究级多指机器人手。
  ko: 연구용 다지향 로봇 손인 Allegro Hand를 제조하는 한국 로봇 기업입니다.
domains:
- 02_components
- 11_applications_markets
layers:
- upstream
- validation_markets
functional_roles:
- organization
- component
tags:
- wonik
- allegro_hand
- robot_hand
- dexterous_manipulation
- research
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-24'
  confidence: high
  notes: Product specifications are available on the official Allegro Hand product
    page.
sources:
- id: src_001
  type: website
  title: Allegro Hand Official Product Page
  url: https://www.allegrohand.com/
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

# Wonik Robotics

## 抽象

> **生活实例**：它就像一家专门制作高端仿生假手的工作室，把产品卖给大学和实验室，让研究人员测试各种抓握和操作方法。

> **自然语言逻辑**：Wonik Robotics 是韩国机器人公司，生产研究级多指灵巧手 Allegro Hand；它为人形机器人末端执行器研究提供了稳定、可重复的硬件基准，常被用来与 LEAP Hand、Dex3-1 等新型手进行比较。

## Overview

Wonik Robotics is a South Korean company that develops robotic hands and related components. Its Allegro Hand is one of the most common research-grade multi-fingered hands used in dexterous manipulation research. The hand is electrically actuated and features 16 independent degrees of freedom.

## Key Products

- **Allegro Hand**: 16-DOF four-fingered robot hand used in grasping, in-hand manipulation, and teleoperation research.
- **Allegro Hand V4**: Updated version with improved finger design and sensing options.

## Relevance to Humanoid Robotics

The Allegro Hand is a frequent baseline in dexterous manipulation papers and is often compared to newer hands such as LEAP Hand, Dex3-1, and RUKA. Its widespread use makes it a useful reference point for evaluating hand cost, reliability, and manipulation capability in humanoid robot design.
