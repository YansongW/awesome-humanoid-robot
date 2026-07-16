---
$id: ent_paper_state_nav_stability_aware_trav_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain'
  zh: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain'
  ko: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain'
summary:
  en: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain is a 2025 work on navigation
    for humanoid robots, with open-source code available.'
  zh: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain is a 2025 work on navigation
    for humanoid robots, with open-source code available.'
  ko: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain is a 2025 work on navigation
    for humanoid robots, with open-source code available.'
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
- navigation
- state_nav
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.01046v4.
sources:
- id: src_001
  type: paper
  title: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain (arXiv)'
  url: https://arxiv.org/abs/2506.01046
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Bipedal robots have advantages in maneuvering human-centered environments, but face greater failure risk compared to other stable mobile platforms such as wheeled or quadrupedal robots. While learning-based traversability has been widely studied for these platforms, bipedal traversability has instead relied on manually designed rules with limited consideration of locomotion stability on rough terrain. In this work, we present the first learning-based traversability estimation and risk-sensitive navigation framework for bipedal robots operating in diverse, uneven environments. TravFormer, a transformer-based neural network, is trained to predict bipedal instability with uncertainty, enabling risk-aware and adaptive planning. Based on the network, we define traversability as stability-aware command velocity-the fastest command velocity that keeps instability below a user-defined limit. This velocity-based traversability is integrated into a hierarchical planner that combines traversability-informed Rapid Random Tree Star (TravRRT*) for time-efficient planning and Model Predictive Control (MPC) for safe execution. We validate our method in MuJoCo simulation and the real world, demonstrating improved navigation performance, with enhanced robustness and time efficiency across varying terrains compared to existing methods.

## 核心内容
Bipedal robots have advantages in maneuvering human-centered environments, but face greater failure risk compared to other stable mobile platforms such as wheeled or quadrupedal robots. While learning-based traversability has been widely studied for these platforms, bipedal traversability has instead relied on manually designed rules with limited consideration of locomotion stability on rough terrain. In this work, we present the first learning-based traversability estimation and risk-sensitive navigation framework for bipedal robots operating in diverse, uneven environments. TravFormer, a transformer-based neural network, is trained to predict bipedal instability with uncertainty, enabling risk-aware and adaptive planning. Based on the network, we define traversability as stability-aware command velocity-the fastest command velocity that keeps instability below a user-defined limit. This velocity-based traversability is integrated into a hierarchical planner that combines traversability-informed Rapid Random Tree Star (TravRRT*) for time-efficient planning and Model Predictive Control (MPC) for safe execution. We validate our method in MuJoCo simulation and the real world, demonstrating improved navigation performance, with enhanced robustness and time efficiency across varying terrains compared to existing methods.

## 参考
- http://arxiv.org/abs/2506.01046v4

## Overview
Bipedal robots have advantages in maneuvering human-centered environments, but face greater failure risk compared to other stable mobile platforms such as wheeled or quadrupedal robots. While learning-based traversability has been widely studied for these platforms, bipedal traversability has instead relied on manually designed rules with limited consideration of locomotion stability on rough terrain. In this work, we present the first learning-based traversability estimation and risk-sensitive navigation framework for bipedal robots operating in diverse, uneven environments. TravFormer, a transformer-based neural network, is trained to predict bipedal instability with uncertainty, enabling risk-aware and adaptive planning. Based on the network, we define traversability as stability-aware command velocity—the fastest command velocity that keeps instability below a user-defined limit. This velocity-based traversability is integrated into a hierarchical planner that combines traversability-informed Rapid Random Tree Star (TravRRT*) for time-efficient planning and Model Predictive Control (MPC) for safe execution. We validate our method in MuJoCo simulation and the real world, demonstrating improved navigation performance, with enhanced robustness and time efficiency across varying terrains compared to existing methods.

