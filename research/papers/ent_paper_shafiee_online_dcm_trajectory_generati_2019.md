---
$id: ent_paper_shafiee_online_dcm_trajectory_generati_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Online DCM Trajectory Generation for Push Recovery of Torque-Controlled Humanoid
    Robots
  zh: 扭矩控制人形机器人_push_recovery_的在线_DCM_轨迹生成
  ko: 토크 제어 휴머노이드 로봇의 푸시 복구를 위한 온라인 DCM 궤적 생성
summary:
  en: This paper presents an online step adapter for push recovery in bipedal walking
    that modifies the next footstep position and timing by enforcing initial and final
    DCM boundary values through exponential ZMP interpolation, validated on the torque-controlled
    iCub humanoid in simulation.
  zh: 本文提出了一种用于双足行走推搡恢复的在线步态适配器，通过指数_ZMP_插值强制_DCM_边界值来修改下一步足位和时长，并在仿真中于扭矩控制的_iCub_人形机器人上进行了验证。
  ko: 본 논문은 지수적 ZMP 보간을 통해 초기 및 최종 DCM 경계값을 강제함으로써 다음 보폭 위치와 타이밍을 수정하는 이족 보행 푸시 복구를
    위한 온라인 스텝 어댑터를 제안하고, 토크 제어 iCub 휴머노이드 로봇 시뮬레이션에서 검증하였다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- push_recovery
- dcm_trajectory
- bipedal_locomotion
- torque_control
- online_qp
- zmp_interpolation
- icub
- humanoid_walking
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from metadata and abstract; requires human review against full
    text before verification.
sources:
- id: src_001
  type: paper
  title: Online DCM Trajectory Generation for Push Recovery of Torque-Controlled Humanoid
    Robots
  url: https://arxiv.org/abs/1909.10403
  date: '2019'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

The paper proposes a computationally efficient online method for planning bipedal walking trajectories with push recovery. It targets control architectures in which Divergent-Component-of-Motion (DCM) trajectories are planned in advance, and adds a step adapter that adjusts planned trajectories to recover from unexpected external pushes. The step adapter operates only during single support phases and computes new positions and timings for the next footstep.

The core technical idea is to impose both initial and final DCM boundary values for a step by using an exponential interpolation of the time-varying Zero-Moment Point (ZMP) trajectory. This formulation converts the push recovery problem into a Quadratic Programming (QP) problem that can be solved online with state-of-the-art optimizers. The step adapter is embedded within a three-layer torque-control walking architecture that also accounts for double support phases, even though adaptation is only active in single support.

## Key Contributions

- An online step adapter that modifies both the position and the timing of the next footstep during single support for push recovery.
- An exponential ZMP interpolation technique that enables enforcement of initial and final DCM boundary values and leads to a QP formulation.
- Integration of the step adapter into an existing DCM-based torque-control walking architecture.
- Simulation validation on the 33 kg iCub humanoid robot walking at 0.28 m/s and resisting external pushes of up to 150 N applied for 0.05 s.

## Relevance to Humanoid Robotics

The work directly improves the robustness of real-time bipedal locomotion for torque-controlled humanoid robots, a capability that is essential for reliable deployment in unstructured environments. By enabling online recovery from external pushes, the method addresses a key challenge in making humanoid robots physically robust during dynamic walking. Its reliance on efficient QP optimization also makes it suitable for online implementation on resource-constrained humanoid hardware.
