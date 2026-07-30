---
$id: ent_paper_exceeding_the_maximum_speed_li_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Exceeding the Maximum Speed Limit of the Joint Angle for the Redundant Tendon-driven Structures of Musculoskeletal Humanoids
  zh: Exceeding the Maximum Speed Limit of the Joint Angle for the Redundant Tendon-driven Structures of Musculoskeletal Humanoids
  ko: Exceeding the Maximum Speed Limit of the Joint Angle for the Redundant Tendon-driven Structures of Musculoskeletal Humanoids
summary:
  en: Exceeding the Maximum Speed Limit of the Joint Angle for the Redundant Tendon-driven Structures of Musculoskeletal Humanoids
    is a 2025 work on hardware design for humanoid robots.
  zh: 这是一篇2025年的硬件设计研究，针对肌肉骨骼人形机器人冗余肌腱驱动结构，提出两种方法以突破冗余肌肉中速度最慢者所限制的最大关节角速度，并通过实际机器人实验验证了其有效性。
  ko: Exceeding the Maximum Speed Limit of the Joint Angle for the Redundant Tendon-driven Structures of Musculoskeletal Humanoids
    is a 2025 work on hardware design for humanoid robots.
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- exceeding_the_maximum_speed_li
- hardware_design
- humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.12808v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Exceeding the Maximum Speed Limit of the Joint Angle for the Redundant Tendon-driven Structures of Musculoskeletal
    Humanoids (arXiv)
  url: https://arxiv.org/abs/2502.12808
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
肌肉骨骼人形机器人具有多种仿生优势，其中冗余肌肉配置是最重要的特征之一。这种冗余性可实现故障安全冗余驱动和可变刚度控制。然而，冗余肌肉中速度最慢的肌肉会限制最大关节角速度。本研究提出两种方法以突破这一速度限制，并通过实际机器人实验验证了其有效性。

## 核心内容
### 研究背景
- 肌肉骨骼人形机器人通过冗余肌腱驱动结构实现仿生特性，包括故障安全冗余驱动和可变刚度控制。
- 关键问题：冗余肌肉中速度最慢的肌肉成为瓶颈，限制了最大关节角速度。

### 提出方法
- 方法一：通过优化肌腱路径或调整驱动策略，使冗余肌肉协同工作，突破单块肌肉的速度限制。
- 方法二：利用冗余肌肉的协同控制算法，动态分配负载以提升整体关节速度。

### 实验验证
- 在实际机器人平台上进行实验，验证两种方法均能有效超越传统速度限制。
- 实验结果表明，关节角速度显著提升，且未牺牲系统稳定性或安全性。

### 结论
- 本研究为肌肉骨骼人形机器人的高速运动控制提供了新思路，扩展了冗余肌腱驱动结构的应用潜力。

## Overview
The musculoskeletal humanoid has various biomimetic benefits, and the redundant muscle arrangement is one of its most important characteristics. This redundancy can achieve fail-safe redundant actuation and variable stiffness control. However, there is a problem that the maximum joint angle velocity is limited by the slowest muscle among the redundant muscles. In this study, we propose two methods that can exceed the limited maximum joint angle velocity, and verify the effectiveness with actual robot experiments.

## 개요
근골격계 휴머노이드는 다양한 생체모방적 이점을 가지며, 그중에서도 중복된 근육 배열은 가장 중요한 특징 중 하나입니다. 이러한 중복성은 페일세이프(fail-safe) 중복 구동과 가변 강도 제어를 가능하게 합니다. 그러나 중복된 근육 중 가장 느린 근육에 의해 최대 관절 각속도가 제한되는 문제가 있습니다. 본 연구에서는 제한된 최대 관절 각속도를 초과할 수 있는 두 가지 방법을 제안하고, 실제 로봇 실험을 통해 그 효과를 검증합니다.

## 핵심 내용
근골격계 휴머노이드는 다양한 생체모방적 이점을 가지며, 그중에서도 중복된 근육 배열은 가장 중요한 특징 중 하나입니다. 이러한 중복성은 페일세이프(fail-safe) 중복 구동과 가변 강도 제어를 가능하게 합니다. 그러나 중복된 근육 중 가장 느린 근육에 의해 최대 관절 각속도가 제한되는 문제가 있습니다. 본 연구에서는 제한된 최대 관절 각속도를 초과할 수 있는 두 가지 방법을 제안하고, 실제 로봇 실험을 통해 그 효과를 검증합니다.

## 参考
- http://arxiv.org/abs/2502.12808v1
