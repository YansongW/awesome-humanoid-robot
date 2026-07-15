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
  zh: 'Recently, there has been a great deal of attention in a class of controllers based on time-varying gains, called prescribed-time
    controllers, that steer the system''s state to the origin in the desired time, a priori set by the user, regardless of
    the initial condition. Furthermore, such a class of controllers has been shown to maintain a prescribed-time convergence
    in the presence of disturbances even if the disturbance bound is unknown. However, such properties require a time-varying
    gain that becomes singular at the terminal time, which limits its application to scenarios under quantization '
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2311.02473v1.
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
Recently, there has been a great deal of attention in a class of controllers based on time-varying gains, called prescribed-time controllers, that steer the system's state to the origin in the desired time, a priori set by the user, regardless of the initial condition. Furthermore, such a class of controllers has been shown to maintain a prescribed-time convergence in the presence of disturbances even if the disturbance bound is unknown. However, such properties require a time-varying gain that becomes singular at the terminal time, which limits its application to scenarios under quantization or measurement noise. This chapter presents a methodology to design a broader class of controllers, called predefined-time controllers, with a prescribed convergence-time bound. Our approach allows designing robust predefined-time controllers based on time-varying gains while maintaining uniformly bounded time-varying gains. We analyze the condition for uniform Lyapunov stability under the proposed time-varying controllers.

## 核心内容
Recently, there has been a great deal of attention in a class of controllers based on time-varying gains, called prescribed-time controllers, that steer the system's state to the origin in the desired time, a priori set by the user, regardless of the initial condition. Furthermore, such a class of controllers has been shown to maintain a prescribed-time convergence in the presence of disturbances even if the disturbance bound is unknown. However, such properties require a time-varying gain that becomes singular at the terminal time, which limits its application to scenarios under quantization or measurement noise. This chapter presents a methodology to design a broader class of controllers, called predefined-time controllers, with a prescribed convergence-time bound. Our approach allows designing robust predefined-time controllers based on time-varying gains while maintaining uniformly bounded time-varying gains. We analyze the condition for uniform Lyapunov stability under the proposed time-varying controllers.

## 参考
- http://arxiv.org/abs/2311.02473v1


