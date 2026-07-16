---
$id: ent_paper_full_order_sampling_based_mpc_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing
  zh: Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing
  ko: Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing
summary:
  en: Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing is a 2024 work on loco-manipulation
    and whole-body-control for humanoid robots.
  zh: Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing is a 2024 work on loco-manipulation
    and whole-body-control for humanoid robots.
  ko: Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing is a 2024 work on loco-manipulation
    and whole-body-control for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- full_order_sampling_based_mpc
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.15610v1.
sources:
- id: src_001
  type: paper
  title: Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing (arXiv)
  url: https://arxiv.org/abs/2409.15610
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Due to high dimensionality and non-convexity, real-time optimal control using full-order dynamics models for legged robots is challenging. Therefore, Nonlinear Model Predictive Control (NMPC) approaches are often limited to reduced-order models. Sampling-based MPC has shown potential in nonconvex even discontinuous problems, but often yields suboptimal solutions with high variance, which limits its applications in high-dimensional locomotion. This work introduces DIAL-MPC (Diffusion-Inspired Annealing for Legged MPC), a sampling-based MPC framework with a novel diffusion-style annealing process. Such an annealing process is supported by the theoretical landscape analysis of Model Predictive Path Integral Control (MPPI) and the connection between MPPI and single-step diffusion. Algorithmically, DIAL-MPC iteratively refines solutions online and achieves both global coverage and local convergence. In quadrupedal torque-level control tasks, DIAL-MPC reduces the tracking error of standard MPPI by $13.4$ times and outperforms reinforcement learning (RL) policies by $50\%$ in challenging climbing tasks without any training. In particular, DIAL-MPC enables precise real-world quadrupedal jumping with payload. To the best of our knowledge, DIAL-MPC is the first training-free method that optimizes over full-order quadruped dynamics in real-time.

## 核心内容
Due to high dimensionality and non-convexity, real-time optimal control using full-order dynamics models for legged robots is challenging. Therefore, Nonlinear Model Predictive Control (NMPC) approaches are often limited to reduced-order models. Sampling-based MPC has shown potential in nonconvex even discontinuous problems, but often yields suboptimal solutions with high variance, which limits its applications in high-dimensional locomotion. This work introduces DIAL-MPC (Diffusion-Inspired Annealing for Legged MPC), a sampling-based MPC framework with a novel diffusion-style annealing process. Such an annealing process is supported by the theoretical landscape analysis of Model Predictive Path Integral Control (MPPI) and the connection between MPPI and single-step diffusion. Algorithmically, DIAL-MPC iteratively refines solutions online and achieves both global coverage and local convergence. In quadrupedal torque-level control tasks, DIAL-MPC reduces the tracking error of standard MPPI by $13.4$ times and outperforms reinforcement learning (RL) policies by $50\%$ in challenging climbing tasks without any training. In particular, DIAL-MPC enables precise real-world quadrupedal jumping with payload. To the best of our knowledge, DIAL-MPC is the first training-free method that optimizes over full-order quadruped dynamics in real-time.

## 参考
- http://arxiv.org/abs/2409.15610v1

## Overview
Due to high dimensionality and non-convexity, real-time optimal control using full-order dynamics models for legged robots is challenging. Therefore, Nonlinear Model Predictive Control (NMPC) approaches are often limited to reduced-order models. Sampling-based MPC has shown potential in nonconvex even discontinuous problems, but often yields suboptimal solutions with high variance, which limits its applications in high-dimensional locomotion. This work introduces DIAL-MPC (Diffusion-Inspired Annealing for Legged MPC), a sampling-based MPC framework with a novel diffusion-style annealing process. Such an annealing process is supported by the theoretical landscape analysis of Model Predictive Path Integral Control (MPPI) and the connection between MPPI and single-step diffusion. Algorithmically, DIAL-MPC iteratively refines solutions online and achieves both global coverage and local convergence. In quadrupedal torque-level control tasks, DIAL-MPC reduces the tracking error of standard MPPI by $13.4$ times and outperforms reinforcement learning (RL) policies by $50\%$ in challenging climbing tasks without any training. In particular, DIAL-MPC enables precise real-world quadrupedal jumping with payload. To the best of our knowledge, DIAL-MPC is the first training-free method that optimizes over full-order quadruped dynamics in real-time.

