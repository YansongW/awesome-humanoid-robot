---
$id: ent_paper_reference_free_sampling_based_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reference-Free Sampling-Based Model Predictive Control
  zh: Reference-Free Sampling-Based Model Predictive Control
  ko: Reference-Free Sampling-Based Model Predictive Control
summary:
  en: Reference-Free Sampling-Based Model Predictive Control is a 2025 work on locomotion for humanoid robots.
  zh: Reference-Free Sampling-Based Model Predictive Control is a 2025 work on locomotion for humanoid robots.
  ko: Reference-Free Sampling-Based Model Predictive Control is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- reference_free_sampling_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.19204v3.
sources:
- id: src_001
  type: paper
  title: Reference-Free Sampling-Based Model Predictive Control (arXiv)
  url: https://arxiv.org/abs/2511.19204
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We present a sampling-based model predictive control (MPC) framework that enables emergent locomotion without relying on handcrafted gait patterns or predefined contact sequences. Our method discovers diverse motion patterns, ranging from trotting to galloping, robust standing policies, jumping, and handstand balancing, purely through the optimization of high-level objectives. Building on model predictive path integral (MPPI), we propose a cubic Hermite spline parameterization that operates on position and velocity control points. Our approach enables contact-making and contact-breaking strategies that adapt automatically to task requirements, requiring only a limited number of sampled trajectories. This sample efficiency enables real-time control on standard CPU hardware, eliminating the GPU acceleration typically required by other state-of-the-art MPPI methods. We validate our approach on the Go2 quadrupedal robot, demonstrating a range of emergent gaits and basic jumping capabilities. In simulation, we further showcase more complex behaviors, such as backflips, dynamic handstand balancing and locomotion on a Humanoid, all without requiring reference tracking or offline pre-training.

## 核心内容
We present a sampling-based model predictive control (MPC) framework that enables emergent locomotion without relying on handcrafted gait patterns or predefined contact sequences. Our method discovers diverse motion patterns, ranging from trotting to galloping, robust standing policies, jumping, and handstand balancing, purely through the optimization of high-level objectives. Building on model predictive path integral (MPPI), we propose a cubic Hermite spline parameterization that operates on position and velocity control points. Our approach enables contact-making and contact-breaking strategies that adapt automatically to task requirements, requiring only a limited number of sampled trajectories. This sample efficiency enables real-time control on standard CPU hardware, eliminating the GPU acceleration typically required by other state-of-the-art MPPI methods. We validate our approach on the Go2 quadrupedal robot, demonstrating a range of emergent gaits and basic jumping capabilities. In simulation, we further showcase more complex behaviors, such as backflips, dynamic handstand balancing and locomotion on a Humanoid, all without requiring reference tracking or offline pre-training.

## 参考
- http://arxiv.org/abs/2511.19204v3

## Overview
We present a sampling-based model predictive control (MPC) framework that enables emergent locomotion without relying on handcrafted gait patterns or predefined contact sequences. Our method discovers diverse motion patterns, ranging from trotting to galloping, robust standing policies, jumping, and handstand balancing, purely through the optimization of high-level objectives. Building on model predictive path integral (MPPI), we propose a cubic Hermite spline parameterization that operates on position and velocity control points. Our approach enables contact-making and contact-breaking strategies that adapt automatically to task requirements, requiring only a limited number of sampled trajectories. This sample efficiency enables real-time control on standard CPU hardware, eliminating the GPU acceleration typically required by other state-of-the-art MPPI methods. We validate our approach on the Go2 quadrupedal robot, demonstrating a range of emergent gaits and basic jumping capabilities. In simulation, we further showcase more complex behaviors, such as backflips, dynamic handstand balancing and locomotion on a Humanoid, all without requiring reference tracking or offline pre-training.

## Content
We present a sampling-based model predictive control (MPC) framework that enables emergent locomotion without relying on handcrafted gait patterns or predefined contact sequences. Our method discovers diverse motion patterns, ranging from trotting to galloping, robust standing policies, jumping, and handstand balancing, purely through the optimization of high-level objectives. Building on model predictive path integral (MPPI), we propose a cubic Hermite spline parameterization that operates on position and velocity control points. Our approach enables contact-making and contact-breaking strategies that adapt automatically to task requirements, requiring only a limited number of sampled trajectories. This sample efficiency enables real-time control on standard CPU hardware, eliminating the GPU acceleration typically required by other state-of-the-art MPPI methods. We validate our approach on the Go2 quadrupedal robot, demonstrating a range of emergent gaits and basic jumping capabilities. In simulation, we further showcase more complex behaviors, such as backflips, dynamic handstand balancing and locomotion on a Humanoid, all without requiring reference tracking or offline pre-training.

## 개요
본 논문에서는 수제 보행 패턴이나 사전 정의된 접촉 순서에 의존하지 않고 창발적 보행을 가능하게 하는 샘플링 기반 모델 예측 제어(MPC) 프레임워크를 제시합니다. 우리의 방법은 높은 수준의 목표 최적화만을 통해 트로팅에서 갤럽에 이르기까지 다양한 운동 패턴, 강건한 서기 정책, 점프, 물구나무서기 균형을 발견합니다. 모델 예측 경로 적분(MPPI)을 기반으로, 위치 및 속도 제어점에서 작동하는 3차 에르미트 스플라인 매개변수화를 제안합니다. 우리의 접근 방식은 작업 요구 사항에 자동으로 적응하는 접촉 생성 및 접촉 해제 전략을 가능하게 하며, 제한된 수의 샘플링된 궤적만 필요로 합니다. 이러한 샘플 효율성은 일반 CPU 하드웨어에서 실시간 제어를 가능하게 하여, 다른 최신 MPPI 방법에서 일반적으로 요구되는 GPU 가속을 제거합니다. 우리는 Go2 사족 보행 로봇에서 접근 방식을 검증하여 다양한 창발적 보행과 기본 점프 능력을 입증합니다. 시뮬레이션에서는 참조 추적이나 오프라인 사전 훈련 없이 백플립, 동적 물구나무서기 균형, 휴머노이드 보행과 같은 더 복잡한 행동을 추가로 보여줍니다.

## 핵심 내용
본 논문에서는 수제 보행 패턴이나 사전 정의된 접촉 순서에 의존하지 않고 창발적 보행을 가능하게 하는 샘플링 기반 모델 예측 제어(MPC) 프레임워크를 제시합니다. 우리의 방법은 높은 수준의 목표 최적화만을 통해 트로팅에서 갤럽에 이르기까지 다양한 운동 패턴, 강건한 서기 정책, 점프, 물구나무서기 균형을 발견합니다. 모델 예측 경로 적분(MPPI)을 기반으로, 위치 및 속도 제어점에서 작동하는 3차 에르미트 스플라인 매개변수화를 제안합니다. 우리의 접근 방식은 작업 요구 사항에 자동으로 적응하는 접촉 생성 및 접촉 해제 전략을 가능하게 하며, 제한된 수의 샘플링된 궤적만 필요로 합니다. 이러한 샘플 효율성은 일반 CPU 하드웨어에서 실시간 제어를 가능하게 하여, 다른 최신 MPPI 방법에서 일반적으로 요구되는 GPU 가속을 제거합니다. 우리는 Go2 사족 보행 로봇에서 접근 방식을 검증하여 다양한 창발적 보행과 기본 점프 능력을 입증합니다. 시뮬레이션에서는 참조 추적이나 오프라인 사전 훈련 없이 백플립, 동적 물구나무서기 균형, 휴머노이드 보행과 같은 더 복잡한 행동을 추가로 보여줍니다.
