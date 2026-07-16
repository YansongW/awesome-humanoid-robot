---
$id: ent_paper_jaeger_dual_level_humanoid_who_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'JAEGER: Dual-Level Humanoid Whole-Body Controller'
  zh: 'JAEGER: Dual-Level Humanoid Whole-Body Controller'
  ko: 'JAEGER: Dual-Level Humanoid Whole-Body Controller'
summary:
  en: 'JAEGER: Dual-Level Humanoid Whole-Body Controller is a 2025 work on loco-manipulation and whole-body-control for humanoid
    robots.'
  zh: 'JAEGER: Dual-Level Humanoid Whole-Body Controller is a 2025 work on loco-manipulation and whole-body-control for humanoid
    robots.'
  ko: 'JAEGER: Dual-Level Humanoid Whole-Body Controller is a 2025 work on loco-manipulation and whole-body-control for humanoid
    robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- jaeger
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.06584v2.
sources:
- id: src_001
  type: paper
  title: 'JAEGER: Dual-Level Humanoid Whole-Body Controller (arXiv)'
  url: https://arxiv.org/abs/2505.06584
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This paper presents JAEGER, a dual-level whole-body controller for humanoid robots that addresses the challenges of training a more robust and versatile policy. Unlike traditional single-controller approaches, JAEGER separates the control of the upper and lower bodies into two independent controllers, so that they can better focus on their distinct tasks. This separation alleviates the dimensionality curse and improves fault tolerance. JAEGER supports both root velocity tracking (coarse-grained control) and local joint angle tracking (fine-grained control), enabling versatile and stable movements. To train the controller, we utilize a human motion dataset (AMASS), retargeting human poses to humanoid poses through an efficient retargeting network, and employ a curriculum learning approach. This method performs supervised learning for initialization, followed by reinforcement learning for further exploration. We conduct our experiments on two humanoid platforms and demonstrate the superiority of our approach against state-of-the-art methods in both simulation and real environments.

## 核心内容
This paper presents JAEGER, a dual-level whole-body controller for humanoid robots that addresses the challenges of training a more robust and versatile policy. Unlike traditional single-controller approaches, JAEGER separates the control of the upper and lower bodies into two independent controllers, so that they can better focus on their distinct tasks. This separation alleviates the dimensionality curse and improves fault tolerance. JAEGER supports both root velocity tracking (coarse-grained control) and local joint angle tracking (fine-grained control), enabling versatile and stable movements. To train the controller, we utilize a human motion dataset (AMASS), retargeting human poses to humanoid poses through an efficient retargeting network, and employ a curriculum learning approach. This method performs supervised learning for initialization, followed by reinforcement learning for further exploration. We conduct our experiments on two humanoid platforms and demonstrate the superiority of our approach against state-of-the-art methods in both simulation and real environments.

## 参考
- http://arxiv.org/abs/2505.06584v2

## Overview
This paper presents JAEGER, a dual-level whole-body controller for humanoid robots that addresses the challenges of training a more robust and versatile policy. Unlike traditional single-controller approaches, JAEGER separates the control of the upper and lower bodies into two independent controllers, so that they can better focus on their distinct tasks. This separation alleviates the dimensionality curse and improves fault tolerance. JAEGER supports both root velocity tracking (coarse-grained control) and local joint angle tracking (fine-grained control), enabling versatile and stable movements. To train the controller, we utilize a human motion dataset (AMASS), retargeting human poses to humanoid poses through an efficient retargeting network, and employ a curriculum learning approach. This method performs supervised learning for initialization, followed by reinforcement learning for further exploration. We conduct our experiments on two humanoid platforms and demonstrate the superiority of our approach against state-of-the-art methods in both simulation and real environments.

## Content
This paper presents JAEGER, a dual-level whole-body controller for humanoid robots that addresses the challenges of training a more robust and versatile policy. Unlike traditional single-controller approaches, JAEGER separates the control of the upper and lower bodies into two independent controllers, so that they can better focus on their distinct tasks. This separation alleviates the dimensionality curse and improves fault tolerance. JAEGER supports both root velocity tracking (coarse-grained control) and local joint angle tracking (fine-grained control), enabling versatile and stable movements. To train the controller, we utilize a human motion dataset (AMASS), retargeting human poses to humanoid poses through an efficient retargeting network, and employ a curriculum learning approach. This method performs supervised learning for initialization, followed by reinforcement learning for further exploration. We conduct our experiments on two humanoid platforms and demonstrate the superiority of our approach against state-of-the-art methods in both simulation and real environments.

## 개요
본 논문은 인간형 로봇을 위한 이중 수준 전신 제어기 JAEGER를 제시하며, 보다 강건하고 다재다능한 정책을 훈련하는 데 따르는 과제를 해결합니다. 기존의 단일 제어기 접근법과 달리 JAEGER는 상체와 하체의 제어를 두 개의 독립적인 제어기로 분리하여 각각의 고유한 작업에 더 집중할 수 있도록 합니다. 이러한 분리는 차원의 저주를 완화하고 내결함성을 향상시킵니다. JAEGER는 루트 속도 추적(세분화된 제어)과 로컬 관절 각도 추적(미세 제어)을 모두 지원하여 다재다능하고 안정적인 움직임을 가능하게 합니다. 제어기를 훈련하기 위해 인간 동작 데이터셋(AMASS)을 활용하고, 효율적인 리타겟팅 네트워크를 통해 인간 자세를 인간형 로봇 자세로 변환하며, 커리큘럼 학습 접근법을 사용합니다. 이 방법은 초기화를 위한 지도 학습을 수행한 후, 추가 탐색을 위한 강화 학습을 진행합니다. 우리는 두 개의 인간형 로봇 플랫폼에서 실험을 수행하고, 시뮬레이션 및 실제 환경 모두에서 최신 방법보다 우리 접근법의 우수성을 입증합니다.

## 핵심 내용
본 논문은 인간형 로봇을 위한 이중 수준 전신 제어기 JAEGER를 제시하며, 보다 강건하고 다재다능한 정책을 훈련하는 데 따르는 과제를 해결합니다. 기존의 단일 제어기 접근법과 달리 JAEGER는 상체와 하체의 제어를 두 개의 독립적인 제어기로 분리하여 각각의 고유한 작업에 더 집중할 수 있도록 합니다. 이러한 분리는 차원의 저주를 완화하고 내결함성을 향상시킵니다. JAEGER는 루트 속도 추적(세분화된 제어)과 로컬 관절 각도 추적(미세 제어)을 모두 지원하여 다재다능하고 안정적인 움직임을 가능하게 합니다. 제어기를 훈련하기 위해 인간 동작 데이터셋(AMASS)을 활용하고, 효율적인 리타겟팅 네트워크를 통해 인간 자세를 인간형 로봇 자세로 변환하며, 커리큘럼 학습 접근법을 사용합니다. 이 방법은 초기화를 위한 지도 학습을 수행한 후, 추가 탐색을 위한 강화 학습을 진행합니다. 우리는 두 개의 인간형 로봇 플랫폼에서 실험을 수행하고, 시뮬레이션 및 실제 환경 모두에서 최신 방법보다 우리 접근법의 우수성을 입증합니다.