## Content
Due to high dimensionality and non-convexity, real-time optimal control using full-order dynamics models for legged robots is challenging. Therefore, Nonlinear Model Predictive Control (NMPC) approaches are often limited to reduced-order models. Sampling-based MPC has shown potential in nonconvex even discontinuous problems, but often yields suboptimal solutions with high variance, which limits its applications in high-dimensional locomotion. This work introduces DIAL-MPC (Diffusion-Inspired Annealing for Legged MPC), a sampling-based MPC framework with a novel diffusion-style annealing process. Such an annealing process is supported by the theoretical landscape analysis of Model Predictive Path Integral Control (MPPI) and the connection between MPPI and single-step diffusion. Algorithmically, DIAL-MPC iteratively refines solutions online and achieves both global coverage and local convergence. In quadrupedal torque-level control tasks, DIAL-MPC reduces the tracking error of standard MPPI by $13.4$ times and outperforms reinforcement learning (RL) policies by $50\%$ in challenging climbing tasks without any training. In particular, DIAL-MPC enables precise real-world quadrupedal jumping with payload. To the best of our knowledge, DIAL-MPC is the first training-free method that optimizes over full-order quadruped dynamics in real-time.

## 개요
고차원성과 비볼록성으로 인해, 보행 로봇의 전차수 동역학 모델을 사용한 실시간 최적 제어는 어렵습니다. 따라서 비선형 모델 예측 제어(NMPC) 접근법은 종종 축소 차수 모델로 제한됩니다. 샘플링 기반 MPC는 비볼록, 심지어 불연속적인 문제에서 잠재력을 보여주었지만, 높은 분산을 가진 차선의 해를 산출하는 경우가 많아 고차원 보행에서의 응용이 제한됩니다. 본 연구는 DIAL-MPC(Diffusion-Inspired Annealing for Legged MPC)를 소개합니다. 이는 새로운 확산 스타일 어닐링 과정을 갖춘 샘플링 기반 MPC 프레임워크입니다. 이러한 어닐링 과정은 모델 예측 경로 적분 제어(MPPI)의 이론적 지형 분석과 MPPI와 단일 단계 확산 간의 연결에 의해 뒷받침됩니다. 알고리즘적으로, DIAL-MPC는 온라인에서 반복적으로 해를 개선하며 전역적 탐색과 지역적 수렴을 모두 달성합니다. 사족 보행 로봇의 토크 수준 제어 작업에서 DIAL-MPC는 표준 MPPI의 추적 오차를 $13.4$배 줄이고, 훈련 없이도 어려운 등반 작업에서 강화 학습(RL) 정책보다 $50\%$ 더 나은 성능을 보입니다. 특히, DIAL-MPC는 페이로드를 실은 정밀한 실제 사족 보행 로봇 점프를 가능하게 합니다. 우리가 아는 한, DIAL-MPC는 실시간으로 전차수 사족 보행 동역학을 최적화하는 최초의 훈련 없는 방법입니다.

## 핵심 내용
고차원성과 비볼록성으로 인해, 보행 로봇의 전차수 동역학 모델을 사용한 실시간 최적 제어는 어렵습니다. 따라서 비선형 모델 예측 제어(NMPC) 접근법은 종종 축소 차수 모델로 제한됩니다. 샘플링 기반 MPC는 비볼록, 심지어 불연속적인 문제에서 잠재력을 보여주었지만, 높은 분산을 가진 차선의 해를 산출하는 경우가 많아 고차원 보행에서의 응용이 제한됩니다. 본 연구는 DIAL-MPC(Diffusion-Inspired Annealing for Legged MPC)를 소개합니다. 이는 새로운 확산 스타일 어닐링 과정을 갖춘 샘플링 기반 MPC 프레임워크입니다. 이러한 어닐링 과정은 모델 예측 경로 적분 제어(MPPI)의 이론적 지형 분석과 MPPI와 단일 단계 확산 간의 연결에 의해 뒷받침됩니다. 알고리즘적으로, DIAL-MPC는 온라인에서 반복적으로 해를 개선하며 전역적 탐색과 지역적 수렴을 모두 달성합니다. 사족 보행 로봇의 토크 수준 제어 작업에서 DIAL-MPC는 표준 MPPI의 추적 오차를 $13.4$배 줄이고, 훈련 없이도 어려운 등반 작업에서 강화 학습(RL) 정책보다 $50\%$ 더 나은 성능을 보입니다. 특히, DIAL-MPC는 페이로드를 실은 정밀한 실제 사족 보행 로봇 점프를 가능하게 합니다. 우리가 아는 한, DIAL-MPC는 실시간으로 전차수 사족 보행 동역학을 최적화하는 최초의 훈련 없는 방법입니다.
