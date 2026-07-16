---
$id: ent_paper_hwc_loco_a_hierarchical_whole_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion'
  zh: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion'
  ko: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion'
summary:
  en: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion is a 2025 work on locomotion for
    humanoid robots.'
  zh: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion is a 2025 work on locomotion for
    humanoid robots.'
  ko: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion is a 2025 work on locomotion for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- hwc_loco
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.00923v3.
sources:
- id: src_001
  type: paper
  title: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion (arXiv)'
  url: https://arxiv.org/abs/2503.00923
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion project page'
  url: https://simonlinsx.github.io/HWC_Loco/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots, capable of assuming human roles in various workplaces, have become essential to embodied intelligence. However, as robots with complex physical structures, learning a control model that can operate robustly across diverse environments remains inherently challenging, particularly under the discrepancies between training and deployment environments. In this study, we propose HWC-Loco, a robust whole-body control algorithm tailored for humanoid locomotion tasks. By reformulating policy learning as a robust optimization problem, HWC-Loco explicitly learns to recover from safety-critical scenarios. While prioritizing safety guarantees, overly conservative behavior can compromise the robot's ability to complete the given tasks. To tackle this challenge, HWC-Loco leverages a hierarchical policy for robust control. This policy can dynamically resolve the trade-off between goal-tracking and safety recovery, guided by human behavior norms and dynamic constraints. To evaluate the performance of HWC-Loco, we conduct extensive comparisons against state-of-the-art humanoid control models, demonstrating HWC-Loco's superior performance across diverse terrains, robot structures, and locomotion tasks under both simulated and real-world environments.

## 核心内容
Humanoid robots, capable of assuming human roles in various workplaces, have become essential to embodied intelligence. However, as robots with complex physical structures, learning a control model that can operate robustly across diverse environments remains inherently challenging, particularly under the discrepancies between training and deployment environments. In this study, we propose HWC-Loco, a robust whole-body control algorithm tailored for humanoid locomotion tasks. By reformulating policy learning as a robust optimization problem, HWC-Loco explicitly learns to recover from safety-critical scenarios. While prioritizing safety guarantees, overly conservative behavior can compromise the robot's ability to complete the given tasks. To tackle this challenge, HWC-Loco leverages a hierarchical policy for robust control. This policy can dynamically resolve the trade-off between goal-tracking and safety recovery, guided by human behavior norms and dynamic constraints. To evaluate the performance of HWC-Loco, we conduct extensive comparisons against state-of-the-art humanoid control models, demonstrating HWC-Loco's superior performance across diverse terrains, robot structures, and locomotion tasks under both simulated and real-world environments.

## 参考
- http://arxiv.org/abs/2503.00923v3

## Overview
Humanoid robots, capable of assuming human roles in various workplaces, have become essential to embodied intelligence. However, as robots with complex physical structures, learning a control model that can operate robustly across diverse environments remains inherently challenging, particularly under the discrepancies between training and deployment environments. In this study, we propose HWC-Loco, a robust whole-body control algorithm tailored for humanoid locomotion tasks. By reformulating policy learning as a robust optimization problem, HWC-Loco explicitly learns to recover from safety-critical scenarios. While prioritizing safety guarantees, overly conservative behavior can compromise the robot's ability to complete the given tasks. To tackle this challenge, HWC-Loco leverages a hierarchical policy for robust control. This policy can dynamically resolve the trade-off between goal-tracking and safety recovery, guided by human behavior norms and dynamic constraints. To evaluate the performance of HWC-Loco, we conduct extensive comparisons against state-of-the-art humanoid control models, demonstrating HWC-Loco's superior performance across diverse terrains, robot structures, and locomotion tasks under both simulated and real-world environments.

