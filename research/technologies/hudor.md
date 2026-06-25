---
$id: ent_hudor
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: dataset
names:
  en: HuDOR
  zh: HuDOR
  ko: HuDOR
summary:
  en: A human-to-robot demonstration dataset or teleoperation framework used to collect
    human hand motion data for training imitation-learning policies on dexterous robot
    hands.
  zh: 一种用于采集人手动作数据以训练灵巧机器人手模仿学习策略的人类到机器人演示数据集或遥操作框架。
  ko: 능숙한 로봇 손의 모방 학습 정책을 훈련하기 위해 인간 손 동작 데이터를 수집하는 데 사용되는 인간-로봇 시연 데이터 세트 또는 원격 조작 프레임워크입니다.
domains:
- 09_data_datasets
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hudor
- teleoperation
- imitation_learning
- dataset
- dexterous_manipulation
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: Mentioned in the RUKA paper as the source of teleoperation/imitation-learning demonstrations;
    exact scope and public availability should be verified.
sources:
- id: src_001
  type: paper
  title: 'RUKA: Rethinking the Design of Humanoid Hands with Learning'
  url: https://arxiv.org/abs/2504.13165
  date: '2025'
  accessed_at: '2026-06-25'
---

# HuDOR

## 生活实例 + 自然语言阐述逻辑

> **生活实例**：它就像一套“人手动作录像教材”——记录真人如何拧瓶盖、叠衣服、拿杯子，然后把这些示范转换成机器人手能学习的动作数据。

> **自然语言逻辑**：HuDOR 是一种人类到机器人的演示数据集或遥操作框架，提供人手运动数据用于训练灵巧机器人手的模仿学习策略；它把人类示范与机器人控制连接起来，帮助低成本、基于学习的机器手掌握复杂的抓握与操作技能。

## Overview

HuDOR appears in the RUKA paper as the data source or framework for teleoperation and imitation-learning demonstrations. It provides human hand-motion data that is used to train controllers for the RUKA tendon-driven hand.

## Relevance to Humanoid Robotics

Teleoperation and imitation learning are key data-collection paradigms for training dexterous manipulation policies. HuDOR-like datasets help bridge human demonstration and robot control for low-cost, learning-based hands.
