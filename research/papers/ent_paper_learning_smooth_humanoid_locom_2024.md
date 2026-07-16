---
$id: ent_paper_learning_smooth_humanoid_locom_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Smooth Humanoid Locomotion through Lipschitz-Constrained Policies
  zh: Learning Smooth Humanoid Locomotion through Lipschitz-Constrained Policies
  ko: Learning Smooth Humanoid Locomotion through Lipschitz-Constrained Policies
summary:
  en: Learning Smooth Humanoid Locomotion through Lipschitz-Constrained Policies is a 2024 work on locomotion for humanoid
    robots, with open-source code available.
  zh: Learning Smooth Humanoid Locomotion through Lipschitz-Constrained Policies is a 2024 work on locomotion for humanoid
    robots, with open-source code available.
  ko: Learning Smooth Humanoid Locomotion through Lipschitz-Constrained Policies is a 2024 work on locomotion for humanoid
    robots, with open-source code available.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_smooth_humanoid_locom
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.11825v3.
sources:
- id: src_001
  type: paper
  title: Learning Smooth Humanoid Locomotion through Lipschitz-Constrained Policies (arXiv)
  url: https://arxiv.org/abs/2410.11825
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Learning Smooth Humanoid Locomotion through Lipschitz-Constrained Policies project page
  url: https://lipschitz-constrained-policy.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning combined with sim-to-real transfer offers a general framework for developing locomotion controllers for legged robots. To facilitate successful deployment in the real world, smoothing techniques, such as low-pass filters and smoothness rewards, are often employed to develop policies with smooth behaviors. However, because these techniques are non-differentiable and usually require tedious tuning of a large set of hyperparameters, they tend to require extensive manual tuning for each robotic platform. To address this challenge and establish a general technique for enforcing smooth behaviors, we propose a simple and effective method that imposes a Lipschitz constraint on a learned policy, which we refer to as Lipschitz-Constrained Policies (LCP). We show that the Lipschitz constraint can be implemented in the form of a gradient penalty, which provides a differentiable objective that can be easily incorporated with automatic differentiation frameworks. We demonstrate that LCP effectively replaces the need for smoothing rewards or low-pass filters and can be easily integrated into training frameworks for many distinct humanoid robots. We extensively evaluate LCP in both simulation and real-world humanoid robots, producing smooth and robust locomotion controllers. All simulation and deployment code, along with complete checkpoints, is available on our project page: https://lipschitz-constrained-policy.github.io.

## 核心内容
Reinforcement learning combined with sim-to-real transfer offers a general framework for developing locomotion controllers for legged robots. To facilitate successful deployment in the real world, smoothing techniques, such as low-pass filters and smoothness rewards, are often employed to develop policies with smooth behaviors. However, because these techniques are non-differentiable and usually require tedious tuning of a large set of hyperparameters, they tend to require extensive manual tuning for each robotic platform. To address this challenge and establish a general technique for enforcing smooth behaviors, we propose a simple and effective method that imposes a Lipschitz constraint on a learned policy, which we refer to as Lipschitz-Constrained Policies (LCP). We show that the Lipschitz constraint can be implemented in the form of a gradient penalty, which provides a differentiable objective that can be easily incorporated with automatic differentiation frameworks. We demonstrate that LCP effectively replaces the need for smoothing rewards or low-pass filters and can be easily integrated into training frameworks for many distinct humanoid robots. We extensively evaluate LCP in both simulation and real-world humanoid robots, producing smooth and robust locomotion controllers. All simulation and deployment code, along with complete checkpoints, is available on our project page: https://lipschitz-constrained-policy.github.io.

## 参考
- http://arxiv.org/abs/2410.11825v3

## Overview
Reinforcement learning combined with sim-to-real transfer offers a general framework for developing locomotion controllers for legged robots. To facilitate successful deployment in the real world, smoothing techniques, such as low-pass filters and smoothness rewards, are often employed to develop policies with smooth behaviors. However, because these techniques are non-differentiable and usually require tedious tuning of a large set of hyperparameters, they tend to require extensive manual tuning for each robotic platform. To address this challenge and establish a general technique for enforcing smooth behaviors, we propose a simple and effective method that imposes a Lipschitz constraint on a learned policy, which we refer to as Lipschitz-Constrained Policies (LCP). We show that the Lipschitz constraint can be implemented in the form of a gradient penalty, which provides a differentiable objective that can be easily incorporated with automatic differentiation frameworks. We demonstrate that LCP effectively replaces the need for smoothing rewards or low-pass filters and can be easily integrated into training frameworks for many distinct humanoid robots. We extensively evaluate LCP in both simulation and real-world humanoid robots, producing smooth and robust locomotion controllers. All simulation and deployment code, along with complete checkpoints, is available on our project page: https://lipschitz-constrained-policy.github.io.

