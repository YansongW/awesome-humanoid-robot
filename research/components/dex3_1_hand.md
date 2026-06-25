---
$id: ent_component_unitree_dex3_1_hand
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Unitree Dex3-1 Dexterous Hand
  zh: Unitree Dex3-1 灵巧手
  ko: Unitree Dex3-1 민첩한 손
summary:
  en: A force-controlled, three-fingered dexterous end effector option for the Unitree G1-EDU
    humanoid robot, adding 7+2 degrees of freedom per hand for object manipulation.
  zh: Unitree G1-EDU 人形机器人的力控三指灵巧末端执行器选件，每只手增加 7+2 个自由度用于物体操作。
  ko: Unitree G1-EDU 휴머노이드 로봇을 위한 힘 제어식 3지 민첩한 엔드 이펙터 옵션으로, 물체 조작을 위해 손당 7+2자유도를 추가함.
domains:
- 02_components
- 06_design_engineering
- 11_applications_markets
layers:
- upstream
- midstream
functional_roles:
- component
- knowledge
tags:
- unitree
- dex3_1
- dexterous_hand
- end_effector
- force_control
- three_finger
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: medium
  notes: Specifications sourced from Unitree reseller listings and official documentation;
    tactile sensor availability depends on EDU Smart variant.
sources:
- id: src_001
  type: website
  title: Unitree G1 Developer Specifications
  url: https://support.unitree.com/home/en/G1_developer
  date: '2026'
  accessed_at: '2026-06-22'
- id: src_002
  type: paper
  title: Identification of a Physics-Based Electrical Power Consumption Model for the
    Unitree G1 Humanoid Arm
  url: https://arxiv.org/abs/2606.15915
  date: '2026'
  accessed_at: '2026-06-22'
---

# Unitree Dex3-1 Dexterous Hand

## 抽象

> **生活实例**：它就像一只鹰爪或机械三指钳——用三根手指配合力控，既能轻轻握住一颗鸡蛋，也能稳稳抓起一把扳手。

> **自然语言逻辑**：Unitree Dex3-1 是 Unitree G1-EDU 的可选三指力控灵巧手，每只手提供 7 个主动自由度（可选 2 个腕部自由度）；它通过力-位混合控制，让机器人能够抓握不同形状和硬度的物体，把人形机器人的操作能力从简单夹持扩展到复杂抓取。

## Overview

The Unitree Dex3-1 is a three-fingered, force-controlled dexterous hand designed as an optional end effector for the Unitree G1-EDU humanoid robot. Each hand provides 7 active degrees of freedom in the fingers, with some configurations adding 2 additional wrist degrees of freedom. The hand uses force-position hybrid control to grasp and manipulate objects of varying shapes and stiffness.

The Dex3-1 enables the G1 platform to perform contact-rich manipulation tasks beyond simple gripping. It is offered in variants with and without fingertip tactile sensing. Because adding two Dex3-1 hands increases the total robot DoF from 23 to 43, it is a key hardware option for researchers studying bimanual dexterous manipulation.

## Key Characteristics

- Three-fingered anthropomorphic layout
- 7 active DoF per hand (plus optional 2-DoF wrist)
- Force-position hybrid control
- Optional tactile fingertip sensors (EDU Smart variant)
- Used on Unitree G1-EDU humanoid robot

## Relevance to Humanoid Robotics

The Dex3-1 illustrates the trade-offs involved in integrating dexterous end effectors into a mass-market humanoid platform: added degrees of freedom increase manipulation capability but also raise control complexity, wiring, power consumption, and cost. It serves as a concrete reference point for end-effector selection in humanoid system design.
