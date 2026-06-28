---
$id: ent_paper_wise_a_certifiably_correct_algorith_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Certifiably Correct Algorithm for Generalized Robot-World and Hand-Eye Calibration
  zh: 广义机器人-世界与手眼校准的可认证正确算法
  ko: 일반화된 로봇-월드 및 핸드-아이 보정을 위한 인증 가능한 정확한 알고리즘
summary:
  en: Presents a fast, certifiably globally optimal algorithm for generalized robot-world
    and hand-eye calibration that jointly estimates multiple sensor and target poses,
    including scale-free monocular cameras, via a tight semidefinite programming relaxation
    of a maximum-likelihood QCQP over SE(3).
  zh: 提出一种快速且可证明全局最优的广义机器人-世界与手眼校准算法，通过对 SE(3) 上最大似然 QCQP 的紧半定规划松弛，联合估计多个传感器与目标位姿，包括无尺度单目相机。
  ko: SE(3) 상 최대우도 QCQP에 대한 긴밀한 SDP 완화를 통해 여러 센서와 대상 자세를 공동으로 추정하고 스케일-프리 단안 카메라를
    포함하는 일반화된 로봇-월드 및 핸드-아이 보정을 위한 빠르고 인증 가능한 전역 최적 알고리즘을 제시한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 04_assembly_integration_testing
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- extrinsic_calibration
- hand_eye_calibration
- robot_world_calibration
- semidefinite_programming
- qcqp
- global_optimality
- certifiable_perception
- monocular_camera
- multi_sensor_fusion
- se3_estimation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; requires human review of
    the full paper before verification.; approved by autonomous review workflow.
sources:
- id: src_001
  type: paper
  title: A Certifiably Correct Algorithm for Generalized Robot-World and Hand-Eye
    Calibration
  url: https://arxiv.org/abs/2507.23045
  date: '2026'
  accessed_at: '2026-06-28'
  doi: 10.1177/ToBeAssigned
theoretical_depth:
- method
---

## Overview

This paper addresses automatic extrinsic calibration for multi-sensor robotic platforms by introducing a certifiably globally optimal algorithm for generalized robot-world and hand-eye calibration (RWHEC). The formulation supports simultaneous estimation of multiple sensor and target poses and allows the use of monocular cameras that cannot directly observe metric scale. The authors reduce the maximum-likelihood QCQP over SE(3) to a rotation-only quadratic program and solve it with a tight semidefinite programming relaxation, providing a priori global-optimality guarantees under bounded measurement errors.

In addition to the algorithm, the paper derives novel identifiability criteria and proposes a new constraint qualification for nonlinear programs with redundant constraints. This qualification is presented as independently useful for proving exactness of SDP relaxations of QCQPs tightened by redundant constraints. The method is validated through extensive simulated and real experiments, and an open-source implementation is released.

## Key Contributions

- First certifiably globally optimal solver for multi-sensor extrinsic calibration.
- Novel identifiability criteria and a priori global-optimality guarantees for generalized RWHEC.
- Extension to scale-free (monocular) sensors and arbitrary multi-sensor/target configurations.
- New constraint qualification for redundant constraints supporting exact SDP relaxation of QCQPs.
- Free and open-source implementation with extensive simulated and real-world validation.

## Relevance to Humanoid Robotics

Accurate extrinsic calibration of cameras, IMUs, and kinematic frames is a foundational requirement for humanoid robots to fuse perception reliably during manipulation, locomotion, and deployment. The paper's certifiable global optimality and reduced reliance on expert tuning are especially relevant for mass production and field maintenance of humanoids, where repeatable calibration across many units is critical. Its support for scale-free monocular cameras also aligns with the multi-camera head and hand-eye configurations common in humanoid platforms.