## Content
Reinforcement learning combined with sim-to-real transfer offers a general framework for developing locomotion controllers for legged robots. To facilitate successful deployment in the real world, smoothing techniques, such as low-pass filters and smoothness rewards, are often employed to develop policies with smooth behaviors. However, because these techniques are non-differentiable and usually require tedious tuning of a large set of hyperparameters, they tend to require extensive manual tuning for each robotic platform. To address this challenge and establish a general technique for enforcing smooth behaviors, we propose a simple and effective method that imposes a Lipschitz constraint on a learned policy, which we refer to as Lipschitz-Constrained Policies (LCP). We show that the Lipschitz constraint can be implemented in the form of a gradient penalty, which provides a differentiable objective that can be easily incorporated with automatic differentiation frameworks. We demonstrate that LCP effectively replaces the need for smoothing rewards or low-pass filters and can be easily integrated into training frameworks for many distinct humanoid robots. We extensively evaluate LCP in both simulation and real-world humanoid robots, producing smooth and robust locomotion controllers. All simulation and deployment code, along with complete checkpoints, is available on our project page: https://lipschitz-constrained-policy.github.io.

## 개요
강화 학습과 시뮬레이션-실제 전환(sim-to-real transfer)을 결합하면 보행 로봇을 위한 보행 제어기를 개발하는 일반적인 프레임워크를 제공합니다. 실제 환경에서 성공적으로 배포하기 위해 저역 통과 필터(low-pass filters) 및 평활도 보상(smoothness rewards)과 같은 평활화 기술이 자주 사용되어 부드러운 동작을 가진 정책을 개발합니다. 그러나 이러한 기술은 미분 불가능하고 일반적으로 많은 하이퍼파라미터를 지루하게 조정해야 하므로 각 로봇 플랫폼에 대해 광범위한 수동 조정이 필요합니다. 이 문제를 해결하고 부드러운 동작을 강제하는 일반적인 기술을 확립하기 위해, 우리는 학습된 정책에 립시츠 제약(Lipschitz constraint)을 부과하는 간단하고 효과적인 방법을 제안하며, 이를 립시츠 제약 정책(Lipschitz-Constrained Policies, LCP)이라고 부릅니다. 립시츠 제약이 그래디언트 페널티(gradient penalty) 형태로 구현될 수 있음을 보여주며, 이는 자동 미분 프레임워크에 쉽게 통합될 수 있는 미분 가능한 목적 함수를 제공합니다. LCP가 평활도 보상이나 저역 통과 필터의 필요성을 효과적으로 대체하고, 다양한 인간형 로봇을 위한 훈련 프레임워크에 쉽게 통합될 수 있음을 입증합니다. 우리는 시뮬레이션과 실제 인간형 로봇 모두에서 LCP를 광범위하게 평가하여 부드럽고 강건한 보행 제어기를 생성합니다. 모든 시뮬레이션 및 배포 코드와 완전한 체크포인트는 프로젝트 페이지(https://lipschitz-constrained-policy.github.io)에서 확인할 수 있습니다.

## 핵심 내용
강화 학습과 시뮬레이션-실제 전환(sim-to-real transfer)을 결합하면 보행 로봇을 위한 보행 제어기를 개발하는 일반적인 프레임워크를 제공합니다. 실제 환경에서 성공적으로 배포하기 위해 저역 통과 필터(low-pass filters) 및 평활도 보상(smoothness rewards)과 같은 평활화 기술이 자주 사용되어 부드러운 동작을 가진 정책을 개발합니다. 그러나 이러한 기술은 미분 불가능하고 일반적으로 많은 하이퍼파라미터를 지루하게 조정해야 하므로 각 로봇 플랫폼에 대해 광범위한 수동 조정이 필요합니다. 이 문제를 해결하고 부드러운 동작을 강제하는 일반적인 기술을 확립하기 위해, 우리는 학습된 정책에 립시츠 제약(Lipschitz constraint)을 부과하는 간단하고 효과적인 방법을 제안하며, 이를 립시츠 제약 정책(Lipschitz-Constrained Policies, LCP)이라고 부릅니다. 립시츠 제약이 그래디언트 페널티(gradient penalty) 형태로 구현될 수 있음을 보여주며, 이는 자동 미분 프레임워크에 쉽게 통합될 수 있는 미분 가능한 목적 함수를 제공합니다. LCP가 평활도 보상이나 저역 통과 필터의 필요성을 효과적으로 대체하고, 다양한 인간형 로봇을 위한 훈련 프레임워크에 쉽게 통합될 수 있음을 입증합니다. 우리는 시뮬레이션과 실제 인간형 로봇 모두에서 LCP를 광범위하게 평가하여 부드럽고 강건한 보행 제어기를 생성합니다. 모든 시뮬레이션 및 배포 코드와 완전한 체크포인트는 프로젝트 페이지(https://lipschitz-constrained-policy.github.io)에서 확인할 수 있습니다.
