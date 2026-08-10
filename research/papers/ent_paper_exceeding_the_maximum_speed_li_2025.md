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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.12808v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    en/ko body retranslated from zh deep-read (457 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2502.12808v1

## Overview
Musculoskeletal humanoid robots offer multiple biomimetic advantages, with redundant muscle configuration being one of the most important features. This redundancy enables fail-safe redundant actuation and variable stiffness control. However, the slowest muscle among the redundant muscles limits the maximum joint angular velocity. This study proposes two methods to overcome this velocity limitation and validates their effectiveness through experiments on an actual robot.

## Content
### Research Background
- Musculoskeletal humanoid robots achieve biomimetic characteristics through redundant tendon-driven structures, including fail-safe redundant actuation and variable stiffness control.
- Key issue: The slowest muscle among the redundant muscles becomes a bottleneck, limiting the maximum joint angular velocity.

### Proposed Methods
- Method 1: Optimize tendon paths or adjust actuation strategies to enable redundant muscles to work collaboratively, overcoming the velocity limitation of a single muscle.
- Method 2: Utilize a collaborative control algorithm for redundant muscles to dynamically allocate loads, thereby enhancing overall joint velocity.

### Experimental Validation
- Experiments were conducted on an actual robot platform, demonstrating that both methods effectively surpass traditional velocity limitations.
- Experimental results show a significant improvement in joint angular velocity without compromising system stability or safety.

### Conclusion
- This study provides new insights for high-speed motion control of musculoskeletal humanoid robots, expanding the application potential of redundant tendon-driven structures.

## 개요
근골격계 휴머노이드 로봇은 다양한 생체모방적 장점을 가지며, 그중에서도 중복 근육 배치는 가장 중요한 특징 중 하나입니다. 이러한 중복성은 고장 안전 중복 구동과 가변 강성 제어를 가능하게 합니다. 그러나 중복 근육 중 가장 느린 근육이 최대 관절 각속도를 제한합니다. 본 연구는 이러한 속도 제한을突破하기 위해 두 가지 방법을 제안하고, 실제 로봇 실험을 통해 그 유효성을 검증했습니다.

## 핵심 내용
### 연구 배경
- 근골격계 휴머노이드 로봇은 중복 힘줄 구동 구조를 통해 생체모방적 특성을 구현하며, 여기에는 고장 안전 중복 구동과 가변 강성 제어가 포함됩니다.
- 핵심 문제: 중복 근육 중 가장 느린 근육이 병목 현상이 되어 최대 관절 각속도를 제한합니다.

### 제안 방법
- 방법 1: 힘줄 경로 최적화 또는 구동 전략 조정을 통해 중복 근육이 협력적으로 작동하도록 하여 단일 근육의 속도 제한을突破합니다.
- 방법 2: 중복 근육의 협력 제어 알고리즘을 활용하여 부하를 동적으로 분배함으로써 전체 관절 속도를 향상시킵니다.

### 실험 검증
- 실제 로봇 플랫폼에서 실험을 수행하여 두 방법 모두 기존 속도 제한을 효과적으로 초과할 수 있음을 검증했습니다.
- 실험 결과, 관절 각속도가 크게 향상되었으며 시스템 안정성이나 안전성을 희생하지 않았습니다.

### 결론
- 본 연구는 근골격계 휴머노이드 로봇의 고속 운동 제어에 새로운 접근 방식을 제공하며, 중복 힘줄 구동 구조의 응용 잠재력을 확장했습니다.