## Content
Bipedal robots have advantages in maneuvering human-centered environments, but face greater failure risk compared to other stable mobile platforms such as wheeled or quadrupedal robots. While learning-based traversability has been widely studied for these platforms, bipedal traversability has instead relied on manually designed rules with limited consideration of locomotion stability on rough terrain. In this work, we present the first learning-based traversability estimation and risk-sensitive navigation framework for bipedal robots operating in diverse, uneven environments. TravFormer, a transformer-based neural network, is trained to predict bipedal instability with uncertainty, enabling risk-aware and adaptive planning. Based on the network, we define traversability as stability-aware command velocity—the fastest command velocity that keeps instability below a user-defined limit. This velocity-based traversability is integrated into a hierarchical planner that combines traversability-informed Rapid Random Tree Star (TravRRT*) for time-efficient planning and Model Predictive Control (MPC) for safe execution. We validate our method in MuJoCo simulation and the real world, demonstrating improved navigation performance, with enhanced robustness and time efficiency across varying terrains compared to existing methods.

## 개요
이족 보행 로봇은 인간 중심 환경에서 기동하는 데 장점이 있지만, 바퀴 달린 로봇이나 사족 보행 로봇과 같은 안정적인 이동 플랫폼에 비해 더 큰 고장 위험에 직면합니다. 학습 기반 주행 가능성은 이러한 플랫폼에서 널리 연구되어 왔지만, 이족 보행 로봇의 주행 가능성은 거친 지형에서의 이동 안정성에 대한 고려가 제한된 수동 설계 규칙에 의존해 왔습니다. 본 연구에서는 다양한 불균일 환경에서 작동하는 이족 보행 로봇을 위한 최초의 학습 기반 주행 가능성 추정 및 위험 민감 내비게이션 프레임워크를 제시합니다. TravFormer는 트랜스포머 기반 신경망으로, 불확실성을 고려하여 이족 보행 불안정성을 예측하도록 훈련되어 위험 인식 및 적응형 계획을 가능하게 합니다. 이 네트워크를 기반으로, 주행 가능성을 안정성 인식 명령 속도, 즉 불안정성을 사용자 정의 한계 이하로 유지하는 가장 빠른 명령 속도로 정의합니다. 이 속도 기반 주행 가능성은 시간 효율적인 계획을 위한 주행 가능성 인식 Rapid Random Tree Star(TravRRT*)와 안전한 실행을 위한 모델 예측 제어(MPC)를 결합한 계층적 플래너에 통합됩니다. 우리는 MuJoCo 시뮬레이션과 실제 환경에서 이 방법을 검증하여, 기존 방법과 비교해 다양한 지형에서 향상된 견고성과 시간 효율성을 갖춘 개선된 내비게이션 성능을 입증했습니다.

## 핵심 내용
이족 보행 로봇은 인간 중심 환경에서 기동하는 데 장점이 있지만, 바퀴 달린 로봇이나 사족 보행 로봇과 같은 안정적인 이동 플랫폼에 비해 더 큰 고장 위험에 직면합니다. 학습 기반 주행 가능성은 이러한 플랫폼에서 널리 연구되어 왔지만, 이족 보행 로봇의 주행 가능성은 거친 지형에서의 이동 안정성에 대한 고려가 제한된 수동 설계 규칙에 의존해 왔습니다. 본 연구에서는 다양한 불균일 환경에서 작동하는 이족 보행 로봇을 위한 최초의 학습 기반 주행 가능성 추정 및 위험 민감 내비게이션 프레임워크를 제시합니다. TravFormer는 트랜스포머 기반 신경망으로, 불확실성을 고려하여 이족 보행 불안정성을 예측하도록 훈련되어 위험 인식 및 적응형 계획을 가능하게 합니다. 이 네트워크를 기반으로, 주행 가능성을 안정성 인식 명령 속도, 즉 불안정성을 사용자 정의 한계 이하로 유지하는 가장 빠른 명령 속도로 정의합니다. 이 속도 기반 주행 가능성은 시간 효율적인 계획을 위한 주행 가능성 인식 Rapid Random Tree Star(TravRRT*)와 안전한 실행을 위한 모델 예측 제어(MPC)를 결합한 계층적 플래너에 통합됩니다. 우리는 MuJoCo 시뮬레이션과 실제 환경에서 이 방법을 검증하여, 기존 방법과 비교해 다양한 지형에서 향상된 견고성과 시간 효율성을 갖춘 개선된 내비게이션 성능을 입증했습니다.
