---
$id: ent_paper_benzi_energy_tank_based_control_fram_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Energy Tank-based Control Framework for Satisfying the ISO/TS 15066 Constraint
  zh: 满足 ISO/TS 15066 约束的能量罐控制框架
  ko: ISO/TS 15066 제약을 만족시키는 에너지 탱크 기반 제어 프레임워크
summary:
  en: This paper proposes an energy tank-based, passivity-based control framework
    that directly enforces the energetic bounds defined by ISO/TS 15066 for collaborative
    robots, avoiding conservative velocity limits while preserving stability during
    free motion and human contact. The approach was validated in simulation on a KUKA
    LWR 4+ 7-DOF force-controlled manipulator.
  zh: 该论文提出了一种基于能量罐的被动控制框架，可直接执行 ISO/TS 15066 为协作机器人规定的能量边界，避免保守速度限制，同时在自由运动和人体接触期间保持稳定。该方法在
    KUKA LWR 4+ 七自由度力控机械臂的仿真中进行了验证。
  ko: 본 논문은 협업 로봇을 위해 ISO/TS 15066에서 정의한 에너지 경계를 직접 적용하는 에너지 탱크 기반 수동성 기반 제어 프레임워크를
    제안하여 보수적인 속도 제한을 피하면서 자유 운동 및 인간 접촉 시 안정성을 유지합니다. 이 접근법은 KUKA LWR 4+ 7자유도 힘 제어
    매니퓰레이터 시뮬레이션에서 검증되었습니다.
domains:
- 07_ai_models_algorithms
- 12_policy_regulation_ethics
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- energy_tank_control
- passivity_based_control
- iso_ts_15066
- power_force_limiting
- collaborative_robots
- human_robot_interaction
- safety_constraints
- kinetic_energy_bounds
- force_control
- industrial_humanoids
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; requires human review against
    the full paper before verification.
sources:
- id: src_001
  type: paper
  title: Energy Tank-based Control Framework for Satisfying the ISO/TS 15066 Constraint
  url: https://arxiv.org/abs/2304.14059
  date: '2023'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## Overview

ISO/TS 15066 defines the foundational safety requirements for collaborative human-robot cells, but conventional implementations typically translate its biomechanical injury limits into conservative velocity bounds. These conservative assumptions reduce robot productivity and can lead to under-utilization of collaborative workstations. This paper addresses that limitation by formulating the ISO/TS 15066 requirements as explicit energetic bounds and enforcing them directly through an energy tank-based controller.

The proposed framework is built on passivity theory: an energy tank stores and releases energy while guaranteeing that the robot does not inject more energy into the environment than permitted by the standard. The controller optimizes the control input online so that the desired motion direction is preserved as much as possible without violating the energetic limits. The formulation is model-agnostic, handles both free motion and human contact, and is extended to time-varying bounds corresponding to different human body parts.

Additional mechanisms are introduced to manage external energy injections and extractions, for example by re-routing energy between tanks. The overall architecture therefore replaces conservative velocity limiting with a direct, energy-aware safety layer that is intended to maintain higher performance while still guaranteeing compliance with the standard.

## Key Contributions

- Direct enforcement of ISO/TS 15066 energetic bounds instead of conservative velocity limits.
- Model-agnostic passivity-based framework ensuring stable behavior in free motion and human contact.
- Extension to time-varying energy bounds for different human body parts.
- Handling of external energy injections and extractions via energy re-routing.

## Relevance to Humanoid Robotics

Humanoid robots deployed in industrial collaborative cells must share workspace with humans while satisfying strict safety standards. The energy tank approach described in this paper provides a model-agnostic safety layer that bounds the kinetic energy transmitted during human-robot contact, which is directly applicable to humanoid arms and manipulation systems. By avoiding the conservative motion slowdowns typical of standard ISO/TS 15066 implementations, the method could help humanoids maintain useful task performance without compromising safety.

Because the framework handles both free-space motion and contact, and can adapt its energy bounds to different body regions, it is well suited to the variable-contact scenarios that humanoids encounter when reaching, handing over objects, or operating near operators. The simulation validation on a force-controlled manipulator further suggests that the same passivity-based control ideas could be transferred to humanoid torque-controlled joints.
