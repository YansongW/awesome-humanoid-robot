---
$id: ent_paper_wang_adaptive_control_of_robot_mani_2014
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics
  zh: 具有不确定运动学和动力学的机器人机械臂自适应控制
  ko: 불확실한 기구학과 동역학을 가진 로봇 매니퓰레이터의 적응 제어
summary:
  en: This paper proposes two adaptive control schemes that achieve task-space trajectory
    tracking for robot manipulators when both kinematic and dynamic parameters are
    uncertain, using inverse-Jacobian feedback with separated adaptation loops.
  zh: 本文提出了两种自适应控制方案，在机器人机械臂的运动学和动力学参数均不确定的情况下，利用逆雅可比反馈和分离的自适应环实现任务空间轨迹跟踪。
  ko: 본 논문은 운동학적 및 동역학적 매개변수가 모두 불확실한 로봇 매니퓰레이터의 작업 공간 궤적 추적을 분리된 적응 루프와 역-야코비안 피드백을
    사용하여 달성하는 두 가지 적응 제어 기법을 제안한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 05_mass_production
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- adaptive_control
- task_space_tracking
- uncertain_kinematics
- uncertain_dynamics
- robot_manipulator
- inverse_jacobian_feedback
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full-text verification
    is needed before promotion to verified.
sources:
- id: src_001
  type: paper
  title: Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics
  url: https://arxiv.org/abs/1403.5204
  date: '2014'
  accessed_at: '2026-06-26'
---

## Overview

This paper addresses the problem of task-space trajectory tracking for robot manipulators when both kinematic and dynamic parameters are uncertain. Existing adaptive controllers often assume exact kinematic knowledge and focus only on dynamic uncertainty, which limits their applicability to real robots whose kinematic parameters may be poorly calibrated. The authors propose two adaptive control schemes that combine inverse-Jacobian feedback with separated kinematic and dynamic adaptation loops, enabling the controller to compensate for both sources of uncertainty simultaneously.

The first controller is designed for all-revolute manipulators and uses an inertia-matrix-dependent gain selection rule to avoid overly conservative gains. The second controller relaxes the revolute-joint restriction so it can also handle prismatic joints. Both schemes replace approximate transpose-Jacobian feedback with inverse-Jacobian feedback, which is argued to improve task-space tracking performance. The authors further show that, with suitable modifications, the first controller can provide certainty-equivalence performance guarantees, including an exponential convergence rate.

Validation is performed through numerical simulations on a 2-DOF planar manipulator. The simulations demonstrate improved tracking accuracy and torque utilization compared with the baseline transpose-Jacobian approach, supporting the practical value of the proposed methods for manipulator control under model uncertainty.

## Key Contributions

- Proposes two adaptive controllers that realize separation between kinematic and dynamic control loops under uncertain kinematics and dynamics.
- Replaces approximate transpose-Jacobian feedback with inverse-Jacobian feedback to improve task-space tracking performance.
- Extends inertia-matrix-dependent gain adaptation to the case with both kinematic and dynamic uncertainties, avoiding conservative gain choice.
- Provides certainty-equivalence performance guarantees, including exponential convergence rate, for the first controller.
- Validates through numerical simulations on a 2-DOF planar manipulator, showing improved tracking accuracy and torque usage.

## Relevance to Humanoid Robotics

Humanoid robots rely heavily on accurate limb and manipulator motion control in task-space, yet their kinematic and dynamic parameters are often uncertain due to manufacturing tolerances, payload variation, and wear. The adaptive framework presented in this paper offers a principled way to maintain tracking performance without requiring exact model knowledge, which is important for reliable operation at scale. By separating kinematic and dynamic adaptation and using inverse-Jacobian feedback, the approach is directly applicable to humanoid arm control and similar articulated limbs.

Although the paper does not study full humanoid bodies or mass-production lines explicitly, its focus on robust, low-gain adaptive control aligns with the needs of scalable humanoid manufacturing and deployment. The simulation-based validation on a 2-DOF planar manipulator provides an initial proof of concept, but physical experiments on humanoid hardware would be needed to confirm its practical impact.
