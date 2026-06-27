---
$id: ent_paper_aldana_lopez_designing_controllers_with_pre_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Designing controllers with predefined convergence-time bound using bounded time-varying
    gains
  zh: 利用有界时变增益设计具有预设收敛时间界的控制器
  ko: 유계 시변 이득을 사용하여 사전 정의된 수렴 시간 한계를 갖는 제어기 설계
summary:
  en: This chapter proposes a redesign methodology to construct robust predefined-time
    controllers for perturbed chains of integrators using uniformly bounded time-varying
    gains, and analyzes conditions for uniform Lyapunov stability.
  zh: 本章提出了一种重设计方法，利用一致有界的时变增益为受扰动积分器链构建鲁棒的预设时间控制器，并分析了一致李雅普诺夫稳定性条件。
  ko: 본 장에서는 일정하게 유계인 시변 이득을 사용하여 외란이 있는 적분기 체인을 위한 강인한 사전 정의 시간 제어기를 구성하는 재설계 방법론을
    제안하고, 균일 리아푸노프 안정성 조건을 분석한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the provided metadata and abstract; full-text section-level
    citations were not independently verified. Requires human review before promotion
    to verified.
sources:
- id: src_001
  type: paper
  title: Designing controllers with predefined convergence-time bound using bounded
    time-varying gains
  url: https://arxiv.org/abs/2311.02473
  date: '2023'
  accessed_at: '2026-06-27'
  doi: 10.1007/978-3-031-37089-2_3
theoretical_depth:
- method
---

## Overview

Aldana-López, Seeber, Haimovich, and Gómez-Gutiérrez (2023) address a practical limitation of prescribed-time control: controllers that guarantee exact convergence at a user-specified terminal time typically rely on time-varying gains that diverge to infinity as the terminal time approaches. Such unbounded gains are problematic in real-world systems subject to quantization, measurement noise, and actuator saturation. To overcome this, the authors introduce a broader class of predefined-time controllers whose gains remain uniformly bounded while still ensuring a prescribed convergence-time bound.

The proposed methodology redesigns an auxiliary finite-time or fixed-time controller by applying a time-varying coordinate change together with a time-scale transformation. This yields controllers for perturbed chains of integrators of arbitrary order that converge within a predefined time and maintain bounded time-varying gains. The authors also establish necessary and sufficient conditions for uniform Lyapunov stability of the resulting closed-loop system and show that autonomous fixed-time controllers can be recovered as a limiting case.

The framework includes tunable parameters (denoted α, β, and ρ) that allow reduction of energy consumption and control magnitude. A hybrid controller structure is used: the bounded predefined-time controller drives the state to the origin before the predefined time, after which a robust controller keeps the state at the origin.

## Key Contributions

- A predefined-time control design that keeps the time-varying gain uniformly bounded.
- A general redesign framework using time-scale transformations and time-varying coordinate changes for arbitrary-order chain-of-integrator systems.
- Energy and control-magnitude reduction through tunable parameters α, β, and ρ.
- Necessary and sufficient conditions for uniform Lyapunov stability of the proposed controllers.
- Recovery of existing autonomous fixed-time controllers as a limiting special case.

## Relevance to Humanoid Robotics

Although the theoretical results are developed for generic perturbed chain-of-integrator plants, the bounded predefined-time stabilizers and uniform stability guarantees are directly relevant to humanoid robot joint servo control. Humanoid joints require predictable settling behavior, rejection of unknown disturbances, and bounded control gains to ensure safe, repeatable motion during mass production and deployment.

Because the controllers avoid gain singularity at the terminal time, they are better suited than classical prescribed-time controllers for implementations with digital encoders, force sensors, and noisy measurements—common in humanoid hardware. The method can therefore serve as a foundational control layer for position, velocity, or torque loops in humanoid actuators, even though the paper does not present explicit humanoid experiments or multi-body dynamics.
