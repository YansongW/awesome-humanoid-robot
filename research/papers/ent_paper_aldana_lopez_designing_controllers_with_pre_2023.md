---
$id: ent_paper_aldana_lopez_designing_controllers_with_pre_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Designing controllers with predefined convergence-time bound using bounded time-varying gains
  zh: 利用有界时变增益设计具有预设收敛时间界的控制器
  ko: 유계 시변 이득을 사용하여 사전 정의된 수렴 시간 한계를 갖는 제어기 설계
summary:
  en: This chapter proposes a redesign methodology to construct robust predefined-time controllers for perturbed chains of
    integrators using uniformly bounded time-varying gains, and analyzes conditions for uniform Lyapunov stability.
  zh: 本文提出一种基于一致有界时变增益的重新设计方法，用于构建受扰积分器链的鲁棒预定义时间控制器。该方法通过保持增益一致有界，克服了传统预设时间控制器在终端时刻出现奇异性的局限，并分析了系统的一致Lyapunov稳定性条件。
  ko: 본 장에서는 일정하게 유계인 시변 이득을 사용하여 외란이 있는 적분기 체인을 위한 강인한 사전 정의 시간 제어기를 구성하는 재설계 방법론을 제안하고, 균일 리아푸노프 안정성 조건을 분석한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 08_software_middleware
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- predefined_time_control
- prescribed_time_control
- bounded_time_varying_gains
- robust_control
- chain_of_integrators
- uniform_lyapunov_stability
- joint_servo_control
- convergence_time_bound
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2311.02473v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (694 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Designing controllers with predefined convergence-time bound using bounded time-varying gains
  url: https://arxiv.org/abs/2311.02473
  date: '2023'
  accessed_at: '2026-06-27'
  doi: 10.1007/978-3-031-37089-2_3
theoretical_depth:
- method
---
## 概述
现有预设时间控制器虽能在未知扰动下实现指定时间收敛，但其时变增益在终端时刻会趋于无穷大，导致在量化或测量噪声场景中应用受限。本文提出一类更广义的预定义时间控制器设计方法，通过采用一致有界时变增益，在保持预设收敛时间界的同时避免增益奇异性。研究重点分析了所提时变控制器下系统的一致Lyapunov稳定性条件，为鲁棒控制提供了新思路。

## 核心内容
### 核心问题
- 传统预设时间控制器（prescribed-time controllers）依赖在终端时刻趋于无穷的时变增益，这限制了其在量化噪声或测量噪声环境中的应用。
- 现有方法虽能保证扰动下预设时间收敛，但增益奇异性成为实际部署的关键障碍。

### 方法创新
- 提出**预定义时间控制器**（predefined-time controllers）的重新设计框架，核心在于使用**一致有界时变增益**（uniformly bounded time-varying gains）。
- 新方法允许用户预先设定收敛时间上界，且增益在整个控制过程中保持有界，避免终端奇异性。

### 理论分析
- 针对受扰积分器链（perturbed chains of integrators），推导了系统在时变控制器作用下实现**一致Lyapunov稳定性**（uniform Lyapunov stability）的充分条件。
- 稳定性分析不依赖于扰动上界的先验知识，增强了鲁棒性。

### 关键结论
- 所提控制器在保持预设收敛时间界的同时，消除了传统方法对增益奇异性的依赖，拓展了在含噪声或量化约束场景中的适用性。

## Overview
Recently, there has been a great deal of attention in a class of controllers based on time-varying gains, called prescribed-time controllers, that steer the system's state to the origin in the desired time, a priori set by the user, regardless of the initial condition. Furthermore, such a class of controllers has been shown to maintain a prescribed-time convergence in the presence of disturbances even if the disturbance bound is unknown. However, such properties require a time-varying gain that becomes singular at the terminal time, which limits its application to scenarios under quantization or measurement noise. This chapter presents a methodology to design a broader class of controllers, called predefined-time controllers, with a prescribed convergence-time bound. Our approach allows designing robust predefined-time controllers based on time-varying gains while maintaining uniformly bounded time-varying gains. We analyze the condition for uniform Lyapunov stability under the proposed time-varying controllers.

## 参考
- http://arxiv.org/abs/2311.02473v1

## 개요
기존의 사전 설정 시간 제어기는 미지의 외란 하에서도 지정된 시간 내 수렴을 보장할 수 있지만, 시간에 따라 변하는 이득이 종료 시점에서 무한대로 발산하여 양자화 또는 측정 잡음 환경에서 적용이 제한됩니다. 본 논문은 일관되게 유계인 시변 이득을 사용하여 사전 설정 수렴 시간 경계를 유지하면서 이득 특이성을 피하는, 더 일반화된 사전 정의 시간 제어기 설계 방법을 제안합니다. 연구는 제안된 시변 제어기 하에서 시스템의 일관된 Lyapunov 안정성 조건을 분석하는 데 중점을 두며, 강건 제어에 새로운 통찰을 제공합니다.

## 핵심 내용
### 핵심 문제
- 기존의 사전 설정 시간 제어기(prescribed-time controllers)는 종료 시점에서 무한대로 발산하는 시변 이득에 의존하여, 양자화 잡음 또는 측정 잡음 환경에서의 적용이 제한됩니다.
- 기존 방법은 외란 하에서도 사전 설정 시간 수렴을 보장할 수 있지만, 이득 특이성이 실제 배포의 핵심 장애물이 됩니다.

### 방법 혁신
- **사전 정의 시간 제어기**(predefined-time controllers)의 재설계 프레임워크를 제안하며, 핵심은 **일관되게 유계인 시변 이득**(uniformly bounded time-varying gains)을 사용하는 것입니다.
- 새로운 방법은 사용자가 수렴 시간 상한을 사전에 설정할 수 있게 하며, 이득은 전체 제어 과정에서 유계를 유지하여 종료 특이성을 피합니다.

### 이론 분석
- 외란을 받는 적분기 체인(perturbed chains of integrators)에 대해, 시변 제어기 하에서 시스템이 **일관된 Lyapunov 안정성**(uniform Lyapunov stability)을 달성하기 위한 충분 조건을 도출합니다.
- 안정성 분석은 외란 상한에 대한 사전 지식에 의존하지 않아 강건성을 향상시킵니다.

### 핵심 결론
- 제안된 제어기는 사전 설정 수렴 시간 경계를 유지하면서 기존 방법의 이득 특이성 의존성을 제거하여, 잡음 또는 양자화 제약이 있는 시나리오에서의 적용 가능성을 확장합니다.