## Content
Humanoid robots, capable of assuming human roles in various workplaces, have become essential to embodied intelligence. However, as robots with complex physical structures, learning a control model that can operate robustly across diverse environments remains inherently challenging, particularly under the discrepancies between training and deployment environments. In this study, we propose HWC-Loco, a robust whole-body control algorithm tailored for humanoid locomotion tasks. By reformulating policy learning as a robust optimization problem, HWC-Loco explicitly learns to recover from safety-critical scenarios. While prioritizing safety guarantees, overly conservative behavior can compromise the robot's ability to complete the given tasks. To tackle this challenge, HWC-Loco leverages a hierarchical policy for robust control. This policy can dynamically resolve the trade-off between goal-tracking and safety recovery, guided by human behavior norms and dynamic constraints. To evaluate the performance of HWC-Loco, we conduct extensive comparisons against state-of-the-art humanoid control models, demonstrating HWC-Loco's superior performance across diverse terrains, robot structures, and locomotion tasks under both simulated and real-world environments.

## 개요
휴머노이드 로봇은 다양한 작업 현장에서 인간의 역할을 대체할 수 있는 능력을 갖추며, 구현된 지능(embodied intelligence)의 핵심 요소가 되었습니다. 그러나 복잡한 물리적 구조를 가진 로봇이 다양한 환경에서 강건하게 작동할 수 있는 제어 모델을 학습하는 것은, 특히 훈련 환경과 배포 환경 간의 차이가 존재할 때 본질적으로 어려운 과제입니다. 본 연구에서는 휴머노이드 보행 작업에 특화된 강건한 전신 제어 알고리즘인 HWC-Loco를 제안합니다. 정책 학습을 강건 최적화 문제로 재구성함으로써, HWC-Loco는 안전이 중요한 시나리오에서 회복하는 방법을 명시적으로 학습합니다. 안전 보장을 우선시하는 과정에서 지나치게 보수적인 행동은 로봇이 주어진 작업을 완료하는 능력을 저하시킬 수 있습니다. 이 문제를 해결하기 위해 HWC-Loco는 계층적 정책을 활용한 강건 제어를 도입합니다. 이 정책은 인간 행동 규범과 동적 제약 조건에 따라 목표 추적과 안전 회복 간의 균형을 동적으로 조정할 수 있습니다. HWC-Loco의 성능을 평가하기 위해 최신 휴머노이드 제어 모델과의 광범위한 비교를 수행하였으며, 시뮬레이션 및 실제 환경 모두에서 다양한 지형, 로봇 구조 및 보행 작업에서 HWC-Loco의 우수한 성능을 입증했습니다.

## 핵심 내용
휴머노이드 로봇은 다양한 작업 현장에서 인간의 역할을 대체할 수 있는 능력을 갖추며, 구현된 지능의 핵심 요소가 되었습니다. 그러나 복잡한 물리적 구조를 가진 로봇이 다양한 환경에서 강건하게 작동할 수 있는 제어 모델을 학습하는 것은, 특히 훈련 환경과 배포 환경 간의 차이가 존재할 때 본질적으로 어려운 과제입니다. 본 연구에서는 휴머노이드 보행 작업에 특화된 강건한 전신 제어 알고리즘인 HWC-Loco를 제안합니다. 정책 학습을 강건 최적화 문제로 재구성함으로써, HWC-Loco는 안전이 중요한 시나리오에서 회복하는 방법을 명시적으로 학습합니다. 안전 보장을 우선시하는 과정에서 지나치게 보수적인 행동은 로봇이 주어진 작업을 완료하는 능력을 저하시킬 수 있습니다. 이 문제를 해결하기 위해 HWC-Loco는 계층적 정책을 활용한 강건 제어를 도입합니다. 이 정책은 인간 행동 규범과 동적 제약 조건에 따라 목표 추적과 안전 회복 간의 균형을 동적으로 조정할 수 있습니다. HWC-Loco의 성능을 평가하기 위해 최신 휴머노이드 제어 모델과의 광범위한 비교를 수행하였으며, 시뮬레이션 및 실제 환경 모두에서 다양한 지형, 로봇 구조 및 보행 작업에서 HWC-Loco의 우수한 성능을 입증했습니다.
